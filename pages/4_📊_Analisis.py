import streamlit as st
import pandas as pd

st.title("🎵 Análisis My music")

# ---------------- MOCK DE CANCIONES ----------------
canciones = [
    {"titulo": "Bohemian Rhapsody", "artista": "Queen", "duracion": 354, "popularidad": 98, "genero": "Rock"},
    {"titulo": "Billie Jean", "artista": "Michael Jackson", "duracion": 294, "popularidad": 95, "genero": "Pop"},
    {"titulo": "Sweet Child O' Mine", "artista": "Guns N' Roses", "duracion": 356, "popularidad": 93, "genero": "Rock"},
    {"titulo": "Imagine", "artista": "John Lennon", "duracion": 183, "popularidad": 92, "genero": "Pop"},
    {"titulo": "Hotel California", "artista": "Eagles", "duracion": 390, "popularidad": 90, "genero": "Rock"},
    {"titulo": "Smells Like Teen Spirit", "artista": "Nirvana", "duracion": 301, "popularidad": 94, "genero": "Grunge"},
    {"titulo": "Hey Jude", "artista": "The Beatles", "duracion": 431, "popularidad": 91, "genero": "Rock"},
    {"titulo": "Thriller", "artista": "Michael Jackson", "duracion": 358, "popularidad": 97, "genero": "Pop"},
]

df = pd.DataFrame(canciones)

# ---------------- POPULARIDAD ----------------
st.subheader("🔥 Popularidad de Canciones")
st.bar_chart(df.set_index("titulo")["popularidad"])

# ---------------- DURACIÓN ----------------
st.subheader("⏱ Evolución de Duración de Canciones")
st.line_chart(df.set_index("titulo")["duracion"])

# ---------------- COMBINADO ----------------
st.subheader("📈 Comparación Popularidad vs Duración")
st.area_chart(df.set_index("titulo")[["popularidad", "duracion"]])

# ---------------- DISTRIBUCIÓN POR GÉNERO ----------------
st.subheader("🎸 Distribución de Canciones por Género")
generos = df.groupby("genero").size().reset_index(name="cantidad")
st.dataframe(generos)
st.bar_chart(generos.set_index("genero"))

# ---------------- TOP ARTISTAS ----------------
st.subheader("👑 Popularidad Promedio por Artista")
top_artistas = df.groupby("artista")["popularidad"].mean().reset_index()
st.bar_chart(top_artistas.set_index("artista"))

# ---------------- MÉTRICAS DESTACADAS ----------------
st.subheader("🏆 Métricas Clave")
col1, col2, col3 = st.columns(3)

with col1:
    cancion_pop = df.loc[df["popularidad"].idxmax()]
    st.metric("Canción más popular", cancion_pop["titulo"], f"{int(cancion_pop['popularidad'])} pts")

with col2:
    cancion_larga = df.loc[df["duracion"].idxmax()]
    st.metric("Canción más larga", cancion_larga["titulo"], f"{int(cancion_larga['duracion'])} s")

with col3:
    artista_top = df["artista"].mode()[0]
    count_top = df["artista"].value_counts().max()
    st.metric("Artista con más canciones", artista_top, f"{count_top} canciones")
