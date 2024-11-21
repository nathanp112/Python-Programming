print("Task 8 ")


# For Task 6

def task6(first_name, last_name):
    """
    returns the last name and first name with comma seperated
    >>> task6("Nathan", "Prince")
    'Prince, Nathan'
    """
    return last_name + ", " + first_name


if __name__ == "__main__":
    import doctest

    doctest.testmod()
