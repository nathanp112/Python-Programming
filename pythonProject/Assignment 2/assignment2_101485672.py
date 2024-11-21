"""
Assignment 1 File

Full Name: Nathan Prince
Student Number: 101485672

Only edit the text where indicated
Make sure that the final result of the function is stored in the variable RESULT
"""


def task1(salary):
    """
    Given the Federal Income Tax Rates chart located below,

    Tax rate	Taxable income threshold
    15%	        $55,000 or less
    21%	        $55,001 up to $111,000
    26%	        $111,001 up to $173,000
    29%	        $173,001 up to $246,000
    33%	        $246,001 or higher

    Code the function that accepts ONE gross salary and returns net salary and tax rate as a string percent as a tuple:

    NOTE: you are required to add the neccessary paramaters, method body and return statement.
    NOTE: The method can accept string and int values (no float values)
    NOTE: the salary will only accept whole values for the gross salary value
    NOTE: the net value should be rounded to the nearest whole number. Remove all decimal values
    NOTE: error handling is not expected of you, assume that if the value passed is a string value, all characters will be 0-9
    >>> task1(100000)
    (79000, '21%')
    >>> task1(180000)
    (127800, '29%')
    >>> task1(250000)
    (167500, '33%')
    >>> task1('23456')
    (19938, '15%')
    >>> task1('55000')
    (46750, '15%')
    """
    ########################
    # Start writing code
    ########################
    tax_rates = {
        0.15: 55000,
        0.21: 111000,
        0.26: 173000,
        0.29: 246000,
        0.33: float('inf')
    }
    salary =int(salary)
    for rate, threshold in tax_rates.items():
        if salary <= threshold:
            net_salary = salary * (1 - rate)
            return round(net_salary), f'{round(rate * 100)}%'
    ########################
    # End writing code
    ########################


def task2(monthly_budget, max_spending, cost_spending):
    """
    Code a function that accepts
        1) Accept a monthly budget value
        2) A maximum expense value
        A dictionary of expenses with 2 keys
            expense name: string value
            expense price: float value
        Iterate the dictionary of values and return one of the following values
            True & sum of all expenses: if the sum of all expenses is less than or equal to the monthly budget vlue
            True & sum of all expenses: if the sum of all expenses is greater than the monthly budget vlue
            False, the expense name & the expense value of the FIRST expense that is greater than the maximum expense value

    NOTE: you are required to add the neccessary paramaters, method body and return statement.
    NOTE: error handling is not expected of you, assume that if the values passed will be int, int and dictionary

    >>> task2(100, 40, {'food': 20, 'fun': 15, 'clothes': 30, 'travel': 25})
    (True, 90)
    >>> task2(150, 35, {'food': 30, 'books': 35, 'internet': 40, 'streaming services': 15})
    (False, 'internet', 40)
    >>> task2(180, 40, {'food': 30, 'fun': 25, 'clothes': 30, 'travel': 25, 'books': 35, 'internet': 40, 'streaming services': 15})
    (False, 200)
    >>> task2(300, 50, {'coat': 30, 'jeans': 20, 'hat': 15, 'scarf': 10, 'boots': 40, 'socks': 5, 'food': 20, 'fun': 15, 'clothes': 30, 'travel': 25})
    (True, 210)
    >>> task2(500, 100, {'coffee': 40, 'restaurant': 200, 'travel': 50, 'plan ticket': 350, 'school': 90})
    (False, 'restaurant', 200)
    """
    ########################
    # Start writing code
    ########################
    total_expenses = sum(cost_spending.values())
    for expenses_name, expenses_price in cost_spending.items():
        if expenses_price > max_spending:
            return False, expenses_name, expenses_price

    if total_expenses < monthly_budget:
        return True, total_expenses
    else:
        return False, total_expenses
    ########################
    # End writing code
    ########################



def task3(data):
    """
    This function accepts one parameter returns either 'odd', 'even' or None.
    The function determines whether or not
        a) if the numerical value is odd or even
        b) if the number of characters of a string is odd or even
        c) if the number of elements in a list, set or tuple is add or even
        d) If any other data type, there is no return

    NOTE: you are required to add the neccessary paramaters, method body and return statement.
    NOTE: you are expected to determine the data type of the parameter and return the appropriate string value


    >>> task3("hello world")
    'odd'
    >>> task3(1234)
    'even'
    >>> task3({1,1,2,3,4,5,2,3,4,5,6})
    'even'
    >>> task3(list(range(2, 11)))
    'odd'
    >>> task3(tuple("cool"))
    'even'
    """
    ########################
    # Start writing code
    ########################
    if isinstance(data, int):\
        return 'even' if data % 2 == 0 else 'odd'
    elif isinstance(data, str):
        return 'even' if len(data) % 2 == 0 else 'odd'
    elif isinstance(data, (list, set, tuple)):
        return 'even' if len(data) % 2 == 0 else 'odd'
    ########################
    # End writing code
    ########################
