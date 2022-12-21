import pytest

def testLogin():
    print("Login Successful...")

def testCal():
    assert 2+2 == 8

@pytest.mark.sanity
def testAdd():
    assert 2+2 == 4