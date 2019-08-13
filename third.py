# coding: utf-8
import random
playCount = 0
while True:
	print'("Welcome to who wants to be a millionare")'
	print'("Im your host, Pineapple!!!")'
	print'("P.S.: I took Chris Tarrants job!!!")'
	print'("Press 1 to play and 2 to quit")'
	ask = raw_input(">>>")
	if ask =="2":
		break
	elif ask == "1":
		money = 0
		if playCount == 1:
			playCount = playCount - 1
			break
		#first question
		print("********")
		print("Your first question is:")
		print("Which of these US presidents appeared on the television series 'Laugh-In?'")
		print("A: Lyndon Johnson")
		print("B: Richard Nixon")
		print("C: Jimmy Carter")
		print("D: Gerald Ford")
		answer1 = raw_input(">>>")
		if answer1 != "B":
		    print("Oh sorry. The answer was B. Richard Nixon")
		    playCount = playCount + 1
		else: 
			money = money + 100
			print("Correct! You have won $" + str(money))
			print("********")
			print("Question 2 is worth $200. Would you like to take your $100 home or risk it all?")
			print("Press 1 to continue and 2 to go home.")
			ask1 = raw_input(">>>")
			if ask1 == "2":
				print("You have won $100! congrats")
			elif ask1 == "1":
				
				print("Your second Question is:")
				print("Which insect shorted out an early supercomputer and inspired the term 'computer bug?'")
				print("A: Moth")
				print("B: Roach")
				print("C: Fly")
				print("D: Japanese beetle")
				answer2 = raw_input(">>>")
				if answer2 != "A":
					print("Whoops, wrong choice. The answer was A. Moth.")
					playCount = playCount + 1
					break
				else:
					money = 200
					print("Correct! You have won $200")
					print("********")
					print("Question 3 is worth $300. Would you like to take your $200 home or risk it all? ")
					print("Press 1 to continue and 2 to go home.")
					ask2 = raw_input(">>>")
					if ask2 == "2":
						print("You have won $200! congrats")
					elif ask2 == "1":
						print("Your third Question is:")
						print("Which of the following men does not have a chemical element named for him?")
						print("A: Albert Einstein")
						print("B: Niels Bohr")
						print("C: Isaac Newton")
						print("D: Enrico Fermi")
						answer3 = raw_input(">>>")
						if answer3 != "C":
							print("Sorry, Wrong Choice. The answer was C. Issac Newton.")
							playCount = playCount + 1
							break
						else:
							money = 300
							print("Correct! You have won $300")
							print("********")
							print("Question 4 is worth $500. Would you like to take your $300 home or risk it all? ")
							print("Press 1 to continue and 2 to go home.")
							ask3 = raw_input(">>>")
					if ask3 == "2":
						print("You have won $300! congrats")
					elif ask3 == "1":
						print("Your fourth Question is:")
						print("In the children’s book series, where is Paddington Bear originally from?")
						print("A: India")
						print("B: Peru")
						print("C: Canada")
						print("D: Iceland")
						answer4 = raw_input(">>>")
						if answer4 != "B":
							print("Whoopsie, Wrong choice. The answer was B. Peru.")
							playCount = playCount + 1
							break
						else:
							money = 500
							print("Correct! You have won $500")
							print("********")
							print("Question 5 is worth $1000. Would you like to take your $500 home or risk it all? ")
							print("Press 1 to continue and 2 to go home.")
							ask4 = raw_input(">>>")
							if ask4 == "2":
								print("You have won $500! congrats")
							elif ask4 == "1":
								print("Your fifth Question is:")
								print("The Earth is approximately how many miles away from the Sun?")
								print("A: 9.3 million ")
								print("B: 39 million")
								print("C: 93 million")
								print("D: 193 million")
								answer5 = raw_input(">>>")
								if answer5 != "C":
									print("Sorry, Wrong Choice The answer was C. 93 million.")
									playCount = playCount + 1
									break
								else:
									money = 1000
									print("Correct! You have won $1000")
									print("********")
									print("Question 6 is worth $2000. Would you like to take your $1000 home or risk it all? ")
									print("Press 1 to continue and 2 to go home.")
									ask5 = raw_input(">>>")
									if ask5 == "2":
										print("You have won $1000! congrats")
									elif ask5 == "1":
										print("Your sixth Question is:")
										print("Which of the following landlocked countries is entirely contained within another country??")
										print("A: Lesotho")
										print("B: Burkina Faso")
										print("C: Mongolia")
										print("D: Luxembourg")
										answer6 = raw_input(">>>")
										if answer6 != "A":
											print("Whoopsie, Wrong choice. The answer was A. Lestho.")
											playCount = playCount + 1
											break
										else:
											money = 2000
											print("Correct! You have won $2000")
											print("********")
											print("Question 7 is worth $4000. Would you like to take your $2000 home or risk it all? ")
											print("Press 1 to continue and 2 to go home.")
											ask6 = raw_input(">>>")
											if ask6 == "2":
												print("You have won $2000! congrats")
											elif ask6 == "1":
												print("Your seventh Question is:")
												print("What letter must appear on the beginning of the registration number of all non-military aircraft in the US?")
												print("A: N")
												print("B: A")
												print("C: U")
												print("D: L")
												answer7 = raw_input(">>>")
												if answer7 != "A":
													print("Whoopsie, Wrong choice. The answer was A. N.")
													playCount = playCount + 1
													break
												else:
													money = 4000 
													print("Correct! You have won $4000")
													print("********")
													print("Question 8 is worth $8000. Would you like to take your $4000 home or risk it all? ")
													print("Press 1 to continue and 2 to go home.")
													ask7 = raw_input(">>>")
													if ask7 == "2":
														print("You have won $4000! congrats")
													elif ask7 == "1":
														print("Your eight Question is:")
														print("Who is credited with inventing the first mass-produced helicopter?")
														print("A: Igor Sikorsky")
														print("B: Elmer Sperry")
														print("C: Ferdinand von Zeppelin")
														print("D: Gottlieb Daimler")
														answer8 = raw_input(">>>")
														if answer8 != "A":
															print("Whoopsie, Wrong choice. The answer was A. Igor Sikorsky.")
															playCount = playCount + 1
															break
														else:
															money = 8000
															print("Correct! You have won $8000")
															print("********")
															print("Question 9 is worth 16000 Would you like to take your $8000 home or risk it all? ")
															print("Press 1 to continue and 2 to go home.")
															ask8 = raw_input(">>>")
															if ask8 == "2":
																print("You have won $8000! congrats")
															elif ask8 == "1":
																print("Your eight Question is:")
															print("The US icon Uncle Sam was based on Samuel Wilson who worked during the War of 1812 as a what?")
															print("A:  Meat inspector")
															print("B: Mail deliverer")
															print("C: Historian")
															print("D: Weapons mechanic")
															answer9 = raw_input(">>>")
															if answer9 != "A":
																print("Whoopsie, Wrong choice. The answer was A. Meat Inspector.")
																playCount = playCount + 1
																break
															else:
																money = 16000
																print("Correct! You have won $16000")
																print("********")
																print("Question 10 is worth $32000. Would you like to take your $16000 home or risk it all? ")
																print("Press 1 to continue and 2 to go home.")
																ask9 = raw_input(">>>")
																if ask9 == "2":
																	print("You have won $16000! congrats")
																elif ask9 == "1":
																	print("Your tenth Question is:")
																print("During World War II, US soldiers used the first commercial aerosol cans to hold what?")
																print("A: Cleaning fluid")
																print("B: Antiseptic")
																print("C: Insecticide")
																print("D: Shaving cream")
															answer10 = raw_input(">>>")
															if answer10 != "C":
																print("Whoopsie, Wrong choice. The answer was C.Insecticide.")
																playCount = playCount + 1
																break
															else:
																money = 32000
																print("Correct! You have won 32000")
																print("********")
																print("Question 11 is worth $64000. Would you like to take your $32000 home or risk it all? ")
																print("Press 1 to continue and 2 to go home.")
																ask10 = raw_input(">>>")
																if ask10 == "2":
																	print("You have won $32000! congrats")
																elif ask10 == "1":
																	print("Your eleventh Question is:")
																print("According to the Population Reference Bureau, what is the approximate number of people who have ever lived on earth?")
																print("A:  50 billion")
																print("B: 100 billion")
																print("C: 1 trillion")
																print("D: 5 trillion")
																answer11 = raw_input(">>>")
																if answer11 != "B":
																	print("Whoopsie, Wrong choice. The answer was B. 100 billion.")
																	playCount = playCount + 1
																	break
																else:
																	money = 64000
																	print("Correct! You have won $64000")
																	print("********")
																	print("Question 12 is worth $125000. Would you like to take your $64000 home or risk it all? ")
																	print("Press 1 to continue and 2 to go home.")
																	ask11 = raw_input(">>>")
																	if ask11 == "2":
																		print("You have won $64000! congrats")
																	elif ask11 == "1":
																		print("Your twelth Question is:")
																		print("Who did artist Grant Wood use as the model for the farmer in his classic painting "'American Gothic?'"")
																		print("A: Traveling salesman")
																		print("B: Local sheriff")
																		print("C:  His dentist")
																		print("D: His butcher")
																		answer12 = raw_input(">>>")
																		if answer12 != "C":
																			print("Whoopsie, Wrong choice. The answer was C. His Dentist.")
																			playCount = playCount + 1
																			break
																		else:
																			money = 125000
																			print("Correct! You have won $125000")
																			print("********")
																			print("Question 13 is worth $250000. Would you like to take your $125000 home or risk it all? ")
																			print("Press 1 to continue and 2 to go home.")
																			ask12 = raw_input(">>>")
																			if ask12 == "2":
																				print("You have won $125000! congrats")
																			elif ask12 == "1":
																				print("Your thirteenth Question is:")
																				print("The song "'God Bless America'" was originally written for what 1918 musical?")
																				print("A: Oh Lady! Lady!!")
																				print("B: Yip, Yip, Yaphank")
																				print("C: Blossom Time")
																				print("D: Watch Your Step")
																				answer13 = raw_input(">>>")
																				if answer13 != "B":
																					print("Whoopsie, Wrong choice. The answer was B. Yip,Yip,Yaphank.")
																					playCount = playCount + 1
																					break
																				else:
																					money = 250000
																					print("Correct! You have won $250000")
																					print("********")
																					print("Question 14 is worth $500000. Would you like to take your $250000 home or risk it all? ")
																					print("Press 1 to continue and 2 to go home.")
																					ask13 = raw_input(">>>")
																					if ask13 == "2":
																						print("You have won $250000! congrats")
																					elif ask13 == "1":
																						print("Your fourthteenth Question is:")
																						print("Khrushchevs famous 1960 shoe-banging outburst at the UN was in response to a delegate from what nation?")
																						print("A: Australia")
																						print("B: The Netherlands")
																						print("C: The Philippines")
																						print("D: Turkey")
																					answer14 = raw_input(">>>")
																					if answer14 != "C":
																						print("Whoopsie, Wrong choice. The answer was C. The Philippines.")
																						playCount = playCount + 1
																						break
																					else:
																						money = 500000
																						print("Correct! You have won $500000")
																						print("********")
																						print("Question 15 is worth $1000000. Would you like to take your $500000 home or risk it all? ")
																						print("Press 1 to continue and 2 to go home.")
																						ask14 = raw_input(">>>")
																						if ask14 == "2":
																							print("You have won $500000! congrats")
																						elif ask14 == "1":
																							print("Your fifteenth Question is:")
																							print("Neurologists believe that the brain's medial ventral prefrontal cortex is activated when you do what?")
																							print("A: Have a panic attack")
																							print("B: Remember a name")
																							print("C: Get a joke")
																							print("D: Listen to music")
																					answer15 = raw_input(">>>")
																					if answer15 != "C":
																						print("Whoopsie, Wrong choice. The answer was C. Get a Joke.")
																						playCount = playCount + 1
																						break
																					else:
																						money = 1000000
																						print("Correct! You have won $1000000")
																						print("********")
																						print("Congrats, You Just Won a Million Dollars!!!")

















