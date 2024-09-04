import streamlit as st

# Set up color scheme based on the Chrome extension
st.markdown(
    """
    <style>
    .main {
        background-color: #e3f2fd;
        color: #0d47a1;
    }
    .stButton>button {
        background-color: #0d47a1;
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-size: 14px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1565c0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header section
st.title("Welcome to AppliTracker")
st.subheader("Track Your Job Applications Seamlessly")

st.write(
    """
    **AppliTracker** is a Chrome extension that helps you track job applications 
    effortlessly by scraping relevant details from LinkedIn and storing them 
    in a Google Spreadsheet. 
    """
)

# Section for answering functionality questions
st.header("Key Features and Functionality")

st.write(
    """
    - **Automated Job Tracking**: AppliTracker scrapes job details such as 
      company name, role, and date applied directly from LinkedIn using DOM 
      manipulation.
    - **Google Sheets Integration**: The extension automatically updates a Google Spreadsheet with your job application data.
    - **OAuth 2.0**: Secure authentication via OAuth ensures that your Google account remains safe.
    - **Data Security**: AppliTracker stores your job application data securely in your Google Drive, and we do not share or store your data elsewhere.
    """
)

# Section for highlighting privacy policy
st.header("Privacy Policy")

st.write(
    """
    We value your privacy. Your data is only used for tracking job applications 
    in your Google Spreadsheet and is not shared with third parties. For a 
    complete overview of our privacy practices, please refer to our [Privacy Policy](https://github.com/PrathamRanjan/AppliTrackrPP).
    """
)

# Footer with an action button
if st.button("Get the AppliTracker Chrome Extension"):
    st.write("Visit the Chrome Web Store to download AppliTracker and streamline your job application process!")
