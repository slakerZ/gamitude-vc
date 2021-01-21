# gamitude-vc
# Vosk
## For vosk-server can eat a lot of ram
docker run -d -p 2700:2700 alphacep/kaldi-en:latest
can be tested with rest_microphone.py
## there is vosk pip package not tested yet
pip3 install vosk
## For SpeechRecognition
in case of error while installing pyaudio  
sudo apt install portaudio19-dev python3-pyaudio
for pocketsphinx error
sudo apt-get install swig
sudo apt-get install libpulse-dev