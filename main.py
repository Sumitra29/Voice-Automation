from TTS.api import TTS

model_name = "tts_models/en/ljspeech/vits"

tts = TTS(model_name)

input_file = r"C:\Users\sumit\Desktop\Me_April26\Python-backend-projects\YouTube-TTS-Automation-Tool\input\input.txt"
output_file = r"C:\Users\sumit\Desktop\Me_April26\Python-backend-projects\YouTube-TTS-Automation-Tool\output\voice.wav"

with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

tts.tts_to_file(text=text, file_path=output_file)
print("Voice clone completed: ", output_file)
