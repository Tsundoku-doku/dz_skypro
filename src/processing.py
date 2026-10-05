def filter_by_state(operations, state="EXECUTED"):
    #Создаем пустой список
    result =[]
    for operation in operations:
        if operation["state"] == state:
            result.append(operation)
    return result

""" Функция, которая  принимает список словарей и необязательный параметр, задающий порядок сортировки"""
def sort_by_date(operations, reverse=True):
    return sorted(operations, key=lambda operation: operation["date"], reverse=True)
