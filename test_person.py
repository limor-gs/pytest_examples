from person import Person

def test_name():
    # setup
    terry = Person(
        'Terry Gilliam',
        'red',
        1940
        )
    
    # test
    assert terry.name == 'Terry Gilliam' 


def test_add_friend():
    # setup for the test 
    terry = Person(
        'Terry Gilliam',
        'red',
        1940
        )
    eric = Person(
        'Eric Idle',
        'blue',
        1943
        )
    
    # actual test
    terry.add_friend(eric)
    assert eric in terry.friends
    assert terry in eric.friends
    
