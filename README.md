# Модуль для интернационализации Python проектов

## Знаю ли я о gettext?
Я знаю, что в Python 3 есть модуль интернационализации и локализации gettext.

## Чем вам не нравиться gettext?
Он не понравился мне тем, что для каждого языка, нужно создать две папки.
- 1. Папка названия языка. Например FR.
- 2. Папка LC_MESSAGES.

Если я использую 5 языков, бесполезных папок должно быть 10. Это уже слишком!

В итоге я написал простейший модуль, который позволяет вам сохранять строки на разных языках, 
обозначающие одно и то-же в одном CSV или DB3(SQLite3) файле. В случае необходимости, желающие могут дописать все, 
что пожелают. 

## Проблемы с числами
Допустим ваше приложение переносит файлы и выводит в консоль следующее:
    перенесен 1 файл
    перенесены 2 файла
    перенесены 3 файла
    перенесены 4 файла
    перенесены 5 файлов
    ...

Как упростить себе жизнь!? Да все просто! Надо меньше мудрствовать! Просто выводите в консоль следующее:
    перенесено файлов: 1
    перенесено файлов: 11
    перенесено файлов: 111
    перенесено файлов: 5

## Вам не нравятся CSV и SQLite
Напишите новый класс, породив его от IDataProvider, пользуясь предоставленными CSVProvider и SQLiteDataProvider,
как примерами.