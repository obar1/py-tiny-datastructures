# pylint: disable=W0106,R1710
from typing import List
from typing import Union, TypeVar
from typing import TypeVar

from zero_to_one_hundred.src.zero_to_one_hundred.factories.a_factory import AFactory
from zero_to_one_hundred.src.zero_to_one_hundred.factories.a_factory_provider import (
    AFactoryProvider,
)


def run_core(argv: List[str], factory_provider: AFactoryProvider):
    """given params and factory provider it runs the core logic

    Args:
        argv (List[str]): args from cmd line
        factory_provider (AFactoryProvider): a factory_type

    """

    factory = factory_provider.provide()
    if factory:
        for processor in factory.get_processor(argv):
            if processor:
                processor.process()
