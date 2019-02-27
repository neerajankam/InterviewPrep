#K-Closest points
# import math
# def kClosestPoints(points,start_point,k):
# 	distance_dict = {}
# 	for point in points:
# 		distance = math.sqrt((start_point[0] - point[0]) ** 2 + (start_point[1] - point[1]) ** 2)
# 		distance_dict[distance] = point
# 	print(distance_dict)
# 	sorted_dict = sorted(distance_dict.items(),key = lambda x:x[1])
# 	print(sorted_dict)
# 	result = []
# 	num_points = 0
# 	for i in range(k):
# 		result.append(sorted_dict[i][1])
# 	return result
	

# points = [[1,2],[2,3],[4,6],[7,9]]
# start_point = [2,2]
# print(kClosestPoints(points,start_point,2))
#-----------------------------------------
#Rectangle Overlap

# def rectangleOverLap(rec1,rec2):
# 	return not(
# 		rec1[1] <= rec2[0] or    #left
# 		rec1[0] <= rec2[2] or   #right
# 		rec1[1] >= rec2[3] or   #top
# 		rec1[3] <= rec2[1])     #bottom

# rec1 = [0,0,2,2]
# rec2 = [1,1,3,3]
# print(rectangleOverLap(rec1,rec2))
#---------------------------------------
#Window Sum

# def slidingWindowMax(nums,windowSize):
# 	result = []
# 	for i in range(len(nums)-2):
# 		maxNum = float("-inf")
# 		for j in range(i,i+windowSize):
# 			if nums[j] > maxNum:
# 				maxNum = nums[j]
# 		result.append(maxNum)
# 	return result


# 	return result
# nums = [1,3,-1,-3,5,3,6,7]
# k  = 3
# print(slidingWindowMax(nums, k))
#---------------------------------------
#Longest palindormic substring

# def getLongestPalin(string):
# 	longest = [0,1]
# 	for i in range(1,len(string)):
# 		odd = getPalinFrom(i-1,i+1,string)
# 		even = getPalinFrom(i-1,i,string)
# 		currentLongest = max(odd,even,key = lambda x:x[1] - x[0])
# 		longest = max(longest,currentLongest,key = lambda x:x[1] - x[0])

# 	return string[longest[0]:longest[1]]

# def getPalinFrom(left,right,string):
# 	while left >= 0 and right < len(string):
# 		if string[left] != string[right]:
# 			break
# 		left -= 1
# 		right += 1
# 	return [left+1,right]

# string = "babad"
# print(getLongestPalin(string))
#------------------------------------------
#BreadthFirstSearch for Graph
# import collections
# def bfsTraversal(graph,root):
# 	visited = set()
# 	queue = collections.deque(root)
# 	visited.add(root)
# 	while queue:
# 		vertex = queue.popleft()
# 		print(vertex)
# 		for neighbor in graph[vertex]:
# 			if neighbor not in visited:
# 				visited.add(neighbor)
# 				queue.append(neighbor)


# graph = {'A': ['B', 'C'],
#              'B': ['C', 'D'],
#              'C': ['D','F'],
#              'D': ['C'],
#              'E': ['F'],
#              'F': ['C']}
# print(bfsTraversal(graph,'A'))

#---------------------------------------
# Depth First Search
# def dfs(graph,root,visited):
# 	if root is None:
# 		return
# 	visited.add(root)
# 	print(root)
# 	for neighbor in graph[root]:
# 		if neighbor not in visited:
# 			# visited.add(neighbor)
# 			dfs(graph,neighbor,visited)

# graph = {2:[0,3],0:[1,2],1:[2],3:[3]}
# visited = set()
# print(dfs(graph,2,visited))
#----------------------------------------
#Graph representation and related methods

# class Graph:
# 	def __init__(self,graph_dict = None):
# 		self.graph_dict = {}

# 	def addVertex(self,vertex):
# 		self.graph_dict[vertex] = []

# 	def addEdge(self,fromVert, toVert):
# 		self.graph_dict[fromVert].append(toVert)

# 	def addEdgeWithWeight(self,fromVert,toVert,weight):
# 		self.graph_dict[fromVert].append((toVert,weight))

# 	def getVertex(self,vertex):
# 		if vertex in self.graph_dict.keys():
# 			return vertex
# 		else:
# 			return None

# 	def getVertices(self):
# 		return self.graph_dict.keys()


# g = Graph()
# g.addVertex('a')
# g.addVertex('b')
# print(g.graph_dict)
# g.addEdgeWithWeight('a','b',4)
# print(g.graph_dict)
# print(g.getVertices())
#----------------------------------------
# 
#Adjacency list implementation of Graph
# class AdjNode: 
#     def __init__(self, data): 
#         self.vertex = data 
#         self.next = None

# class Graph: 
#     def __init__(self, vertices): 
#         self.V = vertices 
#         self.graph = [None] * self.V 
  
#     # Function to add an edge in an undirected graph 
#     def add_edge(self, src, dest): 
#         # Adding the node to the source node 
#         node = AdjNode(dest) 
#         node.next = self.graph[src] 
#         self.graph[src] = node 
  
