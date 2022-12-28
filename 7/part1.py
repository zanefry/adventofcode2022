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
    child_node.parent = child_node


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

final_sum = 0
def node_total(node: TreeNode):
    global final_sum
    if not node.children:
        return node.value

    total = sum([node_total(child) for child in node.children])
    if total <= 100000:
        final_sum += total

    return total

node_total(cwd)
print(final_sum)
