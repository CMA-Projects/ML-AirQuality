from dataclasses import field
import requests
import os
import csv

# Google Maps API key (replace with your own key)
api_key = 'AIzaSyBSJL1d-xJz4pOfAw64rRI4bqnb9nHon7w'

# Zoom level and image size
zoom_level = 19
image_size = '600x300'

# 
coordinates_list = [(31.128750, 121.432415), 
                    (31.125760, 121.419155), 
                    (31.058295, 121.149336),
                    (31.120104, 121.324637),
                    (31.104103, 121.618877),
                    (31.022991, 121.570945),
                    (30.981937, 121.721032),
                    (31.054041, 121.143287),
                    (31.054981, 121.152121),
                    (31.263566, 121.298869),
                    (31.252342, 121.304740),
                    (31.158357, 121.656052),
                    (31.059909, 121.778977),
                    (31.058631, 121.776603),
                    (31.035842, 121.752543),
                    (30.979443, 121.764994),
                    (30.966342, 121.736733),
                    (31.374595, 121.312414),
                    (31.354323, 121.298653),
                    (31.334044, 121.272441)
                    ]

aqi_list = [82, 
            82, 
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            82,
            ]

file_names = []

# Specify satellite view
map_type = 'satellite'

file_names = []  # Initialize an empty list to store file names

# Iterate through the coordinates list
for i, (latitude, longitude) in enumerate(coordinates_list):
    # Construct the API request URL with satellite view
    api_url = f'https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom={zoom_level}&size={image_size}&maptype={map_type}&key={api_key}'

    # Send HTTP request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Specify the folder to save the image
        save_folder = os.path.join(os.getcwd(), 'screenshots')  # Use os.getcwd() to get the current working directory

        # Create the folder if it doesn't exist
        os.makedirs(save_folder, exist_ok=True)

        # Save the image to the folder
        image_path = os.path.join(save_folder, f'satellite_screenshot_{i}_AQI_{aqi_list[i]}.png')
        with open(image_path, 'wb') as f:
            f.write(response.content)
        
        # Append file name to list
        file_names.append(f'satellite_screenshot_{i}_AQI_{aqi_list[i]}.png')

        print(f'Satellite screenshot {i} saved to: {image_path}')
    else:
        print(f'Error: Unable to fetch the image. Status code: {response.status_code}')

# Now, 'file_names' list contains the names of the saved images


# Create the csv file of the data
# Adjust the paths based on the location of your code
#base_directory = os.path.dirname(__file__)
#data_directory = os.path.join(base_directory,'data')
#os.makedirs(data_directory, exist_ok=True)
#csv_file_path = os.path.join(data_directory, 'aqi_data2.csv')
csv_file_path = 'data/aqi_data2.csv'
with open(csv_file_path, 'w', newline = '') as csvfile:
    fieldnames = ['File_Name', 'AQI']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    for file_name, aqi in zip(file_names, aqi_list):
        writer.writerow({'File_Name': file_name, 'AQI': aqi})

print(f'CSV file created: {csv_file_path}')