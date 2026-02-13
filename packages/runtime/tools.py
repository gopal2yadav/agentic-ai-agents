from typing import Callable, Any, Dict

class Tool:
    """Base class for tools that agents can use."""

    def __init__(self, name: str, func: Callable[..., Any], description: str = ""):
        self.name = name
        self.func = func
        self.description = description

    def __call__(self, *args, **kwargs) -> Any:
        return self.func(*args, **kwargs)


class ToolRegistry:
    """Registry to manage available tools."""

    def __init__(self):
        self.tools: Dict[str, Tool] = {}

    def register(self, tool: Tool):
        self.tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        return self.tools.get(name)
