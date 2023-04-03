import pytest


class User:
    def __init__(self, age=42) -> None:
        self.age = age or 42


    def remove(self):
        self.age = None



@pytest.fixture(scope="session")
def user():
    # before test
    print("Create user")
    user = User(42)

    #pass user object test
    yield user 

    #after test
    print("Remove user")
    user.remove()





