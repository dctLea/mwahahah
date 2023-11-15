import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp, kstest

#all data set by name 
Sample_A_batch1 = [.00798641298853596, .009260195313289796, .009138882710932288, .01631654501708486, .027113366626903092, .020542267332538063, .041124972199195295, .038071938373198, .04674578944175984, .05436826462322328, .06106067651994582, .05893770597868942, .07569906387108515, .06203117733880588, .06892577690612427, .06013061323520492, .05780545502335267, .060636082411694534, .05125457449604723, .04063972178976526, .03071230716350917, .028083867445763157, .019693079116035503, .011302290786307852, .011544915991022867, .007197881073212156, .004529003821346974, .0077033502497017734, .004043753411916941, .004407691218989466, .0029923775248185368]
Sample_B_batch1 = [.005072624459474443, .007026832243042466, .006028938906752411, .011780685220090919, .019916287836789, .015980153010311565, .03536977491961415, .02846767934360794, .040137487526333296, .061647632775252245, .06659552056769043, .05140536644860849, .07945725690209558, .06346324426211332, .07444007096130391, .05704623572458144, .0594855305466238, .05937465350925823, .052874487193702184, .04931256236833352, .033360128617363344, .03484310899212773, .02471171970284954, .012030158554163433, .014899101895997338, .009078057434305356, .005488413349595299, .008385075950770595, .003825257789111875, .004726133717707063, .0037698192704290943]
Sample_C_batch1 = [.003156837422872722, .003989094561630076, .0056249103171186685, .0110919787630937, .004548715741139331, .015741139331324438, .010934136891950065, .018510546706844596, .040981489453293156, .04696513129573827, .031554024967714166, .06699669966996699, .027392739273927394, .08573683455302052, .003845601951499498, .07441526761371789, .11274214377959535, .06497345386712584, .09246663796814464, .04976323719328454, .03677715597646721, .03416559047209069, .025326445688047067, .040737552016071175, .011378963983354856, .02179652747883484, .012426460037308079, .006629358588032716, .002496771416272062, .0016501650165016502, .0005739704405223131]
Sample_A_batch2 = [.008030509397984201, .006428766003813675, .010885317352220104, .01391446472350858, .01577771724325797, .015047670934350313, .029910106238082268, .01457913375102152, .025039498774175974, .05965676927267775, .036720239716698445, .03137019885589758, .06070280577499319, .03971669844728957, .07083628439117406, .030367747207845273, .07259057477526559, .07346227186052846, .07154453827295015, .05605012258240261, .058403704712612366, .04365023154453827, .034551893217107055, .03651321165894852, .029626804685371832, .010024516480523018, .015548896758376464, .01635521656224462, .003748297466630346, .007322255516208118, .0016235358213020975]
Sample_B_batch2 = [.004356365462143922, .0037804391807079465, .0051538018518245046, .0067043726095367484, .007162160166575601, .00887517167033389, .017484531210774253, .019581493568823192, .026020054048466412, .058567272619873885, .03200082697107078, .03922205649984494, .06251015254662788, .04638421666642054, .06323375223356026, .049130942008653665, .05796181165733863, .07851794970243808, .07331984582896466, .05794704431678899, .05508218025015875, .05079965149076303, .035810800832878006, .03996042352732696, .03092281111094703, .01420618160875408, .017218719080880723, .019625795590472114, .0062908870741468165, .00959877135726627, .002569517255637432]
Sample_C_batch2 = [.003424859178426331, .0029538183745166924, .0047300347392592885, .006486624403838983, .007458146061902612, .00912641557574925, .014209730917940767, .014258797668348021, .025171242958921317, .05226590253380699, .029420423544189514, .028674608937999255, .06686816745500579, .02914564974190889, .06885046417145885, .05043080606857569, .05396361209789798, .0766226374359679, .07543522207611235, .061598398461266704, .05944927479342898, .05445427960197052, .04117681694176758, .04671154638770583, .035288806892897095, .014847598673235068, .0207061686718612, .02316931954230535, .007369825911169555, .012482581303605425, .003248218876960217]
Sample_D_batch2 = [.0025016314988035677, .0019034152708288013, .003358168370676528, .0051120295845116384, .005995758103110724, .007817598433761149, .02735479660648249, .021644550793996083, .036124102675658035, .06698662170981075, .044295192516858824, .022514683489232107, .0742875788557755, .0351859908636067, .08443006308462041, .052751794648683924, .027232434196214923, .07818958016097455, .062187296062649555, .05052207961714161, .06379160321949097, .042663693713291276, .043071568414183165, .041372090493800306, .03398955840765717, .006961061561888188, .021073526212747443, .019836306286708724, .003453339134217968, .011461279095061998, .001930606917554927]
Sample_E_batch2 = [.004031945413662092, .0035279522369543303, .005950996355741645, .007734356827169109, .009498332945646275, .013336434829805382, .021632937892533146, .01899666589129255, .02903776071954718, .05704815073272854, .03285647825075599, .0340389237807242, .057765371791889585, .04904241296425525, .054799565790493915, .06166162673489959, .046483678374815846, .0719159494456075, .06834922850275257, .05823059626269675, .05514848414359929, .05070946731798093, .039253314724354504, .0431495696673645, .032371869426998524, .013278281770954485, .0183375978909824, .020334186244863148, .00628053035589672, .011805070946731798, .003392261766302241]
Sample_F_batch2 = [.007109120521172638, .006767100977198697, .011465798045602606, .007328990228013029, .006359934853420196, .009657980456026059, .01987785016286645, .018892508143322474, .02560260586319218, .0648615635179153, .033745928338762214, .03419381107491857, .06329804560260587, .046628664495114006, .058737785016286646, .050472312703583065, .047125407166123776, .07192182410423453, .06811889250814332, .056799674267100975, .054617263843648206, .051392508143322475, .03796416938110749, .04527687296416938, .033802931596091206, .0126628664495114, .018338762214983713, .019063517915309445, .00486970684039088, .00993485342019544, .0031107491856677523]
Sample_G_batch2 = [.007329046532531287, .006845052893590542, .00981815667565512, .013690105787181083, .015556938394523958, .0170780612597663, .0213648620618129, .0213648620618129, .02744935352278227, .0629191730622969, .029177902233284935, .03367212888059185, .06692940607066307, .04950563506879624, .05323930028348199, .05330844223190209, .04494226647306921, .06250432137177625, .06457857982437945, .04950563506879624, .05206388716034018, .049159925326695705, .03816635552789878, .04459655673096868, .031736154324828875, .013067828251400125, .016386641775565234, .01901403581552928, .006845052893590542, .013136970199820231, .005047362234667773]

print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaah")
print("eheheh")
print(("hihihihihihihi"))
print("loooooooooooooool")