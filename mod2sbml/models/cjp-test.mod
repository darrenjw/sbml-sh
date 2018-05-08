@model:2.3.0=PolyQModel
@units
 substance=item
@compartments
 cytosol=1.0
@species
 cytosol:PolyQ=1000.0s
 cytosol:Proteasome=500.0s
 cytosol:PolyQ_Proteasome=0.0s
 cytosol:ROS=10.0s
 cytosol:Source=1.0sbc
 cytosol:Sink=1.0sbc
 cytosol:p38death=0.0s
 cytosol:PIdeath=0.0s
 cytosol:polyQseq=0.0s
 cytosol:ProtSeq=0.0s
@parameters
 ksynPolyQ=0.007
 kbinPolyQ=1e-007
 krelPolyQ=1e-009
 kdegPolyQ=0.0025
 kalive=1.0v
@reactions
@r=polyQSynthesis
 Source -> PolyQ
 ksynPolyQ * Source * kalive
@r=polyqProteasomeBinding
 PolyQ+Proteasome -> PolyQ_Proteasome
 kbinPolyQ * PolyQ * Proteasome * kalive
@r=polyqProteasomeRelease
 PolyQ_Proteasome -> PolyQ+Proteasome
 krelPolyQ * PolyQ_Proteasome * kalive
@r=PolyQDegradation
 PolyQ_Proteasome -> Proteasome
 kdegPolyQ * PolyQ_Proteasome * kalive
@events
 PIcellDeath= lt(Proteasome, 300) : PIdeath=1; kalive=0 "cellDeath"
