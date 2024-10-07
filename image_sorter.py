from PIL import Image, ImageDraw, ImageFont
import os

# List Input : 
couple_list = [
    "Marco", "Polo" #Input strings here
]

# Create the directory if it doesn't exist
output_dir = "outputted_images"
os.makedirs(output_dir, exist_ok=True)

# Create each image
for couple in couple_list:
    # Create a blank 100x100 white image
    width = 100
    height = 100
    img = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Set font size
    try:
        font = ImageFont.truetype("arial.ttf", 15)  # Adjust size as needed
    except IOError:
        font = ImageFont.load_default()  # Use default font if specific font is unavailable

    # Get text bounding box to calculate size and position for centering
    text_bbox = draw.textbbox((0, 0), couple, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    
    # Add the couple's name to the image
    draw.text((text_x, text_y), couple, font=font, fill=(0, 0, 0))

    # Save the image in the 'couples' folder
    img.save(os.path.join(output_dir, f"{couple.replace(' ', '_')}.jpeg"), "JPEG")

print(f"All images have been created and saved in the '{output_dir}' folder.")
