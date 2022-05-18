# https://stackoverflow.com/questions/24348452/read-a-file-from-a-position-in-robot-framework

class readmore(object):
     ROBOT_LIBRARY_SCOPE = "TEST SUITE"

     def __init__(self):
          self.fp = {}

     def read_more(self, path):
          # if we don't already know about this file, 
          # set the file pointer to zero
          if path not in self.fp:
               self.fp[path] = 0

          # open the file, move the pointer to the stored
          # position, read the file, and reset the pointer
          with open(path) as f:
               f.seek(self.fp[path])
               data = f.read()
               self.fp[path] = f.tell()

               return data
				  
