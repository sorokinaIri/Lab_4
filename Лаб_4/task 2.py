# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open('input.csv', 'r') as file:
        read = csv.DictReader(file, delimiter=",",quotechar="'")
        json_data = list (read)

    # TODO считать содержимое csv файла

    with open('output.json', 'w') as file:
        json.dump(json_data, file, indent=4)

    # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
