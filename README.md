# zepto-capstone-project
Zepto Data & AI Platform

An end-to-end AI/ML project developed as part of the Certificate Program in Artificial Intelligence and Machine Learning.

Project Modules:
### module1 - Data Pipeline:

Scraped 60+ books from Books to Scrape using Requests and BeautifulSoup.
Cleaned and transformed price, rating, and availability data.
Converted GBP to INR using the fixed rate 1 GBP = 105.50 INR.
Stored the data in a normalized SQLite database.
Performed SQL queries and Pandas-based data validation.

### module 2 - Analytics & Machine Learning:

Performed data cleaning, EDA, visualization, and statistical analysis on the Titanic dataset.
Analyzed missing values, outliers, correlations, and survival patterns.
Built and evaluated Logistic Regression, Decision Tree, and Random Forest models.
Performed SMOTE, hyperparameter tuning, and model comparison.
Built a Linear Regression model for fare prediction.
Saved the complete ML pipeline using Joblib.

### module 3 - GenAI Support Assistant:

Built a policy-based RAG support assistant using Zepto policy documents.
Generated embeddings using all-MiniLM-L6-v2 and stored them in ChromaDB.
Implemented intent routing using LangGraph.
Added deterministic MOCK_LLM mode for offline execution.
Exposed the assistant through a FastAPI /ask API.
Added Docker support for local deployment.

Tech Stack:

Python | Pandas | NumPy | BeautifulSoup | SQLite | Seaborn | Scikit-learn | SMOTE | Joblib | Sentence Transformers | ChromaDB | LangGraph | FastAPI | Docker

Repository Structure
zepto-data-ai-platform/
│
├── README.md
│
├── data_pipeline/
│   ├── README.md
│   ├── scrape_and_load.py
│   └── queries.py
│
├── analytics/
│   ├── README.md
│   ├── 01_eda.ipynb
│   ├── 02_modeling.ipynb
│   └── titanic.csv
│
└── support_assistant/
    ├── README.md
    ├── ingestion.py
    ├── rag_graph.py
    ├── main.py
    ├── Dockerfile
    └── docs/

Key Learning Outcomes

This project demonstrates practical skills in data engineering, SQL, data analysis, machine learning, model evaluation, RAG, vector databases, API development, and Docker deployment.
