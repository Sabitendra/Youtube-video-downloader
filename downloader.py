import pyttsx3
from pytube import YouTube

engine = pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("please  Enter youtube link")
link =input(" please enter youtube link :  ")
yt =YouTube(link)
speak("link is taken")
videos = yt.streams.all()

i=1
for stream in videos:
    print(str(i) + " "+str(stream) )
    i +=1
speak("sellect the strem number")
stream_no =int(input("enter strem no : "))
speak(f"you entered: {stream_no}\n")
video=videos[stream_no-1]
speak("please enter destination ")
destination=str(input("Enter your destination : "))
video.download(destination)

speak("video downloaded")
print("downloaded ")