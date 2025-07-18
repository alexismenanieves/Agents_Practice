import streamlit as st
from fitness_agent import get_fitness_plan

st.title("🏋️‍♂️ AI Health & Fitness Plan Generator")
st.markdown("### Personalized fitness plan to achieve your health goals")

st.sidebar.header("⚙️ Health & Fitness Inputs")
st.sidebar.subheader("Personalize your plan")

age = st.sidebar.number_input("Age (in years)", min_value=10, max_value=100, value=25)
weight = st.sidebar.number_input("Weight (in kg)", min_value=30, max_value=200, value=70)
height = st.sidebar.number_input("Height (in cm)", min_value=100, max_value=250, value=170)
activity_level = st.sidebar.selectbox("Activity Level", ["Low", "Moderate", "High"])
fitness_level = st.sidebar.selectbox("Fitness Level", ["Beginner", "Intermediate", "Expert"])
fitness_goal = st.sidebar.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Endurance", "Flexibility"])

# Divider for aesthetics
st.markdown("---")

if st.sidebar.button("Generate exercise plan"):
    if not age or not weight or not height:
        st.sidebar.warning("Please fill in all required fields")
    else:
        with st.spinner("💥 Generating your personalized fitness plan..."):
            full_plan = get_fitness_plan(
                age, weight, height, activity_level, 
                fitness_level, fitness_goal
            )
            st.subheader("This is your personalized plan:")
            st.markdown(full_plan.content)
