class piano_key():

	def __init__(self, x1Bound,x2Bound, z1Bound, z2Bound):
		self.x1Bound=x1Bound  #the boundaries of the key (each key can be defined as a rectangle)
		self.x2Bound=x2Bound  #bound 1 is the lesser boundarx
		self.z1Bound=z1Bound
		self.z2Bound=z2Bound

	def is_pressed(self, bone):
		if(bone.next_joint.x>self.x1Bound and bone.next_joint.x<self.x2Bound and bone.next_joint.z>self.z1Bound and bone.next_joint.z<self.z2Bound): ##and bone.next_joint.z
			return True
		else:
			return False

def create_piano_keys():
	key0=piano_key(-153,-69,-124,-9)
	key1=piano_key(-153, -69,-9,100)
	key2=piano_key(-69,17,-124,-9)
	key3=piano_key(-69,17, -9, 100)
	key4=piano_key(17, 75, -124, -9)
	key5=piano_key(17, 75, -9, 100)
	return [key0, key1, key2, key3, key4, key5]
