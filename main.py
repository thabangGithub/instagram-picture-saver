from tkinter import *
import  instaloader
from tkinter import massagebox

insta=instaloader.Instaloader()


def download():
    username=entryfield.get()
    insta.download_profice(username,profile_pic_only=True)
    massagebox.showinfo('Success','Profile Image is Succefully downloaded')


root=Tk()
root.title('Instagram Profile Pic Downloader')

 logoImage=PhotoImage(file='instagram.png')

LogoLabel=Label(root,Images=logoImage)
LogoLabel.grid(pady=10)

titleLabel=Label(root,text='Instagram profile Image Downloader',font=('Times New Roman',20,'bold'))
titleLabel.grid(row=1,column=8,pady=10,pack=30)


enterLabel=Label(root,text='Enter Username:',font=('arial', 20 ,'bold'))
enterLabel.grid(row=2,column=0,pady=10)
entryfield=Entry(root,width=40,font=('areal',15,'bold'),bd=5)
entryfield.grid(row=3,column=0,paydy=10)

downloadButton=Button(root,text='DOWNLOAD',font=('arial',15,'bold'),command=download)
downloadButton.grid(row=4,colom=0,pady=10)
root.mainloop()