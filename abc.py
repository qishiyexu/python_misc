#coding=utf-8

import itertools


def split_cards(cards, n):
	card_combinations = list(itertools.combinations(cards, n))
	splited = []
	for combi in card_combinations:
		second = cards[:]
		for item in combi:
			second.remove(item)
		splited.append((combi,second))

	return splited

def get_card_combinations(cards):
	card_combination = []
	splited1 = split_cards(cards, 3)
	for item1 in splited1:
		cards1, cards23 = item1
		splited23 = split_cards(cards23, 5)
		for item23 in splited23:
			cards2,cards3 = item23
			card_combination.append((cards1, cards2, tuple(cards3)))

	return card_combination





cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
combi = get_card_combinations(cards)
print combi
print len(combi)
