import os
import shutil
path = r'C:\Users\windows\Documents\de3'
num = os.listdir(path)
d = num[len(num)-1]
sour= r'C:\Users\windows\Videos'+'\\'+ str(d)
des = r"G:\Meine Ablage\"+'\\'+ str(d)
shutil.move(sour,des)
