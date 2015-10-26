
from mcp23017 import MCP23017

mcp23017 = MCP23017(1)
v=0
mcp23017.writePin("A", 0, v)
mcp23017.writePin("A", 1, v)
mcp23017.writePin("A", 2, v)
mcp23017.writePin("A", 3, v)
mcp23017.writePin("A", 4, v)
mcp23017.writePin("A", 5, v)
mcp23017.writePin("A", 6, v)
mcp23017.writePin("A", 7, v)
mcp23017.writePin("B", 0, v)
mcp23017.writePin("B", 1, v)
mcp23017.writePin("B", 2, v)
mcp23017.writePin("B", 3, v)
mcp23017.writePin("B", 4, v)
mcp23017.writePin("B", 5, v)
mcp23017.writePin("B", 6, v)
mcp23017.writePin("B", 7, v)

mcp23017.writePin("B", 3, 1)

mcp23017.writeData()
