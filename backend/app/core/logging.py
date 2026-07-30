# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

import logging


def setup_logging():

    logging.basicConfig(
        level=logging.INFO,
        format=
        "%(asctime)s | %(levelname)s | %(message)s"
    )


logger = logging.getLogger("spam")
