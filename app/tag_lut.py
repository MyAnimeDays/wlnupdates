



# Tag replacement map. old-value -> fixed-value.
tag_fix_lut = {
	'female-protagonist'                   : 'female-lead',
	'male-protagonist'                     : 'male-lead',
	'non-human-protagonist'                : 'non-human-lead',

	'hiding-true-abilities'                : 'hiding-true-ability/ies',
	'hiding-true-ability'                  : 'hiding-true-ability/ies',

	'sword-and-magic'                      : 'sword-and-sorcery',
	'transported-into-another-world'       : 'transported-to-another-world',

	# WTF is generating censored tags?
	'an*l'                                 : 'anal',
	'c*nnilingus'                          : 'cunnilingus',
	'f*llatio'                             : 'fellatio',
	'h*ndjob'                              : 'handjob',
	'reverse-r*pe'                         : 'reverse-rape',
	'r*pe'                                 : 'rape',
	'r*pe-victim-becomes-lover'            : 'rape-victim-becomes-lover',
	's*x-slaves'                           : 'sex-slaves',
}

# If the key is present, the value should also be present.
# Basically, this ensures non-gendered tags are applied
# if a gendered tag is present.
tag_extend_lut = {

	'calm-female-lead'               : 'calm-lead',
	'calm-male-lead'                 : 'calm-lead',

	'capable-female-lead'            : 'capable-lead',
	'capable-male-lead'              : 'capable-lead',

	'confident-male-lead'            : 'confident-lead',

	'hot-blooded-female-lead'        : 'hot-blooded-lead',
	'hot-blooded-male-lead'          : 'hot-blooded-lead',

	'determined-female-lead'         : 'determined-lead',
	'determined-male-lead'           : 'determined-lead',

	'devoted-female-lead'            : 'devious-lead',
	'devoted-male-lead'              : 'devious-lead',

	'emotionally-strong-female-lead' : 'emotionally-strong-lead',
	'emotionally-strong-male-lead'   : 'emotionally-strong-lead',
	'emotionally-weak-female-lead'   : 'emotionally-weak-lead',

	'hard-working-female-lead'       : 'hard-working-lead',
	'hard-working-male-lead'         : 'hard-working-lead',

	'kind-female-lead'               : 'kind-lead',
	'kind-male-lead'                 : 'kind-lead',

	'manipulative-female-lead'       : 'manipulative-lead',
	'manipulative-male-lead'         : 'manipulative-lead',

	'perverted-female-lead'          : 'perverted-lead',
	'perverted-male-lead'            : 'perverted-lead',

	'strong-female-lead'             : 'strong-lead',
	'strong-male-lead'               : 'strong-lead',

	'young-female-lead'              : 'young-lead',
	'young-male-lead'                : 'young-lead',

	'male-to-female'                 : 'gender-bender',
	'female-to-male'                 : 'gender-bender',
}

# Half of this shit isn't even a genre. Sigh.
genre_replace_lut = {
	'characters-with-a-past' : [],
	'comedy.'                : ['comedy'],
	'sci-fic'                : ['sci-fi'],
	'apocaylptic-fiction'    : [],
	'mil-gyo'                : [],
	'action-adventure'                                                                                     : ['action', 'adventure'],
	'action-adventure-drama-fantasy-harem-romance'                                                         : ['action', 'adventure', 'drama', 'fantasy', 'harem', 'romance'],
	'fantasy,-romance'                                                                                     : ['fantasy', 'romance'],
	'fantasy,-transported-to-another-world'                                                                : ['fantasy'],
	'fantasy/tragedy'                                                                                      : ['fantasy', 'tragedy'],
	'far-future/post-apocalyptic'                                                                          : [],
	'time-travel-reborn,'                                                                                  : [],
	'xian-xia-fiction,-fantasy-cultivation,supernatural,adventure'                                         : ['xianxia', 'supernatural', 'adventure'],
	'xuanhuan,-action,-martial-arts,-mature,-fantasy,-romance,-adventure,-strong-male-lead,-demons,-gods,' : ['xuanhuan', 'action', 'mature', 'fantasy', 'romance', 'adventure'],

}


