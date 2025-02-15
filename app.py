import streamlit as st
from transformers import pipeline

# Load the text-generation model from Hugging Face
generator = pipeline("text-generation", model="gpt2")

# Streamlit UI
st.title("AI-Powered Resume Generator")
st.write("Fill in your details to generate a professional resume.")

# User Inputs
name = st.text_input("Full Name")
job_title = st.text_input("Target Job Title")
experience = st.text_area("Work Experience (e.g., years, key roles, etc.)")
skills = st.text_area("Key Skills (e.g., programming languages, technologies, etc.)")
education = st.text_area("Education (e.g., degrees, institutions, etc.)")
projects = st.text_area("Notable Projects (e.g., web development, personal projects, etc.)")
awards = st.text_area("Awards & Achievements (e.g., recognitions, titles, etc.)")
additional_info = st.text_area("Additional Information (e.g., open-source contributions, personal goals, etc.)")

# Generating the Resume
if st.button("Generate Resume"):
    # Format the resume content as a prompt
    prompt = f"""
    Create a structured professional resume for {name}, targeting {job_title}.

    ### Personal Information:
    - Name: {name}
    - Target Job Title: {job_title}

    ### Work Experience:
    {experience}

    ### Key Skills:
    {skills}

    ### Education:
    {education}

    ### Projects:
    {projects}

    ### Awards & Achievements:
    {awards}

    ### Additional Information:
    {additional_info}

    ### Professional Summary:
    Write a compelling summary highlighting strengths, achievements, and experience in the software web development field. Emphasize your passion for web design, technical expertise, and contributions to open-source communities.
    """
    
    # Generate resume content using Hugging Face GPT-2 model
    response = generator(prompt, max_length=700, num_return_sequences=1, no_repeat_ngram_size=2)

    # Display the generated resume
    st.subheader("Generated Resume")
    st.write(response[0]['generated_text'])
