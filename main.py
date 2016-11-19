# -*- coding: utf-8 -*-
from a_star import a_star
from estimatees import get_estimation


if __name__ == "__main__":
	
	for assignation in a_star():
		print (assignation.task, assignation.name)