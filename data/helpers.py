import random
import string


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def generate_user_payload():
    random_part = generate_random_string(6)
    return {
        "email": f"test_user_{random_part}@yandex.ru",
        "password": f"pass_{random_part}",
        "name": f"Name_{random_part}",
    }