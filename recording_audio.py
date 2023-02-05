import pyaudio   #install with "python -m pip install pyaudio" for windows
import wave   #wave to write the out put

FRAMES_PER_BUFFER = 3200  #it chan be changed
FORMAT = pyaudio.paInt16  #defining the binary format
CHANNELS = 1  #channels to use
RATE = 44100 #freq

p = pyaudio.PyAudio()  #calling pyaudio

#combinning the variable to show what is the record to expect
stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = FRAMES_PER_BUFFER
)

print("start recording") #showing when the code begin

seconds = 30  #time of record you want
frames = []   #frames undefined
#allowing the record for time set for all time you want the record
for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

#closing of the record part
stream.stop_stream()
stream.close()
p.terminate()

#writing the input to wav out put
obj = wave.open("output.wav", 'wb')
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close
