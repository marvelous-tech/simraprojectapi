import secrets
import string


def random_string(n=10):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(n))


def random_ascii_uppercase():
    return secrets.choice(string.ascii_uppercase)
