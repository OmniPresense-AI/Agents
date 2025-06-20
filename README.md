# ESG Agent

An AI agent system designed to provide comprehensive information and guidance about ESG (Environmental, Social, and Governance) standards, specifically focusing on SASB (Sustainability Accounting Standards Board) industry standards.

## Overview

This project implements a multi-agent system built using Google's Agent Development Kit (ADK) and CrewAI framework. The system leverages advanced AI models through LiteLlm integration to provide accurate and contextual information about sustainability standards, making it easier for organizations to understand and implement ESG requirements.

The architecture combines:
- Google's ADK for robust agent development and management
- CrewAI for advanced tool integration and agent orchestration
- LiteLlm for flexible model integration and API management
- OpenAI's GPT models for intelligent responses and analysis

## Features

- **Industry-Specific Standards**: Coverage of multiple industry sectors including:
  - Consumer Goods
  - Extractives & Minerals Processing
  - Financials
  - Food & Beverage
  - Health Care
  - Infrastructure
  - Renewable Resources & Alternative Energy
  - Resource Transformation
  - Services
  - Technology & Communications
  - Transportation

- **Intelligent Search**: Advanced semantic search capabilities across:
  - SASB Industry Standards
  - SASB Conceptual Framework
  - Application Guidance
  - Industry Classification Data

- **Multi-Agent Architecture**: Specialized agents for different industries and purposes:
  - Industry Finder Agent
  - Industry-Specific Standards Agents
  - File Search Capabilities

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Google Cloud credentials (for ADK)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/OmniPresense-AI/Agents.git
cd Agents
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
├── ESG/                       # Main agent implementations and tests
├── Tools/                     # File and web search utilities
├── Standards/                 # SASB standards PDFs, taxonomy, and data
├── Prompts/                   # Standardized agent instruction prompts
├── db/                        # (Database or persistent storage)
├── requirements.txt           # Project dependencies
└── README.md                  # This documentation
```

## Repository Contents

- **/Prompts/**
  Over 70 standardized markdown prompt files, each following a unified template for agent instructions. These cover every SASB industry, sector, and special agent (e.g., Industry Finder, ESG Orchestrator, Application Guidance).
  Each file is organized as:
  - `## Role`
  - `## Task`
  - `## Input`
  - `## Output`
  - `## Constrictions`
  - `## Capabilities`
  - `## Ambiguity handling`

- **/Standards/**
  The full set of SASB industry standards PDFs, the SASB Conceptual Framework, Application Guidance, taxonomy files, and supporting data (e.g., `SASB_Industry_Data.json`).

- **/ESG/**
  Main agent implementations (`agent.py`), initialization, and test data for industry classification.

- **/Tools/**
  Utility scripts for file and web search, supporting the agent system.

- **/db/**
  (Contents not listed, but likely for persistent storage or vector DBs.)

- **/requirements.txt**
  Python dependencies for the project.

- **README.md**
  This documentation.

## Usage

The system can be used to:
1. Identify relevant industry standards for a specific business
2. Get detailed information about specific ESG metrics and requirements
3. Search through the complete SASB standards library
4. Access industry-specific guidance and best practices
