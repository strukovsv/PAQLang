# Сервисные операции

- [error](#error)
- [include](#include)
- [info](#info)
- [msleep](#msleep)
- [opers](#opers)
- [popers](#popers)
- [send_errors](#send_errors)
- [send_success](#send_success)
- [sleep](#sleep)

---

## **error**

```text
Вывести очередь в error поток

Входная очередь сообщение
name:str = None or param:str = None - заголовок
test-attr:str = None - тестируемый аттрибут
Условие параметры:
"lt", "le", "eq", "ne", "gt", "ge", "instr", "notinstr"
send-attr:str = None - отправляемый атрибут иначе печатаем весь элемент

```

[/tests/main/test_error.py](/tests/main/test_error.py)

---

## **include**

```text
Загрузить подпрограммы

Входная очередь - имена json и yaml файлов

```

[/tests/main/test_include.py](/tests/main/test_include.py)

---

## **info**

```text
Вывести очередь в info поток

Входная очередь сообщение
name:str = None or param:str = None - заголовок
test-attr:str = None - тестируемый аттрибут
Условие параметры:
"lt", "le", "eq", "ne", "gt", "ge", "instr", "notinstr"
send-attr:str = None - отправляемый атрибут иначе печатаем весь элемент

```

[/tests/main/test_info.py](/tests/main/test_info.py)

---

## **msleep**

```text
Асинхронно заснуть на заданное кол-во секунд.
Запустить несколько потоков, в зависимости от входной очереди.
Для отладки асинхронности

in_queue:list - очередь задержек

```

[/tests/main/test_msleep.py](/tests/main/test_msleep.py)

---

## **opers**

```text
Вывести словарь операций
```

[/tests/main/test_opers.py](/tests/main/test_opers.py)

---

## **popers**

```text
Вывести словарь операций

group:[str|list] или param:str или None -
вывеcти только данные группы операций
path: = None - если указано, то вывести в файлы по данному маршруту
```

[/tests/main/test_popers.py](/tests/main/test_popers.py)

---

## **send_errors**

```text
Отправить сообщение об ошибке

Входная очередь сообщение
name:str = None or param:str = None - сообщение в заголовке,
по умолчанию PAQLang
test-attr:str = None - тестируемый аттрибут
Условие параметры:
"lt", "le", "eq", "ne", "gt", "ge", "instr", "notinstr"
send-attr:str = None - отправляемый атрибут иначе печатаем весь элемент

```

[/tests/main/test_send_errors.py](/tests/main/test_send_errors.py)

---

## **send_success**

```text
Отправить успешное сообщение

Входная очередь сообщение
name:str = None or param:str = None - сообщение в заголовке,
по умолчанию PAQLang
test-attr:str = None - тестируемый аттрибут
Условие параметры:
"lt", "le", "eq", "ne", "gt", "ge", "instr", "notinstr"
send-attr:str = None - отправляемый атрибут иначе печатаем весь элемент

```

[/tests/main/test_send_success.py](/tests/main/test_send_success.py)

---

## **sleep**

```text
Асинхронно заснуть на заданное кол-во секунд

param:float - кол-во секунд, если не задано, то 1 секунда

```

[/tests/main/test_sleep.py](/tests/main/test_sleep.py)
