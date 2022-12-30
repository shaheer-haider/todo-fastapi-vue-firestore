from database import db_collection
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from models import DeleteTodoModel, TodoModel
from uuid import uuid4
from publisher import publish

# # # # # CLOUD ALERT # # # # #
data = "<h1>The Server has been started</h1>"
publish(data)


# # # # # ROUTES # # # # #

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/write-todo")
async def write_todo(todo: TodoModel):
    id = str(uuid4())
    doc_ref = db_collection.document(id)
    doc_ref.set({"name": todo.name, "description": todo.description, "id": id})  # type: ignore
    message = f"""
    <h1>A Task has been Added</h1>
    <h4>Name: {todo.name}</h4>
    <h4>Description: {todo.description}</h4>
    """
    publish(message)
    return 200


@app.get("/read-todo")
async def read_todo():
    todo = db_collection.get()
    doc = [el.to_dict() for el in todo]
    return doc


@app.post("/delete-todo")
async def delete_todo(data: DeleteTodoModel):
    doc_ref = db_collection.document(data.id)
    doc_ref.delete()
    return 200
