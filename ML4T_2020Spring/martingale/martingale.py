"""Assess a betting strategy.

Copyright 2018, Georgia Institute of Technology (Georgia Tech)
Atlanta, Georgia 30332
All Rights Reserved

Template code for CS 4646/7646

Georgia Tech asserts copyright ownership of this template and all derivative
works, including solutions to the projects assigned in this course. Students
and other users of this template code are advised not to share it with others
or to make it available on publicly viewable websites including repositories
such as github and gitlab.  This copyright statement should not be removed
or edited.

We do grant permission to share solutions privately with non-students such
as potential employers. However, sharing with other current or future
students of CS 7646 is prohibited and subject to being investigated as a
GT honor code violation.

-----do not edit anything above this line---

Student Name: Tucker Balch (replace with your name)
GT User ID: tb34 (replace with your User ID)
GT ID: 900897987 (replace with your GT ID)
"""

import numpy as np
import matplotlib.pyplot as plt
import math


def author():
    return 'tb34'  # replace tb34 with your Georgia Tech username.


def gtid():
	return 900897987  # replace with your GT ID number


def get_spin_result(win_prob):
	result = False
	if np.random.random() <= win_prob:
		result = True
	return result

def simulate(win_prob):
	winnings = np.array([0])
	episode_winnings = 0

	for i in range(1000):
		while episode_winnings < 80:
			won = False
			bet_amount = 1
			while won == False:
				#bet_amount = bet_amount * 2
				won = get_spin_result(win_prob)
				if won == True:
					episode_winnings = episode_winnings + bet_amount
				else:
					episode_winnings = episode_winnings - bet_amount
					bet_amount = bet_amount * 2
				winnings = np.append(winnings, np.array([episode_winnings]))

		winnings = np.append(winnings, np.array([80]))
	
	return winnings

def test_code():
	win_prob = 0.474  # set appropriately to the probability of a win
	np.random.seed(gtid())  # do this only once
	#print(get_spin_result(win_prob)) # test the roulette spin
	# add your code here to implement the experiments
	
	"""""""""""""""
	"	Figure 1  "
	"""""""""""""""
	fig, axs = plt.subplots(5, 2, constrained_layout=True, figsize=(12, 12))
	fig.suptitle('Figure 1')
	for i in range(10):
		winnings = simulate(win_prob)
		col = 0 if i % 2 == 0 else 1
		row = math.floor(i/2)
		ax = axs[row, col]
		ax.plot(range(len(winnings)), winnings)
		ax.set_title('Run'+str(i+1))
		ax.label_outer()
		ax.set_xlim([0, 300])
		ax.set_ylim([-256, 100])

	plt.savefig('ML4T_2020Spring/martingale/figure_1.png')

	"""""""""""""""
	"	Figure 2  "
	"""""""""""""""
	fig2, ax2 = plt.subplots(1, 1)
	fig2.suptitle('Figure 2')
	mean = np.array([])
	std = np.array([])
	for i in range(1000):
		sim = simulate(win_prob)
		mean = np.append(mean, np.array([np.mean(sim)]))
		std = np.append(std, np.array([np.std(sim)]))

	xs = range(len(mean))
	ax2.plot(xs, mean, c='g')
	ax2.plot(xs, mean+std, c='b')
	ax2.plot(xs, mean-std, c='b')
	ax2.set_xlabel('Num os Simulations')
	ax2.set_ylabel('Mean +/- Std')
	ax2.set_xlim([0, 300])
	ax2.set_ylim([-256, 100])
	plt.savefig('ML4T_2020Spring/martingale/figure_2.png')

	"""""""""""""""
	"	Figure 3  "
	"""""""""""""""
	fig3, ax3 = plt.subplots(1, 1)
	fig3.suptitle('Figure 3')
	median = np.array([])
	std = np.array([])
	for i in range(1000):
		sim = simulate(win_prob)
		median = np.append(median, np.array([np.median(sim)]))
		std = np.append(std, np.array([np.std(sim)]))

	xs = range(len(median))
	ax3.plot(xs, median, c='g')
	ax3.plot(xs, median+std, c='b')
	ax3.plot(xs, median-std, c='b')
	ax3.set_xlabel('Num os Simulations')
	ax3.set_ylabel('Median +/- Std')
	ax3.set_xlim([0, 300])
	ax3.set_ylim([-256, 100])
	plt.savefig('ML4T_2020Spring/martingale/figure_3.png')

if __name__ == "__main__":  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
    test_code()  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
