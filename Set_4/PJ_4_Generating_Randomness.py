import random


class Ai():
    def __init__(self, minlen=100):
        self.minlen = minlen
        self.store = ''
        self.triads = ["000", "001", "010", "011", "100", "101", "110", "111"]

    def UserInpts(self):

        print("Please provide AI some data to learn...")
        print(f"The current data length is {str(len(self.store))},"
              f" {str(self.minlen - len(self.store))} symbols left")
        while len(self.store) < self.minlen:
            print("Print a random string containing 0 or 1:\n")
            userin = input()
            for i in userin:
                if i.isnumeric():
                    if int(i) == 1 or int(i) == 0:
                        self.store += i
            if len(self.store) < self.minlen:
                print(f"The current data length is {str(len(self.store))},"
                      f" {str(self.minlen - len(self.store))} symbols left")
        print(f"\nFinal data string: \n"
              f"{self.store}\n")

    def learn(self):
        k = 0
        results = dict.fromkeys(self.triads, [0, 0])
        while k < len(self.triads):
            x = 0
            y = 0
            i = 0
            newstring = self.store
            t = len(newstring)
            while i < t - 3:
                if newstring[0:3] == self.triads[k]:
                    if newstring[3] == "0":
                        x += 1
                        results[self.triads[k]] = [x, y]
                    if newstring[3] == "1":
                        y += 1
                        results[self.triads[k]] = [x, y]
                newstring = newstring[1:]
                i += 1
            k += 1
        prob = dict.fromkeys(self.triads, [0, 0])
        for key in results:
            values = results[key]
            prob1 = values[0] / (values[0] + values[1])
            prob2 = values[1] / (values[0] + values[1])
            prob[key] = [prob1, prob2]
        return prob

    def game(self, money=1000, stop=0):
        prob = self.learn()
        print(f"You have ${money}. Every time the system successfully predicts your next press, you lose $1.")
        print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!\n')
        while money > 0 and stop != 1:
            # Playng the game
            # game_userin = ""
            passed = 0
            while passed == 0:
                print("Print a random string containing 0 or 1:")
                game_userin = input()
                if game_userin == "enough":
                    stop = 1
                    break
                game_string = ""
                for s in game_userin:
                    if s.isnumeric():
                        if int(s) == 1 or int(s) == 0:
                            game_string += s
                if len(game_string) >= 4:
                    passed = 1
            if stop == 1:
                break
            firtsthree = ""
            while len(firtsthree) != 3:
                t = str(random.randrange(2))
                firtsthree += t
            finalstring = firtsthree
            test = game_string[3:]
            for s in test:
                if len(test) > 3:
                    for key in prob:
                        add = ""
                        if test[0:3] == key:
                            q = prob[key]
                            if q[0] > q[1]:
                                add = str(0)
                            elif q[1] > q[0]:
                                add = str(1)
                            else:
                                add = str(random.randrange(2))
                            finalstring += add
                            test = test[1:]
                            break
            count = 0
            nice = 0
            for s in game_string[3:]:
                if game_string[count + 3] == finalstring[count]:
                    nice += 1
                count += 1
            totall = len(finalstring)
            x = totall - nice
            y = nice - x
            money = money - y
            print(f"predictions:\n {finalstring}")
            print(f"Computer guessed {str(nice)} out of {str(len(finalstring))} symbols right \n"
                  f" {str(round((nice / (len(finalstring)) * 100), 2))}%\n"
                  f"Your balance is now ${money}")
        print("Game over!")

    def run(self):
        self.UserInpts()
        self.learn()
        self.game()


Ai(100).run()
