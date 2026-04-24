import pytest
from io import StringIO
from contextlib import redirect_stdout
from maths.juggler_sequence import juggler_sequence

def test_juggler_sequence_with_three():
    with StringIO() as buf, redirect_stdout(buf):
        print(",".join(map(str, juggler_sequence(3))) + "\n")
        output = buf.getvalue()
    assert output == "3,5,11,36,6,2,1\n"

def test_juggler_sequence_with_two():
    with StringIO() as buf, redirect_stdout(buf):
        print(",".join(map(str, juggler_sequence(2))) + "\n")
        output = buf.getvalue()
    assert output == "2,1\n"

def test_juggler_sequence_with_nine():
    with StringIO() as buf, redirect_stdout(buf):
        print(",".join(map(str, juggler_sequence(9))) + "\n")
        output = buf.getvalue()
    assert output == "9,27,140,11,36,6,2,1\n"

def test_juggler_sequence_with_one():
    with StringIO() as buf, redirect_stdout(buf):
        print(",".join(map(str, juggler_sequence(1))) + "\n")
        output = buf.getvalue()
    assert output == "1\n"