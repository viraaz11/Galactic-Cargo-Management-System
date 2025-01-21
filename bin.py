from avl import AVLTree
import pdb
import typing
from node import Node
def comp_1(node_1,node_2):
    return node_1.key-node_2.key
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id  
        self.capacity = capacity  
        self.remaining_capacity = capacity  
        self.objects = AVLTree(comp_1)

    def add_object(self, object):
        # Implement logic to add an object to this bin
        self.objects.node=self.objects.insert(object.object_id,object)
        self.remaining_capacity -= object.size
        object.bin=self

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        object = self.objects.find(object_id)
        if object:
            self.objects.node = self.objects.delete(Node(object_id,object))
            self.remaining_capacity += object.size
            object.bin=None
    def _in_order(self):
        ans=[]
        def traverse(root,ans):
            if not root: return
            traverse(root.left,ans)
            ans.append(root.key)
            traverse(root.right,ans)
        traverse(self.objects.node,ans)
        return ans
    