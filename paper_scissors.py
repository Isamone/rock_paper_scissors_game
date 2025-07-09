import streamlit as st
import random

st.title("✊ Rock, 🖐 Paper, ✌️ Scissors Game")

options = ["Rock", "Paper", "Scissors"]
Saddiqahs_choice = st.selectbox("Choose your move:", options)

if st.button("Play"):
    AI_ISMAIL_choice = random.choice(options)

    st.write(f"🧍 Saddiqas chose: **{Saddiqahs_choice}**")
    st.write(f"🤖 AI ISMAIL chose: **{AI_ISMAIL_choice}**")

    if Saddiqahs_choice == AI_ISMAIL_choice:
        st.info("It's a tie!")
    elif (
        (Saddiqahs_choice == "Rock" and AI_ISMAIL_choice == "Scissors") or
        (Saddiqahs_choice == "Scissors" and AI_ISMAIL_choice == "Paper") or
        (Saddiqahs_choice == "Paper" and AI_ISMAIL_choice == "Rock")
    ):
        st.success("Saddiqah wins! 🎉")
    else:
        st.error("AI ISMAIL wins! 😢")