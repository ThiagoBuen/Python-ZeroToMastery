# Python-ZeroToMastery

Miscelaneous projects developed with Zero To Mastery's Python Developer coursework. 

## Description

This repository follows the Zero to Mastery's course, which covers several topics and projects with Python language.

Each project and topic has its own folder here and I will try my best to highlight the requirements for each one.


## Image Processing:


### Functionalities
- [X] ImageProcessing.py: Introduction to manipulate Image Files with Pillow.
- [X] JPGtoPNG.py: Automates the image type convertion from the .jpeg files at __Pokedex/__ to the .png format at __new/__. You can change these dir if you wish!
- [X] pdfPython.py: Introduction to manipulate PDF files with PyPDF2.
- [X] PDFMerger.py: Automates the .pdf files with python with PyPDF2. At my setup, I save the merged pdf into __./pdfFiles__ directory.

### Requirements
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Python3]

#### Image-related scripts
``` sh
pip3 install Pillow 
```
#### PDF-related scripts
``` sh
pip3 install PyPDF2 
```

### How to use?

Most of the scripts run as python3 <<python_file.py>>, yet there is a list bellow with the specific ones:

- __JPGtoPNG.py__ :
``` sh
python3 JPGtoPNG.py Pokedex/ new/
```

- __JPGtoPNG.py__ :
``` sh
python3 JPGtoPNG.py Pokedex/ new/
```

- __JPGtoPNG.py__ :
``` sh
python3 PDFMerger.py <pdfFile1> <pdfFile2> ... <pdfFileN>
```




