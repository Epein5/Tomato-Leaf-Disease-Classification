from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from typing import List
import uvicorn
from io import BytesIO
from predict import predict_image
import os
import sys

# Get the path of the parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Image Classification API"}


@app.post("/classify_image")
async def classify_image_endpoint(image: UploadFile = File(...)):
    # Read the image data
    image_data = await image.read()

    # Make predictions
    predicted_class = predict_image(BytesIO(image_data))

    # Return the predicted class
    return {"predicted_class": predicted_class}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)