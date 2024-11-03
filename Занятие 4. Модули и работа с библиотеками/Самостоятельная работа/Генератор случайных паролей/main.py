import string
from random import sample

SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + string.digits
print(SYMBOLS)

def get_random_password() -> str:
    return ''.join(sample(SYMBOLS, 8))  # TODO написать функцию генерации случайных паролей


print(get_random_password())
