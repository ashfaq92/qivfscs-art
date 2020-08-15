from ctypes import *

print("hi fella")
# filePath = "E:\\testProg.dll"
filePath = "/home/ashfaq/PycharmProjects/ART/programs/roughProgram/testProg.dll"
lib = cdll.LoadLibrary(filePath)
lib.square.argtypes = [c_ulonglong]
print(type(lib))
print(lib.square(657270))

