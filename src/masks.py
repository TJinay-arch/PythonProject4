def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер кредитной карты и возвращает маску, скрывающую большую часть
    номеров кроме первых трехи последнего блока."""
    card_mask = card_number[0:4] + " " + card_number[5:7] + "** **** " + card_number[12:16]
    return card_mask


def get_mask_account(account: str) -> str:
    """Функция принимает номер счета и возвращает его маску, скрывающую большую часть кроме
    последних четырех символов.
    :rtype: str"""
    account_mask = "**" + account[-4:]
    return account_mask



