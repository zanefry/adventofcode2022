#!/usr/bin/env python3

class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes
    self.parent = None

  def add_child(self, child_node):
    self.children.append(child_node)
    child_node.parent = self

  def remove_child(self, child_node):
    self.children = [child for child in self.children if child is not child_node]
    child_node.parent = None

def tree_size(node: TreeNode):
    if not node.children:
        return node.value

    node.value = sum([tree_size(child) for child in node.children])
    return node.value

lines: list[list[str]]
with open('input') as f:
    lines = [l.rstrip().split() for l in f.readlines()[1:]] # exclude cd /

# build up tree
cwd = TreeNode('/')
for line in lines:
    if '$' in line:
        if line[1] == 'cd':
            if line[2] == '..':
                cwd = cwd.parent
            else:
                child = TreeNode(line[2])
                cwd.add_child(child)
                cwd = child
    elif line[0] != 'dir':
        size = int(line[0])
        cwd.add_child(TreeNode(size))

# traverse back up
while cwd.parent:
    cwd = cwd.parent

unused = 70000000 - tree_size(cwd)

options = []
def find_options(node: TreeNode):
    global options

    big_enough = [child for child in node.children if unused + child.value >= 30000000]
    if not big_enough:
        options.append(node.value)
    else:
        for child in big_enough:
            find_options(child)

find_options(cwd)
print(min(options))
