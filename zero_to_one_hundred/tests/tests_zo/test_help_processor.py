from zero_to_one_hundred.src.zero_to_one_hundred.processors.help_processor import (
    HelpProcessor,
)


def test_process(get_factory):
    actual: HelpProcessor = get_factory.get_processor(["help"])
    for p in actual:
        p.process()
