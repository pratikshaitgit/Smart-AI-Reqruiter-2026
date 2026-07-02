import os 
os.environ["OPENBLAS_NUM_THREADS"] = "1"

from sentence_transformers import SentenceTransformer, util

import json

# Load candidates
candidates = []
with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidates.append(json.loads(line))

# Load job description
with open("data/job_description.txt", "r", encoding="utf-8") as f:
    job_desc = f.read()

print("Total Candidates:", len(candidates))
#print("\nJob Description Preview:\n", job_desc[:100])
print("\n--- Candidate Matching ---\n")


keywords = ["python", "sql", "spark", "nlp", "machine learning", "aws", "deep learning", "flask", "django", "data engineering", 
            "numpy", "pandas", "pytorch", "hadoop", "airflow", "tensorflow", "kafka", "llm", "transformers", "ai"]

#model = SentenceTransformer('all-miniLM-L6-v2')

job_desc_lower = job_desc.lower()
required_skills = []
#jd_embedding = model.encode(job_desc, convert_to_tensor=True)

for kw in keywords:
    if kw in job_desc_lower:
        required_skills.append(kw)

print("\nExtracted Skills from JD:", required_skills)
print("\nFull JD:\n", job_desc)


results = []

for c in candidates:
    name = c["profile"]["anonymized_name"]
    skills = [s["name"].lower() for s in c["skills"]]

    score = 0

    experience = c.get("experience", 0)

    if experience >= 3:
        score += 3
    elif experience >= 1:
        score += 1
    reasons = []

    matched = set()

    for skill in skills:
        for req in required_skills:
            if req == skill and req not in matched:
                score += 5
                reasons.append(f"{req} (exact)")
                matched.add(req)
            elif req in skill and abs(len(skill)-len(req)) <= 3 and req not in matched:
                score += 2
                reasons.append(f"{req} (partial)")
                matched.add(req)

    #PROJECTS SCORING
    projects = c.get("projects", [])

    for project in projects:
        project_text = project.lower()

        for req in required_skills:
            if req in project_text:
                score += 3
                reasons.append(f"{req} (project)")
                break


    education_list = c.get("education", [])

    education = " ".join(
    " ".join(str(v) for v in edu.values()) if isinstance(edu, dict) else str(edu)
    for edu in education_list).lower()

    if "computer" in education or "ai" in education:
        score += 2
        reasons.append("relevant education")

    #   (AI ROLE BOOST)

    candidate_text = ""

    # skills
    candidate_text += " ".join([s["name"] for s in c["skills"]]) + " "

    # projects
    candidate_text += " ".join(c.get("projects", [])) + " "

    # education
    candidate_text += education + " "

    # convert to embedding
    """candidate_embedding = model.encode(candidate_text, convert_to_tensor=True)

    # similarity
    similarity = util.cos_sim(jd_embedding, candidate_embedding).item()

    # add to score
    ai_score = round(similarity * 10, 2)
    score += ai_score

    reasons.append(f"AI match: {ai_score}")"""

    if "ai" in required_skills or "ml" in required_skills:
        if "tensorflow" in skills or "pytorch" in skills:
            score += 2
            reasons.append("ai framework bonus")
    
    results.append((name, score, reasons))


print("\nTop Candidates:\n")

# sort results properly
results_sorted = sorted(results, key=lambda x: x[1], reverse=True)

for name, score, reasons in results_sorted[:5]:
    print(f"{name} → Score: {round(score,2)}")
    
    print("Reasons:")
    for r in reasons:
        print(" -", r)
    
    print("-" * 40)

print("\nPROGRAM FINISHED")