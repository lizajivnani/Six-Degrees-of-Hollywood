d1 = {'a':{'jh'},'b':2}
#print(d1['a'].add(2))
c = d1['a']
#print(type(c))

names = {'k': {1,2}}
l1 = list(names.get('k'))
#print(l1)

s1 = {(1, 2), (3, 4)}
for i in s1:
    print(i)

people = {'102': {'movies': ("h", "i")}}
print(people['102']['movies'][1])

from util import Node, StackFrontier, QueueFrontier
result = []
node = Node(state="node1",parent=None,action=2)
node2 = Node(state="node2", parent=None,action=2)
node3 = Node(state="node3", parent=None,action=4)
result = [node, node2, node3]
result2 = [node for node in result if node.action == (min(node.action for node in result))]
print(result2)


frontier = []

if len(frontier) is not 0:
    print("yes")







