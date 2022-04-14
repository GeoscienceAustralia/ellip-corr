f77=gfortran

.f.o:
	$(f77) -c $*.f

TAUD=../tau/
TAUL=$(TAUD)/libtau.o $(TAUD)/libsun.o
TAUF=$(TAUD)/libtau.f $(TAUD)/libsun.f
#
#  path of executables
BIN =  
#
# ellipticity correction to travel times
TEF = ttimel.o ellip.o
TEFF = ttimel.f ellip.f

ttimel: $(TEF) $(TAUL) 
	$(f77) -o $(BIN)ttimel $(TEF) $(TAUL)

pyellip:
	f2py3.6 -c pyellip.f -m pyellip

#
# direct access conversion of ellipticity corrections
DEF = direct.o     
direct: $(DEF) 
	$(f77) -o $(BIN)direct $(DEF)

all: ttimel direct pyellip

clean:	
	rm -f *.o ttimel direct
