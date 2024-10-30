import time
import random


class MainProgram:

    def greeting(self):
        print("Welcome to Haiku Bot!")
        print("What would you like to do?")

    def get_answer(self):
        print("1. Generate new haiku")
        print("2. View past haikus")
        print("3. Exit")
        answer = input("Please enter the corresponding number.\n")

        return answer

    def fulfill_answer(self):
        answer = self.get_answer()
        print("Please wait. One command at a time.\n")
        time.sleep(1)
        while True:
            if answer == "1":
                input_or_rand = input("1. Input Haiku Topic\n"
                                      "2. Generate Random Haiku\n")
                self.haiku(input_or_rand)
                break
            elif answer == "2":
                # Show past haikus
                pass
            elif answer == "3":
                # Exit haiku bot
                print("Thank you for using Haiku Bot! Session will now be closed.\n")
                return 1
            else:
                "Number not recognized. Please enter 1, 2, or 3.\n"
                answer = input("Please enter the corresponding number.\n")

    def haiku(self, user_input):
        if user_input == "1":
            pass
        if user_input == "2":
            output = self.generate_random_haiku()
            return output

    def generate_random_haiku(self):
        random_haikus = {
            1: "Just because where you\n"
               "Are doesn't seem right, doesn't\n"
               "Mean that it is wrong",
            2: "Cool, calm refreshing\n"
               "Fast, slow, but always moving\n"
               "All around the world",
            3: "Dangerous and wild\n"
               "Destroys all things in its wake\n"
               "Can't be tamed and harsh"
        }
        random_num = random.randint(1, 3)
        print(random_haikus[random_num])


if __name__ == "__main__":
    program = MainProgram()
    program.greeting()

    while True:
        continue_loop = program.fulfill_answer()
        if continue_loop:
            break
