import subprocess

def renderimage(blender, filename, frame, output):
    cmd = [blender, ' -b ', filename, '-F PNG -o ', output, ' -f ', frame]
    res = ' '.join(cmd)
    subprocess.run(res)
    return("DONE")

def renderanim(blender, filename, output, renderdevice):
    cmd = [blender, ' -b ', filename, ' -o ', output, '  -a --  --cycles-device ', renderdevice]
    res = ' '.join(cmd)
    subprocess.run(res)
    return("DONE")

#renderimage(r'"D:/Blender/Blender 5.2/blender.exe"', r'"D:/Blender/Model Files/teapotblend5.blend"', "1", r'"D:\Projects\VoltzRenderer\output\frame"')
#renderanim(r'"D:/Blender/Blender 5.2/blender.exe"', r'"D:/Blender/Model Files/teapotblend5.blend"', r'"D:/Projects/VoltzRenderer/output/frame"', "OPTIX")