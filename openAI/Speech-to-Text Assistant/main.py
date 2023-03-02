import gradio as gr
import openai
import config

openai.api_key = config.OPENAI_API_KEY



def transcribe(audio):
    print(audio)

    return "transcribing"


ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source='microphone', type='filepath'), outputs='text')

ui.launch()
