# Доработайте функцию ask_numЬer() так, чтобы ее можно было вызывать еще с одним параметром
# -кратностью (величиной шага).
# Сделайте шаг по умолчанию равным 1.


def ask_number(question, low, high, multiplicity=1):
    """Просит ввести число из диапозона."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response * multiplicity