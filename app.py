from flask import Flask, request
import os
import zipfile
import smtplib
from email.message import EmailMessage


app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Mashup Generator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: white;
            }
            .box {
                width: 400px;
                margin: 120px auto;
                padding: 20px;
                border: 1px solid black;
            }
            h2 {
                text-align: center;
                margin-bottom: 20px;
            }
            input {
                width: 100%;
                padding: 6px;
                margin-top: 5px;
                margin-bottom: 12px;
            }
            button {
                background: orange;
                border: none;
                padding: 8px;
                width: 100%;
                cursor: pointer;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h2>Mashup Generator</h2>

            <form action="/create" method="post">
                Singer Name:
                <input name="singer" required>

                Number of Videos:
                <input name="count" required>

                Duration (seconds):
                <input name="duration" required>

                Email:
                <input name="email" required>

                <button type="submit">Submit</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route("/create", methods=["POST"])
def create():
    singer = request.form["singer"]
    count = int(request.form["count"])
    duration = int(request.form["duration"])
    email = request.form["email"]
    return f"Processing mashup for {singer}. File will be sent to {email}"



if __name__ == "__main__":
    app.run(debug=True)
