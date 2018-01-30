#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_modint
----------------------------------

Tests for `modint` module.
"""

import pytest
import subprocess
import sys


def _test_input_output(args, input_, expected_output, desc):
    proc = subprocess.Popen(
        [sys.executable, 'zenfilter.py'] + args,
        stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    got_output = proc.communicate(input=input_)[0]
    print(desc)
    assert got_output == expected_output


def test_modint():
    _test_input_output(
        ['--last', '2'], b'1\n2\n3\n4\n', b'LAST\t3\nLAST\t4\n', 'test --last')
