import streamlit as st
from stlite_sandbox import stlite_sandbox
import streamlit.components.v1 as components
from  code_snippet import code_snippets
import os

st.set_page_config(page_title="Streamlit Live Code Preview",
                     page_icon="random",
                    layout="wide",
                    initial_sidebar_state="auto"
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
    st.subheader("Real-time Preview 🔮")

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
            st.markdown("""<a href="https://www.producthunt.com/posts/streamlit-preview?embed=true&utm_source=badge-featured&utm_medium=badge&utm_souce=badge-streamlit&#0045;preview" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=938526&theme=light&t=1741278956797" alt="Streamlit&#0032;Preview - Live&#0032;preview&#0032;of&#0032;your&#0032;streamlit&#0032;app&#0032;in&#0032;Browser&#0046; | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>""", unsafe_allow_html=True)
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

st.markdown("""<a href="https://www.producthunt.com/posts/streamlit-preview?embed=true&utm_source=badge-featured&utm_medium=badge&utm_souce=badge-streamlit&#0045;preview" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=938526&theme=light&t=1741278956797" alt="Streamlit&#0032;Preview - Live&#0032;preview&#0032;of&#0032;your&#0032;streamlit&#0032;app&#0032;in&#0032;Browser&#0046; | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>""", unsafe_allow_html=True)

show_render_file("setup.md")



# Footer
st.markdown("---")
st.markdown("Copyright 2025. All Rights Reserved.")
st.markdown("[SAHIL KUMAR DHALA](https://github.com/sahilkumardhala)")
