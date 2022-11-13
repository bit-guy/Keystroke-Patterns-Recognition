import pandas as pd
import string

char = list(string.printable[:-3])
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n

pairs = [a+b for a in char for b in char]
column_name = ['class'] + pairs

df = pd.DataFrame(columns=column_name)

user_input = input('This may replace your data.csv. Do you want to continue? (yes/no):\n')

if user_input.lower() == 'yes':
    df.to_csv("dataset/data.csv", index=False)
    print('Finish initiating data.csv')