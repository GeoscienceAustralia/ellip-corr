      program ttimel
      save
      parameter (max=60)
      logical log,prnt(3)
      character*8 phcd(max),phlst(10),phase
      character*20 modnam
      dimension tt(max),dtdd(max),dtdh(max),dddp(max),mn(max),ts(max)
      dimension te(max)
      dimension usrc(2)
      data in/1/,phlst(1)/'query'/,prnt(3)/.true./
c
      write(6,*) 'enter model name:'
      read(5,*) modnam
      write(6,*) 'This routine for calculating travel times for'
      write(6,*) 'specific distances uses a set of precalculated'
      write(6,*) 'tau-p tables for the',modnam,' model stored as'
      write(6,*) modnam,'.hed  ',modnam,'.tbl'
      write(6,*)
      prnt(1) = .false.
      prnt(2) = .false.
      call assign(10,2,'ttim1.lis')
      call tabin(in,modnam)
      write(6,*) 'The source depth has to be specified and also'
      write(6,*) 'the phase codes or keywords for the required branches'
      write(6,*) 'ALL will give all available branches'
      write(6,*) 'P  gives P-up,P,Pdiff,PKP, and PKiKP'
      write(6,*) 'P+ gives P-up,P,Pdiff,PKP,PKiKP,PcP,pP,pPdiff,pPKP,' 
      write(6,*) '         pPKiKP,sP,sPdiff,sPKP, and sPKiKP'
      write(6,*) 'S  gives S-up,S,Sdiff, and SKS'
      write(6,*) 'S+ gives S-up,S,Sdiff,SKS,sS,sSdiff,sSKS,pS,pSdiff,'
      write(6,*) '         and pSKS '
      write(6,*) 'basic gives P+ and S+ as well as '
      write(6,*) '         ScP, SKP, PKKP, SKKP, PP, and PKPPKP '
      write(6,*)
      write(6,*) 'or give a generic phase name'
      write(6,*)
      write(6,*) 'You will have to enter a distance,'
      write(6,*) 'if this is negative a new depth is calculated'
      write(6,*) 'TO EXIT: give negative depth'
      write(6,*)
      call brnset(1,phlst,prnt)
      degrad = 45.0/atan(1.0)
c                                  open ellipticity correction file
      open(21,file='elcordir.tbl',access='direct',
     &     form='formatted',recl=80) 
c
      call query('Source latitude:',log)
      read(5,*)  slat
      ecolat = (90.0-slat)/degrad
      call ellref(ecolat)
c                                    choose source depth
 3    call query('Source depth (km):',log)
      read(*,*)zs
      if(zs.lt.0.) go to 13
      call depset(zs,usrc)
      edepth = zs
c                                    loop on delta
 1    write(*,*)
      call query('Azimuth from source:',log)
      read(5,*)  bazim  
      bazim = bazim/degrad
      call query('Enter delta:',log)
      read(*,*)delta
      if(delta.lt.0.) go to 3
      write(6,*)
     %'  delta    # code       time    time(el)    dT/dD',
     %'     dT/dh      d2T/dD2'
      call trtm(delta,max,n,tt,dtdd,dtdh,dddp,phcd)
      if(n.le.0) go to 2
      do 4 i=1,n
        phase = phcd(i)
        call ellcor(phase,delta,edepth,ecolat,bazim,tcor,abrt)
        te(i) = tt(i)+tcor
 4    continue
c
      write(*,100)delta,(i,phcd(i),tt(i),te(i),dtdd(i),dtdh(i),
     1 dddp(i),i=1,n)
 100  format(/1x,f6.2,i5,2x,a,f9.2,f11.2,f11.4,1p2e11.2/
     1 (7x,i5,2x,a,0pf9.2,f11.2,f11.4,1p2e11.2))
      go to 1
 2    write(*,101)delta
 101  format(/1x,'No arrivals for delta =',f7.2)
      go to 1
c                                    end delta loop
 13   call retrns(in)
      call retrns(10)
      call exit(0)
      end
