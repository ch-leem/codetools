import os
from PIL import Image

def resize_images(images, target_width, target_height):
    """
    Resize images to the specified width and height.

    Parameters:
        images (list): List of PIL Image objects.
        target_width (int): Target width for resizing.
        target_height (int): Target height for resizing.

    Returns:
        list: List of resized PIL Image objects.
    """
    resized_images = []
    for img in images:
        resized = img.resize((target_width, target_height), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
        resized_images.append(resized)
    return resized_images

def create_gif_from_images(folder_path, output_path="output.gif", fps=10, width=None, height=None):
    """
    Create a GIF file from all image files in the specified folder with optional resizing.

    Parameters:
        folder_path (str): Path to the folder containing image files.
        output_path (str): Path to save the generated GIF file. Default is 'output.gif'.
        fps (int): Frames per second for the GIF. Default is 10 FPS.
        width (int): Target width for resizing images. If None, original width is used.
        height (int): Target height for resizing images. If None, original height is used.

    Returns:
        None
    """
    # Supported image formats
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')
    
    # Get all image file paths from the folder
    images = [os.path.join(folder_path, file) for file in os.listdir(folder_path)
              if file.lower().endswith(supported_formats)]
    
    if not images:
        print("No images found in the specified folder.")
        return
    
    # Sort images to ensure consistent order
    images.sort()

    # Load images
    frames = [Image.open(image) for image in images]

    # Resize images if width and height are specified
    if width and height:
        frames = resize_images(frames, width, height)

    # Calculate duration per frame in milliseconds
    duration = int(1000 / fps)

    # Save as GIF
    frames[0].save(output_path, format="GIF", save_all=True, append_images=frames[1:], duration=duration, loop=0)
    print(f"GIF created and saved at {output_path}")

# (customize**)
folder = "./images"
output = "wrong2.gif"
fps = 5
width = int(1920 / 2)  # Target width
height = int(1200 / 2)  # Target height
# (customize**)

create_gif_from_images(folder, output, fps, width, height)