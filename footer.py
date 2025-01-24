import streamlit as st

def display_footer():
    st.write("---")
    st.markdown(
        """
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
        <style>
            footer {
                text-align: center;
                font-size: 0.9em;
                color: #95a5a6;
                margin-top: 30px;
            }
            footer a {
                color: #3498db;
                text-decoration: none;
                margin: 0 10px;
                font-size: 1.2em;
            }
            footer a:hover {
                color: #2ecc71;
            }
        </style>
        <footer>
            EcoTrackify © 2025<br>
            Connect with us: 
            <a href="https://github.com/Hanzllasoomro" target="_blank" title="GitHub">
                <i class="fab fa-github"></i>
            </a>
            <a href="https://www.instagram.com/hanzllasoomro/#" target="_blank" title="Instagram">
                <i class="fab fa-instagram"></i>
            </a>
            <a href="https://www.linkedin.com/in/hanzlla-soomro-85a258211/" target="_blank" title="LinkedIn">
                <i class="fab fa-linkedin"></i>
            </a>
        </footer>
        """,
        unsafe_allow_html=True,
    )

