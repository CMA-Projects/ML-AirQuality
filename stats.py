import numpy as np

predicted_aqi_values = [55.17, 75.52, 57.31, 63.44, 61.50, 62.26, 60.60, 73.67, 46.11]

std_deviation = np.std(predicted_aqi_values)

mean_aqi = np.mean(predicted_aqi_values)

n = len(predicted_aqi_values)
z_score = 1.96
confidence_interval = z_score * (std_deviation/ np.sqrt(n))

lower_bound = mean_aqi - confidence_interval
upper_bound = mean_aqi + confidence_interval

print(f"Mean AQI: {mean_aqi}")
print(f"Standard Deviation: {std_deviation}")
print(f"95% Confidence Interval: {confidence_interval}")