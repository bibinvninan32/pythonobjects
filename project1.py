#!/bin/python
""" 
I'll add some scenarios here and we'll work through them and once completed I'll add more to it.
At all times this file should be able to run without error.
"""

# Step 1
# Create a class named 'Action'. 
# Within the class, create a constructor method (look it up if you're not sure).
# The constructor should take two lists as arguments (Look into positional vs named arguments). 
# Save those lists to a variable which would be accessible by every other method within the class (once we add more methods/functions).
#
print("check")

class Action:
	# class for different actions to be performed
	cls_basic_actions = []
	cls_advanced_actions = []

	''' uncomment to execute constructor method with takes positional aruments
	def __init__(self, basact, advact): # constructor method, assumes as positional one
		print("constructor method called")
		self.basacts = basact
		self.advacts = advact
		#print("base actions are " + str(self.basacts) + "and advanced actions are " + str(self.advacts))
		print ("base actions are ", end="")
		for x in self.basacts:
			print(x, end=", ")
		print ("\nadvanced actions are ", end="")
		for x in self.advacts:
			print(x, end=", ")
	'''	

    # constructor which takes named argements
	def __init__(self, adv, base): # constructor method, assumes as named one
		print("constructor method called")
		self.basacts = base
		self.advacts = adv
		#print("base actions are " + str(self.basacts) + "and advanced actions are " + str(self.advacts))

		# basic action section
		length_bas = len(self.basacts)
		print ("base actions are ", end="")
		for x in self.basacts:
			Action.cls_basic_actions.append(x)
			if self.basacts.index(x) != length_bas-1:
				print(x, end=", ")
			else:
				print(x)

		# basic action section
		length_adv = len(self.advacts)
		print ("advanced actions are ", end="")
		for x in self.advacts:
			Action.cls_advanced_actions.append(x)
			if self.advacts.index(x) != length_adv-1:
				print(x, end=", ")
			else:
				print(x, end="\n")


	def check_list():
		print(Action.cls_basic_actions)
		print(Action.cls_advanced_actions)





basic_actions = ['enquiry','withdraw','deposit', 'balance check'] # 1st list
advanced_actions = ['account opening', 'transfer', 'mustering'] # 2nd list
act_1 = Action(base=basic_actions, adv=advanced_actions)  # object initialization and passing arguemnt as named ones.


Action.check_list() #function to chek whether both the new list are accessible inside new functions inside the class.