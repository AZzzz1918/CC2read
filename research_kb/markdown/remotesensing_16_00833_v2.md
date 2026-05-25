<!-- PAGE: 1 -->

remote sensing
Article
Real-Time Precise Orbit Determination of Low Earth Orbit
Satellites Based on GPS and BDS-3 PPP B2b Service
YaliShi1,TianheXu1 ,MinLi1,* ,KaiWei2,ShuaiWang3andDixingWang1
1 InstituteofSpaceSciences,ShandongUniversity,Weihai264209,China;202121029@mail.sdu.edu.cn(Y.S.);
thxu@sdu.edu.cn(T.X.);202221163@mail.sdu.edu.cn(D.W.)
2 QiluAerospaceInformationResearchInstitute,ChineseAcademyofSciences,Jinan250100,China;
weikai@aircas.ac.cn
3 SchoolofSystemsScienceandEngineering,SunYat-SenUniversity,Guangzhou510275,China;
wangsh523@mail2.sysu.edu.cn
* Correspondence:limin0614@sdu.edu.cn;Tel.:+86-19563039268
Abstract:Thisstudyinvestigatesandverifiesthefeasibilityoftheprecisepointpositioning(PPP)-B2b
enhancedreal-time(RT)preciseorbitdetermination(POD)oflowEarthorbit(LEO)satellites.The
principlesandcharacteristicsofmatchingvariousPPP-B2bcorrectionsareintroducedandanalyzed.
The performance and accuracy of broadcast ephemeris and PPP-B2b signals are compared and
evaluatedbyreferringtothepreciseephemeris. Therootmeansquare(RMS)errorsintheGlobal
PositioningSystem(GPS)andBeiDouNavigationSatelliteSystem(BDS)-3broadcastephemeris
orbits in the along direction are larger than those in the other two (radial and cross) directions,
andcorrespondingly,thealongcomponentPPP-B2bcorrectionsaregreatest. Thecontinuityand
smoothnessoftheGPSandBDS-3broadcastephemerisorbitsandclockoffsetsareimprovedwith
thePPP-B2bcorrections. TheavailabilityofPPP-B2bcorrectionsiscomprehensivelyanalyzedfor
theTJU-01satellite.SeveralcomparativeschemesareadoptedfortheRTPODoftheTJU-01satellite
usingthebroadcastephemerisandPPP-B2bcorrections. TheRTPODperformanceisimproved
considerablywiththebroadcastephemeriscorrectedbythePPP-B2bsignals. TheRMSoftheRT
orbitalerrorsintheradial,along,andcrossdirectionsis0.10,0.13,and0.09m,respectively,using
BDS-3 and GPS PPP-B2b corrections, with reference to the solutions calculated with the precise
Citation:Shi,Y.;Xu,T.;Li,M.;Wei,K.;
ephemeris.Theaccuracyisimprovedby5.1%,43.9%,and28.7%inthethreedirections,respectively,
Wang,S.;Wang,D.Real-TimePrecise
relativetothatachievedwiththebroadcastephemeris.Itisconcludedthatagreaterproportionof
OrbitDeterminationofLowEarth
receivedPPP-B2bsatellitesignalscorrespondstoagreaterimprovementintheaccuracyoftheRT
OrbitSatellitesBasedonGPSand
PODoftheLEOsatellite.
BDS-3PPPB2bService.RemoteSens.
2024,16,833. https://doi.org/
10.3390/rs16050833 Keywords:GPS;BDS-3;broadcastephemeris;realtime;PPP-B2b;preciseorbitdetermination
AcademicEditors:JianguoYanand
XiaogongHu
Received:15December2023 1. Introduction
Revised:14February2024 Forthelastfewyears,withanincreasingfrequencyofspacemissions,therehasbeen
Accepted:26February2024 agrowingneedforthepreciseandreal-time(RT)orbitdeterminationoflowEarthorbit
Published:28February2024
(LEO) satellites, which has been widely studied [1–3]. According to the actual Global
PositioningSystem(GPS)broadcastephemeriswiththeJetPropulsionLaboratory’sglobal
differentialGPScorrections,therootmeansquare(RMS)errorinthethree-dimensional(3D)
directionoftheRTPODoftheChallengingMiniSatellitePayload(CHAMP)spacecraft
Copyright: © 2024 by the authors.
is30cm[4]. TheRTPODofMeteorologicalOperationalSatellite-A(MetOp-A)hasbeen
Licensee MDPI, Basel, Switzerland.
performedusingobservationsrecordedbytheglobalnavigationsatellitesystem(GNSS)
Thisarticleisanopenaccessarticle
receiverofanonboardatmosphericsoundinginstrumentandtheresultsindicatethatthe
distributed under the terms and
accuracycanreach0.5minthethreeaxialdirectionsoftheGPSbroadcastephemeris[5].
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// Throughdynamicmodelcompensation,thestandarddeviation(STD)oftheRTPODofthe
creativecommons.org/licenses/by/ Fengyun-3CusingBDS/GPSpseudo-rangemeasurementscanreachthemeterlevel[6].
4.0/).
RemoteSens.2024,16,833.https://doi.org/10.3390/rs16050833 https://www.mdpi.com/journal/remotesensing

<!-- PAGE: 2 -->

RemoteSens.2024,16,833 2of25
TheglobalnetworkingoftheBeidouGlobalNavigationSatelliteSystem(BDS)was
completedin2020. PPP-B2bisoneoftheservicesprovidedbytheBDS-3navigationsystem
andisusedtoenhanceprecisepointpositioning(PPP).ThePPP-B2bsignalisusedasthe
broadcastchannel,andBDS-3geosynchronousorbit(GEO)satellitesbroadcastcorrection
informationtousers. ThissignalprovidesuserswithRTPPPservices[7]. Thewidespread
applicationofPPP-B2bhascoincidedwiththestudyofPPP-B2bbymanyscholars[7–13].
Yangetal. reportedthephysicalpropertiesofPPP-B2bincludingtheareacoveredbyits
signalanditsaccuracyforPPP[14]. Liuetal. foundtheprecisionofPPPenhancedby
PPP-B2bproductsishigherthanthatofRTproductsfromWuhanUniversity[8]. Taoetal.
comparedthekinematicsPPPaccuracywhenusingBDS-3PPP-B2bwiththatwhenusing
theGPSandanRTservice(RTS)providedbytheNationalCentreforSpaceStudies[11].
Chenetal. evaluatedtheperformanceofRTproductsprovidedbytheBDS[15].
ManyscholarshavestudiedRTcorrectionsfortheRTPODofLEOsatellites. When
using the high-quality RT GPS precise ephemeris and clocks from the German Space
OperationsCenterfortheRTPODoftheTerraSyntheticApertureRadar-Xmission,the
RMS error of orbits was 2.1 cm [16]. Xiao et al. (2022) explored an innovative way of
controllingthereceiverclockoffsetqualityintheRTPODfortheGravityRecoveryand
ClimateExperiment(GRACE)follow-onmissionanddemonstratedthattheRMSerrorin
thethreeorthogonaldirectionsoftheRTPODofthemissionusingtheGermanResearch
Centre for Geosciences BeiDou multi-GNSS product is about 8 cm and that using the
NationalCentreforSpaceStudiesRTephemerisisapproximately10cm[17]. Usinghigh-
precisionRTorbitandclockoffsetproductsfromIGS-RTS,theaccuracyoftheRTPODof
GRACE-CintheradialdirectionusingspaceborneGPSobservationsreachesthecentimeter
level [18]. In summary, the accuracy of the RT POD of LEO satellites is improved by
RTcorrections.
AhighlyaccuratebroadcastephemerisisneededfortheRTPODofanLEOsatellite.
TheaccuracyofabroadcastephemeriscanbeimprovedusingthePPP-B2bservice. Al-
thoughspaceborneGNSSdatareceiversdonotreceivePPP-B2bcorrectionscurrently,chips
thatcanreceivethebroadcastephemerisandPPP-B2bsignalatthesametimehavebeen
manufactured,e.g.,theK803boardmanufacturedbySinoGNSS.Therefore,theRTPODof
LEOsatellitescanbeperformedwiththebroadcastephemerisandPPP-B2bservicesbased
on GPS and BDS observations. The present study takes the Tianjin University Satellite
No. 1 (TJU-01) as an example to verify the feasibility of the RT POD of LEO satellites
withthebroadcastephemerisandPPP-B2bservice. ItisthefirsttoanalyzetheGPSand
BDSLEOsatelliteorbitdeterminationbasedonthePPP-B2bservice. TheTJU-01satellite
isanessentialcomponentoftheYunyaoconstellation,withmorethan20satellitestobe
networked. TJU-01waslaunchedinDecember2021,hasamassof20.53kg,andoperates
in a 512 km Sun-synchronous orbit. It is equipped with an onboard GPS and BDS-2/3
multi-GNSSreceiverforGNSSoccultationandPODservice. TheRTPODperformanceof
TJU-01withaPPP-B2bserviceisdemonstratedindetail.
Therestofthisarticleisarrangedasfollows. Themathematicalprinciplesandpro-
cessing of the RT POD using PPP-B2b with its matching and correction algorithm are
introducedanddescribed. Thevariationcharacteristics,accuracy,andavailabilitystatistics
ofthePPP-B2bcorrectionarethenanalyzed. TheexperimentalresultsoftheRTPODofthe
TJU-01satelliteusingPPP-B2banditsimprovementarenextanalyzed. Finally,conclusions
aredrawnfromtheresultsoftheresearch.
2. PrincipleoftheBroadcastEphemerisCorrectionwiththePPP-B2bService
PPP-B2b has seven types of messages for correcting the broadcast ephemeris and
pseudo-rangeobservations. Theapplicationofthesecorrectionsusuallycomprisestwo
parts. Thefirstpartisthematchingofvariouscorrectionsandthesecondisthecorrection
ofthebroadcastephemerisandcodemeasurements.

<!-- PAGE: 3 -->

RemoteSens.2024,16,833 3of25
2.1. MatchingAlgorithmsofPPP-B2bMessages
TherearesevenmessagetypesinPPP-B2b. Thesesevenmessagetypesrefertofive
types of data, namely the satellite mask, differential code bias (DCB), orbit corrections,
clockcorrections,andtheuserrangingaccuracyindex,asgiveninTable1. ThesePPP-B2b
correctionsshouldbematchedbeforebeingmade. ThealgorithmsforPPP-B2bmatching
andcorrectingLANVandCNAVephemeridesduringthereal-timepreciseorbitdetermi-
nation(RTPOD)ofLEOsatellitesareidenticaltothoseusedinotherscenarios,suchas
traditionalPPP,withnodistinction. Firstly,theIssueofDataStateSpaceRepresentation
(IOD SSR) should match between various types of messages before the corrections can
beusedtogether[10]. Secondly, theIssueofDataofthePRNmask(IODP)includedin
message types 4, 5, and 6 must be the same as the IODP of message type 1 before the
correctionsaremade. ThePPP-B2bIssueofData,Navigation(IODN)shouldbeconsistent
withtheGNSSIOD.AninconsistencyindicatesthattheGNSShasupdateditsbroadcast
ephemeris. ThepreviousbroadcastephemerisshouldbeusedformatchingthePPP-B2b
until the PPP-B2b IODN is updated and matches the GNSS IOD. Again, for the same
satellite,theversionnumberoftheclockcorrectionmessage(IODofthecorrection,IOD
Corr)shouldbethesameasintheorbitcorrection,suchthattheclockcorrectionandorbit
correction(inmessagetype2)matcheachother. Finally,thebroadcasttimeofthebroadcast
ephemerismustmatchthebroadcasttimeofitscorrespondingcorrectionmessageand
mustnotexceedthevalidityperiodofthecorrection. Thus,thecorrectionmessagecanbe
used[19]. ThevalidityperiodsofvariousmessagetypesofPPP-B2baregiveninTable1.
Table1.Validityperiodsofvariouscorrections.
TheContentofCorrection MessageType NominalValidity UpdateInterval
Satellitemask 1 86,400s 48s
Orbitcorrection 2,6,7 96s 48s
Clockcorrection 3 86,400s 12s
Differentialcodebias 4,6,7 12s 6s
Userrangingaccuracyindex 2,5,6,7 96s 48s
2.2. CorrectionAlgorithm
AfterthePPP-B2bcorrectionsarematched,weobtainthecorrectedsatelliteposition
withtheorbitcorrectionmessage:
X = X −δX (1)
orbit broadcast
where X denotesthe3Dcoordinatesofsatellitepositionscalculatedthroughthe
broadcast
(cid:2) (cid:3)
broadcast ephemeris. δX = e radial e cross e along ·δO is the orbit correction message,
.
wheree
radial
=
|r
r
|
,e
cross
=
|
r
r
×
×
r
r .|
,ande
along
= e
cross
×e
raidial
,withrbeingthe3Dposition
.
coordinatevectorandr beingthe3DvelocitycoordinatevectorintheECEFcoordinate
system. Thesevectorsareobtainedfromthebroadcastephemeris. e denotesaunitvector
i
withthesubscripti = {radial,along,cross}indicatingthedirectioninthecentroidorbit
coordinatesystem. δOisthe3DorbitcorrectionvectorbroadcastbythePPP-B2bservice.
TheequationforobtainingtheclockoffsetofPPP-B2bis
c
t = t − 0 (2)
satellite broadcast c
wheret istheclockoffsetofPPP-B2b,t istheuncorrectedclockoffsetcalcu-
satellite broadcast
latedfromthebroadcastephemeris,cisaconstantrepresentingthespeedoflight,andc is
0
theclockoffsetcorrection. TheequationoftheDCBcorrectionalgorithmis
(cid:101)l = l −DCB (3)
broadcast B2b

