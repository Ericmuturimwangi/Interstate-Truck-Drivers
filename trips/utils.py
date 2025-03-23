from PIL import Image, ImageDraw, ImageFont

import os

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
