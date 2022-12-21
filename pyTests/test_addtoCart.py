import pytest

@pytest.fixture()
def setUp():
    print("launch the Browser")
    print("Login")
    print("Browse the Items")
    yield
    print("Logoff")
    print("Close Browser..")
def testAddItems(setUp):
    print("Add Items to the Cart...")

def testDeleteItems(setUp):
    print("Delete Items from  the Cart...")