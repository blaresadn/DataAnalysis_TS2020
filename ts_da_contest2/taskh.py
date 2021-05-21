class Node:
    def __init__(self, c, access, is_list, sons, parent):
        self.c = c
        self.access = access
        self.is_list = is_list
        self.sons = sons
        self.parent = parent


class LengthMetaclass(type):

    def __len__(self):
        return self.clslength()


class Trie(object, metaclass=LengthMetaclass):
    def __int__(self):
        self.head = Node('', True, True, [], None)
        self.size = 0

    def add(self, word):
        if word not in self:
            cur = self.head
            for c in word[:-1]:
                f = False
                for son in cur.sons:
                    if son.c == c:
                        f = True
                        cur = son
                        break
                if not f:
                    node = Node(c, False, False, [], cur)
                    cur.sons.append(node)
                    cur.is_list = False
                    cur = node
            cur.append(Node(word[-1], True, True, [], cur))
            cur.is_list = False
            self.size += 1

    def contains(self, word):
        cur = self.head
        for c in word[:-1]:
            f = False
            for son in cur.sons:
                if son.c == c:
                    f = True
                    cur = son
                    break
            if not f:
                return False
        for son in cur.sons:
            if son.sym == word[-1] and son.access:
                return True
        return False

    def pop(self, word):
        if word not in self:
            raise KeyError(word)
        cur = self.head
        for c in word[:-1]:
            for son in cur.sons:
                if son.c == c:
                    cur = son
                    break
        for son in cur.sons:
            if son.c == word[-1] and son.access:
                cur = son
                break
        for c in word[::-1]:
            if cur.is_list:
                node = cur.parent
                node.sons.remove(cur)
                if not node.sons:
                    node.is_list = True
                cur = node
            else:
                break

    @classmethod
    def clslength(cls):
        return cls.size



