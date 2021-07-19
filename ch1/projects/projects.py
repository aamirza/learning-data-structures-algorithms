"""Write a Python program that can take a positive integer greater than 2 as input and write out the number of times
one must repeatedly divide this number by 2 before getting a value less than 2."""

def num_of_divisions_by_2_to_get_less_than_2(positive_integer):
    """Get the number of digits in bits, then substract by one.
    >>> num_of_divisions_by_2_to_get_less_than_2(18)
    4
    >>> num_of_divisions_by_2_to_get_less_than_2(100)
    6
    >>> num_of_divisions_by_2_to_get_less_than_2(40332473874287356767474)
    75
    """
    return len(f"{positive_integer:b}") - 1


"""Write a Python program that can 'make change'. Your program should take two numbers as input, one that is a
monetary amount given. It should then return the number of each kind of bill and coin to give back as change for the
difference between the amounts given and the amount charged. Try to design your program so that it returns as few
bills and coins as possible."""

def change_needed(money_given, price):
    bills = {
        "hundred-dollar": 100,
        "fifty-dollar": 50,
        "twenty-dollar": 20,
        "ten-dollar": 10,
        "five-dollar": 5,
        "toonie": 2,
        "loonie": 1,
        "quarter": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
        "penny": 0.01,
    }
    bills_given = {}
    change_remaining = money_given - price
    while change_remaining >= 0.01:
        for name, value in bills.items():
            number_of_bills = change_remaining // value
            change_remaining -= number_of_bills * value
            if number_of_bills > 0:
                bills_given[name] = number_of_bills
    return bills_given


def calculator_program():
    class Reset(Exception):
        pass

    def advanced_input(word):
        user_input = input(f"{word} >>> ")
        if user_input.lower() in ('clear', 'reset'):
            raise Reset
        return user_input

    print("Welcome to the calculator!")
    while True:
        try:
            left_operand = float(advanced_input("Number"))
            operator = advanced_input("Operator")
            right_operand = float(advanced_input("Number"))
            print(eval(f"{left_operand} {operator} {right_operand}"))
        except Reset:
            continue
        except ValueError:
            print("Please input a number!")
            continue


def interview_probability(chance_of_interview, number_of_applications):
    percent_chance_of_no_interview = (100 - chance_of_interview) / 100
    return (1 - percent_chance_of_no_interview ** number_of_applications) * 100
