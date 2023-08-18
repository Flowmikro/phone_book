import os
import csv
from typing import List

# Путь к файлу с данными
DATA_FILE = 'phonebook.csv'

# Заголовки таблицы
TABLE_HEADERS = ['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']

# Максимальное количество записей на странице
PAGE_SIZE = 10


def load_data() -> List[List[str]]:
    """Загружает данные из файла"""
    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
    return data


def save_data(data: List[List[str]]) -> None:
    """Сохраняет данные в файл"""
    with open(DATA_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


def print_table(data: List[List[str]], page: int = 1) -> None:
    """Выводит таблицу данных на экран"""
    start_index = (page - 1) * PAGE_SIZE
    end_index = start_index + PAGE_SIZE
    page_data = data[start_index:end_index]
    print('{:<20}{:<20}{:<20}{:<30}{:<20}{:<20}'.format(*TABLE_HEADERS))
    print('-' * 130)
    for row in page_data:
        print('{:<20}{:<20}{:<20}{:<30}{:<20}{:<20}'.format(*row))
    print('-' * 130)
    print('Страница {} из {}'.format(page, (len(data) - 1) // PAGE_SIZE + 1))


def add_record(data: List[List[str]]) -> None:
    """Добавляет новую запись в справочник"""
    record = []
    for header in TABLE_HEADERS:
        value = input('{}: '.format(header))
        record.append(value)
    data.append(record)
    save_data(data)
    print('Запись добавлена')


def edit_record(data: List[List[str]]) -> None:
    """Редактирует существующую запись"""
    index = int(input('Введите номер записи: '))
    if index < 1 or index > len(data):
        print('Некорректный номер записи')
        return
    record = data[index - 1]
    for i, header in enumerate(TABLE_HEADERS):
        value = input('{} ({}): '.format(header, record[i]))
        if value:
            record[i] = value
    save_data(data)
    print('Запись изменена')


def search_records(data: List[List[str]]) -> None:
    """Ищет записи по заданным характеристикам"""
    search_term = input("Введите фамилию или название организации для поиска: ")

    found_records = []
    for record in data:
        fields = [field.strip() for field in record]
        if search_term.lower() in [fields[0].lower(), fields[3].lower()]:
            found_records.append(record)

    if len(found_records) == 0:
        print("Записи не найдены!")
    else:
        print(f"Найдено {len(found_records)} записей:")
        for record in found_records:
            print(record)


def main() -> None:
    data = load_data()
    while True:
        print_table(data)
        print('Выберите действие:')
        print('1. Добавить запись')
        print('2. Редактировать запись')
        print('3. Поиск записей')
        print('4. Выход')
        choice = input('>>> ')
        if choice == '1':
            add_record(data)
        elif choice == '2':
            edit_record(data)
        elif choice == '3':
            search_records(data)
        elif choice == '4':
            break
        else:
            print('Некорректный выбор')


if __name__ == '__main__':
    main()
