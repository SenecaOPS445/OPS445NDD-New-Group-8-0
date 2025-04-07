#!/usr/bin/env python3

import sys
from Backup_Function import backup
from Restore_Function import restore_zip
from zip_module import zip_folder

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 assignment2.py backup <source> <destination>")
        print("  python3 assignment2.py zip <source folder> <outputzip>")
        print("  python3 assignment2.py restore <sourcezip or folder> <destination>")
        sys.exit(1)

    entry = sys.argv[1]

    if entry == "backup":
        if len(sys.argv) != 4:
            print("Usage: python3 assignment2.py backup <source> <destination>")
            sys.exit(1)
        source = sys.argv[2]
        destination = sys.argv[3]
        backup(source, destination)

    elif entry == "zip":
        if len(sys.argv) != 4:
            print("Usage: python3 assignment2.py zip <sourcefolder> <outputzip>")
            sys.exit(1)
        source_folder = sys.argv[2]
        output_zip = sys.argv[3]
        zip_folder(source_folder, output_zip)

    elif entry == "restore":
        if len(sys.argv) != 4:
            print("Usage: python3 assignment2.py restore <sourcezip or folder> <destination>")
            sys.exit(1)
        source = sys.argv[2]
        destination = sys.argv[3]
        restore_zip(source, destination)
    else:
        print("Unknown command: " + entry)
        print("Options avaliable: backup, zip, restore")
        sys.exit(1)
