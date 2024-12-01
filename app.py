import streamlit as st

def main():
    st.set_page_config(page_title="CV LAHCEN OUMOULID", page_icon=":briefcase:")

    # En-tête
    st.title("CV de LAHCEN OUMOULID")
    st.subheader("Ingénieur en Procédés Chimiques")

    # Section À propos
    st.header("À propos")
    st.write("""
    Je suis Lahcen Oumoulid, un étudiant en ingénierie spécialisé en Ingénierie des Procédés. 
    Avec une expérience pratique dans le traitement des minéraux et la fabrication de plastiques, 
    j'ai développé des compétences en optimisation des procédés, conduite de machines et efficacité de production. 
    Mes stages ont affiné mes capacités de résolution de problèmes et de travail d'équipe, 
    et je suis toujours désireux d'apprendre et d'innover.
    """)

    # Compétences techniques
    st.header("Compétences Techniques")
    skills = {
        "Aspen Plus": 30,
        "Matlab": 50,
        "Maple": 50,
        "SolidWorks": 40,
        "SQL Server": 80,
        "Excel": 80,
        "PowerPoint": 90,
        "Word": 90
    }
    
    for skill, level in skills.items():
        st.progress(level)
        st.write(f"{skill}: {level}%")

    # Projets
    st.header("Projets")
    projets = [
        "Développement de programmes de différences finies et éléments finis(1D,2D)",
        "Développement web: conception d'un site de production et vente",
        "Projet de Simulation de Distillation Binaire",
        "Développement d'une Application pour une Clinique Dentaire",
        "Simulation numérique pour l'optimisation du transfert de matière"
    ]
    
    for projet in projets:
        st.write(f"- {projet}")

    # Stages
    st.header("Stages")
    stages = [
        {
            "entreprise": "Eljanoub Plastique, Marrakech",
            "periode": "15/07/2022 - 15/08/2022",
            "description": "Stage d'observation en opérations de production"
        },
        {
            "entreprise": "OCP Group, Gantour Division",
            "periode": "03/04/2023 - 30/05/2023",
            "description": "Optimisation des processus de flottation"
        }
    ]
    
    for stage in stages:
        st.write(f"**{stage['entreprise']}**")
        st.write(f"Période: {stage['periode']}")
        st.write(f"Description: {stage['description']}")

    # Formations
    st.header("Formations")
    formations = [
        {
            "etablissement": "Faculté des Sciences et Techniques, Settat",
            "diplome": "Procédés et Ingénierie Chimique",
            "annee": "2024 - Présent"
        },
        {
            "etablissement": "École Supérieure de Technologie, Beni Mellal",
            "diplome": "Génie des Procédés",
            "annee": "2022 - 2023"
        }
    ]
    
    for formation in formations:
        st.write(f"**{formation['etablissement']}**")
        st.write(f"Diplôme: {formation['diplome']}")
        st.write(f"Année: {formation['annee']}")

    # Intérêts
    st.header("Centres d'Intérêt")
    interets = ["Photographie", "Voyage", "Escalade", "Natation", "Course à pied", "Cyclisme"]
    st.write(", ".join(interets))

    # Contact
    st.header("Contact")
    with st.form(key='contact_form'):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label='Envoyer')
        
        if submit_button:
            st.success("Message envoyé avec succès!")

if __name__ == "__main__":
    main()