from fastapi import FastAPI

dummy_data = {
    1: {
        "Title": {"Crime and Punishment"},
        "Author": {"Fedor Dostoevsky"},
        "Price:": {10.12}
    },
    2: {
        "Title": {"Complete Poetry of Edgar Allan Poe"},
        "Author": {"Edgar Allan Poe"},
        "Price:": {4.99}
    },
    3: {
        "Title": {"Pride and Prejustice"},
        "Author": {"Jane Austen "},
        "Price:": {5.99}
    },
    4: {
        "Title": {"To Kill a Mockingbird"},
        "Author": {"Harper Lee "},
        "Price:": {9.99}
    }
}

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/about")
def about():
    return {"info": "This API is exremely useful and cool"}

@app.get("/catalog/{item_id}")
def get_item_by_id(item_id: int):
    return dummy_data[item_id]