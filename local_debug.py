import sys
from shellix.ai_core import process_input

COMMAND = "Run pwd and ls commands"

def main():
    user_input = sys.argv[1] if len(sys.argv) > 1 else COMMAND

    print("\nProcessing...\n")
    process_input(user_input)


if __name__ == "__main__":
    main()