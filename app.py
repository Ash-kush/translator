from tkinter import*
from translate import Translator

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(Input.get())
    Output.set(Translation)

root = Tk()
root.title("Translator")
canvas = Canvas(root, width=600, height=400, bg='lightblue')
canvas.pack()
canvas.grid(columnspan=3, rowspan=3)
label = Label(root, text="Language Translator", fg="green", font=("Ink Free", 25), bg="lightblue")
label.place(x=150,y=30)
InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Hindi')
LanguageChoices = {'Hindi','English','French','German','Spanish'}

InputLanguageChoiceMenu = OptionMenu(root,InputLanguageChoice,*LanguageChoices)
InputLanguageChoiceMenu.place(x=200,y=100)
label1 = Label(root, text="to", fg="blue", font=("Times New Roman", 15), bg="lightblue")
label1.place(x=300,y=100)
LanguageChoices = {'Hindi','English','French','German','Spanish'}
InputLanguageChoiceMenu = OptionMenu(root,TranslateLanguageChoice,*LanguageChoices)
InputLanguageChoiceMenu.place(x=338,y=100)

label2 = Label(root, text="Enter Text", fg="blue", font=("Times New Roman", 16), bg="lightblue")
label2.place(x=100,y=180)
Input = StringVar()
TextBox = Entry(root,textvariable=Input).place(x=250,y=183)
label3 = Label(root, text="Your Translated Text", fg="blue", font=("Times New Roman", 16), bg="lightblue")
label3.place(x=60,y=250)
Output = StringVar()
TextBox = Entry(root,textvariable=Output).place(x=250,y=253)

imagebutton = Button(root, command=Translate, text='Translate',width=8,fg='white',activebackground='blue',bg='red',font=(6),  relief = GROOVE).place(x=250,y=320)

root.resizable(0,0)
root.mainloop()