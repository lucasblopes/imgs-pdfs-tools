import os
from PIL import Image
from PyPDF2 import PdfMerger

########################### parameters ###########################
PATH = "~/pdfs/"
dir_results = "~/output/"
output = "output.pdf"

#################### functions ####################


def convert_image_to_pdf(image_path, output_path):
    with Image.open(image_path) as img:
        img.convert("RGB").save(output_path, "PDF")


def combine_pdfs(pdf_list, output_name):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_name)
    merger.close()


####################### main ########################

# Collect all files
all_files = [
    os.path.join(PATH, f)
    for f in os.listdir(PATH)
    if f.endswith((".png", ".jpg", ".jpeg", ".pdf"))
]

# Separate images and pdfs
pdf_files = []
temp_image_pdfs = []

for file in all_files:
    if file.endswith(".pdf"):
        pdf_files.append(file)
    elif file.endswith((".png", ".jpg", ".jpeg")):
        # Convert image to pdf and add to temp list
        temp_pdf = file.rsplit(".", 1)[0] + ".pdf"
        convert_image_to_pdf(file, temp_pdf)
        temp_image_pdfs.append(temp_pdf)

# Combine all PDFs
all_pdfs = pdf_files + temp_image_pdfs
combine_pdfs(all_pdfs, output)

# Clean up temporary files
for temp_pdf in temp_image_pdfs:
    os.remove(temp_pdf)

print("Done! Output:", output)
