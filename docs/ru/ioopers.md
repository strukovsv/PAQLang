# Операции ввода/вывода

- [freads](#freads)
- [to_json](#to_json)
- [walk](#walk)

---

## **freads**

```text
Прочитать файл и положить содержимое в выходную очередь
{fname, text}

encoding:str, если не задано, то param:str - по умолчанию utf-8
кодировка для windows файлов cp1251
to_json = None, если указан атрибут,
то файл преобразовать в объект и вернуть как массив
split:str = None, есил указан атрибут,
то разбить текстовый файл на строки.
Если указан символ разбиения, то разбить соответственно ему.

```

[/tests/main/test_freads.py](/tests/main/test_freads.py)

---

## **to_json**

```text
Распарсить JSON или YAML строковый элемент и положить в очередь

Входная строка преобразуется в JSON, несколько массивов склеиваются
attr:str = None
или param:str = None - задает имя атрибута текста JSON или YAML

```

[/tests/main/test_to_json.py](/tests/main/test_to_json.py)

---

## **walk**

```text
Получить список файлов в директории

path:str или param:str - корневой маршрут поиска файлов
regex:str - шаблон отбора файлов, если не задан, то все файлы

```

[/tests/main/test_walk.py](/tests/main/test_walk.py)
