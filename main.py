from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def greet():
    return {"welcome to fast api class"}


@app.get("/hello")
def greet_with_name():
    return "hello pramod"
