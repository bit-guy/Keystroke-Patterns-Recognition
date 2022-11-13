import tkinter as tk
from timeit import default_timer as timer
import string
import pandas as pd

char = list(string.printable[:-3]) # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n
keyTimestamp = [] # list of timestamp for each key release
paragraph = "abcdef"*100

def get_paragraph():
    df = pd.read_csv("dataset/paragraph.csv")
    return df["Paragraph"].sample(1).values[0]

def save_data():
    # get data from input
    textVal = (inputText.get('1.0', tk.END))[:-1]
    nameVal = (inputName.get('1.0', tk.END))[:-1]
    Digraph = dict()
    for i in char:
        for j in char:
            Digraph[i+j] = []
    for i in range(0,len(keyTimestamp)-1):
        if textVal[i:i+2] in Digraph.keys():
            Digraph[textVal[i:i+2]].append(keyTimestamp[i+1]-keyTimestamp[i])
    map = {key: (sum(val)/len(val)) for key,val in Digraph.items() if Digraph[key] != []}
    map['class'] = nameVal
    
    # append data to dataset/data.csv
    df = pd.read_csv('dataset/data.csv')
    df2 = pd.Series(map)
    df = df.append(df2, ignore_index=True)
    df.to_csv("dataset/data.csv", index=False)

    print('Saved')
    window.destroy()

window = tk.Tk()
window.title('Please Type the Following Paragraph')

label_1 = tk.Label(window, text = "The paragraph :")
label_1.pack()

message = tk.Text(window, 
    width = 120, 
    height= 15,
    )
message.insert(tk.END, get_paragraph())
message.pack(padx=10, pady=5)

label_2 = tk.Label(window, text = "Typing here :")
label_2.pack()

inputText = tk.Text(window, 
    width = 120, 
    height = 15,
    )
inputText.bind('<KeyRelease>', lambda event: keyTimestamp.append(timer()))
inputText.pack(padx=10, pady=5)

frame = tk.Frame()
label_3 = tk.Label(frame, text = "Enter your full name :")
label_3.pack(side=tk.LEFT)

inputName = tk.Text(frame, 
    width = 50,
    height = 1
    )
inputName.pack(side=tk.LEFT)

button = tk.Button(frame, 
    text = "DONE", 
    command = save_data,
    width = 5, 
    bg = 'grey'
    )
button.pack(side=tk.LEFT)
frame.pack(padx=10, pady=5)

tk.mainloop()