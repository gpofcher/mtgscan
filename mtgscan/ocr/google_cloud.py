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
    
    def image_to_box_texts(self, image: str) -> BoxTextList:

        client = vision.ImageAnnotatorClient()

        # only local files for now
        with open(image, "rb") as image_file:
            content = image_file.read()

        data = vision.Image(content=content)

        logging.info(f"Send {image} to Google")
        response = client.text_detection(image = data)
        texts = response.text_annotations
        print("Texts:")

        for text in texts:
            print(f'\n"{text.description}"')

            vertices = [
                f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
            ]

            print("bounds: {}".format(",".join(vertices)))

        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )

        # box_texts = BoxTextList()
        
        # return box_texts