import time
import random
import requests

HAIKU_API_URL = "http://127.0.0.1:5001/generate-haiku"
DATETIME_API_URL = "http://127.0.0.1:5002/datetime"
VALIDATOR_API_URL = "http://127.0.0.1:5003/validate-haiku"


class MainProgram:

    def greeting(self):
        print("Welcome to Haiku Bot!")
        print("What would you like to do?")

    # IH3: User has freedom to read documentation if they need it, and jump straight to the app's main function if not.
    # IH4: The structure of the main menu will not be changed so that current users will never have to look hard for the
    # features relevant to them, even with updates.
    # IH6: The documentation provides an explicit path through through the task in its current state. When the user-
    # generated option is added, there will be an explicit path provided for that as well.
    # IH8: Users are free to select any option in its current state without breaking the app. When more functionality is
    # added, users should expect the same level of freedom without worrying about breaking the app.
    def get_answer(self):
        print("1. Generate new haiku")
        print("2. Documentation & Usage")  # IH1, IH2,
        print("3. Exit")
        answer = input("Please enter the corresponding number.\n")

        return answer

    def fulfill_answer(self):
        answer = self.get_answer()
        print("Please wait.\n")
        time.sleep(1)
        while True:
            if answer == "1":
                # IH5: Make the option to back out of the haiku menu, if a user needs to return to the main menu.
                # IH7: User has the option to generate a random haiku or input a topic for the haiku to be based on.
                input_or_rand = input("1. Input Haiku Topic\n"
                                      "2. Generate Random Haiku\n"
                                      "3. Go back to main menu\n")
                self.haiku(input_or_rand)
                break
            elif answer == "2":
                # Show documentation (IH #...)
                self.print_documentation()
                return 0
            elif answer == "3":
                # Exit haiku bot
                print("Thank you for using Haiku Bot! Session will now be closed.\n")
                return 1
            else:
                "Number not recognized. Please enter 1, 2, or 3.\n"
                answer = input("Please enter the corresponding number.\n")

    def haiku(self, user_input):
        #  For user generated Haiku
        if user_input == "1":
            topic = input("What would you like your Haiku to be about?\n")

            # Build payload for API
            payload = {
                "topic": topic
            }

            try:
                response = requests.post(HAIKU_API_URL, json=payload)
                response.raise_for_status()

                data = response.json()
                haiku = data.get("haiku")

                is_valid = self.validate_haiku(haiku)

                print(f"Haiku about {topic}\n\n", haiku, "\n")
                self.get_datetime()
                if is_valid:
                    print("Haiku was validated as 5-7-5 syllables.\n")
                else:
                    print("Haiku was invalidated as 5-7-5 syllables.\n")
            except requests.exceptions.RequestException as e:
                print("Error:", e)

        if user_input == "2":
            self.generate_random_haiku()

    def generate_random_haiku(self):
        random_haikus = {
            1: "Just because where you\n"
               "Are doesn't seem right, doesn't\n"
               "Mean that it is wrong\n",
            2: "Cool, calm refreshing\n"
               "Fast, slow, but always moving\n"
               "All around the world\n",
            3: "Dangerous and wild\n"
               "Destroys all things in its wake\n"
               "Can't be tamed and harsh\n"
        }
        random_num = random.randint(1, 3)
        print(random_haikus[random_num])

    def get_datetime(self):
        try:
            response = requests.get(DATETIME_API_URL)
            response.raise_for_status()
            data = response.json()
            print(data["date_time"], "\n")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def validate_haiku(self, haiku):
        try:
            response = requests.post(VALIDATOR_API_URL, json={"haiku": haiku})
            data = response.json()
            status = data.get("valid")

            if status:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print("Error:", e)


    def print_documentation(self):
        with open("documentation.txt", "r") as f:
            print(f.read())


if __name__ == "__main__":
    program = MainProgram()
    program.greeting()

    while True:
        continue_loop = program.fulfill_answer()
        if continue_loop:
            break
