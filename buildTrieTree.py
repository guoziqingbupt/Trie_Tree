class TrieTreeNode(object):
    def __init__(self):
        self.end = False

        # The labels of pointers in the node
        self.pointerLabels = []

        # The pointers
        self.pointers = []


def buildTrieTree(stringList):
    """
    :param stringList: the collection of strings
    :return:
    """

    root = TrieTreeNode()

    for ele in stringList:
        cur = root

        for char in ele:

            if char not in cur.pointerlabels:
                cur.pointerLabels.append(char)
                newNode = TrieTreeNode()
                cur.pointers.append(newNode)

                if char != ele[-1]:
                    cur = newNode

            # When char in cur.pointerlabels
            elif char != ele[-1]:
                pos = cur.pointerlabels.index(char)
                cur = cur.pointers[pos]
            else:
                cur.end = True
    return root


