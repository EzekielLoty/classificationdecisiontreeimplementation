import numpy as np

class Node:
    def __init__(self, attribute, child_nodes=None, prev_node=None):
        self.attribute = attribute
        self.child_nodes = child_nodes if child_nodes is not None else []
        self.prev_node = prev_node
    
    def add_child_node(self, node):
        self.child_nodes.append(node)
        

class DecisionTree:
    def __init__(self):
        self.nodes = []
    
    def add_node(self, node):
        self.nodes.append(node)

def calculate_entropy(probabilities):
    probabilities = np.array(probabilities)
    total_entropy = -np.sum(probabilities * np.log2(probabilities))
    return total_entropy

def calculate_information_gain(entropy_i, entropy_a):
    return entropy_i - entropy_a