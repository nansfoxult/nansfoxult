import pyautogui as pag
from time import sleep
import re

def write_text(text_to_write):
    words_per_minute = 200
    words = text_to_write.split()
    num_words = len(words)

    minutes = num_words / words_per_minute

    for word in words:
        pag.typewrite(word + " ")
        sleep(0 / words_per_minute)         # If you change the value to a higher number the script will be slower.

        # Copy the text through image-to-text extension and put it in here
multiline_text = """	
"""
b = re.sub(r'\n', ' ', multiline_text)

sleep(3)

write_text(b)
