@model:2.1.3=ImmigrationDeathProcess
@compartments
 Cell=1
@species
 Cell:X=0
@parameters
 Lambda=10
 Mu=1
@reactions
@r=Immigration
 ->  X
 Lambda
@r=Death
 X -> 
 Mu*X
