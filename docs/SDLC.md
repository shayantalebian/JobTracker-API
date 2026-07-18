# 🔄 Software Development Life Cycle (SDLC)

For JobTrackr API, we utilize an **Iterative and Incremental Agile** approach, heavily optimized for an AI-Augmented Development workflow.

1. **Requirement Analysis & Vibe Definition:** Understanding the "why" and "what" before touching code. Leveraging LLMs (Gemini, Claude) to brainstorm and structure requirements.
2. **System Design:** Drafting data flow, database schemas, and API contracts.
3. **Implementation (Vibe Coding):**
   - Writing code iteratively.
   - Deeply analyzing and understanding the generated/written code.
   - Refactoring immediately for maintainability.
4. **Testing:** Local testing via Bruno/Swagger UI. Transitioning to automated `pytest` in Phase 2.
5. **Deployment (Local/Containerized):** Ensuring the application runs flawlessly in a Dockerized environment to guarantee "works on my machine" translates to "works everywhere".
6. **Review & Documentation:** Continuous updating of README and architectural docs as the system evolves.
