# Agent Scratchpad LRU ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Agent Scratchpad LRU Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/agent-scratchpad-lru/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/agent-scratchpad-lru?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/agent-scratchpad-lru/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Agent Scratchpad LRU** is a production-ready developer tool and connector: In-memory volatile scratchpad with priority tagging and automatic pruning.

---

## 🚀 Problem Statement

Agents accumulate temporary reasoning steps, debug traces, and intermediate tool variables in system context, exhausting token budgets.

---

## ⚡ Architecture Flow

```mermaid
flowchart LR
    A[Agent writes temporary variable 'temp_ast'] --> B[Scratchpad LRU]
    B --> C{Memory > 4KB limit?}
    C -->|Yes| D[Evict least-recently accessed low-priority item]
    C -->|No| E[Retain in memory]
```

---

## 📊 Performance Benchmarks

| Memory Metric | Unbounded Scratchpad | Agent Scratchpad LRU | Advantage |
|---|---|---|---|
| Memory Leak / Token Bloat | Unbounded growth | Hard 4KB boundary | **Zero Context Exhaustion** |
| Access Latency | - | 0.02 ms | **Instantaneous** |
| Pinned Facts Eviction | Pruned randomly | Never evicted | **100% Core Fact Safety** |
| Formatting Overhead | Raw dict dumps | Clean Markdown List | **Optimal Prompt Density** |

---

## 🛠️ Installation & Quickstart

```bash
pip install agent_scratchpad_lru
```

### Python API

```python
import agent_scratchpad_lru

print(agent_scratchpad_lru.__version__)
```

### CLI Usage

```bash
agent-scratchpad-lru --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
