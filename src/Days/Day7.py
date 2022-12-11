from Days.Base.BaseDay import BaseDay

class Node:
    def get_parent_dir(self):
        p = self.parent
        path = []
        while not p == None:
            path.insert(0,p.directory)
            p = p.parent
        res = ""
        for dir in path:
            res += dir + "/"
        return res

    def __str__(self):
        return f"{self.get_parent_dir()}{self.directory}/ chil:{len(self.children)} fil:{len(self.files)} size:{self.get_total_size()}"

    def __repr__(self) -> str:
        return str(self)

    def __init__(self, parent, new_dir) -> None:
        self.children = []
        self.files = {}
        self.directory = ""
        self.size_files = 0
        self.size_children = 0
        self.parent = parent
        self.directory = new_dir

    def get_total_size(self):
        return self.size_files + self.size_children

    def add_child(self, dir):
        self.children.append(Node(self,dir))

    def add_file(self, sizestr, name):
        size = int(sizestr)
        self.files[name] = size
        self.size_files += size


    def get_parent(self):
        return self.parent

    def get_child(self, dir):
        for child in self.children:
            if child.directory == dir:
                return child

class Tree:
    root = Node(None, "/")
    curr_node = root

    def __str__(self):
        return str(self.curr_node)
    
    def __repr__(self) -> str:
        return str(self)
    
    def calc_sizes(self, curr_node):
        child_size = 0
        for child in curr_node.children:
            child_size += self.calc_sizes(child) + child.size_files
        curr_node.size_children = child_size
        return child_size

    def parse_input_line(self, line):
        if line[0] == "$":
            cmd = line.split()
            if cmd[1] == "cd":
                if cmd[2] == "..":
                    self.curr_node = self.curr_node.get_parent()

                else:
                    child = self.curr_node.get_child(cmd[2])
                    if not child == None:
                        self.curr_node = child
        else:
            file_stats = line.split()
            if file_stats[0] == "dir":
                self.curr_node.add_child(file_stats[1])
            else:
                self.curr_node.add_file(file_stats[0], file_stats[1])

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
    
    def parse_tree(self, tree):
        for line in self.input[:-1]:
            tree.parse_input_line(line)
        tree.calc_sizes(tree.root)

    def sum_nodes_lt(self, curr_node, max):
        res = 0
        s_curr_node = curr_node.get_total_size()
        if s_curr_node < max:
            res += s_curr_node
        for child in curr_node.children:
            res += self.sum_nodes_lt(child, max)
        return res

    def find_smallest_node_mt(self, root, min):
        if root == None or root.get_total_size() < min:
            return 
        curr_min = root
        
        s_curr_min = root.get_total_size()
        for child in root.children:
            min_child = self.find_smallest_node_mt(child, min)
            if min_child == None: continue
            s_min_child = min_child.get_total_size()

            if s_min_child >= min and s_min_child < s_curr_min:
                curr_min = min_child
        
        return curr_min

    def calcP1(self):
        tree = Tree()
        self.parse_tree(tree)
        return self.sum_nodes_lt(tree.root, 100_000)


    def calcP2(self):
        tree = Tree()
        # self.parse_tree(tree)
        s_free = 70_000_000 - tree.root.get_total_size()
        s_req = 30_000_000 - s_free

        to_be_deleted = self.find_smallest_node_mt(tree.root, s_req)
        return to_be_deleted