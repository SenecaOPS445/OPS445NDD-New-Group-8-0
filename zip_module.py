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

    try:
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=source_folder)
                    try:
                        zipf.write(file_path, arcname)
                    except PermissionError:
                        print(f"Error: Permission denied to read {file_path}.")
                        sys.exit(1)
                    except FileNotFoundError:
                        print(f"Error: File not found: {file_path}.")
                        sys.exit(1)
                    except OSError as e:
                        print(f"Error: OS error with {file_path}: {e}")
                        sys.exit(1)

        print(f"ZIP file created successfully: {output_zip}")

    except PermissionError:
        print(f"Error: Permission denied to write {output_zip}. Please check the output directory.")
        sys.exit(1)
    except zipfile.BadZipFile:
        print("Error: Failed to create a valid ZIP file. Possibly corrupt data or unsupported file type.")
        sys.exit(1)
    except OSError as e:
        print(f"Error: OS error while creating ZIP file: {e}")
        sys.exit(1)
