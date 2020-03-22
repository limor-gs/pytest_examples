import pytest
from person import Person

@pytest.fixture
def eric():
    return Person('Eric Idle', 'red', 1943)

@pytest.fixture
def terry():
    return Person('Terry Gilliam', 'blue', 1940)

def test_add_friend(eric, terry):
    eric.add_friend(terry)
    assert eric in terry.friends
    assert terry in eric.friends
    
