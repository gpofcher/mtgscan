# basic usage of mtgscan with the Google Cloud Vision API

from mtgscan.text import MagicRecognition
from mtgscan.ocr.google_cloud import Google

gcp = Google()
rec = MagicRecognition(file_all_cards="all_cards.txt", file_keywords="Keywords.json")
texts = gcp.image_to_text_list("tests/samples/arena_aristocrats/image.jpg")
deck = rec.list_to_deck(texts)
for c, k in deck:
    print(c, k)
