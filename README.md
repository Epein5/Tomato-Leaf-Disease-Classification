# Tomato Leaf Classification with Dockerization and Azure Deployment

This is a project on Tomato leaf classification with dockerization and deployment in Azure.

Our classes are:

- Tomato___Bacterial_spot
- Tomato___Early_blight
- Tomato___healthy
- Tomato___Late_blight
- Tomato___Leaf_Mold
- Tomato___Septoria_leaf_spot
- Tomato___Spider_mites Two-spotted_spider_mite
- Tomato___Target_Spot
- Tomato___Tomato_mosaic_virus
- Tomato___Tomato_Yellow_Leaf_Curl_Virus

## How to set up

1. Clone the repository:

       git clone https://github.com/your-repo/tomato-leaf-classification.git
2. Install the requirements using the `requirements.txt` file:


       pip install -r requirements.txt
3. Create the following folders:
   - `Datasets`: This folder will contain your dataset.
   - `ML`: This folder is where you should add your ML model.

4. Download the dataset from [Tomato Leaf Disease Detection on Kaggle](https://www.kaggle.com/datasets/arjunbhasin2013/tomato-leaf-disease-detection) and place it in the `Datasets` folder.

5. Add your ML model to the `ML` folder and change the paths in the code to point to your model.

6. Navigate to the main directory and run the following command to start the application:

       uvicorn BACKEND.main:app
   
Now you should be able to access the API on your web browser on:

      http://127.0.0.1:8000/docs
