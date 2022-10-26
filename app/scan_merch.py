from PyPDF2 import PdfReader, PdfWriter
import filemanagement as fm

def merge_double_page_PDF():
    files_tup = fm.import_files()
    if files_tup == 2:
        pass
    else:
        print("Attancion you have not selected the required '2' Files")
    
    
    
        
