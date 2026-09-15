from pathlib import Path
import shutil


# Altere este caminho para uma pasta de teste criada por você.
SOURCE_FOLDER = Path("arquivos-para-organizar")


def list_files(folder):
    """Retorna os arquivos diretamente dentro de folder."""
    pass


def category_for(file_path):
    """Retorna a categoria de um arquivo com base na extensão."""
    image_extensions = {".jpg", ".jpeg", ".png", ".gif"}
    document_extensions = {".pdf", ".docx", ".txt"}
    spreadsheet_extensions = {".csv", ".xlsx", ".ods"}

    extension = file_path.suffix.lower()

    if extension in image_extensions:
        return "imagens"
    if extension in document_extensions:
        return "documentos"
    if extension in spreadsheet_extensions:
        return "planilhas"
    return "outros"


def organize_files(folder):
    """Move os arquivos de folder para subpastas por categoria."""
    pass


if __name__ == "__main__":
    organize_files(SOURCE_FOLDER)