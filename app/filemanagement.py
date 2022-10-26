import tkinter as tk
from tkinter import filedialog
import os
 
def import_files():
    root = tk.Tk()
    root.withdraw()
    doc_path = os.path.expanduser("~\OneDrive\Dokumente")
    file_path = filedialog.askopenfilenames(title= "Select PDF Files",
                                            initialdir = doc_path,
                                            filetypes = [("PDF files","*.pdf")])
    return file_path

#import_files()