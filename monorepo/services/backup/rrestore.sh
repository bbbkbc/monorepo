#!/bin/bash

# Check if a date was provided
if [ $# -eq 0 ]; then
    echo "Please provide the backup date as an argument in the format YYYY-MM-DD_HH-MM-SS."
    exit 1
fi

# Define the directory where your backups are stored
backup_dir="/path/to/backup"

# Construct the backup path from the provided date
backup_path="${backup_dir}/backup_$1"

# Check if the specified backup exists
if [ ! -d "${backup_path}" ]; then
    echo "The specified backup does not exist: ${backup_path}"
    exit 1
fi

# Restore the backup
rsync -aAXv --exclude-from='./exclude.txt' "${backup_path}/" /

echo "Restore completed successfully."

