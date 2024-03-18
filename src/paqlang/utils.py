import logging
import json
import os
import re
import errno
import dataclasses
import datetime
import decimal
from datetime import date, datetime  # noqa
from typing import Any

import aiofiles  # noqa
import yaml  # noqa
import httpx  # noqa

from boto3.session import Session  # noqa

from ruamel.yaml.representer import RoundTripRepresenter  # noqa
from ruamel.yaml import YAML  # noqa

from .aio_gitlab import git_pool as gitlab_pool
from .aio_github import git_pool as github_pool

# Установить текущи логгер
logger = logging.getLogger(__name__)


# Перегрузить сохранение YAML файлов на формирование многострочных значений,
# с использованием "|"
def repr_str(dumper: RoundTripRepresenter, data: str):
    if "\n" in data:
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", data, style="|"
        )
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


# Создать свой объект YAML для сохранения файлов в заданном формате
yamlx = YAML(typ=["rt", "string"])
yamlx.representer.add_representer(str, repr_str)


def get_json_data(text: str) -> dict:
    # Заменить переменные окружения в конфиг файле
    for key, value in os.environ.items():
        text = text.replace("${" + f"{key}" + "}", value)
    # Убрать пробелы вокруг текста
    text = text.strip()
    # Если пустой файл, то вернуть пустой
    if text is None:
        return {}
    elif text[0:1] == "{" or text[0:1] == "}":
        # Распарсит как JSON
        return json.loads(text)
    else:
        # Распарсить yaml текст настроек
        return yamlx.load(text)
        # return yaml.safe_load(text)


def abs_file_path(file_name: str, path: str = None) -> str:
    """Получить абсолютный путь к файлу,
    с учетом относительного пути, запуска пакета"""
    return os.path.join(path or os.getcwd(), file_name)


def freads(file_name: str, encoding: str = None):
    """Обычное чтение файла"""
    with open(
        abs_file_path(file_name),
        mode="r",
        encoding=encoding if encoding else "utf-8",
    ) as f:
        return f.read()


async def aio_reads(file_name: str, encoding: str = None):
    """Асинхронное чтение файла"""
    async with aiofiles.open(
        abs_file_path(file_name),
        mode="r",
        encoding=encoding if encoding else "utf-8",
    ) as f:
        return await f.read()


def get_json(file_name: str = None, text: str = None) -> dict:
    """Загрузить файл конфигурации и заменить переменные окружения

    :param str config_file: путь файлу конфигурации
    :return dict: словарь опций
    """
    return get_json_data(
        text=(freads(file_name=file_name) if file_name else text)
    )


async def aio_get_json(file_name: str = None, text: str = None) -> dict:
    """Загрузить файл конфигурации и заменить переменные окружения

    :param str config_file: путь файлу конфигурации
    :return dict: словарь опций
    """
    return get_json_data(
        text=(await aio_reads(file_name=file_name) if file_name else text)
    )


def setenv(name: str, value: str):
    """Записать параметр окружения

    :param str name: наименование параметра
    :param str value: значение параметра
    """
    os.environ[name] = value


def getenv(name: str, default: str = None) -> str:
    """Получить параметр окружения

    :param str name: имя параметра
    :param str default: значение параметра по умолчанию
    :return str: Вовзращаемое значение
    """
    if name:
        value = os.environ.get(name.upper(), None)
        if value:
            return value.replace("\r", "").replace("\n", "").rstrip()
        else:
            return default
    else:
        return None


def mkdir_path(path):
    """Создать директорий, если не существует
    http://stackoverflow.com/a/600612/190597 (tzot)
    """
    try:
        os.makedirs(path, exist_ok=True)
    except TypeError:
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise


def hide_passwords(value: dict, key: str = None) -> dict:
    """Скрыть пароли и токены в словаре

    :param dict value: исходный словарь
    :param str key: Ключ
    :return dict: преобразованный словарь
    """
    if value is None:
        return None
    elif isinstance(value, dict):
        return {k: hide_passwords(v, k) for k, v in value.items()}
    elif isinstance(value, list):
        return [hide_passwords(elem) for elem in value]
    else:
        if key:
            for key_denied in ["PASS", "TOKEN", "ACCESS_KEY", "PWD"]:
                if key_denied in key.upper():
                    return "<hidden>"
        return value


