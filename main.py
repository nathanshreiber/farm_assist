

class node:

	#Initializer
	def __init__(self,slot,color,neighbors):
		self.slot = slot
		self.color = color
		self.neighbors = neighbors

class color:
	def __init__(self,color,k,number_left,collision):
		self.color = color
		self.k = k
		self.number_left = number_left
		self.collision = collision


#(list of nodes,index of node, colors objects)
def assign_color(nodes_to_check,hops,index,colors):
	
	hop = hops[index]					#find hop value
	node = nodex_to_check[index] 		#find node
	potential_nodes = append(node[2])	#potential children to add

	for n in potential_nodes:
		if n not in nodes_to_check:
			nodes_to_check.apend(n)		#add to list of nodes to check
			hops.append(hops[index]+1)  #add to list of hops

	list_of_colors = most_left(colors)	#create list of colors in decreasing order of preseidence
	
	#if (node.color):

	for color in list_of_colors:
		temp = colors.get(color)
		k = temp.k


def most_left(colorsList):
	return sorted(colorsList,key=most_left_compare,reveserse=True)

def most_left_compare(color1):
	return color1.number_left, color1.k

#pass a list of OBj colors (some of them)
#return list sorted by how bad their collision was as a percentage
# percentage = collsion / k 
#larger the percentage, better priority -> 1 being the best 
def most_collide(colorList):
	for color in colorsList:
		color.collision = color.collision / color.k
	return sorted(colorsList,key=most_collide_compare,reveserse=True)

def most_collide_compare(color1):
	return color1.collision, color1.number_left

if __name__ == '__main__':
	
#first floor node initialization
	node_1 = (1,None,[2])
	node_2 = (2,None,[1,3])
	node_3 = (3,None,[2,4])
	node_4 = (4,None,[3,5,35])
	node_5 = (5,None,[4,35])
	node_6 = (6,None,[5,7,36])
	node_7 = (7,None,[6,8,17])
	node_8 = (8,None,[7,9,16])
	node_9 = (9,None,[8,15,16])
	node_10 = (10,None,[9,11,14])
	node_11 = (11,None,[10,12,14])
	node_12 = (12,None,[11,13,14])
	node_13 = (13,None,[12])
	node_14 = (14,None,[10,11,12,15])
	node_15 = (15,None,[9,14,16])
	node_16 = (16,None,[8,15,17])
	node_17 = (17,None,[7,16,18])
	node_18 = (18,None,[17,19])
	node_19 = (19,None,[18,20])
	node_20 = (20,None,[19,21])
	node_21 = (21,None,[20,22,38])
	node_22 = (22,None,[21,23,39])
	node_23 = (23,None,[22,24,40])
	node_24 = (24,None,[23,25,41])
	node_25 = (25,None,[24,26])
	node_26 = (26,None,[25,26,41])
	node_27 = (27,None,[26,28])
	node_28 = (28,None,[27,28,42])
	node_29 = (29,None,[28,30,43,44])
	node_30 = (30,None,[28,31])
	node_31 = (31,None,[30,32])
	node_32 = (32,None,[31,33])
	node_33 = (33,None,[32,34])
	node_34 = (34,None,[33,35])
	node_35 = (35,None,[4,5,34,36])
	node_36 = (36,None,[6,35,37])
	node_37 = (37,None,[36,38])
	node_38 = (38,None,[21,37,39])
	node_39 = (39,None,[22,38,40])
	node_40 = (40,None,[23,39,41])
	node_41 = (41,None,[24,26,40,42])
	node_42 = (42,None,[28,41,43])
	node_43 = (43,None,[28,42,44])
	node_44 = (44,None,[28,43])
#node_x = (slot,"color",[n1,n2...])
#second floor node initialization
	node_45 = (45,None,[46])
	node_46 = (46,None,[45,71])
	node_47 = (47,None,[48,71,73])
	node_48 = (48,None,[47,49,77])
	node_49 = (49,None,[48,50])
	node_50 = (50,None,[49,51])
	node_51 = (51,None,[50,52])
	node_52 = (52,None,[51,53])
	node_53 = (53,None,[52,54])
	node_54 = (54,None,[53,55])
	node_55 = (55,None,[52,56,78])
	node_56 = (56,None,[55,57,79])
	node_57 = (57,None,[56,58])
	node_58 = (58,None,[57,81])
	node_59 = (59,None,[60,81,82])
	node_60 = (60,None,[59,61,83])
	node_61 = (61,None,[60,62])
	node_62 = (62,None,[61,63])
	node_63 = (63,None,[62,64])
	node_64 = (64,None,[63,65,84])
	node_65 = (65,None,[64,66])
	node_66 = (66,None,[65,67])
	node_67 = (67,None,[66,68])
	node_68 = (68,None,[67,69])
	node_69 = (69,None,[68,70])
	node_70 = (70,None,[69,70])
	node_71 = (71,None,[46,47,70,72])
	node_72 = (72,None,[71,73])
	node_73 = (73,None,[47,72,74])
	node_74 = (74,None,[73,75])
	node_75 = (75,None,[74,76])
	node_76 = (76,None,[75,77])
	node_77 = (77,None,[48,76])
	node_78 = (78,None,[55,79])
	node_79 = (79,None,[56,78])
	node_80 = (80,None,[81,82])
	node_81 = (81,None,[58,59,80])
	node_82 = (82,None,[59,80])
	node_83 = (83,None,[60])
	node_84 = (84,None,[64])

