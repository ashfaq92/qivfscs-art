import faiss
import numpy as np

d = 2
X = 100
np.random.seed(1234)
E = np.random.random((X, d)).astype('float32')

faissIndex = faiss.IndexFlatL2(d)
faissIndex.add(E)

C = np.random.random((10, d)).astype('float32')

resp = faissIndex.search(C, 1)
print("query point:", tuple(C[0]))
print("nearest neighbor:", tuple(E[resp[1]]))
print("distance:", resp[0])


ENew = np.random.random((10000, d)).astype('float32')
faissIndex.add(ENew)


