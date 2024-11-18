import os


def process_gsc_files(directory):
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    replacements = {
        "character\\shadow_company_assault": "character\\shadow_co_assault",
        "character\\shadow_company_smg": "character\\shadow_co_smg",
        "character\\shadow_company_lmg": "character\\shadow_co_lmg",
        "character\\shadow_company_shotgun": "character\\shadow_co_shotgun",
        "viewbody_us_army": "worldbody_h1_sas_woodland"
    }

    for filename in os.listdir(directory):
        if filename.endswith(".gsc"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r+') as file:
                    content = file.read()
                    updated_content = content

                    # Apply replacements
                    for old_text, new_text in replacements.items():
                        updated_content = updated_content.replace(old_text, new_text)

                    if updated_content != content:  # Only rewrite if changes are made
                        file.seek(0)
                        file.write(updated_content)
                        file.truncate()
            except Exception as e:
                log_error(f"Error processing file '{filepath}': {e}")


def log_error(message):
    log_file = "error_log.txt"
    with open(log_file, 'a') as log:
        log.write(message + "\n")


# Usage example
if __name__ == "__main__":
    directory_path = "E:\\h1\\h1-mod\\maps"
    try:
        process_gsc_files(directory_path)
        print(f"Processing completed for directory: {directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
