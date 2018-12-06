import numpy as np
import boundary_tree

class BF:
  def __init__(self, X, y, n_trees=10):
      self.X = X
      self.y = y
      self.n_trees = n_trees
      self.trees = list()

  def BFQuery(self, query_node):
      result_labels = list()
      for tree in self.trees:
          result_node = tree.BTQuery(query_node)
          result_labels.append(result_node.label)

      return result_labels

  def BFTrain(self, k):
      for i in range(0, self.n_trees):
          indx = np.random.choice(self.X.shape[0], np.floor(self.X.shape[0]/self.n_trees).astype(int))
          bt = boundary_tree.BT(self.X[indx], self.y[indx], k)
          bt.BTTrain()
          self.trees.append(bt)
