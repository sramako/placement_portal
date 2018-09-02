from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

"""
train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'abc'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'abc'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'abc'),
    ('My boss is horrible.', 'neg')
]
test = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]

cl = NaiveBayesClassifier(train)

# Classify some text
print(cl.classify("Their burgers are amazing."))  # "pos"
print(cl.classify("I don't like their pizza."))   # "neg"


# Classify a TextBlob
blob = TextBlob("The beer was amazing. But the hangover was horrible. "
                "My boss was not pleased.", classifier=cl)
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
cl.show_informative_features(5)
"""
file = open("NB/keys",'r')
count=0
train = []
test = []
for line in file:
    line = line[:-1]
    f = open("NB/"+str(count),'r')
    a = []
    for l in f:
        l = l[:-1]
        a.append(l)
    train.append((a[int(0.2*len(a)):],line))
    test.append((a[:int(0.5*len(a))],line))
    f.close()
    count+=1



cl.show_informative_features()
