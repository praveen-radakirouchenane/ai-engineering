from fastapi import FastAPI, Body
from ollama import Client


app = FastAPI()
client = Client(
    host="http://localhost:11434/"
)


@app.get("/")
def say_hello():
    return {"msg":"Hi, Hello!"}

@app.get("/contact")
def contact_us():
    return {"msg":"contact us on this email address hi@contact.com."}

@app.post("/")
def ask_question(message:str = Body(..., description="Client message")
):
    response = client.chat(model="gemma:2b",
                messages=[
                    {"role":"user", "content":message}
                    ])
    return { "response": response.message.content }
    