class RandomPasswordGenerator:

	def genPass(self, trans):
		while (trans):
			print("Hey")
			transs = str(input("Run again? "))
			if(transs == "yes"):
				self.genPass(self, True)
			else:
				self.genPass(self, False)

t = RandomPasswordGenerator()
t.genPass(True)
