1️⃣ Importing the re module
import re
This imports the re module, which allows us to use regular expressions (regex) for pattern matching.
Regular expressions help identify keywords in user input without requiring an exact match.

--

2️⃣ Displaying the Chatbot's Greeting

print("Chatbot: Hello! I'm your AI assistant. Type 'exit' to end the conversation.")
The chatbot greets the user and explains how to exit.
This message appears when the chatbot starts.
--

3️⃣ Running an Infinite Loop
while True:
The chatbot runs inside a while True loop, meaning it keeps running until explicitly stopped.
It ensures continuous interaction until the user types "exit" or "bye".
--

4️⃣ Taking User Input
user_input = input("You: ").lower()
The chatbot asks for user input and stores it in user_input.
.lower() converts the input to lowercase so that variations like "Hello" and "hello" are treated the same.
--

5️⃣ Handling Greetings
if re.search(r"\b(hi|hello|hey|hola)\b", user_input):
    print("Chatbot: Hello! How can I assist you today?")
re.search(r"\b(hi|hello|hey|hola)\b", user_input)
Searches for greeting words in user input.
\b ensures only whole words match (e.g., "highlight" won’t match "hi").
If a match is found, the chatbot responds with "Hello! How can I assist you today?".
--
6️⃣ Responding to Name-Related Queries
elif re.search(r"\b(your name|who are you)\b", user_input):
    print("Chatbot: I am a simple chatbot designed to assist you.")
Checks if the user asks for the chatbot’s name or identity.
If detected, the chatbot introduces itself.
--

7️⃣ Responding to "How Are You?"
elif re.search(r"\b(how are you|how's it going)\b", user_input):
    print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
Detects if the user asks about the chatbot’s well-being.
The chatbot responds in a friendly way and asks how the user is doing.
--

8️⃣ Answering Python-Related Questions
elif re.search(r"\b(python|learn python|python programming)\b", user_input):
    print("Chatbot: Python is a versatile programming language used for AI, web development, and more.")
If the user mentions "Python", the chatbot provides a brief description of it.
Useful for basic programming assistance.
--

9️⃣ Responding to Chatbot Capability Questions
elif re.search(r"\b(what can you do|your abilities|your features)\b", user_input):
    print("Chatbot: I can answer simple questions, chat with you, and provide basic programming information.")
Checks if the user asks what the chatbot can do.
The chatbot explains its basic features and purpose.
--

🔟 Handling Farewell Messages (Exit Condition)
elif re.search(r"\b(bye|exit|goodbye|see you)\b", user_input):
    print("Chatbot: Goodbye! Have a great day!")
    break
Detects if the user wants to exit using words like "bye", "exit", or "goodbye".
If matched, the chatbot says goodbye and exits the loop using break.
--

1️⃣1️⃣ Handling Unrecognized Input
else:
    print("Chatbot: I'm sorry, I didn't understand that. Can you rephrase?")
If no predefined pattern is found in the user input, the chatbot asks the user to rephrase the question.
--

1️⃣2️⃣ Running the Chatbot
chatbot()
This calls the chatbot() function to start the chatbot.
However, this line is unnecessary since the function was already defined. The chatbot should be executed directly within the script instead.
--
Example Chat Session:

Chatbot: Hello! I'm your AI assistant. Type 'exit' to end the conversation.
You: Hi
Chatbot: Hello! How can I assist you today?
You: What is Python?
Chatbot: Python is a versatile programming language used for AI, web development, and more.
You: What can you do?
Chatbot: I can answer simple questions, chat with you, and provide basic programming information.
You: Bye
Chatbot: Goodbye! Have a great day!
--

Key Features of This Chatbot
✅ Pattern Matching (re.search()): Allows flexible input recognition.
✅ Looping for Continuous Conversation: Runs until the user decides to exit.
✅ Lowercase Input Handling: Avoids case sensitivity issues.
✅ Multiple Response Categories: Can handle greetings, questions, and farewells.
✅ Graceful Exit (break): Stops the chatbot when the user wants to leave.
