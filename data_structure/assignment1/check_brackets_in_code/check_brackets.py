# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False
def checker(text):
    stack = []
    for i, next in enumerate(text,start=1):
        if next == '(' or next == '[' or next == '{':
            stack.append(Bracket(next,i))
        elif next == ')' or next == ']' or next == '}':
            if not stack:
                return i
            top=stack.pop()
            if not top.Match(next):
                return i
    if stack:
        top=stack.pop()
        return top.position
    return "Success"
if __name__ == "__main__":
    text = sys.stdin.read().strip("\n")
    print (checker(text))


        # Process closing bracket, write your code here

    # Printing answer, write your code here
