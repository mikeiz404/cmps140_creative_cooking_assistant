run:
	python2.6 command_line_interface.py

test:
	rm -f combined_taggers.pkl
	py.test --doctest-modules -k-scraper

refresh:
	### Download DB ###
	sh update_database.sh
	
	### Regenerate wordlists ###
	python2.6 generate_cuisines.py
	python2.6 generate_ingredients.py

	### Remove cached tagger ###
	rm -f combined_taggers.pkl
	
	### Done. ###
	
clean:
	### Remove python compiled files ###
	-find -name "*.pyc" | xargs rm
	### Remove log files ###
	-find -name "*.log" | xargs rm
