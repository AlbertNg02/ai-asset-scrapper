
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
from io import BytesIO
uri = "mongodb+srv://admin_albert:binbin300502@cluster0.cj28qq4.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

image_urls = ["https://cdn.leonardo.ai/users/3e02ee10-773f-4ea3-b69a-ca8536a3da92/generations/6d99e409-b758-46e8-9e71-f7d82c1d9602/DreamShaper_v7_a_delicious_triple_meat_burger_with_bacon_and_y_1.jpg", "https://cdn.leonardo.ai/users/b4c9db97-65e9-472e-8dd7-8c6d4a89789d/generations/19af9b99-0cb2-4970-a89a-380d88532b73/DreamShaper_v6_Vietnamese_girl_primary_colors_with_white_highl_1.jpg", "https://cdn.leonardo.ai/users/8b6a7ae6-02c5-42f6-a05d-53767a6f610c/generations/f1f1a693-3b7f-460b-bad2-de0c43f564dd/RPG_40_Waist_high_Portrait_of_an_exotic_beautiful_caucasian_wo_3.jpg"]

import json

# Read the JSON file
import json

image_data = []

with open('extrac2.json', 'r') as file:
    data = json.load(file)

    # Extract the "src" values from each object
    src_list = [item['src'] for item in data]

    # Print the extracted src values
    for src in src_list:
        image_data.append(src)


# Loop through the image URLs
for url in image_data:
    # Download the image
    response = requests.get(url)
    if response.status_code == 200:
        # Convert the image data to binary
        image_data = BytesIO(response.content).read()

        # Save the image to the MongoDB database
        client.your_database_name.your_collection_name.insert_one({'image': image_data})
        print("Uploaded image:", url)
    else:
        print("Failed to download image:", url)