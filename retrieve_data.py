from dataclasses import field
import requests
import os
import csv

# Google Maps API key (replace with your own key)
api_key = 'AIzaSyBSJL1d-xJz4pOfAw64rRI4bqnb9nHon7w'

# Zoom level and image size
zoom_level = 18
image_size = '600x300'

# 
coordinates_list = [(31.263078, 121.211594), 
                    (32.123456, 120.987654), 
                    (30.567890, 122.345678),
                    (31.120104, 121.324637),
                    (31.104103, 121.618877),
                    (31.022991, 121.570945),
                    (30.981937, 121.721032),
                    ]

aqi_list = [50, 
            75, 
            90,
            82,
            82,
            82,
            82]

file_names = []

# Specify satellite view
map_type = 'satellite'

# Iterate through the coordinates list
for i, (latitude, longitude) in enumerate (coordinates_list):
    # Construct the API request URL with satellite view
    api_url = f'https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom={zoom_level}&size={image_size}&maptype={map_type}&key={api_key}'

    # Send HTTP request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Specify the folder to save the image
        save_folder = 'screenshots'

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

# Create the csv file of the data
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