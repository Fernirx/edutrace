from fastapi import FastAPI

app = FastAPI(
    title="EduTrace API",
    version="0.1.0"
)

@app.get("/")
def home():
    return "Welcome to EduTrace Api"