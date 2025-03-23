from PIL import Image, ImageDraw, ImageFont
import requests
import os
from dotenv import load_dotenv


load_dotenv()
def generate_log_sheet(trip_id):
    width, height = 800, 600
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # drawing grid and models
    for i in range(25):
        x = 50 + (i * 30)
        draw.line ([(x, 100), (x, 500)], fill="black")

    draw.text ((50, 50), f"driver's daily log - Trip ID {trip_id}", fill="black")

    # saving the image
    log_path = f"media/logs/log_{trip_id}.png"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    image.save(log_path)

    return log_path

ORS_API_KEY = os.getenv("ORS_API_KEY")

def get_route (start, end):
    url =f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={ORS_API_KEY}&start={start}&end={end}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None