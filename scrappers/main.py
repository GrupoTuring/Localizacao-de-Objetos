#! /usr/bin/python

from typing import List
from pathlib import Path
import pokebase as pb
from functools import partial
from multiprocessing import Pool

# import bulbapedia
import gameinfo
import pokemondb
import pokemon
import serebii

import acess

_NUMBER_POOLS = 16


def getAllImagesURLbyId(id: int) -> List[str]:
    print(f"> Pushando #{id}")
    acc = []
    acc += pokemon.getImagesURLbyId(id)
    acc += gameinfo.getImagesURLbyId(id)
    acc += serebii.getImagesURLbyId(id)
    acc += pokemondb.getImagesURLbyId(id)
    # acc += bulbapedia.getImagesURLbyId(id)
    return acc


def getAllImagesAndSaveById(id: int, base_path: Path) -> List[Path]:
    pokemon = pb.pokemon(id)

    imgsURL = getAllImagesURLbyId(id)
    imgs = acess.downloadImgs(imgsURL)
    path = base_path / pokemon.name
    acess.createDirIfNotExist(path)
    acess.writeImages(path, imgs)


def getAllImagesAndSaveByIds(ids: List[int], base_path: Path) -> List[Path]:
    f = partial(getAllImagesAndSaveById, base_path=base_path)
    with Pool(_NUMBER_POOLS) as p:
        p.map(f, ids)


def _main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Baixa imagens de pokemons em um diretorio')
    parser.add_argument('-b', '--begin', default=1,
                        type=int, help='pokemon inicial')
    parser.add_argument('-e', '--end', default=151, type=int,
                        help='ultimo pokemon a ser procurado')
    parser.add_argument('-p', '--path', default='../data',
                        type=str, help='diretorio que será salvo')

    args = parser.parse_args()
    path = Path(args.path)
    getAllImagesAndSaveByIds(range(args.begin, args.end+1), path)


if __name__ == "__main__":
    _main()
