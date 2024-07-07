import os
from PyPDF2 import PdfMerger

def merge_pdfs(folder_path, output_path, sorted=False):
    merger = PdfMerger()

    files = os.listdir(folder_path)
    # pdf files if sorted is True then sort otherwise not pdf_files = sorted([f for f in files if f.endswith('.pdf')])
    pdf_files = [f for f in files if f.endswith('.pdf')]
    if sorted:
        pdf_files = sorted(pdf_files)
    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        merger.append(pdf_path)
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)
    merger.close()
    print(f'Pdf files merged successfully to {output_path}')


if __name__ == '__main__':
    merge_pdfs('Inputs', 'Outputs/merged.pdf', sorted=False)

    