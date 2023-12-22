import numpy as np
token_embedding_dict = np.load("../data/token_embedding_dict.npy", allow_pickle=True)[()]

print(type(token_embedding_dict))
#print(token_embedding_dict)