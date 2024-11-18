import random
import string


def id_(ids):
    while True:
        id = random.randint(10000, 99999)
        if any(int(d) % 2 != 0 for d in str(id)) and id not in ids:
            ids.add(id)
            return str(id)


def login_(logins):
    glas = set("aeiou")
    while True:
        login = ''.join(random.choices(string.ascii_lowercase, k=6))
        if sum(1 for ch in login if ch in glas) >= 2 and login not in logins:
            logins.add(login)
            return login


def password_(passwords):
    while True:
        characters = string.ascii_letters + string.digits
        password = ''.join(random.sample(characters, 10))
        if (
                sum(ch.isdigit() for ch in password) >= 3 and
                any(ch.islower() for ch in password) and
                password not in passwords
        ):
            passwords.add(password)
            return password


def result_(n):
    ids = set()
    logins = set()
    passwords = set()
    result = []

    for _ in range(n):
        id = id_(ids)
        login = login_(logins)
        password = password_(passwords)
        result.append((id, login, password))

    return result



n = int(input("Введите количество записей: "))
results = result_(n)

for result in results:
    print(' - '.join(result))
