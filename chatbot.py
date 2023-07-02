import tkinter as tk
from tkinter import scrolledtext

class ChatBot:
    def __init__(self):
        self.responses = {
            'hello': 'Hi there!',
            'how are you?': 'I am fine, thank you!',
            'what is your name?': 'My name is ChatBot.',
            'what can you do?': 'I can answer questions and have simple conversations.',
            'who created you?': 'I was created by LAST-HOPE.',
            'how old are you?': 'I am an artificial intelligence and do not have an age.',
            'where are you from?': 'I exist in the digital world and do not have a physical location.',
            'what is the meaning of life?': 'The meaning of life is subjective and can vary for each individual.',
            'exit': 'Goodbye!',
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "I'm sorry, I don't understand."

def send_message():
    user_input = input_box.get("1.0", "end-1c")
    chat_log.configure(state='normal')
    chat_log.insert(tk.END, f"User: {user_input}\n")
    chat_log.insert(tk.END, f"ChatBot: {chatbot.get_response(user_input)}\n")
    chat_log.configure(state='disabled')
    input_box.delete("1.0", tk.END)

# Create the chatbot instance
chatbot = ChatBot()

# Create the GUI window
window = tk.Tk()
window.title("LAST-HOPE ChatBot")

# Create a scrolled text widget for displaying the chat log
chat_log = scrolledtext.ScrolledText(window, width=50, height=20)
chat_log.configure(state='disabled')
chat_log.pack()

# Create an input box for the user to type messages
input_box = tk.Text(window, width=50, height=2)
input_box.pack()

# Create a send button to send the user input
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Run the GUI event loop
window.mainloop()

