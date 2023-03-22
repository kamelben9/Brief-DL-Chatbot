import streamlit as st
from streamlit_chat import message as st_message
from transformers import BlenderbotTokenizer
from transformers import BlenderbotForConditionalGeneration
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

# Vos identifiants LUIS
LUIS_APP_ID = "45a8a0ff-4a92-4e40-9435-c8778f550d36"
LUIS_SUBSCRIPTION_KEY = "7f586401c872466486e4c057b08fee10"
LUIS_RUNTIME_ENDPOINT = "https://briefagilecedrickamelkevinomar-authoring.cognitiveservices.azure.com/"

st.experimental_singleton
def get_models():
    model_name= 'facebook/blenderbot-400M-distill'
    tokenizer=BlenderbotTokenizer.from_pretrained(model_name)
    model=BlenderbotForConditionalGeneration.from_pretrained(model_name)
    return tokenizer,model

if "history" not in st.session_state:
    st.session_state.history=[]

st.title("Hello Chatbot")

# Fonction pour envoyer une requête à LUIS et obtenir l'intention et les entités
def get_intent(input_text):
    credentials = CognitiveServicesCredentials(LUIS_SUBSCRIPTION_KEY)
    client = LUISRuntimeClient(endpoint=LUIS_RUNTIME_ENDPOINT, credentials=credentials)
    prediction_request = {"query": input_text}
    prediction_response = client.prediction.get_slot_prediction(LUIS_APP_ID, "production", prediction_request)
    intent = prediction_response.prediction.top_intent
    entities = prediction_response.prediction.entities
    return intent, entities

def generate_answer():
    tokenizer,model = get_models()
    user_message= st.session_state.input_text

    # Obtenir l'intention et les entités avec LUIS
    intent, entities = get_intent(user_message)

    # Ajouter les entités à la requête du modèle
    inputs = tokenizer(user_message, return_tensors="pt")
    for entity in entities:
        inputs[entity['type']] = [entity['entity']]

    result = model.generate(**inputs)

    st.session_state.history.append({"message":user_message,"is_user":True})
    st.session_state.history.append({"message":tokenizer.decode(result[0]),"is_user":False})

st.text_input("Talk to the bot",key="input_text",on_change=generate_answer)

for chat in st.session_state.history:
    st_message(**chat)