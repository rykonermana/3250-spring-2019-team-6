from jvpm.OpCodes import *


class DemoCode:

    def main_menu(self):
        print("In Main Menu")
        print("Please select an option")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: Exit")
        choice = input()
        while choice != 5:
            decider = {"1": add, "2": subtract, "3": multiply, "4": divide}
            decider.get(choice, lambda: "Invalid")()
            print("Please select an option")
            print("1: Add")
            print("2: Subtract")
            print("3: Multiply")
            print("4: Divide")
            print("5: Exit")
            choice = input()


    def add(self):
        print("Adding two numbers")
        print("Input first value")
        op.push_to_stack(input())
        print("Input second number")
        op.push_to_stack(input())
        op.add()
        print("Result: " + op.pop_from_stack())


    def subtract(self):
        print("Subtracting two numbers")
        print("Input first value")
        a = input()
        print("Input second number")
        op.push_to_stack(input())
        op.push_to_stack(a)
        op.sub()
        print("Result: " + op.pop_from_stack())

    def multiply(self):
        print("Multiplying two numbers")
        print("Input first value")
        op.push_to_stack(input())
        print("Input second number")
        op.push_to_stack(input())
        op.mul()
        print("Result: " + op.pop_from_stack())

    def divide(self):
        print("Dividing two numbers")
        print("Input numerator")
        op.push_to_stack(input())
        print("Input denominator")
        op.push_to_stack(input())
        op.div()
        print("Result: " + op.pop_from_stack())


def main():
    op = OpCodes()
    main_menu()


if __name__ == "__main__":
    main()
