# Personal Code Assistant - Ollama + Langchain + Streamlit

This project demonstrates how to create a personal code assistant using a local open-source large language model (llm). We will utilize Codellama, a fine-tuned version of Llama specifically designed for coding tasks, along with Langchain and Streamlit to build a robust, interactive and user-friendly interface.

## Table of Contents
- [Pre-requisites](#pre-requisites)
- [Setting up the Environment](#setting-up-the-environment)
- [Customizing and testing the model](#customizing-and-testing-the-model)
- [Building UI-Langchain and Streamlit](#building-ui-langchain-and-streamlit)

## Pre-requisites

Before getting started, ensure that you have the following installed:
- [Conda](https://docs.conda.io/en/latest/miniconda.html): Package and environment management system.
- [Ollama](https://ollama.com/download): Platform that facilitates to make use of LLMs easily.

Also for doing this project, it is good to have experience using OpenAI API using Langchain integration for getting done with it more faster. 

## Setting up the Environment

- Create new conda environment:
```bash
conda create -n personal_code_assistant python=3.11
```
- Activate the environment:
```bash
conda activate personal_code_assistant
```
- Install all the required packages:
```bash
pip install -r requirements.txt
```

## Customizing and testing the model

We will be customizing the model for this project as we want the model to behave as closely as we want it to. `Modefile` enables us to achieve this. 

Steps as follows:

1. For this project, we will be downloading the quantized version (Q4_K_M) of **codellama** [model](https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF).

2. Go to models directory, download the model in it and then go back to the main directory of the project:
```bash
cd models
wget https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF/resolve/main/codellama-7b-instruct.Q4_K_M.gguf
cd ..
```

3. Include the following in `Modelfile`:
```
FROM models/codellama-7b-instruct.Q4_K_M.gguf

TEMPLATE "[INST] <<SYS>> {{ .System }} <</SYS>> {{ .Prompt }} [/INST]"
PARAMETER rope_frequency_base 1e+06
PARAMETER stop "[INST]"
PARAMETER stop "[/INST]"
PARAMETER stop "<<SYS>>"
PARAMETER stop "<</SYS>>"
SYSTEM """You are an intelligent coding assistant - CodyBot. Answer all the code related to the questions asked. Your capabilities include understanding and generating code in multiple programming languages, troubleshooting coding issues, optimizing algorithms, and providing explanations of complex programming concepts in a clear and concise manner."""
```

4. Run the command:
```bash
ollama create codybot -f Modelfile
```
Message at the end - success will indicate if the model is successfully customized. For further customization, checkout the [link](https://github.com/ollama/ollama/blob/main/docs/modelfile.md). 

5. Before going ahead with running in Python followed by building UI using Streamlit library, lets try our code assistant in the terminal:
```bash
ollama run codybot
```

Once we are satisfied with the behavior of how model is responding, we will proceed ahead.

## Building UI-Langchain and Streamlit

- Langchain provides wrapper to access local models - `ChatOllama` which can be used in the same way as `ChatOpenAI` module.
- `utils` folder includes all of the helper functions (`helper.py`), and commonly used libraries (`common_libraries.py`) organized. Prompt template(s) and other environment variable(s) (if used) are included `constants.py` folder.
- `app.py` includes the Streamlit implementation - making use of the libraries and helper functions from `utils` folder. 

Once the code is ready, we can run the following command:
```bash
streamlit run app.py
```



## References
- End To End Multi Programming Code Assistant App Using CodeLlama LLAMA2 Large Language Model: https://www.youtube.com/watch?v=-28YtPZ5u4s&t=96s&ab_channel=KrishNaik
- Unlock Ollama's Modelfile: https://www.youtube.com/watch?v=QTv3DQ1tY6I&ab_channel=PromptEngineer
