all:
	cd tau && make -f Makefile clean &&	make -f Makefile all
	cd ellip &&	make -f Makefile clean &&	make -f Makefile all
	mv ellip/pyellip*.so ./
clean:
	rm pyellip*.so
	cd tau && make -f Makefile clean 
	cd ellip &&	make -f Makefile clean 
