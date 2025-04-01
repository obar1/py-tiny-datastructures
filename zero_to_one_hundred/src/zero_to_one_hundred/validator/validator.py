import argparse
import logging
import re
import traceback

from zero_to_one_hundred.src.zero_to_one_hundred.exceptions.errors import (
    NotURLFormatError,
)


class Validator:
    @classmethod
    def is_valid_http(cls, url: str):
        pattern = r"^[^https?:\/\/].*"
        if re.match(pattern, url) is not None:
            raise NotURLFormatError(f"{url} not valid")

    @classmethod
    def print_e(cls, e: Exception):
        logging.exception(traceback.format_exc())
        logging.exception(f"#DDD issue with {e}")

    @classmethod
    def validate_args(cls, args):
        parser = argparse.ArgumentParser()
        parser.add_argument("cmd", type=str, nargs="?", default=None)
        parser.add_argument("p1", type=str, nargs="?", default=None)
        parser.add_argument("p2", type=str, nargs="?", default=None)

        args = parser.parse_args(args)  # skip fn
        cmd = args.cmd
        p1 = args.p1
        p2 = args.p2
        return cmd, p1, p2
