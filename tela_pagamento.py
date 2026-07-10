from datetime import date


class TelaPagamento:
    """Tela para operações de Pagamento."""

    def mostrar_opcoes(self) -> int:
        print("\n--- PAGAMENTOS ---")
        print("1 - Incluir")
        print("2 - Excluir")
        print("3 - Listar")
        print("0 - Voltar")
        return int(input("Opção: "))

    def pegar_dados_pagamento(self) -> dict:
        print("\n--- Dados do Pagamento ---")
        indice_atend = int(input("Número do atendimento: ")) - 1
        cpf_paciente = input("CPF do paciente: ")
        data_str     = input("Data do pagamento (AAAA-MM-DD): ")
        valor_pago   = float(input("Valor pago (R$): "))
        modalidade   = self.pegar_modalidade()
        dados = {
            "indice_atendimento": indice_atend,
            "cpf_paciente":       cpf_paciente,
            "data_pagamento":     date(*map(int, data_str.split("-"))),
            "valor_pago":         valor_pago,
            "modalidade":         modalidade,
        }
        if modalidade == "pix":
            dados["cpf_pagador"] = input("CPF do pagador (Pix): ")
        elif modalidade == "cartao":
            dados["numero_cartao"] = input("Número do cartão: ")
            dados["bandeira"]      = input("Bandeira (Visa/Mastercard/Elo/Amex): ")
        return dados

    def pegar_modalidade(self) -> str:
        print("Modalidade: 1-Dinheiro  2-Pix  3-Cartão")
        op = int(input("Opção: "))
        return {1: "dinheiro", 2: "pix", 3: "cartao"}.get(op, "dinheiro")

    def pegar_indice(self, tamanho: int) -> int:
        return int(input(f"Número do pagamento (1-{tamanho}): ")) - 1

    def mostrar_pagamentos(self, lista: list):
        if not lista:
            print("Nenhum pagamento cadastrado.")
            return
        print("\n--- Pagamentos ---")
        for i, p in enumerate(lista, 1):
            print(f"  {i}. [{p.modalidade()}] {p.paciente.nome} | "
                  f"R$ {p.valor_pago:.2f} | Restante: R$ {p.valor_restante:.2f} | "
                  f"{p.data_pagamento}")

    def mostrar_mensagem(self, msg: str):
        print(f"\n{msg}")
