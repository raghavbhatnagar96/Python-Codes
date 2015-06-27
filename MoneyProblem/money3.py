#!/usr/bin/python
import sys

'''
This version of money is different w.r.t money1 in the following:
  - It uses a solution tree explicitly.

This results in more efficient space usage. The time to query of value is proportional to the height of the solution tree; earlier it was constant time operation.
'''
sys.path.append("../tree")

import tree2 as T
import bfs2 as bfs

def makeChange(Q, D):

## Helper functions - begin ######################
  def getValue(n):
    p = T.parent(n)
    if(p == None):
      return T.getContents(n)
    else:
      return T.getContents(n) + getValue(p)

  def shouldBeAdded(n):
    return (not getValue(n) > Q)
  # Given a partial solution s, extend it by one step using each of the denominations available in D.
  def extendSolution(n):
    nss = []
    for i in D:
      nc = i
      st = T.makeLeaf(nc, n)
      if(shouldBeAdded(st)):
        T.addSubtree(n, st)
        nss.append(st)
    return nss
  
  def isSolution(n):
    return getValue(n) == Q

## Helper functions - end ######################
## Main algorithm - begin ######################
  return bfs.search(0, extendSolution, isSolution)
## Main algorithm - end ######################

if __name__ == "__main__":
  print makeChange(80, [10, 4, 6]) 
  print makeChange(8, [1, 4, 6])
  print makeChange(11, [4, 6]) # No solution
