import cv2
import numpy as np

def split_tiles(image_path, num_tiles_x=4, num_tiles_y=4):
    # Load the image
    img = cv2.imread(image_path)

    # Check if the image has been loaded properly
    if img is None:
        print("Error: Image did not load properly. Please check the path and try again.")
        return

    # Get dimensions of the image
    img_height, img_width, _ = img.shape

    # Calculate the size of each tile
    tile_width = img_width // num_tiles_x
    tile_height = img_height // num_tiles_y

    # List to store the tiles
    tiles = []
    
    # Loop through the image and extract each tile
    for y in range(0, num_tiles_y):
        for x in range(0, num_tiles_x):
            x0 = x * tile_width
            y0 = y * tile_height
            x1 = x0 + tile_width
            y1 = y0 + tile_height
            tile = img[y0:y1, x0:x1]
            tiles.append(tile)
    
    # Save or process the tiles
    for idx, tile in enumerate(tiles):
        tile_filename = f"./tiles/tile_{idx+1}.png"
        cv2.imwrite(tile_filename, tile)
        print(f"Saved '{tile_filename}'")

    print(f"Total {len(tiles)} tiles extracted and saved.")

# Example usage:
split_tiles("./screens.png")