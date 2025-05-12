import os

def rename_files_in_directory(directory, new_prefix):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Iterate through all files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Skip directories, only process files
        if os.path.isfile(file_path):
            # check if first 3 characters of file name contain numbers
            if file_name[:2].isdigit():
                # Rename the first 3 characters of the file name
                new_name = new_prefix + file_name[3:]
                new_file_path = os.path.join(directory, new_name)

                # Rename the file
                os.rename(file_path, new_file_path)
                print(f"Renamed: {file_name} -> {new_name}")
            else:
                new_name = new_prefix + file_name
                new_file_path = os.path.join(directory, new_name)

                # Rename the file
                os.rename(file_path, new_file_path)
                print(f"Renamed: {file_name} -> {new_name}")

# Example usage
directory_path = "C://Users//angsa//Downloads//Phantom of the opera"  # Replace with the path to your directory
new_prefix = "Phantom of the Opera - "  # Replace with the desired prefix
rename_files_in_directory(directory_path, new_prefix)