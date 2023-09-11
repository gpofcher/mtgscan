import logging
import os
import time

import requests
from mtgscan.box_text import BoxTextList
from mtgscan.utils import is_url
from .ocr import OCR

class Google(OCR):
    def __init__(self):
        try:
            # Credential code goes here
            pass
        except IndexError as e:
            print(str(e))
            print(
                "Google Cloud credentials should be stored in environment variables GOOGLE_VISION_KEY and GOOGLE_VISION_ENDPOINT"
            )
    
    def __str__(self):
        return "Google"
    
    def image_to_box_texts(self, image: str) -> BoxTextList:
        
        return box_texts