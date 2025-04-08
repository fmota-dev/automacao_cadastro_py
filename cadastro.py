import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3


def esperar_e_localizar(imagem, imagem_alternativa=None, confidence=0.9, timeout=10):
    """Tenta localizar a imagem na tela, com tempo máximo de espera e imagem alternativa."""
    inicio = time.time()
    while time.time() - inicio < timeout:
        local = pyautogui.locateOnScreen(imagem, confidence=confidence)
        if local:
            return local
        if imagem_alternativa:
            local_alt = pyautogui.locateOnScreen(
                imagem_alternativa, confidence=confidence
            )
            if local_alt:
                return local_alt
    raise pyautogui.ImageNotFoundException(
        f"Imagem não encontrada: {imagem} nem {imagem_alternativa}"
    )


def abrir_navegador():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    pyautogui.press("enter")
    time.sleep(3)


def fazer_login(email, senha):
    campo_email = esperar_e_localizar("./imgs/campo_email.png")
    pyautogui.click(campo_email)
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)


def cadastrar_produto(dados_produto, primeira_vez=False):
    if primeira_vez:
        try:
            campo_codigo = esperar_e_localizar(
                "./imgs/campo_codigo.png",
                imagem_alternativa="./imgs/campo_codigo_apos_cadastro.png",
            )
            pyautogui.click(campo_codigo)
        except pyautogui.ImageNotFoundException:
            print(
                "⚠️ Campo código não encontrado na primeira vez. Usando coordenadas fixas."
            )
            pyautogui.click(x=653, y=294)
    else:
        pyautogui.click(x=653, y=294)

    pyautogui.write(str(dados_produto["codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(dados_produto["marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(dados_produto["tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(dados_produto["categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(dados_produto["preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(dados_produto["custo"]))
    pyautogui.press("tab")

    obs = dados_produto.get("obs", "")
    if pd.notna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")  # clicar em "Cadastrar"
    time.sleep(1)
    pyautogui.scroll(5000)  # voltar ao topo para próximo cadastro


def fechar_popup_se_existir():
    try:
        botao_ok = pyautogui.locateOnScreen("./imgs/popup_ok.png", confidence=0.9)
        if botao_ok:
            pyautogui.click(botao_ok)
            time.sleep(1)
    except:
        pass  # ignora se não encontrar


def main():
    email = "pythonimpressionador@gmail.com"
    senha = "messinhodoboqueteiro"

    inicio = time.time()  # Início da contagem de tempo

    abrir_navegador()
    fazer_login(email, senha)
    fechar_popup_se_existir()

    tabela = pd.read_csv("produtos.csv")
    print(tabela)

    for i, linha in enumerate(tabela.index):
        dados_produto = tabela.loc[linha]
        cadastrar_produto(dados_produto, primeira_vez=(i == 0))

    fim = time.time()  # Fim da contagem de tempo
    tempo_total = fim - inicio
    minutos = int(tempo_total // 60)
    segundos = int(tempo_total % 60)
    print(f"\n✅ Cadastro finalizado! Tempo total: {minutos}m {segundos}s.")


if __name__ == "__main__":
    main()
