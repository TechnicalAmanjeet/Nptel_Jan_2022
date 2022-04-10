# speech recognition by using google speech api
import speech_recognition as sr
# import pyaudio

# to get how many microphones are there in your pc.
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print(index, " ", name)

# print mike name which is present in my device.
mike_names = sr.Microphone.list_microphone_names();
print(mike_names)

# speech recogniser object
r = sr.Recognizer()

# can record from microphone and convert it into text.
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something..")

    # start listening the song.
    audio = r.listen(source)

    # by using below file handling method we can only write or read string in file not audio or video.
    # with open("file.wav", "w") as file:
    #     file.write(audio)

    # convert audio file into text
    try:
        text = r.recognize_google(audio)

        # saving text file.
        with open("mySpeech.txt", "w") as file:
            file.write(text)


        print("You said : " + text )
    # try catching the error.
    except sr.UnknownValueError:
        print("Google speech recognition does not understand the audio.")
    except sr.RequestError as e:
        print("This error has occurred : " + e)

# if we have audio file with us then we can read that audio file as well.
# with sr.AudioFile("audio.wav") as source: # the extension of audio file must be .wav.
#     # because google speech recogniser only work on .wav audio file.
#
#     audio2 = r.record(source)  # will get the data of audio file.
#
#     # now we will convert it into text with exception handling.
#     try:
#         text2 = r.recognize_google(audio2)
#
#         print("Your audio file contains : " + text2)
#
#     except sr.UnknownValueError:
#         print("Google speech recogniser does not understand your audio.")
#
#     except sr.RequestError as e:
#         print("These are the error : " + e)




