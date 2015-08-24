__author__ = 'daming'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        result = "val: "+ str(self.val)
        # if self.left:
        #     result += ", left: "+ str(self.left.val)
        # if self.right:
        #     result += ", right: "+ str(self.right.val)
        # return result + " | "
        return str(self.val)

def build_tree(tree_vals):
    # print 'tree_vals : ', tree_vals
    root = None

    tree_nodes = []
    for i in range(0, len(tree_vals)):
        cur_node = None
        if tree_vals[i]!='#':
            cur_node = TreeNode(int(tree_vals[i]))
        tree_nodes.append(cur_node)

    # print 'tree_nodes :', tree_nodes

    for i in range(0, len(tree_nodes)):
        if i*2+1 < len(tree_nodes):
            if tree_nodes[i*2+1]:
                tree_nodes[i].left = tree_nodes[i*2+1]
        if i*2+2 < len(tree_nodes):
            if tree_nodes[i*2+2]:
                tree_nodes[i].right = tree_nodes[i*2+2]
    return tree_nodes[0]

def bst_in_order(root):
    if root:
        bst_in_order(root.left)
        print root.val
        bst_in_order(root.right)

def get_test_bsts(filename=""):
    if filename=="":
        filename="sample_bst"

    with open(filename) as f:
        # content = f.readlines()
        # print content
        trees = []
        tree_vals = []
        tree_num = ""
        for line in f:
            line = line.strip()
            if line == "":
                continue
            if 'Tree' in line and ":" in line:
                if tree_vals!=[]:
                    trees.append(build_tree(tree_vals))
                tree_vals = []
                pieces = line.split(":")
                tree_num = pieces[1].strip()
                continue
            pieces = line.split()
            tree_vals.extend(pieces)
        if tree_vals!=[]:
            trees.append(build_tree(tree_vals))
    return trees


def disp_bst(root):
    print "\n"
    length = 1
    queue = [root]
    cur_level_counter = 0
    left_indent = 24
    child_width = 10
    while queue:
        nothing_on_this_level = True
        # cur_level_output = " " * left_indent
        cur_level_output = ""
        while cur_level_counter<length:
            cur_level_counter+=1
            cur_node = queue.pop(0)
            if cur_node:
                nothing_on_this_level = False
                cur_level_output += str(cur_node.val)
                cur_level_output += " "*child_width
                queue.append(cur_node.left)
                queue.append(cur_node.right)
            else:
                cur_level_output += '#'
                queue.append(None)
                queue.append(None)
                cur_level_output += " "*child_width
        if nothing_on_this_level:
            return
        print cur_level_output
        cur_level_counter = 0
        length = length*2
        left_indent /= 2
        child_width /= 2



