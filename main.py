import os
import re

directory = "E:\\Ga me s\\Original Ga me s\\Battle.net\\Call of Duty - Modern Warfare 2 CR\\mods\\aitype"
word_map = {"_ID3217": "animtree", "_ID2032": "additionalassets", "_ID36736": "subclass", "_ID949": "secondaryweapon", "_ID34144": ""}

for filename in os.listdir(directory):
    if filename.endswith(".gsc"):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            file_text = file.read()
        for search_word, replace_word in word_map.items():
            edited_text = re.sub(search_word, replace_word, file_text)
            file_text = edited_text
        with open(file_path, 'w') as file:
            file.write(edited_text)
