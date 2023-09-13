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

        box_texts = BoxTextList()
        
        return box_texts