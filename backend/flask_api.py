from flask import Flask, request, jsonify
from flask_cors import CORS

from backend.parser import extract_text_from_pdf
from backend.preprocessing import clean_text
from backend.skills import extract_skills
from backend.ats import calculate_ats_score
from backend.llm import get_ai_suggestions

import tempfile
import os

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():

    return {
        "message": "Resume Evaluator Flask API Running"
    }


@app.route("/analyze", methods=["POST"])
def analyze_resume():

    try:

        if "resume" not in request.files:

            return jsonify({
                "error": "Resume file missing"
            }), 400

        resume_file = request.files["resume"]

        jd_text = request.form.get(
            "job_description"
        )

        if not jd_text:

            return jsonify({
                "error": "Job description missing"
            }), 400

        # save temporary PDF

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            resume_file.save(
                temp_file.name
            )

            temp_path = temp_file.name

        # extract text

        with open(temp_path, "rb") as f:

            resume_text = extract_text_from_pdf(f)

        # delete temp file

        os.remove(temp_path)

        # clean text

        cleaned_resume = clean_text(
            resume_text
        )

        cleaned_jd = clean_text(
            jd_text
        )

        # extract skills

        resume_skills = extract_skills(
            cleaned_resume
        )

        jd_skills = extract_skills(
            cleaned_jd
        )

        # matched skills

        matched_skills = list(
            set(resume_skills).intersection(
                set(jd_skills)
            )
        )

        # missing skills

        missing_skills = list(
            set(jd_skills) - set(resume_skills)
        )

        # skill match %

        if len(jd_skills) > 0:

            skill_match_percentage = (
                len(matched_skills)
                / len(jd_skills)
            ) * 100

        else:

            skill_match_percentage = 0

        # ATS score

        ats_score = calculate_ats_score(
            cleaned_resume,
            cleaned_jd
        )

        # AI suggestions

        ai_suggestions = get_ai_suggestions(
            cleaned_resume,
            cleaned_jd
        )

        return jsonify({

            "ats_score": round(
                ats_score,
                2
            ),

            "skill_match_percentage": round(
                skill_match_percentage,
                2
            ),

            "resume_skills": resume_skills,

            "jd_skills": jd_skills,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "ai_suggestions": ai_suggestions
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )