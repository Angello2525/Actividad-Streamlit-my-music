import streamlit as st

st.title("⭐ Recomendaciones para Ti")
st.write("Basadas en tus gustos, historial y tendencias actuales 🎧")

# ---------------- DESTACADOS ----------------
st.subheader("🔥 Destacados de la Semana")
cols = st.columns(3)
destacados = [
    {"titulo": "Indie Essentials", "img": "https://image-cdn-fa.spotifycdn.com/image/ab67706c0000da84b44cb379853c9598e9a840bd", "url": "https://open.spotify.com/embed/playlist/37i9dQZF1DX2Nc3B70tvx0"},
    {"titulo": "Top Global", "img": "https://charts-images.scdn.co/assets/locale_en/regional/daily/region_global_default.jpg", "url": "https://open.spotify.com/embed/playlist/37i9dQZEVXbMDoHDwVN2tF"},
    {"titulo": "Rap Latino", "img": "https://image-cdn-ak.spotifycdn.com/image/ab67706c0000da84afe242b3207e80cf7c24b853", "url": "https://open.spotify.com/embed/playlist/37i9dQZF1DX186v583rmzp"},
]
for i, d in enumerate(destacados):
    with cols[i]:
        st.image(d["img"], use_container_width=True)
        st.markdown(f"**{d['titulo']}**")
        st.components.v1.iframe(d["url"], height=200)

# ---------------- BASADO EN TI ----------------
st.subheader("🎵 Basado en lo que escuchas")
recs = [
    {"titulo": "Descubrimiento Semanal", "url": "https://open.spotify.com/embed/playlist/37i9dQZF1DWXRqgorJj26U"},
    {"titulo": "Daily Mix 1", "url": "https://open.spotify.com/embed/playlist/37i9dQZF1DX4dyzvuaRJ0n"},
    {"titulo": "Daily Mix 2", "url": "https://open.spotify.com/embed/playlist/37i9dQZF1DX1s9knjP51Oa"},
]
cols = st.columns(3)
for i, r in enumerate(recs):
    with cols[i]:
        st.markdown(f"**{r['titulo']}**")
        st.components.v1.iframe(r["url"], height=200)

# ---------------- ARTISTAS SIMILARES ----------------
st.subheader("👥 Artistas que te podrían gustar")
artistas = [
    {"nombre": "Tame Impala", "img": "https://m.media-amazon.com/images/M/MV5BNjYyMWRmNmQtZjFlYi00MmU5LTg5NjQtMTI1YjIxMmMzN2IzXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"},
    {"nombre": "Arctic Monkeys", "img": "https://imagenes.elpais.com/resizer/v2/LQD3CWJLDE3DCQSRWHUQDD2RW4.jpg?auth=d3d0c73cd4a60b908937471df10dd979e4667ae5b06f5dee54c656ea74d5532a&width=1960&height=1103&smart=true"},
    {"nombre": "The Strokes", "img": "https://i.guim.co.uk/img/media/d1ecdacdbb470243fc248a5b38bc521de6aae4e0/52_84_2430_1457/master/2430.jpg?width=1200&quality=85&auto=format&fit=max&s=ea38beaf0a4e51b9e214e025cf4b10fb"},
]

cols = st.columns(3)
for i, art in enumerate(artistas):
    with cols[i]:
        st.markdown(
            f"""
            <div style="text-align:center;">
                <img src="{art['img']}" style="width:100%; height:220px; object-fit:cover; border-radius:15px;"/>
                <p><b>{art['nombre']}</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- CSS HOVER ----------------
st.markdown(
    """
    <style>
    img {
        transition: transform 0.3s ease;
    }
    img:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(0,0,0,0.35);
    }
    </style>
    """,
    unsafe_allow_html=True
)
