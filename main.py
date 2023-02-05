from fastapi import FastAPI, Path
from typing import Optional

dummy_data = {
    1: {
        "Title": "Crime and Punishment",
        "Author": "Fedor Dostoefieldsky",
        "Price:": 10.12
    },
    2: {
        "Title": "Complete Poetry of Edgar Allan Poe",
        "Author": "Edgar Allan Poe",
        "Price:": 4.99
    },
    3: {
        "Title": "Pride and Prejustice",
        "Author": "Jane Austen",
        "Price:": 5.99
    },
    4: {
        "Title": "To Kill a Mockingbird",
        "Author": "Harper Lee",
        "Price:": 9.99
    }
}

min_id = min(dummy_data.keys())
max_id = max(dummy_data.keys())

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/about")
def about():
    return {"info": "This API is exremely useful and cool"}

@app.get("/catalog")
def get_all_items():
    return dummy_data

@app.get("/catalog/id/{item_id}")
def get_item_by_id(item_id: int = Path(None, description="An ID of the item in a catalog", ge=min_id, le=max_id)):
    return dummy_data[item_id]

@app.get("/catalog/query")
def get_item_by_author(name: Optional[str] = None):
    for _, inner in dummy_data.items():
        if inner["Author"] == name:
            return inner
    return {"error": "Not Found"}
