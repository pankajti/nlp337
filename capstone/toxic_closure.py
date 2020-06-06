# Select relations that have a mammal as hypo and hypernym
import pandas as pd
import re


nouns = pd.read_csv('nouns_and_adjectives_closure.csv')

# Extract the set of nouns that have "mammal.n.01" as a hypernym
toxic_set = set(nouns[nouns.id2 == 'fool.n.01'].id1.unique())
toxic_set.add('fool.n.01')

# Select relations that have a mammal as hypo and hypernym
toxic = nouns[nouns.id1.isin(toxic_set) & nouns.id2.isin(toxic_set)]

with open('toxic_filter.txt', 'r') as fin:
    filt = re.compile(f'({"|".join([l.strip() for l in fin.readlines()])})')


filtered_toxic = toxic[~toxic.id1.str.cat(' ' + toxic.id2).str.match(filt)]
print(filtered_toxic)