from main import Node, Tree

def syntax(input):

    tree = Tree()

    message = 'Syntax completed successfully.\n'
    output = ''

    for entry in input:
        node = Node(entry)
        output += str(node) + '\n'

    return message, output