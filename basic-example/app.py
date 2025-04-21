import streamlit as st

st.title("Zoo Ticket")
adult = st.number_input("How many adult tickets: ")
children = st.number_input("How many children tickets: ")
day_selection = st.radio("select any one ", ("Weekend", "Weekdays"))

button_click = st.button("Submit")

if button_click:
    if day_selection == "Weekend":
        adult = adult * 12.5
        children = children * 7.5
        total = adult + children
    elif day_selection == "Weekdays":
         adult = adult * 10
         children = children * 5.5
         total = adult + children
    st.write("Total amount is ", total)