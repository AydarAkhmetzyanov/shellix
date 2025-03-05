import sys


def main():
    if len(sys.argv) > 1:
        # If arguments are provided, join them as the input message.
        user_input = " ".join(sys.argv[1:])
    else:
        # No arguments: start interactive multiline mode.
        print("Enter your input (submit an empty line to finish):")
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line == "":
                break
            lines.append(line)
        user_input = "\n".join(lines)

    print(user_input)


if __name__ == "__main__":
    main()
