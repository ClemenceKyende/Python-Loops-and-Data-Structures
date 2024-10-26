def ask_for_input():
    """
    Continuously prompts the user for input, printing each entry
    until the user types "exit" to stop the loop.
    """
    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print(user_input)

# Run the function
ask_for_input()
