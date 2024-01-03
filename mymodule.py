import os
from gtts import gTTS
from translate import Translator
from tkinter import * 
from tkinter import filedialog
import subprocess
# creating a new tkinter window named root
root =Tk()
# initializing tkinter variables to keep track of which checkbox is selected
en_var= IntVar() 
fr_var= IntVar()
nl_var= IntVar()
es_var= IntVar()
de_var= IntVar()
ta_var= IntVar() 

# creating a list of languages
languages=['']*6 

def open_dialog():
    root.inputfilename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    file_path_label = Label(root, text=root.inputfilename).pack()
def open_audio_files():
    root.outputfilename =  filedialog.askopenfilename(initialdir="audio_files", title="audio files for your text", filetypes=(("mp3 files", "*.mp3"),))
    file_path_label = Label(root, text=root.outputfilename).pack()
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
def convert():
    infolabel = Label(root, text="your audio files are ready")
    infolabel.pack()
 # Input file containing the text you want to convert to speech
    input_file = root.inputfilename
# Output directory for audio files
    output_directory = 'audio_files'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
# Loop through each language and convert the text to speech
    with open(input_file, 'r') as file:
        text = file.read()
        for lang in languages:
            translated_text = translate_text(text, lang)
            output_file = os.path.join(output_directory, f'output_{lang}.mp3')
            text_to_speech(translated_text, lang, output_file)
            # text_to_speech_pyttsx3(translated_text, lang)
               
# Function to check which checkbox is selected
def check():
    if en_var.get():
        enselected = Label(root, text="English selected")
        languages[0]='en'
    if fr_var.get():
        frselected = Label(root, text="French selected")
        languages[1]='fr'
    if nl_var.get():
        nlselected = Label(root, text="Dutch selected")
        languages[2]='nl'
    if es_var.get():
        esselected = Label(root, text="Spanish selected")
        languages[3]='es'
    if de_var.get():
        deselected = Label(root, text="German selected")
        languages[4]='de'
    if ta_var.get():
        taselected = Label(root, text="Tamil selected")
        languages[5]='ta'
prompt_label = Label(root, text="Convert any text file into an audio file")
prompt_label.pack()
browsebutton = Button(root, text="browse files", command=open_dialog, fg="blue", bg="silver")
browsebutton.pack(padx=20, pady=20)
takes_time = Label(root, text="converting may take some time")
takes_time.pack(padx=20, pady=20)