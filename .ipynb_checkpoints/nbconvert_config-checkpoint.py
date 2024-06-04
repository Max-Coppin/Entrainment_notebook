## This script is aiming to convert only the result of the cell of a notebook into a pdf file, 
## It is designed to show easily the result of my work to my Phd supervisors

## First you mus install the package  "nbconvert" and "pandoc"
# 'pip install nbconvert'
# 'brew install pandoc'    # command valable for Mac 


c = get_config()

# Only include the output of code cells and Markdown cells
c.TemplateExporter.exclude_input = True


# You must execute this command in the terminal where the notebook is(you must also type its name) : 

# jupyter nbconvert --to pdf --config nbconvert_config.py example_notebook.ipynb
