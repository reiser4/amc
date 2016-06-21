
import os
pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

cmdlines = list()

for pid in pids:
    try:
        cmdline = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
        #print cmdline
        cmdlines.append(cmdline.replace("\x00"," ").strip())
    except IOError: # proc has already terminated
        continue

#print cmdlines

components = list(["display", "ioloop", "keyboard", "main", "relay", "sercom", "leds", "band"])

for c in components:
    print "Componente", c,"...",
    running = False
    for cl in cmdlines:
        if cl == "python " + c + ".py":
            running = True
    if running:
        print "Trovato."
    else:
        print "Non trovato: eseguo",
        cmdline = "cd " + c + " && python " + c + ".py > out.log 2> err.log &"
        print "[",cmdline,"]"
        os.system(cmdline)

