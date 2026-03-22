from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from query import search

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Career Assistant running"}

@app.get("/ask")
def ask(question: str):
    response = search(question)
    return response
