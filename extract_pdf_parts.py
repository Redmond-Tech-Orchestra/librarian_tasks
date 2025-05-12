import os
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
from PyPDF2 import PdfWriter, PdfReader

# Example usage
filePath = "Waltz 2 Part 2.pdf"  # Path to the input PDF
instruments_file = "instruments_list.txt"  # Path to instruments_list.txt

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\angsa\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

# Load the list of instruments
with open(instruments_file, 'r') as f:
    instruments = [line.strip() for line in f.readlines()]

# Convert PDF to images
doc = convert_from_path(filePath)
path, fileName = os.path.split(filePath)
fileBaseName, fileExtension = os.path.splitext(fileName)

# Read the original PDF for extracting pages
pdf_reader = PdfReader(filePath)

# Dictionary to store pages for each instrument (using a set to avoid duplicates)
instrument_pages = {instrument: set() for instrument in instruments}

# Process each page
for page_number, page_data in enumerate(doc):
    # Extract text from the page
    txt = pytesseract.image_to_string(page_data)
    
    # Check if any instrument name is in the text
    for instrument in instruments:
        if instrument.lower() in txt.lower():
            instrument_pages[instrument].add(page_number)  # Add page number to the set

# Create separate PDFs for each instrument
for instrument, pages in instrument_pages.items():
    if pages:
        pdf_writer = PdfWriter()
        unique_pages = sorted(pages)  # Convert set to sorted list
        for page_number in unique_pages:
            pdf_writer.add_page(pdf_reader.pages[page_number])
        
        # Save the new PDF
        output_file = f"Waltz No 2 - {instrument}.pdf"
        with open(output_file, 'wb') as f:
            pdf_writer.write(f)
        print(f"Created: {output_file}")