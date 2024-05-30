import sys
from pathlib import Path

FILE_PATH = Path(__file__)

sys.path.append(str(FILE_PATH.parent.parent))

from src import AbcDict

yaml_file = FILE_PATH.with_suffix('.yaml')

abcDict = AbcDict(yaml_file)
abcDict.dump(yaml_file.with_stem('save'))
