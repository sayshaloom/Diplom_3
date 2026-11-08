import random
import string

def generate_user_payload():
    random_part = "".join(random.choice(string.ascii_lowercase) for _ in range(6))
    return {
        "email": f"test_user_{random_part}@yandex.ru",
        "password": f"pass_{random_part}",
        "name": f"Name_{random_part}",
    }