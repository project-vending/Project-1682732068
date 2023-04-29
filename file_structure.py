  
import os

# Define the project directory
project_dir = 'Data Visualization Project'

# Define the directories to create
directories = [
    'data',
    'visualization'
]

# Define the files to create
files = [
    'README.md',
    'LICENSE',
    'requirements.txt'
]

# Create directories and files
for directory in directories:
    os.makedirs(os.path.join(project_dir, directory), exist_ok=True)
for file in files:
    for directory in directories:
        with open(os.path.join(project_dir, directory, file), 'w'):
            pass
