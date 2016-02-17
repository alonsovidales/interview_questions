#
# Example final output:
#
# 1000 main
#   1000 workLoop
#     900 read
#       900 __sys_read
#     100 parse
#       100 strcmp

# dh@uber.com
class Node(object):
    def __init__(self, name, times=1):
        self.times = times
        self.name = name
        self.childs = {}

class TracesProcessor(object):
    def __init__(self, traces):
        """
        Initializes the tree that contains the traces
        using the specified traces on the second param
        
        Traces format example:
            [
                ["main", "workloop", "select"],
                ["main", "parse_args"],
                ["main", "workloop", "parse_data", "parse_entry"],
                ["main", "workloop", "select"]
            ]
        """

        self._traces_tree = Node("")
        for trace in traces:
            node = self._traces_tree
            for func in trace:
                if func in node.childs:
                    node.childs[func].times += 1
                else:
                    node.childs[func] = Node(func)
                
                node = node.childs[func]
        
    def print_traces(self, node=None, deep=0):
        """
        Prints the traces nested by levels on the standar output
        adding the corresponding format
        """

        if node is None:
            node = self._traces_tree
            
        if node.name != '':
            print("{} {} {}".format('  ' * (deep-1), node.times, node.name))
        
        for child in node.childs.values():
            self.print_traces(child, deep+1)

if __name__ == "__main__":
    def get_stacktraces():
        return [
            ["main", "workloop", "select"],
            ["main", "parse_args"],
            ["main", "workloop", "parse_data", "parse_entry"],
            ["main", "workloop", "select"]
        ]
    
    TracesProcessor(get_stacktraces()).print_traces()

    # Testing some corner cases
    print("Corner cases...")
    TracesProcessor([]).print_traces()
    TracesProcessor([[]]).print_traces()
    TracesProcessor([["a", "b", "c"], []]).print_traces()
    TracesProcessor([[], ["a", "b", "c"]]).print_traces()
    TracesProcessor([["aaaa"]]).print_traces()
