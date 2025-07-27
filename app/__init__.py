import sys
from pathlib import Path

from loguru import logger

if (home := Path(__file__).parent.parent) not in sys.path:
    logger.debug(f'Adding {home} to sys.path')
    sys.path.append(home.as_posix())
