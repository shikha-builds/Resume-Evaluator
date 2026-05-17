import matplotlib.pyplot as plt

from matplotlib_venn import venn2

def generate_venn(
    resume_skills,
    jd_skills
):

    resume_set = set(
        resume_skills
    )

    jd_set = set(
        jd_skills
    )

    fig, ax = plt.subplots(
        figsize=(4, 4)
    )

    venn2(
        subsets=(
            resume_set,
            jd_set
        ),
        set_labels=(
            "Resume Skills",
            "JD Skills"
        ),
        ax=ax
    )

    plt.tight_layout()

    return fig