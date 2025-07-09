import streamlit as st
import random

st.title("✊ Rock, 🖐 Paper, ✌️ Scissors Game")

options = ["Rock", "Paper", "Scissors"]
player_choice = st.selectbox("Choose your move:", options)

if st.button("Play"):
    AI_ISMAIL_choice = random.choice(options)

    st.write(f"🧍 You chose: **{player_choice}**")
    st.write(f"🤖 AI_ISMAIL chose: **{AI_ISMAIL_choice}**")

    if player_choice == AI_ISMAIL_choice:
        st.info("It's a tie!")
    elif (
        (player_choice == "Rock" and AI_ISMAIL_choice == "Scissors") or
        (player_choice == "Scissors" and AI_ISMAIL_choice == "Paper") or
        (player_choice == "Paper" and AI_ISMAIL_choice == "Rock")
    ):
        st.success("You win! 🎉")
    else:
        st.error("AI_ISMAIL wins! 😢")