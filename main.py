from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_hell0():
    return 'Hello world'
