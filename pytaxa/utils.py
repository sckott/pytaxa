from collections import OrderedDict
from .ranks_ref import *

def gt(l, d, default):
  try:
    return l[d]
  except TypeError:
    return default

# x = "aberration"
def which_ranks(x):
  z = ranks_ref()
  return list({ k:v for k,v in z.items() if x in v.split(',') }.keys())  

def flatten(x):
  return [item for sublist in x for item in sublist]

def flatten_int(x):
  # convert sublist to str() in case of an int
  return [item for sublist in x for item in str(sublist)]

def uniq(x):
  return list(set(x))

def argsort(seq):
  return sorted(range(len(seq)), key=seq.__getitem__)

def unique(l):
  return OrderedDict((x, True) for x in l).keys()

def all_none(m):
  return all([ z is None for z in m ])

def any_none(m):
  return any([ z is None for z in m ])

def no_nones(m):
  return not any_none(m)

def int2str(x):
  if x is not None:
    if isinstance(x, list):
      return [str(w) for w in x]
    else:
      return str(x)
