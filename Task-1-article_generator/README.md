# Task 1: LLM Article Generator Chatbot

## Description
This project builds and compares a chatbot that uses three different open-source Large Language Models (LLMs) to generate articles based on user input. The goal is to assess their performance and identify the most suitable model for high-quality article creation.

The three models evaluated are:
* **Mistral-7B-Instruct-v0.2**
* **Phi-3-mini-4k-instruct**
* **Gemma-2B-IT**

## Instructions
1.  Ensure all dependencies from the updated `requirements.txt` are installed.
2.  Run the `article_generator.ipynb` notebook. The notebook contains the code to load the models, the Gradio GUI for interaction, and a detailed qualitative evaluation of the models.
3.  Launch the Gradio interface from the notebook to interact with the chatbot.

## Evaluation Method
The performance of the three LLMs is evaluated qualitatively within the main notebook (`article_generator.ipynb`).
* A standardized prompt is used to generate an article from each model.
* The outputs are then compared side-by-side.
* The assessment is based on criteria such as **coherence, relevance to the prompt, detail, and overall readability.**
* Based on this analysis, a concluding recommendation is provided for the most appropriate model for this task.
