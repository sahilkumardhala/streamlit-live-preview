
code_snippets = {
    "Hello Streamlit": """import streamlit as st
st.title("Hello, Streamlit Preview!")
st.info("I am a streamlit preview application.Here, I am streaming the Livepreview of your `Streamlit_app.py` application")""",
    
     "user input": """import streamlit as st
st.write("Here write your code")""",

"My portfolio":'''import streamlit as st
st.markdown("""
    <iframe src="https://sahil-kumar-dhala-portfolio.vercel.app"
            width="100%" height="800px"></iframe>
""", unsafe_allow_html=True)''',
    "Chart Example": """import streamlit as st
import pandas as pd
import altair as alt

data = pd.DataFrame({'x': range(10), 'y': range(10)})
st.altair_chart(alt.Chart(data).mark_line().encode(x='x', y='y'))
""",

    "Basic Button": """import streamlit as st
st.button('Click Me!')
""",

    "Text Input": """import streamlit as st
user_input = st.text_input("Enter some text:")
st.write("You entered:", user_input)
""",

    "Slider Example": """import streamlit as st
value = st.slider("Select a value", 0, 100, 50)
st.write("Slider value:", value)
""",

    "Checkbox Example": """import streamlit as st
if st.checkbox("Show/Hide"):
    st.write("You checked the box!")
""",

    "Radio Button Example": """import streamlit as st
choice = st.radio("Pick an option:", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", choice)
""",

    "Dropdown Selectbox": """import streamlit as st
option = st.selectbox("Choose a fruit:", ["Apple", "Banana", "Orange"])
st.write("You selected:", option)
""",

    "File Uploader": """import streamlit as st
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file:
    st.write("File uploaded successfully!")
""",

    "Progress Bar": """import streamlit as st
import time

progress = st.progress(0)
for i in range(101):
    time.sleep(0.05)
    progress.progress(i)
st.success("Task Completed!")
""",

    "DataFrame Display": """import streamlit as st
import pandas as pd

df = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]})
st.dataframe(df)
""",

    "Matplotlib Chart": """import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
""",

    "Line Chart": """import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(data)
""",

    "Bar Chart": """import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.bar_chart(data)
""",

    "Expander Example": """import streamlit as st
with st.expander("Click to expand"):
    st.write("This is hidden content revealed by clicking the expander.")
""",

    "Session State Counter": """import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.write("Counter:", st.session_state.counter)

if st.button("Increase"):
    st.session_state.counter += 1
""",
}
