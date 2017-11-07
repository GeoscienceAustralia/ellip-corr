f77=gfortran

.f.o:
	$(f77) -c $*.f

IASQ=emtvelin.o
TAUL=libtau.o libsun.o
#
#  path of executables
BIN = 
#
#  resampling of model 
REM = remodl.o
remodlv: $(REM) $(TAUL) $(IASQ)
	$(f77) -fdump-fortran-original -o $(BIN)remodlv $(REM) $(IASQ) $(TAUL)
#
#  set branches  program
SBR = setbrn.o
setbrn: $(SBR) $(TAUL) 
	$(f77) -o $(BIN)setbrn $(SBR) $(TAUL)
#
# travel time branches program
TBR =  ttimes.o       
ttimes: $(TBR) $(TAUL)
	$(f77) -o $(BIN)ttimes $(TBR) $(TAUL)
#

all: remodlv setbrn ttimes
clean:
	rm -f *.o ttimes setbrn remodlv
