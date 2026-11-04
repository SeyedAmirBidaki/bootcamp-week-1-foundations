"""
Week 1 exercises: starter file.

Fill in every part marked TODO, then run this file:

    python3 exercises_template.py

You will see one line per exercise. PASS means your answer is correct.
FAIL means your answer does not match yet: the message points at the problem
without giving you the answer. ERROR means the code broke before it could be
checked, and the exception type is printed so you can read it.

Do not rename the variables and functions below. The checks at the bottom of
the file look for those exact names.
"""

# ----------------------------------------------------------------------
# Exercise 1 (easy): predict the output.
# Write each printed line as a string, in the order it appears on screen.
# Example of the shape: ["first line", "second line", "third line"]
# ----------------------------------------------------------------------
prediction_1 = []  # TODO


# ----------------------------------------------------------------------
# Exercise 2 (easy): predict the output.
# ----------------------------------------------------------------------
prediction_2 = []  # TODO


# ----------------------------------------------------------------------
# Exercise 3 (easy): find and fix the bug.
# The function below breaks when it is called. Fix it in place.
# ----------------------------------------------------------------------
def describe_item(item, price):
    # TODO: this line is wrong. Fix it without renaming the function.
    return item + " costs " + price + " dollars."


# ----------------------------------------------------------------------
# Exercise 4 (medium): write a function from its specification.
# ----------------------------------------------------------------------
def initials(full_name):
    """Return the initials of a full name, each followed by a dot.

    initials("ada lovelace")            -> "A.L."
    initials(" grace brewster murray ")  -> "G.B.M."
    initials("plato")                   -> "P."
    """
    # TODO
    raise NotImplementedError("exercise 4 is not written yet")


# ----------------------------------------------------------------------
# Exercise 5 (medium): explain the code in your own words.
# Write at least three sentences. There is no single correct wording.
# ----------------------------------------------------------------------
explanation_5 = ""  # TODO


# ----------------------------------------------------------------------
# Exercise 6 (medium): find and fix the bug.
# This function is supposed to return a new list with only the passing
# scores. It loses some scores instead. Fix it.
# ----------------------------------------------------------------------
def remove_failed(scores):
    # TODO: this works on some inputs and not others. Fix it.
    for score in scores:
        if score < 50:
            scores.remove(score)
    return scores


# ----------------------------------------------------------------------
# Exercise 7 (medium): write a function using a list comprehension.
# ----------------------------------------------------------------------
def passing_names(students):
    """Return the names of students who scored 60 or more, in the same order.

    students is a list of dictionaries, each with "name" and "score".
    An empty list gives an empty list.
    """
    # TODO
    raise NotImplementedError("exercise 7 is not written yet")


# ----------------------------------------------------------------------
# Exercise 8 (harder): predict the output.
# ----------------------------------------------------------------------
prediction_8 = []  # TODO


# ----------------------------------------------------------------------
# Exercise 9 (harder): write a function using a loop and a dictionary.
# ----------------------------------------------------------------------
def summarise_orders(orders):
    """Return one total per customer.

    orders is a list of dictionaries like
    [{"customer": "ada", "amount": 20}, {"customer": "ada", "amount": 10}]
    and the result is {"ada": 30}.
    An empty list gives an empty dictionary.
    """
    # TODO
    raise NotImplementedError("exercise 9 is not written yet")


# ----------------------------------------------------------------------
# Exercise 10 (harder): explain the difference between two versions.
# Write at least four sentences: what each version gives the caller, and
# which one you would choose for a function that another part of a bigger
# program has to use.
# ----------------------------------------------------------------------
explanation_10 = ""  # TODO


# ======================================================================
# Nothing below this line needs to be edited.
# ======================================================================

STOCK = {"pens": 3, "paper": 0, "ink": 7}


def compare_prediction(given, expected):
    """Compare a prediction without revealing the answer."""
    given = list(given)
    assert len(given) == len(expected), (
        f"you wrote {len(given)} lines, the program prints {len(expected)}"
    )
    for index, (mine, real) in enumerate(zip(given, expected), start=1):
        assert str(mine) == str(real), f"line {index} is not what the program prints"


def check_1():
    a, b = 9, 4
    expected = [str(a / b), f"{a // b} {a % b} {a ** 2}", str(round(a / b, 2))]
    compare_prediction(prediction_1, expected)


def check_2():
    name = "  Ada Lovelace  "
    clean = name.strip()
    parts = clean.split()
    expected = [
        clean,
        f"{clean[0]} {clean[-1]}",
        parts[0].upper() + " " + parts[1][:3],
        f"{len(clean)} {len(parts)}",
    ]
    compare_prediction(prediction_2, expected)


def check_3():
    assert describe_item("pen", 2) == "pen costs 2 dollars.", (
        f'got {describe_item("pen", 2)!r}'
    )
    assert describe_item("notebook", 12) == "notebook costs 12 dollars.", (
        f'got {describe_item("notebook", 12)!r}'
    )


def check_4():
    assert initials("ada lovelace") == "A.L."
    assert initials("  grace   brewster   murray ") == "G.B.M."
    assert initials("plato") == "P."


def check_5():
    assert len(explanation_5.split()) >= 20, (
        "write at least three full sentences, not a single phrase"
    )


def check_6():
    assert remove_failed([45, 80, 30, 55]) == [80, 55], (
        "the result should keep every score of 50 or more, in the original order"
    )
    assert remove_failed([40, 41, 42, 90]) == [90], (
        "three failing scores in a row should all be removed"
    )
    assert remove_failed([10, 20]) == [], "a list of failing scores should come back empty"
    assert remove_failed([90, 95, 100]) == [90, 95, 100], (
        "a list with no failing scores should come back unchanged"
    )


def check_7():
    students = [
        {"name": "ada", "score": 91},
        {"name": "bob", "score": 42},
        {"name": "cy", "score": 60},
    ]
    assert passing_names(students) == ["ada", "cy"]
    assert passing_names([]) == []


def check_8():
    available = {item: qty for item, qty in STOCK.items() if qty > 0}
    numbers = [x * 2 for x in range(1, 5) if x % 2 == 0]
    expected = [
        str(available),
        str(sorted(available, key=available.get)),
        str(sum(available.values())),
        str(numbers),
    ]
    compare_prediction(prediction_8, expected)


def check_9():
    orders = [
        {"customer": "ada", "amount": 20},
        {"customer": "bob", "amount": 5},
        {"customer": "ada", "amount": 10},
    ]
    assert summarise_orders(orders) == {"ada": 30, "bob": 5}
    assert summarise_orders([]) == {}


def check_10():
    assert len(explanation_10.split()) >= 30, (
        "write at least four full sentences"
    )


CHECKS = [
    ("1", check_1),
    ("2", check_2),
    ("3", check_3),
    ("4", check_4),
    ("5", check_5),
    ("6", check_6),
    ("7", check_7),
    ("8", check_8),
    ("9", check_9),
    ("10", check_10),
]


def main():
    passed = 0
    for number, check in CHECKS:
        try:
            check()
        except AssertionError as error:
            print(f"{number:>2}: FAIL  {error}")
        except NotImplementedError as error:
            print(f"{number:>2}: TODO  {error}")
        except Exception as error:
            print(f"{number:>2}: ERROR {type(error).__name__}: {error}")
        else:
            print(f"{number:>2}: PASS")
            passed += 1
    print(f"\n{passed} of {len(CHECKS)} checks passed")


if __name__ == "__main__":
    main()
