# Chatbot for Student Enquiry  -  README

## Description
The Chatbot for Student Enquiry is designed to assist new students and their parents by answering queries about the college, such as admission processes, fee structures, and facilities. It automates the enquiry desk operations, reducing the workload on staff while providing prompt, accurate responses. Key features include speech recognition, text-to-speech, and multilingual support (English, Kannada, and Telugu).

## Table of Contents
1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Requirements/Dependencies](#requirementsdependencies)
4. [Installation Steps](#installation-steps-to-setup-project)
5. [Usage Instructions](#usage-instructions)
6. [Project goals](#projectgoals)
7. [Future Enhancements](#futureenhancements)
8. [Acknowledgements](#acknowledgements)
9. [Conclusion](#conclusion)
10. [References](#references)

## Introduction
A chatbot is an AI-powered software application that simulates human-like conversations via text or voice. The purpose of this chatbot is to address college-related queries and improve the user experience. It ensures seamless communication through advanced features like Natural Language Processing (NLP), speech-to-text conversion, and multilingual interactions.


## Technologies Used
- **Programming Language:** Python 3.6+
- **Framework:** Flask (for the backend)
- **Database:** MySQL
- **Libraries/Tools:**
  - NLTK for NLP tasks
  - PySpellChecker for spell correction
  - Sklearn for TF-IDF and cosine similarity
  - HTML, CSS, JavaScript for frontend
  - Google Translator API for multilingual support

## Requirements/Dependencies
### Hardware Requirements
- **Processor:** Dual-core or higher
- **RAM:** 4 GB or more
- **Storage:** 1 GB minimum
- **Network:** Internet connectivity

### Software Requirements
- **Operating System:** Windows/Linux/macOS
- **Tools:** Visual Studio Code, MySQL Workbench
- **Dependencies:** Python libraries such as Flask, NLTK, and PySpellChecker



## Installation Steps to Setup Project
- **Install Dependencies:**
  - Ensure Python 3.6+ is installed. Use pip to install the required libraries:
    ```bash
        Pip install flask nltk sklearn PyMySQL
- **Set Up the Database:**
   - Create a database and import the provided schema.
   - Update the database connection settings in config.py.
- ** Start the Flask Server:**
   ```bash
        Python app.py
-Open the application in your web browser at http://localhost:5000 .

## Usage
- **Register/Login:** Create an account or log in with your credentials.
- **Interact with the Bot:** Type your query or use the voice input feature and Select your preferred language for responses.
- **FAQs:** Click on predefined FAQs for quick answers.

## Project Goals
- **Student Empowerment:** Provide instant, accurate information to students.
-** Accessibility:** Ensure inclusivity for users with language or physical barriers.
- ** Efficiency:** Reduce workload on administrative staff and improve response times.


## Future Enhancements
- Integrate deep learning models for enhanced intent recognition.
- Expand language support for broader accessibility.

- Add personalized interaction features and analytics-driven insights.

  ## Acknowledgement
- Ms. ShwethaShree A, Assistant Professor, Department of CSE, BITM, Ballari, for her invaluable  guidance and support.
- The faculty and staff of BITM for providing the resources and encouragement that made this project possible.

## Conclusion
The Chatbot for Student Enquiry successfully streamlines communication by automating responses to routine queries, thereby enhancing operational efficiency and accessibility. Its advanced features, such as NLP, multilingual support, and speech functionalities, make it a valuable tool for students and parents.

## References
- Walaa Hassan, Shereen elBohy, Mina Rafik, Ahmed Ashraf, Sherif Gorgui, Michael Emil, Karim Ali. “An Interactive Chatbot for College Enquiry” Journal of Computing and Communication Vol.2, No.1, PP. 20-28, 2023
- A. Kousar Nikhath, Vijaya Saraswathi R, MD Abdul Rab, N Venkata Bharadwaja, L Goutham Reddy, K Saicharan, C Venkat Manas Reddy. "An Intelligent College Enquiry Bot using NLP and Deep Learning based techniques.” Janauary-2022.
- Pavithra N, M A Bindhushree, Nanditha V, Pooja R, Shilpa. "AI-Based Automated Voice Responder for College Queries." International Journal of Innovative Research in Science, Engineering and Technology (IJIRSET) Volume 13, Issue 5, May 2024.
- A. Balamurugan, D. Thiruppathi, S. P. Santhoshkumar, K. Susithra. "Artificial Intelligence-Based Chatbot with Voice Assistance.” 2024 International Conference on Trends in Quantum Computing and Emerging Business Technologies CHRIST (Deemed to be University), Pune Lavasa Campus, India. Mar 22-23, 2024.
- Sangeeta Kumari, Zaid Naikwadi, Akshay Akole, Purushottam Darshankar. “Enhancing College Chat Bot Assistant with the Help of Richer Human Computer Interaction and Speech Recognition.” Proceedings of the International Conference on Electronics and Sustainable Communication Systems (ICESC 2020) IEEE Xplore Part Number: CFP20V66-ART; ISBN: 978-1-7281-4108-4
