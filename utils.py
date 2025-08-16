from PIL import Image

def add_white_background(image_path):
    # Open the transparent image
    image = Image.open(image_path).convert("RGBA")

    # Create a new image with a white background
    white_background = Image.new("RGBA", image.size, (255, 255, 255, 255))

    # Paste the transparent image onto the white background
    white_background.paste(image, (0, 0), image)

    # Convert to RGB mode (removes alpha channel)
    image = white_background.convert("RGB")

    # Save the result, replacing the old image
    image.save(image_path)

add_white_background(r'C:\Users\Andrei\Desktop\Projects\project-euler-solutions\solutions\101 - 150\139.png')