import shark

doc = shark.Dpy("Channel")

for f in doc.find_all:
    print(f)