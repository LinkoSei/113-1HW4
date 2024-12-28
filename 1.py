class BSTA:
    def __init__(self, size):
        self.tree = [None] * size  #初始化
        self.size = size

    def insert(self, value):
        if self.tree[0] is None:  #根節點 = 空(none)
            self.tree[0] = value
            return
        index = 0
        while index < self.size:
            if value < self.tree[index]:  #左
                next_index = 2 * index + 1
            else:  #右
                next_index = 2 * index + 2

            if next_index >= self.size:
                print("樹值已滿，無法加入")
                return
            if self.tree[next_index] is None:
                self.tree[next_index] = value
                return
            index = next_index

    def __str__(self):
        return str(self.tree)
print("\n") #讓輸出結果在VSC上有分行以便辨識
bst = BSTA(4)
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

print(bst)
