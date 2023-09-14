# basic usage of mtgscan with the Google Cloud Vision API

from mtgscan.text_google import MagicRecognition
from mtgscan.ocr.google_cloud import Google

gcp = Google()
rec = MagicRecognition(file_all_cards="all_cards.txt", file_keywords="Keywords.json")
box_texts = gcp.image_to_box_texts("tests\samples\cube_RB\image.jpg")
deck = rec.box_texts_to_deck(box_texts)
for c, k in deck:
    print(c, k)
