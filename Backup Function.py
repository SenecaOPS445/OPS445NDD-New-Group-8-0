#!/usr/bin/env python3
import os

def copy_files(source, destination):
    """Recursively copies files from source to destination."""
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isdir(source_path):
            if os.path.exists(destination_path) == False:
                os.makedirs(destination_path)
            copy_files(source_path, destination_path)
        else:
            src_file = open(source_path, 'r')
            content = src_file.read()
            src_file.close()

            dest_file = open(destination_path, 'w')
            dest_file.write(content)
            dest_file.close()