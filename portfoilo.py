#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Basic Information
st.title("My Portfolio")
st.write("Welcome to my portfolio! Here you'll find information about my skills, projects, and experience.")

# About Section
st.header("About Me")
st.write("Hello! I'm [Your Name], a [Your Profession]. I specialize in [Your Specialization] and have experience in [Your Experience].")

# Skills Section
st.header("Skills")
st.write("Here are some of the skills I bring to the table:")
skills = ["Python", "Machine Learning", "Data Analysis", "Streamlit", "OpenCV"]
for skill in skills:
    st.markdown(f"- {skill}")

# Projects Section
st.header("Projects")
project1 = {
    "title": "Project 1",
    "description": "Description of project 1. What did you achieve? What tech stack did you use?",
    "link": "http://github.com/your-profile/project1"
}
project2 = {
    "title": "Project 2",
    "description": "Description of project 2. What did you achieve? What tech stack did you use?",
    "link": "http://github.com/your-profile/project2"
}

for project in [project1, project2]:
    st.subheader(project["title"])
    st.write(project["description"])
    st.write(f"[GitHub Link]({project['link']})")

# Contact Section
st.header("Contact Me")
st.write("Feel free to reach out to me through:")
st.write("- [LinkedIn](https://linkedin.com/in/your-profile)")
st.write("- [GitHub](https://github.com/your-profile)")
st.write("- [Email](mailto:your-email@example.com)")

