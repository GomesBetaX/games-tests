import requests
import re

# Gemini config
GEMINI_API_KEY = "AIzaSyAwtSlrpGOJVTILUpQD6Zv5J_1VqdNhF6E"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

class GPT:

    def __init__(self):
        self.theme = ""
        self.plan = self.fetch_lesson_plan(self.theme)
        # print("\n📘 PLANO FORMATADO:")
        # for k, v in self.plan.items():
        #     print(f"\n{k}\n{v}")

    def remove_markdown(self, text):
        return re.sub(r'[*_`]', '', text).strip()

    def fetch_lesson_plan(self, theme):
        prompt = (
            "Você é um professor com muita experiência, e precisa criar uma aula baseada no Bloom's Taxonomy e CRISP. "
            f"Pegue o tema da aula: '{theme}', e crie a aula, categorizando as informações e atividades seguindo os títulos abaixo:\n"
            "- warm up: uma atividade de listar algo baseado no tema\n"
            "- question: uma pergunta a ser feita a outros 2 alunos sobre a lista montada anteriormente\n"
            "- lead_in: algo a ser feito com a lista criada anteriormente\n"
            "- page: número da página no livro\n"
            "- production: algo a ser criado utilizando o tema/gramática\n"
            "- wrap-up: três frases de review, com duas opções cada, baseadas no tema\n"
            "- homework: dever de casa baseado no tema\n\n"
            "Responda com os títulos e conteúdo direto. Mantenha o título EXATEMENTE como na chave. Sem explicações adicionais."
        )

        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        headers = {"Content-Type": "application/json"}

        response = requests.post(GEMINI_URL, json=payload, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Erro ao chamar Gemini: {response.status_code} {response.text}")

        response_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        print("🔍 RESPOSTA BRUTA DO GEMINI:\n", response_text)  # Veja como o modelo respondeu
        return self.parse_response_to_dict(response_text)

    def parse_response_to_dict(self, text):
        keys = {
            "warm_up:": ["warm up"],
            "question:": ["question"],
            "lead_in:": ["lead in"],
            "page:": ["page"],
            "production:": ["production"],
            "wrap_up": ["wrap-up"],
            "homework:": ["homework"]
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

        print(result)
        return result
