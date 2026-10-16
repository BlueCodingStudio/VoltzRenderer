import subprocess

def renderimage(blender, filename, frame, output):
    cmd = [blender, ' -b ', filename, '-F PNG -o ', output, ' -f ', frame]
    res = ' '.join(cmd)
    print(res)
    subprocess.run(res)
    return("DONE")

def renderanim(blender, filename, output, renderdevice):
    cmd = [blender, ' -b ', filename, ' -o ', output, '  -a --  --cycles-device ', renderdevice]
    print(cmd)
    res = ' '.join(cmd)
    subprocess.run(res)
    return("DONE")