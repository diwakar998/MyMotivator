#import dotenv
import openai
import requests
import datetime
#import os
import streamlit as st
#from dotenv import load_dotenv
#load_dotenv()
#import os
openai.api_key = st.secrets["OPENAI_API_KEY"]  #api_key=st.secrets["OPENAI_API_KEY"]
#print("the api key is ", os.getenv("OPENAI_API_KEY"))
#client = OpenAI(api_key="KngEsfDmjmHorBGnxKLr2mieuELUjRoFdli7ajyBftpFj5PibIkfvcVLukEbtgDt4-2gxVnumT3BlbkFJp4Ospqv2VR1gat8LaUSsXz0j4QaCy-vk_96_br2PvuArMbK4IMcCfEh23li1yftbKvgA6sLsUA")
#client = openai(api_key)

# Set the app title
st.title("🤖🤖 Your Motivation Expert")
st.title("Welcome to the AI Assistant 🎉")
st.write("Select your choice:")

choice = st.radio(
    "Pick your vibe:",
    [
        "Motivational Speaker (Akshay Kumar)",
        "Strict Teacher (Gabbar Singh)",
        "Yoga Instructor (Baba Ramdev)"
    ]
)

st.write(f"You selected: **{choice}** 🚀")

#choice = int(input("Enter your choice: "))

if choice == "Motivational Speaker (Akshay Kumar)":
    SYSTEM_PROMPT = """You are a helpful Motivational speaker AI assistant who is specialized in boosting user's confidence by resolving the user query in positive manner.
    You give response in bollywood actor Akshay Kumar's style. A light weight comedy style is must."""
elif choice == "Strict Teacher (Gabbar Singh)":
    SYSTEM_PROMPT = """You are a strict teacher AI assistant who is specialized in resolving user query in a very strict and disciplined manner.
    You give response in Bollywood actor Gabbar Singh's style. Add "Are o Samba" style in your reply. You don't tolerate any nonsense. Give reply in two - three punchy lines. """
elif choice == "Yoga Instructor (Baba Ramdev)":
    SYSTEM_PROMPT = """You are a Yoga instructor AI assistant who is specialized in resolving user query in a very calm and peaceful manner.
    You give response in Indian yoga guru Baba Ramdev's style. You always promote yoga and healthy lifestyle.
    Always reply in Hindi language. 
    Add "Yoga se hoga" at the end of each response."""

messages = [
    {"role":"system", "content": SYSTEM_PROMPT}
]
while True:
    # User input
    query = st.chat_input("How can I help you today...")
    #query = input(">Enter your query: ")
    if query.lower() in ["exit", "quit", "bye","end"]:
        print("Goodbye!")
        break
    messages.append({"role":"user", "content": query})
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    #print(response.choices[0].message.content)
    st.markdown(response.choices[0].message.content)

    #print(response.output_text)
