from tkinter import *
from tkinter import filedialog,ttk,PhotoImage
import sv_ttk
import Render
import time

window = Tk()
window.resizable(False, False)
window.configure(bg="#1c0036")    
window.title('Voltz Renderer')
window.geometry("1280x720")

app_icon = PhotoImage(file="icon.png")
window.iconphoto(True, app_icon)

# Set window size
style = ttk.Style(window)
style.theme_use('xpnative')


#Functions
def browseExec():
    global blenderexec
    blenderexec = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Blender", "*.exe*"), ("Blender", "*.exe*")))
    label_file_explorer.configure(text="Blender Executable: "+blenderexec)
def browseFile():
    global blenderfile
    blenderfile = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Blender files", "*.blend*"), ("Blender files", "*.blend*")))
    label_file_explorer.configure(text="File Opened: "+blenderfile)
def outputFolder():
    global outputfile
    outputfile = filedialog.askdirectory(title="Select a Folder", initialdir="/")
    label_file_explorer.configure(text="File Opened: "+outputfile)
def image():
    label_file_explorer.configure(text="RENDERING IMAGE...")
    label_file_explorer.configure(text=Render.renderimage('"'+blenderexec+'"', '"'+blenderfile+'"', text_frames.get("1.0", "end-1c"), '"'+outputfile+'/"'))
def anim():
    label_file_explorer.configure(text="RENDERING ANIMATION...")
    label_file_explorer.configure(text=Render.renderanim('"'+blenderexec+'"', '"'+blenderfile+'"', '"'+outputfile+'/"', "OPTIX"))


#Main Page
label_file_explorer = Label(window, text = "Voltz Renderer v.0.1a", height=4, fg = "#ff006a", bg = "#0b0014", font=("System", 36))
button_blender = ttk.Button(window,text = "Select Blender Executable", width=20, command = browseExec)
button_explore = ttk.Button(window,text = "Select Blender File", width=20, command = browseFile)
button_output = ttk.Button(window,text = "Select Output Folder", width=20, command = outputFolder)
label_frames =  Label(window,text = "Frame:")
text_frames = Text(window, height = 1, width = 25)
text_frames.insert(END, "1")
button_renderImage = ttk.Button(window,text = "Render Image", width=20, command = lambda:image())  
button_renderAnimation = ttk.Button(window,text = "Render Animation", width=20, command = lambda:anim())  
button_exit = ttk.Button(window,text = "Exit",command = exit) 

#Layout
window.grid_columnconfigure(0, weight=1)
label_file_explorer.grid(column = 0, row = 0, sticky="nsew")
button_blender.grid(column = 0, row = 4)
window.grid_rowconfigure(4, minsize=50)
button_explore.grid(column = 0, row = 5)
window.grid_rowconfigure(5, minsize=50)
button_output.grid(column = 0, row = 6)
window.grid_rowconfigure(6, minsize=50)
label_frames.grid(column = 0, row = 7)
text_frames.grid(column = 0, row = 8)
window.grid_rowconfigure(8, minsize=50)
button_renderImage.grid(column = 0, row = 9)
window.grid_rowconfigure(9, minsize=50)
button_renderAnimation.grid(column = 0, row = 10)
window.grid_rowconfigure(10, minsize=50)
button_exit.grid(column = 0, row = 11)
window.grid_rowconfigure(11, minsize=50)
sv_ttk.set_theme("dark")


window.mainloop()