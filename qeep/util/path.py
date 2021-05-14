"""
    Funções uteis para o Path
"""

from pathlib import Path
from typing import Union


def create_dir_if_not_exist(path: Union[Path, str]) -> None:
    """
    Descrição
    --------
    Cria um diretorio se ele não existe

    Entradas
    --------
    path: Path | str
    Path do diretorio que será avaliado

    Saídas
    ------
    None

    """
    if path is str:
        path = Path(path)

    if not path.exists():
        print("> Create dir:", path)
        path.mkdir()