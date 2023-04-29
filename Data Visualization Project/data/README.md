
import os

# Define the project directory
project_dir = 'Data Visualization Project'

# Define the file path
file_path = os.path.join(project_dir, 'data', 'README.md')

# Create the file
with open(file_path, 'w') as f:
    f.write('# Data Visualization Project Data Directory\n\nPut your data files for the Data Visualization Project in this directory.\n\n')
