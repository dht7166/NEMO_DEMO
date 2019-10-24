import numpy as np
import sys
from scipy.sparse import lil_matrix as matrix
from scipy.sparse import save_npz,load_npz
from tqdm import tqdm

WM = 750000
Stream = 4000000
GM = 250000

average_stream_per_vox = 43000

down_factor = 64

WM = int(WM/down_factor)
Stream = int(Stream/down_factor)
GM = int(GM/down_factor)
average_stream_per_vox = int(average_stream_per_vox/down_factor)

def generate_WM_Stream():

    # Specific to DOK matrix
    sparse = matrix((WM,Stream),dtype=np.bool_)
    for i in tqdm(range(WM)):
        connected = np.random.randint(low=0, high=Stream, size=average_stream_per_vox)
        for j in connected:
            sparse[i,j] = 1
    return sparse

def generate_Stream_GM():
    sparse = matrix((Stream,GM),dtype=np.bool_)
    for i in tqdm(range(Stream)):
        connected = np.random.randint(low=0, high=GM, size=20)
        for j in connected:
            sparse[i,j]=1
    return sparse


WS = generate_WM_Stream()
WS = WS.tocoo()
SG = generate_Stream_GM()
SG = SG.tocoo()
# Save generation to files
save_npz('WM_ST.npz',WS)
save_npz('ST_GM.npz',SG)





