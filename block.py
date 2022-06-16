
from ipaddress import ip_address
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("Website Blocker")
frame = Frame(root)
Label(root, text="Website Blocker", font=("Helvetica", 20)).pack()
Label(root, text="Block any unwanted website for free", font =("Verdana",15)).pack(side=BOTTOM)

host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = ''

Label(root, text ='Enter Website URL:' , font ='arial 13 bold').place(x=10 ,y=80)
Websites = Text(root,font = 'arial 10',height='2', width = '40', wrap = WORD, padx=10, pady=10)
Websites.place(x= 180,y = 60)

def Block():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)

def Unblock():
    website_lists = website_lists.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
     file_content = host_file.readlines()
    for web in Website:
      if web in website_lists:
       with open (host_path , 'r+') as f:
        for line in file_content:
         if line.strip(',') != website_lists:
           f.write(line)
           Label(root, text = "UnBlocked", font = 'arial').place(x=350,y =200)
           pass
         else:
           Label=Label(root, text = 'Already UnBlocked' , font = 'arial')
           Label.place(x=350,y=200)

block = Button(root, text = 'Block',font = 'arial 12 bold',pady = 5,command = Block ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')
unblock = Button(root, text = 'UnBlock',font = 'arial 12 bold',pady = 5,command = Unblock ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')
block.place(x = 230, y = 150)
unblock.place(x =230, y = 200)
root.mainloop()