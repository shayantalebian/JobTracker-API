# Git Commit Message Convention

This project adheres to the [Conventional Commits](https://www.conventionalcommits.org/) standard. A well-structured git history makes debugging, code reviews, and automated changelog generation much easier.

## 📌 Commit Message Structure

```text
<type>(<scope>): <short description>

[optional body giving more details]

## 🛠️ Allowed Types

*   **`feat`**: A new feature (e.g., adding a new API endpoint).
*   **`fix`**: A bug fix (e.g., handling a database connection timeout).
*   **`docs`**: Documentation only changes (README, architecture files).
*   **`style`**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc.).
*   **`refactor`**: A code change that neither fixes a bug nor adds a feature (e.g., renaming variables, restructuring folders).
*   **`perf`**: A code change that improves performance.
*   **`test`**: Adding missing tests or correcting existing tests (Pytest).
*   **`chore`**: Changes to the build process, auxiliary tools, or dependency updates (`uv`, Dockerfile).

## 📍 Scope (Optional but recommended)
The scope provides context on which part of the codebase is affected.
*   *Examples:* `auth`, `database`, `docker`, `models`, `routes`, `ui`.

## ✅ Good vs. Bad Examples

### Bad ❌
*   `added new stuff to db`
*   `fix bug`
*   `wip`
*   `update readme`

### Good ✅
*   `feat(models): create JobApplication SQLAlchemy model`
*   `fix(auth): resolve JWT token expiration issue`
*   `chore(deps): update fastapi to version 0.110.0`
*   `docs(readme): add system design navigation buttons`

## 💡 Best Practices
1.  Use the **imperative mood** in the description ("add feature" not "added feature").
2.  Keep the first line under **50-72 characters**.
3.  Do not end the short description with a period.
4.  Use the body (optional) to explain **what** and **why**, not **how** (the code explains how).


---
```
