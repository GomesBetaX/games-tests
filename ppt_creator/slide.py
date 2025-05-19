import comtypes.client
import os
import sys
import re
import json
import creator
from tkinter import messagebox

def recurso_caminho(relative_path):
    """Retorna o caminho absoluto para recursos dentro do .exe ou do projeto."""
    try:
        base_path = sys._MEIPASS  # Quando empacotado pelo PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")  # Durante execução normal
    return os.path.join(base_path, relative_path)


class Preencher():
    def __init__(self):
        self.template = None
        self.skeleton = 0
        self.type_class = None

    def create_skeleton(self, nome, texto):
        # Caminho absoluto para a pasta de saída
        pasta_aulas = recurso_caminho("aulas")
        os.makedirs(pasta_aulas, exist_ok=True)
        caminho_txt = os.path.join(pasta_aulas, f"{nome}.txt")

        sket = creator.GPT()
        text = sket.get_skeleton(texto)
        with open(caminho_txt, "w", encoding="utf-8") as file:
            file.write(text)

    def limpar(self, texto):
        return texto.replace("(", "").replace(")", "").replace("\n", " ").strip()
    
    def preencher_template(self, classe, caminho_template=None, caminho_saida=None):

        caminho_template = self.template or "template"
        caminho_template_pptx = recurso_caminho(f"{caminho_template}.pptx")

        if not os.path.exists(caminho_template_pptx):
            raise FileNotFoundError(f"Arquivo de template não encontrado: {caminho_template_pptx}")

        # Caminho base para salvar o slide
        pasta_aulas = recurso_caminho("aulas")
        os.makedirs(pasta_aulas, exist_ok=True)

        if caminho_saida is None:
            caminho_saida = os.path.join(pasta_aulas, "aula_gerada.pptx")

        # Inicializa PowerPoint
        powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
        presentation = powerpoint.Presentations.Open(caminho_template_pptx, ReadOnly=1)

        wrap_ups = self.parse_wrap_up(classe.get("wrap_up", ""))
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

        for slide in presentation.Slides:
            for shape in slide.Shapes:
                if shape.HasTextFrame and shape.TextFrame.HasText:
                    shape.TextFrame2.AutoSize = 2
                    texto = shape.TextFrame.TextRange.Text
                    for placeholder, valor in valores.items():
                        if placeholder in texto:
                            texto = texto.replace(placeholder, valor)
                    shape.TextFrame.TextRange.Text = texto

        # Garantir nome único
        base_name = os.path.splitext(os.path.basename(caminho_saida))[0]
        ext = ".pptx"
        i = 1
        novo_caminho = caminho_saida
        while os.path.exists(novo_caminho):
            novo_caminho = os.path.join(pasta_aulas, f"{base_name}_{i}{ext}")
            i += 1
        txt_name = os.path.splitext(os.path.basename(novo_caminho))[0]

        messagebox.showinfo(title="Confirmação", message=f"✅ Slide gerado em: {novo_caminho}")

        if self.skeleton != 0:
            print(f"Aula criada: {classe}")
            self.create_skeleton(txt_name, classe)
            messagebox.showinfo(title="Confirmação", message=f"✅ Esqueleto da aula gerado em: {txt_name}.txt")

        os.startfile(os.path.dirname(novo_caminho))

        presentation.SaveAs(novo_caminho)
        presentation.Close()
        powerpoint.Quit()

    def parse_wrap_up(self, texto):
        resultado = {}
        try:
            match = re.search(r"\[\s*{.*?}\s*\]", texto, re.DOTALL)
            if match:
                perguntas = json.loads(match.group(0))
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
        return resultado

