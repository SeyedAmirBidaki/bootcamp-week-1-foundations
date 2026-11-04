# Week 1 hints

One hint per exercise. None of them is an answer. Read a hint only after you
have spent real time on the exercise: try the code, read the error, print the
intermediate values. The point of getting stuck for a while is that the fix
sticks afterwards.

If a hint is not enough, the next step is the official documentation, not this
file. Search docs.python.org for the thing named in the hint.

---

**1 — predictable output.** Look at the operator, not at your memory of
school maths. `/` always gives a float in Python 3, even when the division
comes out whole. `//` throws away the fraction; `%` gives what is left over.
Run `print(9 / 2, 9 // 2, 9 % 2)` and compare that with the exercise, then
apply the same reading to it.

**2 — predictable output.** Count the characters by hand, spaces included:
the original string has 16, and the stripped one has 12. Two of the four lines
print a length, so be sure which string each `len` is measuring. Then remember
that indexing happens after the strip, and that `parts[1][:3]` takes three
characters from the *second word*, not from the whole string.

**3 — find the bug.** Read the `TypeError` message character by character. It
says which type is on the left and which is on the right of the `+`. You
cannot glue a number to a string without converting something. There is a
string-formatting tool from the beginning of the course that converts for you
and that most people use instead of `+` today.

**4 — initials.** `"  grace   brewster   murray ".split()` gives you a clean
list of three words whatever the spacing. From each word you need exactly one
character. Build the result by adding `"."` after each initial, then think
about whether `"".join(...)` or a plain loop is easier to read.

**5 — explain this code.** The question is not "what does a checkout do". It
is "what does this checkout do for a total of exactly 100". Compare `>` with
`>=` in your head, then run both versions.

**6 — find the bug.** Print the list after every iteration of the loop.
Watch where the loop's position points after you remove an item. The fix is
not to delete more carefully; it is to build the result you want instead of
editing the list you were given. A comprehension does this in one line.

**7 — passing names.** You have a list of dictionaries, and you want a list of
strings. Each dictionary is one student: `student["score"]` for the condition,
`student["name"]` for the result. Write the loop version first; it is easier to
get right, and converting it afterwards is mechanical.

**8 — predictable output.** Print `stock` on its own first, then the
dictionary comprehension. For `sorted` with a key, write the list of
`(quantity, item)` pairs by hand and sort that on paper. Which item has the
smallest quantity among the available ones?

**9 — summarise orders.** You need to add to a value that may not exist yet.
`totals.get(customer, 0)` gives you either the running total or a zero, and
then you add the new amount to it and store it back. Do not forget to store it
back.

**10 — explain the difference.** Ask what the caller receives in each case.
One function hands back nothing, which in Python is the value `None`. What can
you do with `None`? What can you do with a number? Then think about where a
`print` still belongs in a program that is bigger than one file.
