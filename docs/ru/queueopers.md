# Работа со списками (QueueOpers)

- [distinct](#distinct)
- [expand](#expand)
- [first](#first)
- [in](#in)
- [intersect](#intersect)
- [last](#last)
- [len](#len)
- [minus](#minus)
- [out](#out)
- [pop](#pop)
- [print](#print)
- [push](#push)
- [save](#save)
- [sort](#sort)
- [union](#union)
- [union_all](#union_all)

---

## **distinct**

>
> Получить уникальные элементы очереди и отсортировать по возрастанию.

[test code: distinct](/tests/main/test_distinct.py)

---

## **expand**

>
> Расширить подмассивы.
>
> **Parameters**:
>
> - **param** - добавляемое значение в очередь

[test code: expand](/tests/main/test_expand.py)

---

## **first**

>
> Вернуть первый элемент очереди.
>
> **Parameters**:
>
> - **param**:str=None - если задано значение, то взять очередь из переменной
> __

[test code: first](/tests/main/test_first.py)

---

## **in**

>
> Положить данные в очередь.

[test code: in](/tests/main/test_in.py)

---

## **intersect**

>
> Вернуть только пересекаемые элементы очереди.
>
> **Parameters**:
>
> - **param**:list - вторая очередь

[test code: intersect](/tests/main/test_intersect.py)

---

## **last**

>
> Вернуть последний элемент очереди.
>
> **Parameters**:
>
> - **param**:str=None - если задано значение, то взять очередь из переменной

[test code: last](/tests/main/test_last.py)

---

## **len**

>
> Вернуть размер входной очереди.

[test code: len](/tests/main/test_len.py)

---

## **minus**

>
> Вычесть очередь из очереди.
>
> **Parameters**:
>
> - **param**:list - вычитаемая очередь

[test code: minus](/tests/main/test_minus.py)

---

## **out**

>
> Содержимое очереди записать в переменную памяти.
>
> **Parameters**:
>
> - **param**:str - наименование переменной памяти

[test code: out](/tests/main/test_out.py)

---

## **pop**

>
> Вытолкнуть последний элемент из очереди.
>
> **Parameters**:
>
> - **param**:str - если задано значение, то взять очередь из переменной

[test code: pop](/tests/main/test_pop.py)

---

## **print**

>
> Распечатать текущую очередь данных, в loggin.info. Очередь не изменяется.
>
> **Parameters**:
>
> - **param**:str - заголовок сообщения

[test code: print](/tests/main/test_print.py)

---

## **push**

>
> Добавить элементы в конец текущей очереди.
>
> **Parameters**:
>
> - **param** - добавляемое значение в очередь

[test code: push](/tests/main/test_push.py)

---

## **save**

>
> Сохранить очередь в файл.
>
> **Parameters**:
>
> - **param**:str - наименование файла данных

[test code: save](/tests/main/test_save.py)

---

## **sort**

>
> Отсортировать входную очередь.
>
> **Parameters**:
>
> - **param**:str - направление сортировки **"desc"**,
>
> - "asc"** - по умолчанию
> __

[test code: sort](/tests/main/test_sort.py)

---

## **union**

>
> Объединить очереди, убрать дубликаты.
>
> **Parameters**:
>
> - **param** - добавляемое значение в очередь

[test code: union](/tests/main/test_union.py)

---

## **union_all**

>
> Объединить очереди.
>
> **Parameters**:
>
> - **param** - добавляемое значение в очередь

[test code: union_all](/tests/main/test_union_all.py)
