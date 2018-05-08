@model:2.4.1=BirthImmigrationDeathProcess
@compartments
 Cell=1
@species
 Cell:X=10
@parameters
 Lambda=1
 Mu=0.9
 Nu=1
@reactions
@r=Birth
 X ->  2X
 Lambda*X
@r=Immigration
 ->  X
 Mu
@r=Death
 X -> 
 Nu*X
