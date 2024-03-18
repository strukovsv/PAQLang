# Gitlab (GitlabOpers)

- [gitlab_branches: Получить список веток в репозитории](#gitlab_branches)
- [gitlab_commits: Получить список коммитов по ветке](#gitlab_commits)
- [gitlab_diff: Получить список измененых файлов по SHA commit](#gitlab_diff)
- [gitlab_freads: Получить содержимое файлов в репозитории](#gitlab_freads)
- [gitlab_projects: Получить список проектов в репозитории](#gitlab_projects)
- [gitlab_tags: Получить список тегов в репозитории](#gitlab_tags)
- [gitlab_walk: Получить список файлов в репозитории](#gitlab_walk)

---

## **gitlab_branches**

>
> Получить список веток в репозитории. Входная очередь - не используется. Результат массив веток.
>
> **Parameters**:
>
> - **git_url**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория
>
> - **search**:str=None - наименование ветки
>
> - **regex**:str=None - regex шаблон отбора веток

[test code: gitlab_branches](/tests/gitlab/test_gitlab_branches.py)

---

## **gitlab_commits**

>
> Получить список коммитов по ветке. Ветка параметр входной очереди.
>
> **Parameters**:
>
> - **git_url**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория
>
> - **since**:str - дата в формате ISO, ограничение глубины просмотра

[test code: gitlab_commits](/tests/gitlab/test_gitlab_commits.py)

---

## **gitlab_diff**

>
> Получить список измененых файлов по SHA commit. Входная очередь массив sha или {"id":}. Результат массив новых файлов.
>
> **Parameters**:
>
> - **tasks**:int = None - кол-во потоков
>
> - **git_url**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория

[test code: gitlab_diff](/tests/gitlab/test_gitlab_diff.py)

---

## **gitlab_freads**

>
> Получить содержимое файлов в репозитории. Входная очередь, содержит список файлов, полный маршрут от корня. Результат массив: {"bom": 0, "branch": ветка, "encode": cp1251 - найденная кодировка, "encode_detect": ASCII, "encoding": 1 - файл раскодирован, "path": - полный путь файла, "text": - содержимое файла}
>
> **Parameters**:
>
> - **tasks**:int=None - максимальное кол-во потоков обработки операций
>
> - **git_url**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория
>
> - **git_branch**:str - ветка
>
> - **path**:str - если задан параметр, то значение :1 заменяется на значение из очереди, для получения имени файла

[test code: gitlab_freads](/tests/gitlab/test_gitlab_freads.py)

---

## **gitlab_projects**

>
> Получить список проектов в репозитории. Входная очередь - не используется. Результат массив проектов.
>
> **Parameters**:
>
> - **git_url**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **search**:str=None - наименование проекта
>
> - **regex**:str=None - regex шаблон отбора веток

[test code: gitlab_projects](/tests/gitlab/test_gitlab_projects.py)

---

## **gitlab_tags**

>
> Получить список тегов в репозитории. Входная очередь - не используется.
>
> **Parameters**:
>
> - **git_url**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория
>
> - **search**:str = None - наименование тега
>
> - **regex**:str = None - regex шаблон отбора тегов

[test code: gitlab_tags](/tests/gitlab/test_gitlab_tags.py)

---

## **gitlab_walk**

>
> Получить список файлов в репозитории. Входная очередь, содержит список корневых узлов, от которых запускается процесс. Все файлы в репозитории идут от "/" Результат массив: {"name": имя файла, "path": полный маршрут файла}
>
> **Parameters**:
>
> - **tasks**:int = None - максимальное кол-во потоков обработки операций
>
> - **git_url**:str - Подключение к gitlab
>
> - **git_token**:str
>
> - **git_repo**:str - проект репозитория
>
> - **git_branch**:str - ветка
>
> - **regex:str**=None - regex шаблон отбора файлов

[test code: gitlab_walk](/tests/gitlab/test_gitlab_walk.py)
