<!-- PAGE: 1 -->

1886 IEEESIGNALPROCESSINGLETTERS,VOL.33,2026
Factor Graph–Based Tightly Coupled PPP-B2b/INS
for Real-Time Precise Positioning
RuiteYi ,XiangweiZhu ,MingjunOuyang,ChengchaoBai ,andGuangtengFan
Abstract—Real-time precise point positioning (PPP) based on provides users with real-time high-precision orbit and clock
BDS-3PPP-B2bcorrectionsoftensuffersfromlimitedrobustness corrections,whichhasgreatlypromotedglobalreal-timeprecise
incomplexenvironments.Toaddressthesechallenges,thisletter
pointpositioning(PPP)applications[1],[2],[3].
proposes a factor-graph-based tightly coupled PPP-B2b/inertial
BDS-3PPP-B2bbroadcastsreal-timecorrectionsviageosta-
navigation system (INS) integration scheme. Unlike traditional
filteringapproaches,theproposedframeworkfusesasynchronous tionaryearthorbit(GEO)satellites[4].Itsasynchronousupdate
GNSSobservationscorrectedbyPPP-B2bwithpre-integratediner- rates(6sforclock,48sfororbit)andtime-varyinguncertainties
tialmeasurementswithinasliding-windowoptimizationarchitec- necessitate a flexible fusion framework, making factor graph
ture.Toexplicitlymitigatenon-Gaussiannoiseandmeasurement
optimization (FGO) superior to traditional filtering. Recent
anomaliesprevalentinurbancanyons,arobustestimationstrat-
studies have evaluated PPP-B2b product quality [5], [6], [7]
egy is implemented. This strategy incorporates Huber loss func-
tionsforoutlierresistanceand,critically,employsatime-varying, andvalidateditsreal-timeaccuracy[8],[9],[10].Comparisons
correction-age-dependentmeasurementcovariancemodeltochar- withGalileohighaccuracyservice(HAS)[11]andmulti-GNSS
acterize the reliability degradation caused by correction latency. advancedorbitandclockaugmentation(MADOCA)-PPP[12],
This formulation enables multiple relinearizations and effective
alongsidesystematicbenchmarking[13],[14],highlightitsdis-
outliermitigationwhilemaintainingboundedcomputationalcost.
tinctservicecharacteristics.However,challengesregardinglong
Experimentalresultsutilizingadenseurbandatasetdemonstrate
thattheproposedmethodreducestheENURMSpositionerrors convergence[3]andinsufficienturbanrobustnesspersist.
from0.797/0.954/1.616mto0.490/0.671/0.797mandthe3DRMS While tightly coupled PPP/inertial navigation system (INS)
from2.04mto1.15m,representinga43.6%improvementoverthe [15]mitigatessignaloutages,mainstreamextendedKalmanfil-
extended Kalman filter (EKF)-based solution. The factor-graph
ter(EKF)-basedapproaches[15],[16]sufferfromlinearization
approach exhibits significantly smoother trajectory behavior in
errors and sensitivity to outliers. Furthermore, standard EKF
challenging environments, confirming that the proposed robust
frameworkofferssuperioraccuracyandreliabilitywiththehigh failstofullyexploitcross-epochconstraintsincomplexreal-time
computationalefficiencyrequiredforreal-timeapplications. scenarios[17].
Alternatively,factorgraphoptimization(FGO)[18]employs
IndexTerms—PPP-B2bsignal,inertialnavigationsystem,factor
sliding-windowsmoothingtoenableiterativerelinearizationand
graphoptimization,integratednavigation.
robustweighting[19],[20].Inglobalnavigationsatellitesystem
(GNSS)/INScontexts,FGOhasbeenshowntoimproveurban
I. INTRODUCTION reliability[21],[22],robustnessagainstabnormalobservations
WITHthecompletionoftheBeiDou-3(BDS-3)constel- [23],andavailabilityinmulti-sourcefusion[24].
lation,thesatellite-basedaugmentationsignalPPP-B2b Nevertheless, dedicated modeling and implementation for
PPP-B2b/INS remain limited. This letter proposes a factor-
graph-basedPPP-B2b/INSframework(Fig.1)toaddressthese
Received9December2025;revised1February2026;accepted9February
limitations.Themaincontributionsofthisletterare:1)afactor-
2026.Dateofpublication27April2026;dateofcurrentversion13May2026.
ThisworkwassupportedinpartbytheYoungScientistsFundoftheNational graph-basedtightlycoupledPPP-B2b/INSframeworkthatlever-
Natural Science Foundation of China under Grant 42404054 and in part by agesiterativerelinearizationtomitigatelinearizationerrors;and
NingboNaturalScienceFoundationunderGrant2023J285.Theassociateeditor
2)atime-varyingvariancemodelwithHuberlosstoexplicitly
coordinatingthereviewofthisarticleandapprovingitforpublicationwasProf.
YongchanGao.(Correspondingauthor:GuangtengFan.) handlecorrectionlatencyandsignaldegradation.
RuiteYiiswiththeSchoolofSystemsScienceandEngineering,SunYat-sen
University,Guangzhou510000,China,andalsowiththeSchoolofElectrical
andCommunicationEngineering,ShenzhenCampusofSunYat-senUniversity, II. METHODOLOGY
Shenzhen518000,China(e-mail:yirt@mail2.sysu.edu.cn).
This section summarizes the tightly coupled PPP-B2b/INS
Xiangwei Zhu is with the School of Electrical and Communication Engi-
neering,ShenzhenCampusofSunYat-senUniversity,Shenzhen518000,China stateandsystemmodels,thePPP-B2b-basedGNSSobservation
(e-mail:zhuxw666@mail.sysu.edu.cn). model,andthefactor-graphadoptedinthiswork.
MingjunOuyangiswiththeSchoolofElectronicsandInformationTech-
nology,GuangdongPolytechnicNormalUniversity,Guangzhou510000,China
(e-mail:work_ouyang@163.com). A. PPPBasedonPPP-B2bCorrectionsObservationModel
ChengchaoBaiiswiththeSchoolofAstronautics,HarbinInstituteofTech-
nology,Harbin150001,China(e-mail:baichengchao@hit.edu.cn). For each satellite s, dual-frequency code and carrier-phase
GuangtengFaniswiththeDefenseInnovationInstitute,AcademyofMilitary measurements on frequencies f1 and f2 are combined into
Sciences(AMS),Beijing100000,China(e-mail:fanguangteng@163.com).
DigitalObjectIdentifier10.1109/LSP.2026.3687756 ionosphere-free(IF)observables.DenotingcodeasP IF,k s and
1070-9908©2026IEEE.Allrightsreserved,includingrightsfortextanddatamining,andtrainingofartificialintelligenceandsimilartechnologies.
Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:43:50 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 2 -->