<!-- PAGE: 4 -->

RemoteSens.2024,16,833 4of25
where l denotes the code measurements corresponding to the ranging signals,
broadcast
(cid:101)l denotes the corrected code measurements corresponding to the ranging signals, and
DCB denotes the DCB correction message of the corresponding ranging signal. The
B2b
dual-frequencyionosphere-freecombinationcodemeasurementsobtainedaftertheDCB
correctionare
(cid:101)l =
γ(cid:101)l
1
−(cid:101)l
2 =
γl
1
−l
2 −
γDCB
1
−DCB
2 (4)
γ−1 γ−1 γ−1
f2
γ = 1 (5)
f2
2
where f isthecenterfrequencyofcarrierphasel and f isthecenterfrequencyofthe
1 1 2
carrierphaseandDCB andDCB arethecorrespondingDCBcorrectionmessages. The
1 2
DCBcorrectionisusedtocorrectpseudo-rangeobservations. Itisalsousedtocorrectthe
clockoffsetwhenevaluatingthePPP-B2bclockoffsetinthisstudy.
3. MathematicalModelsfortheRTPODofLEOSatellites
3.1. PreprocessingofPseudo-RangeandCarrier-PhaseMeasurementsafterB2bCorrection
Comparedwithgroundreceivers,LEOsatellitestravelmorequicklyandhaveshorter
signaltrackingtimesforGNSSsatellites,andtheirobservationsthushavegreatergross
errors. ItisthusnecessarytopreprocessthespacebornemeasurementsoftheLEOsatellites.
Theon-the-flydata-editingmethodisadoptedinpreprocessingtheRTPODdataofLEO
satellites using PPP-B2b [2]. PPP-B2b corrections are used for correcting the broadcast
ephemeris and pseudo-range. Next, in the filtering process, the LEO orbit calculated
throughdynamicintegrationcombinedwitheachGNSSsatelliteorbitobtainedfromthe
GNSS broadcast ephemeris corrected by PPP-B2b is used to compute each spaceborne
GNSSreceiverclockoffsetandthencheckwhetherallthesatellitepseudo-rangeresiduals
exceedagiventolerance[20]. Ifso,thepseudo-rangeobservationswithgrosserrorsare
eliminated. The carrier-phase measurements are processed using the same method. If
necessary, the above process is repeated to delete faulty error measurements and thus
ensurethatthedataarecorrect.
3.2. ObservationModel
TheobservationmodelconsideringtheLEOdynamicparametersispresentedinthe
following. An LEO satellite flies above the troposphere, and the tropospheric delay is
thusignored. Thelinearizationionosphere-freeobservationmodelfortheRTPODofLEO
satelliteswithouttroposphericdelayisexpressedas[21]
PG = −uG Φ(t ,t )leo oleo+cδtG +εpG (6)
leo,IF,i leo s 0 leo,i leo,IF,i
LG = −uG Φ(t ,t )leo oleo+cδtG +λG BG +εLG (7)
leo,IF,i leo s 0 leo IF leo,IF leo,IF,i
PC = −uC Φ(t ,t )leo oleo+cδtC +ISBG/C+εpC (8)
leo,IF,i leo s 0 leo leo,IF,i
LC = −uC Φ(t ,t )leo oleo+cδtC +ISBG/C+λC BC +εLC (9)
leo,IF,i leo s 0 leo IF leo,IF leo,IF,i
oleo = (cid:104) xleo,yleo,zleo,x .leo ,y .leo ,z .leo ,pleo,pleo,···pleo (cid:105)T (10)
0 0 0 0 0 0 0 1 2 n
A superscript G indicates the GPS whereas a superscript C indicates the BDS. A
subscript IF indicates ionosphere-free combination observations and a subscript leo in-
dicatesanLEOsatellite. Pindicatestheobserved-minus-computedcodemeasurements
atthecorrespondingepoch. Similarly,Lindicatestheobserved-minus-computedcarrier
measurementsatthecorrespondingepoch. uistheunitvectorinthedirectionfromthe
satellite-borne receiver to the navigation satellite. Φ(t ,t )leo is the matrix for the tran-
s 0
sition between epoch t and epoch t . oleo indicates the unknown initial receiver state.
0 s 0

<!-- PAGE: 5 -->

RemoteSens.2024,16,833 5of25
(cid:104)
xleo,yleo,zleo
(cid:105)T
isthe3DpositionvectoroftheLEOsatellite.
(cid:104)
x
.leo
,y
.leo
,z
.leo (cid:105)T
isthe3Dve-
0 0 0 0 0 0
locityvectoroftheLEOsatellite. [pleo,pleo,···pleo] T aredynamicparametersincludingthe
1 2 n
coefficientofsolarpressureC ,atmosphericdragcoefficientC ,andempiricalacceleration
R D
vectorsa = [a ,a ,a ]inthethreeaxialdirectionsofthecentroidorbitcoordinatesystem.
R a c
cisaconstantrepresentingthespeedoflight. δtisthespacebornereceiverclockoffset.
ISBG/C istheinter-systembias(ISB)parameterbetweentheGPSreceiverclockoffsetand
BDSreceiverclockoffset. Brepresentsthefloating-pointsolutionofambiguity. λisthe
wavelength,εPisthecodemeasurementsnoise,andεListhephasemeasurementsnoise.
ThismodelisapplicabletonotonlythebroadcastephemerisbutalsoPPP-B2b.
3.3. KalmanFilteringModel
InRTPOD,Kalmanfilteringisadoptedtocalculatealltheparameterstobesolved
consideringthemodeldynamics. Thecalculatedparametersare
X = (cid:104) (oleo) T ,δtG ,ISBG/C,(Bs )T (cid:105)T (11)
0 leo,i leo,IF
TheKalmanfilterisfirstinitialized.TheinitialstateestimateXˆ issetasX ref calculated
0 0
fromthekinematicsolutionbasedoncodeobservations.TheinitialstatecovariancePˆ isset
0
asPˆref
inTable4[20].Thefourth-orderRunge–KuttaschemewithRichardsonextrapolation
0
is adopted to calculate the position
(cid:104)
xleo,yleo,zleo
(cid:105)T
and velocity
(cid:104)
x
.leo
,y
.leo
,z
.leo (cid:105)T
in the
0 0 0 0 0 0
predictedstate. Theempiricalaccelerationpredictionis
a i = e−|ti−ti−1|/τ·aˆ i−1 (12)
whereτisthetimecorrespondingtotheempiricalaccelerations. aˆ i−1 isthepredictionof
theempiricalaccelerationatepochtimet i−1 anda i istheempiricalaccelerationatepoch
time t. In a continuous observation arc, the prediction of the coefficients C and C ,
i R D
the prediction of the spaceborne GPS receiver clock offset δt, and the prediction of the
inter-systembiases ISBG/C andtheambiguityparameter(Bs )T areallconstantsduring
leo,IF
thefilterpropagationprocess. Itisthusconcludedthat
(C ,C ,δtG ,ISBG/C,(Bs )T) = (C ,C ,δtG ,ISBG/C,(Bs )T) (13)
R D leo,i leo,IF i R D leo,i leo,IF i−1
Firstly,thetransitionmatrixΦ i,i−1 = ∂X i ref/∂X i r − ef 1 iscalculated. ThepredictedstateXis
thencomputedas
X i = X i ref +Φ i,i−1 (Xˆ i−1 −X i r − ef 1 ) (14)
whereXˆ i−1 denotesthestateestimateatthepreviousepochi−1andX i ref isthereference
statematrixobtainedfromtheobservationinformationatepochi. Thecovariancematrix
P isthencomputedas
i
P i = Φ i,i−1 Pˆ i−1 Φ i T ,i−1 +Q i (15)
Duringthefilteringprocess,thecovarianceandbiasmatricesofsatellitesthatareno
longertrackedbytheLEOsatellitesareclearedandthoseofsatellitesthatareretracedare
initialized[2]. Q istheincreaseincovarianceresultingfromthecumulativeeffectofthe
i
processingnoiseandPˆ i−1 isthecovarianceoftheestimatesatepochi−1. Thegainmatrix
K ,stateestimatesXˆ ,andcovariancematrixPˆ arethenobtainedaccordingto
i i i
K = P HT(HPHT+R )
−1
(16)
i i i i i i
Xˆ = X+K L (17)
i i i
Pˆ= (I−K H)P(I−K H) T +K R KT (18)
i i i i i i

<!-- PAGE: 6 -->

RemoteSens.2024,16,833 6of25
whereR isthemeasurementnoisecovariancematrix. Thenon-negativityofthecovariance
i
matrixisguaranteedbyEquation(18). Thedesignmatrixis H. L denotestheobserved-
i
minus-calculatedcodeandphasemeasurements.
To solve the divergence problem caused by traditional linear Kalman filtering, ex-
tended Kalman filtering is adopted for the RT POD of the LEO satellite in this study.
ref
Here,thereferencestatevectorX iscomputedthroughtheorbitalintegrationofsatellite
i
dynamicsas
X(cid:101) = X
i
ref +x
i
(19)
wherex = (HTPH) −1 HTPL andP = R −1istheweightoftheobservations.Inthisstudy,
i i i i i i i i i
throughhigh-precisionpseudo-rangeobservations,navigationsatelliteorbits,andclock
offsetsobtainedfromthebroadcastephemeriscorrectedbyPPP-B2b,thehigh-precision
3DcoordinateincrementofLEOsatellitesisobtained,andthehigh-precisionorbitsare
transferredtothenextepoch.
3.4. ProcessingStrategy
Dynamic models for the RT POD of the TJU-01 satellite are first introduced. The
detailedRTPODstrategyisthenpresentedinTables2and3. Thisisfollowedbythesetting
ofparametersrelatingtotheprocessingnoise,asgiveninTable4. Theseparametersareset
consideringtheresultsofmultiplepreviousexperiments.
TheGNSSdataprocessingstrategyfortheTJU-01satelliteRTPODispresentedin
Table3.
On the basis of the strategy mentioned above, the data processing is outlined in
Figure1.
Table2.DynamicmodelfortheRTPODoftheTJU-01satellite.
TypeofForce ModelAdopted
Earthgravitymodel EIGEN-6C(70×70)[22]
N-bodydisturbance JPLDE405
Solidtideandpoletide IERS2010[23]
Oceantide FES2014b[24]
Relativeeffect IERS2010[23]
Solarradiationpressure MacroModel[22]
Harris–Priesterdensitymodel,fixedarea,estimatingthedrag
Atmospheredrag
parameterC every240min[20]
D
Earthrotationparameter PredictingEOPfromBulletinAinIERS2010[23]
Sixpiecewiseperiodicaltermsinthethree(along,cross,and
radial)directions,CrandSrrepresentradialperiodical
Empiricalforces
parameters,CtandStrepresentthatinthealongdirection,
andCn,Snforthecrossdirection,estimatedevery90min
Table3.GNSSdataprocessingstrategyfortheTJU-01satelliteRTPOD.
Items ModelAdopted
Carrier-phaseandpseudo-rangeundifferenced
Observationmodel
dual-frequencyionospheric-freecombination
Cut-offelevation 1◦
Processingarc 9-dayarc
Samplinginterval 1s
Terrestrialframe ITRF2020[25]
P=sine/σ2.σ2representsthevarianceincodeor
Observationweight
carrier-phasemeasurements
Receiverclockoffset Whitenoiseestimation
ReceiverISB Randomwalkprocess
Filteringmethod ExtendedKalmanfilter
Ambiguityparameter Floatsolution

