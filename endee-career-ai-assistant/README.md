# 🤖 AI Career Assistant using Endee (Vector-Based RAG System)

---

## 🚀 Project Overview

The **AI Career Assistant** is a SaaS-style intelligent system designed to provide career guidance using **vector-based semantic search and Retrieval-Augmented Generation (RAG)** concepts.

It allows users to:

* Explore career roles
* Get skill recommendations
* Generate career roadmaps
* Compare different job roles
* Identify skill gaps

The system mimics real-world AI assistants by combining **search + reasoning + structured responses**.

---

## 💡 Problem Statement

Students and professionals often struggle to:

* Choose the right career path
* Understand required skills
* Compare job roles
* Plan learning roadmaps

Traditional search systems lack **context awareness** and do not provide intelligent recommendations.

---

## ✅ Proposed Solution

This project implements an **AI-powered career assistant** using:

* Vector-based semantic search
* RAG-inspired retrieval
* Intent-based response generation

The system understands user queries and dynamically provides:

* Relevant career recommendations
* Structured insights
* Roadmaps and comparisons

---

## 🧠 System Architecture

User Query
⬇
Intent Detection
⬇
Vectorization (TF-IDF)
⬇
Similarity Search (Vector Matching)
⬇
Top Relevant Results
⬇
Response Formatting (RAG Style)
⬇
Frontend Chat UI

---

## ⚙️ Technical Approach

* Career data is stored as text documents
* Converted into vectors using **TF-IDF**
* User query is also vectorized
* **Cosine similarity** is used to find closest matches
* Results are filtered and structured
* Intent detection enables dynamic responses (roadmap, comparison, etc.)

---

## 🔍 How Endee is Used

* The project is built on top of the **forked Endee repository**
* Endee represents a **vector database system**
* This project demonstrates core concepts of vector databases:

  * Embedding generation
  * Vector similarity search
  * Retrieval-based AI (RAG)

> Note: This implementation focuses on demonstrating vector search principles inspired by Endee.

---

## 🚀 Features

### 🔍 Semantic Search

* Finds relevant career roles using vector similarity

### 🧠 RAG-based Responses

* Retrieves and formats structured career insights

### 🎯 Career Recommendations

* Top 3 relevant roles with confidence score

### 🧭 Career Roadmap Generator

* Step-by-step guidance for selected roles

### ⚖️ Career Comparison

* Compare multiple roles side-by-side

### 📉 Skill Gap Analysis

* Suggests missing skills required for target role

### 🤖 Agentic Career Suggestions

* Suggests roles based on user interest (e.g., "I like coding")

### 📊 Smart Tags

* Displays tags like:

  * 🔥 High Demand
  * 💰 High Salary
  * 🧠 AI Role

### 💬 Chat-based UI (SaaS Style)

* Interactive assistant similar to ChatGPT

---

## 💻 Tech Stack

* **Backend:** Python, FastAPI
* **ML:** Scikit-learn (TF-IDF, similarity)
* **Frontend:** HTML, CSS, JavaScript
* **Vector Concept:** Endee-inspired architecture

---

## ▶️ Setup & Installation

### 1. Clone Repository

```bash
git clone https://github.com/Attrivishal/endee.git
cd endee-career-ai-assistant
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Backend

```bash
uvicorn app:app --reload
```

### 5. Open Frontend

```bash
explorer.exe index.html
```

---

## 🌐 Usage

* Open the UI

* Ask questions like:

  * "Skills for data analyst"
  * "How to become data scientist"
  * "Compare frontend and backend"
  * "I like coding"

* Get intelligent responses instantly

---

## 🔮 Future Improvements

* Integrate full Endee vector database
* Add LLM-based response generation (OpenAI)
* Deploy as cloud SaaS application
* Add user authentication & history

---

## 🏆 Conclusion

This project demonstrates how modern AI systems work using:

* Semantic search
* Vector similarity
* RAG architecture
* Intelligent query handling

It provides a **real-world AI application** for career guidance.

---

## 📎 Submission

GitHub Repository:
👉 https://github.com/Attrivishal/endee

---

## 🙌 Acknowledgment

Inspired by vector database concepts and Endee architecture.
