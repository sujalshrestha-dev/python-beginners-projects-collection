import random
import time


class MathQuiz:
    def __init__(self, operator_choice, total_problems):
        self.total_problems = total_problems
        self.correct = 0
        self.wrong = 0
        self.MIN_OPERAND = 3
        self.MAX_OPERAND = 12

        if operator_choice == "1":
            self.operators = ["+"]
        elif operator_choice == "2":
            self.operators = ["-"]
        elif operator_choice == "3":
            self.operators = ["*"]
        else:
            self.operators = ["+", "-", "*"]

    def generate_problem(self):
        left = random.randint(self.MIN_OPERAND, self.MAX_OPERAND)
        right = random.randint(self.MIN_OPERAND, self.MAX_OPERAND)
        operator = random.choice(self.operators)
        expr = str(left) + " " + operator + " " + str(right)
        answer = eval(expr)
        return expr, answer

    def run(self):
        input("Press Enter to start!")
        print("-------------------------------------")

        start_time = time.time()

        for i in range(self.total_problems):
            expr, answer = self.generate_problem()
            while True:
                guess = input(f"Problem #{i + 1}: {expr} = ")
                if guess == str(answer):
                    print("Correct!")
                    self.correct += 1
                    break
                else:
                    print("Wrong, try again!")
                    self.wrong += 1

        end_time = time.time()
        total_seconds = end_time - start_time
        minutes = int(total_seconds // 60)
        seconds = round(total_seconds % 60, 2)

        print("-------------------------------------")
        print(f"Nice work! You completed {self.total_problems} problems.")
        print(f"Correct answers      : {self.correct}")
        print(f"Total wrong attempts : {self.wrong}")
        print(f"Time taken           : {minutes}m {seconds}s")


class Menu:
    def show(self):
        print("=====================================")
        print("         MATH QUIZ GAME")
        print("=====================================")
        print("1. Only Addition")
        print("2. Only Subtraction")
        print("3. Only Multiplication")
        print("4. All Operations")
        print("=====================================")

    def get_operator_choice(self):
        while True:
            choice = input("Select mode (1-4): ")
            if choice in ["1", "2", "3", "4"]:
                return choice
            print("Invalid choice, please enter 1 to 4.")

    def get_total_problems(self):
        while True:
            try:
                total = int(input("How many problems do you want? "))
                if total > 0:
                    return total
                print("Please enter a number greater than 0.")
            except ValueError:
                print("Invalid input, please enter a number.")


menu = Menu()
menu.show()
operator_choice = menu.get_operator_choice()
total_problems = menu.get_total_problems()

quiz = MathQuiz(operator_choice, total_problems)
quiz.run()