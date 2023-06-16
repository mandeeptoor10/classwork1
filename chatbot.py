import tkinter as tk
import random

# Define some greetings and responses
greetings = [    "Hello, how are you doing today?",    "Hi there, how's your day going?",    "Hey, how are things with you?",]
responses = {
    "hello": "Hi there, how can I assist you today?",
    "hi": "Hello, what can I help you with?",
    "hey": "Hey there, how can I be of service?",
    "how are you": "I'm doing well, thanks for asking!",
    "what's up": "Not much, just chatting with you!",
    "weather": "The weather is currently sunny and 75 degrees.",
    "i love you": "I don't have feelings, I'm created by Mani Toor.",

    "i'm upset": "Don't feel sad, listen to some songs!",
    "how are you": "i m good thanmks  for asking, what about you",
    "i love you": "she loves you too",
    "i fuck you": "i dont have ass and pussy",
    "you like me": "yes i like you your preety good",
    "have u spend a night with someone to do sex": "i dont have emotions and feelings ",
    "can you do me a fevor": " sure i can help you in every cases ",
    "i need to complete my home work ": "do your work by your self ",
    "please": " sure tell em how i can help if ican i will do ",
    "may your name": " im just cahat system which is created by mani toor",
    "you are so amazing": 'yes i know i m amzing',
    "thank you ": "your welcome  im always here for help",
    "toor":" he created me its his surname, his full anme is mani Toor "
    
    }

# Function to generate responses
def get_response(user_message):
    if user_message in responses:
        return responses[user_message]
    else:
        return "Sorry, I don't understand. Can you please rephrase?"

# Function to send messages and get responses
def send_message(event=None):
    user_message = user_input.get()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_message + "\n")
    chat_history.insert(tk.END, "Bot: " + get_response(user_message) + "\n\n")
    chat_history.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)

# Function to create the GUI
def create_gui():
    global user_input, chat_history

    root = tk.Tk()
    root.title("Chatbot")

    # Set background color and font size for chat history
    chat_history = tk.Text(root, height=20, width=50, bg="lightgreen", fg="grey", font=("Arial", 14))
    chat_history.config(state=tk.DISABLED)

    # Set background color and font size for user input field
    user_input = tk.Entry(root, width=50, bg="white", fg="black", font=("Arial", 14))
    user_input.bind("<Return>", send_message)

    # Set background color and font size for send button
    send_button = tk.Button(root, text="Send", command=send_message, bg="blue", fg="white", font=("Arial", 14))

    # Instructions for the user
    instructions_label = tk.Label(root, text="Enter your message below and press 'Send' or press 'Enter' to send the message.", font=("Arial", 12))
    instructions_label.pack()

    # Set background color for the GUI window
    root.config(bg="lightgray")

    chat_history.pack()
    user_input.pack(side=tk.LEFT)
    send_button.pack(side=tk.RIGHT)

    user_input.focus_set()

    root.mainloop()

if __name__ == '__main__':
    create_gui()