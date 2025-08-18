def filter_by_state(data_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data_list if item.get("state") == state]


def sort_by_date(data_list: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по полю 'date'
    """

    return sorted(data_list, key=lambda item: item["date"], reverse=reverse)
