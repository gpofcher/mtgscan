import logging
import os
import time

import requests
from mtgscan.box_text import BoxTextList
from mtgscan.utils import is_url
from .ocr import OCR
from google.cloud import vision

class Google(OCR):
    def __init__(self):
        try:
            # Credential code goes here
            pass
        except IndexError as e:
            print(str(e))
            print(
                "Google Cloud credentials not configured properly"
            )
    
    def __str__(self):
        return "Google"
    
    def image_to_text_list(self, image: str) -> list:

        client = vision.ImageAnnotatorClient()

        # only local files for now
        with open(image, "rb") as image_file:
            content = image_file.read()

        data = vision.Image(content=content)

        logging.info(f"Send {image} to Google")
        response = client.text_detection(image = data)
        annotations = response.text_annotations
        text = str(annotations[0])

        
        description_start = text.rindex('description: "') + 14
        description_end = text.index('"\nbounding_poly')
        print(description_start, description_end)
        description = text[description_start:description_end]
        print(description)
        lines = description.split("\\n")
        print(lines)


        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )

        return lines