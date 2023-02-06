from pydub import AudioSegment

audio = AudioSegment.from_wav("output.wav")

#increase the volume by 6db
audio = audio + 6

audio = audio * 2

#fade in 2 sec
audio = audio.fade_in(2000)

#exporting to the correct file
audio.export("welcome.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("welcome.mp3")

print("done")