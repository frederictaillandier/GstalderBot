
def return5():
    """
    Mostly used to check if the tests and the framework run
    >>> return5()
    5
    """
    return 5

if __name__ == "__main__":
    print("tests")
    import doctest
    doctest.testmod()
