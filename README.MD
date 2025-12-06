# US Weather App CLI
[![Tests](https://github.com/chuck-w-moore/is4010-final-weather-app/actions/workflows/python-app.yml/badge.svg)]
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python command-line application using an interactive interface to fetch and display real-time weather forecasts for United States cities using a Dual-API architecture.

## Overview

This tool provides an interactive interface to query weather data without needing to know geographic coordinates. Users simply enter a city name (e.g., "Cincinnati, OH"), and the application automatically resolves the location and fetches the latest forecast from the National Weather Service.

## Features

* **Interactive Interface:** A user-friendly, loop-based CLI that allows continuous searching without restarting the app.
* **Smart Geocoding:**
    * Users can input city names ("Miami, FL") instead of raw coordinates.
    * Automatically converts city names to Latitude/Longitude using OpenStreetMap.
* **Dual-API Integration:** Orchestrates data flow between the Nominatim API (Location) and the NWS API (Weather).
* **Detailed Forecasts:** Displays temperature, wind speed/direction, and short forecast descriptions in a formatted table.
* **Built-in Validation:** Ensures coordinates are within US boundaries and handles API errors (403/404) gracefully.
* **Custom User-Agent:** Implements compliant headers to ensure reliable API access.

## API Information

This project integrates two distinct public APIs:

1.  **OpenStreetMap (Nominatim):** Used for Geocoding (City -> Lat/Lon).
    * Endpoint: `https://nominatim.openstreetmap.org/search`
2.  **National Weather Service (NWS):** Used for weather grid and forecast data.
    * Endpoint: `https://api.weather.gov/points/{lat},{lon}`

## Installation

Follow these steps to set up the project locally.

**Prerequisites:**

* Python 3.10 or higher installed.
* Git installed.

**Steps:**

1.  **Clone the repository:** Open your terminal and navigate to where you want to store the project.
    ```bash
    git clone <your-repo-url-here>
    cd weather-cli-app
    ```

2.  **Create and activate a virtual environment:** Highly recommended to isolate dependencies.
    ```bash
    python -m venv venv
    ```
    * **On Windows:** `venv\Scripts\activate`
    * **On macOS/Linux:** `source venv/bin/activate`

3.  **Install required dependencies:**
    ```bash
    pip install requests tabulate pytest pytest-mock
    ```

## Usage

This application is designed to be run from the project root.

**Starting the Application:**

Ensure your virtual environment is active, then run:

```bash
python main.py
```
**Example Usage**

Enter a US City (e.g., 'Miami, FL'): Austin, TX
Searching for 'Austin, TX'...
Found: Austin, Travis County, Texas, United States

The forecast for Austin, Travis County, Texas, United States:

| Period         | Temp   | Wind      | Forecast                          |
| :------------- | :----- | :-------- | :-------------------------------- |
| This Afternoon | 75 F   | 5 mph S   | Sunny                             |
| Tonight        | 55 F   | 10 mph SW | Mostly Clear                      |

## License

Please review the license file to view the license.