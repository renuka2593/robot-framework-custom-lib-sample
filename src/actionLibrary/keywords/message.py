from robot.api.deco import keyword

class Messgae:

    @keyword
    def print_custom_message(self, message):
        print(f"Custom message: {message}")

