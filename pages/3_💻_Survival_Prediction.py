import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time

with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)



st.title("Survival Prediction")
st.markdown("Enter a hypothetical case and we will predict its survival using a Artificial Intelligence")

left,right = st.columns(2)

with left:
    first_name=st.text_input("First Name")
with right:
    last_name = st.text_input("Last Name")


selected_inputs = []
with left:
    sex = st.selectbox('Sex', ['Male', 'Female'])
    if sex == 'Male':
        sex_male = True
    else:
        sex_male = False

with right:
    # Widget for selecting age
    age = st.slider('Age', 1, 100)

# Widget for selecting total family members

with left:
    seat_class = st.selectbox('Class', ['First Class', 'Second Class','Third Class'])
    with right:
        if seat_class == 'First Class':
            seat = 1
            fare = st.slider('Fare Range ($)', 50, 500)
        elif seat_class == 'Second Class' :
            seat = 2
            fare = st.slider('Fare Range ($)', 10, 50)
        elif seat_class == 'Third Class':
            seat = 3
            fare = st.slider('Fare Range($)', 1, 10)

selected_inputs.append(seat) 

total_family = st.selectbox('Total Family Members', list(range(11)))
selected_inputs.append(total_family)




selected_inputs.append(sex_male)
    
embarked_options = ["Cherbough","Queenstown",'Southampton']
embarked = st.selectbox('Embarked', embarked_options)
if embarked == 'Cherbough':
    embarked_bin = [True,False,False]
if embarked == 'Queenstown':
    embarked_bin = [False,True,False]
if embarked == 'Southampton':
    embarked_bin = [False,False,True]

selected_inputs.extend(embarked_bin)


if age < 12:
    age_bin = [True,False,False,False]
elif age < 20:
    age_bin = [False,True,False,False]
elif age < 60:
    age_bin = [False,False,True,False]
else:
    age_bin = [False,False,False,True]

selected_inputs.extend(age_bin)

#0,7.91,14.45,31,512

if fare <= 8:
    fare_bin = [True,False,False,False]
elif fare <= 15:
    fare_bin = [False,True,False,False]
elif fare <= 32:
    fare_bin = [False,False,True,False]
else:
    fare_bin = [False,False,False,True]

selected_inputs.extend(fare_bin)
    






if st.button('Predict'):
    prediction = model.predict([selected_inputs])
    progress_text = "Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty() 
    
    
    st.markdown(f""" ### Your Case study 
    - Your name is {first_name} {last_name} a {age} year old {sex.lower()} 
    - You are travelling with {total_family} family members.
    - You are {seat_class} passenger who has bought their ticket with ${fare}
                """)
    
    def stream_data():
        for word in line.split(' '):
            yield word + ' '
            time.sleep(0.05) 
    
    
    st.markdown("### Analysis of Case: ")
    
    if (age < 10) and (sex == "Male"):
        line = "1.Considering the survival rates, a 'children and women first' approach was implemented, thereby increasing your chances of survival."
        st.write_stream(stream_data)      
    elif sex == "Male":
        line = "1. We analyze that male teens/adults have a lower chance of survival due to the 'children and women first' approach for lifeboat accommodation."
        st.write_stream(stream_data)                 
    elif sex == "Female":
        line = ("1. We analyse that females have a higher chance of survival due to the \"children and women first\" approach for life boat accomodation")
        st.write_stream(stream_data)
    
    if(total_family > 0):
        line = "2. Even 1 family member increases chances of survival"
        st.write_stream(stream_data)
    else:
        line = "2. No family members considerably decrease chances of survival"
        st.write_stream(stream_data)
    
    if seat_class == "First Class":
        line = "3. First-class passengers may have had better access to lifeboats and evacuation assistance"
        st.write_stream(stream_data)
    else:
        line = "3. Second and Third-class passengers may have had less access to lifeboats and evacuation assistance compared to the First Class passengers"
        st.write_stream(stream_data)

    with st.spinner('Prediction Loading...'):
        time.sleep(2.5)
    st.success('Done!')
    
    st.markdown("### Prediction")
    
    if prediction == False:
        st.markdown(f"According to my AI model there is a 84% chance that **you would have not survived**. ")
    if prediction == True:
        st.markdown(f"According to my AI model there is a 84% chance that **you would have survived**. ")
