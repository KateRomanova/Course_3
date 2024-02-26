from src.main import mask_card_number


def test_mask_card_number():
    assert mask_card_number('visa 1234567891234567') == 'visa 1234 56** **** 4567'
