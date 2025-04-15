# Load libraries
import cv2
import face_recognition
from datetime import datetime
#pronounce
import  googletrans
import speech_recognition as sr
import gtts
from playsound import playsound
recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'fr-FR'
output_lang = 'en'
output_lang2 = 'ar'
arabic_name = ['fatine', 'falima','mouad']

# #compute encoding of images
def findEncoding(myImgs): # myImgs is the list of images (matrix of pixels)
    encodeList = []
    for myimg in myImgs:
        img = cv2.cvtColor(myimg, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return  encodeList
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        # Retrieve existing name from the file
        myDataList = f.readlines()#steve, 12:00:35
        nameList = []
        for line in myDataList:
            entry = line.split(',') # entry [0]='Steve1',entry[1]= 12:00:35
            nameList.append(entry[0])
            # print(entry[0])
            # print(nameList)
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H: ,%M: %S')
            f.writelines(f'{name},{dtString}\n')
            print(f'{name}  added successfully identified!')
            text =  f'added successfully identified!'
            text_en = f'{name} successfully identified!'
            new_name = name.lower()
            if new_name in arabic_name:
                converted_name = gtts.gTTS(new_name, lang=output_lang2)
                converted_name.save(f'{name}.mp3')
                converted_audio = gtts.gTTS(text, lang=output_lang)
                converted_audio.save(f'confirm{name}.mp3')
                playsound(f'{name}.mp3')
                playsound(f'confirm{name}.mp3')
            else:
                pass




        else:
            pass