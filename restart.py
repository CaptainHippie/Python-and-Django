import os

restart = input("restart?(yes/no): ")
if restart == 'yes':
    os.system("shutdown /r /t 1")
else:
    exit()