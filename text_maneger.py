import sys 
import os 
import json 


def json_encoder(file_dest, obj):
    """writes a 'object' to a json formated file"""
    try:
        #in case the file doesnt exists it will write a new one
        # in case it does it will format and rewrite  
        with open(file_dest, 'w') as file:
            token = json.dumps(obj, sort_keys=True, indent=4)
            file.write(token) #writes to a file 
    except Exception: #cahnge this latter 
        pass

def json_decoder(file_origen):
    """takes a file dest (str) and returns a python object
        in case of file not found return 0
        in case of file not permited returns -1
    """
    try:
        with open(file_origen, 'r') as file: #opens the file as 'read'
            token = file.read() #reads all the file :file -> str
            obj = json.loads(token)
            return obj

    except FileNotFoundError:
        print(f"[!] file { file_origen } not found")
        return 0
    
    except PermissionError:
        print(f"[!] file { file_origen } access not permited")
        return -1 

