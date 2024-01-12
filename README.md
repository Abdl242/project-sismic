# Earthquake Intensity and Location Prediction Project

## Overview
This project aims to predict earthquake intensity and potential locations using advanced data engineering and machine learning techniques. It involves a pipeline for real-time data processing and two machine learning models for predictive analytics.

## Pipeline Architecture
- Data Source: The data is sourced from a streaming data service using a publish/subscribe (pub/sub) model.
- Data Processing: Utilizing Google Cloud Dataflow, the streamed data is processed and then inserted into BigQuery for further analysis and storage.
Technology Stack: Key technologies used in this pipeline include Google Cloud Pub/Sub, Google Cloud Dataflow, and BigQuery.

## Machine Learning Models
### Earthquake Intensity Prediction Model
- Dataset: Historical earthquake data spanning from 1963 to 2023.
- Objective: To predict the intensity of earthquakes.
- Methodology: The model is trained on various features extracted from the historical data to predict the intensity of future earthquakes.
### Earthquake Location Prediction Model
- Current Status: This model is currently in the training phase.
- Objective: To predict potential locations of future earthquakes.
- Approach: The model is being designed to analyze seismic activity patterns and other relevant geographical features to predict possible earthquake locations.

## Usage
[Instructions on how to set up, configure, and use the pipeline and models.]

## Contributing
[Details on how others can contribute to the project, if applicable.]

## License
[Information about the project's licensing.]

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.