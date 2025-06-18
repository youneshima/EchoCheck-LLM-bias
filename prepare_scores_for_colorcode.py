import json

# Input and output filenames
INPUT_FILE = r"C:\Users\slaou\VibeCode_Hackathon\final_scores.json"
OUTPUT_FILE = "stretched_scores.json"

# Set your desired new min and max
NEW_MIN = 4
NEW_MAX = 9

with open(INPUT_FILE, "r") as f:
    scores = json.load(f)

all_scores = [score for group in scores.values() for score in group.values()]
min_score = min(all_scores)
max_score = max(all_scores)

if max_score == min_score:
    stretched_scores = {k: {m: (NEW_MIN + NEW_MAX) / 2 for m in v} for k, v in scores.items()}
else:
    stretched_scores = {}
    for community, models in scores.items():
        stretched_scores[community] = {}
        for model, score in models.items():
            new_score = NEW_MIN + (NEW_MAX - NEW_MIN) * (score - min_score) / (max_score - min_score)
            stretched_scores[community][model] = round(new_score, 2)

with open(OUTPUT_FILE, "w") as f:
    json.dump(stretched_scores, f, indent=4)

print(f"Stretched scores saved to '{OUTPUT_FILE}'")