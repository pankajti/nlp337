import matplotlib.pyplot as plt
import numpy as np

words = []
word_targets= []
sentences=[]
senetence_targets= []


with open('../data/train.txt') as f:
    sentence = []
    senetence_target = []

    for l in f.readlines():
        if len(l.strip())==0:
            print("end of sentence")
            sentences.append(sentence)
            senetence_targets.append(senetence_target)
            sentence=[]
            senetence_target = []

            continue

        word_parts = l.split(" ")
        word = word_parts[0]
        words.append(word)
        word_targets.append(word_parts[-1].strip())
        sentence.append(word)
        senetence_target.append(word_parts[-1].strip())

target_index = {}
word_index = {}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2

idx =3

for word in words:
    if word not in word_index:
        word_index[word] = idx
        idx= idx+1


target_index["<PAD>"] = 0
target_index["<START>"] = 1
target_index["<UNK>"] = 2

idx =3
for word_target in word_targets:
    if word_target not in target_index:
        target_index[word_target] = idx
        idx= idx+1

sentence_lengths = list(map(lambda x:len(x) , sentences))
plt.hist(sentence_lengths, bins=100)
plt.show()

sentence_length = 30
sentence_indexes = []

for sent in sentences:
    sent_idx=[]
    for word in sent:
        index = word_index[word]
        sent_idx.append(index)
    sentence_indexes.append(sent_idx)

senetence_target_indexes = []

for target in senetence_targets:
    sent_target_idx=[]
    for t in target:
        index = target_index[t]
        sent_target_idx.append(index)
    senetence_target_indexes.append(sent_target_idx)

padded_sentence_indexes = []
padded_sentence_target_indexes = []

for sent_idx in sentence_indexes:
    padded_sentence_index=[]
    pad_len = 30-len(sent_idx)
    padded_sentence_index[0:pad_len] = pad_len*[word_index['<PAD>']]
    padded_sentence_index.extend(sent_idx[:30])
    padded_sentence_indexes.append(padded_sentence_index)

for sent_target_idx in senetence_target_indexes:
    padded_sentence_target_index=[]
    pad_len = 30-len(sent_target_idx)
    padded_sentence_target_index[0:pad_len] = pad_len*[target_index['<PAD>']]
    padded_sentence_target_index.extend(sent_target_idx[:30])
    padded_sentence_target_indexes.append(padded_sentence_target_index)


import numpy
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import  LSTM as LSTM, SimpleRNN,  GRU,TimeDistributed
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing import sequence


X_train = np.array(padded_sentence_indexes, dtype = float)
y_train = np.array(padded_sentence_target_indexes,  dtype = float)

X_train= X_train.reshape(1,X_train.shape[0], X_train.shape[1])
y_train= y_train.reshape(1,y_train.shape[0], y_train.shape[1])

embedding_vecor_length = 80
model2 = Sequential()
model2.add(LSTM(1024, activation='relu', return_sequences=True))
model2.add(TimeDistributed(Dense(30)))

model2.compile( loss= 'mse' , optimizer='adam' )

model2.fit( X_train, y_train, epochs=3, batch_size=64)

print(model2.summary())

print("done")