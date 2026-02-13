from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI(title="Agentic AI Agents API")

# In-memory stores
agents_store: Dict[str, Dict[str, Any]] = {}
tools_store: Dict[str, Dict[str, Any]] = {}

class AgentCreate(BaseModel):
    name: str
    description: str = ""

class ToolCreate(BaseModel):
    name: str
    description: str = ""

class RunRequest(BaseModel):
    agent_name: str
    input: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to Agentic AI Agents API"}

@app.get("/agents")
async def list_agents():
    return list(agents_store.values())

@app.post("/agents")
async def create_agent(agent: AgentCreate):
    if agent.name in agents_store:
        raise HTTPException(status_code=400, detail="Agent already exists")
    agents_store[agent.name] = agent.dict()
    return agents_store[agent.name]

@app.get("/tools")
async def list_tools():
    return list(tools_store.values())

@app.post("/tools")
async def create_tool(tool: ToolCreate):
    if tool.name in tools_store:
        raise HTTPException(status_code=400, detail="Tool already exists")
    tools_store[tool.name] = tool.dict()
    return tools_store[tool.name]

@app.post("/runs")
async def run_agent(req: RunRequest):
    if req.agent_name not in agents_store:
        raise HTTPException(status_code=404, detail="Agent not found")
    # Simple echo response; integrate with agent runtime later
    return {"agent": req.agent_name, "input": req.input, "output": f"Echo: {req.input}"}
