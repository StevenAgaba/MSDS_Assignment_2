## Agaba Steven. 
### Registration Number: S26M19/002. 
### Access Number: B38624

# Weather Forecast Application

## Overview

The Weather Forecast Application is a Python-based project that retrieves weather forecast information using the Open-Meteo APIs.

The application performs the following tasks:

1. Converts a user-specified location name into geographic coordinates using the Open-Meteo Geocoding API.
2. Retrieves weather forecast data using the Open-Meteo Forecast API.
3. Processes JSON responses and converts them into a Pandas DataFrame.
4. Displays weather forecasts in a user-friendly format.
5. Generates basic weather summary statistics.
6. Implements Object-Oriented Programming (OOP) principles and robust error handling.

---

## Objectives

The objectives of this project are to:

- Demonstrate the use of REST APIs in Python.
- Retrieve and process JSON data.
- Apply Object-Oriented Programming concepts.
- Implement error handling and retry mechanisms.
- Analyze weather data using Pandas.

---

## APIs Used

### Open-Meteo Geocoding API

Used to convert a location name into latitude and longitude coordinates.

```text
https://geocoding-api.open-meteo.com/v1/search
```

### Open-Meteo Weather Forecast API

Used to retrieve weather forecast data for specific coordinates.

```text
https://api.open-meteo.com/v1/forecast
```

---

## Features

- Geographic location lookup
- Weather forecast retrieval
- JSON data processing
- Pandas DataFrame creation
- Weather summary statistics
- Retry mechanism with exponential backoff
- Custom exception handling
- Modular OOP design

---

## Project Structure

```text
weather_project/
│
├── src/
│   └── weather_client.py
│
├── Weather_Forecast.ipynb
├── sample_weather.json
├── README.md
└── requirements.txt
```

---

## Technologies Used

- Python
- Jupyter Notebook
- Requests
- Pandas
- JSON
- Open-Meteo APIs

---

## Object-Oriented Design

The project uses the following classes:

### WeatherAPIClient

Responsible for:

- Geocoding location names
- Fetching weather forecasts
- Managing API requests
- Implementing retry logic

### WeatherAPIError

Custom exception used to handle API-related failures.

---

## Error Handling

The application implements:

- Request validation
- Custom exceptions
- Retry mechanism
- Exponential backoff strategy

This ensures the application can recover from temporary network or API failures.

---

## Data Processing

The weather forecast JSON response is transformed into a Pandas DataFrame containing:

- Date
- Maximum Temperature
- Minimum Temperature
- Rainfall

The application also calculates:

- Average Maximum Temperature
- Average Minimum Temperature
- Total Rainfall

---

## Running the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Open Jupyter Notebook

```bash
jupyter notebook
```

### 3. Open the Notebook

```text
Weather_Forecast.ipynb
```

### 4. Run All Cells

From the Jupyter menu:

```text
Kernel → Restart & Run All
```

---

## Sample Output

The application:

- Retrieves coordinates for a location.
- Retrieves daily weather forecasts.
- Displays forecast data in tabular form.
- Calculates weather summary statistics.
- Saves a sample JSON response to:

```text
sample_weather.json
```

---

## Privacy Considerations

The project uses publicly available Open-Meteo APIs and does not require personal user information.

Only the location name provided by the user is submitted to the API service.

---

## AI Assistance Declaration

Microsoft Copilot was used to:

- Explain assignment requirements
- Assist with debugging
- Suggest project organization and structure
- Explain Object-Oriented Programming concepts

All code was reviewed, tested, and understood by the author prior to submission.

---

## Author

Steven Agaba

Monitoring SC G

Kampala, Uganda

