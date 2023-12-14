import os
import openai
from google.cloud import speech
import google.cloud.texttospeech as tts
from flask import session

from app.db import get_db

openai.api_key = "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"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'client_service_key.json'
speech_client = speech.SpeechClient()

def text_to_wav(voice_name: str, text: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )
    filename = f"{voice_name}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)

def speech_to_text(
    config: speech.RecognitionConfig,
    audio: speech.RecognitionAudio,
) -> speech.RecognizeResponse:
    client = speech.SpeechClient()

    # Synchronous speech recognition request
    response = client.recognize(config=config, audio=audio)

    return response

def simplifier(prompt):
    messages = message_history()
    messages.append({"role": "user", "content":f"Please simplify this sentence, so it can be understood by people with dyslexia: {prompt}"})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages).choices[0].message.content
    db = get_db()
    db.execute("INSERT INTO messages (user_id, user_message, system_response) VALUES (?, ?, ?)", (session["user_id"], prompt, response))
    db.commit()
    return response

def summarizer(prompt):
    messages = message_history()
    messages.append({"role": "user", "content":f"Please summarize this text, in an easy and understandable way, so it can be understood by people with dyslexia, use bulletpoints: {prompt}"})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages).choices[0].message.content
    db = get_db()
    db.execute("INSERT INTO messages (user_id, user_message, system_response) VALUES (?, ?, ?)", (session["user_id"], prompt, response))
    db.commit()
    return response

def former(prompt):
    messages = message_history()
    messages.append({"role": "user", "content":f"Please form this text into a one or two sentence: {prompt}"})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages).choices[0].message.content
    db = get_db()
    db.execute("INSERT INTO messages (user_id, user_message, system_response) VALUES (?, ?, ?)", (session["user_id"], prompt, response))
    db.commit()
    return response

def fixer(prompt):
    messages = message_history()
    messages.append({"role": "user", "content":f"Please correct this sentence: {prompt}"})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages).choices[0].message.content
    db = get_db()
    db.execute("INSERT INTO messages (user_id, user_message, system_response) VALUES (?, ?, ?)", (session["user_id"], prompt, response))
    db.commit()
    return response

def feedbacker(prompt):
    messages = message_history()
    messages.append({"role": "user", "content":f"Give me easily understandable feedback on this text correctness: {prompt}"})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages).choices[0].message.content
    db = get_db()
    db.execute("INSERT INTO messages (user_id, user_message, system_response) VALUES (?, ?, ?)", (session["user_id"], prompt, response))
    db.commit()
    return response 

def message_history():
    message_dict = []
    
    db = get_db()
    
    messages = db.execute("SELECT * FROM messages WHERE user_id == ?", (session["user_id"],)).fetchall()
    for message in messages:
        message_dict.append({"role": "user", "content": message["user_message"]})
        message_dict.append({"role": "system", "content": message["system_response"]})
    return message_dict
    