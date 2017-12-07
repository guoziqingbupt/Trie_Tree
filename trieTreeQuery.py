from buildTrieTree import *


def trieTreeQuery(inputString, trieTreeRoot):
    """
    :param inputString: the string that need to be searched
    :param trieTreeRoot: the root of Trie tree
    :return:
    """
    cur = trieTreeRoot
    for char in inputString:
        if char not in cur.pointerlabels:
            return False
        else:
            pos = cur.pointerlabels.index(char)
            cur = cur.pointers[pos]
    if cur.end is True:
        return True
    return False


if __name__ == "__main__":
    strList = ["asd", "ast", "sd", "sdf", "sdt"]
    root = buildTrieTree(strList)
    inputString = "sdtrg"
    print(trieTreeQuery(inputString, root))