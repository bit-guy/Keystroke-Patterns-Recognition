import tkinter as tk
from timeit import default_timer as timer
import string
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.metrics.pairwise import nan_euclidean_distances

char = list(string.printable[:-3])
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n
keyTimestamp = [] # list of timestamp for each key release
data_path = "dummy_dataset/data.csv"

def knn(x_data, y_data, test_data, k):
    result = nan_euclidean_distances(x_data,[test_data])
    argmin_k = np.argsort(result, axis=0)[:k]
    print(result)
    print(argmin_k)
    return stats.mode([y_data[i] for i in argmin_k])[0]

def get_paragraph():
    df = pd.read_csv("dataset/paragraph.csv")
    return df["Paragraph"].sample(1).values[0]

def get_sentence():
    textVal = (inputText.get('1.0', tk.END))[:-1]
    Digraph = dict()
    for i in char:
        for j in char:
            Digraph[i+j] = []
    for i in range(0,len(keyTimestamp)-1):
        if textVal[i:i+2] in Digraph.keys():
            Digraph[textVal[i:i+2]].append(keyTimestamp[i+1]-keyTimestamp[i])
    new_dict = {key: (sum(val)/len(val)) for key,val in Digraph.items() if Digraph[key] != []}

    train_data = pd.read_csv(data_path)
    test_data = pd.Series(new_dict)
    y_data = train_data.pop('class')
    x_data = train_data[test_data.index]
    print(knn(y_data, x_data, test_data, k=3))

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

button = tk.Button(window, 
    text = "DONE", 
    command = get_sentence,
    width = 5, 
    bg = 'grey'
    )
button.pack(padx=10, pady=5)

tk.mainloop()