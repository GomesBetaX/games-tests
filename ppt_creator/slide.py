import comtypes.client
import os
import re
import json
import creator
from tkinter import messagebox

class Preencher():
    def __init__(self):
        self.template = None
        self.skeleton = 0

    def create_skeleton(self, nome, texto):
        sket = creator.GPT()
        text = sket.get_skeleton(texto)
        print(text)
        with open(f"{nome}.txt", "w") as file:
            file.write(text)

    def limpar(self, texto):
        return texto.replace("(", "").replace(")", "").replace("\n", " ").strip()
    
    def preencher_template(self, classe, caminho_template=None, caminho_saida="aula_gerada.pptx"):

        # print(classe)
        caminho_template = self.template

        if caminho_template == None or caminho_template == "neutro":
            caminho_template = "template"

        caminho_absoluto = os.path.abspath(f"{caminho_template}.pptx")
        if not os.path.exists(caminho_absoluto):
            raise FileNotFoundError(f"Arquivo de template não encontrado: {caminho_absoluto}")

        # Inicializa PowerPoint
        powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
        # powerpoint.Visible = 0
        presentation = powerpoint.Presentations.Open(caminho_absoluto, ReadOnly=1)

        # Separa o conteúdo do wrap-up
        wrap_ups = self.parse_wrap_up(classe.get("wrap_up", ""))

        # Dicionário base para substituição
        valores = {
            "{{warmup}}": self.limpar(classe.get("warm_up", "")),
            "{{question}}": self.limpar(classe.get("question", "")),
            "{{lead_in}}": self.limpar(classe.get("lead_in", "")),
            "{{example}}": self.limpar(classe.get("example", "")),
            "{{pair_work}}": self.limpar(classe.get("pair_work", "")),
            "{{pg}}": self.limpar(classe.get("page", "")),
            "{{production}}": self.limpar(classe.get("production", "")),
            "{{example_production}}": self.limpar(classe.get("example_production", "")),
            "{{actv1_wrap_up}}": self.limpar(wrap_ups.get("actv1", "")),
            "{{opt1_correct}}": self.limpar(wrap_ups.get("opt1_correct", "")),
            "{{opt2}}": self.limpar(wrap_ups.get("opt2", "")),
            "{{actv2_wrap_up}}": self.limpar(wrap_ups.get("actv2", "")),
            "{{opt1.1}}": self.limpar(wrap_ups.get("opt1.1", "")),
            "{{opt2.2_correct}}": self.limpar(wrap_ups.get("opt2.2_correct", "")),
            "{{actv3_wrap_up}}": self.limpar(wrap_ups.get("actv3", "")),
            "{{opt3.1_correct}}": self.limpar(wrap_ups.get("opt3.1_correct", "")),
            "{{opt3.2}}": self.limpar(wrap_ups.get("opt3.2", "")),
            "{{homework}}": self.limpar(classe.get("homework", ""))
        }

        # Substitui os placeholders nos slides
        for slide in presentation.Slides:
            for shape in slide.Shapes:
                if shape.HasTextFrame and shape.TextFrame.HasText:
                    shape.TextFrame2.AutoSize = 2
                    texto = shape.TextFrame.TextRange.Text
                    for placeholder, valor in valores.items():
                        if placeholder in texto:
                            texto = texto.replace(placeholder, valor)
                    shape.TextFrame.TextRange.Text = texto

        # Salva e fecha
        # Caminho base sem extensão
        base_name = os.path.splitext(os.path.basename(caminho_saida))[0]
        directory = os.path.dirname(os.path.abspath(caminho_saida))
        ext = ".pptx"

        # Tenta encontrar um nome único
        i = 1
        novo_nome = f"{base_name}{ext}"
        txt_name = f"{base_name}"
        novo_caminho = os.path.join(directory, novo_nome)
        while os.path.exists(novo_caminho):
            novo_nome = f"{base_name}_{i}{ext}"
            txt_name = f"{base_name}_{i}"
            novo_caminho = os.path.join(directory, novo_nome)
            i += 1
        print(f"✅ Slide gerado em: {caminho_saida}")

        # criar skeleton
        self.create_skeleton(txt_name, classe)

        presentation.SaveAs(novo_caminho)
        presentation.Close()
        messagebox.askyesno(title="Confirmação", message="Gostaria de abrir o esqueleto da aula?")
        powerpoint.Quit()



    def parse_wrap_up(self, texto):
        """
        Extrai JSON do wrap-up mesmo que esteja embutido em outro texto.
        """
        resultado = {}
        try:
            match = re.search(r"\[\s*{.*?}\s*\]", texto, re.DOTALL)
            if match:
                perguntas = json.loads(match.group(0))
                # print("Perguntas carregadas do JSON:", perguntas)

                if len(perguntas) >= 3:
                    resultado["actv1"] = perguntas[0]["pergunta"]
                    resultado["opt1_correct"] = perguntas[0]["a"]
                    resultado["opt2"] = perguntas[0]["b"]

                    resultado["actv2"] = perguntas[1]["pergunta"]
                    resultado["opt1.1"] = perguntas[1]["a"]
                    resultado["opt2.2_correct"] = perguntas[1]["b"]

                    resultado["actv3"] = perguntas[2]["pergunta"]
                    resultado["opt3.1_correct"] = perguntas[2]["a"]
                    resultado["opt3.2"] = perguntas[2]["b"]
            else:
                print("❌ Nenhum JSON encontrado no texto.")
        except json.JSONDecodeError as e:
            print("❌ Erro ao decodificar o JSON do wrap-up:", e)

        # print("✅ Resultado do parse_wrap_up (corrigido):", resultado)
        return resultado

