# Oracle

- [execute](#execute)
- [oracle_execute](#oracle_execute)
- [oracle_fetchall](#oracle_fetchall)
- [oracle_fetchone](#oracle_fetchone)

---

## **execute**

```text

```

[/tests/main/test_execute.py](/tests/main/test_execute.py)

---

## **oracle_execute**

```text
Выполнить SQL запрос. Запросы разбиваются на подзапросы "/" и ";"

oracle_user:str - Подключение к oracle
oracle_password:str
oracle_dsn:str

Входная очередь:
- если не заданы параметры, то список текстов запросов.
- если git_url:str, то список файлов из getlab.
Файл загружается из git и выполняется.
Необходимы также git_token, git_repo, git_branch
- если path:str, то список файлов из директория на диске.
Формат атрибута "...:1...". Вместо :1 подставляется заданный файл.

Результат массив выполенных запросов
{"result": 0 или 1, # 0 - error execute, 1 - succes execute
"output":str, # строки dbms_output потока
"errmsg":str, # ошибка выполнения, если result = 0
"file":str, # путь к файлу, если запрос был загружен из файла или git
}

```

[/tests/main/test_oracle_execute.py](/tests/main/test_oracle_execute.py)

---

## **oracle_fetchall**

```text

```

[/tests/main/test_oracle_fetchall.py](/tests/main/test_oracle_fetchall.py)

---

## **oracle_fetchone**

```text

```

[/tests/main/test_oracle_fetchone.py](/tests/main/test_oracle_fetchone.py)
