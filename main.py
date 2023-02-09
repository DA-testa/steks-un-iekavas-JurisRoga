# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            if not opening_brackets_stack:
                print(i+1)
                return
            elif not are_matching(next, next):
                print(i+1)
            opening_brackets_stack.pop()
            # Process closing bracket, write your code here
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    print("Success")
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
