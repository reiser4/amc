
from mcp23017 import MCP23017

mcp23017 = MCP23017(1)


mcp23017.writePin("A", 0, 0)
mcp23017.writePin("A", 1, 0)
mcp23017.writePin("A", 2, 0)
mcp23017.writePin("A", 3, 0)
mcp23017.writePin("A", 4, 0)
mcp23017.writePin("A", 5, 0)
mcp23017.writePin("A", 6, 0)
mcp23017.writePin("A", 7, 0)
mcp23017.writePin("B", 0, 0)
mcp23017.writePin("B", 1, 0)
mcp23017.writePin("B", 2, 0)
mcp23017.writePin("B", 3, 0)
mcp23017.writePin("B", 4, 0)
mcp23017.writePin("B", 5, 0)
mcp23017.writePin("B", 6, 0)
mcp23017.writePin("B", 7, 0)

mcp23017.writePin("B", 0, 1)

mcp23017.writeData()
