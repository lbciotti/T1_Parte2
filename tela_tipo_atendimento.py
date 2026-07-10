class TelaTipoAtendimento:
    """Tela para operações de Tipo de Atendimento."""

    def mostrar_opcoes(self) -> int:
        print("\n--- TIPOS DE ATENDIMENTO ---")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        return int(input("Opção: "))

    def pegar_dados_tipo(self) -> dict:
        descricao = input("Descrição do tipo (ex: Consulta, Exame, Retorno): ")
        return {"descricao": descricao}

    def pegar_descricao(self) -> str:
        return input("Descrição do tipo: ")

    def mostrar_tipos(self, lista: list):
        if not lista:
            print("Nenhum tipo cadastrado.")
            return
        print("\n--- Tipos de Atendimento ---")
        for t in lista:
            print(f"  {t.descricao}")

    def mostrar_mensagem(self, msg: str):
        print(f"\n{msg}")
