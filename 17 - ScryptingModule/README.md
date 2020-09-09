# Python-ZeroToMastery

Miscelaneous projects developed with Zero To Mastery's Python Developer coursework. 

## Description

This repository follows the Zero to Mastery's course, which covers several topics and projects with Python language.

Each project and topic has its own folder here and I will try my best to highlight the requirements for each one.


## 17 - Scripting Module:


### Functionalities
- [X] ImageProcessing.py: Introduction to manipulate Image Files with Pillow.
- [X] JPGtoPNG.py: Automates the image type convertion from the .jpeg files at __Pokedex/__ to the .png format at __new/__. You can change these dir if you wish!
- [X] pdfPython.py: Introduction to manipulate PDF files with PyPDF2.
- [X] PDFMerger.py: Automates the .pdf files with python with PyPDF2. At my setup, I save the merged pdf into __./pdfFiles__ directory.
- [X] watermark.py: Automates the watermarking .pdf files with python and PyPDF2. At my setup, I merge the __./pdfFiles/wtr.pdf__ with the desired PDFs. You can change your watermark model by replacing this file! The generated files are also inside __./pdfFiles__ directory names as __watermarkedPDF#__, wherein # varies as the number of arguments passed to the script.
- [X] sendEmail.py: Scrypt that sends emails from a gmail account to any receiver. Just fill this script with your own data.
- [X] passwordChecker.py: Scrypt that verifies if any password has been compromised. It uses k-anonymity technique to preserve user's anonymousness by requesting the pwnedpasswords website analysis. 


### Requirements
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Python3]
- [Requests]

#### Image-related scripts
``` sh
pip3 install Pillow 
```
#### PDF-related scripts
``` sh
pip3 install PyPDF2 
```

#### passwordChecker script
``` sh
pip3 install requests 
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

- __PDFMerger.py__ :
``` sh
python3 PDFMerger.py <pdfFile1> <pdfFile2> ... <pdfFileN>
```

- __watermark.py__ :
``` sh
python3 watermark.py <pdfFile1> <pdfFile2> ... <pdfFileN>
```

- __sendEmail.py__ :
__P.S:__ Modify email['from'], email['to'], and smtp.login('', '') lines with your own data... Remember that smtp.login must receive a valid gmail and its password at the first and second arguments.

``` sh
python3 sendEmail.py
```


- __passwordChecker.py__ :
``` sh
python3 passwordChecker.py <password1> <password2> ... <passwordN>
```

