"""
EULER WALK by Vincent Nguyen
Given user inputs, finds an Euler Walk if possible.
Works for multigraphs as well.
In order to make work for multigraphs, I used lists instead of sets to
construct an adjacency table that could have multiple bridges between
two vertices.  

EXAMPLES:

>>> Enter all vertices as chars sep by ' ': A B C
>>> Adjacent to A: B B C C
>>> Adjacent to B: A A C C
>>> Adjacent to C: B B A A
>>> One possible Euler-Walk:
>>> A -> B -> A -> C -> B -> C -> A

>>> Enter all vertices as chars sep by ' ': A B C D E F
>>> Adjacent to A: B D F C
>>> Adjacent to B: E D C A
>>> Adjacent to C: E B F A
>>> Adjacent to D: B E F A
>>> Adjacent to E: B D F C
>>> Adjacent to F: E D C A
>>> One possible Euler-Walk:
>>> A -> B -> E -> D -> B -> C -> E -> F -> D -> A -> F -> C -> A

>>> Enter all vertices as chars sep by ' ': A B C D
>>> Adjacent to A: B C D
>>> Adjacent to B: A C
>>> Adjacent to C: B A D
>>> Adjacent to D: A C
>>> One possible Euler-Walk:
>>> A -> B -> C -> A -> D -> C
"""

from collections import Counter

class euler_walk(object):
    
    #creates deepcopy of original dic: set() structure
    def deepcopy(self, dic):
        copy = dict().fromkeys(dic)
        for k, v in dic.iteritems():
            copy[k] = v[:]
        return copy
    
    #constructs graph given command line user inputs
    def define_graph(self):
        vertices = [s for s in raw_input("Enter all vertices as chars sep by ' ': ").strip().split()]
        graph = {v: [s for s in raw_input("Adjacent to %s: " % v).strip().split()] for v in vertices}
        return graph
    
    #confirms whether euler walk is possible, i.e., all vertices must have even degree 
    #in which case start and end is the same or two and only two vertices have odd degree
    #and the rest are even in which case start and end are at the odd vertices
    def validate_euler(self, graph):
        odd_v = [v for v in graph if len(graph[v]) % 2 != 0]
        if not(len(odd_v) == 2 or len(odd_v) == 0):
            raise ValueError("Euler walk is not possible")
        return odd_v
    
    #depth first search to validate connectedness of graph
    def dfs(self, graph, start):
        visited = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                common =  list((Counter(graph[vertex]) & Counter(visited)).elements())
                lst = graph[vertex]
                for e in common:
                    lst.remove(e)
                stack.extend(lst)
        return visited
    
    #modifies graph by removing vertices with no connecting bridges
    def mod_graph(self, graph, visited, v, start):
        graph[start].remove(v)
        graph[v].remove(start)
        graph = {k: v for k, v in graph.items() if v}
        visited.append(v)
        return visited, graph

    #fleury algo for euler walk
    def fleury(self, graph, start):
        visited = [start]
        while graph:
            adjacent = graph[start]
            for v in adjacent:
                new_graph = self.deepcopy(graph)
                new_graph[start].remove(v)
                new_graph[v].remove(start)
                l = sum(1 for k in new_graph if new_graph[k])
                if l == 0:
                    visited, graph = self.mod_graph(graph, visited, v, start)
                    break
                else:
                    if len(self.dfs(new_graph, v)) == l:
                        visited, graph = self.mod_graph(graph, visited, v, start)
                        start = v
                        break
        return visited
    
    def main(self):
        graph = self.define_graph()
        odd_v = self.validate_euler(graph)
        if len(odd_v) == 0:
            start, end = graph.keys()[0], graph.keys()[0]
        else:
            start, end = odd_v
        walk = self.fleury(graph, start)
        assert(start == walk[0] and end == walk[-1])
        print "One possible Euler-Walk:"
        print " -> ".join(map(str, walk))
        return ""

if __name__ == "__main__":
    euler_walk().main()







