from model.models import Pagamento, PagamentoDinheiro, PagamentoPix, PagamentoCartao
from view.tela_pagamento import TelaPagamento


class ControladorPagamento:
    """Controlador responsável pelo CRUD de Pagamentos."""

    def __init__(self, ctrl_atendimento, ctrl_paciente):
        self.__pagamentos: list[Pagamento] = []
        self.__tela = TelaPagamento()
        # Associações com outros controladores
        self.__ctrl_atendimento = ctrl_atendimento
        self.__ctrl_paciente    = ctrl_paciente

    def abrir_menu(self):
        while True:
            try:
                op = self.__tela.mostrar_opcoes()
                if op == 0:
                    break
                elif op == 1:
                    self.incluir_pagamento()
                elif op == 2:
                    self.excluir_pagamento()
                elif op == 3:
                    self.listar_pagamentos()
                else:
                    self.__tela.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Erro: {e}")

    def incluir_pagamento(self):
        # Exibe atendimentos disponíveis para referência
        self.__ctrl_atendimento.listar_atendimentos()
        dados = self.__tela.pegar_dados_pagamento()

        atendimento = self.__ctrl_atendimento.buscar_por_indice(dados["indice_atendimento"])
        paciente    = self.__ctrl_paciente.buscar_por_cpf(dados["cpf_paciente"])

        if not atendimento or not paciente:
            self.__tela.mostrar_mensagem("Atendimento ou paciente não encontrado.")
            return

        modalidade = dados["modalidade"]
        kwargs = dict(
            data_pagamento=dados["data_pagamento"],
            atendimento=atendimento,
            paciente=paciente,
            valor_pago=dados["valor_pago"],
        )

        if modalidade == "dinheiro":
            pagamento = PagamentoDinheiro(**kwargs)
        elif modalidade == "pix":
            pagamento = PagamentoPix(**kwargs, cpf_pagador=dados["cpf_pagador"])
        elif modalidade == "cartao":
            pagamento = PagamentoCartao(**kwargs,
                                        numero_cartao=dados["numero_cartao"],
                                        bandeira=dados["bandeira"])
        else:
            self.__tela.mostrar_mensagem("Modalidade inválida.")
            return

        self.__pagamentos.append(pagamento)
        self.__tela.mostrar_mensagem(
            f"Pagamento registrado. Valor restante: R$ {pagamento.valor_restante:.2f}")

    def excluir_pagamento(self):
        self.listar_pagamentos()
        if not self.__pagamentos:
            return
        idx = self.__tela.pegar_indice(len(self.__pagamentos))
        if idx < 0 or idx >= len(self.__pagamentos):
            self.__tela.mostrar_mensagem("Índice inválido.")
            return
        self.__pagamentos.pop(idx)
        self.__tela.mostrar_mensagem("Pagamento excluído.")

    def listar_pagamentos(self):
        self.__tela.mostrar_pagamentos(self.__pagamentos)

    def get_pagamentos(self) -> list:
        return list(self.__pagamentos)
