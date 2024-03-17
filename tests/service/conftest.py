import logging

import pytest  # noqa

# Погасить INFO сообщения от httpx
logging.getLogger("httpx").setLevel(logging.WARNING)

from paqlang.program import pgm  # noqa

from paqlang.ext.oracle_opers import OracleOpers  # noqa


@pytest.fixture()
def main():

    def __main(text: str = None, js: dict = None, request=None, datas=None):
        # Создать объект управления выполнением задач,
        # загрузив исходный текст программы
        return pgm(
            pgm_code=js or text,
            pgm_libs=None,
            in_classes=[OracleOpers],
            datas=datas,
            request=request,
        )

    return __main
