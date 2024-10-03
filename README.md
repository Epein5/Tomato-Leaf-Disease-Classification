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

4. Download the dataset from [Tomato Leaf Disease Detection on Kaggle](https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf) and place it in the `Datasets` folder.

5. Correct the paths to the Datasets and train the Model using the code in ML/train.ipynb.

6. Add your ML model to the `ML` folder and change the paths in the code to point to your model.

7. Navigate to the main directory and run the following command to start the application:

       uvicorn BACKEND.main:app
   
Now you should be able to access the API on your web browser on:

      http://127.0.0.1:8000/docs

8. If you want to dockerize the the application download and install docker in your desktop run the following command in the terminal.

          docker build -t <your_docker_image_name> .
   
10. Now you can create the docker container manually through the docker desktop or run the command in the terminal to run the container:

           docker run -p 8000:8000 <your_docker_image_name>

11. To publish on the docker hub.

    First Create a new docker tag using the following command:
    
           docker tag <your_docker_image_name> <your_username>/<your_docker_image_name>:v1.0

    Then push the tag to the docker hub:

           docker push <your_username>/<your_docker_image_name>:v1.0

12. Now your docker image is ready to be shared and hosted in different platforms

### The pictures below showcase the results of the project when hosted on Azure.

## Project Images

<p float="left">
  <img src="https://github.com/Epein5/Tomato-Leaf-Disease-Classification/assets/110723354/a23b2f49-dea1-4aa3-91ff-af9cf45cd064" width="48%" />
  <img src="https://github.com/Epein5/Tomato-Leaf-Disease-Classification/assets/110723354/c6153ffb-2209-41c6-b828-fb9a2f4a67de" width="48%" />
</p>
<p float="left">
  <img src="https://github.com/Epein5/Tomato-Leaf-Disease-Classification/assets/110723354/539c128b-0151-4bd9-a1bf-1f69d19205e2" width="48%" />
  <img src="https://github.com/Epein5/Tomato-Leaf-Disease-Classification/assets/110723354/8fd52919-18fa-4410-b58d-21ce99b7e138" width="48%" />
</p>



## Video Demonstration

[![Demo Video](https://img.youtube.com/vi/aBMZkS6D_xo/0.jpg)](https://www.youtube.com/watch?v=aBMZkS6D_xo)

Click the image above to watch the demo video.