def my_json_dump(obj: Any, indent: int = None) -> str:
    """Преобразовать в json, сериализировать подчиненные объекты, скрыть пароли

    :param Any obj: исходное значение
    :return str: json как строка
    """

    def default(object_):
        """Функция обработки неизвестных типов"""
        if isinstance(object_, decimal.Decimal):
            return str(object_)
        elif isinstance(object_, date) or isinstance(object_, datetime):
            return object_.isoformat()
        elif dataclasses.is_dataclass(object_):
            return dataclasses.asdict(object_)
        raise TypeError(
            f"Don't know how to serialize to json type {type(object_)}"
        )

    return json.dumps(
        hide_passwords(obj),
        ensure_ascii=False,
        default=default,
        sort_keys=True,
        indent=indent,
    )


def print_dict_json_indent(value: dict) -> str:
    """Преобразовать словарь в строку json, пароли и токены погасить,
    убрать пустые значения"""
    return my_json_dump(obj=value, indent=2)


def print_dict_json(value: dict) -> str:
    """Преобразовать словарь в строку json, пароли и токены погасить,
    убрать пустые значения"""
    return my_json_dump(value)


def print_dict_yaml(value: dict) -> str:
    """Преобразовать словарь в yaml, пароли и токены погасить,
    убрать пустые значения"""
    return yaml.dump(hide_passwords(value), allow_unicode=True)


def start_process_timestamp() -> str:
    """Заполнить переменную окружения, старта процесса

    :return str: timestamp старта процесса
    """
    result = getenv("__START_PROCESS_TIMESTAMP__")
    if result is None:
        result = datetime.now().strftime("%Y%m%d %H%M%S")
        setenv("__START_PROCESS_TIMESTAMP__", result)
    return result


def file_temp_path():
    # Получить директорий сохранения файла
    LOG_PATH = getenv("LOG_PATH")
    # Сформировать timestamp файла
    START_PROCESS_TIMESTAMP = start_process_timestamp()
    if LOG_PATH:
        # Получить путь до файла
        file_path = f"{LOG_PATH}/{START_PROCESS_TIMESTAMP}"
        # Создать директорий, если еще нет
        mkdir_path(file_path)
        return file_path
    else:
        return None


def save_dict(
    value_dict: dict, filename: str, desc: str = None, tp: str = "yaml"
):
    """Сохранить словарь как YAML файл в локальной папке или в S3.
    Зависит от параметров окружения.
    Если значение не выгружено ни туда ни туда,
    то отправим в info лог как json !!!

    :param dict value_dict: сохраняемый словарь
    :param str filename: имя файла
    :param str desc: описание словаря
    :param str tp: Тип сохранения как "json" или "yaml"
    """
    if tp.lower() == "yaml":
        _filename = (
            filename if ".yaml" in filename.lower() else f"{filename}.yaml"
        )
        # Функция преобразования в строку
        dict2str = print_dict_yaml
    elif tp.lower() == "json":
        _filename = (
            filename if ".json" in filename.lower() else f"{filename}.json"
        )
        # Функция преобразования в строку
        dict2str = print_dict_json_indent
    else:
        raise Exception(f'Неизвестный тип преобразования "{tp}" словаря')
    # Получить директорий сохранения файла
    LOG_PATH = getenv("LOG_PATH")
    # Сформировать timestamp файла
    START_PROCESS_TIMESTAMP = start_process_timestamp()
    is_save = False
    if LOG_PATH:
        # Получить путь до файла
        file_path = f"{LOG_PATH}/{START_PROCESS_TIMESTAMP}"
        # Создать директорий, если еще нет
        mkdir_path(file_path)
        # Если задан директорий, то в нем создать yaml файл
        full_path = f"{file_path}/{_filename}"
        open(full_path, "w", encoding="utf-8").write(dict2str(value_dict))
        logger.info(f'save as {tp.lower()} into file: "{full_path}')
        is_save = True
    if getenv("S3_URL", None):
        # Если, заданы параметры хранилища S3
        # Установить сессию с S3
        session = Session(
            aws_access_key_id=getenv("S3_ACCESS_KEY_ID", None),
            aws_secret_access_key=getenv("S3_SECRET_ACCESS_KEY", None),
        )
        s3 = session.resource("s3", endpoint_url=getenv("S3_URL", None))
        # Получить имя корзины
        backet_name = getenv("S3_BUCKET_NAME", None)
        # Сохранить данные
        s3.Bucket(backet_name).put_object(
            Key=f"{START_PROCESS_TIMESTAMP}/{_filename}",
            Body=dict2str(value_dict),
            ContentDisposition=desc or "",
            ContentType="text/x-yaml",
        )
        logger.info(
            f'save as {tp.lower()} into s3: "{backet_name}/{START_PROCESS_TIMESTAMP}/{_filename}"'  # noqa
        )
        is_save = True
    return is_save


