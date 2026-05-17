import streamlit as st

from backend.parser import extract_text_from_pdf
from backend.preprocessing import clean_text
from backend.skills import extract_skills
from backend.ats import calculate_ats_score
from backend.llm import get_ai_suggestions
from backend.venn import generate_venn

# page configuration

st.set_page_config(
    page_title="Resume Evaluator",
    page_icon="📄",
    layout="centered"
)

# customized CSS
st.markdown(
    """
    <style>

    .block-container {

        max-width: 850px;

        padding-top: 2rem;

        padding-bottom: 2rem;
    }

    h1, h2, h3 {

        text-align: center;
    }

    .stButton > button {

        width: 100%;

        border-radius: 10px;

        height: 3em;

        font-size: 18px;

        font-weight: bold;
    }

    [data-testid="stMetric"] {

        text-align: center;

        border: 1px solid #e6e6e6;

        border-radius: 12px;

        padding: 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# page title
st.title("📄 Resume Evaluator")

st.markdown(
    """
    <div style='text-align:center; font-size:18px;'>

    AI-Powered Resume Analyzer

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# user inputs
uploaded_file = st.file_uploader(
    "Upload Resume (PDF Only)",
    type=["pdf"]
)

jd_text = st.text_area(
    "Paste Job Description",
    height=220
)

# buttons
if st.button("🚀 Evaluate Resume"):

    if uploaded_file and jd_text:

        try:

            with st.spinner(
                "Analyzing Resume..."
            ):                  
                
                # extract text
                resume_text = extract_text_from_pdf(
                    uploaded_file
                )
                                
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

                # skills matched %
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

            st.markdown("---")
            
            # ATS score
            st.subheader("1️⃣ ATS Score")

            st.metric(
                label="",
                value=f"{round(ats_score, 2)}%"
            )

            st.markdown("<br>", unsafe_allow_html=True)
 
            # venn diagram
            st.subheader("2️⃣ Venn Diagram")

            col1, col2, col3 = st.columns([1,2,1])

            with col2:

                fig = generate_venn(
                    resume_skills,
                    jd_skills
                )

                st.pyplot(
                    fig,
                    width="content"
                )

            st.markdown(
                """
                <div style='text-align:center;'>

                Left-side: Resume-only Skills<br>

                Intersection: Matched Skills<br>

                Right-side: Job Description Requirements

                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("<br>", unsafe_allow_html=True)

            # skills match
            st.subheader(
                "3️⃣ Percentage of Skills Matched"
            )

            st.metric(
                label="",
                value=f"{round(skill_match_percentage, 2)}%"
            )

            st.markdown("<br>", unsafe_allow_html=True)

            # missing skills
            st.subheader("4️⃣ Missing Skills")

            if len(missing_skills) == 0:

                st.success(
                    "No Missing Skills Found"
                )

            else:

                for skill in missing_skills:

                    st.write(
                        f"❌ {skill}"
                    )

            st.markdown("<br>", unsafe_allow_html=True)

            # AI suggestions
            st.subheader("5️⃣ AI Suggestions")

            st.write(
                ai_suggestions
            )

        except Exception as e:

            st.error(str(e))

    else:

        st.warning(
            "Please upload resume and paste job description."
        )