<!-- PAGE: 7 -->

RemoteSens.2024,16,833 7of25
Table4.Settingofparametersrelatingtoprocessingnoise.
TheValueofInitial TheValueof
Parameter CorrelationTime
Variance Steady-StateVariance
LEOsatelliteposition[m] 1.0 - -
LEOsatellitevelocity[m/s] 1.0 - -
GPSreceiverclock
500.0 50.0 1s
offset[m]
ISB(G-C)[m] 1.2 1 1s
Empiricalforceaccelerationinradialdirection[nm/s2] 100.0 200.0 1s
Empiricalforceaccelerationinalongdirection[nm/s2] 400.0 800.0 1s
Empiricalforceaccelerationincrossdirection[nm/s2] 200.0 400.0 1s
Remote Sens. 2024, 16, x FOR PEER REVIEW 8 of 26
Ambiguityparameter 0 0 1s
FFiigguurree 11. .PProrocecsessinsign flgoflwo cwhacrht. art.
4. Analysis and Evaluation of the PPP-B2b and Broadcast Ephemeris Performance
Before applying the PPP-B2b signals in the RT POD of LEO satellites, the statistical
characteristics of the PPP-B2b corrections are analyzed and the RT orbit and clock offset
accuracy of the PPP-B2b and broadcast ephemeris is evaluated.

<!-- PAGE: 8 -->

RemoteSens.2024,16,833 8of25
Remote Sens. 2024, 16, x FOR PEER REVIEW 9 of 26
4. AnalysisandEvaluationofthePPP-B2bandBroadcastEphemerisPerformance
4.1. AnalyBseifso roef athpep lCyihnagrathcetePrPisPti-cBs2 bofs itghnea PlsPinP-tBhe2bR TCPoOrrDecotifoLnE TOimsaete Slleitreise,st hestatistical
characteristicsofthePPP-B2bcorrectionsareanalyzedandtheRTorbitandclockoffset
Taking a three-day dataset as an example, the PPP-B2b orbit and clock correction time
accuracyofthePPP-B2bandbroadcastephemerisisevaluated.
series for the GPS (top) and BDS-3 (bottom) are shown in Figure 2. The GPS broadcast
4.1. AnalysisoftheCharacteristicsofthePPP-B2bCorrectionTimeSeries
ephemeris (GPS LANV broadcast ephemeris) orbit errors and their PPP-B2b corrections
Takingathree-daydatasetasanexample,thePPP-B2borbitandclockcorrectiontime
in the along direction are the largest among the three axial directions of the centroid orbit
seriesfortheGPS(top)andBDS-3(bottom)areshowninFigure2. TheGPSbroadcast
coordinate system. Similarly, the BDS-3 medium Earth orbit (MEO) satellite orbit errors
ephemeris(GPSLANVbroadcastephemeris)orbiterrorsandtheirPPP-B2bcorrections
and tinhethire PalPonPg-Bd2irbec ctioornraercetitohenlsa rigne tshtaem aolongngth edtihrerecetiaoxnia ladreir etchtieo nlasrogfethste acemntoronigd othrbei tthree axial
direcctoioorndsi noaft etshyes tceemn.tSriomidila orlryb,tiht ecBoDorSd-3inmaetdei usmysEteamrth. oInrb iatd(MdiEtOio)ns,a ttehlleit eborrobaidtecrarsotr sephemeris
orbita enrdrtohresi raPnPdP -tBh2ebirc oPrrPePct-ioBn2sbi ncothrereaclotniogndsi raecrteio lnaragreetrh feolra rtgheest BamDoSn-3g tIhnectlhinreeeda xGiaeloSynchro-
directionsofthecentroidorbitcoordinatesystem. Inaddition,thebroadcastephemeris
nous Orbit (IGSO) satellites than for the BDS-3 MEO satellites. A comparison of the dif-
orbiterrorsandtheirPPP-B2bcorrectionsarelargerfortheBDS-3InclinedGeoSynchronous
ferent navigation systems reveals that the broadcast ephemeris orbit errors and their PPP-
Orbit(IGSO)satellitesthanfortheBDS-3MEOsatellites. Acomparisonofthedifferent
B2b cnoavrrigeacttiioonnssy satreem ssmreavlelaelrs tfhoart tthhee bBroDaSd-c3a sMteEphOe msaerteislloirtbeist ethrraonrs faonrd tthhee irGPPPSP -sBa2tbellites. It is
conccluordreecdti ofrnosmar ethsem aalbleorvfeo rsuthmemBDaSr-y3 aMnEdO Fsigatuelrleit e2s tthhaant lfaorrgtehre oGrPbSit searterlolirtses a.nIdt icslock offset
concludedfromtheabovesummaryandFigure2thatlargerorbiterrorsandclockoffset
errors correspond to larger corrections and that the broadcast ephemeris errors positively
errorscorrespondtolargercorrectionsandthatthebroadcastephemeriserrorspositively
correlate with the PPP-B2b corrections.
correlatewiththePPP-B2bcorrections.
FigurFei g2u. rPeP2.PP-PBP2-bB 2cbocrorrercetcitoionn ttiimmees seerireise.s.
4.2. Evaluation of the PPP-B2b and Broadcast Orbit Accuracy
The final precision German Research Centre for Geosciences (GFZ) products are a
reference for evaluating the accuracy of RT orbit determination [26]. The broadcast orbit
reference point is the antenna phase center of the navigation satellite as for the PPP-B2b
orbit whereas the GFZ precise orbit reference point is the centroid of the navigation satel-
lite. Therefore, the IGS satellite antenna phase center offset correction file is used for elim-
inating the reference difference among the broadcast, PPP-B2b, and precise orbit. Figure
3 shows the GPS PPP-B2b and broadcast ephemeris orbit error series for a period of 3
days. The graph shows that after correction, the GPS satellite orbit errors in all three

<!-- PAGE: 9 -->

RemoteSens.2024,16,833 9of25
4.2. EvaluationofthePPP-B2bandBroadcastOrbitAccuracy
The final precision German Research Centre for Geosciences (GFZ) products are a
referenceforevaluatingtheaccuracyofRTorbitdetermination[26]. Thebroadcastorbit
referencepointistheantennaphasecenterofthenavigationsatelliteasforthePPP-B2b
orbitwhereastheGFZpreciseorbitreferencepointisthecentroidofthenavigationsatellite.
Remote Sens. 2024, 16, x FOR PEER REVIEW 10 of 26
Therefore,theIGSsatelliteantennaphasecenteroffsetcorrectionfileisusedforeliminating
thereferencedifferenceamongthebroadcast,PPP-B2b,andpreciseorbit. Figure3shows
theGPSPPP-B2bandbroadcastephemerisorbiterrorseriesforaperiodof3days. The
graphshowsthataftercorrection,theGPSsatelliteorbiterrorsinallthreedirectionsare
directions are not only smaller but also smoother, and the errors due to broadcast ephem-
not only smaller but also smoother, and the errors due to broadcast ephemeris update
eris update jumps are thus well compensated. The orbit errors in the along direction are
jumpsarethuswellcompensated. Theorbiterrorsinthealongdirectionarethelargest,
the largest, and correspondingly, the correction in the along direction is the most obvious.
andcorrespondingly,thecorrectioninthealongdirectionisthemostobvious.
FigureF i3gu. rGeP3.SG oPrSboitr beitrreorrro rsseerriieess aaffteterrP PPPP-BP2-bBc2obr rceoctriorenc(tlieoftn) a(nldefwt)i tahnthde wGPitShb trohaed GcaPstSe pbhreomaedricsast ephem-
(right).
eris (right).
Figure4showsthePPP-B2bandbroadcastephemerisorbiterrorseriesfortheBDS-3
FMigEuOrsea t4e lslihteosw. Osv tehrael lP,tPhPe-PBP2Pb-B a2nbdo rbbritoeardrocrassotf ethpehBeDmSe-3riMs EoOrbsiatt eelrlirtoesr asreersileigsh ftolyr the BDS-
3 MEOsm saallteerltlhitaenst.h Oevererroarslli,n ththee PbProPa-dBca2sbt eoprhbeimt eerrirso.rHso owf etvheer, BitDisSp-o3s MsibEleOth saatttehleliBtDesS -a3re slightly
MEOPPP-B2borbitprecisionisalittleworsethantheBDS-3MEObroadcastephemeris
smaller than the errors in the broadcast ephemeris. However, it is possible that the BDS-3
(BDS-3CNAV1broadcastephemeris)orbitprecisioninsomecases. Itisthuspossibleto
MEO PPP-B2b orbit precision is a little worse than the BDS-3 MEO broadcast ephemeris
sacrificesomeorbitalnumericalaccuracytomaketheorbitsmootherandmorecontinuous.
(BDS-3 CNAV1 broadcast ephemeris) orbit precision in some cases. It is thus possible to
sacrifice some orbital numerical accuracy to make the orbit smoother and more continu-
ous. Therefore, the BDS-3 PPP-B2b orbit corrections not only slightly reduce the broadcast
ephemeris orbit errors but also affect their discontinuity due to data updates.

<!-- PAGE: 10 -->

RemoteSens.2024,16,833 10of25
Remote Sens. 2024, 16, x FOR PEER REVIEW 11 of 26
Therefore, the BDS-3 PPP-B2b orbit corrections not only slightly reduce the broadcast
ephemerisorbiterrorsbutalsoaffecttheirdiscontinuityduetodataupdates.
FigureF ig4u. rOer4b.iOt rebrirtoerr rosrersieersie soof fBBDDSS--33 MMEEOOs astealtleitlelsitaefste arfPtPePr -PB2PbPc-oBr2rebc tcioonrr(elecftti)oann d(lwefitth) tahned with the
originoarli gbirnoalabdrcoaasdtc aespthepehmemereirsi s((rriigghhtt))..
Figure5showstheBDS-3IGSOsatellitebroadcastephemerisorbiterrorserieswith
Figure 5 shows the BDS-3 IGSO satellite broadcast ephemeris orbit error series with
andwithoutPPP-B2bcorrection. SimilartothecasefortheBDS-3MEOsatellites,after
and wcoirtrheoctuiotn P,tPhPe-BBD2Sb-3 cIoDrSrOecstaitoelnli.t eSbimroaildacra sttoe pthheem cearisseo rfboirt etrhroer sBaDreSo-3n lyMslEigOh tlsyalteeslslites, after
correcbtuitotnh,e ythaere BsDmSo-o3th IeDr.SFOig usraetse4llaitned b5rtooagdetchaesrtr eevpehaletmhaetrtihse onrubmite erircraolrpsr eacrisei oonnolyft shleightly less
but thberoya adrceas stmoroboittahnedr.P FPiPg-uBr2ebso 4rb aitnodf t5h etoBgDeSth-3eIrG rSeOvesaatle tllhitaet itshmeu ncuhmwoerrsiecathl apnrethcaistion of the
ofthecorrespondingBDS-3MEOsatellite. Thisisduetoonlyafewmonitoringstations
broadcast orbit and PPP-B2b orbit of the BDS-3 IGSO satellite is much worse than that of
inspecificareasreceivingsignalsfromtheIGSOsatellites,resultinginapoorgeometric
the corresponding BDS-3 MEO satellite. This is due to only a few monitoring stations in
configurationwhencalculatingtheIGSOsatellitebroadcastephemeris. Theorbitaccuracy
specifiofct ahereIaGsS Orescaetievlliintegs issitghnuasllso wfreormth athneth IaGtoSfOth seaMteEllOitseast,e rlleitseus.lting in a poor geometric con-
figurationT owmhaekne acnalincu-dleapttihncgo mthpea rIiGsoSnOo fstahteeolrlbitiet nburmoeardiccaalsptr eecpishioenmbeetrwise.e nThthee oPPrbP-iBt 2abccuracy of
andbroadcastephemeris,theRMSerrorsofthePPP-B2bandbroadcastephemerisorbitare
the IGSO satellites is thus lower than that of the MEO satellites.
calculatedfor9daysofdata. TheobtainedorbitprecisionsarepresentedinFigure6and
Table5.TheRMSerrorsoftheGPSPPP-B2borbitinthethreeaxialdirectionsofthecentroid
orbitcoordinatesystemare0.12(radial),0.34(along),and0.26(cross)m,respectively. These
valuesaremuchsmallerthanthoseoftheGPSbroadcastephemeris,whichare0.17,0.92,
and0.49minthecorrespondingdirections. Insummary,theGPSPPP-B2bclearlyimproves
theGPSbroadcastorbits. ThesameisobservedfortheBDS-3satellites. TheBDS-3MEO
satellitebroadcastorbitismoreaccuratethanthatoftheGPSsatellitebroadcastephemeris

