# Algorithmic Codex

This repository serves as a centralized reference library for functioning code snippets, algorithmic patterns, and system design principles. It is designed to act as a compendium of knowledge for rapid retrieval and implementation in future technical designs.

---

## 🔗 Project Links
* **Reference Site:** [phuchduong.github.io/algorithmic-codex/](https://phuchduong.github.io/algorithmic-codex/)
* **BTC Price History:** [phuchduong.github.io/algorithmic-codex/btc_dt/](https://phuchduong.github.io/algorithmic-codex/btc_dt/)
* **Source Code:** [github.com/phuchduong/algorithmic-codex](https://github.com/phuchduong/algorithmic-codex)

## 👤 Author
**Phuc Duong**
* **GitHub:** [@phuchduong](https://github.com/phuchduong)
* **LinkedIn:** [in/phuchduong](https://www.linkedin.com/in/phuchduong/)

---

## 🎯 Objectives
The Codex is being developed to store and organize:

* **Algorithmic Patterns:** Python implementations of core data structures and LeetCode-style problem-solving logic.
* **SQL References:** A collection of optimized queries, window functions, and data transformation snippets.
* **System Design:** Documentation and blueprints for scalable architecture and distributed systems.
* **Coding Boilerplates:** Production-ready functions for recurring engineering tasks.

### 📈 Financial Automation
* **yfinance Utilities:** Production-ready scripts to extract historical Bitcoin (BTC) price data, including yearly closing summaries and full historical exports to CSV.
* **BTC Visualization (btc_dt):** A web-based dashboard utilizing D3.js and DataTables to visualize historical Bitcoin market trends directly from CSV exports.

### 🛠️ Developer Tooling
* **Environment Setup:** PowerShell scripts for streamlined Python installations using `winget`.
* **Context Generation:** Custom automation tools to generate repository snapshots for AI-assisted development.

---

## 🏗️ Project Structure
```text
./
├── btc_dt/              # Bitcoin price dashboard and local server tools
│   ├── index.html       # D3.js and DataTables visualization interface
│   └── start_local_server_example.sh
├── LeetCode 75/        # Logic patterns and string manipulations
├── SQL 50/             # Optimized database queries
├── Python/
│   ├── yfinance/       # Market data extraction scripts
│   └── setup/          # Environment configuration scripts
└── context_generator.py # Repository documentation automation