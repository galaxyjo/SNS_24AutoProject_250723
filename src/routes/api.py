# 📄 src/routes/api.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "SNS Auto Project API Root"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": "0.0.0"}
