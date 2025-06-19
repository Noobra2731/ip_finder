import streamlit as st
import requests


def get_public_ip():

    try:
        return requests.get("https://api.ipify.org").text
    except requests.exceptions.RequestException as ex:
        return f"ip not found: {ex}"


st.badge("Home", color="green")
st.title = ("Public IP Detector")
st.subheader("create by Anup das(A-23119)")
if st.button("Detect IP"):
    st.badge("success")
    st.success(f"Your public IP address is: {get_public_ip()}")
    st.text(f"thanks for using....")
else:
    st.badge("need reviev..")
