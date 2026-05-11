# Quickstart

## 1. Create the GitHub repo

Create a new public repository named:

```text
ai-evaluation-workbench
```

Suggested repo description:

```text
A lightweight GenAI evaluation framework for product managers to define quality, detect failures, and make launch decisions using synthetic data.
```

Suggested topics:

```text
ai-product-management, llm-evaluation, genai, product-leadership, responsible-ai, streamlit, synthetic-data
```

## 2. Push this starter kit

```bash
cd ai-evaluation-workbench
git init
git add .
git commit -m "Initial AI evaluation workbench"
git branch -M main
git remote add origin https://github.com/<your-username>/ai-evaluation-workbench.git
git push -u origin main
```

## 3. Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python evals/scoring.py
streamlit run app/app.py
```

## 4. What to do before pinning this repo

- Add one screenshot to `assets/`
- Add a short demo GIF if possible
- Replace `coming soon` links in your profile README with this repo link
- Add a 1-paragraph LinkedIn post explaining the product problem
