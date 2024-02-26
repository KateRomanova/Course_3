from src.utils import load_last_five_executed_operations
import datetime

last_operations = load_last_five_executed_operations

for operation in last_operations():


    def formatted_date():
        """Переводим формат даты исходника в требуемый формат"""
        date = operation['date']
        dt = datetime.datetime.fromisoformat(date)
        return datetime.datetime.strftime(dt, '%d.%m.%Y')


    "извлекаем счет, с которого производится перевод, если он есть"
    operation_from = operation.get('from', '')


    def mask_card_number():
        """Маскируем номер карты, чтобы были видны только первые 6 цифр и последние 4 цифры карты"""
        parts = operation_from.split()

        if parts:
            last_part = parts[-1]
            masked_last_part = last_part[:4] + ' ' + last_part[4:6] + '**' + ' ' + '****' + ' ' + last_part[-4:]
            masked_from = ' '.join(parts[:-1] + [masked_last_part]) + ' -> '
        else:
            masked_from = ""

        return masked_from

    def mask_account_number():
        """Маскируем номер счета, чтобы были видны только последние 4 цифры счета"""
        operation_to = operation['to']
        masked_account_nr = "Счет **" + operation_to[-4:]
        return masked_account_nr

    print(formatted_date(), operation['description'])
    print(mask_card_number(), mask_account_number())
    print(operation['operationAmount']['amount'], operation['operationAmount']['currency']['name'])
    print()
