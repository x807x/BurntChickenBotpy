import os
while True:
    command=input("please input {key_name},{key_value}\n")
    if(command=="exit" or command=="exit()"): break
    key=command.split(",")
    os.environ[key[0]]=key[1]