from gensim.models.poincare import PoincareModel, PoincareKeyedVectors, PoincareRelations
from  gensim.viz.poincare import poincare_distance_heatmap


from tensorflow.keras.layers import Embedding

wordnet_mamal_file_path = '/Users/pankaj/dev/git/smu/nlp337/data/mamals.tsv'
relations = PoincareRelations(wordnet_mamal_file_path, delimiter='\t')
model = PoincareModel(train_data=relations, size=2 , burn_in=0)
model.train(epochs = 2 , print_every = 500)


pcv = PoincareKeyedVectors(vector_size=20)

poincare_distance_heatmap((0,0), x_range=(-1.0, 1.0), y_range=(-1.0, 1.0), num_points=100)