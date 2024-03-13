# Строковые операции

- [join](#join)
- [match](#match)
- [replace](#replace)
- [search](#search)
- [split](#split)
- [subst](#subst)
- [transform](#transform)

---

## **join**

```text
Соединить элементы массива в строку

param:str - строка объединения, по умолчанию 


```

[/tests/main/test_join.py](/tests/main/test_join.py)

---

## **match**

```text
Вырезать из элемента, заданный regex подстроку

in_queue - входная очередь
regex:str или param:str - условие получения подстроки, группа 1

```

[/tests/main/test_match.py](/tests/main/test_match.py)

---

## **replace**

```text
Заменить во входной очереди, в строках, заданный regex на подстроку

in_queue - входная очередь
regex:str или param:str - условие получения подстроки
dest:str - на что заменять, если не указано, заменяем на пустую строку

```

[/tests/main/test_replace.py](/tests/main/test_replace.py)

---

## **search**

```text
Отобрать элементы из очереди, удовлетворяющие условию

in_queue - входная очередь
attr:str - если указано, то анализировать атрибут из элемента очереди
regex:str или param:str - условия отбора

```

[/tests/main/test_search.py](/tests/main/test_search.py)

---

## **split**

```text
Разбить строку на элементы

param:str - строка разбиения, по умолчанию 

```

[/tests/main/test_split.py](/tests/main/test_split.py)

---

## **subst**

```text
Заменить в заданной строке :1, на элементы из входной очереди

in_queue - входная очередь
text:str или param:str - строка шаблон

```

[/tests/main/test_subst.py](/tests/main/test_subst.py)

---

## **transform**

```text
Найти в списке элемент,
независимо от регистра и вернуть правильное наименование
```

[/tests/main/test_transform.py](/tests/main/test_transform.py)
