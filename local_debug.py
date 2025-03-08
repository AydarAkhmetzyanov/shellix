from shellix.ai_core import process_input


def main():
    user_input = "Run pwd and ls commands"

    print("\nProcessing...\n")
    process_input(user_input)


if __name__ == "__main__":
    main()
