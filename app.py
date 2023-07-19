from flask import Flask

app = Flask(__name__)

@app.get("/welcome")
def welcome_message():
    """prints welcome message"""
    return "<h1>welcome</h1>"

@app.get("/welcome/home")
def home_welcome_message():
    """prints 'welcome home' message"""
    return "<h1>welcome home</h1>"

@app.get("/welcome/back")
def welcome_back_message():
    """prints 'welcome back' message"""
    return "<h1>welcome back</h1>"

