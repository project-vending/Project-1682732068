python
import os

# Define the project directory
project_dir = 'Data Visualization Project'

# Define the directory and file paths
readme_path = os.path.join(project_dir, 'visualization', 'README.md')

# Create the README.md file
with open(readme_path, 'w') as f:
    f.write('# Data Visualization Project\n\nThis folder contains the visualization code and output for the Data Visualization Project.')
