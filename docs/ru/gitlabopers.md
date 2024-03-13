# Gitlab

- [gitlab_branches](#gitlab_branches)
- [gitlab_commits](#gitlab_commits)
- [gitlab_diff](#gitlab_diff)
- [gitlab_freads](#gitlab_freads)
- [gitlab_projects](#gitlab_projects)
- [gitlab_tags](#gitlab_tags)
- [gitlab_walk](#gitlab_walk)

---

## **gitlab_branches**

```text
Получить список веток в репозитории

git_url:str - Подключение к gitlab
git_token:str
git_repo:str - проект репозитория
search:str = None - наименование ветки
regex:str = None - regex шаблон отбора веток

Входная очередь - не используется

Результат массив веток

```

[/tests/main/test_gitlab_branches.py](/tests/main/test_gitlab_branches.py)

---

## **gitlab_commits**

```text
Получить список тегов в репозитории

git_url:str - Подключение к gitlab
git_token:str
git_repo:str - проект репозитория

Результат массив тегов

```

[/tests/main/test_gitlab_commits.py](/tests/main/test_gitlab_commits.py)

---

## **gitlab_diff**

```text
Получить список измененых файлов по SHA commit

tasks:int = None - кол-во потоков
git_url:str - Подключение к gitlab
git_token:str
git_repo:str - проект репозитория

Входная очередь массив sha или {"id":}
Результат массив новых файлов

```

[/tests/main/test_gitlab_diff.py](/tests/main/test_gitlab_diff.py)

---

## **gitlab_freads**

```text
Получить содержимое файлов в репозитории

tasks:int = None - Максимальное кол-во потоков обработки операций
git_url:str - Подключение к gitlab
git_token:str
git_repo:str - проект репозитория
git_branch:str - ветка

Входная очередь, содержит список файлов, полный маршрут от корня

Результат массив
- bom: 0
branch: - ветка
encode: cp1251 - найденная кодировка
encode_detect: ASCII
encoding: 1 - файл раскодирован
path: - полный путь файла
text: - содержимое файла

```

[/tests/main/test_gitlab_freads.py](/tests/main/test_gitlab_freads.py)

---

## **gitlab_projects**

```text
Получить список проектов в репозитории

git_url:str - Подключение к gitlab
git_token:str
search:str = None - наименование проекта
regex:str = None - regex шаблон отбора веток

Входная очередь - не используется

Результат массив проектов

```

[/tests/main/test_gitlab_projects.py](/tests/main/test_gitlab_projects.py)

---

## **gitlab_tags**

```text
Получить список тегов в репозитории

git_url:str - Подключение к gitlab
git_token:str
git_repo:str - проект репозитория
search:str = None - наименование тега
regex:str = None - regex шаблон отбора тегов

Входная очередь - не используется

Результат массив тегов

```

[/tests/main/test_gitlab_tags.py](/tests/main/test_gitlab_tags.py)

---

## **gitlab_walk**

```text
Получить список файлов в репозитории

tasks:int = None - Максимальное кол-во потоков обработки операций
git_url:str - Подключение к gitlab
git_token:str
git_repo:str - проект репозитория
git_branch:str - ветка
regex:str = None - regex шаблон отбора файлов

Входная очередь, содержит список корневых узлов,
от которых запускается процесс
Все файлы в репозитории идут от "/"

Результат массив
- name: - имя файла
path: - полный маршрут файла

```

[/tests/main/test_gitlab_walk.py](/tests/main/test_gitlab_walk.py)
