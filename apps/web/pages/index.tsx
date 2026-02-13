import { useEffect, useState } from 'react';

export default function Home() {
  const [agents, setAgents] = useState([]);

  useEffect(() => {
    fetch('/api/agents')
      .then((res) => res.json())
      .then((data) => setAgents(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <main style={{ padding: '2rem' }}>
      <h1>Agentic AI Studio</h1>
      <p>Create and manage your agents.</p>
      <h2>Agents</h2>
      <ul>
        {agents.map((agent: any) => (
          <li key={agent.name}>{agent.name}: {agent.description}</li>
        ))}
      </ul>
    </main>
  );
}
