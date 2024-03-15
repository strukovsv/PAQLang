# Сервисные операции (OtherOpers)

- [error: Вывести очередь в error поток](#error)
- [include: Загрузить подпрограммы](#include)
- [info: Вывести очередь в info поток](#info)
- [msleep: Асинхронно заснуть на заданное кол-во секунд](#msleep)
- [opers: Вывести словарь функций](#opers)
- [popers: Подготовить документацию по функциям](#popers)
- [send_errors: Отправить сообщение об ошибке](#send_errors)
- [send_success: Отправить успешное сообщение](#send_success)
- [sleep: Асинхронно заснуть на заданное кол-во секунд](#sleep)

---

## **error**

>
> Вывести очередь в error поток. Входная очередь сообщений.
>
> **Parameters**:
>
> - **name**:str=None or **param**:str = None - заголовок
>
> - **test-attr**:str=None - тестируемый аттрибут
>
> - **lt** - меньше
>
> - **le** - Меньше или равно
>
> - **eq** - равно
>
> - **ne** - не равно
>
> - **gt** - больше
>
> - **ge** - больше или равно
>
> - **instr** - входит в строку
>
> - **notinstr** - не входит в строку
>
> - **send-attr**:str=None - отправляемый атрибут, иначе печатаем весь элемент

[test code: error](/tests/main/test_error.py)

---

## **include**

>
> Загрузить подпрограммы.
>
> **Parameters**:
>
> - **Входная очередь** - имена json и yaml файлов

[test code: include](/tests/main/test_include.py)

---

## **info**

>
> Вывести очередь в info поток. Входная очередь сообщений.
>
> **Parameters**:
>
> - **name**:str=None or **param**:str = None - заголовок
>
> - **test-attr**:str=None - тестируемый аттрибут
>
> - **send-attr**:str=None - отправляемый атрибут,
>
> - **lt** - меньше
>
> - **le** - Меньше или равно
>
> - **eq** - равно
>
> - **ne** - не равно
>
> - **gt** - больше
>
> - **ge** - больше или равно
>
> - **instr** - входит в строку
>
> - **notinstr** - не входит в строку иначе печатаем весь элемент

[test code: info](/tests/main/test_info.py)

---

## **msleep**

>
> Асинхронно заснуть на заданное кол-во секунд. Запустить несколько потоков, в зависимости от входной очереди. Для отладки асинхронности.
>
> **Parameters**:
>
> - **Входная очередь**:list - очередь задержек

[test code: msleep](/tests/main/test_msleep.py)

---

## **opers**

>
> Вывести словарь функций.
>
> **Parameters**:
>
> - **param**:str=None - по заданной группе функций

[test code: opers](/tests/main/test_opers.py)

---

## **popers**

>
> Подготовить документацию по функциям.
>
> **Parameters**:
>
> - **groups**:[str|list] или param:str или None - вывеcти только данные заданной группы функций
>
> - **path**:str - вывести в файлы по данному маршруту

[test code: popers](/tests/main/test_popers.py)

---

## **send_errors**

>
> Отправить сообщение об ошибке. Входная очередь сообщение.
>
> **Parameters**:
>
> - **name**:str = None or **param**:str = None - сообщение в заголовке, по умолчанию PAQLang
>
> - **test-attr**:str = None - тестируемый аттрибут
>
> - **send-attr**:str = None - отправляемый атрибут, иначе печатаем весь элемент
>
> - **lt** - меньше
>
> - **le** - Меньше или равно
>
> - **eq** - равно
>
> - **ne** - не равно
>
> - **gt** - больше
>
> - **ge** - больше или равно
>
> - **instr** - входит в строку
>
> - **notinstr** - не входит в строку

[test code: send_errors](/tests/main/test_send_errors.py)

---

## **send_success**

>
> Отправить успешное сообщение. Входная очередь сообщение.
>
> **Parameters**:
>
> - **name**:str = None or **param**:str = None - сообщение в заголовке, по умолчанию PAQLang
>
> - **test-attr**:str = None - тестируемый аттрибут
>
> - **send-attr**:str = None - отправляемый атрибут, иначе печатаем весь элемент
>
> - **lt** - меньше
>
> - **le** - Меньше или равно
>
> - **eq** - равно
>
> - **ne** - не равно
>
> - **gt** - больше
>
> - **ge** - больше или равно
>
> - **instr** - входит в строку
>
> - **notinstr** - не входит в строку

[test code: send_success](/tests/main/test_send_success.py)

---

## **sleep**

>
> Асинхронно заснуть на заданное кол-во секунд.
>
> **Parameters**:
>
> - **param**:float - кол-во секунд, если не задано, то 1 секунда

[test code: sleep](/tests/main/test_sleep.py)
