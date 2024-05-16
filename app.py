import json
import random

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Load quotes from quotes.json
with open("quotes.json", "r") as f:
    quotes = json.load(f)

# Mount static directory for serving frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/{full_path:path}", response_class=HTMLResponse)
def get_random_quote(request: Request, full_path: str):
    random_quote = random.choice(quotes)
    if not full_path:
        name = ""
    else:
        name = full_path.title() + ",\n"
    # return random_quote  # Return the quote text directly as plain text
    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Centered Text</title>
            <link rel="stylesheet" href="/static/styles.css">
        </head>
        <body>
            <div id="text-container">
                <p id="centered-text">{name}</p>
                <p id="centered-text">{random_quote}</p>
            </div>
        </body>
        </html>
        """


# Run uvicorn server directly from __main__
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
