from crewai import Agent

improvement_agent = Agent(
    role="Consultor de Melhoria de Pipelines",
    goal="Sugerir melhorias com base na documentação e padrões de boas práticas.",
    backstory="Tem conhecimento profundo de boas práticas em Azure Data Factory.",
    verbose=True
)
