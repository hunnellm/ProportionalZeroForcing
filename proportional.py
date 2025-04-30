def abzerosgame(g,F=[],alpha=1,beta=1):
	'''
	Returns a dictionary with the weights of vertices after applying proportional color change rule as much as possible
	
	g a graph
	F a set of initially filled vertices
	alpha the proportion of weight a filled vertex transfers to a vertex it forces
	beta the threshold to be filled
	
	
	'''
	
	unfilled_vertices=set(g.vertices()).difference(set(F)) # current unfilled/partially filled vertices
	filled_vertices=set(F) # current filled vertices

	again=1 # iterate again or not
	weights={} # initialize weights
	for v in g.vertices():
		weights[v]=0
	for v in filled_vertices:
		weights[v]=1
	for x in unfilled_vertices:
		N=set(g.neighbors(x))# all neighbors of white vertex
		D=N.intersection(filled_vertices) # set of white neighbors
		for d in D:
				P=set(g.neighbors(d)).difference(filled_vertices)#unfilled or partially filled neighbors
				if len(P)==1:
					weights[x]=weights[x]+alpha*weights[d]
		if weights[x]>=beta:
			filled_vertices.add(x)
	return weights

def is_ab_forcing_set(g,S=[],alpha=1,beta=1):
	'''
	Returns boolean whether S is an alpha,beta zero forcing set of g
	
	g a graph
	S a set of filled vertices to test
	alpha the proportion of weight a filled vertex transfers to a vertex it forces
	beta the threshold to be filled
	
	
	'''
	weights=abzerosgame(g,S,alpha,beta)
	filled=[]
	for v in g.vertices():
		if weights[v]>=beta:
			filled.append(v)
	if len(filled)==len(g.vertices()):
		return True
	return False

def Zab(g,alpha=1,beta=1,return_set=False,min_bound=1):
	k=min_bound
	while k<=len(g.vertices()):
		for S in Subsets(g.vertices(),k):
			if is_ab_forcing_set(g,list(S),alpha,beta):
				if return_set==True:
					return list(S)
				else:
					return k
		k+=1		
	return False

def all_ab_forcing_sets(g,k,alpha=1,beta=1):
	'''
	Returns all alpha,beta zero forcing sets of size k for a graph g
	
	g a graph
	k the size of subsets to consider
	alpha the proportion of weight a filled vertex transfers to a vertex it forces
	beta the threshold to be filled
	
	
	'''
	working_sets=[]
	for s in Subsets(g.vertices(),k):
		if is_ab_forcing_set(g,list(s),alpha,beta):
			working_sets.append(list(s))
	return working_sets
