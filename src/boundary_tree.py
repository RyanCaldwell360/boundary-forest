import node
import numpy as np

class BT:
    def __init__(self, X, y, k):
        self.X = X
        self.y = y
        self.root_node = node.Node(self.X[0], self.y[0])
        self.k = k

    def BTQuery(self, query_node):
        current_node = self.root_node
        children = current_node.children

        if len(children) < self.k:
            children.append(current_node)

        node_distances = [query_node.NodeDist(node) for node in children]
        nearest_node = children[np.argmin(node_distances)]

        if nearest_node != query_node:
            current_node = nearest_node

        return current_node

    def BTTrain(self):
        for i in range(1, len(self.X)):
            query_node = node.Node(self.X[i], self.y[i])
            nearest_node = self.BTQuery(query_node)
            if nearest_node.label != query_node.label:
                nearest_node.AddChild(query_node)
