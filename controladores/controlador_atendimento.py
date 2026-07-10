from model.models import Atendimento, Procedimento
from view.tela_atendimento import TelaAtendimento


class ControladorAtendimento:
    """
    Controlador responsável pelo CRUD de Atendimentos e Procedimentos,
    além da geração de relatórios.
    """

    def __init__(self, ctrl_clinica, ctrl_paciente, ctrl_profissional, ctrl_tipo):
        self.__atendimentos: list[Atendimento] = []
        self.__tela = TelaAtendimento()
        # Referências para outros controladores (associação)
        self.__ctrl_clinica      = ctrl_clinica
        self.__ctrl_paciente     = ctrl_paciente
        self.__ctrl_profissional = ctrl_profissional
        self.__ctrl_tipo         = ctrl_tipo

    def abrir_menu(self):
        while True:
            try:
                op = self.__tela.mostrar_opcoes()
                if op == 0:
                    break
                elif op == 1:
                    self.incluir_atendimento()
                elif op == 2:
                    self.alterar_atendimento()
                elif op == 3:
                    self.excluir_atendimento()
                elif op == 4:
                    self.listar_atendimentos()
                elif op == 5:
                    self.adicionar_procedimento()
                else:
                    self.__tela.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Erro: {e}")

    def incluir_atendimento(self):
        dados = self.__tela.pegar_dados_atendimento()

        clinica      = self.__ctrl_clinica.buscar_por_nome(dados["nome_clinica"])
        paciente     = self.__ctrl_paciente.buscar_por_cpf(dados["cpf_paciente"])
        profissional = self.__ctrl_profissional.buscar_por_cpf(dados["cpf_profissional"])
        tipo         = self.__ctrl_tipo.buscar_por_descricao(dados["tipo_desc"])

        if not all([clinica, paciente, profissional, tipo]):
            self.__tela.mostrar_mensagem("Clínica, paciente, profissional ou tipo não encontrado.")
            return

        atendimento = Atendimento(
            clinica=clinica,
            paciente=paciente,
            profissional=profissional,
            data=dados["data"],
            hora_inicio=dados["hora_inicio"],
            hora_fim=dados["hora_fim"],
            tipo=tipo,
            valor=dados["valor"],
        )
        self.__atendimentos.append(atendimento)
        self.__tela.mostrar_mensagem("Atendimento incluído com sucesso.")

    def alterar_atendimento(self):
        self.listar_atendimentos()
        if not self.__atendimentos:
            return
        idx = self.__tela.pegar_indice(len(self.__atendimentos))
        if idx < 0 or idx >= len(self.__atendimentos):
            self.__tela.mostrar_mensagem("Índice inválido.")
            return
        self.__atendimentos.pop(idx)
        self.incluir_atendimento()

    def excluir_atendimento(self):
        self.listar_atendimentos()
        if not self.__atendimentos:
            return
        idx = self.__tela.pegar_indice(len(self.__atendimentos))
        if idx < 0 or idx >= len(self.__atendimentos):
            self.__tela.mostrar_mensagem("Índice inválido.")
            return
        self.__atendimentos.pop(idx)
        self.__tela.mostrar_mensagem("Atendimento excluído.")

    def listar_atendimentos(self):
        self.__tela.mostrar_atendimentos(self.__atendimentos)

    def adicionar_procedimento(self):
        self.listar_atendimentos()
        if not self.__atendimentos:
            return
        idx = self.__tela.pegar_indice(len(self.__atendimentos))
        dados = self.__tela.pegar_dados_procedimento()
        prof = self.__ctrl_profissional.buscar_por_cpf(dados["cpf_profissional"])
        if not prof:
            self.__tela.mostrar_mensagem("Profissional não encontrado.")
            return
        proc = Procedimento(dados["descricao"], dados["custo"], prof)
        self.__atendimentos[idx].adicionar_procedimento(proc)
        self.__tela.mostrar_mensagem("Procedimento adicionado.")

    # ---- Relatórios ----

    def relatorio_clinica_mais_atendimentos(self) -> list:
        """Clínicas ordenadas por número de atendimentos."""
        contagem = {}
        for a in self.__atendimentos:
            contagem[a.clinica.nome] = contagem.get(a.clinica.nome, 0) + 1
        ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
        return [f"{nome}: {qtd} atendimento(s)" for nome, qtd in ordenado]

    def relatorio_mais_caros_baratos(self) -> list:
        """Atendimentos mais caros e mais baratos."""
        if not self.__atendimentos:
            return ["Sem atendimentos."]
        ordenado = sorted(self.__atendimentos, key=lambda a: a.valor, reverse=True)
        resultado = ["=== Mais caros ==="]
        for a in ordenado[:3]:
            resultado.append(f"  {a.paciente.nome} | {a.clinica.nome} | R$ {a.valor:.2f}")
        resultado.append("=== Mais baratos ===")
        for a in ordenado[-3:]:
            resultado.append(f"  {a.paciente.nome} | {a.clinica.nome} | R$ {a.valor:.2f}")
        return resultado

    def relatorio_procedimentos_populares(self) -> list:
        """Procedimentos mais realizados."""
        contagem = {}
        for a in self.__atendimentos:
            for p in a.procedimentos:
                contagem[p.descricao] = contagem.get(p.descricao, 0) + 1
        if not contagem:
            return ["Nenhum procedimento registrado."]
        ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
        return [f"{desc}: {qtd}x" for desc, qtd in ordenado]

    def relatorio_procedimentos_caros_baratos(self) -> list:
        """Procedimentos mais caros e mais baratos."""
        procs = [p for a in self.__atendimentos for p in a.procedimentos]
        if not procs:
            return ["Nenhum procedimento registrado."]
        ordenado = sorted(procs, key=lambda p: p.custo, reverse=True)
        resultado = ["=== Mais caros ==="]
        for p in ordenado[:3]:
            resultado.append(f"  {p.descricao} | R$ {p.custo:.2f}")
        resultado.append("=== Mais baratos ===")
        for p in ordenado[-3:]:
            resultado.append(f"  {p.descricao} | R$ {p.custo:.2f}")
        return resultado

    def get_atendimentos(self) -> list:
        return list(self.__atendimentos)

    def buscar_por_indice(self, idx: int):
        if 0 <= idx < len(self.__atendimentos):
            return self.__atendimentos[idx]
        return None
