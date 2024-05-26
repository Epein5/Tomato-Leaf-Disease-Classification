from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from typing import List
import uvicorn
from io import BytesIO
from .predict import predict_image
import os
import sys
from .data import disease_data  # Import the disease data

# Get the path of the parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory to the Python path 
sys.path.append(parent_dir)

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Image Classification API"}

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

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

    # Fetch disease information
    disease_info = disease_data.get(predicted_class, {"Description": "Unknown", "Prevention_measures": "Unknown"})

    # Return the predicted class and disease information
    return {
        "predicted_class": predicted_class,
        "disease_info": disease_info
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)