YIetal.:FACTORGRAPH–BASEDTIGHTLYCOUPLEDPPP-B2B/INSFORREAL-TIMEPRECISEPOSITIONING 1887
thatthevarianceinflationinthefactorgraphaccuratelyreflects
therapiddegradationofclockestimatesovertime,whichisthe
dominanterrorsourceinreal-timeprocessing.
Toensurethereproducibilityoftheexperiment,thestochastic
model explicitly accounts for the noise amplification of the IF
combination and the time-varying quality of PPP-B2b correc-
tions.Thevarianceσ2 fortheIFmeasurementofasatelliteat
IF
elevationθismodeledas
(cid:2) (cid:3)
σ 2 =R2 · a 2 +
b2
σ +(e˙ ·Δt )2 , (6)
IF type σ sin2 θ clk age
wherea andb areempiricalbasenoiseconstants(setto0.003
σ σ
m for carrier phase); R is the noise ratio factor, set to 1
type
for carrier phase and 100–500 for pseudorange measurements
Fig.1. Factor-graph-basedtightlycoupledPPP-B2b/INSintegrationframe- to reflect the lower precision of code observations; and e˙ clk
work. represents the uncertainty growth rate of the satellite clock
(empirically set to 0.002 m/s). This function ensures that the
phaseasΦs onfrequencyfi,theIFcombinationsare: weightoftheobservationautomaticallydegradesasthesatellite
IF,k
elevationdecreasesorthecorrectionlatencyincreases.
P
I
s
F,k
=α
1
P
1
s
,k
+α2P
2
s
,k
, (1)
Theresultingvariancesareassembledintoadiagonalcovari-
Φs
IF,k
=α1 Φs
1,k
+α2 Φs
2,k
, (2) ance matrix RGNSS,k for each epoch, which is used in the
GNSS factors of the graph and forms a key component of the
whereα i =f i 2/(f 1 2−f 2 2)andthecorrespondingIFwavelength proposedrobustfactor-graph-basedPPP-B2b/INSintegration.
isλIF.
BDS-3PPP-B2borbitandclockcorrectionsareappliedtothe B. StateandINSModels
broadcastephemeristoobtaincorrectedsatellitepositionsrs,∗
and clocks δts,∗ . Let ρ(r ,rs,∗) denote the geometric distan k ce Weuseastandarderror-stateformulationfortightlycoupled
k k k GNSS/INS integration. At epoch k, the navigation state is de-
between the receiver and satellite, Tk the slant tropospheric
finedas
delay,andbs P ,bs Φ theremainingcodeandphasehardwaredelays. (cid:4) (cid:5)
ThePPP-B2b-providedsatelliteDCBs(referencedtoB3Isignal) x = rT vT θT bT bT δt d NT T , (7)
k k k k g,k a,k k T,k k
are applied to the raw code measurements before forming the
wherer andv arethereceiverpositionandvelocityinthelocal
ionosphere-freeobservables.Theobservationequationsforthe k k
navigationframe,θ isaminimalattituderepresentation(e.g.,
IFcodeandphaseatepochkaremodeledas k
roll,pitch,yaw),b andb aregyroscopeandaccelerometer
Ps =ρ(r ,rs,∗)+c(δt −δts,∗)+T +bs +εs , (3) biases,δt isther g e , c k eiverc a lo ,k ckoffset,d isthezenithtropo-
IF,k k k k k k P P,k k T,k
spheric delay, and N stacks the carrier-phase ambiguities for
Φs =ρ(r ,rs,∗)+c(δt −δts,∗)+T k
IF,k k k k k k alltrackedsatellitesandarcs.
+λ Ns+bs +εs , (4) Letωm,kandbg,kdenotetherawinertialmeasurementunit
IF k Φ Φ,k
(IMU)measurementsofangularrateandspecificforceattime
where N k s is the IF ambiguity, and εs P,k , εs Φ,k are zero-mean k. After bias compensation, the effective inputs for strapdown
observationerrors.Theinformationfromtheremovedobserva- mechanizationare
tionsandstatesregardingthisambiguityiscompressedintothe
ω(cid:6)k =ωm,k−bg,k, (8)
priorfactor,whichimposesconstraintsontheremainingstates
andambiguities. f (cid:6) k =fm,k−bm,k . (9)
Inordertoaddresstheasynchronousupdateintervalsofthe
PPP-B2b corrections (48 s for orbit and 6 s for clock), we Thecontinuous-timeINSdynamicscanbewrittencompactly
employedtheHold-Lastmethodtoalignthesecorrectionswith as (cid:7) (cid:8)
the1HzGNSSdata.Inthisapproach,themostrecentavailable x˙k =f xk,ω(cid:6)k,f (cid:6) k +wk, (10)
PPP-B2b corrections are retained. However, considering that
satelliteclockerrorsexhibitsignificantlyfastertemporalvaria- where f(·) collects the standard strapdown inertial equations
tionsthanorbiterrors,thestochasticmodelisprimarilydriven together with random-walk models for sensor biases, clock
bythelatencyoftheclockcorrections.Therefore,wedefinethe offsetandtroposphere,andwk iszero-meanGaussianprocess
correctionageΔt age specificallyasthetimeelapsedsincethe noise.
lastreceivedclockcorrection: In the factor graph, a high-rate stream of IMU samples be-
tweentwokeyepochsissummarizedbyanIMUpre-integration
Δt =t −t (5)
age now last_clock factor.Fortwoconsecutivekeyframesk−1andk,allrawIMU
where t
now
is the current GNSS epoch and t
last_clock
is the measurements in (t k−1,t
k
] are integrated to obtain a relative
timetagofthemostrecentPPP-B2bclockupdate.Thisensures motion constraint with mean and covariance that depend on
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:43:50 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 3 -->

