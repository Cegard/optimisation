# -*- coding: utf-8 -*-
from a_star import a_star


if __name__ == "__main__":
	
	for assignation in (list(a_star())):
		print (assignation.task, assignation.name)