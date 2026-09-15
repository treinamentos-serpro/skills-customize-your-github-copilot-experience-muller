"""Starter code for the FastAPI REST API assignment.

Install the dependencies with:
    pip install fastapi uvicorn

Run the application with:
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI

app = FastAPI(title="Book API")

# TODO: Add a list of books and Pydantic models for the request and response data.


@app.get("/")
def read_root():
    """Return a welcome message from the API."""
    # TODO: Return a JSON object with a welcome message.
    pass


# TODO: Add GET /books to list all books.
# TODO: Add GET /books/{book_id} to retrieve one book.
# TODO: Add POST /books to create a book.
# TODO: Add PUT /books/{book_id} to update a book.
# TODO: Add DELETE /books/{book_id} to delete a book.
# TODO: Raise HTTPException with status_code=404 for unknown book IDs.
