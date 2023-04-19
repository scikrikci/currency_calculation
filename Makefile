.PHONY: run

exit:
	@echo "\x1B[31mcommand needed, like: \n \
	 >>> make start"
	@exit 0

install:
	@pip3 install -r requirements.txt

run:
	@python3 currency_calculation.py -f $(FORM) -t $(TO) -a $(AMOUNT)