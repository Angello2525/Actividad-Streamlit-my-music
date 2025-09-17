import streamlit as st

st.title("📚 Biblioteca")
st.write("Aquí puedes acceder a tus playlists favoritas, canciones guardadas y explorar por géneros.")

# ---------------- PLAYLISTS FAVORITAS ----------------
st.subheader("💿 Tus Playlists Favoritas")
playlists = {
    "🔥 Lo Mejor del Rock": "https://open.spotify.com/embed/playlist/37i9dQZF1DXcF6B6QPhFDv",
    "🎧 Chill Vibes": "https://open.spotify.com/embed/playlist/37i9dQZF1DX4WYpdgoIcn6",
    "🎉 Party Mix": "https://open.spotify.com/embed/playlist/37i9dQZF1DX0BcQWzuB7ZO",
}
cols = st.columns(len(playlists))
for i, (nombre, url) in enumerate(playlists.items()):
    with cols[i]:
        st.markdown(f"**{nombre}**")
        st.components.v1.iframe(url, height=200)

# ---------------- CANCIONES GUARDADAS ----------------
st.subheader("🎶 Canciones Guardadas")
canciones = [
    {"titulo": "Smells Like Teen Spirit", "artista": "Nirvana", "img": "https://i.scdn.co/image/ab67616d0000b273e175a19e530c898d167d39bf"},
    {"titulo": "Shape of You", "artista": "Ed Sheeran", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiljQVGwQLB0-QN3LWYmj7AqhD2oT4EAE7Mw&s"},
    {"titulo": "Imagine", "artista": "John Lennon", "img": "https://m.media-amazon.com/images/I/61EHasGroeL._UF1000,1000_QL80_.jpg"},
]
cols = st.columns(3)
for i, cancion in enumerate(canciones):
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

# ---------------- EXPLORA POR GÉNERO ----------------
st.subheader("🎵 Explorar por Género")
generos = {
    "🎸 Rock": [
        "https://open.spotify.com/embed/playlist/37i9dQZF1DWXRqgorJj26U",
        "https://open.spotify.com/embed/playlist/37i9dQZF1DXcF6B6QPhFDv"
    ],
    "🎤 Pop": [
        "https://open.spotify.com/embed/playlist/37i9dQZF1DWYmmr74INQlb",
        "https://open.spotify.com/embed/playlist/37i9dQZF1DX0AMssoUKCz7"
    ],
    "🎹 Electrónica": [
        "https://open.spotify.com/embed/playlist/37i9dQZF1DX4dyzvuaRJ0n",
        "https://open.spotify.com/embed/playlist/37i9dQZF1DX0BcQWzuB7ZO"
    ],
    "🎻 Clásica": [
        "https://open.spotify.com/embed/playlist/37i9dQZF1DWWEJlAGA9gs0",
        "https://open.spotify.com/embed/playlist/37i9dQZF1DX1s9knjP51Oa"
    ],
}

for genero, urls in generos.items():
    with st.expander(genero):
        cols = st.columns(len(urls))
        for i, url in enumerate(urls):
            with cols[i]:
                st.components.v1.iframe(url, height=250)

# ---------------- CSS ----------------
st.markdown(
    """
    <style>
    .hover-card {
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        border-radius: 12px;
        overflow: hidden;
        text-align: center;
        margin-bottom: 10px;
    }
    .hover-card img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 12px;
    }
    .hover-card:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 18px rgba(0,0,0,0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)
