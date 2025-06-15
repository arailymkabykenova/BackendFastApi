import requests
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Data
from app.worker import celery
import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)

@celery.task
def fetch_data():
    try:
        # Get API key from environment variable
        api_key = os.getenv('OPENWEATHER_API_KEY')
        if not api_key:
            logger.error("OpenWeather API key not found")
            return False

        # Example: Fetch weather data for New York
        city = "New York"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        
        # Process the data
        data = {
            'title': f"Weather in {city}",
            'content': f"Temperature: {weather_data['main']['temp']}°C, "
                      f"Description: {weather_data['weather'][0]['description']}, "
                      f"Humidity: {weather_data['main']['humidity']}%, "
                      f"Wind Speed: {weather_data['wind']['speed']} m/s"
        }
        
        # Save to database
        db = next(get_db())
        new_data = Data(**data)
        db.add(new_data)
        db.commit()
        
        logger.info(f"Successfully fetched and saved weather data for {city}")
        return True
    except Exception as e:
        logger.error(f"Error fetching weather data: {str(e)}")
        return False 