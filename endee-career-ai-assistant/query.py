from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Load data
with open("data/careers.txt", "r") as f:
    docs = f.readlines()

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(docs)


# 🔹 Format structured response
def format_response(text):
    parts = text.split(".")

    return {
        "role": parts[0].strip(),
        "skills": parts[1].strip() if len(parts) > 1 else "",
        "description": parts[2].strip() if len(parts) > 2 else ""
    }


# 🔹 Roadmap generator
def generate_roadmap(role):
    roadmap = {
        "Data Analyst": [
            "Learn Excel & SQL",
            "Learn Python (Pandas, NumPy)",
            "Data Visualization (Power BI/Tableau)",
            "Build projects",
            "Apply for internships"
        ],
        "Data Scientist": [
            "Learn Python",
            "Statistics & Probability",
            "Machine Learning",
            "Deep Learning",
            "Build ML projects"
        ],
        "Frontend Developer": [
            "Learn HTML, CSS",
            "JavaScript fundamentals",
            "React.js",
            "Build portfolio projects",
            "Deploy websites"
        ],
        "Backend Developer": [
            "Learn Node.js / Python",
            "Database (SQL/NoSQL)",
            "Build APIs",
            "Authentication & security",
            "Deploy backend"
        ]
    }

    return roadmap.get(role, ["Start with basics", "Build projects", "Practice daily"])


# 🔹 Intent detection
def detect_intent(query):
    q = query.lower()

    if "roadmap" in q or "how to become" in q:
        return "roadmap"
    elif "suggest" in q or "recommend" in q:
        return "recommend"
    else:
        return "search"


# 🔹 Main AI function (UPGRADED)
def search(query):
    intent = detect_intent(query)

    # 🔥 HANDLE GREETINGS
    greetings = ["hi", "hello", "hlo", "hey"]
    if query.lower().strip() in greetings:
        return {
            "type": "message",
            "text": "Hello 👋 Ask me about careers, skills, or roadmaps!"
        }

    query_vec = vectorizer.transform([query])
    similarity = (vectors * query_vec.T).toarray().flatten()

    # sort all results
    sorted_indices = similarity.argsort()[::-1]

    results = []

    for i in sorted_indices:
        score = round(similarity[i] * 100, 2)

        # 🔥 FILTER LOW QUALITY RESULTS
        if score < 10:
            continue

        formatted = format_response(docs[i])

        results.append({
            "role": formatted["role"],
            "skills": formatted["skills"],
            "description": formatted["description"],
            "score": score
        })

        # limit to top 3 GOOD matches
        if len(results) == 3:
            break

    # 🔥 NO MATCH CASE
    if len(results) == 0:
        return {
            "type": "message",
            "text": "⚠️ I couldn't find a strong match. Try asking like 'skills for data analyst' or 'how to become data scientist'."
        }

    # 🔥 ROADMAP RESPONSE
    if intent == "roadmap":
        main_role = results[0]["role"]
        return {
            "type": "roadmap",
            "role": main_role,
            "steps": generate_roadmap(main_role)
        }

    # 🔥 NORMAL RECOMMENDATION
    return {
        "type": "recommendation",
        "results": results
    }
