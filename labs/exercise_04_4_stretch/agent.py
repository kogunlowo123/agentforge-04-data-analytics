"""AgentForge Exercise 04.4 — Data & Analytics Agents (stretch)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from core.agent_base import AgentBase

def main():
    agent = AgentBase(name="ex-04-4", instruction="You are a Data & Analytics Agents agent.")
    print(f"Exercise 04.4 ready: {agent.name}")

if __name__ == "__main__":
    main()
