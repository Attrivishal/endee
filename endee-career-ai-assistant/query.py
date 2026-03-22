from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

with open("data/careers.txt", "r") as f:
    docs = f.readlines()

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(docs)

def search(query):
    query_vec = vectorizer.transform([query])
    similarity = (vectors * query_vec.T).toarray()
    best_index = np.argmax(similarity)
    return docs[best_index]

if __name__ == "__main__":
    q = input("Ask your career question: ")
    result = search(q)
    print("Answer:", result)
