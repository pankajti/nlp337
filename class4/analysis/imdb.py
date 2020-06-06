data_path = r'/Users/pankaj/dev/git/smu/nlp337/class4/data/sentiment labelled sentences/amazon_cells_labelled.txt'
import re

data = []
labels = []
with open(data_path, 'r') as f :
    for line in f.readlines():
        match = re.search('\d$', line)
        data.append(line[:match.start()].strip())
        labels.append(line[match.start():].strip())


print(data)

from sklearn import *
from tensorflow import keras as keras
from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(num_words = 2000)
tokenizer.fit_on_texts(data)
sequences = tokenizer.texts_to_sequences(data)
one_hot_results = tokenizer.texts_to_matrix(data , mode = 'binary')


print(sequences)


