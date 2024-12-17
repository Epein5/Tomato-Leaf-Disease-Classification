from fastapi import FastAPI, File, UploadFile, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
import uvicorn
from io import BytesIO
from .predict import predict_image
import os
import sys
import google.generativeai as genai
from .data import disease_data  # Import the disease data

# Get the path of the parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory to the Python path 
sys.path.append(parent_dir)

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="Static"), name="static")

chat_history = []
predicted_classs = []
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to the Image Classification API"})

@app.get("/info", response_class=HTMLResponse)
async def read_info(request: Request):
    return templates.TemplateResponse("index2.html", {"request": request})

@app.get("/classify", response_class=HTMLResponse)
async def read_info(request: Request):
    return templates.TemplateResponse("index3.html", {"request": request})

@app.post("/classify_image")
async def classify_image_endpoint(image: UploadFile = File(...)):
    # Read the image data
    image_data = await image.read()

    # Make predictions
    predicted_class = predict_image(BytesIO(image_data))
    predicted_classs.append(predicted_class)
    if len(predicted_classs) > 1:
        predicted_classs.pop(0)
        chat_history.clear()

    # Fetch disease information
    disease_info = disease_data.get(predicted_class, {"Description": "Unknown", "Prevention_measures": "Unknown"})

    # Return the predicted class and disease information
    return {
        "predicted_class": predicted_class,
        "disease_info": disease_info,
        "chat_history": chat_history  # Include chat history in the response
    }

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    print(data)
    message = data.get("message")

    # Configure and use the Gemini API to get a response
    gemini_api_key = 'YOUR GEMINI API HERE'
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Create a prompt that includes chat history and predicted class
    prompt = f"Chat history: {chat_history}\nPredicted class: {predicted_classs}\nUser query: {message}"
    print(prompt)

    response = model.generate_content(prompt)
    reply = response.text if response else "Sorry, I couldn't understand that."

    # Save chat history
    chat_history.append({"user": message, "system": reply})

    return {"reply": reply, "chat_history": chat_history}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)