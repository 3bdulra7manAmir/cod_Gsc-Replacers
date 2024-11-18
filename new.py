import os

directory_path = input("Enter the directory path: ")

# loop through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".gsc") and "smg" in filename:
        # read the file
        with open(os.path.join(directory_path, filename), "r") as f:
            file_contents = f.readlines()

        # make the replacements
        new_file_contents = []
        for line in file_contents:
            if line.startswith("character") and (line.endswith("::main();")):
                new_line = "character\character_shadow_co_smg_b::main();"
                new_file_contents.append(new_line)
            elif line.startswith("character") and line.endswith("::precache();"):
                new_line = "character\character_shadow_co_smg_b::precache();"
                new_file_contents.append(new_line)

        # write the modified file back to disk
        with open(os.path.join(directory_path, filename), "w") as f:
            f.writelines(new_file_contents)
