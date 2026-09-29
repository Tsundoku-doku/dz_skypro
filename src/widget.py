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

