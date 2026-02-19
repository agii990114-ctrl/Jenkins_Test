from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World22", "Status": "Jenkins Build Success!"}
