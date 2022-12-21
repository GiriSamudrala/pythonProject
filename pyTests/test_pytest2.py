import pytest

@pytest.mark.skip
def testLogin():
    print("Login Successful...")

@pytest.mark.sanity
def testCal():
    assert 2+2 == 8

def testAdd():
    assert 2+2 == 4