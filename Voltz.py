from tkinter import *
from tkinter import filedialog,ttk
import os
import settings
import render

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

window = Tk()
window.resizable(False, False)
window.configure(bg="#1c0036")    
window.title('Voltz Renderer')
window.geometry("1280x720")

ICON_PATH = os.path.join(SCRIPT_DIR, "icon.png")
app_icon = PhotoImage(file=ICON_PATH)
window.iconphoto(True, app_icon)

#Functions
def configuration():
    config = settings.load()
    global blenderexec
    blenderexec = config[0]
    global outputfile
    outputfile = config[1]

configuration()

def browseExec():
    blenderexec = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Blender", "*.exe*"), ("Blender", "*.exe*")))
    if blenderexec!="":
        label_file_explorer.configure(text="Blender Executable: "+blenderexec)
        settings.save(blenderexec, outputfile)
        configuration()
def browseFile():
    global blenderfile 
    blenderfile = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Blender files", "*.blend*"), ("Blender files", "*.blend*")))
    if blenderfile!="":
        label_file_explorer.configure(text="File Opened: "+blenderfile)
def outputFolder():
    outputfile = filedialog.askdirectory(title="Select a Folder", initialdir="/")
    if outputfile!="":
        label_file_explorer.configure(text="File Opened: "+outputfile)
        settings.save(blenderexec, outputfile)
        configuration()
def image():
    label_file_explorer.configure(text="Rendering Image...")
    window.update()
    file = os.path.splitext(os.path.basename(blenderfile))
    label_file_explorer.configure(text=render.renderimage('"'+blenderexec+'"', '"'+blenderfile+'"', text_frames.get("1.0", "end-1c"), '"'+outputfile+f'/{file[0]}"'))
def anim():
    label_file_explorer.configure(text="Rendering Animation...")
    window.update()
    file = os.path.splitext(os.path.basename(blenderfile))
    label_file_explorer.configure(text=render.renderanim('"'+blenderexec+'"', '"'+blenderfile+'"', '"'+outputfile+f'/{file[0]}"', "OPTIX"))
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


#Main Page
buttonwidth = 35
label_file_explorer = Label(window, text = "Voltz Renderer v.0.21a", height=4, fg = "#ff006a", bg = "#0b0014", font=("System", 36))
button_blender = ttk.Button(window,text = "Select Blender Executable", width=buttonwidth, command = browseExec)
button_explore = ttk.Button(window,text = "Select Blender File", width=buttonwidth, command = browseFile)
button_output = ttk.Button(window,text = "Select Output Folder", width=buttonwidth, command = outputFolder)
label_frames =  ttk.Label(window,text = "Frame:")
text_frames = Text(window, height = 1, width = 25, font=("System", 24), background="#1c0036", foreground="#E0E0E0")
text_frames.insert(END, "1")
button_renderImage = ttk.Button(window,text = "Render Image", width=buttonwidth, command = lambda:image())  
button_renderAnimation = ttk.Button(window,text = "Render Animation", width=buttonwidth, command = lambda:anim())  
button_exit = ttk.Button(window,text = "Exit", command = exit) 

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

style = ttk.Style(window)
style.theme_use('clam')
style.configure("TButton", font=("Terminal", 12), padding=6)
style.configure("TLabel", font=("Terminal", 12), padding=6, background = "#1c0036", foreground="white")
style.map(
    "TButton",
    background=[("active", "#1c0036"), ("!active", "#0b0014")],
    foreground=[("active", "#FFFFA0"), ("!active", "#E0E0E0")],
)

center_window(window)

window.mainloop()