import streamlit as st
import requests

def main():
    st.title("Item List App")

    items = requests.get('http://backend:5000/api/items').json()

    st.write("Items:")
    for item in items:
        st.write(f"- {item['name']}")

if __name__ == "__main__":
    main()
    