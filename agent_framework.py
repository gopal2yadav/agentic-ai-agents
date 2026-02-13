class Agent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def handle(self, message: str, context: dict) -> str:
        """
        Placeholder for agent-specific logic.
        """
        return f"{self.name} ({self.role}) received: {message}"


class Orchestrator:
    def __init__(self, agents):
        self.agents = agents

    def run(self, task: str):
        context = {}
        responses = []
        for agent in self.agents:
            responses.append(agent.handle(task, context))
        return responses


if __name__ == '__main__':
    agents = [
        Agent('Retriever', 'data retrieval'),
        Agent('Reasoner', 'reasoning'),
        Agent('Summarizer', 'summarization')
    ]
    orchestrator = Orchestrator(agents)
    task = 'Describe the concept of reinforcement learning.'
    results = orchestrator.run(task)
    for r in results:
        print(r)
