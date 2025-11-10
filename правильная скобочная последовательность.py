def is_valid_bracket_sequence(s):
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return "no"
            if stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return "no"

    return "yes" if not stack else "no"


def main():
    sequence = input().strip()
    print(is_valid_bracket_sequence(sequence))


if __name__ == "__main__":
    main()


регулярные выражения