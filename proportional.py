def abzerosgame(g,B=[],alpha=1,beta=1):
	'''
	Returns a dictionary with the weights of vertices after applying proportional color change rule as much as possible
	
	g a graph
	B a set of initially filled vertices
	alpha the proportion of weight a filled vertex transfers to a vertex it forces
	beta the threshold to be filled
	
	
	'''
	unfilled_vertices=set(g.vertices()).difference(set(B)) # current unfilled/partially filled vertices
	filled_vertices=set(B) # current filled vertices
	again=1 # iterate again or not
	weights={} # initialize weights
	collected_forces=[]
	for v in g.vertices():
		weights[v]=0
	for v in filled_vertices:
		weights[v]=1
	while again==1:
		again=0
		UF=unfilled_vertices.copy()
		F=filled_vertices.copy()
		unfilled_vertices2=unfilled_vertices.copy()
		for x in F:
			N=set(g.neighbors(x))# all neighbors of filled vertex
			D=N.intersection(UF) # set of unfilled neighbors
			if len(D)==1 and [x,next(iter(D))] not in collected_forces:
				again=1
				for d in D:
					#print(x," forcing ",d)
					weights[d]=weights[d]+alpha*weights[x]
					collected_forces.append([x,d])
					if weights[d]>=beta:
						filled_vertices.add(d)
						unfilled_vertices.discard(d)
						break
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
