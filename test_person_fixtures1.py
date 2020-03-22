import pytest
from person import Person

@pytest.fixture
def person_name():
    return 'Terry Gilliam'

@pytest.fixture
def birth_year():
    return 1940

@pytest.fixture
def favorite_color():
    return 'red'

def test_person_name(person_name, favorite_color, birth_year):
    person = Person(person_name, favorite_color, birth_year)
 
    # test
    assert person.name == person_name
    
