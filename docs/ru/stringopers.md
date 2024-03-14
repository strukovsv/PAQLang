# Строковые операции (StringOpers)

- [join](#join)
- [match](#match)
- [replace](#replace)
- [search](#search)
- [split](#split)
- [subst](#subst)
- [transform](#transform)

---

## **join**

>
> Соединить элементы массива в строку.
>
> **Parameters**:
>
> - **param**:str - строка объединения, по умолчанию "**\n**"

[test code: join](/tests/main/test_join.py)

---

## **match**

>
> Вырезать из элемента, заданный regex подстроку.
>
> **Parameters**:
>
> - **regex**:str или **param**:str - условие получения подстроки, группа 1

[test code: match](/tests/main/test_match.py)

---

## **replace**

>
> Заменить во входной очереди, в строках, заданный regex на подстроку.
>
> **Parameters**:
>
> - **regex**:str или **param**:str - условие получения подстроки
>
> - **dest**:str - на что заменять, если не указано, заменяем на пустую строку

[test code: replace](/tests/main/test_replace.py)

---

## **search**

>
> Отобрать элементы из очереди, удовлетворяющие условию.
>
> **Parameters**:
>
> - **attr**:str=None - если указано, то анализировать атрибут из элемента очереди
>
> - **regex**:str или **param**:str - условия отбора

[test code: search](/tests/main/test_search.py)

---

## **split**

>
> Разбить строку на элементы.
>
> **Parameters**:
>
> - **param**:str - строка разбиения, по умолчанию "**\n**"

[test code: split](/tests/main/test_split.py)

---

## **subst**

>
> Заменить в заданной строке :1, на элементы из входной очереди.
>
> **Parameters**:
>
> - **text**:str или **param**:str - строка шаблон

[test code: subst](/tests/main/test_subst.py)

---

## **transform**

>
> Найти в списке элемент, независимо от регистра и вернуть правильное наименование

[test code: transform](/tests/main/test_transform.py)
