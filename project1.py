import streamlit as slt
from googletrans import Translator

slt.header('Language Translator')
input = slt.text_area("Please enter the text", value="")
option = slt.selectbox(
    'Language to which you wish to translate this text to?',
    ('Malayalam', 'Hindi', 'Tamil'))
if slt.button("Translate"):
    translator = Translator()
    translation = translator.translate(input, dest=option)
    slt.write(translation.text)


