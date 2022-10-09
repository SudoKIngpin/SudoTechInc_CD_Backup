import os
import time 
with open('requirements.txt') as p:
    a=p.read()
os.system(f'pip install {a}')
print("Installation successful  !")
time.sleep(2)
input("Hit Enter to exit !")
