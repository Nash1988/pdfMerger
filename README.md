# pdfMerger
A python script to merger 2 or more pdf files in one single document.


This Python-based tool is designed to merge multiple PDF files into a single PDF document effortlessly.

## Introduction

The PDF Merger project is a command-line tool built with Python that streamlines the process of merging multiple PDF files into one cohesive document. It provides a simple interface for combining PDFs while maintaining their original quality and content.
## Features 
- **Merge PDFs:**  Combine multiple PDF files into one document. 
- **Customize Order:**  Arrange files in a specific order for merging. 
- **Cross-Platform:**  Works on Windows, macOS, and Linux.
## Installation 
1. **Clone the Repository:** 

```bash
git clone https://github.com/Nash1988/pdfMerger.git
``` 
2. **Install Dependencies:** 

Navigate into the project directory and install the required dependencies using:

```bash
pip install -r requirements.txt
```
## Usage

To merge PDF files, run the following command in the terminal:

```bash
python pdfmerger.py file1.pdf file2.pdf file3.pdf -o output.pdf
```

 
- Replace `file1.pdf`, `file2.pdf`, etc., with the names of the PDF files you want to merge. 
- `-o output.pdf` specifies the name of the output file. Change `output.pdf` to your desired filename.
## Examples

Merge three PDF files named `document1.pdf`, `document2.pdf`, and `document3.pdf` into a file named `merged_document.pdf`:

```bash
python pdfmerger.py document1.pdf document2.pdf document3.pdf -o merged_document.pdf
```


## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, please feel free to open an issue or create a pull request following the guidelines in the [CONTRIBUTING.md](https://chat.openai.com/c/CONTRIBUTING.md)  file.
## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE)  file for details.---

Feel free to modify or expand upon this template to best suit your project's specific details and instructions!

