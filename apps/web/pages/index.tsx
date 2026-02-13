import { useEffect, useState } from 'react';

export default function Home() {
  const [agents, setAgents] = useState<{ name: string; description?: string }[]>([]);
  const [selectedAgent, setSelectedAgent] = useState('');
  const [message, setMessage] = useState('');
  const [output, setOutput] = useState<string | null>(null);

  useEffect(() => {
    fetch('/api/agents')
      .then(res => res.json())
      .then(data => setAgents(data))
      .catch(err => console.error(err));
  }, []);

  const handleRun = async () => {
    if (!selectedAgent || !message) return;
    try {
      const res = await fetch('/api/runs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ agent_name: selectedAgent, input: message }),
      });
      const data = await res.json();
      setOutput(data.output);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <main style={{ padding: '2rem' }}>
      <h1>Agentic AI Studio</h1>
      <p>Create and manage your agents.</p>
      <h2>Agents</h2>
      <ul>
        {agents.map((agent) => (
          <li key={agent.name}>
            {agent.name}: {agent.description}
          </li>
        ))}
      </ul>
      <h2>Run an Agent</h2>
      <div>
        <label>
          Select agent:
          <select value={selectedAgent} onChange={(e) => setSelectedAgent(e.target.value)}>
            <option value="">-- Select --</option>
            {agents.map((agent) => (
              <option key={agent.name} value={agent.name}>
                {agent.name}
              </option>
            ))}
          </select>
        </label>
      </div>
      <div>
        <label>
          Message:
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            style={{ width: '300px', marginLeft: '0.5rem' }}
          />
        </label>
      </div>
      <button onClick={handleRun} style={{ marginTop: '1rem' }}>
        Run
      </button>
      {output && (
        <div style={{ marginTop: '1rem' }}>
          <strong>Output:</strong> {output}
        </div>
      )}
    </main>
  );
}
