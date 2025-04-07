This project was created for OPS445 as a component of Assignment 2. 

Tool for Data Backup and Restore
   Directories may be backed up, compressed into ZIP files, and restored using this Python-based tool.

Proposal Subjects

1. Data Restore and Backup
   Uses command-line options to automate backups.
   Select directories are backed up, and zipped backups can be restored.
   Resolves issues like missing permissions and prevents overwriting.
   Backup logs are saved to a file.
   
How the Program Operates

Input
The following can be accepted by the program using command-line arguments :
A backup folder
A place to keep the backup
A folder or `.zip` file to restore from

This implies that everything is run straight from the terminal, with no menus or user prompts.

Handling
We have developed distinct functions to: - Copy directories and files
Restore files from a `.zip` file - Convert a backup into a `.zip` file

We also take care of frequent faults like permission problems, missing directories, and existing backups (to prevent overwriting).

Results
The script uses the terminal to display messages and progress.  In order to keep track of what was backed up and when, it additionally logs backup activity to a text file.

How to USE 

Here are some instances of how to use the application:

python3 assignment2.py backup /home/user/documents /mnt/backup

Zip a folder

python3 assignment2.py zip /mnt/backup/documents_backup /mnt/backup/documents_backup.zip

Restore a backup
python3 assignment2.py restore /mnt/backup/documents_backup.zip /home/user/restored_docs







    
