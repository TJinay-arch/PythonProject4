def filter_by_state(data_list, state="EXECUTED"):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data_list: Список словарей, каждый словарь содержит хотя бы один ключ 'state'.
    :param state: Значение фильтра (опциональный аргумент), по умолчанию равно 'EXECUTED'.
    :return: Новый список словарей, удовлетворяющих фильтру.
    """
    return [item for item in data_list if item.get("state") == state]


def sort_by_date(data_list, reverse=True):
    """
    Сортирует список словарей по полю 'date'
    """
    # Сортировка осуществляется прямо по значению поля 'date'
    return sorted(data_list, key=lambda item: item["date"], reverse=reverse)
