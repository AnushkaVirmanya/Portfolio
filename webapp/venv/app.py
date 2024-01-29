import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def l_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lco = l_url("https://lottie.host/ed2b5b6d-fbd0-4b94-a405-f886f2cf92f3/s1Er8xnaE1.json")

#--Header
with st.container():
    st.subheader("Hi, I am Anushka Virmanya :wave:")
    st.title("Data Analyst & Tech Enthusiast")
    st.write("Hello there! I'm a seasoned Data Analyst with a Master's in Business Analytics, specializing in Data Science. I've contributed to impactful projects in SQL, Python, and Tableau, ranging from predictive modeling for HR efficiency to dynamic Tableau dashboards. Join me as I bring a unique blend of analytical expertise and a passion for data science innovation to your team!")
    st.write("[Tableau Profile>](https://public.tableau.com/app/profile/anushka2687/vizzes)")
    st.write("[Github>](https://github.com/AnushkaVirmanya)")

#-- about me
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Professional Experience:")
        st.write("##")
        st.write(
            """
            Passionate Explorer of Data: Navigating the world of data analytics with a focus on human resources, customer insights, and operational efficiency.

            Technology Enthusiast: Embracing the power of tools like SQL, Python, and Tableau to craft meaningful narratives from complex datasets.

            Innovator in Action: From predictive modeling to dynamic dashboards, each project reflects a commitment to making data-driven decisions accessible and impactful.

            Continuous Learner: Bridging the realms of business analytics and data science, exploring new horizons in the ever-evolving landscape of technology and its applications.
            """
        )
    with right_column:
        st_lottie(lco, height = 400)

# Contact --
with st.container():
    st.write("---")
    st.write("Get in touch with me!")
    st.write("##")

#contact
    contact_form = """
    <form action="https://formsubmit.co/anushka26081998@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="False">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea ="message" name="email" placeholder="Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


# CSS Snippet
css_snippet = """
/* CSS Snippet from W3schools: https://www.w3schools.com/howto/howto_css_contact_form.asp */
/* Style inputs with type="text", select elements and textareas */
input[type=message], input[type=email], input[type=text], textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
}

/* Style the submit button with a specific background color etc */
button[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
button[type=submit]:hover {
  background-color: #45a049;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
"""

# Display CSS in Streamlit app
st.markdown(f'<style>{css_snippet}</style>', unsafe_allow_html=True)
