import os
import re


def process_files_with_replacements(directory, word_map):
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    for filename in os.listdir(directory):
        if filename.endswith(".gsc"):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r') as file:
                    file_text = file.read()

                updated_text = file_text
                for search_word, replace_word in word_map.items():
                    updated_text = re.sub(search_word, replace_word, updated_text)

                # Write back only if changes are made
                if updated_text != file_text:
                    with open(file_path, 'w') as file:
                        file.write(updated_text)
            except Exception as e:
                log_error(f"Error processing file '{file_path}': {e}")


def log_error(message):
    log_file = "error_log.txt"
    with open(log_file, 'a') as log:
        log.write(message + "\n")


# Usage example
if __name__ == "__main__":
    directory_path = "E:\\Ga me s\\Original Ga me s\\Battle.net\\Call of Duty - Modern Warfare 2 CR\\mods\\aitype"
    word_map = {
        "_ID3217": "animtree",
        "_ID2032": "additionalassets",
        "_ID36736": "subclass",
        "_ID949": "secondaryweapon",
        "_ID34144": ""
    }
    try:
        process_files_with_replacements(directory_path, word_map)
        print(f"Processing completed for directory: {directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
