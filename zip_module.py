#!/usr/bin/env python3
"""
ZIP-Module: It Compress a folder into a .zip archive.
"""

import os
import zipfile
import sys

def zip_folder(source_folder, output_zip):
    """
    Compresses the source_folder into a .zip file named output_zip.
    """
    # Check if source folder exists
    if not os.path.exists(source_folder):
        print("Error: Source folder does not exist.")
        sys.exit(1)

    # Warn if output ZIP already exists
    if os.path.exists(output_zip):
        print(f"Warning: {output_zip} already exists. It will be overwritten.")

    # Ensure .zip extension
    if not output_zip.endswith(".zip"):
        output_zip += ".zip"
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Go through every folder, subfolder, and file inside the source folder
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    file_path = os.path.join(root, file)  # Full path to the file
                    arcname = os.path.relpath(file_path, start=source_folder)  # This keeps folder structure inside zip
                    zipf.write(file_path, arcname)  # Add the file to the zip archive
