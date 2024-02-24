# coordinates_aqi_lists.py
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

import csv

# Your coordinates_list
coordinates_list = [
    (31.128750, 121.432415),
    (31.125760, 121.419155),
    # ... (rest of the coordinates)
]

# Specify the CSV file path
csv_file_path = 'coordinates.csv'

# Write the coordinates_list to the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Latitude', 'Longitude']
    writer = csv.writer(csvfile)
    
    # Write the header
    writer.writerow(fieldnames)
    
    # Write the data
    writer.writerows(coordinates_list)

print(f'CSV file created: {csv_file_path}')