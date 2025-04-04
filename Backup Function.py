#!/usr/bin/env python3
import os

def copy_files(source, destination):
    """Recursively copies files from source to destination."""
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

