#!/bin/bash

# Define the directory where you want to store your backups
backup_dir="/run/media/bst/backups/"

# Create a timestamp for the backup folder
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
backup_path="${backup_dir}/backup_${timestamp}"

# Create the backup
rsync -aAXv --exclude-from='./exclude.txt' /* "${backup_path}/"

echo "Backup completed successfully. Backup stored at ${backup_path}"

