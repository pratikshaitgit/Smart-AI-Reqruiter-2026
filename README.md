# AI Recruiter System

## 📌 Overview
This project is an AI-based recruiter system that ranks candidates based on a given job description.

It helps recruiters identify the best candidates by analyzing their skills, education, and relevance to the job role.

---

## 🚀 Features
- Skill matching (Python, NLP, AI)
- Candidate scoring system
- Ranking of candidates
- Explanation for each candidate

---

## 🧠 Approach
- Extract important keywords from the job description
- Match candidate skills with job requirements
- Assign scores based on relevance
- Rank candidates accordingly

Optional:
- Semantic similarity using AI models (SentenceTransformers)

---

## 🛠️ Tech Stack
- Python
- NLP concepts
- Rule-based scoring

---

## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the project:
python main.py

---

## 📊 Output
The system outputs ranked candidates with scores and reasons in the output.txt file.

---

## 🔮 Future Improvements
- Add semantic search using embeddings
- Integrate LLM for better understanding
- Build a web interface

---

## 📂 Project Structure

AI-RECRUITER/
│── data/
│   ├── candidates.jsonl
│   ├── job_description.txt
│── src/
│   ├── embed.py
│   ├── preprocess.py
│   ├── rank.py
│── main.py
│── requirements.txt
│── output.txt
│── README.md
