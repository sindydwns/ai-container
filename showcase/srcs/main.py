import requests
import gradio as gr

fastapi_test_server = "http://fastapi:8000"
response = requests.get(fastapi_test_server)

with gr.Blocks() as demo:
    with gr.Tab("test docker networks"):
        gr.Label(value=response.text)

demo.launch(server_name="0.0.0.0", server_port=7860)
