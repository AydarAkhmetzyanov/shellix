import os
import sys
from shellix.ai_core import process_input
from shellix.memory import clear_memory

def main():
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        print("Enter your input and Ctrl+D twice to execute):")
        # Read all input from stdin until EOF
        user_input = sys.stdin.read().strip()
        print(user_input)

    print("\nProcessing...\n")
    if user_input.lower() == 'clear':
        clear_memory()
        print('Memory cleared successfully.')
    else:
        process_input(user_input)


if __name__ == "__main__":
    main()