1888 IEEESIGNALPROCESSINGLETTERS,VOL.33,2026
thecontinuousINSmodelabove.Thissignificantlyreducesthe
numberofvariablesandallowsustohandlehigh-rateIMU(e.g.,
hundredsofHz)togetherwithlower-ratePPP-B2bobservations
inaunifiedoptimizationframework.
C. FactorGraphOptimization
LetX ={x0,x1,...,xK}denotethesetofstateswithinthe
Fig.2. Typicalscenarioofthedataset.
currenttimewindowandZthecollectionofallIMUandPPP-
B2b measurements in this window. Under standard Gaussian
assumptions,theposteriordensityfactorsas
(cid:9) (cid:9)
p(X|Z)∝f0 (x0 ) f
IMU
(x k−1,x
k
) f
G
s
NSS
(x
k
), (11)
k k,s
where f0 (·) is the prior factor on the initial state,
f
IMU
(x k−1,x
k
)representstheIMUpre-integrationconstraint
betweentwokeyframes,andfs (x )collectsthecodeand
GNSS k
phasemeasurementsfromsatellitesatepochk.
Maximizingthisposteriorisequivalenttominimizinganon-
linearleast-squarescostfunctionoftheform
(cid:10)
J(X)=||r0 ||2
Σ−1
+ ||r
k
IMU||2
Σ−1
0 IMU,k
k
(cid:10) (cid:7) (cid:8) Fig.3. HorizontaltrajectorycomparisonbetweentheEKF-basedandFGO-
+ ρ ||rGNSS,s||2 , (12) basedtightlycoupledPPP-B2b/INSsolutions.
k R−1
GNSS,k
k,s
wherer0 isthepriorresidual,r
k
IMU istheIMUpre-integration Inthisexperiment,ahigh-gradefiberopticIMUwasrigidly
residualbetweenx k−1andx
k
,r
k
GNSS,sstacksthecodeandphase m
tra
o
j
u
ec
n
t
t
o
e
r
d
y.
o
T
n
h
t
e
he
fib
p
e
la
r
tf
I
o
M
rm
U
a
d
n
a
d
ta
u
a
s
n
e
d
d
G
to
N
g
S
e
S
ne
r
r
a
a
w
te
m
th
e
e
as
r
u
e
r
f
e
e
m
re
e
n
n
c
t
e
s
residuals for satellite s at epoch k; Σ 0, Σ IMU,k and R GNSS,k
were post-processed in a tightly coupled GNSS/INS scheme
arethecorrespondingcovariancematrices,andρ(·)isarobust
withforward–backwardsmoothing.Theresultingsolutionpro-
lossfunctionappliedtotheGNSSresiduals.
videscentimeter-levelpositionandhigh-accuracyattitude,and
Inthiswork,aHuberkernelisusedasρ(r )tosuppressthe
w,i istreatedasthegroundtruthforevaluatingthereal-timePPP-
influenceofmultipathandoutlierswhilekeepingsmallresiduals
B2b/INSalgorithms.
almost unchanged. In the optimization, for the i-th whitened
residualcomponentr ,theHubercostfunctionisdefinedas
w,i
(cid:11) B. AlgorithmandParameterSettings
1 r2 if|r |≤δ
ρ(r )= 2 w,i w,i . (13) We employ a sliding-window factor graph optimization
w,i δ(|r |− 1 δ) if|r |>δ
w,i 2 w,i framework with a window size of 3 keyframes. Given the 1
Hz GNSS update rate, this corresponds to a time window of
III. EXPERIMENTS
3.0seconds.Statesoutsidethewindowaremarginalizedateach
A. ExperimentalSetup update, so the number of states and factors per optimization
remainsbounded,resultinginboundedper-epochcomputational
Toassesstheeffectivenessoftheproposedfactor-graph-based
cost. A Huber loss with threshold δ =1.5 is applied to the
PPP-B2b/INS integration, one representative dataset was se-
whitenedGNSSresiduals.
lectedfromtheopen-sourceGICI-LIBproject[22].Thedataset
To ensure a fair comparison, the baseline EKF incorporates
containssynchronizeddual-frequencyGNSSandMEMS-IMU
innovation-based outlier detection and IGG III robust filtering
observationscollectedunderdifferentenvironmentalconditions.
[25].Thus,thestudyeffectivelycompares“RobustEKF”against
Dataset5.1wasrecordedinadenseurbanenvironmentwithfre-
the proposed “Robust FGO.” The performance gains are at-
quentsignalblockageandstrongmultipath.Atypicalscenario
tributed to FGO’s iterative relinearization and sliding-window
isshowninFig.2.
optimizationcapabilities,whichoffersuperiorhandlingofnon-
GNSS measurements were processed at 1 Hz, IMU data at
linearitiescomparedtotherecursiveEKF,evenwhenbothutilize
400Hz.ThePPP-B2bcorrectionwasdecodedbySinoK803S
robustkernels.
receiverandaligned,androbustkernelweightingtogetherwith
time-varyingmeasurementcovariancewasappliedwithineach
C. ResultsonDataset5.1
optimization iteration. For comparison, a conventional EKF-
basedtightlycoupledPPP-B2b/INSsolutionwasimplemented Fig. 3 compares the horizontal trajectories obtained from
usingthesameGNSS/IMUdataandPPP-B2bcorrections. theproposedPPP-B2b/INStightlycoupledsolutionswithEKF
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:43:50 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 4 -->

