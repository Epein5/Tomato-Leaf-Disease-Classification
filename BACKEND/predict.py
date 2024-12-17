import torch
import torch.nn as nn
import numpy as np
from PIL import Image
from torchvision import transforms

# Define the CNN architecture
class PlantVillageCNN(nn.Module):
    def __init__(self):
        super(PlantVillageCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 16, 3, padding=1)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.conv3 = nn.Conv2d(16, 8, 3, padding=1)
        self.pool3 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(8 * 16 * 16, 128)
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool1(nn.functional.relu(self.conv1(x)))
        x = self.pool2(nn.functional.relu(self.conv2(x)))
        x = self.pool3(nn.functional.relu(self.conv3(x)))
        x = x.view(-1, 8 * 16 * 16)
        x = nn.functional.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

# Load the trained PyTorch model
model = PlantVillageCNN()

try:
    model.load_state_dict(torch.load('/media/epein5/Data/Tomato-Leaf-Disease-Classification/ML/sequential_model.pth'))
    # model.load_state_dict(torch.load('/app/ML/sequential_model.pth'))
except:
    print("Model not found")

model.eval()

# Define the class labels
class_labels = ['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy',
                'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
                'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
                'Tomato___Tomato_mosaic_virus', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus']

# Define the image preprocessing transforms
preprocess = transforms.Compose([
    transforms.Resize(128),
    transforms.CenterCrop(128),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def predict_image(image_data):
    # Load and preprocess the image data
    img = Image.open(image_data)
    img = preprocess(img)
    img = img.unsqueeze(0)  # Add batch dimension

    # Make the prediction
    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs.data, 1)

    # Get the predicted class label
    predicted_class = class_labels[predicted.item()]

    return predicted_class