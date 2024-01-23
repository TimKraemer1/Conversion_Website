from PIL import Image
import docx2pdf
import pdf2docx

import os
import io
import contextlib
import sys

@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = io.BytesIO()
    yield
    sys.stdout = save_stdout

def jpgTopng(orig):
    im1 = Image.open(orig)
    orig, orig_extension = os.path.splitext(orig)
    if orig_extension != '.jpg':
        raise Exception("Error: File type not .jpg")
    im1.save(orig + '.png')
    os.remove(orig + '.jpg')
    return 1

def pngTojpg(orig):
    im1 = Image.open(orig)
    orig, orig_extension = os.path.splitext(orig)
    if orig_extension != '.png':
        raise Exception("Error: File type not .png")
    im1.save(orig + '.jpg')
    os.remove(orig + '.png')
    return 1

def docxTopdf(orig, dest):
    orig, orig_extension = os.path.splitext(orig)
    if orig_extension != '.docx':
        raise Exception("Error: File type not .docx")
    
    with nostdout():
        docx2pdf.convert(orig + orig_extension, dest)

    return 1

def pdfTodocx(orig, dest):
    orig, orig_extension = os.path.splitext(orig)
    if orig_extension != '.pdf':
        raise Exception("Error: File type not .pdf")
    
    with nostdout():
        pdf2docx.parse(orig + orig_extension, dest)

    return 1