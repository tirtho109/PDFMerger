# PDF Merger Installation Guide

This guide will walk you through the steps to set up a Conda environment with Python 3.12.3 for the PDF Merger project.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Conda (Miniconda or Anaconda)

## Steps

1. Open a terminal or command prompt.

2. Create a new Conda environment named "pdfmerger" with Python 3.12.3 by running the following command:

    ```bash
    conda create -n pdfmerger python=3.12.3
    ```

3. Activate the "pdfmerger" environment:

    ```bash
    conda activate pdfmerger
    ```

4. Install the project dependencies by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

    This command will read the `requirements.txt` file and install all the necessary dependencies for the PDF Merger project.

    Note: Make sure you are in the root directory of the project where the `requirements.txt` file is located.

5. Once the dependencies are installed, you can proceed with using the PDF Merger project.

## Conclusion

You have successfully set up the Conda environment with Python 3.12.3 and installed the project dependencies. You are now ready to use the PDF Merger project.

Happy coding!

