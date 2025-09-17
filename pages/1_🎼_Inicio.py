import streamlit as st

st.title("🎼 Inicio")
st.write("Descubre música adaptada a tu estado de ánimo y clásicos de siempre.")

# ---------------- MOOD ----------------
st.subheader("🎧 Música por Estado de Ánimo")
moods = {
    "😊 Feliz": "https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC",
    "😌 Relax": "https://open.spotify.com/embed/playlist/37i9dQZF1DWU0ScTcjJBdj",
    "🔥 Fiesta": "https://open.spotify.com/embed/playlist/37i9dQZF1DX0BcQWzuB7ZO",
}
cols = st.columns(len(moods))
for i, (mood, url) in enumerate(moods.items()):
    with cols[i]:
        st.markdown(f"**{mood}**")
        st.components.v1.iframe(url, height=200)

# ---------------- ESTILOS CSS ----------------
st.markdown(
    """
    <style>
    .hover-card {
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        border-radius: 12px;
        overflow: hidden;
        text-align: center;
        background: #111;
        color: white;
        padding: 6px;
    }
    .hover-card img {
        width: 100%;
        height: 220px;  /* tamaño fijo */
        object-fit: cover;  /* recorta la imagen sin deformarla */
        border-radius: 12px;
    }
    .hover-card:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 18px rgba(0,0,0,0.3);
    }
    .hover-card p {
        margin-top: 8px;
        font-size: 14px;
    }
    
    .artist-card, .album-card {
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        border-radius: 14px;
        overflow: hidden;
        background: linear-gradient(145deg, #1a1a1a, #2a2a2a);
        color: white;
        padding: 14px;
        margin-bottom: 20px;
    }
    .artist-card:hover, .album-card:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    }
    .artist-card img, .album-card img {
        border-radius: 12px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TOP CLÁSICOS ----------------
st.subheader("📊 Top 3 Clásicos del Momento")
top_clasicos = [
    {
        "titulo": "Bohemian Rhapsody",
        "artista": "Queen",
        "img": "https://i.scdn.co/image/ab67616d0000b2737c39dd133836c2c1c87e34d6"
    },
    {
        "titulo": "Billie Jean",
        "artista": "Michael Jackson",
        "img": "https://i.scdn.co/image/ab67616d00001e0286a14b2986ff774e8e6e3341"
    },
    {
        "titulo": "Sweet Child O' Mine",
        "artista": "Guns N' Roses",
        "img": "https://i.scdn.co/image/ab67616d0000b27321ebf49b3292c3f0f575f0f5"
    },
]
cols = st.columns(3)
for i, cancion in enumerate(top_clasicos):
    with cols[i]:
        st.markdown(
            f"""
            <div class="hover-card">
                <img src="{cancion['img']}" alt="{cancion['titulo']}">
                <p><b>{cancion['titulo']}</b><br>{cancion['artista']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- ARTISTA DESTACADO ----------------
st.subheader("🎤 Artista Destacado de la Semana")
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown(
        """
        <div class="artist-card">
            <img src="https://m.media-amazon.com/images/M/MV5BMjI4OTIwNDAxMF5BMl5BanBnXkFtZTgwOTkzOTAyODE@._V1_.jpg" width="250">
        </div>
        """,
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        """
        <div class="artist-card">
            Esta semana celebramos a <b>Queen</b>, una de las bandas más influyentes de la historia del rock.  
            Revive sus mejores éxitos en nuestra selección especial.
        </div>
        """,
        unsafe_allow_html=True
    )
# ---------------- ÁLBUM RECOMENDADO ----------------
st.subheader("📀 Álbum Recomendado")
col1, col2 = st.columns([1, 1.5])
with col1:
    st.markdown(
        """
        <div class="album-card">
            <img src="https://i.scdn.co/image/ab67616d0000b273ba5db46f4b838ef6027e6f96" width="180">
        </div>
        """,
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        """
        <div class="album-card">
            <b>Divide - Ed Sheeran (2017)</b><br>
            Un álbum que mezcla pop y baladas modernas, con éxitos como <i>Shape of You</i> y <i>Perfect</i>.<br><br>
            <a href="https://open.spotify.com/album/3T4tUhGYeRNVUGevb0wThu" target="_blank">🎧 Escuchar en Spotify</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- RANKING EXTRA ----------------
st.subheader("📈 Ranking Clásicos Top 5")
ranking = [
    "1. Hotel California - Eagles",
    "2. Stairway to Heaven - Led Zeppelin",
    "3. Imagine - John Lennon",
    "4. Smells Like Teen Spirit - Nirvana",
    "5. Hey Jude - The Beatles"
]
for r in ranking:
    st.markdown(f"- {r}")

# ---------------- NOTICIAS ----------------
st.subheader("📰 Noticias Musicales")
noticias = [
    "🎶 Queen revive con una reedición especial de *Bohemian Rhapsody*.",
    "🎸 Guns N' Roses anuncia gira mundial con todos sus clásicos.",
    "🕺 Tributo a Michael Jackson reúne a miles de fans alrededor del mundo."
]
for n in noticias:
    st.markdown(f"- {n}")
