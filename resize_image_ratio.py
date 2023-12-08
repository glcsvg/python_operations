
from PIL import Image
import os

def resize_with_padding(image_path, target_size):
    # Open the image
    
    image = Image.open(image_path)

    # Get the original size
    original_width, original_height = image.size

    # Calculate the aspect ratio
    aspect_ratio = original_width / original_height

    # Calculate the target width and height based on the aspect ratio
    target_width, target_height = target_size
    target_aspect_ratio = target_width / target_height

    if target_aspect_ratio > aspect_ratio:
        # Target image is wider, resize based on height
        new_width = int(target_height * aspect_ratio)
        new_height = target_height
    else:
        # Target image is taller or has the same aspect ratio, resize based on width
        new_width = target_width
        new_height = int(target_width / aspect_ratio)

    # Resize the image while maintaining aspect ratio
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

    # Create a new blank image with the target size
    padded_image = Image.new('RGB', target_size, (255, 255, 255))

    # Calculate the position to paste the resized image to center it
    x = (target_width - new_width) // 2
    y = (target_height - new_height) // 2

    # Paste the resized image onto the padded image
    padded_image.paste(resized_image, (x, y))

    # Return the padded image
    return padded_image

rootdir = '/home/dell/Desktop//person/'

# Target size for the padded images
target_size = (128,256)

# Output folder to save the resized images
output_folder = '/home/dell/Desktop/new_person'

# # Iterate over each file in the folder
# for filename in os.listdir(folder_path):
#     # Check if the file is an image
#     if filename.endswith('.jpg') or filename.endswith('.png'):
#         # Construct the full file path
#         file_path = os.path.join(folder_path, filename)
        
#         # Resize and add padding to the image
#         padded_image = resize_with_padding(file_path, target_size)

#         # Save the padded image in the output folder
#         output_path = os.path.join(output_folder, filename)
#         padded_image.save(output_path)

#         print(f"Resized and saved: {output_path}")        
for folder in os.listdir(rootdir):
    d = os.path.join(rootdir, folder)
    if os.path.isdir(d):
        #print(d,folder)
        for i, file in enumerate(os.listdir(d)):
            
            file_path = os.path.join(d, file)
            # Resize and add padding to the image
            padded_image = resize_with_padding(file_path, target_size)

            out_folder = os.path.join(output_folder, folder)
            if not os.path.exists(out_folder):
                os.makedirs(out_folder)
            output_path = os.path.join(out_folder, file)
            print(output_path)

                
            padded_image.save(output_path)