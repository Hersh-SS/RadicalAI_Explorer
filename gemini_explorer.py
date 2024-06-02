import vertextai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import generativeModel, Part, Context, ChatSession

project = "sample-gemini"
vertexai.init(project = project)

config = generative_models.GenerationConfig(
    temperature=0.4
)
# Load model with config
model = GenerativeModel(
    "gemini-pro",
    generation_config = config
)
chat = model.start_chat()