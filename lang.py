from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from textblob import TextBlob

root=Tk()
root.geometry("600x500")
root.title("Translator")
root.resizable(True,True)
root.configure(bg="pink")

lang_dict={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
           'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
           'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw',
           'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
           'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy',
           'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
           'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu',
           'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
           'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku',
           'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb',
           'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi',
           'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or',
           'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro',
           'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn',
           'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es',
           'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th',
           'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi',
           'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
############## Functions of button ##############
def click(event=None):
    try:
         wrd3= TextBlob(varname.get())
         ln=wrd3.detect_language()
         lang_todict = languages.get()
         ln_to=lang_dict[lang_todict]

         wrd3=wrd3.translate(from_lang=ln,to=ln_to)
         label3.configure(text=wrd3)
         varname1.set(wrd3)
         sp=wrd3.split()
    except:
        varname1.set("try another keyword")
def exit():
     rr= messagebox.askyesno("Notification",'Are you sure want to exit',parent=root)
     if rr== True:
         root.destroy()
############### Binding function ######################
def on_enterentry1(e):
    entry1['bg']= 'red'
def on_leaveentry1(e):
    entry1['bg'] = 'white'

def on_enterentry2(e):
    entry2['bg'] = 'springgreen'

def on_leaveentry2(e):
    entry2['bg'] = 'white'

def on_enterbtn(e):
    btn['bg'] = 'purple'

def on_leavebtn(e):
    btn['bg'] = 'orange'

def on_enterbtn1(e):
    btn1['bg'] = 'blue'

def on_leavebtn1(e):
    btn1['bg'] = 'springgreen'

##################### Combo Box######################################
languages=StringVar()

font_box=ttk.Combobox(root,width=30,textvariable=languages,state='writeRead')
font_box['values']=[e for e in lang_dict.keys()]
font_box.current(37)
font_box.place(x=300,y=0)
################### Entry box####################################
varname=StringVar()
varname1=StringVar()

entry1=Entry(root,width=25,textvariable=varname,font=("Italic",18,'bold'),relief='ridge')
entry1.place(x=180,y=50)
entry2=Entry(root,width=25,textvariable=varname1,font=("Italic",18,'bold'),relief='ridge')
entry2.place(x=180,y=150)

################ Labels Name######################

label1= Label(root,text="Enter words : ",font=("Italic",18,'bold'),bg="green")
label1.place(x=1,y=50)

label2= Label(root,text="Translated ",font=("Italic",18,'bold'),bg="Powder blue")
label2.place(x=0.5,y=150)

label3= Label(root,text=" ",font=("Italic",18,'bold'),bg="red")
label3.place(x=10,y=350)

############### Button #################################################
btn=Button(root,text="Click ",bd=10,width=10,font=("Italic",18,'bold'),bg="Powder blue",command=click)
btn.place(x=70,y=230)

btn1=Button(root,text="Exit ",bd=10,width=10,font=("Italic",18,'bold'),bg="Powder blue",command=exit)
btn1.place(x=295,y=230)
root.bind('<Return>',click)
############### Binding  ###############################

entry1.bind('<Enter>',on_enterentry1)
entry1.bind('<Leave>',on_leaveentry1)

entry2.bind('<Enter>',on_enterentry2)
entry2.bind('<Leave>',on_leaveentry2)

btn.bind('<Enter>',on_enterbtn)
btn.bind('<Leave>',on_leavebtn)

btn1.bind('<Enter>',on_enterbtn1)
btn1.bind('<Leave>',on_leavebtn1)

root.mainloop()