import streamlit as st

st.title("Primeiros Socorros Básicos")


st.subheader("Engasgamento")
st.write("""
1. Verifique se a pessoa consegue tossir ou falar.  
2. Se não conseguir, faça a manobra de Heimlich.  
""")

st.subheader("Cortes")
st.write("""
1. Lave bem as mãos antes de tocar no ferimento.  
2. Faça pressão no corte com um pano limpo.  
3. Procure atendimento se o corte for profundo.  
""")

st.subheader("Queimaduras")
st.write("""
1. Resfrie a área com água corrente por pelo menos 10 minutos.  
2. Não use pomadas nem estoure bolhas.  
3. Cubra levemente com um pano limpo.  
""")


html = """
<html>
<head><title>Primeiros Socorros</title></head>
<body>
<h1>Primeiros Socorros Básicos</h1>
<h2>Engasgamento</h2>
<p>1. Verifique se a pessoa consegue tossir ou falar.</p>
<p>2. Se não conseguir, faça a manobra de Heimlich.</p>

<h2>Cortes</h2>
<p>1. Lave bem as mãos antes de tocar no ferimento.</p>
<p>2. Faça pressão no corte com um pano limpo.</p>

<h2>Queimaduras</h2>
<p>1. Resfrie a área com água corrente por pelo menos 10 minutos.</p>
<p>2. Não use pomadas nem estoure bolhas.</p>
</body>
</html>
"""

 # python -m streamlit run app.py
with open("site.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Site criado! Abra o arquivo site.html no navegador.")


st.image("classe do fogo.png", width= 500)
st.image("codigo de comunicação via radio.png")
st.image("desengasgo de bebês.png")
st.image("evitar incêndio de gas de cozinha.png")
st.image("modo de uso.png", width= 500)
st.image("oque fazer em caso de convulção.png")
st.image("queimaduras tipo 1,2,3.png", width= 500)
st.image("tipos de extintores mais usados.png")
st.image("tipos de hemorragias.png")