import requests
import os
import pandas as pd

# Google Maps API key
api_key = 'AIzaSyBSJL1d-xJz4pOfAw64rRI4bqnb9nHon7w'

# Parameters for Google Maps API
zoom_level = 19
image_size = '600x300'
map_type = 'satellite'

# Function to read coordinates and AQI data from a CSV file using pandas
def read_coordinates_aqi(csv_file_path):
    try:
        df = pd.read_csv(csv_file_path)
        # Convert the list to a dictionary
        return df.to_dict(orient='records')
    except FileNotFoundError:
        print(f'Error: CSV file not found at path {csv_file_path}')
        return []

# Function to take a screenshot using Google Maps API
def take_screenshot(api_key, latitude, longitude, zoom_level, image_size, map_type, index, aqi):
    api_url = f'https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom={zoom_level}&size={image_size}&maptype={map_type}&key={api_key}'
    response = requests.get(api_url)

    if response.status_code == 200:
        save_folder = os.path.join(os.getcwd(), 'screenshots')
        os.makedirs(save_folder, exist_ok=True)

        image_path = os.path.join(save_folder, f'satellite_screenshot_{index}_AQI_{aqi}.png')
        with open(image_path, 'wb') as f:
            f.write(response.content)

        print(f'Satellite screenshot {index} saved to: {image_path}')
        return image_path
    else:
        print(f'Error: Unable to fetch the image. Status code: {response.status_code}')
        return None

# Function to update a CSV file with file names and AQI data using pandas
def update_csv(file_names, aqi_list, csv_file_path):
    df = pd.DataFrame({'File_Name': file_names, 'AQI': aqi_list})
    df.to_csv(csv_file_path, index=False)
    print(f'CSV file updated: {csv_file_path}')

# Main function
def main():
    # Read coordinates and AQI data from the CSV file
    csv_file_path = 'data_to_retrieve.csv'
    coordinate_aqi_data = read_coordinates_aqi(csv_file_path)

    # Initialize empty lists
    file_names = []
    aqi_list = []

    # Iterate through the coordinates list
    for i, row in enumerate(coordinate_aqi_data):
        latitude = float(row['Latitude'])
        longitude = float(row['Longitude'])
        aqi = int(row['AQI'])

        # Take screenshot and get the image path
        screenshot_path = take_screenshot(api_key, latitude, longitude, zoom_level, image_size, map_type, i, aqi)

        # Update lists
        if screenshot_path:
            file_names.append(os.path.basename(screenshot_path))
            aqi_list.append(aqi)

    # Update the CSV file using pandas
    csv_file_path = 'data/aqi_data2.csv'
    update_csv(file_names, aqi_list, csv_file_path)

if __name__ == "__main__":
    main()
