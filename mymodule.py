import os
from gtts import gTTS
from translate import Translator
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
import subprocess
import time

# creating a new tkinter window named root
root =Tk()
# initializing tkinter variables to keep track of which checkbox is selected
en_var= IntVar() 
fr_var= IntVar()
nl_var= IntVar()
es_var= IntVar()
de_var= IntVar()
ta_var= IntVar() 

# creating a list to store languages
languages=['']*6 

def open_dialog():
    root.inputfilename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    file_path_label = Label(root, text=root.inputfilename).pack()

# To check if open_dialog() has been called 
root.inputfilename = None

def open_audio_files():
    root.outputfilename =  filedialog.askopenfilename(initialdir="audio_files", title="audio files for your text", filetypes=(("mp3 files", "*.mp3"),))
    subprocess.Popen(["start", " ", root.outputfilename], shell=True)
# Function to translate text to a target language
def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation
def text_to_speech(text, language, output_file):
    if language == 'auto':
        # Automatically detect the language
        tts = gTTS(text, lang='auto')
    else:
        tts = gTTS(text, lang=language)

    tts.save(output_file)

# Function to check which checkbox is selected
def check(languages):
    global checkflag
    checkflag = True
    if en_var.get():
        languages[0]='en'
    if fr_var.get():
        languages[1]='fr'
    if nl_var.get():
        languages[2]='nl'
    if es_var.get():
        languages[3]='es'
    if de_var.get():
        languages[4]='de'
    if ta_var.get():
        languages[5]='ta'

#flag variable for check() 
checkflag = False

def convert(languages):
    if root.inputfilename == None:
        messagebox.showwarning("Warning", "Please select a file")
        return
    elif checkflag == False:
        messagebox.showwarning("Warning", "Please select at least one language")
        return
# Input file containing the text you want to convert to speech
    input_file = root.inputfilename
# Output directory for audio files
    output_directory = 'audio_files'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    # exception handling if no input files is selected from the dialog box
    try:
        with open(input_file, 'r') as file:
            text = file.read()
    except:
        messagebox.showwarning("Warning", "Please select a file")
        return
# To show the cursor as a watch
    root.configure(cursor="watch")
# to give some time for tkinter to update the mainloop 
    time.sleep(0.1)
# This line updates the Tkinter main loop, which allows the GUI to respond to changes. It's used here to ensure that the cursor change is immediately visible.
    root.update()
# Loop through each language and convert the text to speech
    for lang in languages:
        # exception handling for non-selected languages
        try:
            translated_text = translate_text(text, lang)
            output_file = os.path.join(output_directory, f'output_{lang}.mp3')
            text_to_speech(translated_text, lang, output_file)    
        except:
            pass                            
    infolabel = Label(root, text="your audio files are ready").pack(padx=20, pady=20)
    root.configure(cursor="arrow")