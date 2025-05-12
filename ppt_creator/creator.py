import requests
import re
from tkinter import messagebox

# Gemini config
GEMINI_API_KEY = "AIzaSyAwtSlrpGOJVTILUpQD6Zv5J_1VqdNhF6E"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

class GPT:

    def __init__(self):
        self.theme = ""
        self.extra = ""
        self.text = ""

        # print("\n📘 PLANO FORMATADO:")
        # for k, v in self.plan.items():
        #     print(f"\n{k}\n{v}")

    def get_skeleton(self, original_response):
        prompt = (
            f"Você é um professor com muita experiência e acabou de gerar a seguinte aula: {original_response}\n"
            "Agora, você precisa criar o esqueleto da aula, isto é, dentro das seguintes categorias, seguindo o mesmo plano de aula já criado(o que já existir) e inventando, de maneira coesa, o que faltar:\n"
            "warm up, lead in, presentation, controlled exercise, less-controlled exercises, freer, production, wrap up, homework assignment."
        )

        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(GEMINI_URL, json=payload, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Erro ao chamar Gemini: {response.status_code} {response.text}")

        response_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return response_text
    
    def remove_markdown(self, text):
        return re.sub(r'[*_`]', '', text).strip()

    def fetch_lesson_plan(self):

        prompt_wrap_up = (
            "Crie 3 atividades de revisão no formato de perguntas com múltipla escolha. "
            "Cada atividade deve ter: "
            '"pergunta", "a", "b" e "correta" (que deve ser "a" ou "b"). '
            "Retorne apenas a lista, como no exemplo: "
            '[{"pergunta": "Eu ___ todos os dias.", "a": "estudo", "b": "durmo", "correta": "a"}]'
        )

        prompt = (
            "Você é um professor com muita experiência, e precisa criar uma aula baseada no Bloom's Taxonomy e CRISP. "
            f"Pegue o tema da aula: '{self.theme}' e informacoes adicionais '{self.extra}', e crie a aula, categorizando as informações e atividades seguindo os títulos abaixo:\n"
            "- warm up: uma atividade de listar algo baseado no tema\n"
            "- question: uma pergunta que os alunos devem fazer entre si baseada no warm up\n"
            "- lead in: uma atividade baseada na lista criada anteriormente\n"
            "- example: um exemplo simples do lead in\n"
            "- pair work: outra pergunta para os alunos praticarem juntos\n"
            "- page: número da página no livro\n"
            "- production: tarefa para os alunos produzirem com o tema/gramática\n"
            "- example_production: um exemplo do production que criou anteriormente\n"
            f"- wrap-up: {prompt_wrap_up}\n"
            "- homework: dever de casa baseado no tema\n"
            "Responda com os títulos e conteúdo direto. Escreva os títulos exatamente como pedi. Sem explicações adicionais."
        )


        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(GEMINI_URL, json=payload, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Erro ao chamar Gemini: {response.status_code} {response.text}")

        response_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        self.text = response_text
        # print("🔍 RESPOSTA BRUTA DO GEMINI:\n", response_text)  # Veja como o modelo respondeu
        return self.parse_response_to_dict(response_text)

    def parse_response_to_dict(self, text):
        keys = {
            "warm_up": ["warm up"],
            "question": ["question"],
            "lead_in": ["lead in"],
            "example": ["example"],
            "pair_work": ["pair work"],
            "page": ["page"],
            "production": ["production"],
            "example_production": ["example_production"],
            "wrap_up": ["wrap-up", "wrapup", "wrap_up"],
            "homework": ["homework"]
        }


        result = {k: "" for k in keys}
        current_key = None

        for line in text.splitlines():
            original_line = line.strip()
            cleaned_line = self.remove_markdown(original_line).lower()

            # Detecta se é um título
            matched = False
            for dict_key, patterns in keys.items():
                for pattern in patterns:
                    if cleaned_line.startswith(pattern):
                        current_key = dict_key
                        content = original_line.split(":", 1)[-1].strip()
                        result[current_key] = self.remove_markdown(content)
                        matched = True
                        break
                if matched:
                    break
            else:
                # Se não for título mas já estivermos numa seção, adiciona conteúdo
                if current_key:
                    result[current_key] += "\n" + self.remove_markdown(original_line)

        # print(result)
        return result
