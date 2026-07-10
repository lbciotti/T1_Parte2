from datetime import date, time


class TelaAtendimento:
    """Tela para operações de Atendimento."""

    def mostrar_opcoes(self) -> int:
        print("\n--- ATENDIMENTOS ---")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("5 - Adicionar procedimento")
        print("0 - Voltar")
        return int(input("Opção: "))

    def pegar_dados_atendimento(self) -> dict:
        print("\n--- Dados do Atendimento ---")
        cpf_paciente     = input("CPF do paciente: ")
        cpf_profissional = input("CPF do profissional: ")
        nome_clinica     = input("Nome da clínica: ")
        tipo_desc        = input("Tipo de atendimento: ")
        data_str         = input("Data (AAAA-MM-DD): ")
        h_ini            = input("Hora início (HH:MM): ")
        h_fim            = input("Hora fim (HH:MM): ")
        valor            = float(input("Valor (R$): "))
        return {
            "cpf_paciente":     cpf_paciente,
            "cpf_profissional": cpf_profissional,
            "nome_clinica":     nome_clinica,
            "tipo_desc":        tipo_desc,
            "data":             date(*map(int, data_str.split("-"))),
            "hora_inicio":      time(*map(int, h_ini.split(":"))),
            "hora_fim":         time(*map(int, h_fim.split(":"))),
            "valor":            valor,
        }

    def pegar_indice(self, tamanho: int) -> int:
        return int(input(f"Número do atendimento (1-{tamanho}): ")) - 1

    def pegar_dados_procedimento(self) -> dict:
        print("\n--- Dados do Procedimento ---")
        descricao        = input("Descrição: ")
        custo            = float(input("Custo (R$): "))
        cpf_profissional = input("CPF do profissional responsável: ")
        return {"descricao": descricao, "custo": custo, "cpf_profissional": cpf_profissional}

    def mostrar_atendimentos(self, lista: list):
        if not lista:
            print("Nenhum atendimento cadastrado.")
            return
        print("\n--- Atendimentos ---")
        for i, a in enumerate(lista, 1):
            print(f"  {i}. {a.paciente.nome} | {a.profissional.nome} | "
                  f"{a.data} {a.hora_inicio}-{a.hora_fim} | "
                  f"{a.clinica.nome} | R$ {a.valor:.2f}")

    def mostrar_relatorio(self, titulo: str, dados: list):
        print(f"\n--- {titulo} ---")
        for linha in dados:
            print(f"  {linha}")

    def mostrar_mensagem(self, msg: str):
        print(f"\n{msg}")
