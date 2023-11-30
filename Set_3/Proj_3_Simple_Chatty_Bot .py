class Chatty_Bot:
    def __init__(self, bot_name, birth_year):
        self.bot_name = bot_name
        self.birth_year = birth_year
        self.person_name = None
        self.person_age = None

    def greet(self):
        print(f'Hello! My name is {self.bot_name}.\n'
              f'I was created in {self.birth_year}')

    def remind_name(self):
        print('Please, remind me your name.')
        self.person_name = input()
        print(f'What a great name you have, {self.person_name}!')

    def guess_age(self):
        print('Let me guess your age.\n'
              'Enter remainders of dividing your age by 3, 5 and 7.')
        rem3 = int(input())
        rem5 = int(input())
        rem7 = int(input())
        self.person_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
        print(f"Your age is {self.person_age}; that's a good time to start programming!")

    @staticmethod
    def count():
        print('Now I will prove to you that I can count to any number you want.')
        num = int(input())
        curr = 0
        while curr <= num:
            print(f"{curr}!")
            curr = curr + 1

    @staticmethod
    def test():
        print("Let's test your programming knowledge.\n"
              "Why do we use methods?\n"
              "1. To repeat a statement multiple times.\n"
              "2. To decompose a program into several small subroutines.\n"
              "3. To determine the execution time of a program.\n"
              "4. To interrupt the execution of a program.\n")
        user_ans = int(input())
        while user_ans != 2:
            print("Please, try again.")
            user_ans = int(input())

    @staticmethod
    def end():
        print('Congratulations, have a nice day!')

    def run(self):
        Chatty_Bot.greet(self)
        Chatty_Bot.remind_name(self)
        Chatty_Bot.guess_age(self)
        Chatty_Bot.count()
        Chatty_Bot.test()
        Chatty_Bot.end()


Chatty_Bot('Chester', '2023').run()
