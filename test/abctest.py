import sys
from pathlib import Path

FILE_PATH = Path(__file__)

sys.path.append(str(FILE_PATH.parent.parent))

from src import AbcDict

yaml_file = FILE_PATH.with_suffix('.yaml')

abcDict = AbcDict(yaml_file)

print(abcDict.path)
print(abcDict.info.age_default_int)
print(type(abcDict.info.age_default_int))
print(abcDict)

abcDict.dump(yaml_file.with_stem('save'))
