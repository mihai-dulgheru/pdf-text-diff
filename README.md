# PDF Text Diff

This is a Python application that compares two PDF files and finds differences in the text. The application was
developed using Python 3.11.

## Prerequisites

### Windows

1. Tesseract OCR (OCR = optical character recognition)
    - [Download and install Tesseract](https://github.com/UB-Mannheim/tesseract/wiki#tesseract-installer-for-windows)
    - Set environment variable  
      After installation, you need to set the environment variable of the Tesseract (
      e.g. `C:\Program Files\Tesseract-OCR`)
    - Verify Tesseract installation  
      Open the Windows Command Prompt and run the next command:

      ```commandline
      tesseract --version
      ```

      You should get a result in form:

      ```commandline
      tesseract v5.3.1.20230401
      ...
      ```

    - Replace `<tesseract_exe_path>` with path to executable tesseract.exe

      ```python
      pytesseract.pytesseract.tesseract_cmd = (
        r"<tesseract_exe_path>"  # e.g. r"C:\Program Files\Tesseract-OCR\tesseract.exe"
      )
      ```

2. Poppler
    - Download the latest binary from [here](https://blog.alivate.com.au/poppler-windows/)
    - Unzip the folder wherever you want and add the path to the environmental variables (
      e.g. `C:\Software\poppler-0.68.0\bin`)
    - Change the value of variable `POPPLER_PATH` in file `constants/constants.py`

      ```python
        # Windows also needs poppler_exe
        POPPLER_PATH = Path(r"<poppler_path>")  # e.g. C:\Software\poppler-0.68.0\bin
      ```

### Linux

1. Tesseract OCR

   To install Tesseract OCR on Linux, run the following commands:

    ```commandline
    git clone https://github.com/tesseract-ocr/tesseract.git
    cd tesseract
    sudo ./autogen.sh
    sudo ./configure
    sudo make
    sudo make install
    sudo ldconfig
    sudo make training
    sudo make training-install
    ```

## Installation

1. Clone the repository
2. Install the required packages: `pip install -r requirements.txt`

## Usage

1. Add two PDF files to the input folder: `template.pdf` and `template_changed.pdf`
2. Run the `main.py` script: `python main.py`
3. The script will compare the two PDF files and output the differences in the text.

## Project structure

The project has the following file structure:

- `constants/`: a package containing constants used throughout the application.
- `functions/`: a package containing all the functions used in the application.
- `input/`: a folder containing the input PDF files.
- `main.py`: the main script that runs the application.
- `requirements.txt`: a file containing the required Python packages to run the application.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue on the repository.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