#         # Adding the source node to the destination as 
#         # it is the undirected graph 
#         node = AdjNode(src) 
#         node.next = self.graph[dest] 
#         self.graph[dest] = node 
  
#     # Function to print the graph 
#     def print_graph(self): 
#         for i in range(self.V): 
#             print("Adjacency list of vertex {}\n head".format(i)) 
#             temp = self.graph[i] 
#             while temp: 
#                 print(" -> {}".format(temp.vertex)) 
#                 temp = temp.next
#             print(" \n") 
		

# g = Graph(5)
# g.add_edge(0,1)
# g.add_edge(0, 4) 
# g.add_edge(1, 2) 
# g.add_edge(1, 3) 
# g.add_edge(1, 4) 
# g.add_edge(2, 3) 
# g.add_edge(3, 4)
# print(g.print_graph())
#---------------------------
#Topological Sort
# from collections import defaultdict
# class jobGraph:
# 	def __init__(self,vertices,dependencies):
# 		self.numVertices = vertices
# 		self.jobGraph = defaultdict(list)
# 		for dependency in dependencies:
# 			self.add_dependency(dependency[0],dependency[1])

# 	def add_dependency(self,u,v):
# 		self.jobGraph[u].append(v)


# 	def topologicalSortUtil(self,curIdx,visited,stack):
# 		visited[curIdx] = True
# 		for i in self.jobGraph[curIdx]:
# 			if visited[i] == False:
# 				self.topologicalSortUtil(i,visited,stack)
# 		stack.insert(0,curIdx)

# 	def topologicalSort(self):
# 		stack = []
# 		visited = [False] * self.numVertices

# 		for i in range(self.numVertices):
# 			if visited[i] == False:
# 				self.topologicalSortUtil(i,visited,stack)
# 		print(stack)

# j = jobGraph(5,[[1,2],[1,3],[3,2],[4,2],[4,3]])
# j.topologicalSort()
#---------------------------------------------------------
# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class CLL:
# 	def __init__(self):
# 		self.head = None

# 	def insert(self,data):
# 		new_node = Node(data)
# 		cur = self.head
# 		if cur is None:
# 			self.head = new_node
# 			self.head.next = self.head
# 		else:
# 			while cur.next != self.head:
# 				cur = cur.next
# 			cur.next = new_node
# 			new_node.next = self.head

# 	def insertNode(self,data):
# 		new_node = Node(data)
# 		cur = self.head
# 		prev = None
# 		while cur.next.data < data:
# 			prev = cur
# 			cur = cur.next
# 		prev.next = new_node
# 		new_node.next = cur

# 	def printLL(self):
# 		cur = self.head
# 		while cur.next != self.head:
# 			print(cur.data)
# 			cur = cur.next
# 		print(cur.data)

# c = CLL()
# c.insert(1)
# c.insert(2)
# c.insert(3)
# c.insert(5)
# c.insertNode(4)
# c.printLL()
#-----------------------------------------
#Pattern matching
# def match(string,pattern):
#   if len(pattern) == 0:
#     return len(string) == 0
  
#   if len(string) == 0:
#     for i in range(len(pattern)):
#       if pattern[i] != '*':
#         return False
#     return True
  
#   if pattern[0] == '?' or pattern[0] == string[0]:
#     return match(string[1:],pattern[1:])
  
#   if pattern[0] == '*':
#     return match(string[1:],pattern) or match(string,pattern[1:])

#   return False

# print(match("gdd","*d"))
#---------------------------------------------
#Target Sum
# def findPair(array,target):
# 	num_dict = {}
# 	for num in array:
# 		requiredNum = target - num
# 		if requiredNum in num_dict:
# 			return sorted([requiredNum,num])
# 		else:
# 			num_dict[num] = True


# print(findPair([1,3,6,7,4],11))
#----------------------------------------------
#Given an ArrayList of Nodes, with each Node having an ID and a parent ID, determine whether the List is given in preorder.
# class Node:
# 	def __init__(self,ID,parent):
# 		self.id = ID
# 		self.parentID = parent
# 		self.left = None
# 		self.right = None
# #The key idea is that a node can be present only after its parent node is present in the array. So, for all the nodes we
# #check if their parent is already present in the array.
# def isPreOrder(self,nodes):
# 	#If there are no nodes, it is a valid PreOrder traversal and hence return True
# 	if not nodes:
# 		return True
# 	#Append the first node's id onto the stack.
# 	stack = [nodes[0].id]
# 	i = 1
	
# 	while i < len(nodes):
# 		if not stack:
# 			return False

# 		if stack[-1].id is nodes[i].parentID:
# 			stack.append(nodes[i].id)
# 			i += 1
		
# 		else:
# 			stack.pop()
# 	return True
#------------------------------------------------------
#Given a text and a pattern, find the indices in the string where an anagram of the pattern starts
# def find_indices_anagrams(text,pattern):
#   value_pattern = 0
#   # set_pattern = set(pattern)
#   result = []
#   for i in range(len(pattern)):
#     value_pattern += ord(pattern[i])
  
