from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root_a():
    return "this is root application"