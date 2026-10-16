""" Фунуция, возвращает новый список словарей"""
def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    #Создаем пустой список
    result =[]
    for operation in operations:
        if operation["state"] == state:
            result.append(operation)
    return result

""" Функция, которая  принимает список словарей и необязательный параметр, задающий порядок сортировки"""
def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    return sorted(operations, key=lambda operation: operation["date"], reverse=True)
