from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

import json
import random
import uvicorn

app = FastAPI()

# Load quotes from quotes.json
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

@app.get('/quote', response_class=PlainTextResponse)
def get_random_quote():
    random_quote = random.choice(quotes)
    return random_quote  # Return the quote text directly as plain text

# Run uvicorn server directly from __main__
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
