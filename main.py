# import streamlit as st
# import time
# import requests
# import random

# st.title("Money Making Machine")

# def generate_money():
#     return random.randint(1,1000)

# st.subheader("Instant Cash Generator")    
# if st.button("Generate Money"):
#     st.write("Counting your Money....")
#     time.sleep(1)
    
# amount = generate_money()
# st.success(f"Your made ${amount}")   

# def fetch_side_hustle():
#     try:
#         response = requests.get("AIzaSyCoRUo91zSV1YmRM82PR5rh0fI0nRCJsfM")
#         if response.status_code == 200:
#             hustles =response.json()
#             return hustles
#         else:
#             return("No side hustles found")
#     except:
#         return("Something went wrong..😟")
    
# st.subheader("Side Hustle Ideas")    
# if st.button("Generate Hustle"):
#      idea=fetch_side_hustle()
#      st.success(idea)

# import streamlit as st
# import random, time
# import google.generativeai as genai


# # ---------- Config ----------
# GOOGLE_API_KEY= ("AIzaSyCoRUo91zSV1YmRM82PR5rh0fI0nRCJsfM")
# genai.configure(api_key=st.secrets["google_api_key"])
# model = genai.GenerativeModel("gemini-pro")

# # ---------- UI ----------
# st.title("💰 Money‑Making Machine")

# # Use session state so the number persists across reruns
# if "cash" not in st.session_state:
#     st.session_state.cash = None

# # ----- Cash generator -----
# st.subheader("Instant Cash Generator")
# if st.button("Generate Money"):
#     st.write("Counting your money…")
#     time.sleep(1)
#     st.session_state.cash = random.randint(1, 1000)
#     st.success(f"You made ${st.session_state.cash}!")

# # ----- Side‑hustle ideas -----
# if st.session_state.cash is not None:
#     st.subheader("Side‑Hustle Ideas")
#     if st.button("Generate Hustle"):
#         prompt = (
#             f"Suggest one creative side‑hustle idea for someone who just made "
#             f"${st.session_state.cash}. Keep it under 30 words."
#         )
#         try:
#             response = model.generate_content(prompt)
#             idea = response.text.strip()
#             st.success(idea)
#         except Exception as e:
#             st.error(f"API error: {e}")
# else:
#     st.info("Generate some cash first, then we’ll find a hustle!")

import streamlit as st
import time
import random
import requests

st.title("💰 Money‑Making Machine")

# ---------- Cash generator ----------
st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money…")
    time.sleep(1)
    amount = random.randint(1, 1000)
    st.success(f"You made ${amount}!")

    # ---------- Side‑hustle fetch ----------
    st.subheader("Side‑Hustle Ideas")

    # Example without an external API
    ideas = [
        "Start a dropshipping store 🛒",
        "Offer freelance graphic design 🎨",
        "Create an online course 📚",
        "Flip items on marketplaces 🔄",
        "Develop a niche newsletter 📨"
    ]
    chosen = random.choice(ideas)
    st.success(chosen)
 
