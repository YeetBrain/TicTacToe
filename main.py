#for loop for 15 times
#selects from a list of words
#gives end result
import random

def wordSelect():
	wordList = ['alchemized', 'amberjacks', 'apoenzymes', 'applejacks', 'appreciate', 'aquaphobes', 'aquaphobia', 'aquaphobic', 'asexualize', 'autoxidize', 'axiomatize', 'azobenzene', 'backchecks', 'backpacked', 'backpacker', 'balkanized', 'bamboozled', 'bedazzling', 'bedjackets', 'bhikkhunis', 'blackbucks', 'blackcocks', 'blackjacks', 'blitzkrieg', 'blizzarded', 'blizzardly', 'bodychecks', 'bolshevize', 'buckjumped', 'buckjumper', 'bumfreezer', 'bumfuzzled', 'bumfuzzles', 'buzzworthy', 'carboxylic', 'carjacking', 'catechizer', 'catechizes', 'chabazites', 'chaptalize', 'checkboxes', 'checkmarks', 'chequebook', 'chernozems', 'chickenpox', 'chiffchaff', 'chimpanzee', 'chinquapin', 'chromizing', 'chymifying', 'cinchonize', 'circumflex', 'cognizably', 'colloquize', 'communized', 'complexify', 'complexity', 'crackajack', 'crazyweeds', 'cyclohexyl', 'dazzlement', 'dazzlingly', 'deoxidized', 'deoxidizer', 'deoxidizes', 'diazotized', 'diazotizes', 'diingly', 'doxography', 'effeminize', 'embezzlers', 'embezzling', 'empathized', 'emphasized', 'enzymology', 'epoxidized', 'epoxidizes', 'equalizers', 'equalizing', 'equivoques', 'euphemized', 'everything', 'exahertzes', 'exchequers', 'exorcizing', 'exoticized', 'exoticizes', 'expertized', 'fetichized', 'fetichizes', 'friendship', 'frizzliest', 'gadzookery', 'grizzliest', 'hokeypokey', 'holoenzyme', 'homozygote', 'homozygous', 'hybridized', 'hybridizer', 'hybridizes', 'hydrazides', 'hydroxylic', 'hyphenized', 'hyphenizes', 'hypnotized', 'hypnotizer', 'hypnotizes', 'hypoxaemia', 'hypoxemias', 'intermezzi', 'intermezzo', 'jabberwock', 'jackhammer', 'jacklights', 'jackrabbit', 'jackscrews', 'jackshafts', 'jackstaffs', 'jacqueries', 'japanizing', 'jargonized', 'jargonizes', 'jayhawkers', 'jaywalkers', 'jaywalking', 'jeopardize', 'jockeyship', 'johnnycake', 'joypopping', 'jumboizing', 'juvenilize', 'juxtaposed', 'karyolymph', 'kazatskies', 'kibbitzing', 'kibbutznik', 'kickboxers', 'kickboxing', 'knickknack', 'knockbacks', 'kolkhoznik', 'lexicalize', 'liquidized', 'liquidizer', 'liquidizes', 'lumberjack', 'lyophilize', 'maximizing', 'mechanized', 'mezzalunas', 'mezzanines', 'mezzotints', 'microquake', 'mizzenmast', 'morbidezza', 'motivation', 'mozzarella', 'mycorrhiza', 'mythicized', 'mythicizer', 'mythicizes', 'myxoedemic', 'myxomycete', 'nephropexy', 'outdazzled', 'outdazzles', 'oxidizable', 'oxycephaly', 'oxygenized', 'oxygenizer', 'oxygenizes', 'packetized', 'packetizes', 'paddywhack', 'passamezzo', 'paycheques', 'photolyzed', 'photolyzes', 'phyllotaxy', 'phytophagy', 'phytotoxic', 'pipsqueaks', 'pizzicatos', 'podzolized', 'podzolizes', 'polygamize', 'polymyxins', 'pozzolanas', 'pozzolanic', 'prequalify', 'puzzledoms', 'puzzlement', 'puzzlingly', 'pyrolyzing', 'quadplexes', 'quadraplex', 'quadratrix', 'quadruplex', 'quantizers', 'quantizing', 'quartzites', 'quatorzain', 'quickbeams', 'quicklimes', 'quicksteps', 'quillbacks', 'quinaquina', 'quincunxes', 'quixotical', 'quizmaster', 'razorbacks', 'rejuvenize', 'rhizomorph', 'rhizophore', 'rhythmized', 'rhythmizes', 'schemozzle', 'schizocarp', 'schizogony', 'schizopods', 'schizziest', 'schmoozing', 'schnozzles', 'schvitzing', 'scuzzballs', 'sexualized', 'shemozzled', 'shemozzles', 'showjumper', 'sjambokked', 'skyjackers', 'skyjacking', 'snazziness', 'squeezable', 'squeezebox', 'squeeziest', 'squirarchy', 'strawberry', 'subjectify', 'supplejack', 'symbolized', 'symptomize', 'synonymize', 'syphilized', 'syphilizes', 'tetrazzini', 'texturized', 'trihydroxy', 'undazzling', 'unmuzzling', 'unoxidized', 'unpuzzling', 'vampirized', 'victimized', 'viziership', 'vizirships', 'whizzbangs', 'whizzingly', 'xanthophyl', 'xerophytic', 'xiphopagic', 'xylophonic', 'youthquake', 'zeaxanthin', 'zigzaggers', 'zigzaggery', 'zigzagging', 'zincifying', 'zombifying', 'zoomorphic', 'zygobranch', 'zygodactyl', 'zygomorphy', 'zygomycete', 'zygophytes']
	r = random.randint(0, 278)
	return wordList[r]

def hangMan(wrong):
	if wrong==6:
		print("  --|")
		print("    |")
		print("    |")
		print(" ___|")
	elif wrong==5:
		print(" 0--|")
		print("    |")
		print("    |")
		print(" ___|")
	elif wrong==4:
		print(" 0--|")
		print(" |  |")
		print("    |")
		print(" ___|")
	elif wrong==3:
		print(" 0--|")
		print("/|  |")
		print("    |")
		print(" ___|")
	elif wrong==2:
		print(" 0--|")
		print("/|\ |")
		print("    |")
		print(" ___|")
	elif wrong==1:
		print(" 0--|")
		print("/|\ |")
		print("/   |")
		print(" ___|")
	elif wrong == 0:
		print(" 0--|")
		print("/|\ |")
		print("/ \ |")
		print(" ___|")

def printGuess(guess):
	print("This is your word so far:", end="")
	for i in guess:
		print("|"+i, end="")
	print("|")

	

########################

print("Welcome to Hangman. You will guess a 10 letter word. Good Luck!")

word = wordSelect()
letters = list(word)
guess = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

	
t=9
i=6
while i>0:
	if t==1:
		i+=1
		print("Correct!")
	elif t==0:
		print("Incorrect:(")
		
	hangMan(i)
	t=0
	printGuess(guess)
	a = input("Please guess a letter: ")
	for p in range(10):
		if a == letters[p]:
			guess[p] = a
			t=1
	i-=1
		
	

print("The word was: "+ word)
hangMan(i)
	


			

	
			
		
	
	
	
	
	
	
