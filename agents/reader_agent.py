from crewai import Agent

reader_agent = Agent(
    role="ADF Pipeline Reader",
    goal="Analisar arquivos JSON de pipelines e datasets e extrair informações relevantes.",
    backstory="Especialista em estruturas de dados do Azure Data Factory.",
    verbose=True
)
