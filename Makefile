generate:
	@./cgol.py > data.csv &
	@echo "Will generate drawing data for 5 seconds"
	@echo "5"
	@sleep 1
	@echo "4"
	@sleep 1
	@echo "3"
	@sleep 1
	@echo "2"
	@sleep 1
	@echo "1"
	@sleep 1
	@killall cgol.py
	@echo "Now run 'make draw' for the wow"

draw:
	./draw.py data.csv
