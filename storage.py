from tinydb import TinyDB, Query
from tinydb.operations import set
from typing import Any
from settings import DEFAULT_PASS_LEN, DEFAULT_ALLOW_NUMBERS, DEFAULT_ALLOW_LOWERCASE, DEFAULT_ALLOW_UPPERCASE,\
    DEFAULT_ALLOW_SPEC, DEFAULT_PASS_COUNT


class UserStorage:

    def __init__(self):
        self.users = TinyDB('db.json', indent=4).table("users")
        self.user = Query()

    def exist(self, user_id: int) -> bool:
        return bool(self.users.search(self.user.user_id == user_id))

    def create(self, user_id: int) -> int:
        return self.users.insert(dict(
            user_id=user_id,
            pass_len=DEFAULT_PASS_LEN,
            pass_count=DEFAULT_PASS_COUNT,
            allow_numbers=DEFAULT_ALLOW_NUMBERS,
            allow_lowercase=DEFAULT_ALLOW_LOWERCASE,
            allow_uppercase=DEFAULT_ALLOW_UPPERCASE,
            allow_spec=DEFAULT_ALLOW_SPEC
        ))

    def get(self, user_id: int) -> dict:
        return self.users.search(self.user.user_id == user_id)[0]

    def update(self, field: str, val: Any, user_id: int):
        self.users.update(set(field, val), self.user.user_id == user_id)

    def get_or_create(self, user_id: int) -> dict:
        if self.exist(user_id):
            return self.get(user_id)
        # Create user if not exist
        else:
            doc_id = self.create(user_id)
            return self.users.get(doc_id=doc_id)


if __name__ == "__main__":
    s = UserStorage()
    print(s.get_or_create(1))