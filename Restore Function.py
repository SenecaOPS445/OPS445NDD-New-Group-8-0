#!/usr/bin/env python3
import os
import zipfile

def find_zip_in_directory(directory):
    """Searches for the first .zip file in a directory."""
    for item in os.listdir(directory):
        if item.endswith(".zip"):
            return os.path.join(directory, item)
    return None

def restore_zip(source, destination):
    """Restores (unzips) a .zip file from the source to the destination."""
    if os.path.exists(source) == False:
        print(f"[ERROR] Source path '{source}' does not exist.")
        return

    if zipfile.is_zipfile(source):
        zip_path = source
    elif os.path.isdir(source):
        zip_path = find_zip_in_directory(source)
        if zip_path == None:
            print("[ERROR] No zip file found in the directory.")
            return
    else:
        print("[ERROR] Source must be a .zip file or a directory containing one.")
        return

    if os.path.exists(destination) == False:
        os.makedirs(destination)

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(destination)
            print(f"[SUCCESS] Restored contents of '{zip_path}' to '{destination}'")
    except zipfile.BadZipFile:
        print(f"[ERROR] Failed to unzip: Bad zip file '{zip_path}'")
    except PermissionError:
        print(f"[ERROR] Permission denied while extracting to '{destination}'")
    except FileNotFoundError:
        print(f"[ERROR] File not found: '{zip_path}'")
    except Exception:
        print("[ERROR] An unexpected error occurred.")
