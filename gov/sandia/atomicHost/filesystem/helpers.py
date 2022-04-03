import os

class Touch:
    
    def __init__(self,path):
        with open(path, 'a'):
            os.utime(path, None)