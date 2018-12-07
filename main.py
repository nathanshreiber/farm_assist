import random

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


	list_of_colors = most_left(colors)	#create list of colors in decreasing order of precedence


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
		collision_colors = most_collide(collision_colors)
		return collision_colors[0].color

	#corner case we havnt thought of
	print("Failure")
	return final_color

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
	node_1 = node(1,None,None)
	node_2 = node(2,None,None)
	node_3 = node(3,None,None)
	node_4 = node(4,None,None)
	node_5 = node(5,None,None)
	node_6 = node(6,None,None)
	node_7 = node(7,None,None)
	node_8 = node(8,None,None)
	node_9 = node(9,None,None)
	node_10 = node(10,None,None)
	node_11 = node(11,None,None)
	node_12 = node(12,None,None)
	node_13 = node(13,None,None)
	node_14 = node(14,None,None)
	node_15 = node(15,None,None)
	node_16 = node(16,None,None)
	node_17 = node(17,None,None)
	node_18 = node(18,None,None)
	node_19 = node(19,None,None)
	node_20 = node(20,None,None)
	node_21 = node(21,None,None)
	node_22 = node(22,None,None)
	node_23 = node(23,None,None)
	node_24 = node(24,None,None)
	node_25 = node(25,None,None)
	node_26 = node(26,None,None)
	node_27 = node(27,None,None)
	node_28 = node(28,None,None)
	node_29 = node(29,None,None)
	node_30 = node(30,None,None)
	node_31 = node(31,None,None)
	node_32 = node(32,None,None)
	node_33 = node(33,None,None)
	node_34 = node(34,None,None)
	node_35 = node(35,None,None)
	node_36 = node(36,None,None)
	node_37 = node(37,None,None)
	node_38 = node(38,None,None)
	node_39 = node(39,None,None)
	node_40 = node(40,None,None)
	node_41 = node(41,None,None)
	node_42 = node(42,None,None)
	node_43 = node(43,None,None)
	node_44 = node(44,None,None)

	floor_1 = [
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

	node_1.children = [node_2]
	node_2.children = [node_1,node_3]
	node_3.children = [node_2,node_4]
	node_4.children = [node_3,node_5,node_35]
	node_5.children = [node_4,node_35]
	node_6.children = [node_5,node_7,node_36]
	node_7.children = [node_6,node_8,node_17]
	node_8.children = [node_7,node_9,node_16]
	node_9.children = [node_8,node_15,node_16]
	node_10.children = [node_9,node_11,node_14]
	node_11.children = [node_10,node_12,node_14]
	node_12.children = [node_11,node_13,node_14]
	node_13.children = [node_12]
	node_14.children = [node_10,node_11,node_12,node_15]
	node_15.children = [node_9,node_14,node_16]
	node_16.children = [node_8,node_15,node_17]
	node_17.children = [node_7,node_16,node_18]
	node_18.children = [node_17,node_19]
	node_19.children = [node_18,node_20]
	node_20.children = [node_19,node_21]
	node_21.children = [node_20,node_22,node_38]
	node_22.children = [node_21,node_23,node_39]
	node_23.children = [node_22,node_24,node_40]
	node_24.children = [node_23,node_25,node_41]
	node_25.children = [node_24,node_26]
	node_26.children = [node_25,node_26,node_41]
	node_27.children = [node_26,node_28]
	node_28.children = [node_27,node_28,node_42]
	node_29.children = [node_28,node_30,node_43,node_44]
	node_30.children = [node_28,node_31]
	node_31.children = [node_30,node_32]
	node_32.children = [node_31,node_33]
	node_33.children = [node_32,node_34]
	node_34.children = [node_33,node_35]
	node_35.children = [node_4,node_5,node_34,node_36]
	node_36.children = [node_6,node_35,node_37]
	node_37.children = [node_36,node_38]
	node_38.children = [node_21,node_37,node_39]
	node_39.children = [node_22,node_38,node_40]
	node_40.children = [node_23,node_39,node_41]
	node_41.children = [node_24,node_26,node_40,node_42]
	node_42.children = [node_28,node_41,node_43]
	node_43.children = [node_28,node_42,node_44]
	node_44.children = [node_28,node_43]
#node_x = (slot,"color",[n1,n2...])
#second floor node initialization
	node_45 = node(45,None,None)
	node_46 = node(46,None,None)
	node_47 = node(47,None,None)
	node_48 = node(48,None,None)
	node_49 = node(49,None,None)
	node_50 = node(50,None,None)
	node_51 = node(51,None,None)
	node_52 = node(52,None,None)
	node_53 = node(53,None,None)
	node_54 = node(54,None,None)
	node_55 = node(55,None,None)
	node_56 = node(56,None,None)
	node_57 = node(57,None,None)
	node_58 = node(58,None,None)
	node_59 = node(59,None,None)
	node_60 = node(60,None,None)
	node_61 = node(61,None,None)
	node_62 = node(62,None,None)
	node_63 = node(63,None,None)
	node_64 = node(64,None,None)
	node_65 = node(65,None,None)
	node_66 = node(66,None,None)
	node_67 = node(67,None,None)
	node_68 = node(68,None,None)
	node_69 = node(69,None,None)
	node_70 = node(70,None,None)
	node_71 = node(71,None,None)
	node_72 = node(72,None,None)
	node_73 = node(73,None,None)
	node_74 = node(74,None,None)
	node_75 = node(75,None,None)
	node_76 = node(76,None,None)
	node_77 = node(77,None,None)
	node_78 = node(78,None,None)
	node_79 = node(79,None,None)
	node_80 = node(80,None,None)
	node_81 = node(81,None,None)
	node_82 = node(82,None,None)
	node_83 = node(83,None,None)
	node_84 = node(84,None,None)

	node_45.children = [node_46]
	node_46.children = [node_45,node_71]
	node_47.children = [node_48,node_71,node_73]
	node_48.children = [node_47,node_49,node_77]
	node_49.children = [node_48,node_50]
	node_50.children = [node_49,node_51]
	node_51.children = [node_50,node_52]
	node_52.children = [node_51,node_53]
	node_53.children = [node_52,node_54]
	node_54.children = [node_53,node_55]
	node_55.children = [node_52,node_56,node_78]
	node_56.children = [node_55,node_57,node_79]
	node_57.children = [node_56,node_58]
	node_58.children = [node_57,node_81]
	node_59.children = [node_60,node_81,node_82]
	node_60.children = [node_59,node_61,node_83]
	node_61.children = [node_60,node_62]
	node_62.children = [node_61,node_63]
	node_63.children = [node_62,node_64]
	node_64.children = [node_63,node_65,node_84]
	node_65.children = [node_64,node_66]
	node_66.children = [node_65,node_67]
	node_67.children = [node_66,node_68]
	node_68.children = [node_67,node_69]
	node_69.children = [node_68,node_70]
	node_70.children = [node_69,node_70]
	node_71.children = [node_46,node_47,node_70,node_72]
	node_72.children = [node_71,node_73]
	node_73.children = [node_47,node_72,node_74]
	node_74.children = [node_73,node_75]
	node_75.children = [node_74,node_76]
	node_76.children = [node_75,node_77]
	node_77.children = [node_48,node_76]
	node_78.children = [node_55,node_79]
	node_79.children = [node_56,node_78]
	node_80.children = [node_81,node_82]
	node_81.children = [node_58,node_59,node_80]
	node_82.children = [node_59,node_80]
	node_83.children = [node_60]
	node_84.children = [node_64]

	floor_2 = [
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
		node_84]

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



#initialize list of completed nodes
	final_graph = 84
#insert already first floor determined vendors
	# n = nodes_1.pop(index(node_38))
	# n = (n[0],"red",n[2])
	# final_graph -= 1
	# print(n[0],n[1],n[2]) 


# #TEST most_left
# 	(most_left(colors_1))

# #TEST most_collide
# 	colorTest  = [	
# 		#color	=("COLOR",K,# of nodes left,collision)
# 		color("CYAN",0,4,4),
# 		color("GREEN",2,13,10),
# 		color("YELLOW",7,5,3),
# 		color("RED",5,7,5),
# 		color("BROWN",3,9,1),
# 		color("ORANGE",21,2,6),
# 		color("BLUE",21,2,9),
# 		color("PINK",0,1,2),
# 		color("PURPLE",43,1,8)
# 	]



#Test nodes
	test_1 = node(1,None,None)
	test_2 = node(2,None,None)
	test_3 = node(3,None,None)
	test_4 = node(4,None,None)
	test_5 = node(5,None,None)
	test_6 = node(6,None,None)
	test_7 = node(7,None,None)
	test_8 = node(8,None,None)
	test_9 = node(9,None,None)
	test_10 = node(10,None,None)
#Test Neighbors
	test_1.neighbors = [test_2,test_10]
	test_2.neighbors = [test_1,test_3]
	test_3.neighbors = [test_2,test_4,test_5]
	test_4.neighbors = [test_3,test_5]
	test_5.neighbors = [test_3,test_4,test_6]
	test_6.neighbors = [test_5,test_7]
	test_7.neighbors = [test_6,test_8]
	test_8.neighbors = [test_7,test_9]
	test_10.neighbors = [test_1,test_9]
#Test Colors
	color_test = {
		"RED" : color("RED", 4,2,None)
		"YELLOW" : color("YELLOW",1,5,None)
		"BLUE" : color("BLUE",2,3,None)
	}


# 	colorTest = most_collide(colorTest)
# 	for color in colorTest:
# 		print(color.color)
# #run breadth frist algo to color nodes
	order1 = random.sample(range(0,44),44)
	order2 = random.sample(range(0,40),40)
	print(order1)
	print(order2)




	final_graph = len(order1)
	for i in order1:
		print(floor_1[i].children)