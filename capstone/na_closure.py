import re
import pandas
from nltk.corpus import wordnet as wn
from tqdm import tqdm
try:
    wn.all_synsets
except LookupError as e:
    import nltk
    nltk.download('wordnet')

# make sure each edge is included only once
edges = set()
poss = ['n']
for p in poss :
    for synset in tqdm(wn.all_synsets(pos= p)):
        # write the transitive closure of all hypernyms of a synset to file
        for hyper in synset.closure(lambda s: s.hypernyms()):
            edges.add((synset.name(), hyper.name()))

        # also write transitive closure for all instances of a synset
        for instance in synset.instance_hyponyms():
            for hyper in instance.closure(lambda s: s.instance_hypernyms()):
                edges.add((instance.name(), hyper.name()))
                for h in hyper.closure(lambda s: s.hypernyms()):
                    edges.add((instance.name(), h.name()))

nouns_and_adjectives  = pandas.DataFrame(list(edges), columns=['id1', 'id2'])
nouns_and_adjectives['weight'] = 1
nouns_and_adjectives.to_csv('nouns_and_adjectives_closure.csv', index=False)
