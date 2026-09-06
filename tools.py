import json
from urllib.parse import quote
from urllib.request import urlopen





def get_crop_information(crop: str) -> str:



    """Get basic agricultural information about a crop."""

    crops = {
        "wheat": {
            "season": "Rabi",
            "water": "Moderate",
            "soil": "Well-drained fertile soil",
            "common_risks": "Rust diseases, aphids, weeds",
            "harvest": "Usually around March-April in Punjab"
        },
        "maize": {
            "season": "Kharif and spring",
            "water": "Moderate to high",
            "soil": "Fertile, well-drained soil",
            "common_risks": "Fall armyworm, stem borer, weeds",
            "harvest": "Depends on variety and planting season"
        },
        "rice": {
            "season": "Kharif",
            "water": "High",
            "soil": "Clayey to loamy soil with good water availability",
            "common_risks": "Rice diseases, insects, weeds",
            "harvest": "Usually around September-October"
        }
    }

    crop = crop.lower()

    if crop not in crops:
        return f"I don't currently have information for {crop}."

    info = crops[crop]

    return (
        f"Crop: {crop.title()}\n"
        f"Season: {info['season']}\n"
        f"Water requirement: {info['water']}\n"
        f"Soil: {info['soil']}\n"
        f"Common risks: {info['common_risks']}\n"
        f"Typical harvest: {info['harvest']}"
    )

    import json
from urllib.parse import quote
from urllib.request import urlopen

from agents import function_tool


@function_tool
def get_weather(city: str) -> str:
    """Get the current weather and temperature for a city."""

    #  Find the city's latitude and longitude
    location_url = (
        "https://geocoding-api.open-meteo.com/v1/search"
        f"?name={quote(city)}&count=1&language=en&format=json"
    )

    with urlopen(location_url) as response:
        location_data = json.loads(response.read().decode())

    if "results" not in location_data:
        return f"I could not find weather information for {city}."

    location = location_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]
    city_name = location["name"]

    # Get current weather
    weather_url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&current=temperature_2m,weather_code"
    )

    with urlopen(weather_url) as response:
        weather_data = json.loads(response.read().decode())

    current = weather_data["current"]

    temperature = current["temperature_2m"]
    weather_code = current["weather_code"]

    return (
        f"City: {city_name}\n"
        f"Temperature: {temperature}°C\n"
        f"Weather code: {weather_code}"
    )
if __name__ == "__main__":
    print(get_weather("Lahore"))
@function_tool
def get_market_price(crop: str) -> str:
    """Get typical (approximate, not live) market price range and selling advice for a crop in Pakistan."""

    prices = {
        "wheat": {
            "range": "Rs. 3,000–3,500 per 40kg (approximate, varies by region and season)",
            "advice": "Prices are usually most stable right after harvest (April-May). Selling immediately after harvest often means lower prices due to high supply; storing for a few weeks if possible can sometimes fetch better rates.",
        },
        "rice": {
            "range": "Rs. 4,000–6,000 per 40kg depending on variety (approximate)",
            "advice": "Basmati varieties typically command higher prices. Prices often rise a few months after the October harvest once immediate post-harvest supply eases.",
        },
        "maize": {
            "range": "Rs. 2,000–2,800 per 40kg (approximate)",
            "advice": "Demand from poultry feed industries stays fairly steady year-round, so timing matters less than for wheat or rice.",
        },
    }

    crop = crop.lower()
    if crop not in prices:
        return f"I don't have price information for {crop}."

    info = prices[crop]
    return (
        f"Typical price range for {crop}: {info['range']}\n"
        f"Selling advice: {info['advice']}\n"
        f"Note: These are approximate figures, not live market prices. Please confirm with your local mandi before selling."
    )
