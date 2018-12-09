import random
#import pdb

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
	#pdb.set_trace()
	print("Node: "+str(nodes_to_check[index].slot)+" Hop: "+str(hops[index]))
	if final_color != None:						#base case
		return final_color

	hop = hops[index]							#find hop value
	node_n = nodes_to_check[index] 				#find node
	potential_nodes = []
	potential_nodes.extend(node_n.neighbors)	#adds neighbors of current node t0
												#potential nodes 
	
	for n in potential_nodes:					
		if n not in nodes_to_check:
			nodes_to_check.append(n)			#add to list of nodes to check
			hops.append(hops[index]+1) 			#add to list of hops
	
	#for x in nodes_to_check:
		#print("Nodes to Check: "+str(x.slot))
	
	#pdb.set_trace();
	if (node_n.color != None):					#accounts for alredy assigned nodes
		c = colors[node_n.color]	 	
		if c.collision == None:			#if no collision assign collision value
			c.collision = hop     	
		#pdb.set_trace();
		#ADDING INDEX CHECK               IDEA 1
		if index + 1 < len(hops):
			final_color = assign_color(nodes_to_check,hops,index + 1,colors,final_color) #Also goes out of index
			return final_color
		#else:  							IDEA 2
			#final_color = assign_color(nodes_to_check,hops,index + 1,colors,final_color)
		#return final_color

	list_of_colors = []
	for i in colors:
		list_of_colors.append(colors[i])
	list_of_colors = most_left(list_of_colors)	#create list of colors in decreasing order of precedence

	#pdb.set_trace()
	for color in list_of_colors:
		k = color.k
		#not sure if color.collision ever gets properly changed 
		if color.collision == None or color.collision > k: 
			print("HOP "+str(hop)+" K "+str(k))
			if hop <= k: 				#we havnt traveled far enough

				#ADDING INDEX CHECK    						IDEA 1
				if index + 1 < len(hops):
					final_color = assign_color(nodes_to_check,hops,index+1,colors,final_color) #Problematic asf
					return final_color
				#else:										IDEA 2
					#final_color = assign_color(nodes_to_check,hops,index+1,colors,final_color)
				#return final_color
			
			if hop > k and color.number_left > 0:	#found color to assign
				#pdb.set_trace();
				for c in list_of_colors:					#collisions reset to null
					c.collision = None
				#print(color.color)
				return color.color

	#if we reach this point, every color has a colision or has 0 left to assign
	collision_colors = []
	#pdb.set_trace();
	for color in list_of_colors:				#add colors with collisions to list
		if color.number_left > 0:				
			collision_colors.append(color) 		
		print()
		print(color.color+str(color.k))
	#pdb.set_trace();
	if len(collision_colors) > 0:				#return least bad collision
		collision_colors = most_collide(collision_colors)
		for c in colors:					#collisions reset to null
			#bug fix
			colors[c].collision = None
		return collision_colors[0].color

	#corner case we havnt thought of
	print("Failure")
	return final_color

def most_left(colorsList):
	return sorted(colorsList,key=most_left_compare)

def most_left_compare(color1):
	#CHANGED: Switched
	return color1.k, color1.number_left

#pass a list of OBj colors (some of them)
#return list sorted by how bad their collision was as a percentage
# percentage = collsion / k 
#larger the percentage, better priority -> 1 being the best 
def most_collide(colorList):
	for color in colorList:
		#Getting an error here 
		#FIX
		if color.collision is None:
			color.collision = 0
		else:
			color.collision = color.collision - color.k
	return sorted(colorList,key=most_collide_compare)

