# Функция маскировки номера банковской карты
def get_mask_card_number(card_number: str)-> str:
    number = str(card_number)
    # Убираем пробелы, если они есть
    number = number.replace(" ", "")
    # Проверяем длину
    if len(number) != 16:
        return "error"

    # Берем первые шесть цифр
    first_six_numb = number[:6]
    # Берем четыре посление цифры
    last_four_numb = number[-4:]
    # Собираем все в одно
    result = first_six_numb[:4] + " " + first_six_numb[4:] + "** **** " + last_four_numb
    return result


# Функция маскировки счета
def get_mask_account(account_number: str) -> str:
    number = str(account_number)
    # Убираем пробелы
    number = number.replace(" ", "")
    # Проверяем длину
    if len(number) < 4:
        return "error"

    last_four_numb = number[-4:]
    result = "**" + last_four_numb
    return result