<!-- PAGE: 11 -->

RemoteSens.2024,16,833 11of25
asinter-satellitelinkobservationsareinvolvedinthegenerationoftheBDS-3MEOsatellite
Remote Sens. 2024, 16, x FOR PEER REVIEWb roadcastorbit[12]. IthasbeenreportedthatthenumericalprecisionoftheBDS-3satellite 12 of 26
broadcastephemerisorbitiscurrentlymuchhigherthanthatof1yearago,astheorbit
accuracyisimprovingevery6months.
FigureF i5g.u Orer5b.iOt rebrirtoerrr soerrsieersie osfo fBBDDSS--33 IIGGSSOOP PPPP-PB2-Bb2(lbe f(tl)eafntd) tahnedB DthSe-3 BIGDSSO-3b rIoGaSdOca sbtreopahedmcaersits ephemeris
(right()r.i ght).
Table5.StatisticalaccuracyofGPSandBDS-3satelliteorbits.
To make an in-depth comparison of the orbit numerical precision between the PPP-
B2b and broadcast ephemerisM, tEhOeO RrbMitS(R MerSr/omr)s of the PPPIG-BSO2bO arbnitd( RbMroS/amd)cast ephemeris
EphemerisType
orbit are calculated for 9 dRaaydsia olf daAtalo. nTghe obCtaroisnsed orRbaidti aplrecisAiolonnsg are pCrreosssented in Fig-
ure 6 andB DTSabbrloea d5c.a Tsthe RMS errors of the GPS PPP-B2b orbit in the three axial directions
0.11 0.31 0.28 0.17 0.34 0.47
of the centrepohidem oerribsit coordinate system are 0.12 (radial), 0.34 (along), and 0.26 (cross) m,
BDSPPP-B2b 0.10 0.27 0.24 0.15 0.32 0.41
respectively. These values are much smaller than those of the GPS broadcast ephemeris,
GPSbroadcast
0.17 0.92 0.49 - - -
which are e0p.h1e7m, e0ri.s92, and 0.49 m in the corresponding directions. In summary, the GPS
GPSPPP-B2b 0.12 0.34 0.26 - - -
PPP-B2b clearly improves the GPS broadcast orbits. The same is observed for the BDS-3
satellites. The BDS-3 MEO satellite broadcast orbit is more accurate than that of the GPS
satellite broadcast ephemeris as inter-satellite link observations are involved in the gener-
ation of the BDS-3 MEO satellite broadcast orbit [12]. It has been reported that the numer-
ical precision of the BDS-3 satellite broadcast ephemeris orbit is currently much higher
than that of 1 year ago, as the orbit accuracy is improving every 6 months.

<!-- PAGE: 12 -->

Remote Sens. 2024, 16, x FOR PEER REVIEW 13 of 26
RemoteSens.2024,16,833 12of25
Figure6.RMSerrorsinGPSsatelliteorbits(top)andBDS-3satelliteorbits(bottom).
Figure 6. RMS errors in GPS satellite orbits (top) and BDS-3 satellite orbits (bottom).
4.3. EvaluationoftheRTClockOffsetAccuracy
Table 5. Statistical accuracy of GPS and BDS-3 satellite orbits.
TheRTclockoffsetperformanceisassessedusingtheGFZpreciseclockoffsetproduct
asareference. Beforecomparison,itisnecessarytoeliminatethereferencetimedifferences
MEO Orbit (RMS/m) IGSO Orbit (RMS/m)
Ephemeris Type among the broadcast clock offset, PPP-B2b clock offset, and precise clock offset of the
Radial Along Cross Radial Along Cross
BDS-3systemusingthetimegroupdelayandtheDCB.WethenselectG32andC40asthe
BDS broadcast referencesatelliteclocksfortheGPSsatellitesandBDS-3satellites,respectively,tomake
0.11 0.31 0.28 0.17 0.34 0.47
ephemeris thetimedatumconsistentbetweenthebroadcastclockoffsetandpreciseclockoffset. The
samemethodisappliedtothePPP-B2bclockoffset. Thecomparisonresultsarepresented
BDS PPP-B2b 0.10 0.27 0.24 0.15 0.32 0.41
inFigure7.
GPS broadcast
Owingtothemonitoringstationsbeingdistributedinsmalllocalareas,onlypartof
0.17 0.92 0.49 - - -
ephemeris thearcofthePPP-B2bclockcorrectionisbroadcast. InthecaseoftheGPSPPP-B2bclock
GPS PPP-B2b offse0t.,1t2h ereareju0m.3p4s inthee0r.r2o6r atregular-i ntervalsthatc-o mpensatefor- thelargeslips
inthebroadcastclockoffsetsresultingfromtheupdatingofthebroadcastephemeris. In
addition,thebroadcastclockoffseterrorsaregreateraftercorrection,mainlybecauseof
4.3. Evaluation of the RT Clock Offset Accuracy
systematicbiasesinthePPP-B2bcorrections. Furthermore,systembiasesareincludedin
The RT clock othffesceotr preecrtfeodrcmloacnkcoef fisse ta.sAseltshsoeudg husthinegB DthSe-3 GPFPZP- Bp2rbeccilsoec kclooffcske tosffalsseot cpornotadin- system
uct as a reference. bBieasfoesr,es uccohmspysatreimsoatnic, ibti aisse nsedcoensostaaryff etcot tehleimRTinPaOteD tahcec urreafceyr.eFnigcue rteim7seh odwifs-thatthe
PPP-B2bclockoffseterrorstendtobemorecontinuousandsmootherthantheerrorsofthe
ferences among the broadcast clock offset, PPP-B2b clock offset, and precise clock offset
of the BDS-3 system using the time group delay and the DCB. We then select G32 and C40
as the reference satellite clocks for the GPS satellites and BDS-3 satellites, respectively, to
make the time datum consistent between the broadcast clock offset and precise clock off-
set. The same method is applied to the PPP-B2b clock offset. The comparison results are
presented in Figure 7.

<!-- PAGE: 13 -->

RemoteSens.2024,16,833 13of25
broadcastephemeris,whicheffectivelyreducestheerrorsduetodataupdating. Owing
tothesystemicbias, thesystematicSTDisusedintheevaluationofthenine-dayclock
offsetdatasets. AlltheevaluationresultsareshowninFigure8. Aftercorrection,theSTD
obtainedfortheGPSPPP-B2bclockoffsetis0.03m,whichis50%lessthanthatoftheGPS
broadcastclockoffset. Similarly,theSTDoftheBDS-3PPP-B2bclockoffsetis6.8cm,which
is70%lessthanthatoftheBDS-3broadcastclockoffset. Figure7showsthattheerrorsin
theGPSPPP-B2bclockoffsetscontainsystematicbiasesandaremuchlargerthanthosein
theBDS-3clockoffsets. Aimingatreducingtheeffectofsystematicbiasesinevaluatingthe
PPP-B2bperformance,asegmentedstatisticsstrategyisappliedtotheGPSPPP-B2band
broadcastclockoffseterrors. TheGPS-PPPB2bandbroadcastclockoffseterrorseriesare
dividedintotheseveralidenticalsegmentsbasedontheGPSPPP-B2bclockoffseterror
jumpcausedbythebroadcastephemerisupdate. TheSTDofeachsegmentoftheclock
offseterrorforeachsatellitewascalculated,thentheaverageoftheseSTDsofeachsatellite
wascalculatedandtheaverageoftheseSTDsofallsatelliteswastakentoobtaintheSTD
Remote Sens. 2024, 16, x FOR PEER REVIEW 14 of 26
oftheentiresatellitesystematlast. TheresultingSTDsoftheGPSPPP-B2boffseterrorsare
smallerthanthoseoftheBDS-3PPP-B2boffseterrors.
Figure 7. Error series iFni gthuree G7.PESr (rtoorpse) raiensdi nBtDheS-G3P (Sb(otottpo)man) dbrBoDaSd-3ca(bsto tctloomck) borffoasdectass atncldo cPkPoPff-sBet2sba cnldocPkP P-B2b
offsets. clockoffsets.
Owing to the monitoring stations being distributed in small local areas, only part of
the arc of the PPP-B2b clock correction is broadcast. In the case of the GPS PPP-B2b clock
offset, there are jumps in the error at regular intervals that compensate for the large slips
in the broadcast clock offsets resulting from the updating of the broadcast ephemeris. In
addition, the broadcast clock offset errors are greater after correction, mainly because of
systematic biases in the PPP-B2b corrections. Furthermore, system biases are included in
the corrected clock offset. Although the BDS-3 PPP-B2b clock offsets also contain system
biases, such systematic biases do not affect the RT POD accuracy. Figure 7 shows that the
PPP-B2b clock offset errors tend to be more continuous and smoother than the errors of
the broadcast ephemeris, which effectively reduces the errors due to data updating. Ow-
ing to the systemic bias, the systematic STD is used in the evaluation of the nine-day clock
offset datasets. All the evaluation results are shown in Figure 8. After correction, the STD
obtained for the GPS PPP-B2b clock offset is 0.03 m, which is 50% less than that of the GPS
broadcast clock offset. Similarly, the STD of the BDS-3 PPP-B2b clock offset is 6.8 cm,
which is 70% less than that of the BDS-3 broadcast clock offset. Figure 7 shows that the
errors in the GPS PPP-B2b clock offsets contain systematic biases and are much larger than
those in the BDS-3 clock offsets. Aiming at reducing the effect of systematic biases in eval-
uating the PPP-B2b performance, a segmented statistics strategy is applied to the GPS
PPP-B2b and broadcast clock offset errors. The GPS-PPP B2b and broadcast clock offset
error series are divided into the several identical segments based on the GPS PPP-B2b
clock offset error jump caused by the broadcast ephemeris update. The STD of each seg-
ment of the clock offset error for each satellite was calculated, then the average of these
STDs of each satellite was calculated and the average of these STDs of all satellites was

<!-- PAGE: 14 -->

