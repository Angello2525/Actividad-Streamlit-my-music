import streamlit as st

st.set_page_config(page_title="My music", page_icon="🎵", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎶 Menú de Navegación")
opcion = st.sidebar.radio(
    "Ir a:",
    ("Inicio", "Biblioteca", "Recomendaciones", "Configuración")
)

# ---------------- INICIO ----------------
if opcion == "Inicio":
    st.title("🎼 Bienvenido a my music")
    st.write("Explora canciones, artistas y playlists sin necesidad de iniciar sesión.")

    # Playlist de Spotify (Embed)
    st.subheader("🔥 Mi Playlist de Spotify")
    playlist_url = "https://open.spotify.com/playlist/4qKjvUxavdbzy3mJZjyHiG"
    st.components.v1.iframe(
        f"https://open.spotify.com/embed/playlist/{playlist_url.split('/')[-1]}",
        height=400
    )

    # Canciones destacadas
    st.subheader("✨ Canciones Destacadas")
    canciones = [
        {
            "titulo": "Que Le Pasa A Lupita",
            "artista": "Fruko & Sus Tesos",
            "img": "https://i.ytimg.com/vi/v5FbyKCSEAE/maxresdefault.jpg"
        },
        {
            "titulo": "Rich Girl",
            "artista": "Gwen Stefani",
            "img": "https://cdn-images.dzcdn.net/images/cover/0dbe967d19dcf74cf7e2ad7e5c350bc4/500x500.jpg"
        },
        {
            "titulo": "Men in Black",
            "artista": "Will Smith",
            "img": "https://i.scdn.co/image/ab67616d0000b273ddf2f9edabd166c60047e3c4"
        },
        {
            "titulo": "Maniac",
            "artista": "Michael Sembello",
            "img": "https://i.ytimg.com/vi/6GCNUeTFSbA/maxresdefault.jpg"
        },
        {
            "titulo": "You Should Be Dancing",
            "artista": "Bee Gees",
            "img": "https://i.scdn.co/image/ab67616d0000b27345b4e9481e0846c16553a048"
        },
        {
            "titulo": "Conteo regresivo - Salsa Version",
            "artista": "Gilberto Santa Rosa",
            "img": "https://i.scdn.co/image/ab67616d00001e0207031a0d94b5340aeb77e824"
        },
    ]

    # CSS para tarjetas con borde
    st.markdown(
        """
        <style>
        .card {
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            cursor: pointer;
            border: 1px solid #ddd;
            border-radius: 12px;
            padding: 10px;
            background-color: #313131FF;
        }
        .card:hover {
            transform: scale(1.05);
            box-shadow: 0px 4px 15px rgba(0,0,0,0.25);
        }
        .card img {
            border-radius: 8px;
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .card p {
            margin-top: 8px;
            font-size: 14px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(3)
    for i, c in enumerate(canciones):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="card" style="text-align:center; margin-bottom:20px;">
                    <img src="{c['img']}">
                    <p><b>{c['titulo']}</b><br>{c['artista']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------- BIBLIOTECA ----------------
elif opcion == "Biblioteca":
    st.title("📂 Tu Biblioteca")
    st.write("Aquí aparecerán tus canciones guardadas (sección en construcción).")

# ---------------- RECOMENDACIONES ----------------
elif opcion == "Recomendaciones":
    st.title("✨ Recomendaciones")
    st.write("Canciones y playlists sugeridas para ti (mock de ejemplo).")

    recs = [
        "🎵 Canción Chill para trabajar",
        "🔥 Playlist de Reguetón 2024",
        "🎸 Rock Clásico",
        "🎹 Lo-Fi Beats"
    ]

    for r in recs:
        st.markdown(f"- {r}")

# ---------------- CONFIGURACIÓN ----------------
elif opcion == "Configuración":
    st.title("⚙️ Configuración")
    st.write("Ajusta tus preferencias aquí.")
    tema = st.selectbox("Elige un tema de color:", ["Claro", "Oscuro", "Automático"])
    st.write(f"Seleccionaste el tema: {tema}")
