import string
from collections import Counter
import matplotlib.pyplot as plt
from googletrans import Translator
import webbrowser
translator = Translator()

def detect_language(text):
    hindi_range = (0x0900, 0x097F)  # Hindi Unicode Range
    english_range = (0x0041, 0x007A)  # English Unicode Range (basic Latin characters)

    hindi_count = 0
    english_count = 0

    for char in text:
        char_code = ord(char)
        if hindi_range[0] <= char_code <= hindi_range[1]:
            hindi_count += 1
        elif english_range[0] <= char_code <= english_range[1]:
            english_count += 1

    if hindi_count > english_count:
        return "Hindi"
    elif english_count > hindi_count:
        return "English"
    else:
        return "Indeterminate"


# Read the text from the file
text = open(r"C:\Users\waghb\OneDrive\Desktop\pbl 2024\venv\output_file.txt", encoding='utf-8').read()

# Lowercase conversion
lower_case = text.lower()

# Removing punctuation
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Tokenizing
token_text = cleaned_text.split()

# Define stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = [word for word in token_text if word not in stop_words]

# Extracting emotions
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)
            print(emotion)
print(emotion_list)
# Translate comments if the language is not English
def translate_comments(comment_list):
    translated_comments = []
    for comment in comment_list:
        # Check if the comment is in Hindi
        if detect_language(comment) == 'Hindi':
            translated_comment = translator.translate(comment, src='hi', dest='en').text
            translated_comments.append(translated_comment)
        else:
            translated_comments.append(comment)
    return translated_comments

translated_emotion_list = translate_comments(emotion_list)

# Count emotions
emotion_counter = Counter(translated_emotion_list)

# Plot emotions
fig, axl = plt.subplots()
axl.bar(emotion_counter.keys(), emotion_counter.values())
fig.autofmt_xdate()
plt.savefig(r'templates\graph.png')
#plt.show()

def open_html_file(file_path):
    webbrowser.open(file_path)

if __name__ == "__main__":
    html_file_path = r"templates\result.html"
    open_html_file(html_file_path)

if __name__ == "__main__":
    html_file_path = r"templates\index.html"
    open_html_file(html_file_path)
