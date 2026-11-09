
import truststore
truststore.inject_into_ssl()

import streamlit as st
from rag_engine import answer_question

st.set_page_config(
    page_title="School RAG",
    page_icon="📚",
    layout="centered"
)

st.title("📚 העוזר של בית ספר אופק")

st.write(
    "שלום! אפשר לשאול אותי שאלות על "
    "נהלי בית הספר, שעות הפעילות, "
    "מבחנים וטיולים."
)

st.divider()

question = st.text_input(
    "מה תרצי לדעת?",
    placeholder="לדוגמה: מהן שעות פעילות הספרייה?"
)

if st.button("שליחת שאלה"):
    if question.strip():
        with st.spinner("מחפש מידע ומכין תשובה..."):
            answer, sources = answer_question(question)

        st.subheader("תשובת העוזר")
        st.write(answer)

        # הצגת שמות המסמכים בלבד, ללא תוכנם
        no_info_message = (
            "לא מצאתי מידע על כך במסמכי בית הספר."
        )

        if sources and answer.strip() != no_info_message:
            file_names = []

            for result in sources:
                file_name = result.node.metadata.get("file_name")

                if file_name and file_name not in file_names:
                    file_names.append(file_name)

            if file_names:
                st.caption(
                    "מסמכים שאוחזרו: " + ", ".join(file_names)
                )

    else:
        st.warning("יש להקליד שאלה לפני השליחה.")
