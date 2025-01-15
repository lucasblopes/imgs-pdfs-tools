import os
from PIL import Image

########################### parameters ###########################
PATH = "~/imgs/"
dir_results = "~/output"
output = "output.png"

#################### functions ####################


def stack_images_horizontally(img_array, output_name):
    # Open images
    img = [Image.open(img_path) for img_path in img_array]

    # Img dimensions
    new_width = sum([im.size[0] for im in img])
    biggest_height = max([im.size[1] for im in img])

    final_image = Image.new("RGB", (new_width, biggest_height))

    # Stack horizontally
    offset = 0
    for i in range(len(img_array)):
        final_image.paste(img[i], (offset, 0))
        offset += img[i].size[0]

    # Save the resulting image
    final_image.save(output_name)


def stack_images_vertically(img_array, output_name):
    # Open images
    img = [Image.open(img_path) for img_path in img_array]

    # Img dimensions
    biggest_width = max([im.size[0] for im in img])
    new_height = sum([im.size[1] for im in img])

    final_image = Image.new("RGB", (biggest_width, new_height))

    # Stack vertically
    offset = 0
    for i in range(len(img_array)):
        final_image.paste(img[i], (0, offset))
        offset += img[i].size[1]

    # Save the resulting image
    final_image.save(output_name)


####################### main ########################

imgs = []
for filename in os.listdir(PATH):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        imgs.append(os.path.join(PATH, filename))

stack_images_vertically(imgs, output)

print("done! output: " + output)
