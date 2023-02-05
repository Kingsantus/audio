import wave  #mode that read wav file
import os   #file system

obj = wave.open("example.wav", "rb")  #open file and read binary

print("Numbers of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("Numbers of frames", obj.getnframes())
print("all parameters", obj.getparams())

""" t_audio = obj.getnframes() / obj.getframerate
print(t_audio) """

frames = obj.readframes(-1)  #defining frame

obj.close() #close this file to ensure smooth flow to the second

obj_new = wave.open("new.wav", "wb")  #creating a dupblicate of write binary

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(44100.0)

obj_new.writeframes(frames)  #the frame defined up there

obj_new.close()  #close again