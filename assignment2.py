#!/usr/bin/env python3

import sys
from Backup_Function import backup
from Restore_Function import restore_zip
from zip_module import zip_folder

def main():
    if len(sys.argv) < 4:
        print("how to Use:")
        print("  python3 assignment2.py backup <sourcedirectory> <destinationdirectory>")
        print("  python3 assignment2.py zip <sourcedirectory> <output zip path>")
        print("  python3 assignment2.py restore <zipped file or folder> <destination>")
        sys.exit(1)


    operation = sys.argv[1]
    source = sys.argv[2]
    destination = sys.argv[3]


    if operation == "backup":
        backup(source, destination)

    elif operation == "zip":
        zip_folder(source, destination)

    elif operation == "restore":
        restore_zip(source, destination)

    else:
        print("Unknown command: " + command)
        print("Options avaliable: backup, zip, restore")
        sys.exit(1)

if __name__ == "__main__":
    main()
