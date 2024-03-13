# Работа со списками

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

```text
Получить уникальные элементы очереди и отсортировать по возрастанию

in_queue - входная очередь

```

[/tests/main/test_distinct.py](/tests/main/test_distinct.py)

---

## **expand**

```text
Расширить подмассивы

in_queue - входная очередь
param - добавляемое значение в очередь

```

[/tests/main/test_expand.py](/tests/main/test_expand.py)

---

## **first**

```text
Вернуть первый элемент очереди

in_queue - входная очередь
param:str - если задано значение, то взять очередь из переменной

```

[/tests/main/test_first.py](/tests/main/test_first.py)

---

## **in**

```text
Положить данные в очередь как список

Результат в выходную очередь out_queue

```

[/tests/main/test_in.py](/tests/main/test_in.py)

---

## **intersect**

```text
Вернуть только пересекаемые элементы очереди

in_queue - первая очередь
param:list - вторая очередь

```

[/tests/main/test_intersect.py](/tests/main/test_intersect.py)

---

## **last**

```text
Вернуть последний элемент очереди

in_queue - входная очередь
param:str - если задано значение, то взять очередь из переменной

```

[/tests/main/test_last.py](/tests/main/test_last.py)

---

## **len**

```text
Вернуть размер входной очереди

in_queue - входная очередь

```

[/tests/main/test_len.py](/tests/main/test_len.py)

---

## **minus**

```text
Вычесть очередь из очереди

in_queue - входная очередь
param:list - вычитаемая очередь

```

[/tests/main/test_minus.py](/tests/main/test_minus.py)

---

## **out**

```text
Содержимое очереди записать в переменную памяти

in_queue - входная очередь
param:str - наименование переменной памяти
ps: очередь не изменяется

```

[/tests/main/test_out.py](/tests/main/test_out.py)

---

## **pop**

```text
Вытолкнуть последний элемент из очереди

in_queue - входная очередь
param:str - если задано значение, то взять очередь из переменной

```

[/tests/main/test_pop.py](/tests/main/test_pop.py)

---

## **print**

```text
Распечатать текущую очередь данных, в loggin.info

in_queue - входная очередь
ps: очередь не изменяется

```

[/tests/main/test_print.py](/tests/main/test_print.py)

---

## **push**

```text
Добавить элементы в конец текущей очереди

in_queue - входная очередь
param - добавляемое значение в очередь

```

[/tests/main/test_push.py](/tests/main/test_push.py)

---

## **save**

```text
Сохранить очередь на диске

in_queue - входная очередь
param:str - наименование файла данных

```

[/tests/main/test_save.py](/tests/main/test_save.py)

---

## **sort**

```text
Отсортировать список

in_queue - входная очередь
param:str - направление сортировки "desc", "asc" - по умолчанию

```

[/tests/main/test_sort.py](/tests/main/test_sort.py)

---

## **union**

```text
Объединить очереди, убрать дубликаты

in_queue - входная очередь
param - добавляемое значение в очередь

```

[/tests/main/test_union.py](/tests/main/test_union.py)

---

## **union_all**

```text
Объединить очереди

in_queue - входная очередь
param - добавляемое значение в очередь

```

[/tests/main/test_union_all.py](/tests/main/test_union_all.py)
