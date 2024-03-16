import logging
import pytest  # noqa


# Погасить INFO сообщения от httpx
logging.getLogger("httpx").setLevel(logging.WARNING)

from paqlang.program import pgm  # noqa
from paqlang.utils import get_json  # noqa

from paqlang.ext.github_opers import GithubOpers  # noqa


@pytest.fixture()
def main():
    def __main(text: str = None, js: dict = None, request=None, datas=None):
        if not js:
            js = get_json(text=text)
        # Создать объект управления выполнением задач,
        # загрузив исходный текст программы
        return pgm(
            pgm_code=js,
            pgm_libs=None,
            in_classes=[GithubOpers],
            datas=datas,
            request=request,
        )

    return __main
