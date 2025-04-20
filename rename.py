import os
import re

# Set the folder path where your files are located
folder_path = 'D:\AUDIO'  # Replace with your actual path

# Pattern to match filenames like MFCC59.BIN
pattern = re.compile(r'^MFCC(\d+)\.BIN$', re.IGNORECASE)

for filename in os.listdir(folder_path):
    match = pattern.match(filename)
    if match:
        number = int(match.group(1))
        new_number = number + 54
        new_filename = f"general{new_number}.BIN"

        # Full path for renaming
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_filename)

        os.rename(src, dst)
        print(f"Renamed: {filename} → {new_filename}")
