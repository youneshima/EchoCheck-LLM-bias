# EchoCheck

A watchdog tool that measures how different AI models perceive and stereotype minority communities.

---

## Project Concept

**The Problem:**  
AI models learn from huge amounts of internet text, which often contains human bias. As a result, AI can repeat or even amplify stereotypes about different groups.

**Our Solution:**  
EchoCheck asks major AI models a set of tough, identical questions about several minority communities. It analyzes the answers for sentiment and bias, then displays the results on a simple dashboard. Anyone can see how fairly (or unfairly) these powerful systems represent our world.

---

## Implementation

**Pipeline:**

1. **Data Generation:**  
   We ask 10 carefully designed questions to three different AI models for four communities. This creates 120 unique text responses, saved in `generated_responses.json`.

2. **Sentiment Analysis:**  
   Each response is analyzed for sentiment using TextBlob. We average the scores for each community-model pair and save them in `final_scores.json`.

3. **Score Normalization:**  
   To make differences more visible, we stretch the scores to a wider range and save them in `stretched_scores.json`. This file powers the user interface.

---

## Technology Used

**Foundation Models:**
- Claude 3.5 Sonnet (Anthropic)
- DeepSeek-V2 (DeepSeek)
- Llama 3 70B Instruct (Meta)

**Services & Libraries:**
- LiteLLM (unified API gateway for models)
- Python (backend scripting)
- TextBlob (sentiment analysis)
- HTML, CSS, JavaScript (frontend UI)

---

## How to Evaluate This Project

**1. Setup**

Install the required Python libraries:
```bash
pip install openai textblob
```

**2. Run the Scripts (in order):**

- **Generate Raw Data:**  
  Calls the AI models 120 times.
  ```bash
  python generate_responses.py
  ```

- **Analyze Sentiment:**  
  Reads the raw text and creates `final_scores.json`.
  ```bash
  python analyze.py
  ```

- **Stretch Scores for UI:**  
  Reads `final_scores.json` and creates `stretched_scores.json`.
  ```bash
  python stretch_scores.py
  ```

**3. View the Dashboard**

Open `index.html` in your web browser. It will load `stretched_scores.json` and display the results.

---

**No special AWS setup is required. All model calls are made via LiteLLM.**
