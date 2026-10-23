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
    global cyclesdevice
    cyclesdevice = config[2]

configuration()

def browseExec():
    blenderexec = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Blender", "*.exe*"), ("Blender", "*.exe*")))
    if blenderexec!="":
        label_file_explorer.configure(text="Blender Executable: "+blenderexec)
        settings.save(blenderexec, outputfile, opt.get())
        configuration()
        update_Labels()

def browseFile():
    global blenderfile 
    blenderfile = filedialog.askopenfilenames(title = "Select a File", filetypes = (("Blender files", "*.blend"), ("Blender files", "*.blend")))
    if blenderfile!="":
        blenderlist = str(blenderfile)
        label_file_explorer.configure(text="File Opened: "+str(blenderlist))
        text_explore.config(state="normal")
        text_explore.delete("1.0", "end-1c")
        text_explore.insert('1.0', blenderlist)
        text_explore.config(state="disabled")

def outputFolder():
    outputfile = filedialog.askdirectory(title="Select a Folder")
    if outputfile!="":
        label_file_explorer.configure(text="File Opened: "+outputfile)
        settings.save(blenderexec, outputfile, opt.get())
        configuration()
        update_Labels()

def cycleDeviceChange(*args):
    cyclesdevice=opt.get()
    settings.save(blenderexec, outputfile, cyclesdevice)

def image():
    for i in range(0, len(blenderfile), 1):
        currentfile = blenderfile[i]
        label_file_explorer.configure(text="Rendering Image...")
        window.update()
        file = os.path.splitext(os.path.basename(currentfile))
        label_file_explorer.configure(text=render.renderimage('"'+blenderexec+'"', '"'+currentfile+'"', text_frames.get("1.0", "end-1c"), '"'+outputfile+f'/{file[0]}"', cyclesdevice))

def anim():
    for i in range(0, len(blenderfile), 1):
        currentfile = blenderfile[i]
        label_file_explorer.configure(text="Rendering Animation...")
        window.update()
        file = os.path.splitext(os.path.basename(currentfile))
        label_file_explorer.configure(text=render.renderanim('"'+blenderexec+'"', '"'+currentfile+'"', '"'+outputfile+f'/{file[0]}"', cyclesdevice))

#GUI
def update_Labels():
    label_blender.configure(text=blenderexec)
    label_output.configure(text=outputfile)


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

buttonwidth = 35
label_file_explorer = Label(window, text = "Voltz Renderer v.beta-1", fg = "#ff006a", bg = "#0b0014", font=("System", 36))

button_blender = ttk.Button(window,text = "Select Blender Executable", width=buttonwidth, command = browseExec)
label_blender =  ttk.Label(window,text = "ERROR")

button_explore = ttk.Button(window,text = "Select Blender File", width=buttonwidth, command = browseFile)
text_explore =  Text(window, font=("System", 12), background="#0b0014", foreground="#E0E0E0", insertbackground="#E0E0E0", selectbackground="#ff006a", selectforeground="#1c0036")
text_explore.insert('1.0', "No Blender File Selected")
text_explore.config(state="disabled")

button_output = ttk.Button(window,text = "Select Output Folder", width=buttonwidth, command = outputFolder)
label_output =  ttk.Label(window,text = "ERROR")

label_cycles =  ttk.Label(window,text = "Render Device:")
CYCLES = ["CPU", "CUDA", "OPTIX", "HIP", "ONEAPI", "METAL"]   
opt = StringVar(value=cyclesdevice)
opt.trace_add("write", cycleDeviceChange)
cycles_dropdown = OptionMenu(window, opt, *CYCLES, command=cycleDeviceChange)
cycles_dropdown.config(bg="#0b0014", fg="#E0E0E0", font=("System"), activeforeground="#1c0036", activebackground="#ff006a") 
cycles_dropdown["menu"].config(bg="#0b0014", fg="#E0E0E0", font=("System"), activeforeground="#1c0036", activebackground="#ff006a")


label_frames =  ttk.Label(window,text = "Frame:")
text_frames = Text(window, height = 1, width = 25, font=("System", 17), background="#0b0014", foreground="#E0E0E0", insertbackground="#E0E0E0", selectbackground="#ff006a", selectforeground="#1c0036")
text_frames.insert(END, "0001")

button_renderImage = ttk.Button(window,text = "Render Image", width=buttonwidth, command = lambda:image())  
button_renderAnimation = ttk.Button(window,text = "Render Animation", width=buttonwidth, command = lambda:anim())  
button_exit = ttk.Button(window,text = "Exit", command = exit) 

#Layout
label_file_explorer.place(relx=0.5, y=72, width=1280, height=36*4, anchor='center')

button_blender.place(relx=0.25, y=200, anchor='center')
label_blender.place(relx=0.5, y=182.5, width=545)
label_output.place(relx=0.5, y=233, width=545)
button_output.place(relx=0.25, y=250, anchor='center')
button_explore.place(relx=0.25, y=300, anchor='center')
text_explore.place(relx=0.506, y=285, height=180, width=525)


label_cycles.place(relx=0.15, y=350, anchor='center')
cycles_dropdown.place(relx=0.22, y=335, width=250)
label_frames.place(relx=0.1125, y=350+50, anchor='center')
text_frames.place(relx=0.145, y=388, width=345)
button_renderImage.place(relx=0.5, y=500, anchor='center')
button_renderAnimation.place(relx=0.5, y=550, anchor='center')
button_exit.place(relx=0.5, y=600, anchor='center')

update_Labels()

style = ttk.Style(window)
style.theme_use('clam')
style.configure("TButton", font=("Terminal", 12), padding=6)
style.configure("TLabel", font=("Terminal", 12), padding=6, background = "#1c0036", foreground="#E0E0E0")

style.map(
    "TButton",
    background=[("active", "#ff006a"), ("!active", "#0b0014")],
    foreground=[("active", "#1c0036"), ("!active", "#E0E0E0")],
)
center_window(window)

window.mainloop()