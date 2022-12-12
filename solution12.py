import numpy as np
import string
from scipy.sparse.csgraph import shortest_path

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

def safe_check_up(x, y, row_ind, col_ind):
  nb_cols = x.shape[1]
  ent = x[row_ind, col_ind]
  muti = row_ind*nb_cols
  try:
    if x[row_ind-1, col_ind] - ent <= 1:
      y[col_ind + muti, col_ind + (row_ind-1)*nb_cols] = 1
  except:
    pass
  
def safe_check_down(x, y, row_ind, col_ind):
  nb_cols = x.shape[1]
  ent = x[row_ind, col_ind]
  muti = row_ind*nb_cols
  try:
    if x[row_ind+1, col_ind] - ent <= 1:
      y[col_ind + muti, col_ind + (row_ind+1)*nb_cols] = 1
  except:
    pass
  
def safe_check_right(x, y, row_ind, col_ind):
  nb_cols = x.shape[1]
  ent = x[row_ind, col_ind]
  muti = row_ind*nb_cols
  try:
    if x[row_ind, col_ind+1] - ent <= 1:
      y[col_ind + muti, col_ind+1 + muti] = 1
  except:
    pass

def safe_check_left(x, y, row_ind, col_ind):
  nb_cols = x.shape[1]
  ent = x[row_ind, col_ind]
  muti = row_ind*nb_cols
  try:
    if x[row_ind, col_ind-1] - ent<= 1:
      y[col_ind + muti, col_ind-1 + muti] = 1
  except:
    pass

def update_if_close(x, y, row_ind, col_ind):
  if row_ind == 0:
    safe_check_right(x, y, row_ind, col_ind)
    safe_check_left(x, y, row_ind, col_ind)
    safe_check_down(x, y, row_ind, col_ind)
  elif col_ind == x.shape[1] - 1:
    safe_check_left(x, y, row_ind, col_ind)
    safe_check_up(x, y, row_ind, col_ind)
    safe_check_down(x, y, row_ind, col_ind)
  elif col_ind == 0:
    safe_check_right(x, y, row_ind, col_ind)
    safe_check_up(x, y, row_ind, col_ind)
    safe_check_down(x, y, row_ind, col_ind)
  elif row_ind == x.shape[0] - 1:
    safe_check_right(x, y, row_ind, col_ind)
    safe_check_up(x, y, row_ind, col_ind)
    safe_check_down(x, y, row_ind, col_ind)
  else:
    safe_check_right(x, y, row_ind, col_ind)
    safe_check_up(x, y, row_ind, col_ind)
    safe_check_down(x, y, row_ind, col_ind)
    safe_check_left(x, y, row_ind, col_ind)
    
def create_adj_mat(x):
  y = np.ones([x.size,x.size]) * np.inf 
  for ri, row in enumerate(x):
    for ci, _ in enumerate(row):
      update_if_close(x, y, ri, ci)
  return y

zb = create_adj_mat(gr)

di = shortest_path(zb)

ending_di_ind = (gr.shape[1])*ending_ind[0] + ending_ind[1]
starting_di_ind = (gr.shape[1])*starting_ind[0] + starting_ind[1]

di[starting_di_ind, ending_di_ind] 

## Part 2

all_a = []
for ind, va in enumerate(np.ravel(gr)):
  if va == 0:
    all_a.append(ind)

path_dist = []

for st_p in all_a:
  path_dist.append(di[st_p, ending_di_ind])

min(path_dist)
