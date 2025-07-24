# Final Internship Report

## Introduction
This report summarizes the work completed during the Generative AI internship with NullClass. The primary objective of this internship was to gain hands-on experience in developing and evaluating real-world Generative AI applications. This document outlines the tasks performed, skills acquired, challenges faced, and the overall outcomes of the internship.

## Learning Objectives
* To understand and implement various open-source and proprietary Large Language Models (LLMs).
* To build multi-modal applications capable of processing both text and image data.
* To integrate sentiment analysis into a conversational AI to create more empathetic and responsive applications.
* To learn best practices for evaluating, comparing, and deploying AI models.

## Activities and Tasks
Three core technical tasks were completed during this internship:

* **Task 1: LLM Article Generator:** A chatbot was developed to generate articles using three different open-source LLMs (Mistral-7B, Phi-3-mini, Gemma-2B-IT). A qualitative evaluation was performed to compare their outputs and identify the most suitable model for the task.

* **Task 2: Multi-Modal Chatbot:** The project was extended to a multi-modal application using Google's Gemini Pro for text and Gemini Pro Vision for image understanding. A Streamlit GUI was created to allow users to interact with the chatbot using either text or uploaded images.

* **Task 3: Sentiment-Aware Chatbot:** Sentiment analysis was integrated using the TextBlob library. The application can now detect the emotional tone (positive, negative, neutral) of user input and tailor its response accordingly. The model's effectiveness was quantitatively verified against a sample dataset.

## Skills and Competencies
* **LLM Integration:** Experience with `transformers`, Google `generative-ai`, and `TextBlob` libraries.
* **UI Development:** Proficiency in building interactive web UIs with `Streamlit` and `Gradio`.
* **API Security:** Understanding of secure API key management using environment variables.
* **Model Evaluation:** Practical application of both qualitative analysis for generative tasks and quantitative metrics (precision, recall, confusion matrix) for classification tasks.

## Challenges and Solutions
* **Challenge 1: Meaningful Evaluation of Generative Models (Task 1).**
    * **Problem:** Initially, a flawed classification metric was used to evaluate article generation, which was not meaningful.
    * **Solution:** The approach was revised to use a qualitative analysis, comparing model outputs on coherence, relevance, and detail—a standard practice for evaluating generative AI.

* **Challenge 2: Verifying Sentiment Model Performance (Task 3).**
    * **Problem:** The initial submission relied on the claimed accuracy of the TextBlob library without verification.
    * **Solution:** A quantitative evaluation was implemented. A labeled dataset was used to test the model, and its performance was formally documented using a classification report and confusion matrix from `scikit-learn`.

## Conclusion
This internship provided invaluable practical experience in the end-to-end development of Generative AI applications. Through the completion of three distinct tasks, I have significantly improved my skills in model integration, multi-modal development, and performance evaluation. The hands-on approach has prepared me for tackling complex, real-world AI challenges.
