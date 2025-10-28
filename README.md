# Markdown2PDF

A terminal application that converts Markdown documents into classy PDF files.

## Setup

### 1. Create the conda environment

```bash
conda env create -f environment.yml
```

### 2. Activate the environment

```bash
conda activate markdown2pdf
```

### 3. Install the package

```bash
pip install -e .
```

## Usage

Convert a markdown file to PDF:

```bash
md2pdf FILE.md
```

Specify output file:

```bash
md2pdf FILE.md -o output.pdf
```

Show help:

```bash
md2pdf --help
```

Show version:

```bash
md2pdf --version
```

## Testing

Try the sample file:

```bash
md2pdf sample.md
```

This will create `sample.pdf` in the current directory.

## Features

- Clean, professional PDF output
- Syntax highlighting for code blocks
- Support for tables, lists, blockquotes
- Automatic page formatting (A4 with proper margins)
- Typography optimized for readability

## Dependencies

- Python 3.11
- weasyprint (PDF generation)
- markdown (Markdown parsing)
- pygments (Syntax highlighting)
- click (CLI framework)
