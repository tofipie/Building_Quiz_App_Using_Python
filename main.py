import streamlit as st
import random
import time

# Title of the Application
st.title("📝 Interactive Quiz Application")

# Instructions
with st.expander("ℹ️ How to Play"):
    st.write("""
    - Select the correct answer from the given options.
    - Click **Submit Answer** to check if you are correct.
    - You will get instant feedback.
    - Click **Next Question** to move forward.
    - Your progress will be displayed at the top.
    """)

# Define quiz questions, options, and answers
questions = [
    {"question": "What is the capital of Pakistan?", "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], "answer": "Islamabad"},
    {"question": "Who is the founder of Pakistan?", "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"], "answer": "Muhammad Ali Jinnah"},
    {"question": "Which is the national language of Pakistan?", "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"], "answer": "Urdu"},
    {"question": "What is the currency of Pakistan?", "options": ["Rupee", "Dollar", "Taka", "Riyal"], "answer": "Rupee"},
    {"question": "Which city is known as the City of Lights in Pakistan?", "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"], "answer": "Karachi"},
]

# Initialize session state variables
if "quiz_progress" not in st.session_state:
    st.session_state.quiz_progress = 0
    st.session_state.correct_answers = 0
    st.session_state.remaining_questions = questions.copy()
    random.shuffle(st.session_state.remaining_questions)

# Show progress
st.progress(st.session_state.quiz_progress / len(questions))
st.write(f"📊 **Question {st.session_state.quiz_progress + 1} of {len(questions)}**")

# Select current question
if st.session_state.remaining_questions:
    current_question = st.session_state.remaining_questions[0]
    st.subheader(current_question["question"])

    # Create radio buttons for answer choices
    selected_option = st.radio("Choose your answer:", current_question["options"], key="answer")

    # Submit button
    if st.button("✅ Submit Answer"):
        if selected_option == current_question["answer"]:
            st.success("🎉 Correct! Well done.")
            st.session_state.correct_answers += 1
        else:
            st.error(f"❌ Incorrect! The correct answer is **{current_question['answer']}**.")

        # Remove the current question from the list
        st.session_state.remaining_questions.pop(0)
        st.session_state.quiz_progress += 1

        time.sleep(2)
        st.rerun()

# Show final score
if not st.session_state.remaining_questions:
    st.subheader("🎉 Quiz Completed!")
    st.write(f"✅ **Your Score: {st.session_state.correct_answers} / {len(questions)}**")
    st.balloons()
    if st.button("🔄 Restart Quiz"):
        st.session_state.quiz_progress = 0
        st.session_state.correct_answers = 0
        st.session_state.remaining_questions = questions.copy()
        random.shuffle(st.session_state.remaining_questions)
        st.rerun()
