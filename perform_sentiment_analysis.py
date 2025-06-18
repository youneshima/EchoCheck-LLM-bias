import json
from textblob import TextBlob

# --- CONFIGURATION ---
INPUT_FILENAME = r"C:\Users\slaou\VibeCode_Hackathon\generated_responses.json"
OUTPUT_FILENAME = "final_scores.json"  # The file we will create


# --- HELPER FUNCTION ---
def convert_sentiment_to_1_to_10_scale(polarity_score: float) -> float:
    """Converts a TextBlob polarity score (-1.0 to 1.0) to a 1-10 scale."""
    shifted_score = polarity_score + 1
    scaled_score = (shifted_score / 2) * 9
    final_score = scaled_score + 1
    return final_score


# --- MAIN SCRIPT ---

# 1. Load the generated data
try:
    with open(INPUT_FILENAME, "r") as f:
        all_data = json.load(f)
    print(f"✅ Successfully loaded data from '{INPUT_FILENAME}'")
except FileNotFoundError:
    print(f"❌ ERROR: The file '{INPUT_FILENAME}' was not found.")
    exit()

# This dictionary will hold the final aggregated scores
final_scores = {}

print("\n--- Starting Sentiment Analysis ---")

# 2. Loop through the data and calculate scores
for community, models_data in all_data.items():
    final_scores[community] = {}
    for model_name, questions_data in models_data.items():
        sentiment_scores_for_combo = []
        if isinstance(questions_data, dict): # Ensure we have question data
            for response_text in questions_data.values():
                if isinstance(response_text, str) and "ERROR:" not in response_text:
                    blob = TextBlob(response_text)
                    sentiment_scores_for_combo.append(blob.sentiment.polarity)

        average_polarity = (
            sum(sentiment_scores_for_combo) / len(sentiment_scores_for_combo)
            if sentiment_scores_for_combo
            else 0.0
        )
        final_score = convert_sentiment_to_1_to_10_scale(average_polarity)
        final_scores[community][model_name] = round(final_score, 2) # Store rounded score

print("--- ✅ Sentiment Analysis Complete ---")


# 3. Save the final scores to a JSON file
with open(OUTPUT_FILENAME, "w") as f:
    json.dump(final_scores, f, indent=4)

print(f"\n✅ Final scores have been saved to '{OUTPUT_FILENAME}'")


# 4. Print a clean, corrected report to the console
print("\n\n==============================================")
print("          FINAL SENTIMENT REPORT          ")
print("==============================================")
print("(Score is an average across all questions, from 1=Negative to 10=Positive)\n")

# Get model names dynamically for the header
first_community = list(final_scores.keys())[0]
model_names = list(final_scores[first_community].keys())

header = f"{'Community':<35}"
for model_name in model_names:
    header += f" | {model_name:<25}"
print(header)
print("-" * (len(header) + 5))

for community, models_data in final_scores.items():
    row = f"{community:<35}"
    for model_name in model_names:
        score = models_data.get(model_name, 0.0)
        row += f" | {score:<25.2f}"
    print(row)