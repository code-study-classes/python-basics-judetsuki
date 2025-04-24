def is_weekend(day):
    weekend_days = {
        1: False,
        2: False,
        3: False,
        4: False,
        5: False,
        6: True,
        7: True
    }
    return weekend_days.get(day, False)


def get_discount(amount: float) -> float:
    match amount:
        case a if a >= 5000:
            return round(a * 0.10, 2)
        case a if a >= 1000:
            return round(a * 0.05, 2)
        case _:
            return 0.0


def describe_number(n: int) -> str:
    parity = "четное" if n % 2 == 0 else "нечетное"
    digit_count = len(str(n))

    match digit_count:
        case 1:
            digit_desc = "однозначное"
        case 2:
            digit_desc = "двузначное"
        case 3:
            digit_desc = "трехзначное"

    return f"{parity} {digit_desc} число"


def convert_to_meters(unitNumber: int, lengthInUnits: float) -> float:
    match unitNumber:
        case 1:  
            return lengthInUnits * 0.1
        case 2:  
            return lengthInUnits * 1000
        case 3:  
            return lengthInUnits * 1
        case 4: 
            return lengthInUnits * 0.001
        case 5:  
            return lengthInUnits * 0.01
        case _:
            return 0.0


def describe_age(age: int) -> str:
    tens_words = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто"
    }
    units_words = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }

    if age == 100:
        age_words = "сто"
    else:
        tens = age // 10
        units = age % 10
        if units == 0:
            age_words = tens_words[tens]
        else:
            age_words = f"{tens_words[tens]} {units_words[units]}"


    if 11 <= age % 100 <= 14:
        suffix = "лет"
    else:
        last_digit = age % 10
        if last_digit == 1:
            suffix = "год"
        elif 2 <= last_digit <= 4:
            suffix = "года"
        else:
            suffix = "лет"

    return f"{age_words} {suffix}"


