import streamlit as st

st.set_page_config(page_title="GitHub Profile Generator")

st.title("GitHub Profile Generator")

# ---- Layout ----
left, right = st.columns(2)

# ---- Form Section ----
with left:
    with st.form("profile_form"):
        st.subheader("Fill your profile details")

        name = st.text_input("Your Name")
        bio = st.text_area("Short Bio")
        github_user = st.text_input("GitHub Username")

        skills_text = st.text_input(
            "Skills (comma-separated)",
            placeholder="Python, JavaScript, Streamlit"
        )

        # include_social 
        linkedin = st.text_input("LinkedIn URL (optional)")
        twitter = st.text_input("Twitter URL (optional)")

        submit = st.form_submit_button("Generate Profile")



# ---- Markdown Creation ----
if submit:
    # Process skills
    skills_list = [skill.strip() for skill in skills_text.split(",") if skill.strip()]

    # ---- Build README content ----
    md = ""
    if name:
        md += f"### Hi, I'm {name} 👋\n\n"
    else:
        md += f"### Hi 👋\n\n"

    if bio:
        md += f"## 👨‍💻 About Me\n{bio}\n\n"

    if skills_list:
        md += "## 🛠 Skills\n"
        for skill in skills_list:
            md += f"- {skill}\n"
        md += "\n"

    if github_user:
        md += f"## 🔗 GitHub\n[@{github_user}](https://github.com/{github_user})\n\n"

    # include_social:
    md += "## 🌍 Social Links\n"
    if linkedin:
        md += f"- [LinkedIn]({linkedin})\n"
    if twitter:
        md += f"- [Twitter]({twitter})\n"
    md += "\n"

    # ---- Preview Section ----
    with right:
        st.subheader("Generated Profile Preview")
        st.markdown(md)

        # ---- Download Button ----
        st.download_button(
            label="Download README.md",
            data=md,
            file_name="README.md",
            mime="text/markdown"
        )
