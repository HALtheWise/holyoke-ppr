class piano_key(y1Bound,y2Bound, z1Bound, z2Bound):
	
	def __init__(self):
		self.y1Bound=y1Bound  #the boundaries of the key (each key can be defined as a rectangle)
		self.y2Bound=y2Bound  #bound 1 is the lesser boundary
		self.z1Bound=z1Bound
		self.z2Bound=z2Bound

	def is_pressed(self, bone):
		if(bone.next_joint.y>y1Bound and bone.next_joint.y<y2Bound and bone.next_joint.z>z1Bound and bone.next_joint.z<z2Bound): ##and bone.next_joint.z
			return true
		else:
			return false

def create_piano_keys():
	key0=piano_key(-153,-69,-124,-9)
	key1=piano_key(-153, -69,-9,100)
	key2=piano_key(-69,17,-124,-9)
	key3=piano_key(-69,17, -9, 100)
	key4=piano_key(17, 75, -124, -9)
	key5=piano_key(17, 75, -9, 100)
	return (key0, key1, key2, key3, key4, key5)