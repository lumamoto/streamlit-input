import streamlit as st
import pandas as pd

DATA_URL = './data.csv'

def main():
    st.title("Write a nice comment!")
    data = pd.read_csv(DATA_URL)

    name = st.text_input("Name")
    comment = st.text_input("Comment")

    if st.button('Add to CSV'):
        new_row = {'Name':name, 'Comment':comment}
        st.markdown('**Added new row!** Name: ' + name + ', Comment: ' + comment)
        data = data.append(new_row, ignore_index=True)
        data.to_csv(DATA_URL, index=False)

    st.markdown('## All Comments')
    st.dataframe(data)

main()