YIetal.:FACTORGRAPH–BASEDTIGHTLYCOUPLEDPPP-B2B/INSFORREAL-TIMEPRECISEPOSITIONING 1889
TABLEI TABLEII
RMSPOSITIONINGERRORSOFTHEPROPOSEDFACTOR-GRAPH-BASED COMPUTATIONALEFFICIENCYCOMPARISON(PEREPOCH)
PPP-B2B/INSSOLUTION
and FGO against the ground truth. At the global scale, both
of 45.6 ms per epoch. This increased computational load is
tightly coupled solutions follow the overall driving path and
expectedandstemsfromtheFGOframework’sspecificdesign:
reproducethemainturnsandstraightsegments,indicatingthat
1) Multiple relinearizations: unlike the single linearization in
thePPP-B2bcorrectionsandtheINSmechanizationareprop-
EKF, the FGO solver performs up to 5 Levenberg-Marquardt
erlyintegrated.However,noticeablediscrepanciesappearwhen
iterations per epoch to iteratively correct linearization errors;
inspectingthelocalenlargedview.
and2)BatchOptimization:Thesolverjointlyoptimizesstates
The zoomed-in inset highlights a representative segment
within a 3.0-second sliding window rather than a single state
around a sharp corner with dense tree cover where satellite
vector.
visibility drops significantly. In this challenging section, the
DespitethehighercomputationalcostcomparedtoEKF,the
EKF-basedsolution(thereddashedtrajectory)exhibitsaclear
FGO processing time (45.6 ms) is significantly lower than the
cross-track bias with respect to the ground truth. In contrast,
GNSS data sampling interval (1000 ms), leaving a substantial
theFGO-basedsolution(bluedash-dottedline)remainsalmost
margin(over95%idletime)forothertasks.Furthermore,asthe
superposedwiththereferencetrajectorythroughoutthestraight
slidingwindowmoves,oldstatesaremarginalized,keepingthe
segmentandclosely.Theseobservationsindicatethatthefactor-
size of the optimization graph constant. This ensures that the
graph formulation can better exploit the temporal correlation
computational cost remains bounded and does not grow over
oftheINSstatesandtheredundancyofmulti-epochPPP-B2b
time. Consequently, the proposed FGO framework achieves a
measurements, thereby constraining the trajectory more effec-
favorabletrade-off,verifyingitscapabilityforonlinereal-time
tively under rapid dynamics and GNSS geometry changes. As
applicationswhiledeliveringthebetteraccuracyandrobustness
aresult,theFGO-basedtightlycoupledPPP-B2b/INSsolution
demonstratedinSectionIII-C.
provides improved horizontal consistency compared with the
conventionalEKFimplementation.
Intheconvergedperiod,theEKFsolutionattainsRMSerrors IV. CONCLUSION
of 0.797 m, 0.954 m, and 1.616 m in the east, north, and
ThisLetterinvestigatedafactor-graph-basedtightlycoupled
up components, respectively, whereas the factor-graph-based
PPP-B2b/INSintegrationschemeforreal-timepreciseposition-
solutionreducestheRMSvaluesto0.490m,0.671m,and0.797
ingwithBDS-3PPP-B2bcorrections.GNSSmeasurementsand
m, as shown in Table I. This corresponds to improvements of
IMUpre-integrationwerejointlymodeledinafactorgraphwith
about 38% (east), 30% (north), and 51% (up) with respect to
robustlossfunctionsandtime-varyingmeasurementcovariance,
the EKF. The improvement is most pronounced in the vertical
so that multipath, signal degradation and correction quality
component, where the factor graph effectively suppresses the
could be handled while maintaining real-time computational
largebiasandlong-termdriftobservedintheEKFtrajectory.
efficiency.UsingonerepresentativedatasetfromtheGICI-LIB,
Overall,theseresultsindicatethattheproposedfactor-graph-
theproposedmethodconsistentlyoutperformedaconventional
based PPP-B2b/INS integration provides faster convergence,
EKF-basedtightlycoupledPPP-B2b/INSsolution,reducingthe
smallersteady-stateerrors,andmorestablebehaviorinallENU
converged RMS position errors from 0.797/0.954/1.616 m to
directionscomparedwiththeconventionalEKF-basedscheme.
0.490/0.671/0.797 m in the east, north and up components,
respectively.Theseresultsdemonstratethatthefactor-graphfor-
D. ComputingEfficiencyandReal-timePerformance
mulationoffersfasterconvergence,highersteady-stateaccuracy
Tovalidatethereal-timefeasibilityoftheproposedscheme, and better robustness under satellite masking and correction
we evaluated the computational efficiency of both the EKF- interruptions, making it a promising alternative to traditional
based and FGO-based algorithms on a standard PC equipped filteringforreal-timePPP-B2b/INSapplications.
with an Intel Core i9-14900HX CPU. The average execution
timesperepochfortheGNSS/INSintegration(at1HzGNSS
ACKNOWLEDGMENT
updaterate)aresummarizedinTableII.
The EKF-TC consumes approximately 4.2 ms per epoch, TheauthorswouldliketothankDr.ChengChifromShanghai
benefitting from its recursive single-step update structure. In JiaoTongUniversityforopen-sourcingtheGICI-Open-Dataset
comparison, the proposed FGO scheme requires an average andcodes.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:43:50 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 5 -->

