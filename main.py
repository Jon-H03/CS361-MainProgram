import time

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
                # Call haiku function
                pass
            elif answer == "2":
                # Show past haikus
                pass
            elif answer == "3":
                break
            else:
                "Number not recognized. Please enter 1, 2, or 3.\n"
                answer = input("Please enter the corresponding number.\n")
