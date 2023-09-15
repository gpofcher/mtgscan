# simple example of using the GCP Vision OCR on an image
from google.cloud import vision

client = vision.ImageAnnotatorClient()
imagePath = "tests\samples\cube_RB\image.jpg"

# only local files for now
with open(imagePath, "rb") as image_file:
    content = image_file.read()

data = vision.Image(content=content)

response = client.text_detection(image = data)
annotations = response.text_annotations
text = str(annotations[0])

if response.error.message:
    raise Exception(
        "{}\nFor more info on error messages, check: "
        "https://cloud.google.com/apis/design/errors".format(response.error.message)
    )

description_start = text.rindex('description: "') + 14
description_end = text.index('"\nbounding_poly')
print(description_start, description_end)
description = text[description_start:description_end]
lines = description.split("\\n")
print(lines)
for line in lines:
    print(line)