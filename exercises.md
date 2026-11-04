# Week 1 exercises

Ten exercises. No AI, no code completion, no chat window. You may use
`python3` itself, the official documentation at docs.python.org, and your own
notes. The rules file explains exactly where the line is.

Work in `exercises_template.py` next to this file. Every exercise below has a
matching number there, with a stub and a check. Run it as often as you like:

```
python3 exercises_template.py
```

Do the exercises in order. If one takes more than 40 minutes, write down what
you tried in a note and move on; come back to it the next day. Finishing all
ten matters less than knowing which ones you cannot yet do.

Marks: **easy** should take 5 to 10 minutes. **medium** should take 15 to 25.
**harder** can take 40. These are honest estimates for someone who has just
finished OOP, not a test of speed.

---

## 1. Predict the output — easy

Read this code. Without running it, write down exactly what it prints, one
line per `print`, as three strings in `prediction_1`.

```python
a = 9
b = 4
print(a / b)
print(a // b, a % b, a ** 2)
print(round(a / b, 2))
```

Then run it in a Python shell (`python3` with no file name) and compare. If
you were wrong, work out why before moving on. Write your three strings into
the list, in order.

---

## 2. Predict the output — easy

```python
name = "  Ada Lovelace  "
clean = name.strip()
parts = clean.split()
print(clean)
print(clean[0], clean[-1])
print(parts[0].upper() + " " + parts[1][:3])
print(len(clean), len(parts))
```

Four `print` calls, so four strings in `prediction_2`. Pay attention to the
spaces: several of these lines print two values separated by one space,
because that is what a comma does inside `print`.

---

## 3. Find the bug — easy

This function looks reasonable and fails the moment it is called.

```python
def describe_item(item, price):
    return item + " costs " + price + " dollars."
```

Call it with `describe_item("pen", 2)`. Read the error message. It tells you
the type on each side of the `+`. Fix the function so both example calls pass,
without changing the function's name or its parameters.

One hint, since this is the first bug of the course: there are two ways to fix
it, and only one of them is the way most Python developers write this line
today.

---

## 4. Write a function — medium

Specification:

```
initials(full_name) -> str
  Take a person's full name and return their initials, each followed by a
  full stop. Extra spaces anywhere in the name are ignored.

  initials("ada lovelace")            -> "A.L."
  initials(" grace brewster murray ")  -> "G.B.M."
  initials("plato")                   -> "P."
```

The template already contains these three checks, so you can see when it is
right. Think about what `split()` does to the messy middle one before you
write any code.

---

## 5. Explain this code — medium

```python
def checkout(prices):
    total = 0
    for price in prices:
        total += price
    if total > 100:
        total = total * 0.9
    return total
```

In at least three sentences, in `explanation_5`, explain what this function
does and what it returns for `checkout([100])` and `checkout([60, 60])`. Say
out loud, in your own words, why those two results are not what a shopper
might expect. Then check yourself in the shell.

This exercise is marked on whether you noticed the detail, not on elegant
prose.

---

## 6. Find the bug — medium

The function is meant to return a new list holding only the passing scores.
It works on the first example and quietly loses data on others.

```python
def remove_failed(scores):
    for score in scores:
        if score < 50:
            scores.remove(score)
    return scores
```

Try `remove_failed([45, 80, 30, 55])` and then
`remove_failed([40, 41, 42, 90])`. Both should keep every score of 50 or more.
The second one does not, and it is not random: work out what happens to the
position of the items as the loop runs, then write a version that cannot have
this problem at all.

Also answer this in a comment at the top of your function: does the returned
list have to be a new list, or is changing the caller's list acceptable here?
The specification says "return a new list", so decide accordingly.

---

## 7. Write a function — medium

```
passing_names(students) -> list of str
  students is a list of dictionaries, each with "name" and "score".
  Return the names of the students who scored 60 or more, in the original
  order. An empty list gives an empty list.

  [{"name": "ada", "score": 91},
   {"name": "bob", "score": 42},
   {"name": "cy",  "score": 60}]        -> ["ada", "cy"]
```

Write it first as a normal loop. Then, once the checks pass, rewrite the body
as a single list comprehension and confirm the checks still pass. Being able
to move between the two forms is the point; the comprehension is not
automatically better, it is just shorter to read once you are used to it.

---

## 8. Predict the output — harder

```python
stock = {"pens": 3, "paper": 0, "ink": 7}

available = {item: qty for item, qty in stock.items() if qty > 0}
print(available)
print(sorted(available, key=available.get))
print(sum(available.values()))

numbers = [x * 2 for x in range(1, 5) if x % 2 == 0]
print(numbers)
```

Four lines of output, four strings in `prediction_8`. Two traps here: what a
dictionary looks like when printed, and what `sorted` does with a key
function that returns numbers rather than names.

---

## 9. Write a function — harder

```
summarise_orders(orders) -> dict
  orders is a list of dictionaries with "customer" and "amount".
  Return one total per customer. Customers keep the order in which they
  first appear. An empty list gives an empty dictionary.

  [{"customer": "ada", "amount": 20},
   {"customer": "bob", "amount": 5},
   {"customer": "ada", "amount": 10}]   -> {"ada": 30, "bob": 5}
```

No `defaultdict`, no imports. Use a plain dictionary and the `.get` method.
Ask yourself before writing: on the first order for a customer, what should
the running total be, and what does `.get` give you when the key is missing?

---

## 10. Explain the difference — harder

Two functions do "the same thing" in different ways.

```python
def checkout_printing(prices):
    total = sum(prices)
    print(f"Total: {total}")

def checkout_returning(prices):
    return sum(prices)
```

In at least four sentences in `explanation_10`, answer:

1. What can a caller do with the result of each version?
2. Where in a real program would you use each one?
3. Why is `sum` a better building block than the manual loop in exercise 5,
   even though the loop is not wrong?

The third question is the interesting one. There is no single correct answer,
but a good answer mentions that `sum` already exists, is tested, and reads as
one idea rather than four lines.

---

## When you have finished

Run the file one final time. Write the final count ("x of 10 checks passed")
in `week-1-foundations/README.md` where the definition of done asks for it,
then commit:

```
git add week-1-foundations/exercises_template.py week-1-foundations/README.md
git commit -m "week 1 exercises"
git push
```

You can leave an exercise unfinished. Note which one and why, in the same
README, and move on to the project. The quiz at the end of the week will show
you whether it was one exercise or a whole idea that did not land.
