import pytest
from variables import *

global age
age = 17

def test_age_now(capsys):
    age_now(age)
    captured = capsys.readouterr()
    assert captured.out == "I am currently 17 years old.\n\n"
    # assert age_now(17) == 17

def test_age_1(capsys):
    age_1(age)
    captured = capsys.readouterr()
    assert captured.out == "Next year I'll be 18 years old.\n\n"
    # assert age_1(17) == 18

def test_age_10(capsys):
    # Test age in 10 years
    age_10(age)
    captured = capsys.readouterr()
    assert captured.out == "In 10 years, I'll be 27!\n\n"
    # assert age_10(17) == 27

def test_age_50(capsys):
    # My age in 50 years!
    age_50(age)
    captured = capsys.readouterr()
    assert captured.out == "In 50 years, I'll be 67! Wow!\n\n"
    # assert age_50(17) == 67