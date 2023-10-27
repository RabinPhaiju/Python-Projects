import sounddevice
from scipy.io.wavfile import write

fs = 44100
second = 10
print('recording...')
record_voice = sounddevice.rec(int(second*fs),samplerate=fs,channels=1)
sounddevice.wait()
write('Python_Apps/Voice_Recorder/output.wav',fs,record_voice)
