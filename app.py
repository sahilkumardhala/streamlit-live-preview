import streamlit as st
from stlite_sandbox import stlite_sandbox
import streamlit.components.v1 as components
from  code_snippet import code_snippets
import os

st.set_page_config(page_title="Streamlit Live Code Preview",
                     page_icon="random",
                    layout="wide",
                    initial_sidebar_state="collapsed"
                    )
st.logo("https://streamlit.io/images/brand/streamlit-mark-color.png")
st.title("Streamlit Live Code Preview")
st.markdown("---")
# css for text areas
st.markdown("""
    <style>
    /* Default height for laptops and desktops */
    .stTextArea textarea {
        height: 200px;
    }

    /* Adjust height for mobile devices */
    @media (max-width: 600px) {
        .stTextArea textarea {
            height: 100px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# st.sidebar.
# st.markdown("---")
# col1, col2 = st.columns(2)
# with col1:
left, right = st.columns([2, 1])
with left:
    st.subheader("Streamlit code Snippets 📚")
with right:
    selected_code = st.selectbox("🔍Choose an example or input:", 
                                    list(code_snippets.keys()),
                                    help="Select a code snippet to preview")

user_code = st.text_area("📝Edit or past your Streamlit script:", 
                            code_snippets[selected_code], 
                            height=300,
                            help="Enter your Streamlit code snippet\
                            by selecting user input in ")

# Sidebar with live preview of the code
if 'show_me' not in st.session_state:
    st.session_state.show_me = False
st.markdown("---")
# with col2:
left, right = st.columns([2, 1])

with left:
    st.subheader("Streamlit.io Preview🔮")

with right:
    if st.button('💫Do magic🪄',key="do_magic"):
        st.session_state.show_me = not st.session_state.show_me
    
    
st.markdown("---")
if user_code:
    try:
        # Display the markdown content if visible
        if st.session_state.show_me:
            stlite_sandbox(user_code)
        else:
            st.warning("Preview hidden by default. Click '��Do magic���' to show.")
    except Exception as e:

        st.error(f"Error in execution: {e}")
    
# Function to read the any file
def get_file_content_as_string(path: str) -> str:
    """Reads a file and returns its content as a string."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
    
# Show file link in the sidebar
def show_render_file(file_path):
    """Render a file content in the sidebar."""
    # file_name = os.path.splitext(file_path)[0] # Remove file extension
    st.sidebar.markdown(get_file_content_as_string(f"{file_path}"))

show_render_file("setup.md")



# Footer
st.markdown("---")
st.markdown("Copyright 2025. All Rights Reserved.")
st.markdown("[Streamlit Prerviews](https://github.com/sahilkumardhala)")
