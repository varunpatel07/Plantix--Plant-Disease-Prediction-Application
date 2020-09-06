import mydatabase as db
import tensorflow
import tkinter
import pickle
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image

window=tkinter.Tk()
window.iconphoto(False, tkinter.PhotoImage(file='C:/Users/lenovo/Desktop/project/logo2.png'))
window.title("Plantix")
window.geometry("400x350")
window.resizable(0,0)
def details(items):
    plant_var=items[0][2]
    disease_var=items[0][3]
    cure=items[0][4]
    plant_name.configure(text=plant_var)
    disease_name.configure(text=disease_var)
    cure_details.configure(text=cure)

def clicked():
    filename =askopenfilename(title="Select Image file",filetypes=(("JPG File","*.jpg"),))
    txt.delete(0,"end")
    txt.insert(0,filename)
    img=Image.open(filename)
    img.thumbnail((70,70))
    img=ImageTk.PhotoImage(img)
    images.configure(image=img)
    images.image=img

def exit_app():
    window.destroy()
    
def clear_text():
    plant_name.configure(text="")
    disease_name.configure(text="")
    cure_details.configure(text="")
    images.configure(image="")
    txt.delete(0,"end")

def search():
    global label
    global details
    instance=pickle.load(open(r"C:/Users/lenovo/Desktop/project/final_project/Label_Instance.pkl","rb"))
    mod=load_model(r"C:/Users/lenovo/Desktop/project/final_project/model.h5")
    img = cv2.imread(txt.get())
    img = cv2.resize(img,(256,256))
    img = np.reshape(img,[1,256,256,3])
    img=img/255.0
    max_val=np.argmax(mod.predict(img))
    label=instance.classes_[max_val]
    details(db.find_details(label))
    
    
    
# frames    
top=tkinter.Frame(window,height=70,bg="black")
top.pack(fill="x")

middle=tkinter.Frame(window,height=50)
middle.pack(fill="x")

mid_lower=tkinter.Frame(window,height=80)
mid_lower.pack(fill="x")

lower=tkinter.Frame(window)
lower.pack(expand=True,fill="both")

#buttons and label
l1= tkinter.Label(middle,text="FILE:",font="times 15")
l1.pack(side="left")

txt= tkinter.Entry(middle,width=40)
txt.pack(side="left",ipady="5",padx="5",pady="5")

bt1=tkinter.Button(middle,text="open",command=clicked)
bt1.pack(side="left",ipadx="10",padx="10",ipady="5")

search=tkinter.Button(mid_lower,text="search",command=search)
search.pack(side="left",ipadx="20",padx="25",pady="7")

clear=tkinter.Button(mid_lower,text="clear",command=clear_text)
clear.pack(side="left",ipadx="15",padx="25",pady="7")

exit_app=tkinter.Button(mid_lower,text="exit",command=exit_app)
exit_app.pack(side="left",ipadx="15",padx="25",pady="7")

head=tkinter.Label(top,text="PLANTIX",font="Britannic 20",fg="red",bg="black")
head.pack()

#status frame

plant_name_lbl=tkinter.Label(lower,text="NAME :",font="ariel 10",anchor="w")
plant_name_lbl.grid(row=0,column=0,padx=5,ipadx=5,pady=5,sticky="w")

plant_name=tkinter.Label(lower,font="ariel 7",anchor="w")
plant_name.grid(row=0,column=1,padx=5,ipadx=5,pady=5,sticky="w")




disease_name_lbl=tkinter.Label(lower,text="DISEASE :",font="ariel 10",anchor="w")
disease_name_lbl.grid(row=1,column=0,padx=5,ipadx=5,pady=5,sticky="w")

disease_name=tkinter.Label(lower,font="ariel 7",anchor="w")
disease_name.grid(row=1,column=1,padx=5,ipadx=5,pady=5,sticky="w")



cure_lbl=tkinter.Label(lower,text="TREATMENT :",font="ariel 10",anchor="w")
cure_lbl.grid(row=2,column=0,padx=5,ipadx=5,pady=5,sticky="w")

cure_details=tkinter.Label(lower,font="ariel 7",anchor="w",wraplength=275,justify="left")
cure_details.grid(row=2,column=1,padx=5,ipadx=5,pady=5,sticky="w")



images_label=tkinter.Label(lower,text="IMAGE:",font="ariel 10",anchor="w")
images_label.grid(row=3,column=0,padx=5,ipadx=5,pady=5,sticky="w")

images=tkinter.Label(lower,anchor="w")
images.grid(row=3,column=1,padx=5,ipadx=5,pady=5,sticky="w")


window.mainloop()





