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

def simulate(win_prob, bankroll = None):
	winnings = np.array([0])
	episode_winnings = 0
	max_bankroll = False

	for i in range(1000):
		while episode_winnings < 80 and max_bankroll is False:
			won = False
			bet_amount = 1
			
			while won == False:

				if bankroll is not None and bet_amount > bankroll:
					print('bet is more than bankroll')
					bet_amount = bankroll
	
				won = get_spin_result(win_prob)
				if won == True:
					episode_winnings = episode_winnings + bet_amount
				else:
					episode_winnings = episode_winnings - bet_amount
					bet_amount = bet_amount * 2

				if bankroll is not None and episode_winnings <= -bankroll:
					#print('max bankroll reached')
					max_bankroll = True
					break;

				winnings = np.append(winnings, np.array([episode_winnings]))

		if max_bankroll is True:
			winnings = np.append(winnings, np.array([-bankroll]))
		else:
			winnings = np.append(winnings, np.array([80]))

	#print(winnings)
	#print(np.min(winnings))
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
	mean2 = np.array([])
	std2 = np.array([])
	for i in range(1000):
		sim2 = simulate(win_prob)
		mean2 = np.append(mean2, np.array([np.mean(sim2)]))
		std2 = np.append(std2, np.array([np.std(sim2)]))

	xs2 = range(len(mean2))
	ax2.plot(xs2, mean2, c='g')
	ax2.plot(xs2, mean2+std2, c='b', alpha=0.5)
	ax2.plot(xs2, mean2-std2, c='b', alpha=0.5)
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
	median3 = np.array([])
	std3 = np.array([])
	for i in range(1000):
		sim3 = simulate(win_prob)
		median3 = np.append(median3, np.array([np.median(sim3)]))
		std3 = np.append(std3, np.array([np.std(sim3)]))

	xs3 = range(len(median3))
	ax3.plot(xs3, median3, c='g')
	ax3.plot(xs3, median3+std3, c='b', alpha=0.5)
	ax3.plot(xs3, median3-std3, c='b', alpha=0.5)
	ax3.set_xlabel('Num os Simulations')
	ax3.set_ylabel('Median +/- Std')
	ax3.set_xlim([0, 300])
	ax3.set_ylim([-256, 100])
	plt.savefig('ML4T_2020Spring/martingale/figure_3.png')


	"""""""""""""""
	"	Figure 4  "
	"""""""""""""""
	fig4, ax4 = plt.subplots(1, 1)
	fig4.suptitle('Figure 4')
	mean4 = np.array([])
	std4 = np.array([])
	for i in range(1000):
		sim4 = simulate(win_prob, 256)
		mean4 = np.append(mean4, np.array([np.mean(sim4)]))
		std4 = np.append(std4, np.array([np.std(sim4)]))

	xs4 = range(len(mean4))
	ax4.plot(xs4, mean4, c='g')
	ax4.plot(xs4, mean4+std4, c='b', alpha=0.5)
	ax4.plot(xs4, mean4-std4, c='b', alpha=0.5)
	ax4.set_xlabel('Num os Simulations')
	ax4.set_ylabel('Mean +/- Std')
	ax4.set_xlim([0, 300])
	ax4.set_ylim([-256, 100])
	plt.savefig('ML4T_2020Spring/martingale/figure_4.png')
	
	"""""""""""""""
	"	Figure 5  "
	"""""""""""""""
	fig5, ax5 = plt.subplots(1, 1)
	fig5.suptitle('Figure 5')
	median5 = np.array([])
	std5 = np.array([])
	for i in range(1000):
		sim5 = simulate(win_prob, 256)
		median5 = np.append(median5, np.array([np.median(sim5)]))
		std5 = np.append(std5, np.array([np.std(sim5)]))

	xs5 = range(len(median5))
	ax5.plot(xs5, median5, c='g')
	ax5.plot(xs5, median5+std5, c='b', alpha=0.5)
	ax5.plot(xs5, median5-std5, c='b', alpha=0.5)
	ax5.set_xlabel('Num os Simulations')
	ax5.set_ylabel('Median +/- Std')
	ax5.set_xlim([0, 300])
	ax5.set_ylim([-256, 100])
	plt.savefig('ML4T_2020Spring/martingale/figure_5.png')

	
if __name__ == "__main__":  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
    test_code()  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
