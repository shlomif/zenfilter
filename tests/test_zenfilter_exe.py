#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_zenfilter
----------------------------------

Tests for `zenfilter` module.
"""

import subprocess
import sys

import pytest  # noqa: F401


def _test_input_output(args, input_, expected_output, desc):
    proc = subprocess.Popen(
        [sys.executable, 'zenfilter.py'] + args,
        stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    got_output = proc.communicate(input=input_)[0]
    print(desc)
    assert got_output == expected_output


def test_zenfilter():
    _test_input_output(
        ['--last', '2'], b'1\n2\n3\n4\n', b'LAST\t3\nLAST\t4\n', 'test --last')
    _test_input_output(
        ['--last', '1', '--filter', 'my.*pat'],
        b'1 my pattern\n2 my please\n3 my patently obvious\n' +
        b'4 foo\n5 spam\n6 pink\n',
        b'FOUND\t1 my pattern\nFOUND\t3 my patently obvious\nLAST\t6 pink\n',
        'test --filter')
    _test_input_output(
        ['--count', '10'],
        b''.join(bytes(str(i+1) + '\n', 'utf-8') for i in range(35)),
        b'COUNT\t0\nCOUNT\t10\nCOUNT\t20\nCOUNT\t30\n',
        'test --count')
    _test_input_output(
        ['--last', '1', '--filter', 'my.*pat', '--count', '3'],
        b'1 my pattern\n2 my please\n3 my patently obvious\n' +
        b'4 foo\n5 spam\n6 pink\n',
        b'COUNT\t0\nFOUND\t1 my pattern\n' +
        b'FOUND\t3 my patently obvious\nCOUNT\t3\nLAST\t6 pink\n',
        'test --filter')
    _test_input_output(
        ['--count', '10', '--last', '10', '--suppress-last-on',
         "All tests successful\\n*\\Z"],
        (b''.join(bytes(str(i+1) + '\n', 'utf-8') for i in range(35)) +
         b'All tests successful\n'),
        b'COUNT\t0\nCOUNT\t10\nCOUNT\t20\nCOUNT\t30\n',
        'test --suppress-last-on')
