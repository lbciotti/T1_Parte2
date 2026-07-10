"""
INE5605 - Desenvolvimento de Sistemas Orientados a Objetos I
Trabalho 1 - Sistema de Gerenciamento de Clínicas

Aluno: Lucca Bolsanello Ciotti (25202568)

Para executar: python main.py
"""

from controller.controlador_geral import ControladorGeral

if __name__ == "__main__":
    sistema = ControladorGeral()
    sistema.iniciar()
