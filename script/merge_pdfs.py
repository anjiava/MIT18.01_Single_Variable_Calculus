#!/usr/bin/env python3
"""
Script to merge all PDF files in the current directory with natural sorting.
Sorting rule: 1a < 1b, 1a < 10a, 2a < 10a
"""

import os
import re
from pathlib import Path
from PyPDF2 import PdfMerger
import sys

def natural_sort_key(filename):
    """
    Generate a sorting key for natural/alphanumeric sorting.
    This handles cases like: 1a < 1b, 1a < 10a, 2a < 10a
    """
    # Split filename into parts (numbers and text)
    parts = re.split(r'(\d+)', filename.lower())
    
    # Convert numeric parts to integers for proper sorting
    for i in range(len(parts)):
        if parts[i].isdigit():
            parts[i] = int(parts[i])
    
    return parts

def merge_pdfs_in_directory(output_filename="merged_output.pdf"):
    """
    Merge all PDF files in the current directory with natural sorting.
    """
    current_dir = Path.cwd()
    
    # Find all PDF files in current directory
    pdf_files = [f for f in current_dir.glob("Ses*.pdf")  if f.name != output_filename]
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    
    # Sort files using natural sorting
    pdf_files.sort(key=lambda x: natural_sort_key(x.name))
    
    print(f"Found {len(pdf_files)} PDF files to merge:")
    for pdf_file in pdf_files:
        print(f"  - {pdf_file.name}")
    
    # Create merger object
    merger = PdfMerger()
    
    try:
        # Add each PDF file to the merger
        for pdf_file in pdf_files:
            print(f"Adding: {pdf_file.name}")
            merger.append(str(pdf_file))
        
        # Write the merged PDF
        output_path = current_dir / output_filename
        with open(output_path, 'wb') as output_file:
            merger.write(output_file)
        
        print(f"\nSuccessfully merged {len(pdf_files)} PDF files into: {output_filename}")
        
    except Exception as e:
        print(f"Error during merging: {e}")
        
    finally:
        merger.close()

if __name__ == "__main__":
    # Check if PyPDF2 is available
    try:
        from PyPDF2 import PdfMerger
    except ImportError:
        print("PyPDF2 is required. Install it with: pip install PyPDF2")
        sys.exit(1)
    
    # Allow custom output filename as command line argument
    output_name = sys.argv[1] if len(sys.argv) > 1 else "merged_output.pdf"
    
    merge_pdfs_in_directory(output_name)
