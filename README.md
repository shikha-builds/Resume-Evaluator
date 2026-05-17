# Resume-Evaluator

## It is a web application built using Machine Learning, NLP, Generative-AI. Analyzing the Resume provided, it results:
1. ATS Resume Scoring
2. Venn Diagram Visualization
3. Skills Matching
4. Missing Skills Detection
5. AI Suggestions using Gemini-API

## Tech stack:
- Frontend: Streamlit
- Backend: Flask
- Machine Learning/NLP: spaCy, Scikit-learn, NLP Processing
- Visualization: Matplotlib, matplotlib-venn
- AI-Integration: Gemini API
- Deployment: Railway

## Dataset
[technical_skills](https://www.kaggle.com/datasets/nitinsen001/tech-skill-dataset-with-categories)

## Project Structure:
```
RESUME-EVALUATOR/
│
├── backend/
│   ├── __init__.py
│   ├── ats.py
│   ├── flask_api.py
│   ├── llm.py
│   ├── parser.py
│   ├── preprocessing.py
│   ├── skills.py
│   └── venn.py
│
├── dataset/
│   └── technical_skills.csv
│
├── models/
│   └── skills.json
│
├── .env
├── .gitignore
├── app.py
├── evaluator.ipynb
├── packages.txt
├── Procfile
├── README.md
├── requirements.txt
```
***Note: test_api.py is a debugging temporary file used to test API connectivity and model response.*** 

## Workflow
1. Upload Resume PDF
2. Paste Job Description
3. Extract Resume Text
4. Clean & Preprocess Text
5. Extract Skills
6. Compare Resume Skills with JD Skills
7. Calculate ATS Score
8. Generate Venn Diagram
9. Detect Missing Skills
10. Generate AI Suggestions using Gemini API

## Future Improvements
- Resume Keyword Optimization
- Downloadable PDF Reports
- Multi-language Resume Support

*Contributions are welcome! Fork the repository and submit a pull request.*
