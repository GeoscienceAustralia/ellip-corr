#
IASQ=emtvelin.o
TAUL=libtau.o libsun.o
#
#  path of executables
BIN = 
#
#  resampling of model 
REM = remodl.o
remodlv: $(REM) $(TAUL) $(IASQ)
	gfortran -o $(BIN)remodlv $(REM) $(IASQ) $(TAUL)
#
#  set branches  program
SBR = setbrn.o
setbrn: $(SBR) $(TAUL) 
	gfortran -o $(BIN)setbrn $(SBR) $(TAUL)
#
# travel time branches program
TBR =  ttimes.o       
ttimes: $(TBR) $(TAUL)
	gfortran -o $(BIN)ttimes $(TBR) $(TAUL)
#
