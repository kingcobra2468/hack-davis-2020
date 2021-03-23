# Greenify

## Inspiration
While at Davis, we noticed that many students still take the car to school even when there is a reliable bus system and accessibility for the bicycle's around the town. We feel that this is due to the lack of scope in regards to how every trip impacts the environment and ones health. Thus, we felt something must be done.

## What It Does

![Alt text](/screenshots/search_screen.png "Client Web App")
Greenify's web application takes in user input for the start and end destination. It displays different possible routes, showing the environmental and health impacts of these routes.

![Alt text](/screenshots/transit_query.png "Client Web App")

As seen from the above route, relying on transit would have a high CO2 emission and little beneficial impact on a person's health.

![Alt text](/screenshots/cycling_query.png "Client Web App")

However, the same route on a bike would be a great workout and also prevent a negative impact on the environment.

## Installation Steps 

1. Get python3 on your system.
2. Install necessary packages with `pip3 install -r requirements.txt`.
3. Setup Google Cloud account to get API key. Then enable api access for the following API's (*Note for some of these API's to work, billing must be enabled*):
   - Directions API
   - Geocoding API 
   - Maps JavaScript API 
   - Places API 
4. Configure `config.py` by adding your API key and changing necessary sever metadata like port of ip address.
5. Run server with `python3 run.py` and go onto the appropriate url.