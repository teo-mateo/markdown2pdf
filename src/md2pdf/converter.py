# Created by Claude Code on 2025-10-28
# Purpose: Core conversion logic from Markdown to PDF
# Context: Handles markdown parsing, HTML generation, and PDF rendering

import os
from pathlib import Path
from typing import Optional

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from weasyprint import HTML, CSS


class MarkdownToPdfConverter:
    """Converts Markdown documents to well-styled PDF files."""

    def __init__(self):
        """Initialize the converter with markdown extensions."""
        self.md = markdown.Markdown(
            extensions=[
                'extra',  # Includes tables, footnotes, etc.
                'codehilite',  # Syntax highlighting
                'fenced_code',  # GitHub-style code blocks
                'nl2br',  # Convert newlines to <br>
            ],
            extension_configs={
                'codehilite': {
                    'css_class': 'highlight',
                    'linenums': False,
                }
            }
        )

        # Get the CSS file path
        self.css_path = Path(__file__).parent / 'styles.css'

    def markdown_to_html(self, markdown_text: str) -> str:
        """
        Convert markdown text to HTML.

        Args:
            markdown_text: The markdown content as a string

        Returns:
            HTML string with proper structure
        """
        html_body = self.md.convert(markdown_text)

        # Wrap in complete HTML document
        html_document = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
{html_body}
</body>
</html>
"""
        return html_document

    def convert(self, input_path: str, output_path: Optional[str] = None) -> str:
        """
        Convert a markdown file to PDF.

        Args:
            input_path: Path to the input markdown file
            output_path: Optional path for the output PDF. If not provided,
                        uses the same name as input with .pdf extension

        Returns:
            Path to the generated PDF file

        Raises:
            FileNotFoundError: If the input file doesn't exist
            IOError: If there's an error reading or writing files
        """
        input_file = Path(input_path)

        if not input_file.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")

        if not input_file.is_file():
            raise IOError(f"Input path is not a file: {input_path}")

        # Determine output path
        if output_path is None:
            output_path = input_file.with_suffix('.pdf')
        else:
            output_path = Path(output_path)

        # Read markdown content
        try:
            markdown_text = input_file.read_text(encoding='utf-8')
        except Exception as e:
            raise IOError(f"Error reading markdown file: {e}")

        # Convert to HTML
        html_content = self.markdown_to_html(markdown_text)

        # Generate PDF
        try:
            html = HTML(string=html_content)
            css = CSS(filename=str(self.css_path))
            html.write_pdf(output_path, stylesheets=[css])
        except Exception as e:
            raise IOError(f"Error generating PDF: {e}")

        return str(output_path)
