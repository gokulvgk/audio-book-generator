import mymodule

mymodule.root.title("Text-to-speech conversion with translation")
# Get the screen width and height
screen_width = mymodule.root.winfo_screenwidth()
screen_height = mymodule.root.winfo_screenheight()

# Set the window size to cover the entire screen
mymodule.root.geometry(f"{screen_width}x{screen_height}+0+0")

mymodule.root.iconbitmap("speaker-image.ico")     
prompt_label = mymodule.Label(mymodule.root, text="Convert any text file into an audio file").pack()
browsebutton = mymodule.Button(mymodule.root, text="browse files", command=mymodule.open_dialog, fg="blue", bg="silver").pack(padx=20, pady=20)
checkbox1=mymodule.Checkbutton(mymodule.root, text="English", variable=mymodule.en_var, command=lambda: mymodule.check(mymodule.languages)).pack(padx=20, pady=20) # lambda: is used only for parameterized functions
checkbox2=mymodule.Checkbutton(mymodule.root, text="French", variable=mymodule.fr_var, command=lambda: mymodule.check(mymodule.languages)).pack(padx=20, pady=20)
checkbox3=mymodule.Checkbutton(mymodule.root, text="Dutch", variable=mymodule.nl_var, command=lambda: mymodule.check(mymodule.languages)).pack(padx=20, pady=20)
checkbox4=mymodule.Checkbutton(mymodule.root, text="Spanish", variable=mymodule.es_var, command=lambda: mymodule.check(mymodule.languages)).pack(padx=20, pady=20)
checkbox5=mymodule.Checkbutton(mymodule.root, text="German", variable=mymodule.de_var, command=lambda: mymodule.check(mymodule.languages)).pack(padx=20, pady=20)
checkbox6=mymodule.Checkbutton(mymodule.root, text="Tamil", variable=mymodule.ta_var, command=lambda: mymodule.check(mymodule.languages)).pack(padx=20, pady=20)
convertbutton= mymodule.Button(mymodule.root, text="convert",command=lambda: mymodule.convert(mymodule.languages)).pack(padx=20)
takes_time = mymodule.Label(mymodule.root, text="converting may take some time").pack(padx=20)
view_audio_button = mymodule.Button(mymodule.root, text="View your Audio files", command=mymodule.open_audio_files).pack(padx=20, pady=20)
mymodule.root.mainloop()