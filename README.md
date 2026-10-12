# DecodeLabs-Rule-Based-AI-Chatbot
Project 1: A beginner-friendly rule-based AI chatbot built using Python for the DecodeLabs Industrial Training Kit, Batch 2026.
# Rule-Based AI Chatbot

**DecodeLabs Industrial Training Kit — Project 1 | Batch 2026**

## 1. Project Overview

The Rule-Based AI Chatbot is a beginner-friendly Python project that demonstrates how a chatbot can interact with users through predefined rules and responses.

The chatbot accepts text input, processes the user's message, and provides an appropriate response based on a predefined knowledge base. It also handles unknown messages, supports alternative phrases, and displays session statistics.

This project introduces the fundamental concepts of artificial intelligence, Python programming, and rule-based decision-making.

## 2. Project Objectives

- Develop a simple interactive chatbot using Python.
- Understand how predefined rules map user inputs to responses.
- Implement input normalization to handle uppercase letters, whitespace, and punctuation.
- Use conditional statements and loops to control program execution.
- Handle unknown inputs through fallback responses.
- Provide a clean exit mechanism and a summary of the chat session.

## 3. Features

- **Interactive conversation:** Accepts multiple messages in a single session.
- **Predefined knowledge base:** Uses a Python dictionary to store messages and responses.
- **Input normalization:** Converts input to lowercase, removes common punctuation, and normalizes whitespace.
- **Alternative phrases:** Maps supported alternative expressions to existing responses.
- **Help command:** Displays available topics and commands.
- **Fallback handling:** Responds politely when a message is not recognized.
- **Session statistics:** Displays message counts, recognized inputs, and unknown inputs.
- **Exit commands:** Supports `bye`, `exit`, and `quit`.
- **Final session report:** Displays conversation statistics when the chatbot exits.

## 4. Technologies Used

- **Programming language:** Python
- **Development environment:** Thonny
- **Python concepts:** Functions, dictionaries, loops, conditional statements, string processing, and counters
- **Standard library:** Python's built-in `string` module

## 5. Requirements

- Python 3 installed on your computer.
- Thonny Python IDE or another Python-compatible editor.
- The project source file: `chatbot2.py`.

No external Python packages are required.

## 6. How to Run the Project in Thonny

1. Open Thonny on your computer.
2. Open the `chatbot2.py` file.
3. Save the file using **Ctrl + S**.
4. Click **Run → Run current script**, or press **F5**.
5. Wait for the welcome message to appear in the Shell.
6. Type a message and press Enter to interact with the chatbot.
7. Type `help` to view available topics.
8. Type `stats` to view session statistics.
9. Type `bye`, `exit`, or `quit` to end the conversation.

## 7. Sample Conversation

```text
==================================================
       INTELLIGENT RULE-BASED AI CHATBOT
==================================================
Hello! I am your Python-based chatbot.
Type 'help' to view available commands.
Type 'bye', 'exit', or 'quit' to end the chat.
--------------------------------------------------

You: hello
Bot: Hello! Welcome. How can I help you?

You: what is ai
Bot: AI stands for Artificial Intelligence.

You: what is python
Bot: Python is a readable, high-level programming language.

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: unknown question
Bot: I don't understand that yet. Try 'help' to see what I can answer.

You: bye
Bot: Goodbye! Thank you for chatting.

==================================================
          CHAT SESSION REPORT
==================================================
Total messages: 6
Recognized messages: 4
Unknown messages: 1
Thank you for using the chatbot!
==================================================
```

*Note: This is an illustrative example. Actual statistics depend on the messages entered during a session.*

## 8. How It Works

The chatbot follows the Input–Process–Output (IPO) model.

1. **Input:** Accepts a message from the user.
2. **Processing:** Normalizes the input, checks exit commands and aliases, and searches the predefined knowledge base.
3. **Output:** Displays the matching response or a fallback message.

The program continues running in a loop until the user enters an exit command.

## 9. Limitations

- The chatbot uses predefined rules and responses rather than a trained machine-learning model.
- It cannot reliably answer questions that are not covered by its knowledge base.
- It does not automatically learn from previous conversations.
- It does not use external APIs or online language models.
- Its response accuracy depends on the rules and alternative phrases defined in the source code.

## 10. Learning Outcomes

Through this project, I learned how to:

- Build a simple interactive application using Python.
- Store and retrieve information using dictionaries.
- Apply loops and conditional statements.
- Normalize and validate user input.
- Handle unknown inputs gracefully.
- Track session statistics using counters.
- Test program behavior with different inputs.
- Understand the basic operation and limitations of rule-based chatbots.

## 11. Future Enhancements

Possible future improvements include:

- Adding more intents and alternative phrases.
- Separating the knowledge base from the main program.
- Creating a graphical user interface.
- Adding automated tests for input handling and response selection.
- Exploring semantic matching or a language-model-based chatbot in a separate project.

## 12. Project Structure

```text
DecodeLabs-Rule-Based-AI-Chatbot/
├── chatbot2.py
└── README.md
```

## 13. Conclusion

This project demonstrates the fundamentals of building a rule-based chatbot using Python. It provides practical experience with input processing, predefined responses, decision-making, fallback handling, and program control flow.

The project serves as a foundation for exploring more advanced chatbot techniques and artificial intelligence applications.

---

**Project:** Rule-Based AI Chatbot  
**Program:** DecodeLabs Industrial Training Kit  
**Batch:** 2026  
**Language:** Python
