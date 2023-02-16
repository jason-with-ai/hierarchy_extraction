import functools
from absl import app
from tf_agents.system import system_multiprocessing as multiprocessing
from absl import logging
from datetime import datetime
import os
import absl
import shutil

class TreeNode(object):
    """Node of a Tree"""

    def __init__(self, name='root', children=None, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def is_root(self):
        if self.parent is None:
            return True
        else:
            return False

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def depth(self):
        if self.is_root():
            return 0
        else:
            return 1 + self.parent.depth()

    def add_child(self, node):
        node.parent = self
        assert isinstance(node, TreeNode)
        self.children.append(node)

    def disp(self):
        self.print_tree(self, 'children', 'name')

    def print_tree(self, current_node, childattr='children', nameattr='name'):
        if hasattr(current_node, nameattr):
            name = lambda node: getattr(node, nameattr)
        else:
            name = lambda node: str(node)

        children = lambda node: getattr(node, childattr)
        nb_children = lambda node: sum(nb_children(child) for child in children(node)) + 1

        def balanced_branches(current_node):
            size_branch = {child: nb_children(child) for child in children(current_node)}

            """ Creation of balanced lists for "a" branch and "b" branch. """
            a = sorted(children(current_node), key=lambda node: nb_children(node))
            b = []
            while a and sum(size_branch[node] for node in b) < sum(size_branch[node] for node in a):
                b.append(a.pop())

            return a, b

        self.display_tree(current_node, balanced_branches, name)

    def display_tree(self, current_node, balanced_branches, name_getter, indent='', last='updown'):

        up, down = balanced_branches(current_node)

        """ Printing of "up" branch. """
        for child in up:
            next_last = 'up' if up.index(child) == 0 else ''
            next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', ' ' * len(name_getter(current_node)))
            self.display_tree(child, balanced_branches, name_getter, next_indent, next_last)

        """ Printing of current node. """
        if last == 'up':
            start_shape = '┌'
        elif last == 'down':
            start_shape = '└'
        elif last == 'updown':
            start_shape = ' '
        else:
            start_shape = '├'

        if up:
            end_shape = '┤'
        elif down:
            end_shape = '┐'
        else:
            end_shape = ''

        logging.info('{0}{1}{2}{3}'.format(indent, start_shape, name_getter(current_node), end_shape))

        """ Printing of "down" branch. """
        for child in down:
            next_last = 'down' if down.index(child) is len(down) - 1 else ''
            next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│',
                                             ' ' * len(name_getter(current_node)))
            self.display_tree(child, balanced_branches, name_getter, next_indent, next_last)


class Tree:
    """Tree implementation as a collection of TreeNode objects"""

    def __init__(self):
        self.root = None
        self.height = 0
        self.nodes = []

    def insert(self, node, parent):
        if parent is not None:
            parent.add_child(node)
        else:
            if self.root is None:
                self.root = node
        self.nodes.append(node)

    def parent_path(self, node):
        if node.is_root():
            return "/" + node.name
        else:
            return self.parent_path(node.parent) + "/" + node.name
    
    def search_child(self, node, depth):
        if len(node.children) == 0:
            return node
        elif node.depth() == depth:
            return node
        else:
            # using recursion to check the same parents
            return self.search_child(node.children, depth)
        
    def find_parent_with_fixed_depth(self, node, depth):
        if node.depth() == depth:
            return node
        else:
            # using recursion to check the same parents
            return self.find_parent_with_fixed_depth(node.parent, depth)

    def search_parent_index(self, name, parent):
        index = -1
        for N in self.nodes:
            index += 1
            if N.name == name:
                # using recursion to check the same parents
                if self.parent_path(N.parent) == self.parent_path(parent):
                    return index
        return None

    def search_current_node(self, name, parent):
        index = -1
        for N in self.nodes:
            index += 1
            if N.name == name:
                # using recursion to check the same parents
                if self.parent_path(N.parent) == self.parent_path(parent):
                    return N
        return None

    def search(self, name, parent):
        index = -1
        for N in self.nodes:
            index += 1
            if N.name == name:
                # using recursion to check the same parents
                if self.parent_path(N.parent) == self.parent_path(parent):
                    return index
        return -1

    def getNode(self, node_id):
        return self.nodes[node_id]

    def root(self):
        return self.root


def main(argv):
    data = [
        ["asap7", "ariane"],
        ["nangate45", "ariane"],
        ["tsmc40lp", "cortexa5"],
        ["tsmc40lp", "cpu_cluster"],
        ["tsmc40lp", "d25_core"]]

    for design_info in data:

        dataset_name = design_info[0]
        design = design_info[1]

        save_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                f"logs/{dataset_name}/hierarchy_extraction-{design}_{datetime.now().strftime('%Y-%m-%d')}")

        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                f"data/{dataset_name}/{design}")
        
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        else:
            if os.path.isdir(save_dir):
                shutil.rmtree(save_dir)  # remove dir and all contains
                os.makedirs(save_dir)
            else:
                raise ValueError("file {} is not a file or dir.".format(save_dir))
        # logging
        logging.set_verbosity(logging.INFO)
        logging.get_absl_handler().setFormatter(None)
        absl.flags.FLAGS.mark_as_parsed()
        logging.get_absl_handler().python_handler.start_logging_to_file(program_name=f"{design}", log_dir=save_dir)

        # loading macro_names
        macros = []
        with open(os.path.join(data_dir, "macro_names.txt")) as file_in:
            for line in file_in:
                macros.append(line.replace("\n", ""))

        # extracting macros
        macro_groups = []
        for macro in macros:
            macro_arr = macro.split("/")
            macro_info = []
            for i in range(len(macro_arr)):
                macro_info.append(macro_arr[i])
            macro_groups.append(macro_info)

        # building a tree
        root = TreeNode('root')
        group_tree = Tree()
        group_tree.insert(root, None)

        # insert tree nodes into the tree
        for macro_info in macro_groups:

            # reset idx, parent
            idx = 0
            parent = root

            for i in range(len(macro_info)):
                # not exist
                if group_tree.search(str(macro_info[i]), parent) == -1:
                    parent_idx = group_tree.search_parent_index(str(macro_info[i]), parent)
                    if parent_idx is None:
                        group_tree.insert(TreeNode(str(macro_info[i])), parent)
                        # update current parent
                        parent = group_tree.search_current_node(str(macro_info[i]), parent)
                    else:
                        group_tree.insert(TreeNode(str(macro_info[i])), group_tree.nodes[parent_idx])
                        # update current parent
                        parent = group_tree.search_current_node(str(macro_info[i]), group_tree.nodes[parent_idx])

                    # a new index node
                    idx += 1
                else:  # existed
                    node_idx = group_tree.search(str(macro_info[i]), parent)
                    # update current parent
                    parent = group_tree.search_current_node(str(macro_info[i]), parent)
                    idx = node_idx

        # display group_tree horizontally
        logging.info("Group Tree")
        group_tree.root.disp()



if __name__ == '__main__':

    multiprocessing.handle_main(functools.partial(app.run, main))
