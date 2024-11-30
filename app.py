import streamlit as st
import pandas as pd
import json
import os


from generate_prompts import (
    get_json,
    get_spawn,
    get_remove
)

# Initialize session state for the text input
if "text_field_value" not in st.session_state:
    st.session_state.text_field_value = ""

if "text_area_value" not in st.session_state:
    st.session_state.text_area_value = ""

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if 'df' not in st.session_state:
    # Read the CSV into the session state DataFrame
    st.session_state.df = pd.DataFrame(columns=["prompt", "formatted_json", "action"])

# Function to update the text field
def update_text_field(value):
    st.session_state.text_field_value = value

def update_text_area(value):
    st.session_state.text_area_value = value

def clear_form():
    st.session_state.text_field_value = ""
    st.session_state.text_area_value = ""

def append_data():
    if st.session_state.text_field_value == "" or st.session_state.text_area_value == "":
        st.warning("Empty Prompt Sample or Formatted JSON")
    else:
        data = json.loads(st.session_state.text_area_value)
        new_data = {
            "prompt": st.session_state.text_field_value,
            "formatted_json": json.dumps(data, separators=(',', ':')),
            "action": data["action"]
        }
        st.session_state.df = st.session_state.df._append(new_data, ignore_index=True)

# App Title
st.title("Prompt Generator")

# Buttons in a row
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Spawn", use_container_width=True):
        # get random move prompt
        prompt = get_spawn()
        update_text_field(prompt)

        # setup default move json
        formatted_json = get_json("spawn")
        update_text_area(formatted_json)

with col2:
    if st.button("Move", use_container_width=True):
        update_text_field("Move button clicked!")

with col3:
    if st.button("Remove", use_container_width=True):
        prompt = get_remove()
        update_text_field(prompt)

        formatted_json = get_json("remove")
        update_text_field(formatted_json)

with col4:
    if st.button("Rotate", use_container_width=True):
        update_text_field("Rotate button clicked!")

with col5:
    if st.button("Replace", use_container_width=True):
        update_text_field("Replace button clicked!")

# Text Field (uses session state for dynamic updates)
text_input = st.text_input("Prompt Sample:", value=st.session_state.text_field_value)

# Textarea at the bottom
text_area = st.text_area("Formatted JSON:", value=st.session_state.text_area_value, height=250)

col6, col7 = st.columns(2)

with col6:
    st.button("Clear", use_container_width=True, on_click=clear_form)

with col7:
    st.button("Add", use_container_width=True, on_click=append_data)

# Show DataFrame here and make it cover the whole container width
sorted_df = st.session_state.df.sort_index(ascending=False)

col8, col9 = st.columns(2)

with col8:
    st.subheader("Output Sample")

st.dataframe(sorted_df, use_container_width=True)