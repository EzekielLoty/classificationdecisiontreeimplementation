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
        self.root = None
    
    def set_root_node(self, node):
        self.root = node

    def add_node(self, node):
        self.nodes.append(node)

def calculate_entropy(probabilities):
    probabilities = np.array(probabilities)
    total_entropy = -np.sum(probabilities * np.log2(probabilities))
    return total_entropy

def build_part_decision_tree(tree):
    return

def build_full_decision_tree(data):
    total_rows = len(data)
    target_col = data.columns[-1]

    # probabilities of each class
    probs = data[target_col].value_counts(normalize=True).tolist()

    root_entropy = calculate_entropy(probs)
    return root_entropy

    