#   for i in range(len(text)-len(pattern)+1):
#     value_string = 0
#     set_string = set()
#     for j in range(i,i + len(pattern)):
#       value_string += ord(text[j])
#       # set_string.add(text[j])
#     print(value_string)
#     if value_string == value_pattern:
#       result.append(i)
#   return result

# print(find_indices_anagrams('ABCDBABEAB','CD'))
#----------------------------------------------------------
#A queue of people are waiting to buy ice cream from you. 
# Each person buys one ice cream, which sells for $5. 
# Each customer is holding a bill of $5, $10 or $20. 
# Your initial balance is 0. 
# Find whether you will be able to make change for every customer in the queue. You must serve customers in the order they come in. 
# For example 
# 5, 5, 5, 10, 20 -> true, 
# 5, 5, 10 -> true, 
# 10, 10 -> false
# def can_return_change(bills):
#   cost_ice_cream = 5
#   current_change = 0
#   for bill in bills:
#     if bill == 5:
#       current_change += bill
#     else:
#       return_change = bill - cost_ice_cream
#       current_change += (bill-return_change) 
#       print(current_change,return_change)
#       if return_change > current_change:
#        return False
#       else:
#         current_change -= return_change
    
#   return True

# print(can_return_change([5,5,5,10,20]))
#--------------------------------------------------------------
#Powersets problem
# def power_set(nums):
#   subsets = [[]]
#   for ele in nums:
#     for i in range(len(subsets)):
#       current_subset = subsets[i]
#       subsets.append(current_subset + [ele])
#   return subsets


# nums = [1,2,3,4,5]
# print(power_set(nums))
#----------------------------------------------------
#Find if the given expression contains redundant parantheses. ex :if expr = a+(b*c) , print
# false, if expr = a+((b*c)), print true
# def duplicate_parantheses(expression):
#   stack = []
#   for char in expression:
#     if char == ')':
#       top = stack.pop()
#       elemsInside = 0
#       while top != '(':
#         top = stack.pop()
#         elemsInside +=1
#       if elemsInside <= 1:
#         return True
#     else:
#       stack.append(char)
#   return False
# print(duplicate_parantheses("(a+(b*c)"))
#-------------------------------------------------------
#Doubly linked list
# class LRUCache:
# 	def __init__(self,maxSize=1):
# 		self.cache = {}
# 		self.maxSize = maxSize
# 		self.currentSize = 0
# 		self.listOfMostRecent = doublyLinkedList()

# 	def insertKeyValuePair(self,key,value):
# 		if key not in self.cache:
# 			if self.currentSize == self.maxSize:
# 				self.evictLeastRecent()
# 			else:
# 				self.currentSize += 1
# 			self.cache[key] = DLLNode(key,value)
# 		else:
# 			self.replaceKey(key,value)
# 		self.updateMostRecent(self.cache[key])

# 	def getValueFromKey(self,key):
# 		if key not in self.cache:
# 			return None
# 		self.updateMostRecent(self.cache[key])
# 		return self.cache[key].value

# 	def getMostRecentKey(self):
# 		return self.listOfMostRecent.head.key

# 	def evictLeastRecent(self):
# 		removal_key = self.listOfMostRecent.tail.key
# 		self.listofMostRecent.removeTail()
# 		del cache[removal_key]

# 	def updateMostRecent(self,node):
# 		self.listOfMostRecent.setHeadTo(node)

# 	def replaceKey(self,key,value):
# 		if key not in self.cache:
# 			raise Exception("The provided key is not in cache")
# 		self.cache[key].value = value

# class doublyLinkedList:
# 	def __init__(self):
# 		self.head = None
# 		self.tail = None

# 	def setHeadTo(self,node):
# 		if self.head == node:
# 			return
# 		elif self.head is None:
# 			self.head = node
# 		elif self.head == self.tail:
# 			self.tail.prev = node
# 			node.next = self.tail
# 			self.head = node
# 		else:
# 			if self.tail == node:
# 				self.removeTail()
# 			node.removeBindings()
# 			self.head.prev = node
# 			node.next = self.head
# 			self.head = node

# 	def removeTail(self):
# 		if self.tail is None:
# 			return
# 		if self.head == self.tail:
# 			self.head = None
# 			self.tail = None
# 			return
# 		self.tail = self.tail.prev
# 		self.next = None


# class DLLNode:
# 	def __init__(self,key,value):
# 		self.key = key
# 		self.value = value
# 		self.next = None
# 		self.prev = None

# 	def removeBindings(self):
# 		if self.prev is not None:
# 			self.prev.next = self.next
# 		if self.next is not None:
# 			self.next.prev = self.prev
# 		self.prev = None
# 		self.next = None

# lru = LRUCache(10)
# lru.insertKeyValuePair("a",99)
# print(lru.getMostRecentKey())
# print(lru.getValueFromKey("a"))
# lru.insertKeyValuePair("a",0)
# print(lru.getValueFromKey("a"))
# lru.insertKeyValuePair("b",90)
# lru.insertKeyValuePair("c",100)
# print(lru.getMostRecentKey())