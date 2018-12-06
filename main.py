

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
def assign_color(nodes_to_check,index,colors):
	
	node = nodex_to_check[index] 		#find node
	nodes_to_check.append(node[2])		#add node's children to nodes_to_check
	list_of_colors = most_left(colors)	#create list of colors in decreasing order of preseidence
	
	if (node.color )
	for color in list_of_colors:
		temp = colors.get(color)
		k = temp.k


def most_left(colorsList):
	return sorted(colorsList,most_left_compare)


def most_left_compare(color1):
	return color1.number_left, color1.k

if __name__ == '__main__':
	
#first floor node initialization
	node_1 = (1,"",[node_2])
	node_2 = (2,"",[node_1,node_3])
	node_3 = (3,"",[node_2,node_4])
	node_4 = (4,"",[node_3,node_5,node_35])
	node_5 = (5,"",[node_4,node_35])
	node_6 = (6,"",[node_5,node_7,node_36])
	node_7 = (7,"",[node_6,node_8,node_17])
	node_8 = (8,"",[node_7,node_9,node_16])
	node_9 = (9,"",[node_8,node_15,node_16])
	node_10 = (10,"",[node_9,node_11,node_14])
	node_11 = (11,"",[node_10,node_12,node_14])
	node_12 = (12,"",[node_11,node_13,node_14])
	node_13 = (13,"",[node_12])
	node_14 = (14,"",[node_10,node_11,node_12,node_15])
	node_15 = (15,"",[node_9,node_14,node_16])
	node_16 = (16,"",[node_8,node_15,node_17])
	node_17 = (17,"",[node_7,node_16,node_18])
	node_18 = (18,"",[node_17,node_19])
	node_19 = (19,"",[node_18,node_20])
	node_20 = (20,"",[node_19,node_21])
	node_21 = (21,"",[node_20,node_22,node_38])
	node_22 = (22,"",[node_21,node_23,node_39])
	node_23 = (23,"",[node_22,node_24,node_40])
	node_24 = (24,"",[node_23,node_25,node_41])
	node_25 = (25,"",[node_24,node_26])
	node_26 = (26,"",[node_25,node_26,node_41])
	node_27 = (27,"",[node_26,node_28])
	node_28 = (28,"",[node_27,node_28,node_42])
	node_29 = (29,"",[node_28,node_30,node_43,node_44])
	node_30 = (30,"",[node_28,node_31])
	node_31 = (31,"",[node_30,node_32])
	node_32 = (32,"",[node_31,node_33])
	node_33 = (33,"",[node_32,node_34])
	node_34 = (34,"",[node_33,node_35])
	node_35 = (35,"",[node_4,node_5,node_34,node_36])
	node_36 = (36,"",[node_6,node_35,node_37])
	node_37 = (37,"",[node_36,node_38])
	node_38 = (38,"",[node_21,node_37,node_39])
	node_39 = (39,"",[node_22,node_38,node_40])
	node_40 = (40,"",[node_23,node_39,node_41])
	node_41 = (41,"",[node_24,node_26,node_40,node_42])
	node_42 = (42,"",[node_28,node_41,node_43])
	node_43 = (43,"",[node_28,node_42,node_44])
	node_44 = (44,"",[node_28,node_43])
#node_x = (slot,"color",[n1,n2...])
#second floor node initialization
	node_45 = (45,"",[node_46])
	node_46 = (46,"",[node_45,node_71])
	node_47 = (47,"",[node_48,node_71,node_73])
	node_48 = (48,"",[node_47,node_49,node_77])
	node_49 = (49,"",[node_48,node_50])
	node_50 = (50,"",[node_49,node_51])
	node_51 = (51,"",[node_50,node_52])
	node_52 = (52,"",[node_51,node_53])
	node_53 = (53,"",[node_52,node_54])
	node_54 = (54,"",[node_53,node_55])
	node_55 = (55,"",[node_52,node_56,node_78])
	node_56 = (56,"",[node_55,node_57,node_79])
	node_57 = (57,"",[node_56,node_58])
	node_58 = (58,"",[node_57,node_81])
	node_59 = (59,"",[node_60,node_81,node_82])
	node_60 = (60,"",[node_59,node_61,node_83])
	node_61 = (61,"",[node_60,node_62])
	node_62 = (62,"",[node_61,node_63])
	node_63 = (63,"",[node_62,node_64])
	node_64 = (64,"",[node_63,node_65,node_84])
	node_65 = (65,"",[node_64,node_66])
	node_66 = (66,"",[node_65,node_67])
	node_67 = (67,"",[node_66,node_68])
	node_68 = (68,"",[node_67,node_69])
	node_69 = (69,"",[node_68,node_70])
	node_70 = (70,"",[node_69,node_70])
	node_71 = (71,"",[node_46,node_47,node_70,node_72])
	node_72 = (72,"",[node_71,node_73])
	node_73 = (73,"",[node_47,node_72,node_74])
	node_74 = (74,"",[node_73,node_75])
	node_75 = (75,"",[node_74,node_76])
	node_76 = (76,"",[node_75,node_77])
	node_77 = (77,"",[node_48,node_76])
	node_78 = (78,"",[node_55,node_79])
	node_79 = (79,"",[node_56,node_78])
	node_80 = (80,"",[node_81,node_82])
	node_81 = (81,"",[node_58,node_59,node_80])
	node_82 = (82,"",[node_59,node_80])
	node_83 = (83,"",[node_60])
	node_84 = (84,"",[node_64])
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


		CYAN=("CYAN",0,4,NULL),
		GREEN=("GREEN",2,13,NULL),
		YELLOW=("YELLOW",7,5,NULL),
		RED=("RED",5,7,NULL),
		BROWN=("BROWN",3,9,NULL),
		ORANGE=("ORANGE",21,2,NULL),
		BLUE=("BLUE",21,2,NULL),
		PINK=("PINK",0,1,NULL),
		PURPLE=("PURPLE",43,1,NULL)

	]
#dictionary of second floor colors
#colors_2 	COLOR : (K,N)
	colors_2 = [
		#color	=("COLOR",K,# of nodes left,collision)
		"CYAN" 	= ("CYAN",0,1,NULL),
		"GREEN" = ("GREEN",0,0,NULL),
		"YELLOW"= ("YELLOW",5,6,NULL),
		"RED" 	= ("RED",12,3,NULL),
		"BROWN"	= ("BROWN",3,10,NULL),
		"ORANGE"= ("ORANGE",0,0,NULL),
		"BLUE" 	= ("BLUE",3,9,NULL),
		"PINK" 	= ("PINK",5,6,NULL),
		"PURPLE"= ("PURPLE",7,5,NULL)
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
print(most_left(colors_1))
#run breadth frist algo to color nodes