def most_collide_compare(color1):
	#color.numleft switched to color1.k
	return color1.collision, color1.k

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

	node_1.neighbors = [node_2]
	node_2.neighbors = [node_1,node_3]
	node_3.neighbors = [node_2,node_4]
	node_4.neighbors = [node_3,node_5,node_35]
	node_5.neighbors = [node_4,node_35]
	node_6.neighbors = [node_5,node_7,node_36]
	node_7.neighbors = [node_6,node_8,node_17]
	node_8.neighbors = [node_7,node_9,node_16]
	node_9.neighbors = [node_8,node_15,node_16]
	node_10.neighbors = [node_9,node_11,node_14]
	node_11.neighbors = [node_10,node_12,node_14]
	node_12.neighbors = [node_11,node_13,node_14]
	node_13.neighbors = [node_12]
	node_14.neighbors = [node_10,node_11,node_12,node_15]
	node_15.neighbors = [node_9,node_14,node_16]
	node_16.neighbors = [node_8,node_15,node_17]
	node_17.neighbors = [node_7,node_16,node_18]
	node_18.neighbors = [node_17,node_19]
	node_19.neighbors = [node_18,node_20]
	node_20.neighbors = [node_19,node_21]
	node_21.neighbors = [node_20,node_22,node_38]
	node_22.neighbors = [node_21,node_23,node_39]
	node_23.neighbors = [node_22,node_24,node_40]
	node_24.neighbors = [node_23,node_25,node_41]
	node_25.neighbors = [node_24,node_26]
	node_26.neighbors = [node_25,node_26,node_41]
	node_27.neighbors = [node_26,node_28]
	node_28.neighbors = [node_27,node_28,node_42]
	node_29.neighbors = [node_28,node_30,node_43,node_44]
	node_30.neighbors = [node_28,node_31]
	node_31.neighbors = [node_30,node_32]
	node_32.neighbors = [node_31,node_33]
	node_33.neighbors = [node_32,node_34]
	node_34.neighbors = [node_33,node_35]
	node_35.neighbors = [node_4,node_5,node_34,node_36]
	node_36.neighbors = [node_6,node_35,node_37]
	node_37.neighbors = [node_36,node_38]
	node_38.neighbors = [node_21,node_37,node_39]
	node_39.neighbors = [node_22,node_38,node_40]
	node_40.neighbors = [node_23,node_39,node_41]
	node_41.neighbors = [node_24,node_26,node_40,node_42]
	node_42.neighbors = [node_28,node_41,node_43]
	node_43.neighbors = [node_28,node_42,node_44]
	node_44.neighbors = [node_28,node_43]
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

	node_45.neighbors = [node_46]
	node_46.neighbors = [node_45,node_71]
	node_47.neighbors = [node_48,node_71,node_73]
	node_48.neighbors = [node_47,node_49,node_77]
	node_49.neighbors = [node_48,node_50]
	node_50.neighbors = [node_49,node_51]
	node_51.neighbors = [node_50,node_52]
	node_52.neighbors = [node_51,node_53]
	node_53.neighbors = [node_52,node_54]
	node_54.neighbors = [node_53,node_55]
	node_55.neighbors = [node_52,node_56,node_78]
	node_56.neighbors = [node_55,node_57,node_79]
	node_57.neighbors = [node_56,node_58]
	node_58.neighbors = [node_57,node_81]
	node_59.neighbors = [node_60,node_81,node_82]
	node_60.neighbors = [node_59,node_61,node_83]
	node_61.neighbors = [node_60,node_62]
	node_62.neighbors = [node_61,node_63]
	node_63.neighbors = [node_62,node_64]
	node_64.neighbors = [node_63,node_65,node_84]
	node_65.neighbors = [node_64,node_66]
	node_66.neighbors = [node_65,node_67]
	node_67.neighbors = [node_66,node_68]
	node_68.neighbors = [node_67,node_69]
	node_69.neighbors = [node_68,node_70]
	node_70.neighbors = [node_69,node_70]
	node_71.neighbors = [node_46,node_47,node_70,node_72]
	node_72.neighbors = [node_71,node_73]
	node_73.neighbors = [node_47,node_72,node_74]
	node_74.neighbors = [node_73,node_75]
	node_75.neighbors = [node_74,node_76]
	node_76.neighbors = [node_75,node_77]
	node_77.neighbors = [node_48,node_76]
	node_78.neighbors = [node_55,node_79]
	node_79.neighbors = [node_56,node_78]
	node_80.neighbors = [node_81,node_82]
	node_81.neighbors = [node_58,node_59,node_80]
	node_82.neighbors = [node_59,node_80]
	node_83.neighbors = [node_60]
	node_84.neighbors = [node_64]

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
	colors_2 = {
		#color	=("COLOR",K,# of nodes left,collision)

		"CYAN" : color("CYAN",0,1,None),
		"GREEN" : ("GREEN",0,0,None),
		"YELLOW" : color("YELLOW",5,6,None),
		"RED" : color("RED",12,3,None),
		"BROWN" : color("BROWN",3,10,None),
		"ORANGE" : color("ORANGE",0,0,None),
		"BLUE" : color("BLUE",3,9,None),
		"PINK" : color("PINK",5,6,None),
		"PURPLE" : color("PURPLE",7,5,None)

	}



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
	test_9.neighbors = [test_8,test_10]
	test_10.neighbors = [test_1,test_9]
#Test Colors
	color_test = {
		"RED" : color("RED", 4,2,None),
		"YELLOW" : color("YELLOW",1,5,None),
		"BLUE" : color("BLUE",2,3,None)
	}
#Test List
	test_list = [
		test_1,
		test_2,
		test_3,
		test_4,
		test_5,
		test_6,
		test_7,
		test_8,
		test_9,
		test_10]


# 	colorTest = most_collide(colorTest)
# 	for color in colorTest:
# 		print(color.color)
# #run breadth frist algo to color nodes
	order1 = random.sample(range(0,44),44)
	order2 = random.sample(range(0,40),40)
	print(order1)
	print(order2)


	#order3 = random.sample(range(0,10),10)
	order3 = [9,8,3,1,7,4,0,2,5,6]
	print(order3)

	final_graph = len(order3)
	for i in order3:
		colour = assign_color([test_list[i]],[0],0,color_test,None)
		color_test[colour].number_left = color_test[colour].number_left -1
		#BUG FIX? assigning the color to the node we just found the color to
		test_list[i].color = colour 
		print("Slot: "+str(floor_1[i].slot)+" Color: "+colour)
