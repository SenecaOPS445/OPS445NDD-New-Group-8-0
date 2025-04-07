#!/usr/bin/env python3
import os
import argparse

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
            src_file = open(source_path, 'rb')
            content = src_file.read()
            src_file.close()

            dest_file = open(destination_path, 'wb')
            dest_file.write(content)
            dest_file.close()

def backup(source, destination):
    """Creates a backup of the source directory in the destination."""
    source_exists = os.path.exists(source)
    if source_exists == False:
        print("Error: Source directory '" + source + "' does not exist.")
        return

    destination_exists = os.path.exists(destination)
    if destination_exists == False:
        print("Warning: Destination directory '" + destination + "' does not exist and will be created.")
        try:
            os.makedirs(destination)
        except PermissionError:
            print("Error: You do not have permission to create the destination directory.")
            return

    source_name = os.path.basename(os.path.normpath(source))
    backup_name = source_name + "_backup"
    backup_path = os.path.join(destination, backup_name)

    count = 1
    original_backup_path = backup_path
    while os.path.exists(backup_path):
        backup_path = original_backup_path + "_" + str(count)
        count += 1

    try:
        path_exists = os.path.exists(backup_path)
        if path_exists == False:
            os.makedirs(backup_path)
    except PermissionError:
        print("Error: You do not have permission to create the backup folder in the destination.")
        return
    except FileExistsError:
        print("Error: Backup folder already exists and cannot be created.")
        return
    
    try:
        copy_files(source, backup_path)
    except:
        print("Error occurred during file copy.")
        return

    print("Backup successful: " + backup_path)
