import os
import sys
from PIL import Image, ExifTags


def compress_and_move_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    full_res_dir = os.path.join(output_dir, "full_res")
    if not os.path.exists(full_res_dir):
        os.makedirs(full_res_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', 'JPG')):
            image_path = os.path.join(input_dir, filename)
            image = Image.open(image_path)
            imageexif = image.getexif()
            # Get the filesize of the full image
            full_image_size = os.path.getsize(image_path)

            # Create a thumbnail version of the image
            thumbnail = image.copy()
            thumbnail.thumbnail((300, 200))  # Adjust the size as needed

            # Convert EXIF data to bytes
            imageexif[0x010e]= f"Full Image Size: {convert_bytes_to_readable_size(full_image_size)} bytes"

            # Save thumbnail with custom EXIF tag
            thumbnail_path = os.path.join(output_dir, filename)
            thumbnail.save(
                thumbnail_path,
                exif=imageexif
            )

            # Move the original image to the 'full_res' directory with modified filename
            new_filename = os.path.splitext(filename)[0] + "_full_res" + os.path.splitext(filename)[1]
            full_res_path = os.path.join(full_res_dir, new_filename)
            os.rename(image_path, full_res_path)

            print(f"Processed: {filename}")

def convert_bytes_to_readable_size(bytes_size):
    if bytes_size < 1024:
        return f"{bytes_size} B"
    elif bytes_size < 1024 ** 2:
        return f"{bytes_size / 1024:.2f} KB"
    elif bytes_size < 1024 ** 3:
        return f"{bytes_size / (1024 ** 2):.2f} MB"
    else:
        return f"{bytes_size / (1024 ** 3):.2f} GB"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = "thumbnails"  # You can change this to the desired output directory
    compress_and_move_images(input_directory, output_directory)