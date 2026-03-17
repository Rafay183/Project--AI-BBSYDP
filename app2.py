import streamlit as st
from PIL import Image
import datetime

# Page configuration
st.set_page_config(
    page_title="Rafay Shaikh | Data Professional",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #0A66C2;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-top: 0;
    }
    .section-title {
        font-size: 2rem;
        color: #0A66C2;
        border-bottom: 2px solid #0A66C2;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .skill-tag {
        background-color: #e6f3ff;
        color: #0A66C2;
        padding: 5px 15px;
        border-radius: 20px;
        display: inline-block;
        margin: 5px;
        font-weight: 500;
    }
    .project-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 4px solid #0A66C2;
    }
    .contact-info {
        text-align: center;
        padding: 20px;
        background-color: #f0f2f5;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="main-header">👨‍💻 Rafay Shaikh</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Data Enthusiast | Python Developer | Problem Solver</p>', unsafe_allow_html=True)

# Profile Summary
with st.container():
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("""
        🎯 Passionate about transforming raw data into actionable insights. 
        Currently exploring the vast possibilities of Data Science and Machine Learning.
        Always eager to learn new technologies and solve real-world problems.
        """)

# About Section
with st.container():
    st.markdown('<h2 class="section-title">📋 About Me</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🎓 Education**
        - **Bachelor's in Computer Science** (Expected 2025)
          *University of Mumbai*
          - CGPA: 8.5/10
          - Relevant coursework: Data Structures, DBMS, Machine Learning
        
        **📜 Certifications**
        - Google Data Analytics Professional Certificate
        - Python for Data Science (IBM)
        - SQL Advanced Certification (HackerRank)
        """)
    
    with col2:
        st.markdown("""
        **💼 Experience**
        
        **Data Analyst Intern** | *Tech Solutions Pvt Ltd*
        *Jan 2024 - Present*
        - Analyzing customer behavior data to improve business strategies
        - Creating interactive dashboards using Streamlit and Plotly
        - Collaborating with cross-functional teams on data projects
        
        **Freelance Python Developer** | *Upwork*
        *2023 - 2024*
        - Developed web scraping solutions for 5+ clients
        - Automated data extraction and processing tasks
        - Built custom data analysis tools using Python
        """)

# Skills Section
with st.container():
    st.markdown('<h2 class="section-title">🛠️ Technical Skills</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Programming Languages**")
        skills1 = ["Python", "SQL", "JavaScript", "R (Basic)"]
        for skill in skills1:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown("**Data Science Stack**")
        skills2 = ["Pandas", "NumPy", "Scikit-learn", "Matplotlib", "Seaborn", "Plotly"]
        for skill in skills2:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("**Web Technologies**")
        skills3 = ["Streamlit", "Flask", "HTML/CSS", "REST APIs"]
        for skill in skills3:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown("**Tools & Platforms**")
        skills4 = ["Git/GitHub", "VS Code", "Jupyter", "MySQL", "PostgreSQL", "Tableau"]
        for skill in skills4:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

# Projects Section
with st.container():
    st.markdown('<h2 class="section-title">🚀 Featured Projects</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.markdown("### 📊 Sales Analytics Dashboard")
            st.markdown("""
            Interactive dashboard for sales team to track KPIs and performance metrics.
            - Real-time data visualization with filters
            - Automated report generation
            - 40% reduction in manual reporting time
            """)
            st.markdown("**Tech Stack:** Python, Streamlit, Pandas, Plotly")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.markdown("### 🤖 Customer Churn Prediction")
            st.markdown("""
            ML model to predict customer churn for telecom company.
            - 85% accuracy using Random Forest
            - Feature importance analysis
            - Deployed as web application
            """)
            st.markdown("**Tech Stack:** Scikit-learn, Pandas, Flask, HTML/CSS")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.markdown("### 🕸️ Web Scraper Tool")
            st.markdown("""
            Custom web scraper for e-commerce price monitoring.
            - Scheduled scraping at regular intervals
            - Price change alerts via email
            - Data export in multiple formats
            """)
            st.markdown("**Tech Stack:** Python, BeautifulSoup, Selenium, SQLite")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.markdown("### 📈 Stock Market Analysis")
            st.markdown("""
            Real-time stock analysis and visualization tool.
            - Live data from Yahoo Finance API
            - Technical indicators calculation
            - Portfolio tracking feature
            """)
            st.markdown("**Tech Stack:** Python, yfinance, Streamlit, Plotly")
            st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
with st.container():
    st.markdown('<h2 class="section-title">📫 Let\'s Connect</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="contact-info">', unsafe_allow_html=True)
        st.markdown("""
        📧 **Email:** [rafay.shaikh@email.com](mailto:rafay.shaikh@email.com)  
        🔗 **LinkedIn:** [linkedin.com/in/hellorafayshaikh/](https://www.linkedin.com/in/hellorafayshaikh/)  
        🐦 **Twitter:** [@rafay_shaikh](https://twitter.com/rafay_shaikh)  
        💻 **GitHub:** [github.com/rafayshaikh](https://github.com/rafayshaikh)
        
        🌟 **Open for:** Data Analyst roles, Internships, and Collaboration
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col2:
    current_year = datetime.datetime.now().year
    st.markdown(f"<p style='text-align: center; color: #666;'>© {current_year} Rafay Shaikh. Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)