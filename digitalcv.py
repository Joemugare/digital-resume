import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def main():
    # Page Configuration
    st.set_page_config(page_title="Digital Resume", page_icon="📄")

    # Header with Photo
    st.title("Joseph Mugare Digital Resume")
    st.subheader("Fullstack Developer")
    
    # Display PNG pic using st.image

    badge1 = Image.open("mugare.png")  # Replace with the actual path to your badge PNG files

    
    # Display badges using st.image
    st.image(badge1, caption="Badge 1 (PNG)", use_column_width=False, width=200)

    # Contact Information
    st.header("Contact Information")
    st.markdown("📧 Email: joemugare@gmail.com")
    st.markdown("📞 Phone: +254720957180")
    st.markdown("🌐 LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/joseph-mugare/)")
    st.markdown("📁 GitHub: [GitHub Profile](https://github.com/joemugare)")
    st.markdown("📺 YouTube: [YouTube Channel](https://www.youtube.com/user/joemugare)")

   # Education
    st.header("Education")

    # Bachelor's Degree
    st.markdown("Bachelor In Information Technology, KCA UNIVERSITY")
    st.markdown("J A N  2009 - D E C E M B ER  2011")

    # Additional Certifications
    st.markdown("CCNA, ZETECH")
    st.markdown("MYSQL, EDX STANFORD")
    st.markdown("FEB 2023 — July 2023")

    st.markdown("Python Data Science, EDX HARVARD")
    st.markdown("January 2023 — June 2023")

    # Work Experience
    st.header("Work Experience")
    st.subheader("Fullstack Developer at BIO HAZARD NBO")
    st.write("Jan 2021 - Present")
    st.write("Developed and maintained web applications.")
    st.write("Collaborated with cross-functional teams to deliver projects.")

    # Skills
    st.header("Skills")
    st.write("Programming Languages: Python, JavaScript")
    st.write("Cloud Computing: AWS")
    st.write("Databases: MySQL, MongoDB")
    st.write("Version Control: Git")

    # Projects
    st.header("Projects")
    st.subheader("E-commerce Website")
    st.write("Developed a full-stack e-commerce website using React and Node.js.")
    st.subheader("Portfolio Website")
    st.write("Created a personal portfolio website using HTML, CSS, and JavaScript")

    # Badges
    st.header("Badges")

     # Display PNG badges horizontally
    badge_paths = ["aws-cloud-quest-data-analytics.png", "aws-cloud-quest-solutions-architect.png", "google analytic cert.png"]  # Replace with the actual paths to your badge PNG files

    badge_images = [Image.open(path) for path in badge_paths]

    # Create a horizontal layout for badges using st.columns
    badge_columns = st.columns(len(badge_images))
    for i, badge_image in enumerate(badge_images):
        with badge_columns[i]:
            st.image(badge_image, caption=f"Badge {i + 1} (PNG)", use_column_width=False, width=200)

    # Skills Proficiency Bar Chart
    st.header("Skills Proficiency")
    
    skills = ["Python", "JavaScript", "Data Analysis", "Machine Learning", "SQL"]
    proficiency = [90, 80, 85, 75, 90]

    # Create a bar chart using Matplotlib
    fig, ax = plt.subplots()
    ax.bar(skills, proficiency)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    st.pyplot(fig)
    
    # Downloadable PDF
    st.header("Downloadable PDF")
    
    # Generate the PDF content
    pdf_filename = "digital_resume.pdf"

    def generate_pdf():
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.setFont("Helvetica", 12)
        
        # Write your CV content here
        c.drawString(100, 700, "Digital Resume")
        c.drawString(100, 680, "Joseph Mugare")
        c.drawString(100, 660, "Software Engineer")
        # ... add more content as needed

        c.showPage()
        c.save()

    # Create a download button
    if st.button("Download PDF"):
        generate_pdf()
        with open(pdf_filename, "rb") as pdf_file:
            st.success("Download your PDF [here](data:application/pdf;base64,%s)" % pdf_file.read().encode("base64").decode())

if __name__ == '__main__':
    main()
