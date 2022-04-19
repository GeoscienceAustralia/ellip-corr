all:
	cd ellip &&	make -f Makefile clean &&	make -f Makefile all
	mv ellip/pyellip*.so ./
