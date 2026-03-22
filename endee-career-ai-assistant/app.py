from fastapi import FastAPI
from query import search

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Career Assistant running"}

@app.get("/ask")
def ask(question: str):
    answer = search(question)
    return {"question": question, "answer": answer}
