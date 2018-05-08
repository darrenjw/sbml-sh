@model:2.4.1=LinearBirthDeathProcess
@compartments
 Cell=1
@species
 Cell:X=5000
@parameters
 Lambda=1.0
 Mu=1.1
@reactions
@r=Birth
 X ->  2X
 Lambda*X
@r=Death
 X -> 
 Mu*X
