import os
dir = 'C:\Amanda\Dois'
for f in os.listdir(dir):
    os.remove(os.path.join (dir, f));
