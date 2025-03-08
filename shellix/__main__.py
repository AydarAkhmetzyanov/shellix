import os
import sys
from shellix.ai_core import process_input

def main():
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        print("Enter your input and Ctrl+D twice to execute):")
        # Read all input from stdin until EOF
        user_input = sys.stdin.read().strip()

    print("\nProcessing...\n")
    process_input(user_input)


if __name__ == "__main__":
    main()
