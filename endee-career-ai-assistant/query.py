from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Load data
with open("data/careers.txt", "r") as f:
    docs = f.readlines()

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(docs)


# 🔹 Format response
def format_response(text):
    parts = text.split(".")
    return {
        "role": parts[0].strip(),
        "skills": parts[1].strip() if len(parts) > 1 else "",
        "description": parts[2].strip() if len(parts) > 2 else ""
    }


# 🔹 Roadmap
def generate_roadmap(role):
    roadmap = {
        "Data Scientist": ["Learn Python", "Statistics", "Machine Learning", "Deep Learning", "Projects"],
        "Data Analyst": ["Excel & SQL", "Python", "Visualization", "Projects"],
        "Frontend Developer": ["HTML/CSS", "JavaScript", "React", "Projects"],
        "Backend Developer": ["Node/Python", "Database", "API", "Deployment"]
    }
    return roadmap.get(role, ["Learn basics", "Build projects"])


# 🔹 Smart Tags
def generate_tags(role):
    tags = {
        "Data Scientist": ["🔥 High Demand", "💰 High Salary", "🧠 AI Role"],
        "DevOps Engineer": ["🔥 High Demand", "⚙️ Infra", "💰 High Salary"],
        "Frontend Developer": ["🎨 Creative", "🌐 Web", "🔥 Popular"],
        "Backend Developer": ["⚙️ Server", "🧠 Logic", "🔥 Demand"]
    }
    return tags.get(role, ["📈 Growing Role"])


# 🔹 Intent detection
def detect_intent(query):
    q = query.lower()

    if "compare" in q or "vs" in q:
        return "compare"
    elif "roadmap" in q or "how to become" in q:
        return "roadmap"
    elif "suggest" in q or "recommend" in q:
        return "recommend"
    elif "i know" in q:
        return "skill_gap"
    elif "i like" in q:
        return "agent"
    else:
        return "search"


# 🔹 Semantic Search
def semantic_search(query):
    query_vec = vectorizer.transform([query])
    similarity = (vectors * query_vec.T).toarray().flatten()
    sorted_indices = similarity.argsort()[::-1]

    results = []

    for i in sorted_indices:
        score = round(similarity[i] * 100, 2)

        if score < 10:
            continue

        formatted = format_response(docs[i])

        results.append({
            "role": formatted["role"],
            "skills": formatted["skills"],
            "description": formatted["description"],
            "score": score,
            "tags": generate_tags(formatted["role"])
        })

        if len(results) == 3:
            break

    return results


# 🔹 MAIN FUNCTION
def search(query):
    intent = detect_intent(query)

    # 🔥 Greeting
    if query.lower().strip() in ["hi", "hello", "hlo", "hey"]:
        return {
            "type": "message",
            "text": "Hello 👋 Ask me about careers, skills, roadmap or comparisons!"
        }

    results = semantic_search(query)

    if len(results) == 0:
        return {
            "type": "message",
            "text": "⚠️ Try asking clearly like 'skills for data analyst' or 'compare roles'."
        }

    # 🔥 1. COMPARISON
    if intent == "compare":
        return {
            "type": "compare",
            "items": results[:2]
        }

    # 🔥 2. ROADMAP
    if intent == "roadmap":
        role = results[0]["role"]
        return {
            "type": "roadmap",
            "role": role,
            "steps": generate_roadmap(role)
        }

    # 🔥 3. SKILL GAP
    if intent == "skill_gap":
        return {
            "type": "skill_gap",
            "role": results[0]["role"],
            "missing_skills": ["Machine Learning", "Statistics"]
        }

    # 🔥 4. AGENT SUGGESTION
    if intent == "agent":
        return {
            "type": "agent",
            "suggestions": results
        }

    # 🔥 DEFAULT
    return {
        "type": "recommendation",
        "results": results
    }
