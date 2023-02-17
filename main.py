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
    if not len(opening_brackets_stack) == 0:
        print(opening_brackets_stack[-1].position)
        return 0
            
def main():
    mismatch = 1
    parbaude = input()
    if parbaude == "I":
        text = input()
        mismatch = find_mismatch(text)
    elif parbaude == "F":
        text = input()
        mismatch = find_mismatch(text)

    if not mismatch == 0:
        print("Success")
    # Printing answer, write your code here
    #print("Success")

if __name__ == "__main__":
    main()
