**PM Copilot AI – Reasoning Agent for Project Management**
**Overview**

PM Copilot AI is an AI-powered Project Management Reasoning Agent that converts unstructured project updates into structured, actionable insights. It helps project managers quickly identify risks, generate tasks, estimate timeline impact, and communicate updates efficiently.

The system simulates intelligent agent behavior by applying multi-step reasoning over natural language inputs and producing structured outputs for decision-making.

**Problem Statement**

Project managers often receive unstructured and inconsistent project updates from multiple stakeholders. These updates are difficult to analyze quickly, leading to delays in identifying risks, blockers, and required actions.

This results in:

Delayed decision-making
Poor visibility of project health
Manual effort in reporting and communication
Increased risk of project delays
**Solution**

PM Copilot AI solves this by acting as an intelligent reasoning agent that:

Understands natural language project updates
Detects risks automatically
Extracts actionable tasks
Calculates project health score
Predicts timeline impact
Generates stakeholder-ready email summaries
**Features**
1. Risk Detection Engine

Identifies:

Schedule delays
QA/resource issues
Scope changes
Dependency blockers
2. Task Extraction

Automatically converts updates into actionable tasks such as:

Resolve blockers
Assign backup resources
Review client changes
Continue execution

3. Project Health Score
Starts at 100
Deducts based on severity of risks
Outputs status:
Healthy
At Risk
Critical

4. Timeline Impact Analysis
Estimates delay risk:

High risk → 6–10 days
Medium risk → 3–5 days
Low risk → minimal delay

5. Automated Email Generator

Generates structured stakeholder updates including:

Risks summary
Tasks list
Timeline impact
Recommendations

6. Streamlit Dashboard

Interactive UI to:

Input project updates
View AI analysis
Generate reports instantly

**Microsoft IQ Alignment**

This project aligns with Microsoft IQ principles:

**Work IQ:** Understands project context and workflows
**Foundry IQ:** Applies reasoning over structured + unstructured data
**Fabric IQ:** Produces structured outputs for reporting and analytics

**GitHub Copilot Usage**

GitHub Copilot was used as an AI pair programmer during development to:

Generate Python logic for risk detection
Structure modular functions
Improve code quality and readability
Accelerate Streamlit UI development

**Architecture**
User Input (Project Update)
        ↓
Streamlit UI
        ↓
PM Copilot AI Agent
   ├── Risk Detection
   ├── Task Extraction
   ├── Health Scoring
   ├── Timeline Analysis
   └── Email Generator
        ↓
Structured Output Dashboard