1890 IEEESIGNALPROCESSINGLETTERS,VOL.33,2026
REFERENCES [14] D. Kiliszek, “GPS and Galileo precise point positioning performance
withtroposphericestimationusingdifferentproducts:BRDM,RTS,HAS,
[1] J.Tao,J.Liu,Z.Hu,Q.Zhao,G.Chen,andB.Ju,“Initialassessmentof and MGEX,” Remote Sens., vol. 17, no. 12, Jun. 2025, Art. no. 2080,
theBDS-3PPP-B2bRTScomparedwiththeCNESRTS,”GPSSolutions, doi:10.3390/rs17122080.
vol.25,no.4,Oct.2021,Art.no.131,doi:10.1007/s10291-021-01168-1. [15] W.Li,C.Pan,J.Gao,Z.Li,andZ.Tao,“Comprehensiveevaluationof
[2] Y.Xu,Y.Yang,andJ.Li,“PerformanceevaluationofBDS-3PPP-B2b real-timeuncombined-PPP/INStightlycoupledintegrationwithBDS-3
precisepointpositioningservice,”GPSSolutions,vol.25,no.4,Oct.2021, PPP-B2bserviceinurbanenvironments,”Meas.Sci.Technol.,vol.36,
Art.no.142,doi:10.1007/s10291-021-01175-2. no.2,Feb.2025,Art.no.026310,doi:10.1088/1361-6501/ad8896.
[3] Y. Yang, Q. Ding, W. Gao, J. Li, Y. Xu, and B. Sun, “Principle and [16] P.Xiao,F.Sun,K.Wang,K.Xiao,X.Shang,andJ.Liu,“Positioning
performanceofBDSBASandPPP-B2bofBDS-3,”Satell.Navigation, performanceanalysisofreal-timeBDS-3PPP-B2b/INStightlycoupled
vol.3,no.1,Dec.2022,Art.no.5,doi:10.1186/s43020-022-00066-2. integration in urban environments,” Adv. Space Res., vol. 72, no. 9,
[4] China Satellite Navigation Office, “BeiDou navigation satellite system pp.4008–4020,Nov.2023,doi:10.1016/j.asr.2023.08.056.
signal in space interface control document: Precise point positioning [17] S.Xin,X.Wang,J.Zhang,K.Zhou,andY.Chen,“Acomparativestudyof
servicesignalPPP-B2b(Version1.0),”Beijing,China:CSNO,2020. factorgraphoptimization-basedandextendedKalmanfilter-basedPPP-
[5] H. Zhou et al., “Multi-frequency BDS-3 real-time positioning per- B2b/INSintegratednavigation,”RemoteSens.,vol.15,no.21,Nov.2023,
formance assessment using new PPP-B2b augmentation service,” Art.no.5144,doi:10.3390/rs15215144.
IEEE Sensors J., vol. 23, no. 5, pp.4994–5002, Mar. 2023, [18] F.R.Kschischang, B.J.Frey,andH.-A. Loeliger,“Factorgraphsand
doi:10.1109/JSEN.2023.3235901. the sum-product algorithm,” IEEE Trans. Inf. Theory, vol. 47, no. 2,
[6] Z.Ren,H.Gong,J.Peng,C.Tang,X.Huang,andG.Sun,“Performance pp.498–519,Feb.2001,doi:10.1109/18.910572.
assessment of real-time precise point positioning using BDS PPP-B2b [19] Z.Yang,X.Ding,Y.Yang,andQ.Wang,“OiSAM-FGO:Anefficient
servicesignal,”Adv.SpaceRes.,vol.68,no.8,pp.3242–3254,Oct.2021, factor graph optimization algorithm for GNSS/INS integrated naviga-
doi:10.1016/j.asr.2021.06.018. tion system,” Satell. Navigation, vol. 6, no. 1, Dec. 2025, Art. no. 23,
[7] W. Dai et al., “BDS-3/GPS uncombined real-time PPP with PPP- doi:10.1186/s43020-025-00173-w.
B2b precise products: Modeling and its long-term performance eval- [20] H. Zhang, X. Xia, M. Nitsch, and D. Abel, “Continuous-time factor
uation,” Adv. Space Res., vol. 75, no. 10, pp.7212–7225, May 2025, graph optimization for trajectory smoothness of GNSS/INS navigation
doi:10.1016/j.asr.2025.01.025. intemporarilyGNSS-deniedenvironments,”IEEERobot.Automat.Lett.,
[8] T. Geng, Z. Li, X. Xie, W. Liu, Y. Li, and Q. Zhao, “Real- vol.7,no.4,pp.9115–9122,Oct.2022,doi:10.1109/LRA.2022.3189824.
time ocean precise point positioning with BDS-3 service signal [21] T. Li, H. Zhang, B. Han, M. Xia, and C. Shi, “Relative accu-
PPP-B2b,” Measurement, vol. 203, Nov. 2022, Art. no. 111911, racy of GNSS/INS integration based on factor graph optimization,”
doi:10.1016/j.measurement.2022.111911. IEEE Sensors J., vol. 24, no. 20, pp.33182–33194, Oct. 2024,
[9] H. Zhou et al., “Real-time single-frequency precise point positioning doi:10.1109/JSEN.2024.3451665.
usingBDS-3PPP-B2bcorrections,”Measurement,vol.205,Dec.2022, [22] C. Chi, X. Zhang, J. Liu, Y. Sun, Z. Zhang, and X. Zhan,
Art.no.112178,doi:10.1016/j.measurement.2022.112178. “GICI-LIB: A GNSS/INS/camera integrated navigation library,” IEEE
[10] C.Ouyang,J.Shi,W.Peng,X.Dong,J.Guo,andY.Yao,“Exploring Robot. Automat. Lett., vol. 8, no. 12, pp.7970–7977, Dec. 2023,
characteristicsofBDS-3PPP-B2baugmentationmessagesbyathree-step doi:10.1109/LRA.2023.3324825.
analysisprocedure,”GPSSolutions,vol.27,no.3,Jul.2023,Art.no.119, [23] X.Xia,L.-T.Hsu,andW.Wen,“Integrity-constrainedfactorgraphop-
doi:10.1007/s10291-023-01457-x. timizationforGNSSpositioning,”inProc.IEEE/IONPositionLocation
[11] N.Naciri,D.Yi,S.Bisnath,F.J.deBlas,andR.Capua,“Assessmentof NavigationSymp.,Monterey,CA,USA,2023,pp.414–420.
Galileohighaccuracyservice(HAS)testsignalsandpreliminaryposition- [24] S.Zhang,R.Tu,Z.Gao,D.Zou,S.Wang,andX.Lu,“LEO-enhanced
ingperformance,”GPSSolutions,vol.27,no.2,Feb.2023,Art.no.73, GNSS/INStightlycoupledintegrationbasedonfactorgraphoptimization
doi:10.1007/s10291-023-01410-y. in the urban environment,” Remote Sens., vol. 16, no. 10, May 2024,
[12] A.S.Pillaietal.,“PerformanceevaluationofMADOCAPPPwithex- Art.no.1782,doi:10.3390/rs16101782.
istingpositioningtechniquesforUAValtitudedetermination,”inProc. [25] Y. Yuanxi, “Robust estimation for dependent observations,”
Int. Conf. Comput. Intell. Appl., Jul. 2025, pp.1–5, doi: 10.1109/CIA- Manuscripta Geodaetica, vol. 19, no. 1, pp.10–17, Feb. 1994,
CON65473.2025.11189728. doi:10.1007/BF03655325.
[13] T. Willems et al., “Disseminating regional ionospheric corrections
from GNSS constellations and application to Galileo high accuracy
service,” GPS Solutions, vol. 29, no. 4, Sep. 2025, Art. no. 194,
doi:10.1007/s10291-025-01955-0.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:43:50 UTC from IEEE Xplore. Restrictions apply.