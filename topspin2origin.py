import numpy as np
geometry = open("yac54-03_ACN_finale.txt", "r")
toto= "yac54-03_ACN_finale.txt"
output = toto.split('.')
fileout = str(output[0])+'.dat'
print(fileout)
ppmwindows = geometry.readlines()[3]
geometry.close
geometry = open("yac54-03_ACN_finale.txt", "r")
stepligne = geometry.readlines()[5]
geometry.close
res = ppmwindows.split()
#print(res)
beginspec = float(res[3])
endspec = float(res[7])
res = stepligne.split()
step = int(res[3]) 
#print(beginspec)
#print(endspec)
#print(step)
allppm = endspec-beginspec
ppmstep= allppm/step
print(ppmstep)

geometry = open("yac54-03_ACN_finale.txt", "r")
lignes = geometry.readlines()[10:]
geometry.close
tab=[]
yppm=[]
for chn in lignes:
    tab.append(chn.split())
    for lst in tab:
        lst[0] = float(lst[0])
        if lst == tab[-1]:
            yppm.append(lst[0])
#print(yppm)
xppm=[None]*step

for i in range(step):
    if i < 1:
        xppm[i] = beginspec
    else:
       xppm[i] = xppm[i-1] + ppmstep
    if yppm[i] < 0:
        yppm[i] = 0.
fichier =open("tmp.dat", "w")
for i in range(step):
    x = xppm[i]
    y = yppm[i]
    fichier.write(f"{x:5.6f}   {y:5.6f}\n")
fichier.close()



