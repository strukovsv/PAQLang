import logging

import pytest  # noqa

# Погасить INFO сообщения от httpx
logging.getLogger("httpx").setLevel(logging.WARNING)

from paqlang.program import pgm  # noqa


@pytest.fixture()
def arr_ints():
    return {"ints": [x for x in range(0, 4)] + ["error_value"]}


@pytest.fixture()
def arr_strings():
    return {
        "strings": [
            "Один",
            "Два",
            "Три",
            "Четыре",
            "Пять",
            "Шесть",
            "Семь",
            "Восемь",
            "Девять",
            "Десять",
        ]
    }


@pytest.fixture()
def arr_dict_strings():
    return {
        "strings": [
            {"code": elem}
            for elem in [
                "Один",
                "Два",
                "Три",
                "Четыре",
                "Пять",
                "Шесть",
                "Семь",
                "Восемь",
                "Девять",
                "Десять",
            ]
        ]
    }


@pytest.fixture()
def main():
    def __main(text: str = None, js: dict = None, request=None, datas=None):
        # Создать объект управления выполнением задач,
        # загрузив исходный текст программы
        return pgm(
            pgm_code=js or text,
            pgm_libs=None,
            in_classes=[],
            datas=datas,
            request=request,
        )

    return __main
