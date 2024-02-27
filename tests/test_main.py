from src.main import *


def test_mask_card_number():
    assert mask_card_number('visa 1234567891234567') == 'visa 1234 56** **** 4567 -> '
    assert mask_card_number('american express 9876543210987654') == 'american express 9876 54** **** 7654 -> '
    assert mask_card_number('') == ''
    assert mask_card_number('5432112345678909') == '5432 11** **** 8909 -> '


def test_formatted_date():
    assert formatted_date('2019-07-03T18:35:29.512364') == '03.07.2019'
    assert formatted_date('2018-06-05') == '05.06.2018'


def test_mask_account_number():
    assert mask_account_number('Счет 64686473678894779589') == 'Счет **9589'

