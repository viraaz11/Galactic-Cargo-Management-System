from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node
def comp_1(node_1, node_2):
    if(node_1.key==node_2.key): return node_1.value.bin_id - node_2.value.bin_id
    return node_1.key - node_2.key
def comp_2(node_1, node_2):
    return node_1.key - node_2.key
def comp_3(node_1, node_2):
    return node_1.key - node_2.key

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bins_by_capacity = AVLTree(comp_1) 
        self.bins_by_id = AVLTree(comp_2)  
        self.objects = AVLTree(comp_3) 

    def add_bin(self, bin_id, capacity):
        new_bin = Bin(bin_id, capacity)
        self.bins_by_capacity.node = self.bins_by_capacity.insert(capacity, new_bin)
        self.bins_by_id.node = self.bins_by_id.insert(bin_id, new_bin)
        
    def add_object(self, object_id, size, color):
        obj = Object(object_id, size, color)
        
        selected_bin: Bin = self._select_bin(size, color)
        if selected_bin is None:
            raise NoBinFoundException
        
        self.bins_by_capacity.node = self.bins_by_capacity.delete(Node(selected_bin.remaining_capacity,selected_bin))
        selected_bin.add_object(obj)
        self.bins_by_capacity.node = self.bins_by_capacity.insert(selected_bin.remaining_capacity,selected_bin)
        self.objects.node = self.objects.insert(object_id, obj)

    def _select_bin(self, size, color):
        if color == Color.RED :
            return self.largest_least_red(size)
        elif color == Color.GREEN:
            return self.largest_greatest_green(size)
        elif color == Color.BLUE:
            return self.bluefind(self.bins_by_capacity.node, size)
        elif color == Color.YELLOW:
            return self.yellowfind(size)
        return None
    
    def delete_object(self, object_id):
        obj = self.objects.find(object_id)
        if obj:
            self.bins_by_capacity.node = self.bins_by_capacity.delete(Node(obj.bin.remaining_capacity,obj.bin))
            temp=obj.bin
            obj.bin.remove_object(object_id)
            self.bins_by_capacity.node = self.bins_by_capacity.insert(temp.remaining_capacity,temp)
            obj.bin=None
            self.objects.node = self.objects.delete(Node(obj.object_id,obj))

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        bin = self.bins_by_id.find(bin_id)
        if bin: return (bin.remaining_capacity,bin._in_order())

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        obj = self.objects.find(object_id)
        if obj: return obj.bin.bin_id
        
    def largest_least_red(self,size):
        root1: Node=self.bins_by_capacity.node
        if root1 is None: return None
        assert root1.key >= 0
        while root1.right:
            root1=root1.right
        if root1.key < size:
            return None
        def findtopsize(root,size):
            if not root:
                return None
            if root.key==size:
                return root
            elif root.key<size:
                return findtopsize(root.right,size)
            return findtopsize(root.left,size)
        temp=findtopsize(self.bins_by_capacity.node,root1.key)
        def findminid(size,node):
            if node is None: return None 
            if node.key==size:
                temp=findminid(size,node.left)
                if temp: return temp
                return node
            return findminid(size,node.right)

        new = findminid(root1.key,temp)
        if not new: return None
        return new.value
    
    def largest_greatest_green(self,size):
        temp=self.bins_by_capacity.node
        if temp is None : return None 
        while temp.right is not None:
            temp=temp.right
        if temp.key<size: return None
        return temp.value
    
    def bluefind(self,root,size):
        if not root:
            return None
        if root.key>=size:
            temp=self.bluefind(root.left,size)
            if temp:
                return temp
            return root.value
        return self.bluefind(root.right,size)
            
    def yellowfind(self, size):
        node = self._find_range_iterative(self.bins_by_capacity.node, size)
        temp = self._searchit_iterative(self.bins_by_capacity.node, node)
        if not temp:
            return None
        new = self._max_id_iterative(temp, temp.key)
        return new.value if new is not None else None

    def _max_id_iterative(self, root, capacity):
        stack = []
        current = root
        max_node = None
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.right
            current = stack.pop()
            
            if current.key == capacity:
                max_node = current
                current = current.right
            else:
                current = current.left
        
        return max_node

    def _searchit_iterative(self, root, node):
        current = root
        
        while current and node != None and current.key != node.key:
            assert isinstance(current, Node)
            assert isinstance(node, Node)
            
            if current.key < node.key:
                current = current.right
            else:
                current = current.left
        
        return current

    def _find_range_iterative(self, root, size):
        current = root
        closest = None
        
        while current:
            if current.key >= size:
                closest = current
                current = current.left
            else:
                current = current.right
        
        return closest
