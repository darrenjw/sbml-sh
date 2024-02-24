@model:2.4.1=ActivatedTranscription
@compartments
 Cell=1
@species
 Cell:I=1
 Cell:A=0
 Cell:mRNA=0
@parameters
 lambda=1
 mu=0.5
 nu=1
 theta=0.01
@reactions
@r=Activate
 I ->  A
 lambda*I
@r=Inactivate
 A ->  I
 mu*A
@r=Transcribe
 A ->  A + mRNA
 nu*A
@r=Degrade
 mRNA -> 
 theta*mRNA
