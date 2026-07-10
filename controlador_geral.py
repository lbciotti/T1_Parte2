from controller.controlador_clinica import ControladorClinica
from controller.controlador_paciente import ControladorPaciente
from controller.controlador_profissional import ControladorProfissional
from controller.controlador_tipo_atendimento import ControladorTipoAtendimento
from controller.controlador_atendimento import ControladorAtendimento
from controller.controlador_pagamento import ControladorPagamento
from view.tela_menu_principal import TelaMenuPrincipal


class ControladorGeral:
    """
    Controlador principal do sistema.
    Instancia e conecta todos os controladores específicos (composição).
    É o único ponto de entrada da aplicação.
    """

    def __init__(self):
        # Cadastros independentes
        self.__ctrl_clinica      = ControladorClinica()
        self.__ctrl_paciente     = ControladorPaciente()
        self.__ctrl_profissional = ControladorProfissional()
        self.__ctrl_tipo         = ControladorTipoAtendimento()

        # Atendimento depende dos quatro acima (associação)
        self.__ctrl_atendimento = ControladorAtendimento(
            ctrl_clinica=self.__ctrl_clinica,
            ctrl_paciente=self.__ctrl_paciente,
            ctrl_profissional=self.__ctrl_profissional,
            ctrl_tipo=self.__ctrl_tipo,
        )

        # Pagamento depende de atendimento e paciente
        self.__ctrl_pagamento = ControladorPagamento(
            ctrl_atendimento=self.__ctrl_atendimento,
            ctrl_paciente=self.__ctrl_paciente,
        )

        self.__tela = TelaMenuPrincipal()

    def iniciar(self):
        """Inicia o sistema e abre o menu principal."""
        self.__tela.mostrar_mensagem("Bem-vindo ao Sistema de Gerenciamento de Clínicas!")
        self.abrir_menu_principal()

    def abrir_menu_principal(self):
        while True:
            try:
                op = self.__tela.mostrar_opcoes()
                if op == 0:
                    self.__tela.mostrar_mensagem("Encerrando o sistema. Até logo!")
                    break
                elif op == 1:
                    self.__ctrl_clinica.abrir_menu()
                elif op == 2:
                    self.__ctrl_paciente.abrir_menu()
                elif op == 3:
                    self.__ctrl_profissional.abrir_menu()
                elif op == 4:
                    self.__ctrl_tipo.abrir_menu()
                elif op == 5:
                    self.__ctrl_atendimento.abrir_menu()
                elif op == 6:
                    self.__ctrl_pagamento.abrir_menu()
                elif op == 7:
                    self.__abrir_relatorios()
                else:
                    self.__tela.mostrar_mensagem("Opção inválida.")
            except ValueError:
                self.__tela.mostrar_mensagem("Digite um número válido.")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Erro inesperado: {e}")

    def __abrir_relatorios(self):
        while True:
            print("\n--- RELATÓRIOS ---")
            print("1 - Clínicas com mais atendimentos")
            print("2 - Atendimentos mais caros e mais baratos")
            print("3 - Procedimentos mais populares")
            print("4 - Procedimentos mais caros e mais baratos")
            print("0 - Voltar")
            try:
                op = int(input("Opção: "))
                if op == 0:
                    break
                elif op == 1:
                    dados = self.__ctrl_atendimento.relatorio_clinica_mais_atendimentos()
                    self.__ctrl_atendimento._ControladorAtendimento__tela.mostrar_relatorio(
                        "Clínicas por Atendimentos", dados)
                elif op == 2:
                    dados = self.__ctrl_atendimento.relatorio_mais_caros_baratos()
                    self.__ctrl_atendimento._ControladorAtendimento__tela.mostrar_relatorio(
                        "Atendimentos por Valor", dados)
                elif op == 3:
                    dados = self.__ctrl_atendimento.relatorio_procedimentos_populares()
                    self.__ctrl_atendimento._ControladorAtendimento__tela.mostrar_relatorio(
                        "Procedimentos Populares", dados)
                elif op == 4:
                    dados = self.__ctrl_atendimento.relatorio_procedimentos_caros_baratos()
                    self.__ctrl_atendimento._ControladorAtendimento__tela.mostrar_relatorio(
                        "Procedimentos por Custo", dados)
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")
