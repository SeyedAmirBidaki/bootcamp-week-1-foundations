# Week 1 project: a notes app in the terminal

**Track B. Cursor is allowed and expected here.** The exercises were yours
alone; this project is about learning to drive an AI assistant without
letting it think for you.

Time: about 5 to 6 hours, spread over the week. Do not leave it until the last
day.

Work in a folder called `project/` inside this week's folder, so the path is
`week-1-foundations/project/notes.py`. Keep `plan.md` and `ai-log.md` beside it.

---

## The goal

A command-line app, run with `python3 notes.py`, that keeps a list of short
notes in a file so they are still there when you run it again.

It must support these four actions:

| Command | What happens |
| --- | --- |
| list | print every note, numbered, oldest first |
| add | ask for the text of a note, save it to the end of the list |
| remove | ask for a number, delete that note |
| quit | leave the program |

A real session might look like this:

```
$ python3 notes.py
notes> add
text: buy milk
saved note 1
notes> add
text: email the tutor
saved note 2
notes> list
1. buy milk
2. email the tutor
notes> remove
number: 1
removed "buy milk"
notes> list
1. email the tutor
notes> quit
bye
```

Then running it again shows the one remaining note.

That is the whole specification. Everything else (how to store the data, how
to structure the code, how to handle a number that does not exist) is a
decision you make, and you will be asked to justify those decisions.

---

## Step 1: break it down before you open Cursor

Do this on paper or in a text file, before any prompt. Cursor should not see
the problem until you have written down your own plan. If you cannot break it
down, you are not ready to prompt, and the AI will fill the gap with guesses.

Answer these in a file called `plan.md`:

1. What data does the app hold while it is running? Write the actual shape.
   A list of strings? A list of dictionaries? Something else?
2. Where does that data live between runs? Name the file and the format.
3. Which functions or classes do you need? List them with a one-line
   description each, and what goes in and what comes out.
