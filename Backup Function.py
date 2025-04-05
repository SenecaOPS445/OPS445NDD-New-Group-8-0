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
            src_file = open(source_path, 'r')
            content = src_file.read()
            src_file.close()

            dest_file = open(destination_path, 'w')
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
            os.makedirs(destination)
        
        count = len(os.listdir(destination)) + 1
        backup_name = "backup_" + str(count)
        backup_path = os.path.join(destination, backup_name)
        os.makedirs(backup_path)

        try:
            copy_files(source, backup_path)
        except:
            print("Error occurred during file copy.")
            return
        print("Backup successful: " + backup_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple backup script")
    parser.add_argument("--source", required=True, help="Source directory to backup")
    parser.add_argument("--destination", required=True, help="Destination directory to store the backup")
    args = parser.parse_args()

    backup(args.source, args.destination)