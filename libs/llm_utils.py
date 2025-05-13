import google.generativeai as genai
from libs.menu_loader import load_menu
import os
from dotenv import load_dotenv

load_dotenv()

cake_menu=load_menu()

SYSTEM_INSTRUCTIONS = (
	f"You are a friendly assistant for a homemade cake business based in Dubai and Sharjah. \n"
    "Your name is Habibi Cakes"
	f"Here is the cake menu : \n {cake_menu}\n\n"
	"Help the customer through the following steps : \n"
	"1. Greet the customer and show the menu. \n"
	"2. Ask what cake they want and confirm if it exists in the menu. \n"
	"3. Ask for their delivery location (only in Dubai and Sharjah) \n"
	"4. Ask for preferred delivery time. \n"
	"5. Ask for the occasion (e.g. Birthday,festival,etc) \n"
	"6. Ask if they need special decorations (name or other requests). \n"
	"7. Once all information is collected, generate a clear and cheerful order summary : \n"
	" Cake Name \n -Price(AED)\n -Location\n -Delivery Time \n - Occasion\n -Decorations\n"
	"Total \n"
	"8. End by reminding them the payment is offline. \n"
	"Usee emojis to make the experience friendly and fun!"
)

API_KEY=os.getenv("LLM_API_KEY")

genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("gemini-2.0-flash")

chat=None
def start_session():
    global chat
    chat=model.start_chat()
    chat.send_message(SYSTEM_INSTRUCTIONS)
    print("LLM Configuration completed!!")

def send_msg_to_llm(message):
    resp=chat.send_message(message)
    return resp.text