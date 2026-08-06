"""
Jogo da Cobrinha (Snake) em Python usando tkinter
--------------------------------------------------
Essa versao usa apenas a biblioteca padrao do Python (tkinter), entao
NAO precisa instalar nada (nem pygame). Funciona em qualquer versao
do Python, incluindo a 3.14.

Como rodar:
   No VS Code, abra este arquivo e clique em "Run" (ou F5),
   ou pelo terminal: python jogo_da_cobrinha.py

Controles:
- Setas do teclado para mover
- Tecla R para reiniciar depois de perder
"""

import tkinter as tk
import random

# ------------------- Configuracoes -------------------
LARGURA_TELA = 1000
ALTURA_TELA = 1000
TAMANHO_BLOCO = 20
VELOCIDADE_INICIAL =100 # em milissegundos entre cada movimento (menor = mais rapido)

COR_FUNDO = "#000000"
COR_COBRA_CABECA = "#00c800"
COR_COBRA_CORPO = "#009600"
COR_COMIDA = "#dc1e1e"
COR_TEXTO = "#ffffff"


class JogoCobrinha:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Jogo da Cobrinha - Python")

        self.canvas = tk.Canvas(
            raiz, width=LARGURA_TELA, height=ALTURA_TELA, bg=COR_FUNDO, highlightthickness=0
        )
        self.canvas.pack()

        self.raiz.bind("<KeyPress>", self.tecla_pressionada)

        self.reiniciar()

    def reiniciar(self):
        x, y = LARGURA_TELA // 2, ALTURA_TELA // 2
        # a cobra e uma lista de posicoes (x, y); o primeiro item e a cabeca
        self.cobra = [(x, y), (x - TAMANHO_BLOCO, y), (x - 2 * TAMANHO_BLOCO, y)]
        self.direcao = "Right"
        self.proxima_direcao = "Right"
        self.pontuacao = 0
        self.velocidade = VELOCIDADE_INICIAL
        self.game_over = False
        self.comida = self.gerar_comida()

        self.desenhar()
        self.loop()

    def gerar_comida(self):
        while True:
            pos = (
                random.randrange(0, LARGURA_TELA, TAMANHO_BLOCO),
                random.randrange(0, ALTURA_TELA, TAMANHO_BLOCO),
            )
            if pos not in self.cobra:
                return pos

    def tecla_pressionada(self, evento):
        tecla = evento.keysym

        if self.game_over:
            if tecla.lower() == "r":
                self.reiniciar()
            return

        opostos = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if tecla in ("Up", "Down", "Left", "Right"):
            if opostos.get(tecla) != self.direcao:
                self.proxima_direcao = tecla

    def mover(self):
        self.direcao = self.proxima_direcao
        x, y = self.cobra[0]

        if self.direcao == "Up":
            y -= TAMANHO_BLOCO
        elif self.direcao == "Down":
            y += TAMANHO_BLOCO
        elif self.direcao == "Left":
            x -= TAMANHO_BLOCO
        elif self.direcao == "Right":
            x += TAMANHO_BLOCO

        nova_cabeca = (x, y)

        bateu_na_parede = x < 0 or x >= LARGURA_TELA or y < 0 or y >= ALTURA_TELA
        bateu_em_si_mesma = nova_cabeca in self.cobra

        if bateu_na_parede or bateu_em_si_mesma:
            self.game_over = True
            return

        self.cobra.insert(0, nova_cabeca)

        if nova_cabeca == self.comida:
            self.pontuacao += 1
            self.comida = self.gerar_comida()
            if self.pontuacao % 5 == 0 and self.velocidade > 60:
                self.velocidade -= 8
        else:
            self.cobra.pop()

    def desenhar(self):
        self.canvas.delete("all")

        # grade sutil de fundo
        for gx in range(0, LARGURA_TELA, TAMANHO_BLOCO):
            self.canvas.create_line(gx, 0, gx, ALTURA_TELA, fill="#282828")
        for gy in range(0, ALTURA_TELA, TAMANHO_BLOCO):
            self.canvas.create_line(0, gy, LARGURA_TELA, gy, fill="#282828")

        # comida
        fx, fy = self.comida
        self.canvas.create_rectangle(
            fx, fy, fx + TAMANHO_BLOCO, fy + TAMANHO_BLOCO, fill=COR_COMIDA, outline=""
        )

        # cobra
        for i, (sx, sy) in enumerate(self.cobra):
            cor = COR_COBRA_CABECA if i == 0 else COR_COBRA_CORPO
            self.canvas.create_rectangle(
                sx, sy, sx + TAMANHO_BLOCO, sy + TAMANHO_BLOCO, fill=cor, outline=COR_FUNDO
            )

        # pontuacao
        self.canvas.create_text(
            60, 15, text=f"Pontos: {self.pontuacao}", fill=COR_TEXTO, font=("Arial", 14)
        )

        if self.game_over:
            self.canvas.create_text(
                LARGURA_TELA // 2, ALTURA_TELA // 2 - 20,
                text="FIM DE JOGO", fill=COR_COMIDA, font=("Arial", 32, "bold")
            )
            self.canvas.create_text(
                LARGURA_TELA // 2, ALTURA_TELA // 2 + 20,
                text=f"Pontuacao final: {self.pontuacao}", fill=COR_TEXTO, font=("Arial", 16)
            )
            self.canvas.create_text(
                LARGURA_TELA // 2, ALTURA_TELA // 2 + 50,
                text="Pressione R para jogar novamente", fill=COR_TEXTO, font=("Arial", 14)
            )

    def loop(self):
        if not self.game_over:
            self.mover()
            self.desenhar()
            self.raiz.after(self.velocidade, self.loop)
        else:
            self.desenhar()


if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.resizable(False, False)
    jogo = JogoCobrinha(raiz)
    raiz.mainloop()