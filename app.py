
import streamlit as st

st.set_page_config(page_title="Calculadora de Rating Elo", page_icon="♟️")

st.title("♟️ Calculadora de Rating Elo - Estilo Social Chess")

st.markdown("""
Esta é uma calculadora simples que simula como funciona o cálculo de rating Elo,
igual aos sistemas usados em plataformas como Social Chess, Lichess e Chess.com.
""")

# Inputs
st.header("Dados da Partida")

rating_jogador = st.number_input("Seu rating atual", min_value=100, max_value=3500, value=1200)
rating_oponente = st.number_input("Rating do oponente", min_value=100, max_value=3500, value=1200)

resultado = st.selectbox(
    "Resultado da partida",
    options=[("Vitória", 1), ("Empate", 0.5), ("Derrota", 0)],
    format_func=lambda x: x[0]
)[1]

k = st.slider("Fator K (sensibilidade da variação)", min_value=10, max_value=64, value=32)


# Função de cálculo
def calcular_elo(rating_jogador, rating_oponente, resultado, k=32):
    expectativa = 1 / (1 + 10 ** ((rating_oponente - rating_jogador) / 400))
    variacao = k * (resultado - expectativa)
    novo_rating = rating_jogador + variacao
    return round(novo_rating, 2), round(variacao, 2), round(expectativa * 100, 2)


# Cálculo
if st.button("Calcular"):
    novo_rating, variacao, expectativa = calcular_elo(rating_jogador, rating_oponente, resultado, k)
    
    st.subheader("🔢 Resultado")
    st.write(f"🔸 **Expectativa de vitória:** {expectativa}%")
    
    if variacao > 0:
        st.success(f"Você GANHOU {variacao} pontos!")
    elif variacao < 0:
        st.error(f"Você PERDEU {abs(variacao)} pontos!")
    else:
        st.info("Seu rating não mudou.")
    
    st.write(f"🏆 **Seu novo rating é:** {novo_rating}")

st.markdown("---")
st.markdown("Desenvolvido com Streamlit.")
