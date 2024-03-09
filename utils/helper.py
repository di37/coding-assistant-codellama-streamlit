import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils.common_libraries import *
from utils.constants import *

def get_realtime_response(user_prompt: str, model="codybot", **kwargs):
    """
    This function takes a user prompt as a string, an optional model parameter, and arbitrary keyword arguments,
    and returns a realtime response.
    """
    llm = ChatOllama(model=model, **kwargs)
    prompt = ChatPromptTemplate.from_template(CODE_TEMPLATE)
    chain = prompt | llm | StrOutputParser()
    response = chain.stream({"user_prompt": user_prompt})
    return response

def configure_generation():
    """
    Add sliders for temperature, top_p, top_k, and max_output_tokens
    """
    # Add sliders for temperature, top_p, top_k, and max_output_tokens
    st.sidebar.header("Generation Configuration")
    temperature = st.sidebar.slider(
        "Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.01
    )
    top_p = st.sidebar.slider(
        "Top P", min_value=0.0, max_value=1.0, value=0.9, step=0.01
    )
    top_k = st.sidebar.slider("Top K", min_value=0, max_value=100, value=40, step=1)
    n_ctx = st.sidebar.slider(
        "Maximum Context Length", min_value=1, max_value=4096, value=2048, step=1
    )

    generation_config = {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "num_ctx": n_ctx,
    }
    
    return generation_config