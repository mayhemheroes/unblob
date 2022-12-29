#! /usr/bin/env python3
import atheris
import sys

from lark import UnexpectedToken

import fuzz_helpers

with atheris.instrument_imports():
    from unblob.parser import InvalidHexString, hexstring2regex

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        hexstring2regex(fdp.ConsumeRemainingString())
    except (InvalidHexString, UnexpectedToken):
        return -1


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
