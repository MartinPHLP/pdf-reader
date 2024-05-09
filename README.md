# pdf-reader
a simple pdf-to-txt converter

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Description](#description)

## Installation

- Clone the repo
- Create env : `python -m venv env`
- Activate env : `source ./env/bin/activate`
- Install dependencies : `pip install --upgrade pip && pip install -r requirements.txt`

## Usage

- `python main.py`
- Enter the path of your file

## Description

This little project allows to convert pdf to text, even if the content is a scanned document, via PdfReader and Tesseract OCR (optical character recognition). It's set for french documents, but you can use it for all languages supported by Tesseract by downloading the data file.
