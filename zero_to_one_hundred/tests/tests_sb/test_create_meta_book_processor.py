from subprocess import CalledProcessError
from unittest.mock import patch

from zero_to_one_hundred.src.zero_to_one_hundred.processors.snatch_book_processor import (
    SnatchBookProcessor,
)


@patch(
    "zero_to_one_hundred.src.zero_to_one_hundred.factories.sb_factory.SBFactory.get_processor"
)
def test_process(get_factory, http_oreilly_1):
    actual: SnatchBookProcessor = get_factory.get_processor(
        [None, "snatch_book", http_oreilly_1]
    )
    for p in actual:
        try:
            p.process()
        except CalledProcessError:
            pass
