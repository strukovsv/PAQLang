# Type

Must be one of the following:

* **build**: Changes that affect the build tool or external dependencies (Изменения влияющие на систему сборки или внешние зависимости)
* **ci**: Changes to our CI configuration files and scripts (Изменения в наших CI файлах или скриптах)
* **docs**: Documentation only changes (Изменяется только документация)
* **feat**: A new feature (Новая функцция)
* **fix**: A bugfix (Исправлена ошибка)
* **perf**: A code change that improves performance (Изменение кода, повышающее производительность)
* **refactor**: A code change that neither fixes a bug nor adds a feature (Изменение кода которое не исправляет ошибку и не добавляет функцию)
* **test**: Adding missing tests or correcting existing tests (Добавление отсутствующих тестов или исправление существующих тестов)

| type     | relea | code   | note                                                                         |
|----------|-------|--------|------------------------------------------------------------------------------|
| breaking | major |  #.x.x | Изменения влияющие на систему сборки или внешние зависимости                 |
| chore    |       |        | обновление задач grunt и т.д.; Отсутствие изменения производственного кода   |
| ci       |       |        | Изменения в наших CI файлах или скриптах                                     |
| docs     |       |        | Изменяется только документация                                               |
| feat     | minor |  x.#.x | Новая функцция                                                               |
| fix      | patch |  x.x.# | Исправлена ошибка                                                            |
| refactor | patch |  x.x.# |Изменение кода которое не исправляет ошибку и не добавляет функцию            |
| security | patch |  x.x.# |                                                                              |
| style    | patch |  x.x.# | Форматирование, отсутствующие точки с запятой и т.д.; Никаких изменений кода |
| test     |       |        | Добавление отсутствующих тестов или исправление существующих тестов          |
