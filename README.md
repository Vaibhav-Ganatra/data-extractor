# data-extractor

In order to set this project up locally and start working on a Linux based system, follow the steps:

1. Clone/Download this repository
2. Setup a python virtual environment by typing ```python3 -m venv venv```
3. Activate the virtual environment by typing ```source <path_to_venv>/bin/activate```
4. Before installing the dependencies from requirements.txt, ensure that ```poppler-utils``` and ```tesseract-ocr-hin``` are installed on your system. If they are not, you can install them by typing ```apt-get install poppler-utils``` and ```apt-get install tesseract-ocr-hin```. You may need to run these commands with ```sudo``` permission
5. Once these are installed, you may install the dependencies by running ```pip3 -r install requirements.txt```
6. Once the requirements are installed, you may navigate to the individual folders of ```wiki_extractor.py``` and ```pdf_extractor.py``` and run the commands to see their behaviour.

Note: For the pdf_extractor.py, the list of pdf_urls need to be specified as a csv file named 'Books.csv', which has one column called book_url.
