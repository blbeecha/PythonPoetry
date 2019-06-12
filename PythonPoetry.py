class PythonPoetry:
	from random import randint

	conj = [ "that", "yet", "for", "and" ]
	nouns = [ "cat", "dog", "mind", "friend" ]
	exist = [ "lay", "existed", "waited", "lived" ]
	adverb = [ "gently", "quiet", "abruptly", "softly" ]
	adj = [ "red", "big", "soft", "slow" ]
	post_noun = [ "contently unaware", "without true purpose", "filling empty time", "making little songs"]
	beg_preps = [ "Within", "Across", "In", "On" ]
	preps = [ "between", "across", "in", "on" ]
	pronoun = [ "she", "him", "they", "it" ]
	actverb = [ "run", "walk", "fight", "fly" ]
	ing_verb = [ "floating", "crying", "lying", "dying"]
	begs = [ "a", "the", "my", "this" ]
	emote = [ "sad", "mellow", "joyous", "listless" ]
	nouns_2 = [ "book", "pipe", "napkin", "dream"]
	emote_ly = [ "happily", "lazily", "cheerfully", "wearily" ]



	word = randint( 0, 3 )
	print( "{0}".format( beg_preps[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0}".format( begs[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0}".format( adverb[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0}".format( ing_verb[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0},".format( nouns[word] ),)
	word = randint( 0, 3 )
	print( "{0}".format( begs[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0}".format( adj[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0}".format( nouns[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0} ".format( exist[word] ) )
	word = randint( 0, 3 )
	print( "{0} ".format( post_noun[word] ) )
	word = randint( 0, 3 )
	print( "{0}".format( preps[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0}".format( begs[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0}".format( adj[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0} ".format( nouns_2[word] ) )
	word = randint( 0, 3 )
	print( "{0} ".format( conj[word] ) )
	word = randint( 0, 3 )
	print( "{0}".format( begs[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0}".format( emote[word] ), end=" " )
	word = randint( 0, 3 )
	print( "{0} ".format( nouns[word] ) )
	word = randint( 0, 3 )
	print( "knew " )
	print( "in time it would be better.")