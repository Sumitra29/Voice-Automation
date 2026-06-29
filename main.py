from TTS.api import TTS
from pydub import AudioSegment
import json
import os

model_name = "tts_models/multilingual/multi-dataset/your_tts"
tts = TTS(model_name)

input_file = r"C:\Users\sumit\Desktop\Me_April26\Python-backend-projects\YouTube-TTS-Automation-Tool\input\quiz.json"
speaker = r"C:\Users\sumit\Desktop\Me_April26\Python-backend-projects\YouTube-TTS-Automation-Tool\clean-voice\clean_voice.wav"
output_folder = r"C:\Users\sumit\Desktop\Me_April26\Python-backend-projects\YouTube-TTS-Automation-Tool\output"

with open(input_file, "r", encoding="utf-8") as f:
    quiz = json.load(f)

audio = AudioSegment.silent(duration=0) 
for item in quiz:
    question_read = f"Question {item['id']}: {item['question']}"
    question_temp = f"question_{item['id']}.wav" 
    tts.tts_to_file(
        text= question_read, 
        speaker_wav = speaker,
        language = "en",
        file_path = question_temp 
    )
    question_audio = AudioSegment.from_wav(question_temp)
    os.remove(question_temp)

    answer_read = f"Answer: {item['answer']}"
    answer_temp = f"answer{(item['id'])}.wav"
    tts.tts_to_file(
        text = answer_read,
        speaker_wav = speaker,
        language = "en",
        file_path = answer_temp
    )
    answer_audio = AudioSegment.from_wav(answer_temp)
    os.remove(answer_temp)

    audio += question_audio
    audio += AudioSegment.silent(duration=5000)

    audio += answer_audio
    audio += AudioSegment.silent(duration=1000)

output_path = os.path.join(output_folder, "quiz_audio.mp3")
audio.export(output_path, format="mp3")
print("Voice clone completed: ", output_path)

