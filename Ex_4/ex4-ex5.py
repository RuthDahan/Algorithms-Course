import random
from typing import Optional




class Node:
    def __init__(self, value):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None

    def print(self):
        if self.left:
            self.left.print()
        print(self.value, ", "
                          "", sep="", end="")
        if self.right:
            self.right.print()

    def print_mermaid(self, id: str):
        # הדפסת השורש עצמו (קורה רק בקריאה הראשונה מה-Tree)
        if self.parent is None:
            id = "t"
            print(f"\t{id}(({self.value}))")  # [cite: 48, 49]

        if self.right is None and self.left is None:
            return

        # טיפול בבן שמאלי
        if self.left:
            # הדפסת הקשת והצומת השמאלי
            print(f"\t{id} --> {id + 'l'}(({self.left.value}))")  # [cite: 51]
            self.left.print_mermaid(id + "l")
        else:
            # הדפסת צומת "רפאים" כדי לשמור על המבנה
            print(f"\t{id} ~~~ {id + 'l'}(( ))")
            print(f"\tstyle {id + 'l'} fill:#fff,stroke-width:0px")  # [cite: 52]

        # טיפול בבן ימני
        if self.right:
            # הדפסת הקשת והצומת הימני
            print(f"\t{id} --> {id + 'r'}(({self.right.value}))")  # [cite: 51]
            self.right.print_mermaid(id + "r")
        else:
            # הדפסת צומת "רפאים"
            print(f"\t{id} ~~~ {id + 'r'}(( ))")
            print(f"\tstyle {id + 'r'} fill:#fff,stroke-width:0px")  # [cite: 52]


    def depth(self) -> int:
        depth = 0
        if self.left:
            depth = max(depth, self.left.depth())
        if self.right:
            depth = max(depth, self.right.depth())
        return depth + 1

    def min(self) -> 'Node':
        if self.left:
            return self.left.min()
        return self

    def max(self) -> 'Node':
        if self.right:
            return self.right.max()
        return self

    def get_number_of_nodes(self) -> int:
        number_of_nodes = 1
        if self.left:
            number_of_nodes += self.left.get_number_of_nodes()
        if self.right:
            number_of_nodes += self.right.get_number_of_nodes()
        return number_of_nodes

    def get_k_node(self, k: int) -> 'Node':
        left_count = 0
        if self.left:
            left_count = self.left.get_number_of_nodes()

        if left_count == k - 1:
            return self
        if left_count < k - 1:
            return self.right.get_k_node(k - left_count - 1)
        return self.left.get_k_node(k)


class Tree:
    # שאלה 4: הוספת key ל-constructor
    def __init__(self, key=lambda x: x):  #
        self.root = None
        self.key = key

    # שאלה 4: מימוש insert עם שימוש ב-key
    def insert(self, value):
        x = self.root
        y: Optional[Node] = None

        while x is not None:
            # שימוש ב-self.key להשוואה
            if self.key(value) == self.key(x.value):
                return
            y = x
            if self.key(value) > self.key(x.value):
                x = x.right
            else:
                x = x.left

        new_node = Node(value)

        if y is None:
            self.root = new_node
            return

        if self.key(value) > self.key(y.value):
            y.right = new_node
        else:
            y.left = new_node

        new_node.parent = y

    def print(self):
        if self.root:
            self.root.print()
        print()

    # שאלה 5: פונקציית המעטפת להדפסת Mermaid
    def print_mermaid(self):
        print("graph TD")  # הכותרת הנדרשת
        if self.root:
            # מתחילים את הרקורסיה מהשורש
            # ה-Node ידאג להדפיס את עצמו כ-t כיוון שאין לו הורה
            self.root.print_mermaid("t")


if __name__ == "__main__":
    tree = Tree()
    values = [10, 2, 4, 16, 15, 17, 20]
    for v in values:
        tree.insert(v)

    print("--- Mermaid Output ---")
    tree.print_mermaid()