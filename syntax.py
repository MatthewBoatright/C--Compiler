from main import Node

def syntax(input):

    root = Node(None, 'A', 0, 'NT')
    numNode = Node(root, 'NUM', 1, 'NT')
    root.addChild(numNode)
    strNode = Node(root, 'STR', 1, 'NT')
    root.addChild(strNode)
    currNode = root

    message = 'Syntax completed successfully.\n'
    output = ''

    for entry in input:
        if entry.getType() == 'NUM_I':
            currNode = numNode
        else:
            currNode = strNode
        d = currNode.depth + 1
        node = Node(currNode, entry.getVal(), d, 'NT')
        currNode.addChild(node)

    output = traverse(root)

    return message, output

def traverse(currNode):
    top = currNode
    line = ''

    if currNode.depth > 0:
        line += '|'
    for x in range (0, currNode.depth):
        line += '_'

    line += currNode.val + '\n'

    if currNode.c_num > 0:
        for x in range (0, currNode.c_num):
            line += traverse(currNode.children.pop())

    return line