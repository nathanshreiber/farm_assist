

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
def assign_color(nodes_to_check,hops,index,colors,final_color):
	
	if final_color != None:				#base case
		return final_color

	hop = hops[index]					#find hop value
	node_n = nodes_to_check[index] 		#find node
	potential_nodes = append(node_n[2])	#potential children to add

	for n in potential_nodes:
		if n not in nodes_to_check:
			nodes_to_check.apend(n)		#add to list of nodes to check
			hops.append(hops[index]+1)  #add to list of hops

	
	if (node_n.color):					#accounts for alredy assigned nodes
		c = colors.get(node_n.color)		
		if c.collision == None:			#if no collision assign collision value
			c.collision = hop
		assign_color(nodes_tocheck,hops,index+1,colors,final_color)
		return final_color


	list_of_colors = most_left(colors)	#create list of colors in decreasing order of preseidence

	for color in list_of_colors:
		k = color.k
		
		if not color.collision or color.collision > k: 
			
			if hop <= k: 				#we havnt traveled far enough
				assign_color(nodes_to_check,hops,index+1,colors,final_color)

			if hop > k and color.number_left > 0:	#found color to assign
				return color.color

	#if we reach this point, every color has a colision or has 0 left to assign
	collision_colors = []

	for color in list_of_colors:				#add colors with collisions to list
		if color.number_left > 0:				
			collision_colors.append(color)

	if len(collision_colors) > 0:				#return least bad collision
		collision_colors = most_colide(collision_colors)
		return collision_colors[0].color

	#corner case we havnt thought of
	print("Failure")
	return final_color

def most_left(colorsList):
	return sorted(colorsList,most_left_compare)

def most_left(colorsList):
	colorsList = sorted(colorsList,key=most_left_compare,reverse=True)
	return colorsList

def most_left_compare(color1):
	return color1.number_left, color1.k

def most_left_compare(color1):
	return color1.number_left, color1.k

if __name__ == '__main__':
	
#first floor node initialization
	node_1 = node(node_1,None,[node_2])
	node_2 = node(node_2,None,[node_1,node_3])
	node_3 = node(node_3,None,[node_2,node_4])
	node_4 = node(node_4,None,[node_3,node_5,node_35])
	node_5 = node(node_5,None,[node_4,node_35])
	node_6 = node(node_6,None,[node_5,node_7,node_36])
	node_7 = node(node_7,None,[node_6,node_8,node_17])
	node_8 = node(node_8,None,[node_7,node_9,node_16])
	node_9 = node(node_9,None,[node_8,node_15,node_16])
	node_10 = node(node_10,None,[node_9,node_11,node_14])
	node_11 = node(node_11,None,[node_10,node_12,node_14])
	node_12 = node(node_12,None,[node_11,node_13,node_14])
	node_13 = node(node_13,None,[node_12])
	node_14 = node(node_14,None,[node_10,node_11,node_12,node_15])
	node_15 = node(node_15,None,[node_9,node_14,node_16])
	node_16 = node(node_16,None,[node_8,node_15,node_17])
	node_17 = node(node_17,None,[node_7,node_16,node_18])
	node_18 = node(node_18,None,[node_17,node_19])
	node_19 = node(node_19,None,[node_18,node_20])
	node_20 = node(node_20,None,[node_19,node_21])
	node_21 = node(node_21,None,[node_20,node_22,node_38])
	node_22 = node(node_22,None,[node_21,node_23,node_39])
	node_23 = node(node_23,None,[node_22,node_24,node_40])
	node_24 = node(node_24,None,[node_23,node_25,node_41])
	node_25 = node(node_25,None,[node_24,node_26])
	node_26 = node(node_26,None,[node_25,node_26,node_41])
	node_27 = node(node_27,None,[node_26,node_28])
	node_28 = node(node_28,None,[node_27,node_28,node_42])
	node_29 = node(node_29,None,[node_28,node_30,node_43,node_44])
	node_30 = node(node_30,None,[node_28,node_31])
	node_31 = node(node_31,None,[node_30,node_32])
	node_32 = node(node_32,None,[node_31,node_33])
	node_33 = node(node_33,None,[node_32,node_34])
	node_34 = node(node_34,None,[node_33,node_35])
	node_35 = node(node_35,None,[node_4,node_5,node_34,node_36])
	node_36 = node(node_36,None,[node_6,node_35,node_37])
	node_37 = node(node_37,None,[node_36,node_38])
	node_38 = node(node_38,None,[node_21,node_37,node_39])
	node_39 = node(node_39,None,[node_22,node_38,node_40])
	node_40 = node(node_40,None,[node_23,node_39,node_41])
	node_41 = node(node_41,None,[node_24,node_26,node_40,node_42])
	node_42 = node(node_42,None,[node_28,node_41,node_43])
	node_43 = node(node_43,None,[node_28,node_42,node_44])
	node_44 = node(node_44,None,[node_28,node_43])
#node_x = (slot,"color",[n1,n2...])
#second floor node initialization
	node_45 = node(node_45,None,[node_46])
	node_46 = node(node_46,None,[node_45,node_71])
	node_47 = node(node_47,None,[node_48,node_71,node_73])
	node_48 = node(node_48,None,[node_47,node_49,node_77])
	node_49 = node(node_49,None,[node_48,node_50])
	node_50 = node(node_50,None,[node_49,node_51])
	node_51 = node(node_51,None,[node_50,node_52])
	node_52 = node(node_52,None,[node_51,node_53])
	node_53 = node(node_53,None,[node_52,node_54])
	node_54 = node(node_54,None,[node_53,node_55])
	node_55 = node(node_55,None,[node_52,node_56,node_78])
	node_56 = node(node_56,None,[node_55,node_57,node_79])
	node_57 = node(node_57,None,[node_56,node_58])
	node_58 = node(node_58,None,[node_57,node_81])
	node_59 = node(node_59,None,[node_60,node_81,node_82])
	node_60 = node(node_60,None,[node_59,node_61,node_83])
	node_61 = node(node_61,None,[node_60,node_62])
	node_62 = node(node_62,None,[node_61,node_63])
	node_63 = node(node_63,None,[node_62,node_64])
	node_64 = node(node_64,None,[node_63,node_65,node_84])
	node_65 = node(node_65,None,[node_64,node_66])
	node_66 = node(node_66,None,[node_65,node_67])
	node_67 = node(node_67,None,[node_66,node_68])
	node_68 = node(node_68,None,[node_67,node_69])
	node_69 = node(node_69,None,[node_68,node_70])
	node_70 = node(node_70,None,[node_69,node_70])
	node_71 = node(node_71,None,[node_46,node_47,node_70,node_72])
	node_72 = node(node_72,None,[node_71,node_73])
	node_73 = node(node_73,None,[node_47,node_72,node_74])
	node_74 = node(node_74,None,[node_73,node_75])
	node_75 = node(node_75,None,[node_74,node_76])
	node_76 = node(node_76,None,[node_75,node_77])
	node_77 = node(node_77,None,[node_48,node_76])
	node_78 = node(node_78,None,[node_55,node_79])
	node_79 = node(node_79,None,[node_56,node_78])
	node_80 = node(node_80,None,[node_81,node_82])
	node_81 = node(node_81,None,[node_58,node_59,node_80])
	node_82 = node(node_82,None,[node_59,node_80])
	node_83 = node(node_83,None,[node_60])
	node_84 = node(node_84,None,[node_64])
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

#run breadth frist algo to color nodes
