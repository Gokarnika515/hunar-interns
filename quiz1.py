class Quiz :
    def __init__(self):
        self.questions = [
            {
                "question": "What country has the highest life expectancy?",
                "options": ["A) India", "B) Poland", "C) Hong Kong", "D) Berlin"],
                "answer": "C"
            },
            {
                "question": "How many elements are there in the periodic table?",
                "options": ["A) 112", "B) 119", "C) 116", "D) 118"],
                "answer": "D"
            },
            {
                "question": "What company was originally called Cadabra?",
                "options": ["A) Microsoft", "B) Apple", "C) Google", "D) Amazon"],
                "answer": "D"
            },
            {
                "question": "What country drinks the most coffee per captia?",
                "options": ["A) Rome", "B) Spanish", "C) Finland", "D) Scottland"],
                "answer": "C"
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": ["A) O2", "B) H2O", "C) CO2", "D) NaCl"],
                "answer": "B"
            },
            {
                "question": "What is the fourth letter of the greek alphabet?",
                "options": ["A) Alpha", "B) Delta", "C) Gama", "D) Beta"],
                "answer": "B"
            },
            {
                "question": "Which planet has the most moons?",
                "options": ["A) Earth", "B) Venus", "C) Saturn", "D) Mars"],
                "answer": "C"
            },
            {
                "question": "How many minutes are in a full week?",
                "options": ["A) 10,200", "B) 10,080", "C) 11,000", "D) 10,008"],
                "answer": "B"
            },
            {
                "question": "What year was the United Nations established?",
                "options": ["A) 1945", "B) 1947", "C) 1948", "D) 1950"],
                "answer": "A"
            },
            {
                "question": "What is the most common surname in United States?",
                "options": ["A) John", "B) Bailey", "C) Kim", "D) Smith"],
                "answer": "D"
            },
            {
                "question": "How many time zones are there in Russia?",
                "options": ["A) 9", "B) 2", "C) 11", "D) 10"],
                "answer": "C"
            },
            {
                "question": "What is the smallest country in the World?",
                "options": ["A) The Vatican", "B) Portugal", "C) Italy", "D) Antarctica"],
                "answer": "A"
            },
            {
                "question": "What is the longest river in the World?",
                "options": ["A) The Ganga", "B) The Nile", "C) Amazon River", "D) Mississippi River"],
                "answer": "B"
            },
            {
                "question": "when was Netflix founded?",
                "options": ["A) 2001", "B) 1998", "C) 1997", "D) 2004"],
                "answer": "C"
            },
            {
                "question": "How many days it take for the Earth to orbit the Sun?",
                "options": ["A) 365", "B) 366", "C) 364", "D) 360"],
                "answer": "A"
            },
        ]
        self.score = 0

    def ask_question(self, question_list):
        print(question_list["question"])
        for option in question_list["options"]:
            print(option)

        answer = input("Select answer (A, B, C, D): ").strip().upper()
        if answer == question_list["answer"]:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer was {questions_list['answer']}.\n")

    def run_quiz(self):
        print("Welcome to the Quiz! Let's get started.\n")
        for question in self.questions:
            self.ask_question(question)

        print(f"Quiz finished! Your final score is: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()
