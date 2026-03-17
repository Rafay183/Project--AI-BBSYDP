import streamlit as st
from PIL import Image
import datetime

# --- Page Config ---
st.set_page_config(page_title="Rafay Shaikh ka Portfolio", page_icon="👨‍💻", layout="wide")

# --- Header Section ---
with st.container():
    st.title("👋 Hi, Main Hoon Rafay Shaikh")
    st.subheader("Ek Aspiring Data Scientist aur Python Developer")
    st.write("""
    Main data ki duniya mein naye-naye patterns dhundhne ka shaukeen hoon.
    Is sample portfolio ko Streamlit ki madad se banaya gaya hai. 
    Aap is code ko apni details se replace karke asli portfolio bana sakte ho!
    """)
    st.write("[LinkedIn Profile ->](https://www.linkedin.com/in/hellorafayshaikh/)") # Link wahi rahega

# --- About & Experience in Columns ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("📝 Thoda Mere Baare Mein")
        st.write("""
        - 👨‍🎓 **Background:** Maine [Aapni Degree] ki hai [University Name] se.
        - 💼 **Current:** Filhal main [Aapni Current Role] ki talash mein hoon / kar raha hoon.
        - 🎯 **Goals:** Data Science aur Machine Learning mein ek impact-full career banana chahta hoon.
        - ⚡ **Hobbies:** Kuch bhi naya seekhna, blogs padhna aur chai ke saath coding karna.
        """)
    with col2:
        st.header("💼 Tajurba (Experience)")
        st.write("""
        **Data Analyst Intern** (Sample Company Pvt Ltd)  
        *June 2023 - August 2023*  
        - Sample project mein Python ka use karke data clean kiya aur analysis kiya.
        - Streamlit ka use karke ek basic dashboard banaya.
        - Team ke saath milke client ki samasya samjhi aur solution propose kiya.
        
        **Freelance Web Scraper** (Fiverr/Upwork - Sample)  
        *2022 - 2023*  
        - BeautifulSoup aur Selenium se data scrape kiya.
        - Scraped data ko CSV aur Excel format mein convert kiya.
        """)

# --- Skills Section ---
with st.container():
    st.write("---")
    st.header("🛠️ Kya Kya Aata Hai? (Skills)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Languages:** Python, SQL, Basics of Java")
    with col2:
        st.write("**Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn")
    with col3:
        st.write("**Tools:** Streamlit, VS Code, Jupyter, Git")

# --- Projects Section ---
with st.container():
    st.write("---")
    st.header("🚀 Kuch Kaam (Projects)")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Project 1: Sample Data Dashboard")
        st.write("""
        Ek interactive dashboard jo Streamlit mein banaya gaya hai.
        Ismein CSV file upload karke real-time charts dekhe ja sakte hain.
        *(Yahan aur details daalni hain toh daal do)*
        """)
        st.caption("Tech: Streamlit, Pandas, Plotly")
    with col2:
        st.subheader("Project 2: Machine Learning Model")
        st.write("""
        Ek simple classification model jo Scikit-learn se banaya.
        Is model ko ek chhoti web app mein deploy kiya gaya hai.
        *(Yahan aur details daalni hain toh daal do)*
        """)
        st.caption("Tech: Python, Scikit-learn, Streamlit")

# --- Contact & Footer ---
with st.container():
    st.write("---")
    st.header("📬 Kahan Miloge Mujhe?")
    st.write("""
    Agar mere kaam mein interest hai toh contact kar sakte ho!
    - 📧 **Email:** [sample.email@domain.com](mailto:sample.email@domain.com) (Ise apna asli email karo)
    - 🔗 **LinkedIn:** [linkedin.com/in/hellorafayshaikh/](https://www.linkedin.com/in/hellorafayshaikh/)
    - 🐦 **Twitter/X:** [@samplehandle](https://twitter.com/samplehandle) (Agar hai toh)
    """)
    
    # Footer mein aaj ki date
    today = datetime.datetime.now().strftime("%Y")
    st.caption(f"© {today} Rafay Shaikh. Ye ek sample portfolio hai.")
