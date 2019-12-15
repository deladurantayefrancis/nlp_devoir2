#!/bin/bash

python3.7 src/preprocess.py

doms="((co\.)?uk|((gc|qc)\.)?ca|(go\.)?com|at|au|biz|ch|cn|co|de|ee|edu|earth|es|eu|fi|fm|fo|fun|fr|gr|gg|gov|hr|hu|ie|info|in|io|is|it|jp|life|lv|ly|pl|me|moe|ms|mx|net|nl|no|nz|org|rs|ru|se|site|sh|sk|space|tr|tv|tw|ua|us|watch|works)"
regex_url="(https?:\/\/)?(w{3}\.)?([a-z0-9]{1,2}\.){0,2}([a-z0-9\-_]{2,}\.)+${doms}\/(([^\s\/()]+|\([^\s\/]\)+))*\/?"


cat data/reviews.txt |\
	# whitespaces
	perl -pe 's/\t/ /g' |\
	perl -pe 's/ {2,}/ /g' |\
	
	# replacing urls
	perl -pe "s/${regex_url}/ \[urllink\] /gi" |\

	# missing newlines between letters and digits
	perl -pe 's/([a-z])(([0-9]\.)?[0-9]+\/[0-9]+)/\1 \2 /gi' |\
	perl -pe 's/(([0-9]\.)?[0-9]+\/[0-9]+)([a-z])/ \1 \3/gi' |\
	perl -pe 's/([0-9]{4})([a-z])/ \1. \2/gi' |\

	# remove escape before some characters
	perl -pe 's/\\([[:punct:]])/\1/g' |\

	# add space after some punctuations
	perl -pe 's/([.!?:;])([a-z0-9])/\1 \2/gi' |\
	perl -pe "s/\)([a-z0-9])/). \1/gi" |\
	perl -pe "s/\]([a-z0-9])/]. \1/gi" |\
	perl -pe "s/\}([a-z0-9])/}. \1/gi" |\

	# missing newlines between letters
	perl -pe 's/([^A-Za-z])([a-z]{2,})([A-Z][A-Za-z])/\1\2. \3/g' |\
	perl -pe 's/([^A-Za-z])([a-z]{2,})((I|A)[^A-Za-z])/\1\2. \3/g' |\
	perl -pe 's/([A-Z][a-z]{3,})(I|A)/\1\2. \3/g' |\
	perl -pe 's/([A-Z]{3,})([A-Z][a-z]{2,})/\1. \2/g' |\
	perl -pe 's/([a-z])(Amazing|Awesome|Be(st|tter)|Bu[ty]|By|Can|D(id|o)|Easy|Enjoy|Eve[nr]|For|From|Game|Good|Graphics|Great|Have|I[st]|Large|More|Much|My|Needs?|Nice|No[tw]?|Of|Ok[ey]|Only|Over|So|St(ep|ill)|Time|Th(at|en?|ere|is)|To|Very|Well|Wh(at|en|ere|o|y)|Worth|Would|Wow|Your?) /\1. \2 /g' |\

	# replacing quotes by real quotes
	perl -pe "s/ \"+([^\"]+)\"+ / \" \1 \" /g" |\
	perl -pe "s/ '+([^']{2,50})'+ / \" \1 \" /g" |\
	perl -pe "s/ “+([^“”]+)”+ / \" \1 \" /g" |\
	perl -pe 's/\"/ \" /g' |\

	# miscellanous
	perl -pe 's/Overview((?!s)[A-Z])/Overview - \1/g' |\
	perl -pe 's/Summary([A-Z])/Summary: \1/g' |\

	# remove multiple spaces and save to file
    perl -pe 's/ {2,}/ /g' > data/cleaned.txt
