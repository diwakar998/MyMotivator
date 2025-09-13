#import dotenv
import OpenAI
import requests
import datetime
#import os
import streamlit as st
#from dotenv import load_dotenv
#load_dotenv()
#import os
api_key=st.secrets["OPENAI_API_KEY"]
#print("the api key is ", os.getenv("OPENAI_API_KEY"))
#client = OpenAI(api_key="KngEsfDmjmHorBGnxKLr2mieuELUjRoFdli7ajyBftpFj5PibIkfvcVLukEbtgDt4-2gxVnumT3BlbkFJp4Ospqv2VR1gat8LaUSsXz0j4QaCy-vk_96_br2PvuArMbK4IMcCfEh23li1yftbKvgA6sLsUA")
client = OpenAI(api_key)
'''
def get_weather(city):
    url=f"https://wttr.in/{city}?format=%C+%t"
    headers = {
        "User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, header=headers)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Could not retrieve weather data."
    except requests.RequestException as e:
        return f"An error occurred: {e}"
    
avaiable_tools = {
    "get_weather": get_weather
}
'''
print("Welcome to the AI assistant. Select your choice:")
print("1. Moticationa Speaker (Akshay Kumar)")
print("2. Strict Teacher (Gabbar Singh)")
print("3. Yoga Instructor (Baba Ramdev)")

choice = int(input("Enter your choice: "))

if choice == 1:
    SYSTEM_PROMPT = """You are a helpful Motivational speaker AI assistant who is specialized in boosting user's confidence by resolving the user query in positive manner.
    You give response in bollywood actor Akshay Kumar's style. A light weight comedy style is must."""
elif choice == 2:
    SYSTEM_PROMPT = """You are a strict teacher AI assistant who is specialized in resolving user query in a very strict and disciplined manner.
    You give response in Bollywood actor Gabbar Singh's style. Add "Are o Samba" style in your reply. You don't tolerate any nonsense. Give reply in two - three punchy lines. """
elif choice == 3:
    SYSTEM_PROMPT = """You are a Yoga instructor AI assistant who is specialized in resolving user query in a very calm and peaceful manner.
    You give response in Indian yoga guru Baba Ramdev's style. You always promote yoga and healthy lifestyle.
    Always reply in Hindi language. 
    Add "Yoga se hoga" at the end of each response."""

messages = [
    {"role":"system", "content": SYSTEM_PROMPT}
]
while True:
    query = input(">Enter your query: ")
    if query.lower() in ["exit", "quit", "bye","end"]:
        print("Goodbye!")
        break
    messages.append({"role":"user", "content": query})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print(response.choices[0].message.content)
    #print(response.output_text)
