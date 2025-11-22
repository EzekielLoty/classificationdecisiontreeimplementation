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
    #Calculate H(S) Root
    total_rows = len(data)
    target_col = data.columns[-1]

    # probabilities of each class
    probs = data[target_col].value_counts(normalize=True).tolist()

    root_entropy = calculate_entropy(probs)

    #Calculate Split Gain for each feature
    # Code:
    # for each column:
    # have variable current biggest information game, and current column loc
    # split column into unique values
    # for each split get the probability for the target value and calculate entropy
    # get weighted entropy by taking the # of that unique value divided by the total amount of rows
    # them sum the weighted entropy of each to get the total weighted entropy 
    # calculate information gain (root entropy - weighted sum entropy) and see if its the current biggest

    