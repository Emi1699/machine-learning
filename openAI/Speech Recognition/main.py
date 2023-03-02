
import config
import whisper
from pytube import YouTube

model = whisper.load_model('base')

output = model.transcribe("fed_meeting.mp4")


f = open("output.txt", 'w')
f.write(output['text'])
f.close()

f = open('output.txt', 'r')
print(f.read())

