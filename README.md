# MUNEEB

**Applied AI Developer building evaluated models, local inference systems, and complete software products.**

I build AI systems from the dataset upward: preparing training data, fine-tuning models, evaluating their behavior, and integrating them into usable products.
My work also covers secure APIs, automation, local-first software, SaaS dashboards, and algorithm-driven desktop applications.

[Portfolio](https://muneeb-anjum.vercel.app/) / [LinkedIn](https://linkedin.com/in/muneebanjum335) / [Email](mailto:muneeb.anjum0@gmail.com)

Islamabad, Pakistan

```ts
const muneeb = {
  builds: [
    "evaluated AI systems",
    "local-first applications",
    "secure APIs",
    "data-driven products"
  ],
  worksWith: [
    "datasets",
    "fine-tuning",
    "retrieval",
    "inference",
    "product engineering"
  ],
  basedIn: "Islamabad, Pakistan"
};
```

## What I Build

### Model and Data Systems

Dataset generation and curation, LoRA and QLoRA fine-tuning, model evaluation, hallucination and schema testing, embeddings, retrieval, and local model deployment.

### Product Engineering

React and Next.js interfaces, FastAPI and Flask APIs, Go services, databases, authentication, dashboards, and production-oriented application structure.

### Automation and Security

Browser automation, OAuth integrations, encrypted credentials, signed HTTP-only sessions, backend-controlled data access, and dependency and repository checks.

### Algorithms and Native Applications

C++, OpenGL, Java, pathfinding, graph algorithms, sorting visualizations, and event-driven desktop applications.

## Systems I Have Built

### [FaultLine](https://github.com/muneeb-anjum0/FaultLine)

Release-risk intelligence that converts support signals into structured incident information, then correlates them with modules, services, releases, and similar incidents.

**Stack:** Qwen 3 8B, QLoRA, custom datasets, evaluation gates, RAG, pgvector, FastAPI, Next.js, PostgreSQL, Redis, Docker.

**Why it matters:** the fine-tuned model is held behind evaluation gates and is not activated unless it beats the base model on schema, hallucination, and task-specific checks.

### [AudioAware](https://github.com/muneeb-anjum0/AudioAware)

Local audio-authenticity screening for speech and environmental audio.

**Stack:** WavLM, Audio Spectrogram Transformer, WebRTC VAD, PyTorch, Hugging Face, FastAPI, React.

**Why it matters:** a speech-ratio router sends speech-heavy clips to WavLM and environmental clips to an AST branch, returning probabilistic screening results rather than legal proof.

### [Drift](https://github.com/muneeb-anjum0/Drift)

Requirements-drift and scope-control system for comparing approved requirements with changing client intent.

**Stack:** Qwen 2.5 7B, LoRA, GGUF, llama.cpp, Go, Gin, FastAPI, React, MongoDB, Docker.

**Why it matters:** it turns changing requests into reviewable change decisions so teams can separate accepted scope from new work.

### [ClassWire](https://github.com/muneeb-anjum0/ClassWire)

Secure timetable automation system that reads changing Gmail timetable formats and produces organized schedules.

**Stack:** Google OAuth, Gmail integration, Flask, React, Firestore, encrypted credentials, signed HTTP-only sessions, CI security checks.

**Why it matters:** the frontend stays away from Firestore while Flask controls data access, sessions, parsing, and encrypted Gmail credentials.

### [North-Grid](https://github.com/muneeb-anjum0/North-Grid)

Polished SaaS operations dashboard for revenue movement, customer health, support pressure, product demand, and activity.

**Stack:** Next.js, TypeScript, Tailwind, Zod, React Hook Form, Recharts, Vitest, Playwright.

**Why it matters:** it demonstrates connected product workflows across dashboard, customer, ticket, request, activity, and export surfaces rather than isolated screens.

### [Path-Finder](https://github.com/muneeb-anjum0/Path-Finder)

C++ maze-generation and pathfinding visualizer with step-by-step execution.

**Stack:** C++, OpenGL, Dear ImGui, DFS, BFS, Dijkstra, A*, Prim, Kruskal, Disjoint Set Union.

**Why it matters:** it visualizes algorithm exploration, maze generation, obstacles, and reconstructed paths through an interactive native application.

## Technology

| Area | Tools |
| --- | --- |
| AI and Data | PyTorch, Hugging Face, Qwen, LoRA / QLoRA, RAG, pgvector, Ollama, llama.cpp, Pandas, NumPy |
| Product Development | React, Next.js, TypeScript, Vite, Tailwind CSS, FastAPI, Flask, Go, Gin |
| Data and Infrastructure | PostgreSQL, MongoDB, Firestore, Redis, SQLite, Docker, GitHub Actions |
| Systems and Fundamentals | C++, OpenGL, Java, Playwright, pytest, Vitest |

## GitHub Activity

The profile is useful without external cards, but these live views show current public GitHub activity when the services are available.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=muneeb-anjum0&amp;show_icons=true&amp;include_all_commits=true&amp;count_private=true&amp;rank_icon=github&amp;hide_border=true&amp;bg_color=00000000&amp;title_color=58a6ff&amp;text_color=c9d1d9&amp;icon_color=79c0ff">
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api?username=muneeb-anjum0&amp;show_icons=true&amp;include_all_commits=true&amp;count_private=true&amp;rank_icon=github&amp;hide_border=true&amp;bg_color=00000000&amp;title_color=0969da&amp;text_color=24292f&amp;icon_color=0969da">
  <img alt="Dynamic GitHub statistics for muneeb-anjum0" src="https://github-readme-stats.vercel.app/api?username=muneeb-anjum0&amp;show_icons=true&amp;include_all_commits=true&amp;count_private=true&amp;rank_icon=github&amp;hide_border=true&amp;bg_color=00000000&amp;title_color=0969da&amp;text_color=24292f&amp;icon_color=0969da" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=muneeb-anjum0&amp;custom_title=Contribution%20Activity&amp;hide_border=true&amp;bg_color=00000000&amp;color=8b949e&amp;line=58a6ff&amp;point=79c0ff&amp;area=false">
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=muneeb-anjum0&amp;custom_title=Contribution%20Activity&amp;hide_border=true&amp;bg_color=00000000&amp;color=57606a&amp;line=0969da&amp;point=0969da&amp;area=false">
  <img alt="Contribution activity graph for muneeb-anjum0" src="https://github-readme-activity-graph.vercel.app/graph?username=muneeb-anjum0&amp;custom_title=Contribution%20Activity&amp;hide_border=true&amp;bg_color=00000000&amp;color=57606a&amp;line=0969da&amp;point=0969da&amp;area=false" width="100%">
</picture>

## Development Principles

- Train against measurable failure cases.
- Keep inference replaceable and evaluation-driven.
- Protect credentials and user data by default.
- Build the product around the workflow, not around the model.

`datasets -> models -> evaluation -> products`
