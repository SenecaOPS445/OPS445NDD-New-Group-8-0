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
