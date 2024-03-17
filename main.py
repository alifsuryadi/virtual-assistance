import speech_recognition as srec
import pyttsx3 as pyt # text to sound
import pywhatkit  # buka youtube dari python
import wikipedia


engine = pyt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def perintah():
    mendengar = srec.Recognizer()  # untuk mengambil attribute dari object srec
    with srec.Microphone() as source: # untuk memasukkan suara sebagai perintah
        
        pyt.speak("hi I am, habibi. can I help you")
        # pyt.speak("Halo, saya adalah Udin")
        
        print('Listening...')
        
        # batas biar listeningnya otomatis berhenti
        mendengar.pause_threshold = 0.9
        
        # phrase_time_limit = semakin besar angka maka sensitifitasnya akan berkurang, agar bisa digunakan di ruangan berisik
        suara = mendengar.listen(source, phrase_time_limit=5)
        
        try:
            print('Processing...')
            Layanan = mendengar.recognize_google(suara)
            # Layanan = mendengar.recognize_google(suara, language="id-ID")
            print(Layanan)
        
            
        except srec.UnknownValueError:
            Layanan = "Tidak mengerti perintah"
            print(Layanan)
            
        except:
            # jika ada anomasi di pass aja
            Layanan = "Tidak dapat terhubung ke layanan pengenalan suara"
            print(Layanan)
            # pass
        
        return Layanan
    
    
def talk(audio):
    engine.say(audio)
    engine.runAndWait()
    
def run_vale():
    Layanan = perintah()
    # print(Layanan)
    if 'open' in Layanan:
        video = Layanan.replace('open', '')
        pyt.speak('opening' + video)
        print(video + ' opening..')
        pywhatkit.playonyt(video)
        
    if 'find out' in Layanan:
        Wiki = Layanan.replace('find out', '')
        hasil = wikipedia.summary(Wiki, sentences = 2)
        print(hasil)
        pyt.speak(hasil)
    
    
run_vale()