4. What are the four or five states the app can be in? ("waiting for a
   command", "asking for note text", "asking for a number to remove"...)
5. How will you handle each of these: an unknown command, a note number that
   does not exist, an empty note, a note containing a comma or a quote, the
   file not existing the first time?
6. How will you know it works? Write three things you will type that you
   expect to succeed, and two that you expect to be rejected cleanly.

Then number the pieces in the order you would build them. A sensible order
starts with the smallest thing that can be run at all, and adds one action at
a time.

Keep `plan.md`. It is part of what you submit, and it is where the interesting
comparison happens at the end.

---

## Step 2: how to prompt

The difference between a good prompt and a bad one is not politeness or
length. It is whether you have given the assistant the constraints it cannot
guess, and whether you have asked for something small enough to judge.

**A bad prompt:**

> write a notes app in python

Why it is bad: it hands over the entire design. You will get something that
runs, that you cannot explain, in a style you did not choose, and you will
learn nothing. If it breaks, you will not know where to look, because none of
the decisions were yours.

**A better prompt:**

> I am writing a small command-line notes app in Python 3.12, in a single file
> `notes.py`. Notes are kept in memory as a list of strings and saved to
> `notes.json` after every change. I have already written `load_notes()` and
> `save_notes()` myself and they work.
>
> I want to add the `add` command now. Write one function
> `add_note(notes, text)` that takes the list and the text, strips whitespace
> from the ends of the text, refuses to add an empty string by returning
> False, otherwise appends it and returns True. Do not write a main loop and
> do not touch the other commands.
>
> Show me the function, then explain in two sentences why you used the error
> handling you chose.

Why it is better: it names the file, the version, the data shape, and what
already exists. It asks for one function. It specifies the return values, so
you can test it. It forbids the AI from writing parts you want to write. And
it asks for a short explanation, which is where you find out whether the code
is right or merely plausible.

Three habits worth forming now:

- **One function or one behaviour per prompt.** "Now write the remove
  command" is a good second prompt. "Now write the whole app" is not.
- **Say what already exists.** AI writes code that duplicates functions you
  already have unless you tell it what you have.
- **Ask for the smallest version first**, get it running, then add. A program
  that lists notes and quits is a working program. Build from there.

---

## Step 3: build it in slices

Suggested slices, each one ending with something you can actually run:

1. **Skeleton.** The loop that reads a command and prints the four options,
   with every action a stub that prints "not implemented yet" and a `quit`
   that works. Prompt for this if you like; it is the least interesting part.
2. **Storage.** `load_notes()` and `save_notes()` reading and writing a JSON
   file. Test them from the shell in a separate five-line script before you
   wire them in. Handle "file does not exist yet" here, once.
3. **Add.** The first real action. Test that the file on disk changes.
4. **List.** Print the notes with numbers. Decide what an empty list prints.
5. **Remove.** Numbering is the trap: the number the user sees is one more
   than the list index, and it changes after every removal. Test removing the
   first, a middle one, and a number that does not exist.
6. **Polish.** Unknown commands, trailing spaces, a note that is only spaces,
   quitting without saving, and whatever else your `plan.md` listed.

At every slice, run the app and try to break it before you move on. Keep a
record of what broke.

---

## Step 4: read what the AI gives you

Before you paste anything into your file, read it and answer these:

- Which line does the work, and which lines are only there for safety?
- Does every branch have a path that returns or prints something sensible?
- Is it using a library function I have not met? Look it up in the docs; do
  not accept it because it looks professional.
- Would I have written this differently, and is my version wrong or just
  different?
- If I delete this line, what breaks? Try it once.

If you cannot answer the second question, you cannot accept the code yet. Ask
a follow-up prompt about that specific branch, then read the answer.

---

## Step 5: the AI log (required)

Create `ai-log.md` in this folder. It is part of the deliverable, and it is
the part that shows whether the project taught you anything.

For every prompt that produced code you kept, write:

```
### Prompt 3: remove a note

What I asked for: one function to delete by the number the user typed.
What I got: a function that deleted by list index, so typing 1 removed the
second note.
How I noticed: I added three notes and removed number 1; note 2 disappeared.
What I changed: subtracted 1 from the number before indexing, and added a
check for numbers outside the list.
What I would ask differently: I should have said the number shown to the user
starts at 1, which is the whole bug.
```

At least **three** entries are required. At least one of them must be a case
where the AI was wrong or incomplete. If every prompt worked first time,
either you were very lucky or you were not checking closely enough; go back
and test the edge cases from your `plan.md`.

An entry that says "it worked" is not an entry. Write what you checked and
what you expected to see.

---

## Step 6: compare with your plan

At the bottom of `ai-log.md`, write a short section called **What I kept and
what I changed**. Compare the finished app with `plan.md`: which of your
decisions survived, which did you abandon because the AI's version was
genuinely better, and which did you abandon only because it was easier? That
last category is the one to be honest about.

---

## Acceptance criteria

The app is done when all of these are true. Test each one, and write the
result in `ai-log.md` under a heading **Acceptance checks**.

1. `python3 notes.py` starts and shows a prompt. `quit` leaves cleanly.
2. `add` saves a note; `list` shows it numbered from 1; the file on disk
   changed (open it and look).
3. Notes survive quitting and restarting the app.
4. `remove 1` removes the *first* note shown, not the second.
5. Removing a number that is not in the list prints a message and does not
   crash or delete something else.
6. Adding an empty line, or a line of only spaces, does not create a note.
7. An unknown command prints something helpful and keeps the app running.
8. A note containing a comma, a quote, and a non-English character survives a
   save and reload unchanged.
9. Running the app when the notes file does not exist yet works, and creates
   it.
10. You can explain every line of `notes.py` to your brother without opening
    Cursor.

Number 10 is the real one. If it fails, the other nine do not count.

---

## Python concepts this should exercise

You should be able to point at a line in your own code for each of these:

- a list, used as the main data structure
- a dictionary, if you chose JSON objects, or indexing and slicing if you
  chose plain strings
- a `while` loop driving the command prompt
- `if` / `elif` / `else` for the command dispatch
- a function with arguments and a return value (`add_note`, `remove_note`)
- f-strings for the output
- `len()` and the difference between a user's number and a list index
- reading and writing a file (a preview of week 3; you may copy a working
  pattern here and understand it properly next week)
- at least one `try` / `except` around something that can genuinely fail, such
  as reading a file that might be missing or corrupt

If a concept is missing from your app, that is a sign the AI made a design
choice you did not notice.

---

## What "good" looks like

Not a long program. A **short** one you understand. Around 80 to 140 lines
with blank lines is normal for this; if you have 400, something has been
generated faster than you can read it.

Good signs:

- the main loop is short and reads like a table of contents
- each action is one function
- the file handling is in two small functions, not scattered
- there is exactly one place where the list is saved
- the messages the user sees are consistent

Weak signs:

- the same logic written twice in two places
- error handling that catches everything and silently continues
- a variable named `data` that holds four different kinds of thing
- code you cannot explain but that "seems to work"

---

## Stretch, if you finish early

Only after the acceptance criteria all pass. Pick one:

- Add an `edit` command that changes the text of an existing note.
- Add a `search` command that lists notes containing a word.
- Add timestamps to each note. This forces you to change the data shape from
  a list of strings to a list of dictionaries, which means reloading old files
  still has to work. That migration problem is real work and worth feeling
  once.
- Split the code into two files: one for storage, one for the interface.

---

## Submitting

```
git add week-1-foundations/
git commit -m "week 1 project: notes app"
git push
```

Then open a pull request into `main` so your brother can review it. The pull
request description should be three lines: what it does, what it does not do
yet, and which part you found hardest.
