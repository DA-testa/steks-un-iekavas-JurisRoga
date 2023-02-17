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
            #print("burkans")
            # Process opening bracket, write your code here
            
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                print(i+1)
                #print("abols")
                return 0
            opening_brackets_stack.pop()
            # Process closing bracket, write your code here
    if len(opening_brackets_stack) == 0:
        return "Success"
    elif not len(opening_brackets_stack) == 0:
        return opening_brackets_stack[-1].position
            
def main():
    mismatch = 0
    parbaude = input()
    if parbaude == "I":
        text = input()
        mismatch = find_mismatch(text)
    elif parbaude == "F":
        text = open(test, "r")
        mismatch = find_mismatch(text)

    if not mismatch == 0:
        print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
