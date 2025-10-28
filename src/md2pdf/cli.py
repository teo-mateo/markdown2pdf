# Created by Claude Code on 2025-10-28
# Purpose: Command-line interface for md2pdf tool
# Context: Provides CLI with --help and --version flags for converting Markdown to PDF

import sys
from pathlib import Path

import click

from . import __version__
from .converter import MarkdownToPdfConverter


@click.command()
@click.argument('input_file', type=click.Path(exists=True), required=False)
@click.option(
    '-o', '--output',
    type=click.Path(),
    help='Output PDF file path (default: same name as input with .pdf extension)'
)
@click.option(
    '-v', '--version',
    is_flag=True,
    help='Show version and exit'
)
@click.version_option(version=__version__, prog_name='md2pdf')
def main(input_file, output, version):
    """
    Convert Markdown documents to classy PDF files.

    Usage:
      md2pdf FILE.md
      md2pdf FILE.md -o output.pdf
      md2pdf --help
      md2pdf --version
    """
    if version:
        click.echo(f'md2pdf version {__version__}')
        return

    if not input_file:
        click.echo('Error: Missing argument INPUT_FILE.')
        click.echo('Try "md2pdf --help" for help.')
        sys.exit(1)

    # Validate input file
    input_path = Path(input_file)
    if not input_path.suffix.lower() in ['.md', '.markdown']:
        click.echo(
            f'Warning: Input file "{input_file}" does not have a .md or .markdown extension.',
            err=True
        )

    # Convert the file
    converter = MarkdownToPdfConverter()

    try:
        output_path = converter.convert(input_file, output)
        click.echo(f'Successfully converted "{input_file}" to "{output_path}"')
    except FileNotFoundError as e:
        click.echo(f'Error: {e}', err=True)
        sys.exit(1)
    except IOError as e:
        click.echo(f'Error: {e}', err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f'Unexpected error: {e}', err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