def save_object(
    value_dict: dict, filename: str, desc: str = None, log_func=None, tp=None
):
    """Сохранить словарь как YAML файл в локальной папке или в S3.
    Зависит от параметров окружения.
    Если значение не выгружено ни туда ни туда,
    то отправим в info лог как json !!!

    :param dict value_dict: сохраняемый словарь
    :param str filename: имя файла
    :param str desc: описание словаря
    :param log_func: функция логирования, если словарь никуда не сохранен
    """
    if not save_dict(
        value_dict=value_dict,
        filename=filename,
        desc=desc,
        tp=tp or getenv("LOG_TABLE_FORMAT", "yaml"),
    ):
        # Если таблица никуда не выгружена, то отправим в лог !!!
        if log_func:
            # Добавим описание в скобочки
            _desc = f"({desc})" if desc else ""
            log_func(f" {filename}{_desc}: {print_dict_json(value_dict)}")


async def telegram(
    message: str, token: str = None, chats: list = None, success: bool = None
):
    """Отправить сообщение в телеграм

    :param str parse_message: отправляемое сообщение
    :param str token: токен для бота, defaults to None
    :param str chats: массив чатов, defaults to None
    :param bool success: отправить хороший или плохой смайлик
    """
    _token = token or getenv("TELEGRAM_TOKEN")
    if _token:
        for chat_id in chats or [getenv("TELEGRAM_CHAT")]:
            if chat_id:
                emoji = (
                    ("%F0%9F%98%83" if success else "%F0%9F%98%A1")
                    if success is not None
                    else None
                )
                for message in [emoji, message]:
                    if message is not None:
                        async with httpx.AsyncClient() as client:
                            try:
                                telegram_url = f"https://api.telegram.org/bot{_token}/sendMessage"  # noqa
                                telegram_param = {
                                    "chat_id": chat_id,
                                    "text": message,
                                    "parse_mode": "HTML",
                                }
                                response = await client.get(
                                    f"{telegram_url}", params=telegram_param
                                )
                                # Если код возврата, ошибка, то поднять ошибку
                                response.raise_for_status()
                                logger.debug("send message to telegram")
                            except httpx.HTTPError as exc:
                                # Не поднимать ошибку,
                                # если нет доступа к телеграмму
                                logger.error(
                                    f'HTTP Exception for "{exc.request.url}" - "{exc}"'  # noqa
                                )


async def teams(message: str, teams_url: str = None, success: bool = None):
    """Отправить сообщение в teams

    :param str parse_message: сообщение
    :param str teams_url: путь до teams, defaults to None
    :param bool success: показать смайлик, defaults to None
    """
    _teams_url = teams_url or getenv("TEAMS_WEBHOOK")
    if _teams_url:
        logger.debug(f'send message in teams path: "{_teams_url}"')
        body = []
        if success is not None:
            body.append(
                {
                    "horizontalAlignment": "left",
                    "type": "TextBlock",
                    "text": "🙂" if success else "🙁",
                    "size": "extraLarge",
                    "weight": "bolder",
                }
            )

        body.append(
            {
                "type": "FactSet",
                "facts": [{"value": line} for line in message.split("\n")],
            }
        )
        # Сформировать сообщение
        js_message = {
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",  # noqa
                    "version": "1.0",
                    "content": {
                        "type": "AdaptiveCard",
                        "padding": "none",
                        "body": body,
                    },
                }
            ],
        }
        # Отправить сообщение
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(f"{_teams_url}", json=js_message)
                # Если код возврата, ошибка, то поднять ошибку
                response.raise_for_status()
                logger.debug("send message to teams")
            except httpx.HTTPError as exc:
                # Не поднимать ошибку, если нет доступа к teams
                logger.error(
                    f'HTTP Exception for "{exc.request.url}" - "{exc}"'
                )


async def send_message(
    message: str = None, success: int = None, service: str = None
):
    """Отправить сообщение пользователю, в телеграм или teams

    :param str message: сообщение, defaults to None
    :param int success: показать упешный или не успешный смайли,
      defaults to None
    """
    _message = message
    if _message:
        if service:
            _message = "\n".join(
                [f"{service}", "===================================", _message]
            )
        # Отправить сообщение в telegram
        await telegram(message=_message, success=success)
        # Отправить сообщение в teams
        await teams(message=_message, success=success)
        if success is None or success:
            logger.info(_message.replace("\n", " "))
        else:
            logger.error(_message.replace("\n", " "))


