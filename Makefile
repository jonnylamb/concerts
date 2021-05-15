all:
	@echo "nothing to do."

concerts.zip: requirements.txt scrape.py ical.py lambda_function.py
	mkdir build
	cp $^ build
	pip install -t build -r $<
	cd build && zip -r ../$@ * && cd ..
	rm -rf build

lambda: concerts.zip
