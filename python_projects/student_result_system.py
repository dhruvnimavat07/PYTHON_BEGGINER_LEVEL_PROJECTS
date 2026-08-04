def student_result():
    """
    Store and display student result.

    Returns:
        None
    """

    all_students = []

    total_students = int(input("Enter Number of Students: "))

    for i in range(total_students):

        print("\nStudent", i + 1)

        name = input("Enter Student Name: ")

        total_subjects = int(input("Enter Number of Subjects: "))

        subject_list = []

        total_marks = 0

        for j in range(total_subjects):

            subject_name = input("Enter Subject Name: ")

            marks = float(input("Enter Marks: "))

            total_marks = total_marks + marks

            subject = {"subject_name": subject_name, "marks": marks}

            subject_list.append(subject)

        percentage = total_marks / total_subjects

        if percentage >= 90:
            grade = "A"

        elif percentage >= 75:
            grade = "B"

        elif percentage >= 60:
            grade = "C"

        else:
            grade = "Fail"

        student = {
            "name": name,
            "subjects": subject_list,
            "percentage": percentage,
            "grade": grade,
        }

        all_students.append(student)

    print("\n================ ALL STUDENT DETAILS ================\n")

    for student in all_students:

        print("Student Name :", student["name"])

        print("Subjects")

        for subject in student["subjects"]:

            print("   ", subject["subject_name"], "-", subject["marks"])

        print("Percentage :", round(student["percentage"], 2))
        print("Grade      :", student["grade"])

        print("----------------------------------------")

    highest = all_students[0]
    lowest = all_students[0]

    for student in all_students:

        if student["percentage"] > highest["percentage"]:
            highest = student

        if student["percentage"] < lowest["percentage"]:
            lowest = student

    print("\n========== HIGHEST RESULT ==========")

    print("Name :", highest["name"])
    print("Percentage :", round(highest["percentage"], 2))
    print("Grade :", highest["grade"])

    print("\n========== LOWEST RESULT ==========")

    print("Name :", lowest["name"])
    print("Percentage :", round(lowest["percentage"], 2))
    print("Grade :", lowest["grade"])


student_result()