Remote Sens. 2024, 16, x FOR PEER REVIEW 15 of 26
taken to obtain the STD of the entire satellite system at last. The resulting STDs of the GPS
RemoteSens.2024,16,833 14of25
PPP-B2b offset errors are smaller than those of the BDS-3 PPP-B2b offset errors.
Figure 8. STDs of GPFSig aunred8 B.DSTSD-3s osfaGtePllSitaen dcloBDckS -o3ffsasteetl leitreroclrosc kwoiftfhse atnerdr owrsitwhiothuat nPdPwPi tBh2obu tcPoPrrPeBc2tibocno.r rection.
4.4. ComparisionoftheGloballyAveragedSignalinSpaceRangeErrorofPPP-B2bandBroadcast
4.4. Comparision of Ethmep Gehleorbisally Averaged Signal in Space Range Error of PPP-B2b and
Broadcast Empeheris
Thesignalinspaceinspacerangeerrorsaremoreeffectivetocharacterizethecom-
The signal in mspoancoer binit sapnadccel orcaknegrero errsrionrtsh earsea tmelloitree-u esfferedctiirvecet itoon sc.hTahriascatertriiczlee ttahkee sctohmes-ignalin
spacerangeerror(SISRE)asthekeyperformanceindicatorofthesystem. Accordingto
mon orbit and clock errors in the satellite-user directions. This article takes the signal in
MontenbruckOliverandXuxiaofei(2021)[27,28],thecombinederroroftheradialorbit
space range error (SISRE) as the key performance indicator of the system. According to
errorandclockerror∆RTcanroughlycharacterizethegloballyaveragedsignalinspace
Montenbruck Oliv
r
e
a
r
n g
a
e
n
e
d
r r
X
or
u
. T
x
h
ia
e
o∆f
R
ei
T ,
(2
S
0
IS
2
R
1
E
)
,
[
a
2
n
7
d
,2
S
8
I
]
S
,
R
t
E
he
(O
c
R
o
B
m
)
b
ar
i
e
n
c
e
a
d
lc
e
u
r
la
r
t
o
e
r
d
o
a
f
s
t
f
h
ol
e
lo
r
w
a
s
d
:
ial orbit
Δ
error and clock error RT can roughly characterize the globally averaged signal in space
range error. The Δ RT , SISRE, and SISRE (O ∆ RRBT) a = reW cRa · lc ∆ uXlraatdeiadl − asc · fo ∆ ltl s ows: (20)
(cid:113)
SI Δ SRRTE = W= ⋅Δ [RXMS(W − c· ⋅Δ∆tXs )]2+W2 ·(A2+C2) (20) (21)
orb R radial R radial A,C
(cid:113)
SISRE = [RMS(W ·∆X −c·∆ts)]2+W2 ·(A2+C2) (22)
SISRE = [RMS(W ⋅Δ X R )]2r+ad W ial2 ⋅(A2 + C2) A,C (21)
orb R radial A,C
where W and W2 are the weight factors for the statistical contribution of radial (R),
R A,C
along-track (A), and cross-track (C) errors to the line-of-sight ranging error. ∆X is
radial
thSeISoRrbEit = erro[RriMnSth(eWrad ⋅Δ iaXldirec − tiocn ⋅Δ ;ct·s)r]e2p + reWsen2ts ⋅ t(hAe2li + ghCt2s)pe edinavacuu(2m2;)and∆ts
R radial A,C
representstheclockoffseterror. AandCaretheRMSoftheorbiterrorsinthealongand
where W and Wcro2ss d a i r r e ec t ti h o e n s w ,r e e i s g p h ec t t f iv a e c l t y o . r T s h f e o w r e t i h g e h t s f t a a c t t i o s r t s ic u a s l e c d o f n or tr c i a b lc u u t l i a o t n in g of t h r e ad SI i S a R l E (R ar ) e , shown
R A,C
inTable6.
Δ
along-track (A), and cross-track (C) errors to the line-of-sight ranging error. X is the
radial
orbit error in the radial direction; c ⋅ represents the light speed in a vacuum; and Δ ts
represents the clock offset error. A and C are the RMS of the orbit errors in the along and

<!-- PAGE: 15 -->

Remote Sens. 2024, 16, x FOR PEER REVIEW 16 of 26
cross directions, respectively. The weight factors used for calculating the SISRE are shown
in Table 6.
Table 6. The weight factors used for SISRE computation.
RemoteSens.2024,16,833 15of25
Type
W W2
Ephemeris R A,C
Table6.TheweightfactorsusedforSISREcomputation.
GPS 0.98 1/49
Type
W W2
EpheBmDerSi-s3 MEO 0.98 R A,C 1/54
BDS-3 IGSO GPS 0.98 0.98 1/491/126
BDS-3MEO 0.98 1/54
BDS-3IGSO 0.98 1/126
Δ
The GPS and BDS-3 PPP-B2b and broadcast ephemeris RT time series are shown
in Figure
T h
9
e
.
G
T
P
h
S
e
a
R
n
T
d B
s
D
er
S
i
-
e
3
s
P
v
P
a
P
l
-
u
B
e
2b
s
a
o
n
f
d
G
b
P
ro
S
a d
P
c
P
a
P
st
-
e
B
p
2
h
b
e m
ar
e
e
ri s
la∆r
R
g
T
er
t im
th
e
a
s
n
e r
t
i
h
es
o
a
s
r
e
e
o
sh
f
o
t
w
he
n
broadcast
epheimnFeirgius reva9l.uTeh,e bReTcaseursiees tvhaelurees iosf Ga PlSarPgPePr- Bs2ybstaeremla brgiears thina nththeo sGePofSt hPePbPro-Bad2cba sctlock offset
Δ
errore.p Ahefmteerr icsovrarleucet,iboenca, utsheet hereRiTsa ltairmgeer ssyesrtieems boifa sthinet PhePGPP-BS2PbP Pa-nB2db bclroocakdocffasestt eerprohr.emeris are
Aftercorrection,the∆RTtimeseriesofthePPP-B2bandbroadcastephemerisaresmoother
smoother than the broadcast ephemeris. Just like the clock offset series curve and orbit
thanthebroadcastepheΔmeris. Justliketheclockoffsetseriescurveandorbiterrorseries
error series curve, the RT series also indicate that the PPP-B2b can reduce the effect
curve,the∆RTseriesalsoindicatethatthePPP-B2bcanreducetheeffectcausedbyerror
caused by error jumps compared to the broadcast ephemeris.
jumpscomparedtothebroadcastephemeris.
FigurFeig 9u.r Tei9m.Teim seersieersie osfo fΔ∆RRTT ffoorrP PPPPP-B-2Bb2abn danbdro abdrcoaasdtecpahsetm eeprhise.meris.
TheSISREandSISRE(ORB)ofthePPP-B2bandbroadcastephemerisareshownin
The SISRE and SISRE (ORB) of the PPP-B2b and broadcast ephemeris are shown in
Table7. ComparedtotheGPSbroadcastephemeris,theSISRE(ORB)ofGPSPPP-B2bhas
Table 7. Compared to the GPS broadcast ephemeris, the SISRE (ORB) of GPS PPP-B2b has
increasedby37.5%andtheSISREofGPSPPP-B2bhasincreasedby141.7%. Comparedto
incretahseeBdD Sb-y3 b3r7o.a5d%ca astnedp htehme eSriIsS,RthEe SoIfS RGEP(SO RPBP)Po-fBB2DbS -h3aPsP iPn-Bcr2ebahsaesdin bcrye a1s4ed1.b7y%2.9 C.8%ompared to
the BanDdSt-h3e bSIrSoRaEdocfaBsDt Se-p3hPePmP-Ber2ibs,h atshien cSreIaSsRedE b(yO1R0.B3%) .oIft cBanDbSe-3se ePnPfPro-mB2Tba bhlea7s ainndcreased by
thestatisticaldatacalculatedabovethatafterPPP-B2bcorrection,theaccuracyoftheGPS
29.8% and the SISRE of BDS-3 PPP-B2b has increased by 10.3%. It can be seen from Table
broadcastephemerisandBDS-3broadcastephemerishavebeenimprovedsignificantly.
7 and the statistical data calculated above that after PPP-B2b correction, the accuracy of
the GPS broadcast ephemeris and BDS-3 broadcast ephemeris have been improved signif-
icantly.

<!-- PAGE: 16 -->

RemoteSens.2024,16,833 16of25
Table7.TheSISRE(ORB)andSISREofthebroadcastephemerisandPPP-B2b.
Type
SISRE(ORB)/m SISRE/m
Ephemeris
GPSbroadcast
1.29 0.54
Ephemeris
GPSPPP-B2b 0.81 0.22
BDS-3broadcastephemeris 1.77 0.14
BDS-3PPP-B2b 1.24 0.12
5. RTPODProcessingandAnalysis
Firstly, theavailabilityoftheonboardGNSSobservationsoftheTJU-01satelliteis
analyzed. ThevisibilityoftheGPSandBDS-3PPP-B2bsignalsisplottedandanalyzed.
ThePPP-B2bimprovementintheRTPODoftheTJU-01satelliteisverified.
5.1. AvailabilityAnalysisofOnboardGNSSData
High-qualityGNSSonboardobservationsarerequiredfortheaccurateRTPODof
LEOsatellites.Inthissubsection,theavailabilityofonboardGNSSobservationsmadeon31
January2022isanalyzedasanexample. TheonboardGNSSreceiverontheTJU-01satellite
tracksallGPSsatellitesand33BDS-2/3satellites. Thereceiverchannelsareassignedto
5GEOsatellitesincludingC01–C05, 7IGSOsatellitesincludingC06–C16, and22MEO
satellitesincludingC11,C12,C14,C19–C30,andC32–C37. Thesamplingintervalis1s.
Approximately8GPSsatellitesand12BDSsatellitesonlyaretrackedinthesameepoch
owingtothelimitednumberofnavigationchannels. Theundifferencedionosphere-free
pseudo-rangeandcarrier-phasecombinationmodelusedinthisstudyrequiresGPS/BDS
dual-frequencyphaseandcodemeasurementsateachepoch. Here,thedataavailabilityof
thesatelliteisdefinedastheratioofthenumberofepochswithcompletedual-frequency
observations to the total number of epochs for that satellite. The data availability of
theobservationsoftheTJU-01satelliteisanalyzedasfollows. Figure10showsthatthe
availabilityofGPSobservationsisclearlylowerthanthatoftheBDSobservations,which
mayleadtotheRTPODhavingaloweraccuracywhenusingtheGPSthanwhenusing
theBDS.
5.2. AvailabilityofPPP-B2bintheRTPODoftheTJU-01Satellite
ThisstudyassumesthattheTJU-01satellitecanreceivePPP-B2bsignals.Thesampling
interval for the TJU-01 satellite observations used in the visibility analysis is 30 s. The
TJU-01satelliteobservationonboardGNSSreceivercantrack8GPSsatellitesand12BDS
satellites,includingBDS-2andBDS-3. Owingtotherestricteddistributionofmonitoring
stations,PPP-B2bcanonlyprovidecorrectionsofflightarcsovertheAsia–Pacificregionfor
theBDS-3andGPSsatellites. ConsideringthehighspeedofLEOsatellites,theirgeometric
configuration with GEO will constantly change. When the Earth is located on the line
connectingGEOandLEOsatellites,itwillobstructthesignalofGEOsatellites,andLEO
satelliteswillnotbeabletoreceivethePPP-B2bcorrection. Theavailabilityandvisibilityof
PPP-B2barecomputedandplottedfortheTJU-01satelliteateachepochon31January2022,
asshowninFigures11and12andTable8(GPS)andTable9(BDS-3). Figure11presents
thenumberofsatellitesthatcanreceivePPP-B2bcorrectionsateachepochcorresponding
tothesub-satellitepointtrajectoryoftheTJU-01satellite. UptoeightGPSsatellitescan
receivePPP-B2bcorrectionsatacertainepoch,whereasuptosevenBDS-3satellitescan
receivethePPP-B2bcorrection.

<!-- PAGE: 17 -->

