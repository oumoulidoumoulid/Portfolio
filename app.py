import streamlit as st
import base64
from PIL import Image

def main():
    st.set_page_config(page_title="Portfolio Lahcen OUMOULID", page_icon="🚀", layout="wide")

    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Sections", [
        "Accueil", 
        "À Propos", 
        "Compétences", 
        "Projets", 
        "Stages", 
        "Formation", 
        "Expériences", 
        "Intérêts", 
        "Contact"
    ])

    # Charger la photo de profil
    profile_photo = Image.open("photo.jpg")

    # Page d'Accueil
    if page == "Accueil":
        st.title("👋 Bonjour, Je suis LAHCEN OUMOULID")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(profile_photo, width=300)
        
        with col2:
            st.markdown("""
            ## Ingénieur en Procédés Chimiques
            
            - 🔬 Spécialisation : Ingénierie des Procédés
            - 💡 Passionné par l'optimisation des processus industriels
            - 🚀 Innovant et orienté solutions
            """)
        
        st.markdown("---")
        
        # Statistiques clés
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Projets", "4+")
        
        with col2:
            st.metric("Stages", "3")
        
        with col3:
            st.metric("Compétences Techniques", "10+")

    # Section À Propos
    elif page == "À Propos":
        st.header("🧑‍💼 Profil Professionnel")
        st.write("""
        Je suis Lahcen Oumoulid, un étudiant ingénieur spécialisé en Ingénierie des Procédés. 
        Mon parcours est marqué par une expertise pratique en transformation des minéraux et fabrication de plastiques.

        🔍 Mes points forts :
        - Optimisation des processus
        - Conduite de machines industrielles
        - Amélioration de l'efficacité de production
        - Résolution de problèmes complexes
        - Travail d'équipe efficace
        """)

    # Section Compétences
    elif page == "Compétences":
        st.header("🛠 Compétences Techniques")
        
        skills = {
            "Logiciels": {
                "Aspen Plus": 30,
                "Matlab": 50,
                "Maple": 50,
                "SolidWorks": 40
            },
            "Informatiques": {
                "SQL Server": 80,
                "Excel": 80,
                "PowerPoint": 90,
                "Word": 90
            }
        }
        
        for category, skills_list in skills.items():
            st.subheader(f"{category}")
            for skill, level in skills_list.items():
                st.progress(level)
                st.write(f"{skill} : {level}%")

    # [Continuer avec les autres sections similairement]

    # Section Contact
    elif page == "Contact":
        st.header("📧 Contactez-moi")
        
        with st.form(key='contact_form'):
            name = st.text_input("Nom")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submit_button = st.form_submit_button(label='Envoyer')

if __name__ == "__main__":
    main()
