from typing import Optional

from fastapi import FastAPI, Path
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    price: float

dummy_data: dict[int, Book] = {
    1: Book(title="Crime and Punishment", author="Fedor Dostoevsky", price=10.12),
    2: Book(title="Complete Poetry of Edgar Allan Poe", author="Edgar Allan Poe", price=4.99),
    3: Book(title="Pride and Prejustice", author="Jane Austen", price=5.99),
    4: Book(title="To Kill a Mockingbird", author="Harper Lee", price=9.99)
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
    item_id: int = Path(None, description="An ID of the item in a catalog", gt=0)
):
    return dummy_data[item_id]


@app.get("/catalog/query")
async def get_item_by_author(name: Optional[str] = None):
    for _, inner in dummy_data.items():
        if inner.author == name:
            return inner
    return {"error": "Not Found"}


@app.post("/catalog/new/{item_id}")
async def create_new_book(book: Book, item_id: int = Path(None, gt=0)):
    if item_id not in dummy_data:
        dummy_data[item_id] = book
    else:
        return {"error": "This ID already exists"}
    return dummy_data[item_id]

@app.put("/catalog/edit/{item_id}")
async def edit_book(book: Book, item_id: int):
    dummy_data[item_id] = book
    return dummy_data[item_id]