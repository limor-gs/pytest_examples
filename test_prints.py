import sys

def test_print_success():
    print(
        """
        @@@@@@@@@@@@@@@
        this statement will NOT be printed
        @@@@@@@@@@@@@@@
        """
    )

    assert 6*7 == 42

def test_print_fail():

    print(
        """
        @@@@@@@@@@@@@@@
        this statement WILL be printed
        @@@@@@@@@@@@@@@
        """
    )
    assert True == False


def test_stderr_capture_success():
    print(
        """
        @@@@@@@@@@@@@@@
        this STDERR statement will NOT be printed
        @@@@@@@@@@@@@@@
        """, 
        file=sys.stderr
    )
     
    assert True


def test_stderr_capture_fail():
    print(
        """
        @@@@@@@@@@@@@@@
        this STDERR statement WILL be printed
        @@@@@@@@@@@@@@@
        """, 
        file=sys.stderr
    )
     
    assert False
    