def get_attr(attr, elem, is_raise: bool = True):
    if attr:
        if attr and isinstance(elem, dict) and (attr in elem):
            return elem[attr]
        else:
            if is_raise:
                raise Exception(
                    f'Не найден атрибут "{attr}" в элементе "{elem}"'
                )
            else:
                return None
    return elem


def coalesce(plist: list):
    for elem in plist:
        if elem is not None:
            return elem
    return None


def get_condition(test_value, param):
    """Проверить условие

    test_value:float:int:str - проверяемое значение
    param:dict - словарь заданных условий
    return bool - результат проверки
    """
    if isinstance(test_value, (float, int)):
        where = True
        conditions_float = {
            "lt": lambda x, y: x < y,
            "le": lambda x, y: x <= y,
            "eq": lambda x, y: x == y if y is not None else x is None,
            "ne": lambda x, y: x != y if y is not None else x is not None,
            "gt": lambda x, y: x > y,
            "ge": lambda x, y: x >= y,
        }
        for key, function in conditions_float.items():
            if key in param.dict:
                where = where and function(test_value, param.get_float(key))
                logger.debug(
                    f"{key=} {test_value=} {param.get_float(key)=} {where=}"
                )
        return where
    elif isinstance(test_value, str):
        where = True
        conditions_str = {
            "lt": lambda x, y: x < y,
            "le": lambda x, y: x <= y,
            "eq": lambda x, y: x == y if y is not None else x is None,
            "ne": lambda x, y: x != y if y is not None else x is not None,
            "gt": lambda x, y: x > y,
            "ge": lambda x, y: x >= y,
            # Входит строка
            "instr": lambda x, y: x in y,
            # Не входит строка
            "notinstr": lambda x, y: x not in y,
        }
        for key, function in conditions_str.items():
            if key in param.dict:
                where = where and function(test_value, param.get_string(key))
                logger.debug(
                    f"{key=} {test_value=} {param.get_string(key)=} {where=}"
                )
        return where
    return False


async def get_text(file_name, param, is_file: int = 0):
    """Получить содержимое файла с диска, gitlab или github.
    param:dict - содержит атрибуты подключения
    is_file - file_name содержит только имя файла,
    иначе может содержать просто текст"""
    if "path" in param.dict:
        path = param.get_string("path")
        # Если path содержит :1, то сделать подстановку,
        # иначе подставить имя файла как есть
        fname = (
            path.replace(":1", file_name)
            if path and (":1" in path)
            else file_name
        )
    else:
        fname = file_name
    if "git_url" in param.dict:
        # То работаем с gitlab
        gl = await gitlab_pool.get_project(param=param)
    elif "git_owner" in param.dict:
        # То работаем с github
        gl = await github_pool.get_project(param=param)
    else:
        # Работаем с файлом
        gl = None
    if gl:
        # Работаем с gitlab
        try:
            # Прочитать файл из git, передаем имя файла
            file = await gl.get_file(param, fname)
        except Exception as e:
            logger.error(f"get file: {fname} - {e}")
            raise
        # Содержимое файла
        sql = file["text"]
    else:
        # Если задана атрибут path,
        # то прочитать файл с локального диска
        if is_file or "path" in param.dict:
            # Возможность задать кодировку файла
            encoding = param.get_string("encoding") or "utf-8"
            # Прочитать содержимое файла
            sql = await aio_reads(file_name=fname, encoding=encoding)
        else:
            # Запрос из потока, не из файла данных
            fname = None
            # В данном случае пришел текст
            sql = file_name
    return (fname, sql)


async def walk(path, param):
    """Получить рекурсивно список файлов с диска,
    gitlab или github.
    param:dict - содержит атрибуты подключения"""
    if "git_url" in param.dict:
        # То работаем с gitlab
        gl = await gitlab_pool.get_project(param=param)
    elif "git_owner" in param.dict:
        # То работаем с github
        gl = await github_pool.get_project(param=param)
    else:
        # Работаем с файлом
        files = []
        regex = param.get_string("regex")
        logger.info(f'{path=}')
        for root, dirs, walk_files in os.walk(path):
            for file_name in [
                os.path.join(root, name) for name in walk_files
            ]:
                if regex and not re.match(regex, file_name):
                    continue
                files.append({
                    "path": file_name,
                    "name": os.path.basename(file_name)})
        return files
    # Работаем с git
    return await gl.get_tree(param=param, path=path)
