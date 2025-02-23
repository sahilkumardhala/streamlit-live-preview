import streamlit as st
import openai  # Ensure OpenAI API is available
import streamlit_pages as stp
import streamlit_navigation as stn
import streamlit_autorefresh
import streamlit_extras.stateful_button as stb
import streamlit_cookies_manager as scm
import streamlit_ace
import streamlit_pydantic
import streamlit_antd_components
import streamlit_lottie
import streamlit_agraph
import streamlit_webrtc
import streamlit_timeline
import streamlit_plotly_events
import streamlit_calendar
import streamlit_authenticator as stauth
import extra_streamlit_components as stx
import streamlit_jwt_authenticator as sja
import streamlit_extras
import streamlit_extras.stylable_container as sc
import streamlit_extras.switch_button as sb
import streamlit_tensorboard as sttb
import streamlit_pandas_profiling
import streamlit_ml_explorer as sme
import streamlit_sortables
import streamlit_javascript
import streamlit_nested_layout
import streamlit_3d_plotly
import streamlit_tqdm

allowed_globals = {
"builtins": {
"print": print,  # Allow safe printing
"len": len,  # Allow len function
"range": range,  # Allow range function
"int": int,  # Allow integer conversion
"float": float,  # Allow float conversion
"str": str,  # Allow string operations
"list": list,  # Allow list operations
"dict": dict,  # Allow dictionary operations
"set": set,  # Allow set operations
"tuple": tuple,  # Allow tuple operations
},
"st": st,  # Allow Streamlit usage
"openai": openai,  # Allow OpenAI API usage
"stp": stp,
"stn": stn,
"streamlit_autorefresh": streamlit_autorefresh,
"stb": stb,
"scm": scm,
"streamlit_ace": streamlit_ace,
"streamlit_pydantic": streamlit_pydantic,
"streamlit_antd_components": streamlit_antd_components,
"streamlit_lottie": streamlit_lottie,
"streamlit_agraph": streamlit_agraph,
"streamlit_webrtc": streamlit_webrtc,
"streamlit_timeline": streamlit_timeline,
"streamlit_plotly_events": streamlit_plotly_events,
"streamlit_calendar": streamlit_calendar,
"stauth": stauth,
"stx": stx,
"sja": sja,
"streamlit_extras": streamlit_extras,
"sc": sc,
"sb": sb,
"sttb": sttb,
"streamlit_pandas_profiling": streamlit_pandas_profiling,
"sme": sme,
"streamlit_sortables": streamlit_sortables,
"streamlit_javascript": streamlit_javascript,
"streamlit_nested_layout": streamlit_nested_layout,
"streamlit_3d_plotly": streamlit_3d_plotly,
"streamlit_tqdm": streamlit_tqdm,
}
code_snippets = {
    "Hello Streamlit": """import streamlit as st
st.title("Hello, Streamlit Preview!")""",
    
     "user input": """import streamlit as st
st.write("Here write your code")""",


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