Remote Sens. 2024, 16, x FOR PEER REVIEW 17 of 26
Table 7. The SISRE (ORB) and SISRE of the broadcast ephemeris and PPP-B2b.
Type
SISRE (ORB)/m SISRE/m
Ephemeris
GPS broadcast
1.29 0.54
Ephemeris
GPS PPP-B2b 0.81 0.22
BDS-3 broadcast ephemeris 1.77 0.14
BDS-3 PPP-B2b 1.24 0.12
5. RT POD Processing and Analysis
Firstly, the availability of the onboard GNSS observations of the TJU-01 satellite is
analyzed. The visibility of the GPS and BDS-3 PPP-B2b signals is plotted and analyzed.
The PPP-B2b improvement in the RT POD of the TJU-01 satellite is verified.
5.1. Availability Analysis of Onboard GNSS Data
High-quality GNSS onboard observations are required for the accurate RT POD of
LEO satellites. In this subsection, the availability of onboard GNSS observations made on
31 January 2022 is analyzed as an example. The onboard GNSS receiver on the TJU-01
satellite tracks all GPS satellites and 33 BDS-2/3 satellites. The receiver channels are as-
signed to 5 GEO satellites including C01–C05, 7 IGSO satellites including C06–C16, and
22 MEO satellites including C11, C12, C14, C19–C30, and C32–C37. The sampling interval
is 1 s. Approximately 8 GPS satellites and 12 BDS satellites only are tracked in the same
epoch owing to the limited number of navigation channels. The undifferenced iono-
sphere-free pseudo-range and carrier-phase combination model used in this study re-
quires GPS/BDS dual-frequency phase and code measurements at each epoch. Here, the
data availability of the satellite is defined as the ratio of the number of epochs with com-
plete dual-frequency observations to the total number of epochs for that satellite. The data
availability of the observations of the TJU-01 satellite is analyzed as follows. Figure 10
shows that the availability of GPS observations is clearly lower than that of the BDS ob-
servations, which may lead to the RT POD having a lower accuracy when using the GPS
RemoteSens.2024,16,833 17of25
than when using the BDS.
Figure 10. Data availability rate of the GPS (top) and BDS (bottom) observations onboard the
TJU-01satellite.
Table8.StatisticalavailabilityoftheGPSPPP-B2bfortheTJU-01Satellite.
NumberofSatellites 0 1 2 3 4 5 6 7 8
Available
800 471 475 450 223 177 79 33 3
epochs
TotalnumberofGPS
6400 3768 3800 3600 1784 1416 632 264 24
satellites
Epoch
proportion 29.5 17.4 17.5 16.5 8.2 6.5 2.9 1.2 0.1
(%)
Quantityproportion
0 12.5 25 37.5 50 67.3 75 87.3 100
(%)
Table9.StatisticalavailabilityofPPP-B2bfortheTJU-01satellite.
NumberofSatellites 0 1 2 3 4 5 6 7
Available
338 543 462 520 436 291 68 2
epochs
TotalnumberofBDS3
2628 4071 3493 3981 3334 2209 500 21
satellites
Epoch
12.7 20.3 17.3 19.5 16.3 10.9 2.5 0.1
proportion(%)
Quantityproportion(%) 0 13.3 26.5 39.2 52.3 65.9 81.6 66.7

<!-- PAGE: 18 -->

Remote Sens. 2024, 16, x FOR PEER REVIEW 18 of 26
Figure 10. Data availability rate of the GPS (top) and BDS (bottom) observations onboard the TJU-
01 satellite.
5.2. Availability of PPP-B2b in the RT POD of the TJU-01 Satellite
This study assumes that the TJU-01 satellite can receive PPP-B2b signals. The sam-
pling interval for the TJU-01 satellite observations used in the visibility analysis is 30 s.
The TJU-01 satellite observation onboard GNSS receiver can track 8 GPS satellites and 12
BDS satellites, including BDS-2 and BDS-3. Owing to the restricted distribution of moni-
toring stations, PPP-B2b can only provide corrections of flight arcs over the Asia–Pacific
region for the BDS-3 and GPS satellites. Considering the high speed of LEO satellites, their
geometric configuration with GEO will constantly change. When the Earth is located on
the line connecting GEO and LEO satellites, it will obstruct the signal of GEO satellites,
and LEO satellites will not be able to receive the PPP-B2b correction. The availability and
visibility of PPP-B2b are computed and plotted for the TJU-01 satellite at each epoch on
31 January 2022, as shown in Figures 11 and 12 and Table 8 (GPS) and Table 9 (BDS-3).
Figure 11 presents the number of satellites that can receive PPP-B2b corrections at each
epoch corresponding to the sub-satellite point trajectory of the TJU-01 satellite. Up to eight
RemoteSens.2024,16,833 GPS satellites can receive PPP-B2b corrections at a certain epoch, whereas up to s1e8voefn2 5
BDS-3 satellites can receive the PPP-B2b correction.
Figure 11. Sub-satellite point trajectory of the TJU-01 satellite with available numbers of GPS PPP-
Figure11.Sub-satellitepointtrajectoryoftheTJU-01satellitewithavailablenumbersofGPSPPP-B2b
B2b (top) and BDS PPP-B2b (bottom) corrections.
(top)andBDSPPP-B2b(bottom)corrections.
Figure12showsthepercentagesoftheGPSandBDS-3satellitesreceivingcorrections
relativetothenumberofsatellitesobservedbytheTJU-01satelliteateachepochonasingle
day. Itisseenthatcomparedwiththesignalsobservedbygroundstations,thePPP-B2b
signalsobservedbyBDS-3andtheGPShaveawidergeographicalrange. Thegeographical
rangeinwhichPPP-B2bisreceivedbytheGPSandBDS-3navigationsystemsismuch
largerthanthegeographicalrangeofgroundstations,mainlybecausetheTJU-01satellite
ismuchhigherthanthegroundstations.
ThepercentageGPSreceptionissmallerthanthepercentageBDS-3receptionfortwo
mainreasons. Firstly,fewerGPSsatellitesthanBDS-3MEOsatellitesreceivethePPP-B2b
signals. ThismainlyresultsfromthedifferentconfigurationsoftheGPSandBDS-3satellite
constellations. Secondly, more GPS satellites than BDS-3 satellites are observed by the
TJU-01satelliteateachepoch.
Figures 11 and 12 reveal that except over the southeastern Pacific, southwestern
Atlantic,andSouthAmerica,theTJU-01satellitereceivesPPP-B2bsignalsfromabovemost
partsoftheworld. ThemainreceivingareaofthePPP-B2bsignalfortheTJU-01satelliteis
overtheChinesemainland.

<!-- PAGE: 19 -->

Remote Sens. 2024, 16, x FOR PEER REVIEW 19 of 26
Figure 12 shows the percentages of the GPS and BDS-3 satellites receiving corrections
relative to the number of satellites observed by the TJU-01 satellite at each epoch on a
single day. It is seen that compared with the signals observed by ground stations, the PPP-
B2b signals observed by BDS-3 and the GPS have a wider geographical range. The geo-
graphical range in which PPP-B2b is received by the GPS and BDS-3 navigation systems
is much larger than the geographical range of ground stations, mainly because the TJU-01
satellite is much higher than the ground stations.
The percentage GPS reception is smaller than the percentage BDS-3 reception for two
main reasons. Firstly, fewer GPS satellites than BDS-3 MEO satellites receive the PPP-B2b
signals. This mainly results from the different configurations of the GPS and BDS-3 satel-
lite constellations. Secondly, more GPS satellites than BDS-3 satellites are observed by the
TJU-01 satellite at each epoch.
Figures 11 and 12 reveal that except over the southeastern Pacific, southwestern At-
lantic, and South America, the TJU-01 satellite receives PPP-B2b signals from above most
RemoteSens.2024,16,833 parts of the world. The main receiving area of the PPP-B2b signal for the TJU-01 satell1i9teo f25
is over the Chinese mainland.
FiguFirgeu 1r2e. 1D2i.stDriibsturtiibount ioofn thoef tphreopproorptioornt ioofn PoPfPP-PBP2-bB s2ibgnsaigl nvaislivbiisliitbyil fitryomfro tmhe tThJeUT-J0U1 -s0a1teslaltiteell. ite.
ThedetailedstatisticalavailabilityoftheGPSPPP-B2bfortheTJU-01satelliteisgiven
Table 8. Statistical availability of the GPS PPP-B2b for the TJU-01 Satellite.
inTable8. ThevalidnumberofGPSobservationsoftheTJU-01satelliteis2711epochs. The
Nnuummbbeerr ooff Ssaatteelllliitteess obse0r vedis1 20,2372, andth3e numbe4r ofPPP5 -B2bco6r rection7 srec8e ived
is525A3v.aTilhabelne umbersofepochsreceivingdifferentnumbersofcorrectionsaregivenin
800 471 475 450 223 177 79 33 3
Table8e.pTohcehse pochsreceivingPPP-B2baccountfor70.5%ofallepochs.Theepochsreceiving
morethanthreePPP-B2bcorrectionsaccountfornearly35%ofallepochs. Thenumber
Total number of GPS
of PPP-B2b corrections64re0c0e iv3e7d68b y3t8h0e0T JU3-60010s ate1ll7it8e4 exc1e4e1d6s 50%63o2f the26n4u m2b4e r of
satellites
satellitesobservedatthesameepochaccountinnearly19%ofallepochs. Relativetothe
GPSbroadcastephemeris,theGPSPPP-B2battheseobservedepochsshouldimprovethe
accuracyoftheRTPODoftheTJU-01satellite.
The detailed statistical availability of the BDS-3 PPP-B2b for the TJU-01 satellite is
giveninTable9.ThevalidnumberofobservationsoftheTJU-01satelliteis2667epochs.The
numberofsatellitesobservedis20,295,andthenumberofPPP-B2bcorrectionsreceived
is 6669. The epochs receiving PPP-B2b account for 87.3% of all epochs. The epochs
receivingPPP-B2bcorrectionsaccountfornearly50%ofallepochs.ThenumberofPPP-B2b
correctionsreceivedbytheTJU-01satelliteexceeds50%ofthenumberofepochsatellitesin
nearly30%ofallepochs. RelativetotheBDS-3broadcastephemeris,theBDS-3PPP-B2bat
theseobservedepochsimprovestheaccuracyoftheRTPODoftheTJU-01satellite.
Figures11and12andTables8and9revealthatcomparedwiththecasefortheBDS-3
satellites,theGPSsatellitesreceivePPP-B2bdataoverasmallergeographicalrange. There
aretwomainreasons. (1)Theconstellationconfigurationsaredifferent. TheMEOsatellites
ofBDS-3arehigherthantheGPSsatellites,whichallowstheTJU-01satellitetomonitor
theBDS-3MEOsatelliteflyingovertheAsia–Pacificregionforlonger. (2)Owingtothe
smallernumberofsignalchannels,theGPSobservationdataintegrityislowerthanthatof

<!-- PAGE: 20 -->

RemoteSens.2024,16,833 20of25
theBDS-3observationdata,resultinginfeweravailableGPSPPP-B2bcorrectionsanda
smallergeographicalrangeofreceptionfortheGPSPPP-B2b. Thesedifferencesmayresult
Remote Sens. 2024, 16, x FOR PEER REVIEW 21 of 26
inthedifferentaccuracyoftheRTPODoftheTJU-01satellite.
5.3. ResultsandAnalysisoftheRTPODoftheTJU-01Satellite
Inthisstudy,theRTPODoftheTJU-01satelliteisperformedinasimulatedmode
with a precise orbit and clock offset from GFZ are used for reference to assess our RT POD
basedonrealonboardobservationsconsideringPPP-B2bsignals. Thepost-PODsolutions
performance. The post-processed orbits overlap differences of TJU-01 are 2–3 cm in the
withapreciseorbitandclockoffsetfromGFZareusedforreferencetoassessourRTPOD
radipael,r faolromnagn,c ae.nTdh cerpoossst -dpriorececstsioednso rfbriotsmo vJearnlaupadriyff e2r8e ntcoe s5 oFfeTbJUru-0a1ryar 2e022–23.c Imn iannth eeffort to test
the ernadhiaaln,caelomnge,natn deffcreocsts odfi rPecPtiPo-nBs2frbo monJa tnhuea rRyT2 8PtOo5DF oebf rLuEarOy 2s0a2t2e.lIlnitaens,e tfhfoer trteostuesltts of the RT
theenhancementeffectofPPP-B2bontheRTPODofLEOsatellites,theresultsoftheRT
POD of the TJU-01 satellite on 31 January 2022 are compared, as presented in Figure 13,
PODoftheTJU-01satelliteon31January2022arecompared,aspresentedinFigure13,
for the GPS PPP-B2b versus the GPS broadcast ephemeris, the BDS-3 PPP-B2b versus the
fortheGPSPPP-B2bversustheGPSbroadcastephemeris,theBDS-3PPP-B2bversusthe
BDS-3 broadcast ephemeris, and the GPS and BDS-3 PPP-B2b versus the GPS and BDS-3
BDS-3broadcastephemeris,andtheGPSandBDS-3PPP-B2bversustheGPSandBDS-3
broabdrocaadsct aesptehpehmemereirsis..
Figure13.ComparisonoferrorseriesoftheRTPODoftheTJU-01satelliteusingthePPP-B2band
Figubrero 1ad3c. aCstoemphpeamreisrios.n of error series of the RT POD of the TJU-01 satellite using the PPP-B2b and
broadcast ephemeris.
Figure13revealsthatPPP-B2bimprovestheRTPODaccuracyoftheTJU-01satellite.
TheRTPODerrorswhenusingPPP-B2baresmallerthanthosewhenusingthebroadcast
Figure 13 reveals that PPP-B2b improves the RT POD accuracy of the TJU-01 satellite.
ephemeris. Meanwhile,thenavigationsatelliteorbiterrorsandTJU-01satellite’sRTPOD
The eRrrTo rPsOinDth eerarloonrgs dwirhecetnio nusairnegth PePlaPrg-eBs2tbam aorneg stmheatlhlerere tdhiarenc ttiohnoss.eIt wishtheuns ucosninclgu dtehde broadcast
ephethmatetrhies.o Mrbietaenrrworhsiolfet,h tehnea nviagvatiigoantsiaotnel lsitaetsealnlidtet hoerRbTit PeOrrDoerrsr oarnsdof TthJUeL-0E1O ssaatteellllitietes’s RT POD
arepositivelycorrelated. TofurtherassesstheimprovementeffectofPPP-B2bontheRT
errors in the along direction are the largest among the three directions. It is thus concluded
that the orbit errors of the navigation satellites and the RT POD errors of the LEO satellites
are positively correlated. To further assess the improvement effect of PPP-B2b on the RT
POD of the TJU-01 satellite, the 9-day results are compared and averaged in Figure 14 and
Table 10. Figure 14 shows that the TJU-01 satellite RT POD errors decrease the most in the
along direction among the three directions, as PPP-B2b has the greatest correction in the
along direction for the navigation satellite orbit errors.

