
# ==================================================
# PROJECT 1: RULE-BASED AI CHATBOT
# DecodeLabs Industrial Training Kit - Batch 2026
# ==================================================

import string


def normalize_input(text):
    """Convert input to lowercase and remove extra spaces
    and common punctuation."""
    text = text.lower().strip()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = " ".join(text.split())
    return text


def chatbot():

    print("=" * 50)
    print("       INTELLIGENT RULE-BASED AI CHATBOT")
    print("=" * 50)
    print("Hello! I am your Python-based chatbot.")
    print("Type 'help' to view available commands.")
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print("-" * 50)

    # Knowledge base: intent phrases mapped to responses
    responses = {
        # Greetings
        "hello": "Hello! Welcome. How can I help you?",
        "hi": "Hi there! Nice to meet you.",
        "hey": "Hey! What would you like to talk about?",
        "good morning": "Good morning! Have a productive day!",
        "good afternoon": "Good afternoon! How can I help?",
        "good evening": "Good evening! Hope you are doing well.",

        # Chatbot information
        "what is your name": "I am a Rule-Based AI Chatbot built using Python.",
        "who are you": "I am a chatbot that responds using predefined rules.",
        "who created you": "I was developed as an Artificial Intelligence project.",
        "what can you do": "I can greet you and answer predefined questions.",
        "how are you": "I am functioning well! Thanks for asking.",

        # AI and programming
        "what is ai": "AI stands for Artificial Intelligence.",
        "what is artificial intelligence":
            "Artificial Intelligence enables computers to perform tasks "
            "that normally require human intelligence.",
        "what is python":
            "Python is a readable, high-level programming language.",
        "what is a chatbot":
            "A chatbot is a program that communicates with users through "
            "text or voice.",
        "what is rule based ai":
            "Rule-based AI uses predefined rules and conditions to "
            "produce responses.",
        "what is a dictionary":
            "A Python dictionary stores information as key-value pairs.",
        "what is a loop":
            "A loop repeats a block of code until its stopping condition "
            "is reached.",

        # Help and commands
        "help":
            "Available commands: hello, how are you, what is AI, "
            "what is Python, tell me a joke, motivation, stats, and bye.",
        "commands":
            "Type help to see available topics, or bye to exit.",
        "thanks": "You are welcome! Happy to help.",
        "thank you": "You are welcome! Keep learning.",

        # Fun and motivation
        "tell me a joke":
            "Why do programmers prefer dark mode? Because light attracts bugs!",
        "motivation":
            "Every expert was once a beginner. Keep learning and improving!",
        "i am sad":
            "I am sorry you are having a difficult day. Take a breath "
            "and remember that small steps matter.",
        "good night": "Good night! Rest well and keep learning."
    }

    # Alternative phrases that map to existing intents
    aliases = {
        "how are you doing": "how are you",
        "whats your name": "what is your name",
        "your name": "what is your name",
        "tell me about yourself": "who are you",
        "define ai": "what is ai",
        "define python": "what is python",
        "tell me a joke": "tell me a joke",
        "show commands": "commands",
        "i need help": "help",
        "i need motivation": "motivation",
        "thanks a lot": "thanks"
    }

    exit_commands = {"bye", "exit", "quit"}

    # Session statistics
    total_inputs = 0
    recognized_inputs = 0
    unknown_inputs = 0

    # Continuous conversation loop
    while True:

        raw_input_text = input("\nYou: ")
        user_input = normalize_input(raw_input_text)

        # Empty input validation
        if not user_input:
            print("Bot: Please enter a message.")
            continue

        # Count non-empty user messages
        total_inputs += 1

        # Exit strategy
        if user_input in exit_commands:
            print("\nBot: Goodbye! Thank you for chatting.")
            break

        # Built-in command: session statistics
        elif user_input == "stats":
            print("\n--- SESSION SUMMARY ---")
            print("Messages received:", total_inputs)
            print("Recognized messages:", recognized_inputs)
            print("Unknown messages:", unknown_inputs)
            continue

        # Resolve alternative phrases
        elif user_input in aliases:
            intent = aliases[user_input]
        else:
            intent = user_input

        # Dictionary lookup and fallback
        if intent in responses:
            reply = responses[intent]
            recognized_inputs += 1
        else:
            reply = (
                "I don't understand that yet. Try 'help' to see "
                "what I can answer."
            )
            unknown_inputs += 1

        print("Bot:", reply)

    # Final session report
    print("\n" + "=" * 40)
    print("          CHAT SESSION REPORT")
    print("=" * 40)
    print("Total messages:", total_inputs)
    print("Recognized messages:", recognized_inputs)
    print("Unknown messages:", unknown_inputs)
    print("Thank you for using the chatbot!")
    print("=" * 40)


# Program entry point
if __name__ == "__main__":
    chatbot()
