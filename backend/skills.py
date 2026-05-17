import json

with open("models/skills.json", "r") as f:
    SKILLS_DB = json.load(f)["skills"]

def extract_skills(text):

    found_skills = []

    for skill in SKILLS_DB:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return list(set(found_skills))