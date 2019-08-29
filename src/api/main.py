from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from time import sleep
app = FastAPI()


class HelloMessage(BaseModel):
    message: str


class NumbersMessage(BaseModel):
    numbers: List[int] = []

@app.get('/hello')
def say_hello(name: str =None):
    if name:
        return HelloMessage(message='Hello, {0}'.format(name))
    return HelloMessage(message='Hello, Who are you?')


@app.get('/count')
def count(num: int):
    nums = [num for num in range(0, num)]
    return NumbersMessage(numbers=nums)
