from scipy.spatial import distance

class Node:
    def __init__(self, feature_vector, label):
        self.feature_vector = feature_vector
        self.label = label
        self.children = list()

    def NodeDist(self, node):
        return distance.euclidean(self.feature_vector, node.feature_vector)

    def AddChild(self, child_node):
        self.children.append(child_node)
