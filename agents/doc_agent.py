from crewai import Agent

doc_agent = Agent(
    role="Documentador Técnico",
    goal="Gerar documentação clara sobre o funcionamento dos pipelines e datasets.",
    backstory="Especialista em documentação técnica e pipelines de dados.",
    verbose=True
)
