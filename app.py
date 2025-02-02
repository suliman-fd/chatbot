import gradio as gr
from transformers import pipeline

# Load your fine-tuned model
generator = pipeline(
    "text-generation",
    model="./my_ai_model",  # Path to your model
    tokenizer="./my_ai_model",
)

def respond(message, history):
    history.append(f"User: {message}")
    prompt = "\n"f"User: {message}\nBot:"
    response = generator(
        prompt,
        max_length=100,
        temperature=0.7,
        do_sample=True,
    )[0]["generated_text"]
    return response.split("Bot:")[1].strip()

# Launch the Gradio app
gr.ChatInterface(respond).launch()