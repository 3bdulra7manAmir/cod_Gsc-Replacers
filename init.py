import os

def process_gsc_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".gsc"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r+') as file:
                content = file.read()
                if "character\\shadow_assault" in content:
                    content = content.replace("character\\shadow_company_assault", "character\\shadow_co_assault")
                if "character\\shadow_smg" in content:
                    content = content.replace("character\\shadow_company_smg", "character\\shadow_co_smg")
                if "character\\shadow_lmg" in content:
                    content = content.replace("character\\shadow_company_lmg", "character\\shadow_co_lmg")
                if "character\\shadow_shotgun" in content:
                    content = content.replace("character\\shadow_company_shotgun", "character\\shadow_co_shotgun")
                if "viewbody_us_army" in content:
                    content = content.replace("viewbody_us_army", "worldbody_h1_sas_woodland")
                file.seek(0)
                file.write(content)

# Usage example
directory_path = "E:\\h1\\h1-mod\\maps"
process_gsc_files(directory_path)
