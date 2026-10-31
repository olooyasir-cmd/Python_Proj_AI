# My First AI App

**Python for Everybody with AI - Level 1** | CloudWithShad | Get Skills Network | Shadrack Darku

Go from Python notebooks to a working, deployed AI application. You'll build a market assistant, a chatbot, a sales dashboard and a group capstone, then explain how your code works.

**Student:** _add your name_ | **Cohort:** _add your cohort_ | **Live app:** _add your URL after your first deployment_

## How the course runs

| Stage | What you do | Where |
|---|---|---|
| 1. Notebooks | Learn the Python foundations | [week1/notebooks/](week1/notebooks/) |
| 2. First script | Run Python from a file in VS Code | [week1/hello.py](week1/hello.py) |
| 3. Guided apps | Build the labs on your own, Meetings 1-7 | `week2/`, `week3/`, `week4/` |
| 4. Group capstone | Plan, build, deploy and present, Meetings 8-10 | [capstone/](capstone/) |

Folder names such as `week2` are build milestones, not calendar weeks. Follow the meeting numbers below. The full schedule is in the [10-meeting roadmap](docs/ROADMAP.md).

## Stage 1: Complete the notebooks first

Finish these in order before opening any lab. They run in Google Colab, Jupyter or VS Code, and they don't need an API key.

| Order | Notebook | You learn | Time |
|---:|---|---|---:|
| 1 | [Python Speaks](week1/notebooks/week1-deepdive-1-python-speaks.ipynb) | Variables, f-strings, string methods, `input()`, reading errors | ~45 min |
| 2 | [Think Like a Programmer](week1/notebooks/week1-deepdive-2-think-like-a-programmer.ipynb) | Lists, loops, decisions, dictionaries | ~50 min |
| 3 | [Week 1 Assignment](week1/notebooks/week1-assignment.ipynb) | Eight self-checking challenges | ~60 min |

Only these three notebooks are in this repository. If your instructor shares others, finish those before moving on too.

## Stage 2: Set up and run your first script

Follow [SETUP.md](SETUP.md) to get your own copy of the repository and install Python 3.12. On Windows PowerShell, the install looks like this:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

SETUP.md also covers macOS, Linux, Git Bash and blocked activation. Then check your setup and run your first script:

```bash
python -c "import streamlit, openai, pandas, coursekit; print('Imports OK')"
python week1/hello.py
```

Run every command from the repository root, with your environment active.

## Stage 3 and 4: Build the apps

Open the starter, complete its TODOs, then run it. Each TODO tells you how to approach the task and which notebook section can help. The [lab guide](docs/LABS.md) explains each meeting.

| Meeting | You build | Starter | If stuck |
|---:|---|---|---|
| 1 | Quantity and price logic | [week2/market_basics.py](week2/market_basics.py) | [solution](solutions/week2/market_basics.py) |
| 2 | Terminal AI assistant | [week2/assistant.py](week2/assistant.py) | [solution](solutions/week2/assistant.py) |
| 3 | First web app | [week2/app.py](week2/app.py) | [solution](solutions/week2/app.py) |
| 4 | Chatbot with memory | [week3/chatbot.py](week3/chatbot.py) | [solution](solutions/week3/chatbot.py) |
| 5 | Persona controls and first deployment | [week3/persona_bot.py](week3/persona_bot.py), [deployment guide](week5/DEPLOY.md) | [solution](solutions/week3/persona_bot.py) |
| 6 | Sales dashboard | [week4/dashboard.py](week4/dashboard.py) | [solution](solutions/week4/dashboard.py) |
| 7 | Questions about sales data | [week4/data_chat.py](week4/data_chat.py) | [solution](solutions/week4/data_chat.py) |
| 8-10 | Group capstone | [capstone/app.py](capstone/app.py), [capstone brief](capstone/README.md) | [example](solutions/capstone/app.py) |

Meetings 1 and 2 are terminal scripts. Later labs are web apps:

```bash
python week2/market_basics.py
python -m streamlit run week2/app.py
```

Press Ctrl+C to stop a web app before starting another. A starter that shows only a checklist is expected until you complete its TODOs.

## When you get stuck

1. Read the last line of the error, then find the line of code it points to.
2. Re-read the TODO and open the notebook section it names.
3. Read the matching meeting in the [lab guide](docs/LABS.md) and the [setup troubleshooting table](SETUP.md#troubleshooting).
4. Ask a classmate or your mentor, and share what you tried.
5. Open the file in `solutions/`. Read it, close it, then write your own version.

You'll have to explain your code in your capstone, so make sure you understand anything you borrow. The capstone solution is only an example: renaming it doesn't count as an independent project.

## Demo mode and live AI

Apps start in **demo mode**. It returns clearly labelled fixed responses, makes no API requests and needs no key. A demo response is not real AI, so it can't prove your app gets good answers.

**Live mode** needs a model ID approved by your instructor and your own API key. See [section 4 of SETUP.md](SETUP.md#4-enable-real-ai-deliberately).

Never put a real key in code, screenshots, chat or commits. If a key is exposed, revoke it with the provider, create a new one and tell your mentor. Once an app is public in live mode, visitors can spend your API credit, so read the [cost and access section](week5/DEPLOY.md#cost-and-access) before sharing it.

## Save your work

Commit after each working step, and check what you're adding first:

```bash
git status
git diff
git add week2/market_basics.py
git commit -m "Validate quantity in calculate_total"
git push
```

## What's in this repository

| Path | Purpose |
|---|---|
| `week1/` | Notebooks and your first script |
| `week2/`, `week3/`, `week4/` | Lab starters, unfinished on purpose |
| `week5/DEPLOY.md` | How to deploy your app |
| `capstone/` | Group project starter and brief, including marks |
| `solutions/` | One worked solution per starter, at the same path |
| `coursekit/` | Shared helpers for calculations, CSV checks, AI calls and app screens |
| `data/sales.csv` | Sample data for the dashboard labs |
| `docs/` | [Roadmap](docs/ROADMAP.md), [lab guide](docs/LABS.md) and [acceptance checks](docs/ACCEPTANCE.md) |
| `tests/` | Automated checks for the shared helpers and the assignment notebook |

## Your progress

- [ ] Notebooks: Deep Dive 1, Deep Dive 2 and the Week 1 Assignment
- [ ] Setup: environment works and `week1/hello.py` runs
- [ ] M1: market logic and a Git checkpoint
- [ ] M2: terminal assistant and first AI request
- [ ] M3: first Streamlit app
- [ ] M4: chatbot memory and reset
- [ ] M5: persona controls, first deployment and group formation
- [ ] M6: validated data dashboard
- [ ] M7: questions about calculated data facts
- [ ] M8: capstone skeleton and reviewed pull request
- [ ] M9: working capstone, tests and deployment
- [ ] M10: demo and individual explanation

## What counts as finished?

A useful app, a readable repository, checked inputs and failure states, a working deployment, and an explanation of your own contribution. Use the [acceptance checks](docs/ACCEPTANCE.md) to test your work.

The stack is Python, Streamlit, OpenAI, pandas and Git/GitHub. This is a learning app, not a hardened public AI service.
