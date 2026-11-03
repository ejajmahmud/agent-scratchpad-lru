"""Command-line interface for Agent Scratchpad LRU."""
import argparse
from .scratchpad import AgentScratchpad

def main():
    parser = argparse.ArgumentParser(description="Agent Scratchpad LRU CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate bounded LRU scratchpad")
    args = parser.parse_args()

    sp = AgentScratchpad(max_entries=3)
    sp.set("user_id", "42", pinned=True)
    sp.set("temp_query", "SELECT 1")
    sp.set("temp_calc", "100 * 2 = 200")
    sp.set("temp_extra", "Over budget item")

    print("Scratchpad memory formatted for prompt:")
    print(sp.format_for_prompt())

if __name__ == "__main__":
    main()
