import os

from flask import Flask

from groq import Groq

from dotenv import load_dotenv, find_dotenv

from pathlib import Path

load_dotenv(Path(".env"))

app = Flask(__name__)

#@app.route("/members")
#def members():
#    return {"members": ["Member1", "Member2", "Member3"]}

#if __name__ == "__main__":
#    app.run(debug=True)

client = Groq(
    api_key=(os.getenv("GROQ_API_KEY")),
)

monthly_expenses = {
    "rent": 0,
    "home insurance": 0,
    "car insurance": 0,
    "transportation": 0,
}

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Give financial advice based on this data: ".join(f"{k}:{v}" for k, v in monthly_expenses.items()),
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)