# Oracle (OracleOpers)

- [oracle_execute: Выполнить SQL запрос](#oracle_execute)
- [oracle_fetchall: Выполнить запрос к базе данных](#oracle_fetchall)
- [oracle_fetchone: Выполнить запрос к базе данных](#oracle_fetchone)

---

## **oracle_execute**

>
> Выполнить SQL запрос. Запросы разбиваются на подзапросы "/" и ";". Результат массив выполнных запросов {"result": 0 - error execute, 1 - succes execute, "output": строки dbms_output потока, "errmsg": ошибка выполнения, "file": путь к файлу, если запрос был загружен из файла или git }
>
> **Parameters**:
>
> - **oracle_user**:str - Подключение к oracle
>
> - **oracle_password**:str
>
> - **oracle_dsn**:str
>
> - если не заданы параметры, то входная очередь спсиок текстов запросов.
>
> - если **git_url**:str, то список файлов из gitlab. Файл загружается из git и выполняется. Необходимы также **git_token**, **git_repo**, **git_branch**
>
> - если **path**:str, то список файлов из директория на диске. Формат атрибута "...:1...". Вместо :1 подставляется заданный файл из очереди.

[test code: oracle_execute](/tests/oracle/test_oracle_execute.py)

---

## **oracle_fetchall**

>
> Выполнить запрос к базе данных. Вернуть все записи.
>
> **Parameters**:
>
> - **oracle_user**:str - Подключение к oracle
>
> - **oracle_password**:str
>
> - **oracle_dsn**:str
>
> - если не заданы параметры, то входная очередь спсиок текстов запросов.
>
> - если **git_url**:str, то список файлов из gitlab. Файл загружается из git и выполняется. Необходимы также **git_token**, **git_repo**, **git_branch**
>
> - если **path**:str, то список файлов из директория на диске. Формат атрибута "...:1...". Вместо :1 подставляется заданный файл из очереди.

[test code: oracle_fetchall](/tests/oracle/test_oracle_fetchall.py)

---

## **oracle_fetchone**

>
> Выполнить запрос к базе данных. Вернуть только первую запись.
>
> **Parameters**:
>
> - **oracle_user**:str - Подключение к oracle
>
> - **oracle_password**:str
>
> - **oracle_dsn**:str
>
> - если не заданы параметры, то входная очередь спсиок текстов запросов.
>
> - если **git_url**:str, то список файлов из gitlab. Файл загружается из git и выполняется. Необходимы также **git_token**, **git_repo**, **git_branch**
>
> - если **path**:str, то список файлов из директория на диске. Формат атрибута "...:1...". Вместо :1 подставляется заданный файл из очереди.

[test code: oracle_fetchone](/tests/oracle/test_oracle_fetchone.py)
