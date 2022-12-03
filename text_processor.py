from collections import Counter
import string
import nltk
nltk.download('omw-1.4')


def get_most_common_words(data, text_col, by, count):
    common_words = {}    
    for val in data[by].unique():
        df = data[data[by] == val]
        common_words[f"{by} = {val}"] = Counter(" ".join(df[text_col]).split()).most_common(count)
    return common_words


def process(text, lemmatize=True):
    stop_words = nltk.corpus.stopwords.words("english")
    text = text.translate(str.maketrans(' ', ' ', string.punctuation))
    tokens = text.split()
    tokens = [t.strip().lower() for t in tokens if t.strip().lower() not in stop_words]
    tokens = [nltk.stem.wordnet.WordNetLemmatizer().lemmatize(t) for t in tokens]
    
    return ' '.join(tokens)

