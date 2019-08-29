from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class HelloMessage(BaseModel):
    message: str


@app.get('/hello')
def say_hello(name: str):
    if name:
        return HelloMessage(message='Hello, {0}'.format(name))
    return HelloMessage(message='Hello, Who are you?')