#node_x = (slot,"color",[n1,n2...])

#first floor categories
	# categories_1 = {
	# 	F_MKT_INFO_MUSIC      :[36,37,11,13],
	# 	F_PRODUCE             :[7,8,9,16,18,19,20,23,24,28,30,34,43],
	# 	F_BAKES_GOODS         :[6,17,26,29,33],
	# 	F_DAIR_MEAT_EGGS      :[39,22,10,5,3,2,1],
	# 	F_COFFEE_SPECIALTY    :[25,21,15,14,4,35,32,31,44],
	# 	F_FLOWERS_PLANTS      :[12,40],
	# 	F_PREPARED_FOODS      :[27,41],
	# 	F_BEER_WINE_SPIRITS   :[38],
	# 	F_HANDMADE_GOODS  :[42]
	# }
#second floor categories
	# categories_2 = {
	# 	S_MKT_INFO_MUSIC      :[72],
	# 	S_PRODUCE             :[],
	# 	S_BAKES_GOODS         :[48,49,50,56,79,84,69],
	# 	S_DAIR_MEAT_EGGS      :[52,55,59],
	# 	S_COFFEE_SPECIALTY    :[71,51,34,57,58,80,83,61,64,67],
	# 	S_FLOWERS_PLANTS      :[],
	# 	S_PREPARED_FOODS      :[45,46,47,70,73,74,75,76,77],
	# 	S_BEER_WINE_SPIRITS   :[81,78,60,63,65,66],
	# 	S_HANDMADE_GOODS      :[53,62,68,82]
	# }

#dictionary of first floor colors
#colors_1 	COLOR : (K,N)
	colors_1 = [
		#color	=("COLOR",K,# of nodes left,collision)

		color("CYAN",0,4,None),
		color("GREEN",2,13,None),
		color("YELLOW",7,5,None),
		color("RED",5,7,None),
		color("BROWN",3,9,None),
		color("ORANGE",21,2,None),
		color("BLUE",21,2,None),
		color("PINK",0,1,None),
		color("PURPLE",43,1,None)

	]
#dictionary of second floor colors
#colors_2 	COLOR : (K,N)
	colors_2 = [
		#color	=("COLOR",K,# of nodes left,collision)

		color("CYAN",0,1,None),
		color("GREEN",0,0,None),
		color("YELLOW",5,6,None),
		color("RED",12,3,None),
		color("BROWN",3,10,None),
		color("ORANGE",0,0,None),
		color("BLUE",3,9,None),
		color("PINK",5,6,None),
		color("PURPLE",7,5,None)

	]

#list of first floor nodes
#nodes_1 = [n1,n2...]
	nodes_1 = [
		node_1,
		node_2,
		node_3,
		node_4,
		node_5,
		node_6,
		node_7,
		node_8,
		node_9,
		node_10,
		node_11,
		node_12,
		node_13,
		node_14,
		node_15,
		node_16,
		node_17,
		node_18,
		node_19,
		node_20,
		node_21,
		node_22,
		node_23,
		node_24,
		node_25,
		node_26,
		node_27,
		node_28,
		node_29,
		node_30,
		node_31,
		node_32,
		node_33,
		node_34,
		node_35,
		node_36,
		node_37,
		node_38,
		node_39,
		node_40,
		node_41,
		node_42,
		node_43,
		node_44
	]
#list of second floor nodes
#nodes_2 = [n1,n2...]
	nodes_2 = [
		node_45,
		node_46,
		node_47,
		node_48,
		node_49,
		node_50,
		node_51,
		node_52,
		node_53,
		node_54,
		node_55,
		node_56,
		node_57,
		node_58,
		node_59,
		node_60,
		node_61,
		node_62,
		node_63,
		node_64,
		node_65,
		node_66,
		node_67,
		node_68,
		node_69,
		node_70,
		node_71,
		node_72,
		node_73,
		node_74,
		node_75,
		node_76,
		node_77,
		node_78,
		node_79,
		node_80,
		node_81,
		node_82,
		node_83,
		node_84
	]

#initialize list of completed nodes
	final_graph = 84
#insert already first floor determined vendors
	n = nodes_1.index(node_38)
	n = (n[0],"red",n[2])
	final_graph -= 1
	print(n[0],n[1],n[2]) 


#TEST most_left
	(most_left(colors_1))

#TEST most_collide
	colorTest  = [	
		#color	=("COLOR",K,# of nodes left,collision)
		color("CYAN",0,4,4),
		color("GREEN",2,13,10),
		color("YELLOW",7,5,3),
		color("RED",5,7,5),
		color("BROWN",3,9,1),
		color("ORANGE",21,2,6),
		color("BLUE",21,2,9),
		color("PINK",0,1,2),
		color("PURPLE",43,1,8)
	]

	colorTest = most_collide(colorTest)
	for color in colorTest:
		print(color.color)
#run breadth frist algo to color nodes
