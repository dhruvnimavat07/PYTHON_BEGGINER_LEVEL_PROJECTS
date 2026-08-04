class Quiz:
    """
    Beginner Level Python Quiz Project
    """

    def __init__(self):
        self.name = ""
        self.email = ""
        self.college = ""
        self.score = 0
        self.wrong_answers = []

        self.questions = [
            {
                "q": "Which keyword is used to create a function?",
                "o": ["function", "define", "def", "fun"],
                "a": 3,
            },
            {
                "q": "Which symbol is used for comments?",
                "o": ["//", "#", "<!--", "**"],
                "a": 2,
            },
            {
                "q": "Which data type stores multiple values?",
                "o": ["int", "list", "float", "bool"],
                "a": 2,
            },
            {
                "q": "Which loop repeats a fixed number of times?",
                "o": ["for", "if", "break", "pass"],
                "a": 1,
            },
            {
                "q": "Which function takes user input?",
                "o": ["print()", "input()", "type()", "len()"],
                "a": 2,
            },
            {
                "q": "What is the output type of input()?",
                "o": ["int", "float", "str", "list"],
                "a": 3,
            },
            {
                "q": "Which keyword is used for conditions?",
                "o": ["loop", "elif", "switch", "case"],
                "a": 2,
            },
            {
                "q": "Which function displays output?",
                "o": ["show()", "display()", "print()", "echo()"],
                "a": 3,
            },
            {
                "q": "Which collection uses []?",
                "o": ["tuple", "list", "set", "dict"],
                "a": 2,
            },
            {
                "q": "Which keyword ends a loop early?",
                "o": ["continue", "break", "stop", "exit"],
                "a": 2,
            },
        ]

    def get_user_details(self):
        print("===== USER DETAILS =====")
        self.name = input("Name: ")
        self.email = input("Email: ")
        self.college = input("College: ")

    def start_quiz(self):
        print("\n===== PYTHON QUIZ =====")
        no = 1
        for q in self.questions:
            print("\nQuestion", no)
            print(q["q"])
            for i, opt in enumerate(q["o"], 1):
                print(i, ".", opt)
            try:
                ans = int(input("Choose (1-4): "))
            except:
                ans = 0
            if ans == q["a"]:
                print("Correct")
                self.score += 1
            else:
                print("Wrong")
                self.wrong_answers.append(
                    {"question": q["q"], "your": ans, "correct": q["o"][q["a"] - 1]}
                )
            no += 1

    def show_result(self):
        total = len(self.questions)
        percentage = (self.score / total) * 100
        status = "PASS" if percentage >= 70 else "FAIL"

        print("\n===== RESULT =====")
        print("Name:", self.name)
        print("Email:", self.email)
        print("College:", self.college)
        print("Score:", self.score, "/", total)
        print("Percentage:", round(percentage, 2), "%")
        print("Status:", status)

        if self.wrong_answers:
            print("\n===== WRONG ANSWERS =====")
            for item in self.wrong_answers:
                print("\nQuestion:", item["question"])
                print("Correct Answer:", item["correct"])
        else:
            print("\nExcellent! All answers are correct.")


quiz = Quiz()
quiz.get_user_details()
quiz.start_quiz()
quiz.show_result()
