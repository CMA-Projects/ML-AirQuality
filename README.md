# Air Quality Project

## Overview
The project's primary objective is to leverage Google Street View images for the development of a machine learning model designed to predict air quality. The utilization of Google Street View images introduces a unique approach to environmental data collection, as it allows for the extraction of valuable information from the visual cues present in these images. 

Key components and goals of the project:

1. **Data Source:** Google Street View images serve as the primary data source for this project. These images capture real-world scenes, including various environmental features and urban landscapes that may provide insights into factors influencing air quality.

2. **Feature Extraction:** The project involves extracting relevant features from the Street View images. These features could include characteristics such as the density of vegetation, types of vehicles, presence of industrial facilities, and overall urban infrastructure. Machine learning algorithms will then use these features to make predictions about air quality.

3. **Machine Learning Model:** A machine learning model will be developed and trained using the extracted features from the Street View images. The goal is to create a model capable of predicting air quality levels based on visual cues present in the images. This could involve classification into different air quality categories or regression to estimate specific air quality indices.

4. **Training Data:** The model will be trained on a dataset that includes both Street View images and corresponding air quality measurements. This dataset serves as the foundation for teaching the model to recognize patterns and relationships between visual features and air quality levels.

5. **Validation and Testing:** The developed model will undergo rigorous validation and testing phases to ensure its accuracy and generalizability. This involves assessing its performance on new, unseen data to confirm its ability to make reliable predictions beyond the training set.

6. **Application:** Once the model proves effective, it can be applied to predict air quality in locations where Street View images are available. This application could have practical implications for urban planning, public health, and environmental monitoring.

7. **Continuous Improvement:** The project may also include provisions for continuous improvement. This involves refining the model based on additional data, feedback, and advancements in machine learning techniques to enhance its predictive capabilities over time.

#### Packages for .ipynb
```
!pip install numpy
!pip install pandas
!pip install opencv-python
!pip install Pillow 
!pip install tensorflow
!pip install matplotlib
!pip install scikit-learn
```
**Pillow** is an image processing library that extends from Python Imaging Library (PIL). For resizing images, filters and image formats.<br>
**opencv-python** is used for computer vision and image processing (Open Source Computer Vision Library). Provides tools and functions for image/video analysis, object detection and more<br>
**tensorflow** is an open-source machine learning framework from Google. Provides tools for building and training machine learning models, especially deep NN

## Progress Log
- **2024.02.17** Cleaned retrieve_data.py
    - Plan on separating the lists onto a different file to make it easier
- **2024.02.23** Changed a lot of the data
    - Coordinates that we want to take screenshots of are now on a separate csv file
    - .py was reorganized into functions to make more modular
    - .py was changed to use pandas instead of csv
    - Renamed files more appropriately
    - Next time we just need to collect more data and organize file names more

## References
AQI [Source 1](https://sthj.sh.gov.cn/kqzlssfb/index.html)

AQI [Source 2](https://www.qweather.com//air/hongkou-101021600.html)