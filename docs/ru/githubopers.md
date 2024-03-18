# Github (GithubOpers)

- [github_branches: Получить список веток в репозитории](#github_branches)
- [github_commits: Получить список коммитов по ветке](#github_commits)
- [github_diff: Получить список измененых файлов по SHA commit](#github_diff)
- [github_freads: Получить содержимое файлов в репозитории](#github_freads)
- [github_projects: Получить список проектов в репозитории github](#github_projects)
- [github_tags: Получить список тегов в репозитории](#github_tags)
- [github_walk: Получить список файлов в репозитории](#github_walk)

---

## **github_branches**

>
> Получить список веток в репозитории. Входная очередь - не используется. Результат массив веток.
>
> **Parameters**:
>
> - **git_owner**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория
>
> - **search**:str=None - наименование ветки
>
> - **regex**:str=None - regex шаблон отбора веток

[test code: github_branches](/tests/github/test_github_branches.py)

---

## **github_commits**

>
> Получить список коммитов по ветке. Ветка параметр входной очереди.
>
> **Parameters**:
>
> - **git_owner**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория
>
> - **since**:str - Only show results that were last updated after the given time in ISO 8601
>
> - **until**:str - Only commits before this date will be returned in ISO 8601
>
> - **path**:str - только commit для файла

[test code: github_commits](/tests/github/test_github_commits.py)

---

## **github_diff**

>
> Получить список измененых файлов по SHA commit. Входная очередь массив sha или {"id":}. Результат массив обновленных файлов.
>
> **Parameters**:
>
> - **tasks**:int = None - кол-во потоков
>
> - **git_owner**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория

[test code: github_diff](/tests/github/test_github_diff.py)

---

## **github_freads**

>
> Получить содержимое файлов в репозитории. Входная очередь, содержит список файлов, полный маршрут от корня. Результат массив: {"bom": 0, "branch": ветка, "encode": cp1251 - найденная кодировка, "encode_detect": ASCII, "encoding": 1 - файл раскодирован, "path": - полный путь файла, "text": - содержимое файла}
>
> **Parameters**:
>
> - **tasks**:int=None - максимальное кол-во потоков обработки операций
>
> - **git_owner**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория
>
> - **git_branch**:str - ветка
>
> - **path**:str - если задан параметр, то значение :1 заменяется на значение из очереди, для получения имени файла

[test code: github_freads](/tests/github/test_github_freads.py)

---

## **github_projects**

>
> Получить список проектов в репозитории github. Входная очередь - не используется. Результат массив проектов.
>
> **Parameters**:
>
> - **git_owner**:str - Подключение к github
>
> - **git_token**:str
>
> - **regex**:str=None - regex шаблон отбора веток

[test code: github_projects](/tests/github/test_github_projects.py)

---

## **github_tags**

>
> Получить список тегов в репозитории. Входная очередь - не используется.
>
> **Parameters**:
>
> - **git_owner**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория
>
> - **search**:str = None - наименование тега
>
> - **regex**:str = None - regex шаблон отбора тегов

[test code: github_tags](/tests/github/test_github_tags.py)

---

## **github_walk**

>
> Получить список файлов в репозитории. Входная очередь, содержит список корневых узлов, от которых запускается процесс. Результат массив: {"name": имя файла, "path": полный маршрут файла}
>
> **Parameters**:
>
> - **tasks**:int = None - максимальное кол-во потоков обработки операций
>
> - **git_owner**:str - Подключение к github
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория
>
> - **git_branch**:str - ветка
>
> - **regex:str**=None - regex шаблон отбора файлов

[test code: github_walk](/tests/github/test_github_walk.py)
