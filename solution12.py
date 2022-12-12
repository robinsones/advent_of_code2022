import numpy as np
import string
from scipy.sparse.csgraph import dijkstra, shortest_path

with open('input12.txt') as f:
  lines = [l.strip() for l in f]

starting_ind = []
ending_ind = []
for row, l in enumerate(lines):
  for col, let in enumerate(l):
    if let == "S":
      starting_ind.append(row)
      starting_ind.append(col)
    elif let == "E":
      ending_ind.append(row)
      ending_ind.append(col)
   
tran_dict = dict(zip(string.ascii_lowercase, range(26)))
tran_dict['E'] = 25
tran_dict['S'] = 0

tran_line = []
for li in lines:
  tran_line.append([tran_dict[i] for i in li])

gr = np.array(tran_line)

def update_if_close(x, y, row_ind, col_ind):
  nb_cols = x.shape[1]
  ent = x[row_ind, col_ind]
  muti = row_ind*nb_cols
  try:
    if ent - x[row_ind, col_ind+1] <= 1:
      y[col_ind + muti, col_ind+1 + muti] = 1
  except:
    pass
  try:
    if ent - x[row_ind+1, col_ind] <= 1:
      y[col_ind + muti, col_ind + (row_ind+1)*nb_cols] = 1
  except:
    pass
  try:
    if ent - x[row_ind-1, col_ind] <= 1:
      y[col_ind + muti, col_ind + (row_ind-1)*nb_cols] = 1
  except:
    pass
  try:
    if ent - x[row_ind, col_ind-1] <= 1:
      y[col_ind + muti, col_ind-1 + muti] = 1
  except:
    pass
  
def create_adj_mat(x):
  y = np.ones([x.size,x.size]) * np.inf 
  for ri, row in enumerate(x):
    for ci, entry in enumerate(row):
      update_if_close(x, y, ri, ci)
  return y

zb = create_adj_mat(gr)

di = shortest_path(zb)

ending_di_ind = (gr.shape[1])*ending_ind[0] + ending_ind[1]
starting_di_ind = (gr.shape[1])*starting_ind[0] + starting_ind[1]

# 413 is too low
di[ending_di_ind, starting_di_ind] 
