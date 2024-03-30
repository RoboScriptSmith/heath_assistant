import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Home',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['house', 'activity', 'heart', 'person'],
                           default_index=0)


# Home Page
if selected == 'Home':
    st.title('Welcome to Health Assistant')
    
    st.header('About Disease Detection:')
    st.write('This application provides prediction for three diseases: Diabetes, Heart Disease, and Parkinson\'s Disease. \
              Select the corresponding option from the sidebar to make predictions.')
    
    st.header('About Diseases:')
    
    st.subheader('Diabetes:')
    st.write('Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or when \
              the body cannot effectively use the insulin it produces.')
    st.write('**Symptoms:** Increased thirst, frequent urination, unexplained weight loss, etc.')
    st.write('[Learn more about diabetes](https://www.diabetes.org/)')
    
    st.subheader('Heart Disease:')
    st.write('Heart disease refers to several types of heart conditions, including coronary artery disease, heart rhythm \
              problems, and heart defects present at birth.')
    st.write('**Symptoms:** Chest pain or discomfort, shortness of breath, fatigue, etc.')
    st.write('[Learn more about heart disease](https://www.heart.org/en/health-topics/heart-attack/about-heart-attacks)')
    
    st.subheader('Parkinson\'s Disease:')
    st.write('Parkinson\'s disease is a progressive nervous system disorder that affects movement. Symptoms start gradually, \
              sometimes starting with a barely noticeable tremor in just one hand.')
    st.write('**Symptoms:** Tremors, bradykinesia, muscle rigidity, etc.')
    st.write('[Learn more about Parkinson\'s disease](https://www.parkinson.org/)')

# Diabetes Prediction Page
elif selected == 'Diabetes Prediction':
    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.slider('Number of Pregnancies', min_value=0, max_value=20, value=0)

    with col2:
        Glucose = st.slider('Glucose Level', min_value=0, max_value=200, value=100)

    with col3:
        BloodPressure = st.slider('Blood Pressure value', min_value=0, max_value=150, value=80)

    with col1:
        SkinThickness = st.slider('Skin Thickness value', min_value=0, max_value=100, value=20)

    with col2:
        Insulin = st.slider('Insulin Level', min_value=0, max_value=300, value=100)

    with col3:
        BMI = st.slider('BMI value', min_value=0, max_value=50, value=25)

    with col1:
        DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function value', min_value=0.0, max_value=2.0, value=0.5, step=0.1)

    with col2:
        Age = st.slider('Age of the Person', min_value=0, max_value=120, value=30)


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider('Age', min_value=20, max_value=100, value=40)

    with col2:
        sex = st.slider('Sex (0 for female, 1 for male)', min_value=0, max_value=1, value=1)

    with col3:
        cp = st.slider('Chest Pain types', min_value=0, max_value=3, value=1)

    with col1:
        trestbps = st.slider('Resting Blood Pressure', min_value=80, max_value=200, value=120)

    with col2:
        chol = st.slider('Serum Cholestoral in mg/dl', min_value=100, max_value=600, value=200)

    with col3:
        fbs = st.slider('Fasting Blood Sugar > 120 mg/dl', min_value=0, max_value=1, value=0)

    with col1:
        restecg = st.slider('Resting Electrocardiographic results', min_value=0, max_value=2, value=0)

    with col2:
        thalach = st.slider('Maximum Heart Rate achieved', min_value=50, max_value=220, value=150)

    with col3:
        exang = st.slider('Exercise Induced Angina', min_value=0, max_value=1, value=0)

    with col1:
        oldpeak = st.slider('ST depression induced by exercise', min_value=0.0, max_value=10.0, value=0.0, step=0.1)

    with col2:
        slope = st.slider('Slope of the peak exercise ST segment', min_value=0, max_value=2, value=1)

    with col3:
        ca = st.slider('Major vessels colored by flourosopy', min_value=0, max_value=4, value=0)

    with col1:
        thal = st.slider('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value=0, max_value=2, value=1)

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
elif selected == "Parkinsons Prediction":

    # Page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.slider('MDVP:Fo(Hz)', min_value=0.0, max_value=300.0, value=150.0)

    with col2:
        fhi = st.slider('MDVP:Fhi(Hz)', min_value=0.0, max_value=300.0, value=150.0)

    with col3:
        flo = st.slider('MDVP:Flo(Hz)', min_value=0.0, max_value=300.0, value=150.0)

    with col4:
        Jitter_percent = st.slider('MDVP:Jitter(%)', min_value=0.0, max_value=2.0, value=0.5)

    with col5:
        Jitter_Abs = st.slider('MDVP:Jitter(Abs)', min_value=0.0, max_value=0.1, value=0.05)

    with col1:
        RAP = st.slider('MDVP:RAP', min_value=0.0, max_value=0.1, value=0.05)

    with col2:
        PPQ = st.slider('MDVP:PPQ', min_value=0.0, max_value=0.1, value=0.05)

    with col3:
        DDP = st.slider('Jitter:DDP', min_value=0.0, max_value=0.1, value=0.05)

    with col4:
        Shimmer = st.slider('MDVP:Shimmer', min_value=0.0, max_value=1.0, value=0.5)

    with col5:
        Shimmer_dB = st.slider('MDVP:Shimmer(dB)', min_value=0.0, max_value=1.0, value=0.5)

    with col1:
        APQ3 = st.slider('Shimmer:APQ3', min_value=0.0, max_value=0.1, value=0.05)

    with col2:
        APQ5 = st.slider('Shimmer:APQ5', min_value=0.0, max_value=0.1, value=0.05)

    with col3:
        APQ = st.slider('MDVP:APQ', min_value=0.0, max_value=0.1, value=0.05)

    with col4:
        DDA = st.slider('Shimmer:DDA', min_value=0.0, max_value=0.1, value=0.05)

    with col5:
        NHR = st.slider('NHR', min_value=0.0, max_value=0.5, value=0.25)

    with col1:
        HNR = st.slider('HNR', min_value=0.0, max_value=30.0, value=15.0)

    with col2:
        RPDE = st.slider('RPDE', min_value=0.0, max_value=1.0, value=0.5)

    with col3:
        DFA = st.slider('DFA', min_value=0.0, max_value=1.0, value=0.5)

    with col4:
        spread1 = st.slider('spread1', min_value=-1.0, max_value=1.0, value=0.0)

    with col5:
        spread2 = st.slider('spread2', min_value=-1.0, max_value=1.0, value=0.0)

    with col1:
        D2 = st.slider('D2', min_value=0.0, max_value=10.0, value=5.0)

    with col2:
        PPE = st.slider('PPE', min_value=0.0, max_value=1.0, value=0.5)

    # Code for Prediction
    parkinsons_diagnosis = ''

    # Creating a button for Prediction
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

