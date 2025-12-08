import streamlit as st
import random

# 🔗 Activer le PWA (manifest + service worker)
st.markdown("""
<link rel="manifest" href="manifest.json">
<script>
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register("service-worker.js")
  }
</script>
""", unsafe_allow_html=True)

# 🎁 Interface GiftMind
st.set_page_config(page_title="GiftMind", page_icon="🎁")
st.title("🎁 GiftMind")
st.markdown("**Un sanctuaire numérique pour semer la gratitude, la sagesse et la lumière.**")

# 🌸 Liste de cadeaux spirituels
cadeaux = [
    "🌿 Une parole douce pour aujourd’hui : *« La gratitude est la mémoire du cœur. »*",
    "🕊️ Une prière silencieuse t’accompagne.",
    "🌙 Une lumière intérieure veille sur toi.",
    "💧 Une larme de miséricorde purifie ton cœur.",
    "🌸 Un souffle de paix pour ton chemin.",
]

# 🎈 Interaction principale
if st.button("Recevoir un cadeau de sagesse"):
    st.success(random.choice(cadeaux))

# ✍️ Zone de vœu
st.markdown("---")
voeu = st.text_area("Exprime un vœu ou une prière")
if voeu:
    st.info("🪶 Que ce vœu s’élève avec douceur.")
