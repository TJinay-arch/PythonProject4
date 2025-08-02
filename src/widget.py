import masks


def mask_account_card(input_string: str) -> str:
    """функция для маскировки номера карты или счета, возвращает значение в формате строки"""
    if "Счет" in input_string:
        changed_string_second_part: str = masks.get_mask_account(input_string[-20:])
        changed_string_first_part: str = input_string[:-20]
        return changed_string_first_part + changed_string_second_part
    else:
        changed_string_second_part = masks.get_mask_card_number(input_string[-16:])
        changed_string_first_part = input_string[:-16]
        return changed_string_first_part + changed_string_second_part


def get_date(input_string: str) -> str:
    """функция преобразует дату к удобному варианту для дальнейшей работы"""
    return input_string[8:10] + "." + input_string[5:7] + "." + input_string[0:4]
