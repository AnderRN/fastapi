from pydantic import basemodel

class User (basemodel):
    username: str
    email: str
    password: str