<!-- PAGE: 21 -->

RemoteSens.2024,16,833 21of25
PODoftheTJU-01satellite,the9-dayresultsarecomparedandaveragedinFigure14and
Table10. Figure14showsthattheTJU-01satelliteRTPODerrorsdecreasethemostinthe
Remote Sens. 2024, 16, x FOR PEER REVIEW 22 of 26
alongdirectionamongthethreedirections,asPPP-B2bhasthegreatestcorrectioninthe
alongdirectionforthenavigationsatelliteorbiterrors.
Figure 14. Comparison of the RMS of the orbit errors in radial, along, and cross directions for the
Figure14.ComparisonoftheRMSoftheorbiterrorsinradial,along,andcrossdirectionsfortheRT
RT PPOODD ooff tthheeT TJUJ-U01-0s1at eslalitteel.lite.
TTabalbel1e0 .1C0o smhpoawrisso nthoaftth tehree saucltcsuorfathceyR oTfP tOhDe RofTth PeOTJDU- 0o1fs tahteell iTteJUbe-tw01ee snattheelulisteeo ifst hheigher when
usinbgro tahdeca BstDepSh-e3m berrisoaanddcPaPsPt- Be2pbh. emeris than when using the GPS broadcast ephemeris and
Directhioingher whReand iuals(iRnMgS t/mhe) BDS-3 PPPA-Blo2nbg (tRhManS/ mw)hen using thCer oGssP(SR MPSP/mP)-B2b. The reasons
are as folNloowt s. (1) OwBi2nbg to the inNteotr-satellite Bli2nbks, the BDNSo-t3 broadcasBt2 borbit accuracy is
Ephemeris higherC tohrarenct ethde GPCS obrrreocateddcast oCrobrriet catecdcuracCyo. r(r2e)c tMedore BCDoSrr-e3ct sedatelliteCso rtrhecatned GPS satellites
GPSbroadcastephemerirseceive P0P.1P5-B2b. (3) T0.h12e integrity0 .o28f GPS obse0r.1v9ations is w0.o19rse than th0a.1t4 of BDS-3 obser-
BDS-3broadcastephemeris 0.12 0.11 0.23 0.20 0.16 0.13
vations. Furthermore, the most accurate scheme is using GPS and BDS-3 PPP-B2b for the
GPS+BDS-3broadcast
0.11 0.10 0.21 0.13 0.12 0.09
ephemeris RT POD of the TJU-01 satellite, as there are more onboard observation GNSS data and
more navigation satellites receiving PPP-B2b corrections.
Table10showsthattheaccuracyoftheRTPODoftheTJU-01satelliteishigherwhen
Tablues 1in0g. tChoemBDpaSr-3isborno aodfc tahset erpehseumltse roisf tthhaen RwTh ePnOuDsi nogf tthhee GTPJUSb-0ro1a sdactaesltlietep hbeemtwereisena ntdhe use of the
broahdicgahsetr ewphheenmuesriinsg atnhde BPDPSP--3BP2PbP. -B2bthanwhenusingtheGPSPPP-B2b. Thereasonsare
Direction Radial (RMS/m) Along (RMS/m) Cross (RMS/m)
Ephemeris Not B2b Not B2b Not B2b
Corrected Corrected Corrected Corrected Corrected Corrected
GPS broadcast
0.15 0.12 0.28 0.19 0.19 0.14
ephemeris
BDS-3 broadcast
0.12 0.11 0.23 0.20 0.16 0.13
ephemeris
GPS + BDS-3 broad-
0.11 0.10 0.21 0.13 0.12 0.09
cast ephemeris
5.4. Correlation Analysis of PPP-B2b Reception Ratio and Accuracy Improvement Ratio

<!-- PAGE: 22 -->

RemoteSens.2024,16,833 22of25
asfollows.(1)Owingtotheinter-satellitelinks,theBDS-3broadcastorbitaccuracyishigher
Remote Sens. 2024, 16, x FOR PEER REVIEW 23 of 26
thantheGPSbroadcastorbitaccuracy. (2)MoreBDS-3satellitesthanGPSsatellitesreceive
PPP-B2b. (3)TheintegrityofGPSobservationsisworsethanthatofBDS-3observations.
Furthermore,themostaccurateschemeisusingGPSandBDS-3PPP-B2bfortheRTPODof
theTTJUh-e0 1cosrarteellalittieo,na sbtehtwereeeanr eRmNo rgeiovnenbo bayrd Eoqbusaetrivoant i(o2n3)G aNndSS δda gtaivaennd bmyo Erequnaatviiogna t(i2o4n)
r
s
is
a t
n
e
e
ll
x
it
t
e
a
s
n
r
a
e
l
c
y
e
z
iv
e
i
d
n
,
g
w
P
h
P
e
P
re
-B 2
R
bNc o
is
rr
t
e
h
c
e
ti o
ra
n
t
s
i
.
o of the number of navigation satellites receiving
r
PPP-B2b corrections to the number of navigation satellites observed at a certain epoch.
5.4. CorrelationAnalysisofPPP-B2bReceptionRatioandAccuracyImprovementRatio
The superscript N indicates the navigation system. N = G indicates the GPS whereas
The correlation between RN given by Equation (23) and δ given by Equation (24)
N = C indicates the BDS. The surbscript r represents reception. NUM is the number
is next analyzed, where RN is the ratio of the number of navigation saBt2ebllites receiving
of PPP-B2b corrections thart the TJU-01 satellite receives at a certain epoch for a certain
PPP-B2bcorrectionstothenumberofnavigationsatellitesobservedatacertainepoch. The
navigation system whereas NUM is the number of the navigation satellites observed
superscript N indicatesthenavigaatlilonsystem. N =GindicatestheGPSwhereas N =C
by the TJU-01 satellite at the same epoch. δ is the percentage improvement, due to PPP-
indicatestheBDS.Thesubscriptrrepresentsreception. NUM isthenumberofPPP-B2b
B2b
B2b, in the accuracy of the RT POD of the TJU-01 satellite relative to the broadcast ephem-
corrections that the TJU-01 satellite receives at a certain epoch for a certain navigation
seyrisst.e m S Brwoadh earnedas S NBU2b Mar
a
e
ll
tihset hReTn PuOmDb eerrroofrst hfoern tahvei TgJaUti-o0n1 ssaatteelllliittees wohbesne ruvseidngb tyhteh beroTaJUd--
0ca1ssta etpelhleitmeeartisth aensda PmPePe-Bp2obc hfo.rδ niasvtihgeatpioernc esynstategme iNm ipnr othvee mtherenet, odrutheotgooPnaPlP d-Bir2ebct,iionnsth aet
aac cceurrtaaciny eopfothche.R MTiPnOorD gorofstsh eerTroJUrs- 0in1 sδat eallriet ereremlaotviveed,t oanthde δbr otiamdcea ssetreiepsh aerme etrhiesn. S fitted
Broad
aanndd Ssmooartheethde. TRhTeP tOimDee rsreorriessf oorf thReNT JaUn-d01 δsa toevlleitre twheh ecnouurssine gotfh oenber odaadyc aasrtee sphhoewmne riins
B2b r
aFnigduPreP P15-B. I2tb isf osreenna vthigaat taio lnarsgyesrt emδ Ncorinretshpeotnhdres etoo rat hgoregaotnear limdiprercotvioenmseantt ainc ethrtea iPnPePp-oBc2hb.
Moribniot rdegtreorsmsienrarotirosni nacδcuarreacrye.m Woev ehda,vaen dδtimeseriesarethenfittedandsmoothed. The
timeseriesofRN andδoverthecourseofonedayareshowninFigure15. Itisseenthata
r S −S
largerδcorrespondstoagreaterimprovδem=enbtroaidntheB2PbP P-B2borbitdeterminationaccur
(
a
2
c
3
y
)
.
Wehave S
B2b
S −S
δ = broad B2b (23)
S
NBU2bM
RN = B2b (24)
RN =
r NUNUMMB2
a b ll (24)
r NUM
all
FFiigguurree 1155.. CCoorrrreellaattiioonn aannaallyyssiiss ooff tthhee PPPPPP--BB22bb rreecceeppttiioonn rraattiioo aanndd aaccccuurraaccyy iimmpprroovveemmeenntt rraattiioo..
Figure 15 shows that RN and δ are positively correlated. As the proportion of PPP-
r
B2b corrections received increases, the improvement in the accuracy of the RT POD of the
TJU-01 satellite using PPP-B2b increases. However, the correlation between the GPS PPP-
B2b reception ratio and accuracy improvement ratio is slightly different from that for the

<!-- PAGE: 23 -->

