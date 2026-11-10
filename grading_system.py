# Student Grading System

students = []

while True:
    print("\n===== STUDENT GRADING SYSTEM =====")
    print("1. Add student")
    print("2. Display all")
    print("3. Class summary")
    print("4. Exit")
    option = input("Choose 1-4: ").strip()

    if option == "1":
        student_number = input("Enter student number: ").strip()
        while student_number == "":
            print("Error: student number cannot be blank.")
            student_number = input("Enter student number: ").strip()

        name = input("Enter student name: ").strip()
        while name == "":
            print("Error: name cannot be blank.")
            name = input("Enter student name: ").strip()

        mark = None
        while mark is None:
            raw_mark = input("Enter mark (0-100): ").strip()
            try:
                value = float(raw_mark)
            except ValueError:
                print("Error: mark must be a number (e.g. 65). Try again.")
            else:
                if 0 <= value <= 100:
                    mark = value
                else:
                    print("Error: mark must be between 0 and 100. Try again.")

        if mark.is_integer():
            mark = int(mark)

        if mark >= 80:
            grade = "A"
            decision = "Excellent"
        elif mark >= 70:
            grade = "B"
            decision = "Very good"
        elif mark >= 60:
            grade = "C"
            decision = "Good"
        elif mark >= 50:
            grade = "D"
            decision = "Pass"
        else:
            grade = "F"
            decision = "Fail"

        record = {
            "student_number": student_number,
            "name": name,
            "mark": mark,
            "grade": grade,
            "decision": decision,
        }
        students.append(record)

        print(f"\nRecord added: {name} ({student_number}) - "
              f"Mark: {mark}, Grade: {grade}, Decision: {decision}")

    elif option == "2":
        if len(students) == 0:
            print("\nNo student records yet. Choose option 1 to add a student.")
        else:
            print("\n----------------------- STUDENT REPORT -----------------------")
            print(f"{'Student No.':<14}{'Name':<24}{'Mark':>6}  {'Grade':<7}{'Decision'}")
            print("-" * 66)
            for student in students:
                print(f"{student['student_number']:<14}"
                      f"{student['name']:<24}"
                      f"{student['mark']:>6}  "
                      f"{student['grade']:<7}"
                      f"{student['decision']}")
            print("-" * 66)

    elif option == "3":
        if len(students) == 0:
            print("\nNo student records yet, so there is no summary to show.")
            print("Choose option 1 to add students first.")
        else:
            total_students = 0
            total_marks = 0
            highest = students[0]["mark"]
            lowest = students[0]["mark"]
            passes = 0
            fails = 0

            for student in students:
                total_students += 1
                total_marks += student["mark"]

                if student["mark"] > highest:
                    highest = student["mark"]
                if student["mark"] < lowest:
                    lowest = student["mark"]

                if student["mark"] >= 50:
                    passes += 1
                else:
                    fails += 1

            average = total_marks / total_students  # Safe because class is not empty.

            print("\n========== CLASS SUMMARY ==========")
            print(f"Total students : {total_students}")
            print(f"Class average  : {average:.2f}")
            print(f"Highest mark   : {highest}")
            print(f"Lowest mark    : {lowest}")
            print(f"Passes (>= 50) : {passes}")
            print(f"Fails  (< 50)  : {fails}")
            print("===================================")

    elif option == "4":
        print("\nGoodbye! Exiting the Student Grading System.")
        break

    else:
        print("\nInvalid option. Please enter 1, 2, 3 or 4.")
