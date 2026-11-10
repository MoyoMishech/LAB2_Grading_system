# Student Grading System

## Overview

The **Student Grading System** is a console-based Python program for recording student marks, assigning grades, displaying student records, and showing a class summary. It uses a menu to let the user choose what to do.

## Input–Process–Output (IPO) Plan

### Input
- Student number
- Student name
- Student mark

### Process
- Check that the student number and name are not blank.
- Check that the mark is numeric and between 0 and 100.
- Use `if`, `elif`, and `else` to assign a grade and decision.
- Store each student's information in a dictionary.
- Add each dictionary to the `students` list.
- Use loops to display records and calculate class statistics.

### Output
- A confirmation after a student is added.
- A report showing each student's number, name, mark, grade, and decision.
- The total number of students.
- The class average, highest mark, and lowest mark.
- The number of passes and fails.
- Informative messages for empty records or invalid menu choices.

## Features

The program provides four menu options:

1. **Add student** — Enter a student's number, name, and mark.
2. **Display all** — View all student records entered during the current run.
3. **Class summary** — View the total number of students, class average, highest mark, lowest mark, number of passes, and number of fails.
4. **Exit** — Close the program.

## Grading System

The program uses the grading scale provided in the lab assignment:

| Mark range | Grade | Decision |
|---|---|---|
| 80–100 | A | Excellent |
| 70–79 | B | Very good |
| 60–69 | C | Good |
| 50–59 | D | Pass |
| 0–49 | F | Fail |

A mark must be numeric and between **0 and 100**. If the input is not numeric or is outside this range, the program displays an error and asks the user to enter the mark again.

## Why a List of Dictionaries Is Suitable

A list of dictionaries is suitable because it allows the program to store many student records in one place. Each dictionary represents one student and contains the student's number, name, mark, grade, and decision. The list makes it possible to add more students and use loops to display their records or calculate class statistics.

## Requirements

- Python 3
- No additional Python packages are required.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Open Command Prompt or a terminal.
3. Move to the folder containing `grading_system.py`.
4. Run:

```bash
python grading_system.py
```

If your computer uses the `python3` command, run:

```bash
python3 grading_system.py
```

5. Follow the menu and enter `1`, `2`, `3`, or `4`.

## Example of Use

- Choose **1** to add a student.
- Enter the student's number, name, and mark when prompted.
- Choose **2** to display all student records.
- Choose **3** to view the class summary.
- Choose **4** to exit.

## How the Program Works

- Student details are stored as dictionaries with the keys `student_number`, `name`, `mark`, `grade`, and `decision`.
- Each dictionary is added to a list called `students`.
- The program uses `if`, `elif`, and `else` to assign grades.
- A `while` loop keeps displaying the menu until the user chooses option 4.
- A `for` loop displays student records and calculates class statistics.
- `try` and `except` are used to handle non-numeric mark input.
- The program checks for an empty class before calculating the average.

## Testing and Verification

Run each test and enter the actual result you observe in the last column. Do not mark a test as passed until you have run it.

| Test | Input or action | Expected result | Observed result |
|---|---|---|---|
| T1 | Add marks 79 and 80 | Grades B and A; both are passes | To be completed after testing |
| T2 | Add marks 49 and 50 | Grades F and D; first fails and second passes | To be completed after testing |
| T3 | Enter -1, 101, and `abc` as marks | Each invalid input is rejected and the program asks again without crashing | To be completed after testing |
| T4 | Choose Class summary before adding students | An informative empty-class message appears; no division-by-zero error | To be completed after testing |
| T5 | Enter an invalid menu option, such as 9 | A warning appears and the menu is shown again | To be completed after testing |

Save screenshots of the program while carrying out the tests. Put them in a folder named `screenshots` in the project folder. The screenshots should show the relevant input and program output.

## Reflection

1. **Why does the order of `if`/`elif` conditions matter at grade boundaries?**

   Python checks the conditions from top to bottom. The conditions must be arranged correctly so that a mark is assigned to the correct grade range.

2. **What error could arise when calculating the average of an empty list?**

   The program could cause a `ZeroDivisionError` because it would be dividing by zero students. The program checks whether the list is empty before calculating the average.

3. **How would you adapt the program to handle two courses per student?**

   I would add two course marks to each student's dictionary and calculate a grade and decision for each course separately.

## Important Note

Student records are kept in the program's memory while it is running. They are **not saved to a file or database**, so the records will be lost when the program is closed.

## Project Files

- `grading_system.py` — The Python source code for the Student Grading System.
- `README.md` — This file, which explains the program, plan, tests, and reflection.
- `screenshots/` — Screenshots showing the program tests (to be added after testing).
