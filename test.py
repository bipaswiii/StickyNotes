import pytest
import random
@pytest.fixture
def tester():
    list_1 = "meeting at 4 pm"
    list_2= "study"
    list_3 = "go meet friends"
    list_4 = "make dinner"
    return (list_1, list_2, list_3, list_4)


def test1(tester):
    list_1 = "meeting at 4 pm"
    assert tester[0] == list_1

def test_2(tester):
    list_2 = "study"
    assert tester[1] == list_2

def test_3(tester):
    list_3 = "go meet friends"
    assert tester[2] == list_3
def test_4(tester):
    list_4 = "make dinner"
    assert tester[3] ==list_4
