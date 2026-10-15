# DATA SCIENCE - PROGRAM 10
# CASE STUDY: NAVARASA TEXT EMOTION DETECTION
# ============================================================
#
# AIM:
# ----
# To detect nine emotions (Navarasalu) from text messages
# using Machine Learning techniques.
#
# ============================================================

# ============================================================
# IMPORT REQUIRED LIBRARIES
# ============================================================

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ============================================================
# CREATE SAMPLE TRAINING DATA
# ============================================================

texts = [
    "I love my family",
    "I am laughing happily",
    "I feel sorry for him",
    "I am very angry",
    "I am brave and strong",
    "I am afraid of darkness",
    "This food is disgusting",
    "Wow this is amazing",
    "I feel peaceful and calm"
]

# Corresponding Navarasa labels

labels = [
    "Shringara - Love",
    "Hasya - Happiness",
    "Karuna - Compassion",
    "Raudra - Anger",
    "Veera - Courage",
    "Bhayanaka - Fear",
    "Bibhatsa - Disgust",
    "Adbhuta - Wonder",
    "Shanta - Peace"
]

# ============================================================
# DISPLAY TRAINING DATA
# ============================================================

print("=" * 60)
print("NAVARASA TRAINING DATA")
print("=" * 60)

for sentence, emotion in zip(texts, labels):
    print(f"Text: {sentence} --> Emotion: {emotion}")

# ============================================================
# TEXT VECTORIZATION
# ============================================================

vec = CountVectorizer()

X = vec.fit_transform(texts)

print("\n")
print("=" * 60)
print("VOCABULARY")
print("=" * 60)

print(vec.get_feature_names_out())

print("\n")
print("=" * 60)
print("VECTORIZED DATA")
print("=" * 60)

print(X.toarray())

# ============================================================
# TRAIN MACHINE LEARNING MODEL
# ============================================================

model = MultinomialNB()

model.fit(X, labels)

print("\nModel Training Completed Successfully")

# ============================================================
# TEST DATA
# ============================================================

new_text = ["I am feeling very peaceful today"]

print("\n")
print("=" * 60)
print("TEST SENTENCE")
print("=" * 60)

print(new_text)

# Convert test text into numerical representation

test = vec.transform(new_text)

print("\nVectorized Test Data:")
print(test.toarray())

# ============================================================
# PREDICTION
# ============================================================

prediction = model.predict(test)

print("\n")
print("=" * 60)
print("PREDICTED NAVARASA EMOTION")
print("=" * 60)

print(prediction[0])

# ============================================================
# ADDITIONAL TEST CASES
# ============================================================

sample_sentences = [
    "I love my friends",
    "I am laughing a lot",
    "I feel sorry for the poor child",
    "I am angry with you",
    "I am strong and brave",
    "I am scared of the ghost",
    "This food smells terrible",
    "Wow this is wonderful",
    "I feel calm and relaxed"
]

print("\n")
print("=" * 60)
print("MULTIPLE NAVARASA PREDICTIONS")
print("=" * 60)

for sentence in sample_sentences:

    # Convert text into vector

    sample_vector = vec.transform([sentence])

    # Predict emotion

    result = model.predict(sample_vector)

    print(f"{sentence} --> {result[0]}")

# ============================================================
# END OF PROGRAM
# ============================================================

print("\n")
print("=" * 60)
print("NAVARASA EMOTION DETECTION COMPLETED")
print("=" * 60) 