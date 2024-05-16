from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import json
import random
import uvicorn

app = FastAPI()

# Load quotes from quotes.json
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

# Mount static directory for serving frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def get_random_quote():
    random_quote = random.choice(quotes)
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
                <p id="centered-text">{random_quote}</p>
            </div>
        </body>
        </html>
        """

# Run uvicorn server directly from __main__
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
