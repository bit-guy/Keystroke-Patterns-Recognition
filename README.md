# Keystroke Pattern Recognition
Like fingerprint, keystroke pattern is considered as biometrics which is unique to each indiviuals. By using classification algorithm such as K-nearest neighbor, we can managed to distinguish and authenticate the user giving the keystroke data of their typing rhythm.
# Usage
## Initiate template dataset
~~~
$ python init_data.py
~~~
This will empty the keystroke data in dataset ("dataset/data.csv").

---
## Add user's keystroke data to the dataset
~~~
$ python add_data.py
~~~
This will activate GUI for typing (using [tkinter](https://docs.python.org/3/library/tkinter.html)). By typing in the textbox below, the program will store the typing rhythm and generating a new row of data in the dataset. After entering user's full name or "class", the data will then append to the dataset.
## GUI for Typing

![image](https://github.com/Gyoowai/Keystroke-Patterns-Recognition/blob/master/images/gui_addData.png)

---
## Using recognizer
~~~
$ python main.py
~~~
Same as adding data, this will activate GUI for typing and collecting typing rhythm to match classes in the dataset. After clicking "DONE", the result will be shown in the command line output.

![image](https://github.com/Gyoowai/Keystroke-Patterns-Recognition/blob/master/images/result.png)

---
2110413 Computer Security, Department of Computer Engineering, Chulalongkorn University
