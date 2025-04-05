from crewai import Crew, Task
from agents.reader_agent import reader_agent
from agents.doc_agent import doc_agent
from agents.improvement_agent import improvement_agent

from dotenv import load_dotenv
load_dotenv()

import os, json

# Leitura dos JSONs
jsons = []
for file in os.listdir("data/pipelines"):
    with open(f"data/pipelines/{file}") as f:
        jsons.append(f.read())

# Tasks
read_task = Task(
    description="Ler e analisar os seguintes arquivos JSON de pipelines e datasets do Azure Data Factory: " + str(jsons),
    expected_output="Resumo técnico do que cada pipeline e dataset faz.",
    agent=reader_agent
)

doc_task = Task(
    description="A partir do resumo técnico, gerar uma documentação clara em Markdown explicando os pipelines e datasets.",
    expected_output="Seções em Markdown explicando cada pipeline, dataset e suas relações.",
    agent=doc_agent
)

improvement_task = Task(
    description="A partir da documentação, sugerir melhorias práticas para o ambiente de Data Factory.",
    expected_output="Lista de sugestões técnicas para melhorar o ambiente de ADF.",
    agent=improvement_agent
)

# Orquestração
crew = Crew(
    agents=[reader_agent, doc_agent, improvement_agent],
    tasks=[read_task, doc_task, improvement_task],
    verbose=True
)

result = crew.run()

# Salvar output
with open("output/adf_assessment.md", "w") as f:
    f.write(result)
