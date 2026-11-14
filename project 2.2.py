
import string

# Read text file
with open("sample.txt", "r") as file:
    text = file.read()

# Convert to lowercase
text = text.lower()

# Remove punctuation
for symbol in string.punctuation:
    text = text.replace(symbol, "")

# Split into words
words = text.split()

# Count words
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Sort by frequency
sorted_words = sorted(
    word_count.items(),
    key=lambda x: x[1],
    reverse=True
)

# Display result
print("Word Count Results")

for word, count in sorted_words:
    print(word, ":", count)

print("Total Words:", len(words))
