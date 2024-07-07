# PDFMerger

PDFMerger is a Python-based tool to merge PDF files locally without uploading personal documents to third-party cloud services.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Using the UI](#using-the-ui)
  - [Using the Command Line](#using-the-command-line)

## Installation

Before you begin, ensure you have Python installed on your system. You can install the necessary libraries by following the instructions in the [installation.md](installation.md) file.

1. Clone the repository:

    ```bash
    git clone https://github.com/tirtho109/PDFMerger.git
    cd PDFMerger
    ```

2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Using the UI

You can use the graphical user interface (GUI) to select, sort, and merge PDF files.

1. Run the `pdf_merger_UI.py` script:

    ```bash
    python pdf_merger_UI.py
    ```

2. Use the UI to select the PDF files you want to merge, arrange them in the desired order, and execute the merge process.

### Using the Command Line

If you prefer to use the command line, you can directly merge files placed in the `Inputs` folder and save the merged PDF in the `Outputs` folder.

1. Place the PDF files you want to merge in the `Inputs` folder.

2. Run the `pdf_merger.py` script:

    ```bash
    python pdf_merger.py
    ```

3. The merged PDF will be saved in the `Outputs` folder.

