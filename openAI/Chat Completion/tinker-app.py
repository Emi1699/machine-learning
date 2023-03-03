import tkinter as tk
import modes
import openai_api

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 500



def process_input():
    input_text = input_box.get("1.0", "end-1c") # Get the text from the input box
    input_box.delete('1.0', tk.END) # clear input box

    # generate chatbot response
    output_text = openai_api.text_text(input_text)

    # display response
    output_box.delete("1.0", tk.END) # Clear the output box
    output_box.insert(tk.END, output_text) # Insert the processed text into the output box

root = tk.Tk()
root.title("J.A.R.V.I.S")

input_label = tk.Label(root, text="> query: ")
input_label.pack()

input_box = tk.Text(root, height=5, width=100)
input_box.pack()

output_label = tk.Label(root, text="> answer: ")
output_label.pack()

output_box = tk.Text(root, height=30, width=100)
output_box.pack()

process_button = tk.Button(root, text="Process", command=process_input)
process_button.pack()

root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')

root.mainloop()