from masks import get_mask_account, get_mask_card_number

def mask_account_card(account_info: str) -> str:
    """Обрабатывает информацию о карте или счёте и возвращает строку с замаскированным номером"""
    # Разбиваем на части
    parts = account_info.split()

   # Определяем, где название, где номер
    number = parts[-1]
    name = " ".join(parts[:-1])

    # Если в номере 20 цифр - счет, 16 - карта, остальное - ошибка
    if len(number) == 20:
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    # Склеиваем все вместе
    return name + " " + masked

""" Функция, которая выводит дату """
def get_date(date: str) -> str:
    # Разбиваем на время и дату
    date_time = date.split("T")
    date_part = date_time[0]

    # Разбиваем по дефису на части
    parts = date_part.split("-")
    year = parts[0]
    month = parts[1]
    day = parts[2]

    return day + "." + month + "." + year