RemoteSens.2024,16,833 23of25
Figure15showsthat RN andδarepositivelycorrelated. AstheproportionofPPP-
r
B2b corrections received increases, the improvement in the accuracy of the RT POD of
theTJU-01satelliteusingPPP-B2bincreases. However,thecorrelationbetweentheGPS
PPP-B2breceptionratioandaccuracyimprovementratioisslightlydifferentfromthatfor
theBDS-3. ThisismainlyduetothedifferentmissingobservationepochsbetweentheGPS
andBDS-3intheTJU-01satelliteobservationsandtheinterpolationof RN and δ inthe
r
differentmissing,thuscausingcorrelationdifferences. Inaddition,forthesamereception
ratio,differentnumbersofGPSandBDS-3satellitesareobservedbytheTJU-01satellite.
AsthenumbersofGPSandBDS-3satellitesthatcanreceivePPP-B2baredifferent,thereare
differencesintheimprovementintheobservationaccuracy. Therefore,therearedifferences
betweentheGPSandBDS-3inthecorrelationbetweenthePPP-B2breceptionratioand
accuracyimprovementratio.
6. Conclusions
Thefollowingconclusionsaredrawnfromtheresultsofthisstudy.
1. TheRMSoftheGPSbroadcastephemerisorbiterrorsinthealongdirection(0.92m)is
greaterthanthatintheradialdirection(0.17m)andthatinthecrossdirection(0.49m).
Inaddition,errorsinthealongdirectionarecorrectedmostbytheGPSPPP-B2b(by
approximately60%)amongthethreedirections. TheRMSoftheGPSPPP-B2borbit
errorsintheradial,along,andcrossdirectionsis0.12,0.34,and0.26m,respectively.
2. ForBDS-3,theorbiterrorsofPPP-B2bareafewcentimeterssmallerthanthoseof
thebroadcastephemeris. TheorbiterrorsoftheIGSOsatellitebroadcastephemeris
aremuchgreaterthanthoseoftheMEOsatellitebroadcastephemeris,andtheorbit
correction of the IGSO satellites is greater than the orbit corrections of the MEO
satellites. The RMS of the MEO satellite PPP-B2b orbit errors in the radial, along,
andcrossdirectionsis0.10,0.27,and0.24m,whichisbetterthanthoseoftheIGSO
satellites,0.15,0.32,and0.41m,respectively.
3. PPP-B2bcorrectionimprovesthebroadcastclockoffsetaccuracyremarkably. ForBDS-
3,theaveragevalueoftheSTDsofthePPP-B2bclockoffsetisapproximately0.07m.
Theaccuracyis70%higherthanthatofthebroadcastephemerisclockoffset. Forthe
GPS,theaveragevalueoftheSTDsofthePPP-B2bclockoffsetisapproximately0.03m,
i.e.,theaccuracyis50%betterthanthatofthebroadcastephemerisclockoffset.
4. Thesmoothnessandcontinuityofthenavigationsatelliteorbitandclockoffseterror
seriesareimprovedbythePPP-B2bservice,whichreducestheerrorsintroducedby
broadcastephemerisdataupdates.
5. AstheTJU-01satelliteismuchhigherthangroundstations,ithasawidergeographical
range of PPP-B2b reception. Up to eight GPS satellites can receive the PPP-B2b
correction at a certain epoch whereas up to seven BDS-3 satellites can receive the
PPP-B2bcorrection.
6. MoreBDS-3satellitesthanGPSsatellitescanreceivePPP-B2b. TheBDS-3andGPS
satellite constellations have different configurations, and the integrity of the GPS
observationsislowerthanthatoftheBDS-3observations.
7. As PPP-B2b mainly reduces errors in the broadcast ephemeris orbit in the along
direction,theerrorsintheRTPODoftheTJU-01satelliteusingPPP-B2binthealong
directionaresmallerthanthosewhenusingthebroadcastephemeris.
8. TheaccuracyoftheRTPODoftheTJU-01satellitewhenusingtheGPSbroadcast
ephemerisislowerthanthatwhenusingtheBDS-3broadcastephemerisbecausethe
inter-satellitelinksimprovetheaccuracyoftheBDS-3broadcastephemeris,andmore
BDS-3satellitesthanGPSsatellitesreceivePPP-B2b. Moreover,theintegrityofthe
GPSobservationsislowerthanthatoftheBDS-3observations.
9. ThemostaccurateschemeisusingtheGPSandBDS-3PPP-B2bfortheRTPODof
the TJU-01 satellite. The accuracy is improved by 5.1%, 43.9%, and 28.7%, respec-
tively,intheradial,along,andcrossdirectionsrelativetousingtheGPSandBDS-3
broadcastephemeris.

<!-- PAGE: 24 -->

RemoteSens.2024,16,833 24of25
10. AstheproportionofPPP-B2bcorrectionreceptionincreases,theaccuracyimprove-
mentofPPP-B2bintheRTPODoftheTJU-01satelliteincreases.
AuthorContributions:Conceptualization,M.L.andT.X.;methodology,Y.S.;software,Y.S.andK.W.;
validation,Y.S.andS.W.;formalanalysis,Y.S.;investigation,M.L.andT.X.;resources,M.L.andT.X.;
datacuration,Y.S.;writing—originaldraftpreparation,Y.S.;writing—reviewandediting,M.L.and
T.X.;visualization,S.W.andD.W.;supervision,M.L.andT.X.;projectadministration,M.L.andT.X.;
fundingacquisition,M.L.andT.X.Allauthorshavereadandagreedtothepublishedversionof
themanuscript.
Funding: ThisresearchwasfundedbytheNationalNaturalScienceFoundationofChina(Grant
No.42204015),NationalKeyResearchandDevelopmentProgramofChina(2020YFB0505800and
2020YFB0505804),andtheNaturalScienceFoundationofShandongProvince(ZR2022QD094).
DataAvailabilityStatement:Themulti-GNSSpreciseclockandorbitproductscanbeaccessedat
ftp://igs.ign.fr//pub/igs/products/mgex/(accessedonfrom28January2022toto5February2022),
theGPSLANVbroadcastephemeriscanbeachievedatftp://igs.gnsswhu.cn/pub/gps/data/daily/
(accessedonfrom28January2022toto5February2022),theBDS-3CNAV1broadcastephemeris
canbeachievedatftp://ftp2.csno-tarc.cn/cnav/2022/(accessedonfrom28January2022toto5
February2022),andthePPP-B2bdatawerereceivedbytheK803boardfromtheSinoNavcompany
(www.sinognss.com(accessedonfrom28January2022toto5February2022)).Theexperimentaldata
includingtheTJU-01onboardGNSSdata(accessedonfrom28January2022toto5February2022)
presentedinthisstudyareavailablebycontactingthecorrespondingauthorwithreasonablerequest.
Acknowledgments:WeareverygratefultotheInternationalGNSSService(IGS)forprovidingthe
muti-GNSSdataandproducts..ThanksalottoTianJinYunyaoAerospaceTechnologyCorporation
forprovidingtheTJU-01onboardGNSSdata.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Lee,B.-S.;Yoon,J.-C.;Hwang,Y.;Kim,J.Orbitdeterminationsystemforthekompsat-2usinggpsmeasurementdata. Acta
Astronaut.2005,57,747–753.[CrossRef]
2. Montenbruck,O.;Ramos-Bosch,P.Precisionreal-timenavigationofleosatellitesusingglobalpositioningsystemmeasurements.
GPSSolut.2007,12,187–198.[CrossRef]
3. Yang,Y.;Yue,X.;Dempster,A.G.Gps-basedonboardreal-timeorbitdeterminationforleosatellitesusingconsiderkalmanfilter.
IEEETrans.Aerosp.Electron.Syst.2016,52,769–777.[CrossRef]
4. Reichert,A.;Meehan,T.;Munson,T.Towarddecimeter-levelreal-timeorbitdetermination: Ademonstrationusingthesac-c
andchampspacecraft. InProceedingsofthe15thInternationalTechnicalMeetingoftheSatelliteDivisionofTheInstituteof
Navigation(IONGPS2002),LosAngeles,CA,USA,4–7February2002;pp.1996–2003.
5. Montenbruck,O.;Hauschild,A.;Andres,Y.;vonEngeln,A.;Marquardt,C.(near-)real-timeorbitdeterminationforgnssradio
occultationprocessing.GPSSolut.2013,17,199–209.[CrossRef]
6. Xiong,C.;Lu,C.;Zhu,J.;Ding,H.Orbitdeterminationusingrealtrackingdatafromfy3c-gnos.Adv.SpaceRes.2017,60,543–556.
[CrossRef]
7. Tang,J.;Lyu,D.;Zeng,F.;Ge,Y.;Zhang,R.Comprehensiveanalysisofppp-b2bserviceanditsimpactonbds-3/gpsreal-time
ppptimetransfer.RemoteSens.2022,14,5366.[CrossRef]
8. Liu,Y.;Yang,C.;Zhang,M.Comprehensiveanalysesofppp-b2bperformanceinchinaandsurroundingareas.RemoteSens.2022,
14,643.[CrossRef]
9. Ren,Z.;Gong,H.;Peng,J.;Tang,C.;Huang,X.;Sun,G.Performanceassessmentofreal-timeprecisepointpositioningusingbds
ppp-b2bservicesignal.Adv.SpaceRes.2021,68,3242–3254.[CrossRef]
10. Tang,C.;Hu,X.;Chen,J.;Liu,L.;Zhou,S.;Guo,R.;Li,X.;He,F.;Liu,J.;Yang,J.Orbitdetermination,clockestimationand
performanceevaluationofbds-3ppp-b2bservice.J.Geod.2022,96,60.[CrossRef]
11. Tao,J.;Liu,J.;Hu,Z.;Zhao,Q.;Chen,G.;Ju,B.Initialassessmentofthebds-3ppp-b2brtscomparedwiththecnesrts.GPSSolut.
2021,25,131.[CrossRef]
12. Xu, Y.; Yang, Y.; Li, J.Performanceevaluationofbds-3ppp-b2bprecisepointpositioningservice. GPSSolut. 2021, 25, 142.
[CrossRef]
13. Yang,Y.;Ding,Q.;Gao,W.;Li,J.;Xu,Y.;Sun,B.Principleandperformanceofbdsbasandppp-b2bofbds-3.Satell.Navig.2022,
3,5.[CrossRef]
14. Yang,Y.;Liu,L.;Li,J.;Yang,Y.;Zhang,T.;Mao,Y.;Sun,B.;Ren,X.Featuredservicesandperformanceofbds-3.Sci.Bull.2021,66,
2135–2143.[CrossRef]

<!-- PAGE: 25 -->

RemoteSens.2024,16,833 25of25
15. Chen,J.;Zhang,Y.;Yu,C.;Wang,A.;Song,Z.;Zhou,J.Modelsandperformanceofsbasandpppofbds.Satell.Navig.2022,3,4.
[CrossRef]
16. Wermuth,M.;Hauschild,A.;Montenbruck,O.;Kahle,R.Terrasar-xpreciseorbitdeterminationwithreal-timegpsephemerides.
Adv.SpaceRes.2012,50,549–559.[CrossRef]
17. Xiao,G.;Liu,G.;Ou,J.;Zhou,C.;He,Z.;Chen,R.;Guo,A.;Yang,Z.Real-timecarrierobservationqualitycontrolalgorithmfor
precisionorbitdeterminationofleosatellites.GPSSolut.2022,26,102.[CrossRef]
18. Li,D.;Zhou,X.;Li,K.Centimeter-levelorbitdeterminationofgrace-cusingigs-rtsdata.RemoteSens.2023,15,1832.[CrossRef]
19. Yang,H.;He,X.;Ferreira,V.;Ji,S.;Xu,Y.;Song,S.Assessmentofprecipitablewatervaporretrievedfromprecisepointpositioning
withppp-b2bservice.EarthSci.Inform.2023,16,315–328.[CrossRef]
20. Li,M.;Xu,T.;Shi,Y.;Wei,K.;Fei,X.;Wang,D.Adaptivekalmanfilterforreal-timepreciseorbitdeterminationoflowearthorbit
satellitesbasedonpseudorangeandepoch-differencedcarrier-phasemeasurements.RemoteSens.2022,14,2273.[CrossRef]
21. Li,B.;Ge,H.;Ge,M.;Nie,L.;Shen,Y.;Schuh,H.Leoenhancedglobalnavigationsatellitesystem(legnss)forreal-timeprecise
positioningservices.Adv.SpaceRes.2019,63,73–93.[CrossRef]
22. Förste,C.;Bruinsma,S.;Flechtner,F.;Abrykosov,O.;Dahle,C.;Marty,J.;Lemoine,J.;Biancale,R.;Barthelmes,F.;Neumayer,K.
Eigen-6c3-thelatestcombinedglobalgravityfieldmodelincludinggocedatauptodegreeandorder1949ofgfzpotsdamand
grgstoulouse.InProceedingsoftheAGUFallMeetingAbstracts,SanFrancisco,CA,USA,5–9December2011;p.G51A-0860.
23. Luzum,B.;Petit,G.Theiersconventions(2010):Referencesystemsandnewmodels.InProceedingsoftheIAUGeneralAssembly,
Beijing,China,20–31August2012.
24. Spiridonov,E.;Vinogradova,O.Y.Oceanictidemodelfes2014b:Comparisonwithgravitymeasurements.Izv.Atmos.Ocean.Phys.
2020,56,1432–1446.[CrossRef]
25. Altamimi, Z.; Rebischung, P.; Collilieux, X.; Métivier, L.; Chanard, K.Itrf2020: Anaugmentedreferenceframerefiningthe
modelingofnonlinearstationmotions.J.Geod.2023,97,47.[CrossRef]
26. Yang,Y.;Li,J.;Wang,A.;Xu,J.;He,H.;Guo,H.;Shen,J.;Dai,X.Preliminaryassessmentofthenavigationandpositioning
performanceofbeidouregionalnavigationsatellitesystem.Sci.ChinaEarthSci2014,57,144–152.[CrossRef]
27. Montenbruck,O.;Steigenberger,P.;Hauschild,A.Multi-gnsssignal-in-spacerangeerrorassessment–methodologyandresults.
Adv.SpaceRes.2018,61,3020–3038.[CrossRef]
28. Xu,X.;Nie,Z.;Wang,Z.;Zhang,Y.;Dong,L.Animprovedbds-3ppp-b2bpositioningapproachbyestimatingsignalinspace
rangeerrors.GPSSolut.2023,27,110.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.