from fastapi import FastAPI, Path
from typing import Optional

from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    price: float


dummy_data = {
    # 1: {
    #     "Title": "Crime and Punishment",
    #     "Author": "Fedor Dostoefieldsky",
    #     "Price:": 10.12,
    # },
    # 2: {
    #     "Title": "Complete Poetry of Edgar Allan Poe",
    #     "Author": "Edgar Allan Poe",
    #     "Price:": 4.99,
    # },
    # 3: {
    #     "Title": "Pride and Prejustice",
    #     "Author": "Jane Austen",
    #     "Price:": 5.99
    # },

    # 4: {
    #     "Title": "To Kill a Mockingbird",
    #     "Author": "Harper Lee",
    #     "Price:": 9.99
    # },
}

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/about")
async def about():
    return {"info": "This API is exremely useful and cool"}


@app.get("/catalog")
async def get_all_items():
    return dummy_data


@app.get("/catalog/id/{item_id}")
async def get_item_by_id(
    item_id: int = Path(
        None,
        description="An ID of the item in a catalog",
        gt=0
    )
):
    return dummy_data[item_id]


@app.get("/catalog/query")
async def get_item_by_author(name: Optional[str] = None):
    for _, inner in dummy_data.items():
        if inner["Author"].name == name:
            return inner
    return {"error": "Not Found"}


@app.post("/catalog/new/{item_id}")
async def create_new_book(
    book: Book, item_id: int = Path(None, gt=0)
):
    if item_id not in dummy_data:
        dummy_data[item_id] = book
    else:
        return {"error": "This ID already exists"}
    return dummy_data[item_id]
