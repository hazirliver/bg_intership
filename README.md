# Решения тестового задания на [стажировку]((https://bostongene.vcv.ru/r/bioinformatics2021)) по биоинформатике BostonGene 2021

---

### Задача 1

Требуется определить идентификационные номера образцов RNA-seq, которые не были удачно загружены с сервера. Для
реализации поставленной задачи написан скрипт, работающий на языке `Python3`.

Запуск скрипта осуществляется из командной строки как показано ниже

```bash
python task_1.py -h
usage: task_1.py [-h] -f F [-r R]

Creates file containing info about aborted downloads.

optional arguments:
  -h, --help  show this help message and exit
  -f F        Folder name where download logs are located. Required argument.
  -r R        Report filename. Default name is aborted_downloads_report.txt
```

Функция принимает два параметра:

- `-f` — Путь до директории, в которой расположены папки, в которых находятся логи загрузок. Требуется передать либо
  абсолютный путь от корня, либо относительный от скрипта. <i>Обязательный параметр</i>.
- `-r` — Имя файла отчета. <i>Не обязательный параметр</i> со значением по умолчанию aborted_downloads_report.txt.

На выходе получаем файл следующей структуры:

```
data_1:
SRR5117471
SRR6384380
data_2:
SRR6384382
```

----