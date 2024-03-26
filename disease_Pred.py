#import necessary libraries
import pickle
import pandas as pd
import streamlit as st 
from streamlit_option_menu import option_menu

#Loading models

dia_model = pickle.load(open("./savedModel/diabetes.sav",'rb'))
heart_model = pickle.load(open("./savedModel/heart.sav",'rb'))
par_model = pickle.load(open("./savedModel/parkinsons.sav",'rb'))


#sidebar for navigation
with st.sidebar:

    selected = option_menu('E-Doctor Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],icons = ['activity','heart','person'],default_index =0)


#Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):

    #Page title
    st.title('Diabetes Prediction using ML')

    #getting the input data from the user
    col1,col2,col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPFV = st.text_input('Diabetes Predigree Function value')
    with col2:
        Age = st.text_input('Age of Person')

# code for Predication
    diab_diagnosis =  ''     

# Create a button for Predication

    if st.button('Diabetes Test Result'):
        diab_prediction = dia_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPFV,Age]])   

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

        st.success(diab_diagnosis)


#Heart diesease Prediction Page
if(selected == 'Heart Disease Prediction'):

    #Page title
    st.title('Heart disease Prediction using ML')

    #getting the input data from the user
    col1,col2,col3,col4 = st.columns(4)

    with col1:
        age = st.text_input('Age of the person')
    
    with col2:
        sex= st.text_input('Sex')

    with col3:
        cp = st.text_input('chest Pain types')
    with col4:
        RestingBP= st.text_input('Resting Blood Pressure')
    with col1:
        chol = st.text_input('Serum Choestroal in mg/dl')
    with col2:   
        fbs = st.text_input('Fating Blood Suger>120 mg/dl')  
    with col3:
        restecg = st.text_input('Resting Electrocardiographic results') 
    with col4:
        maxxHeartRate = st.text_input('Maximum hart rate achieved')
    with col1:
        exang = st.text_input('Exercise Induced Angina')
    with col2:
        oldpeak = st.text_input('oldpeak')
    with col3:
        slope = st.text_input('ST depression induced by erercise')
    with col4:
        ca= st.text_input('Slope of the peak exercise ST segment')
    with col1:
        thal = st.text_input('Major vessels coloures by flourosopy')

# code for Predication
    heart_diagnosis =  ''     

# Create a button for Predication

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age,sex,cp,RestingBP,chol,fbs,restecg,maxxHeartRate,exang,oldpeak,slope,ca,thal]])   

        if(heart_prediction[0]==1):
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'

        st.success(heart_diagnosis)

#Parkinson's diesease Prediction Page
if(selected == 'Parkinsons Prediction'):

    #Page title
    st.title('Parkinson disease Prediction using ML')

    #getting the input data from the user
    col1,col2,col3 = st.columns(3)

    with col1:
        MDVPFo = st.text_input('MDVP_Fo(HZ)')
    with col2:
        MDVPFhi= st.text_input('MDVP_Fhi(HZ)')
    with col3:
        MDVPFlo = st.text_input('MDVP_Flo(HZ)')
    with col1:
        MDPVJitter_per= st.text_input('MDPV_Jitter(%)')
    with col2:
        MDPVJitter_abs= st.text_input('MDPV_Jitter(Abs)')
    with col3:
        MDVPRAP = st.text_input('MDVP_RAP')
    with col1:
        MDVPPPQ = st.text_input('MDVP_PPQ')   
    with col2:
        JitterDDP	 = st.text_input('Jitter_DDP')
    with col3:
        MDVPShimmer = st.text_input('MDVP_Shimmer')
    with col1:
        MDVPShimmer_dB = st.text_input('MDVP_Shimmer(dB)')
    with col2:
        ShimmerAPQ3	= st.text_input('Shimmer_APQ3')
    with col3:
        ShimmerAPQ5 = st.text_input('Shimmer_APQ5')
    with col1:
        MDVPAPQ= st.text_input('MDVP_APQ')
    with col2:
        ShimmerDDA = st.text_input('Shimmer_DDA')
    with col3:
        NHR= st.text_input('NHR')
    with col1:
        HNR= st.text_input('HNR')
    with col2:
        RPDE= st.text_input('RPDE')
    with col3:
        DFA= st.text_input('DFA')
    with col1:
        spread1= st.text_input('spread1')    
    with col2:
        spread2= st.text_input('spread2')
    with col3:
        D2=st.text_input('D2')    
    with col1:
        PPE= st.text_input('PPE')                                  

# code for Predication
    parkinsons_diagnosis =  ''     

# Create a button for Predication

    if st.button('Parkinsons Test Result'):
        parkinsons_prediction = par_model.predict([[MDVPFo,MDVPFhi,MDVPFlo, MDPVJitter_per,MDPVJitter_abs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer ,MDVPShimmer_dB,ShimmerAPQ3, ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])   

        if(parkinsons_prediction[0]==1):
            parkinsons_diagnosis = 'The person has parkinsons disease'
        else:
            parkinsons_diagnosis = 'The person does not have parkinsons disease'

        st.success(parkinsons_diagnosis)
