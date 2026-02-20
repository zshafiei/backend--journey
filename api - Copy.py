from fastapi import FastAPI
import os

app = FastAPI()

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return file.read().splitlines()

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

@app.get("/")
def read_root():
    return {"message": "Task API is running 🚀"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    save_tasks(tasks)
    return {"message": "Task added", "tasks": tasks}
