import subprocess
bat = open('C:\\Amanda\COPY.bat')
processo = bat.read("COPY").strip("COPY")
subprocess.Popen(processo);
