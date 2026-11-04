# Week 1: foundations

**Theme:** the pieces of Python you already met, used without a safety net.
Strings, lists, dictionaries, loops, conditionals and comprehensions, at the
level where you can read a piece of code and say what it will do before
running it.

**Time:** 15 to 20 hours, spread across the week. Do not plan to do it in two
days; the second day of an exercise is where the learning happens.

---

## What you will be able to do by Sunday

- Read a short program and predict what it prints, including the awkward
  cases: integer division, negative indices, dictionary ordering.
- Find a bug from the error message and the type of the values, without
  guessing.
- Write a function from a written specification, including edge cases.
- Choose between mutating a list you were given and returning a new one, and
  say why.
- Use a list comprehension where it reads better, and a loop where it does not.
- Drive Cursor on a small project: plan first, prompt in slices, read the
  output critically, and keep a log of what the AI got wrong.
- Commit and push work on a branch, and open a pull request.

---

## Before you start

You should have finished week 0. That means: Git installed, a GitHub account,
the repo cloned, and the three drills done. If `git clone` and `git push` are
still mysterious, do week 0 first; this week assumes them.

You should also be able to run `python3 --version` in a terminal and get a
number starting with 3.10 or higher, and `python3 notes.py`-style commands
should not surprise you.

---

## What to read and watch

Reading beats watching here, but a little of each is fine. Do not spend more
than about 90 minutes in total on this section; the exercises are the week.

**Read, in the official tutorial** (docs.python.org/3/tutorial/):

- sections 3 and 4, "An Informal Introduction" and "More Control Flow Tools"
- section 5, "Data Structures", at least the parts on lists, dictionaries and
  looping techniques
- the page on built-in functions, but only the entries for `len`, `range`,
  `sorted`, `sum`, `enumerate` and `zip`

Read those with the exercises open beside them. Skim on the first pass; you
are building a map, not memorising.

**Watch, if you prefer video:** any recent "Python lists and dictionaries for
beginners" and "Python list comprehensions explained" video will do. Prefer
one shorter than 30 minutes each. If a video is teaching you `print("hello")`
and how to install Python, it is too basic for this week.

**Bookmark these three, because you will need them all course:**

- docs.python.org/3/library/functions.html — every built-in, one paragraph each
- docs.python.org/3/tutorial/errors.html — the errors chapter, for week 3
- the Python style guide, PEP 8, at pep8.org — read only the naming and
  whitespace sections for now

---

## The shape of the week

| Day | Work | Time |
| --- | --- | --- |
| 1 | Read the tutorial sections. Exercises 1 to 3. | 2 to 3 h |
| 2 | Exercises 4 to 6. Write `project/plan.md` for the project in the evening. | 2 to 3 h |
| 3 | Exercises 7 to 8. Start the project: skeleton and storage. | 2 to 3 h |
| 4 | Exercises 9 and 10. Project: add, list, remove. | 2 to 3 h |
| 5 | Project: polish and the edge cases from your plan. | 2 to 3 h |
| 6 | Project: acceptance checks, AI log, pull request. Quiz. | 2 to 3 h |
| 7 | Buffer. Anything unfinished, or the stretch task. | 1 to 3 h |

Two sessions a day of about 90 minutes, with a break between, works better
than one long one. Stop in the middle of something you understand rather than
at the end of something you do not.

---

## This week's work

1. **[exercises.md](exercises.md)** — ten exercises, no AI. Work in
   `exercises_template.py`; it checks your answers as you go.
2. **[hints.md](hints.md)** — one nudge per exercise, no answers. Read a hint
   only after real effort, and never before you have run the code once.
3. **[project.md](project.md)** — the Cursor project: a terminal notes app.
   Read all of it before you start, including the acceptance criteria.
4. **The quiz** — sent by your brother, since it lives in his private solutions repo. Ten questions, 20 minutes, closed book.

Do the exercises before the project. The project will use the same ideas, and
having just written them by hand is what makes the AI's output judgeable.

---

## Definition of done

All of the following, committed to your `week-1` branch:

- [ ] `exercises_template.py` runs and reports at least 8 of 10 checks passing.
- [ ] The two exercises you did not finish are named here, with one sentence
      on where you got stuck.
- [ ] `project/notes.py` runs, and all ten acceptance checks in `project.md`
      pass. You have written the result of each check in `project/ai-log.md`.
- [ ] `project/plan.md` exists and was written before you prompted.
- [ ] `project/ai-log.md` has at least three entries, one of them a real AI
      mistake, and the "What I kept and what I changed" section.
- [ ] You can explain every line of `project/notes.py` out loud.
- [ ] The quiz is done and scored.
- [ ] A pull request is open into `main` with the three-line description.

Fill in below before you open the pull request:

```
Final exercise score: ___ of 10
Unfinished exercises and why:

Quiz score: ___ of 10
Hardest part of the week:
Easiest part:
```

---

## If this week feels wrong

Two things to watch for, and what they mean.

**The exercises take twice as long as the estimates.** Normal, especially for
the predict-the-output ones; you are training a skill, not recalling a fact.
Do not skip them and go to Cursor. Give it two more days before you conclude
anything.

**You understand the code the AI writes but cannot write it yourself.**
Different problem, and worth taking seriously. The usual cause is reading
code instead of writing it. Go back to the exercises and type them from
scratch, with the AI closed. If you cannot, the AI is doing the learning for
you, and week 2 will feel much worse.

If neither applies and you are simply not enjoying it, note that too. It is
information, not a failure, and it belongs in the conversation with your
brother at the end of week 4.

---

[← Back to the course hub](https://github.com/SeyedAmirBidaki/python-bootcamp) · [Course rules](https://github.com/SeyedAmirBidaki/python-bootcamp/blob/main/rules.md)
