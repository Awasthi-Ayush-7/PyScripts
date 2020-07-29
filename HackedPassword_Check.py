import requests
import hashlib


def request_from_api(query):
    url = "https://api.pwnedpasswords.com/range/" + query
    respone = requests.get(url)
    if respone.status_code != 200:
        raise RuntimeError("Bad response code. Check your API.")
    return respone


def get_the_count(hashes_we_get, hash_to_check):
    hashes_we_get = (i.split(":") for i in hashes_we_get.text.splitlines())
    for h, count in hashes_we_get:
        if h == hash_to_check:
            return count
    return 0


def lets_check_password(password):
    sha1_pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1_pass[:5], sha1_pass[5:]
    response_ = request_from_api(first5_char)
    return get_the_count(response_, tail)


def main(*args):
    for password in args:
        count = lets_check_password(password)
        if count:
            print(f"{password} was found {count} times! Might wanna change your password.")
        else:
            print(f"{password} not found! You are good to go.")


if __name__ == '__main__':
    main("hello")
