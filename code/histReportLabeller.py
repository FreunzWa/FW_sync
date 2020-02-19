import pandas as pd
import os
import tkinter as tk
import numpy as np

PATH_TO_CSV = "~/Documents/sync/code/"
FORM_NAME = "Histology Report Labeller"
FNAME = "histRadReports.csv"
reportDataFrame = pd.read_csv(PATH_TO_CSV+FNAME)
ind = 0

if not 'pathDiagnosis' in reportDataFrame:
    #create a new empty column for the diagnosis number to sit in.
    reportDataFrame['pathDiagnosis'] = pd.DataFrame()
    print("Added the PathDiagnosis column to the DataFrame ")

#get a list of histology reports
reports = reportDataFrame['histReport']

class CustomText(tk.Text):
    '''
    text = CustomText()
    text.tag_configure("red", foreground="#ff0000")
    text.highlight_pattern("this should be red", "red")

    The highlight_pattern method is a simplified python
    version of the tcl code at http://wiki.tcl.tk/3246
    '''
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")

def update_progress():
    return "Progress: "+str(ind+1)+"/"+str(len(reports))+" ===  %"+str(100*float(ind+1)/len(reports))
#When button is pressed the next report is shown
def record_label(labelText):
    global ind
    print(labelText)
    reportDataFrame['pathDiagnosis'].at[ind] = labelText
    ind+=1
    text.delete(1.0, tk.END)
    label['text'] = "Current Label: " + str(reportDataFrame['pathDiagnosis'].at[ind])

    try:
        text.insert(tk.INSERT, reports[ind])
        progressLabel['text']=update_progress()
    except KeyError:
        text.insert(tk.INSERT, "End of series reached.")
    #highlighting tags
    run_highlighting(text)


def run_highlighting(text_object):
    text_object.highlight_pattern('malign', 'red')
    text_object.highlight_pattern('malignant', 'red')
    text_object.highlight_pattern('benign', 'green')
    text_object.highlight_pattern('no evidence of malignan', 'green')
    text_object.highlight_pattern('No malignan', 'green')
    text_object.highlight_pattern('DCIS', 'blue')

progressString = update_progress()

#setting up the window
root = tk.Tk()
root.title("FORM: "+FORM_NAME)
root.geometry('500x500')

#binding keys to function
KEY_BENIGN = 'a'
ID_BENIGN = 1
KEY_MALIGNANT = 's'
ID_MALIGNANT = 2
KEY_UNSURE = 'd'
ID_UNSURE = 3
KEY_DUMP = 'x'
ID_DUMP = 4

root.bind(KEY_BENIGN, lambda x: record_label(ID_BENIGN))
root.bind(KEY_MALIGNANT, lambda x: record_label(ID_MALIGNANT))
root.bind(KEY_UNSURE, lambda x: record_label(ID_UNSURE))
root.bind(KEY_DUMP, lambda x: record_label(ID_DUMP))

topFrame = tk.Frame(root, width=20, height=20, borderwidth=4)
topFrame.grid(row=0, column=0, sticky=tk.N)

titleLabel = tk.Label(topFrame, text=FORM_NAME, wraplengt=300, font="none 12 bold")
titleLabel.grid(row=0, column=0)
progressLabel = tk.Label(topFrame, text=progressString, wraplengt=300, font="none 9")
progressLabel.grid(row=0, column=1)


mainFrame = tk.Frame(root, width=200, height=200, background="white", borderwidth=4)
mainFrame.grid(row=1, column=0)

#label = tk.Label(mainFrame, width=40, height=20, bg="white", wraplengt=300)
#label['text']= reports[0]
#label.grid(row=0, column=0)

text = CustomText(mainFrame, width=50, height=20, bg="white", wrap=tk.WORD)
text.insert(tk.INSERT, reports[ind])
text.tag_configure("red", foreground="#ff0000")
text.tag_configure("green", foreground="#00ff00")
text.tag_configure("blue", foreground="#0000ff")
run_highlighting(text)
text.grid(row=0, column=0)

label = tk.Label(mainFrame, width=40, height=1)
label['text'] = "Current Label: " + str(reportDataFrame['pathDiagnosis'].at[ind])
label.grid(row=2, column=0)

buttonFrame = tk.Frame(root, width=20, height=100, background="yellow", borderwidth=4)
buttonFrame.grid(row=3, column=0)

#List of Buttons to edit
button = tk.Button(buttonFrame, text = '({l}) Benign'.format(l=KEY_BENIGN), 
    bg="green", fg="white", command = lambda: record_label(ID_BENIGN))
button.grid(row=0, column=0,sticky=tk.S)

button = tk.Button(buttonFrame, text = '({l}) Malignant'.format(l=KEY_MALIGNANT), 
    bg="red", fg="white", command = lambda: record_label(ID_MALIGNANT))
button.grid(row=0, column=1,sticky=tk.S)

button = tk.Button(buttonFrame, text = '({l}) Indeterminant'.format(l=KEY_UNSURE), 
    command = lambda: record_label(ID_UNSURE))
button.grid(row=0, column=2,sticky=tk.S)

button = tk.Button(buttonFrame, text = '({l}) Dump'.format(l=KEY_DUMP), 
    command = lambda: record_label(ID_DUMP))
button.grid(row=1, column=1,sticky=tk.S)


root.mainloop()

#save the edited dataframe
reportDataFrame.to_csv(PATH_TO_CSV+FNAME, index=False)