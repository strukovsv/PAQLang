# PAQLang

Python Async Queue Language 

[![Super-Linter](https://github.com/strukovsv/PAQLang/actions/workflows/lint.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Pytest](https://github.com/strukovsv/PAQLang/actions/workflows/pytest.yml/badge.svg)](https://github.com/strukovsv/PAQLang/tree/master/tests/main)

## Содержание

- [PAQLang](#paqlang)
  - [Содержание](#содержание)
  - [Назначение](#назначение)
  - [Install](#install)
  - [Документация](#документация)
  - [Пример обработки текстов](#пример-обработки-текстов)

## Назначение
Пакет предназначен, для выполнения асинхронных функций на языке Python. Пакет содержит встроенные функции и возможность расширения своих функций

## Install

Установка только встроенных функций 
pip install PAQLang

Установка с пакетами работы Gitlab и Oracle
pip install PAQLang[all]

## Документация
Документацию по встроенным функциям системы можно получить по [этой ссылке](./docs/ru/functions.md).

## Пример обработки текстов

```
# Задать имя файла лога oracle
- in: /app/pgm/data/oracle.yaml
# Прочитать файл и положить содержимое в очередь
# {"filename": , "text": }
- freads
# Распарсить текст файла из атрибута "text" в json
- to_json: text
# Вытащить текст атрибута text
- attr: text
# Сохранить в файле oracle
- save: oracle

# Проанализировать файл names лога
- in: /app/pgm/data/monitor.yaml
- freads
- to_json: text
# Вытащить значение из атрибута line
- attr: line
- save: monitor
```
