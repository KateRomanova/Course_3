import json
import operator


def load_operations():
    """
    Загружает список операций из файла
    """
    with open('./operations.json', 'r', encoding='utf-8') as o:
        operations = json.load(o)

    return operations


def load_last_five_executed_operations():
    """
    Создает список исполненных операций, сортирует их по дате и выводит 5 последних операций
    """
    all_operations = load_operations()
    executed_operations = []
    for operation in all_operations:
        for key, value in operation.items():
            if key == 'state' and value == 'EXECUTED':
                executed_operations.append(operation)
    sorted_operations = sorted(executed_operations, key=operator.itemgetter('date'), reverse=True)
    last_operations = sorted_operations[:5]
    return last_operations
