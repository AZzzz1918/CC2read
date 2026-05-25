<!-- PAGE: 1 -->

Real-timekinematicorbitdetermination(KOD)basedonbroad-
castephemerides(BRD)enablesonboardhigh-rateorbitupdatesfor
Real-Time Kinematic Orbit lowEarthorbit(LEO)missionsbutwithlimitedaccuracy.Withthe
operationalavailabilityoftheGalileoHighAccuracyService(HAS)
and the BDS-3 Precise Point Positioning-B2b (PPP-B2b), real-time
Determination for LEO by
high-accuracycorrectionshavebecomeaccessibletospacebornere-
ceivers, enhancing orbit determination performance. Nevertheless,
Integrating Broadcast eachproductexhibitsdistinctstrengthsandlimitations:BRDprovides
globalcoverageatrelativelylowaccuracy,HASdeliversglobalcor-
rectionsbutexhibitsdegradedperformanceintheAsia–Pacific,and
Ephemerides, Galileo HAS,
PPP-B2bachieveshighaccuracybutisconfinedtoaregionalservice
centered on China. These complementary characteristics motivate
and BDS-3 PPP-B2b their integration to achieve both high precision and robust global
performance.UsingtheLuTan-1Amissionasacasestudy,weassess
thequalityandavailabilityofHASandPPP-B2bproductsandpropose
a real-time KOD method that integrates BRD, HAS and PPP-B2b.
Carrier-phasepseudoambiguitiesaremodeledasrandomwalks,with
noise parameters determined for each ephemeris source through a
parametricsearchexperiment.Resultsshowthatthe3-Dorbiterror
DINGYILIU decreases from 25.06 cm for the combination of GPS and BDS-3
ChineseAcademyofSciences,Beijing,China BRDto18.86cmwhenHASisincorporatedandfurtherto17.09cm
UniversityofChineseAcademyofSciences,Beijing,China withtheadditionofPPP-B2b.Especially,intheAsia–Pacificregion,
adding PPP-B2b to BRD+HAS reduces the orbit error from 20.57
HAOBOLI
to 16.63 cm. Overall, these findings demonstrate the stability and
RMITUniversity,Melbourne,VIC,Australia
adaptabilityoftheproposedintegratedmethodundercurrentGlobal
JINGLEIZHANG NavigationSatelliteSystemconfigurations,providingapracticalpath-
ChineseAcademyofSciences,Beijing,China waytohigherprecisionreal-timeorbitdeterminationforfutureLEO
missions.
XIAOMINGWANG
ChineseAcademyofSciences,Beijing,China
UniversityofChineseAcademyofSciences,Beijing,China I. INTRODUCTION
SHUXU Nowadays, the demand for real-time high-precision
ChineseAcademyofSciences,Beijing,China orbit information has risen rapidly with the expanding
use of large low Earth orbit (LEO) satellite constellations
SUELYNNCHOY
RMITUniversity,Melbourne,VIC,Australia for applications like real-time Earth observation [1], [2],
[3], navigation augmentation [4], [5], [6], and formation
YINGXU flying [7], [8], [9]. Among these emerging approaches,
ZHELI reduced-dynamic orbit determination (ROD), which com-
ChineseAcademyofSciences,Beijing,China
bines the advantages of kinematic positioning with those
UniversityofChineseAcademyofSciences,Beijing,China
offullydynamictrajectorymodeling,hasbeenwidelyrec-
ognized as apromising method forreal-timeapplications.
Received5October2025;revised7January2026;accepted16February Reichert et al. [10] provided one of the earliest onboard
2026.Dateofpublication23February2026;dateofcurrentversion20 demonstrationsontheSatélitedeAplicacionesCientíficas-
April2026. C(SAC-C)mission,yieldinga3-Dorbitaccuracyof∼1.5m
DOI.No.10.1109/TAES.2026.3666831 using dual-frequency GPS pseudorange observations and
broadcast ephemerides (BRD). Montenbruck and Ramos-
RefereeingofthiscontributionwashandledbyR.Armellin.
Bosch[11]subsequentlyimprovedthereal-timeaccuracyto
ThisworkwassupportedbytheNationalNaturalScienceFoundationof
lessthan1mbyincorporatingcarrier-phasemeasurements
ChinaunderGrant42474015.
intoROD.Morerecently,HauschildandMontenbruck[12]
Authors’ addresses: Dingyi Liu, Xiaoming Wang, Ying Xu, and have shown that decimeter-level accuracy is attainable
Zhe Li are with the Aerospace Information Research Institute, Chi-
by integrating multi-Global Navigation Satellite System
nese Academy of Sciences, Beijing 100094, China, and also with
(GNSS)observations(GPS,Galileo,andBDS)toenhance
the School of Electronic, Electrical and Communication Engineer-
ing, University of Chinese Academy of Sciences, Beijing 101408, measurementgeometry.InadditiontotheuseofBRDinthe
China, E-mail: (liudingyi21@mails.ucas.ac.cn; wxm@aoe.ac.cn; xuy- aforementionedstudies,severalrecentworkshaveexplored
ing@aircas.ac.cn; lizhe22@mails.ucas.ac.cn); Haobo Li and Suelynn real-timeRODwiththeInternationalGNSSService(IGS)
ChoyarewithRMITUniversity,Melbourne,VIC3001,Australia,E-mail:
real-timeservice(RTS),indicatingthattheaccuracycanbe
(haobo.li@rmit.edu.au; suelynn.choy@rmit.edu.au); Jinglei Zhang and
furtherimprovedtocentimeterlevel[13],[14],[15].
Shu Xu are with the Aerospace Information Research Institute, Chi-
nese Academy of Sciences, Beijing 100094, China, E-mail: (zhangjin- Despiteitshighaccuracy,therelianceofRODoncom-
glei@aircas.ac.cn;xushu@aircas.ac.cn).(Correspondingauthor:Xiaom- plexdynamicalmodelsimposessubstantialcomputational
ingWang.) load, making real-time high-rate (e.g., 1 Hz) LEO imple-
mentations particularly challenging [16], [17], [18]. This
0018-9251©2026IEEE limitation was demonstrated in the autonomous precise
6788 IEEETRANSACTIONSONAEROSPACEANDELECTRONICSYSTEMS VOL.62 2026
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 2 -->

navigationexperimentonthePROBA-2spacecraft,where nanosatellites support only limited multi-GNSS tracking
eachRODintegrationsteprequiredupto21sofexecution duetoconstraintsincost,power,andhardwaredesign.This
timeonanARM7-classonboardprocessor,therebymaking furtherunderscorestheneedforanintegratedapproachto
real-time operation impractical for platforms with limited maximizesatelliteavailabilityandmaintainreliableperfor-
computational resources [17]. To address this, kinematic manceunderpracticalconditions.
orbit determination (KOD) has emerged as an alternative. Motivated by these opportunities and challenges, this
Compared with ROD, KOD is a geometric approach that study develops a real-time KOD method that integrates
estimates satellite positions directly from GNSS obser- HAS and PPP-B2b with BRD and validates its real-time
vations without the need to rely on dynamical models, orbit performance using the LuTan-1A (LT-1A) satellite.
supportingonboardreal-timesolutionsathighersampling The main contributions can be summarized from three
rates[19],[20],[21].Furthermore,sinceKODisinherently aspects.First,weassessthequalityandavailabilityofBRD,
independent of dynamical force modeling, it offers addi- HAS,andPPP-B2bproductsandfurthervalidatethemul-
tional benefits for real-time applications such as gravity ticonstellationperformanceofHASandPPP-B2bthrough
field recovery, atmospheric density estimation, and orbit ground-basedexperimentsusingIGSstationstoestablisha
maneuverdetection[22],[23],[24]. performance baseline. Second, with the use of a paramet-
Earlyapplicationsofreal-timeKODweremainlylim- ric search method, we calibrate ephemeris-specific pseu-
ited by the meter-level accuracy of BRD and single- doambiguity random-walk noise. Based on these optimal
constellation(GPS-only)receivers,resultinginorbitaccu- settings, we implement and evaluate a dual-constellation
racies of several meters [25], significantly worse than the real-time KOD solution under a BRD-only regime. Third,
decimeter-levelaccuracyachievedbyreal-timeROD[26], we propose a robust ephemeris integration strategy that
[27], [28]. However, recent studies have shown that real- dynamically combines BRD, HAS, and PPP-B2, which is
timeKODusingBRDcanachieveabout0.7m[21],bene- validated through global and regional orbit determination
fitingfromimprovementsinBRD[29]andthewidespread experiments, demonstrating significant improvements in
adoptionofsignal-in-spacerangeerror(SISRE)parameter- accuracy and robustness, particularly in the Asia–Pacific
ization or pseudoambiguity random-walk modeling [30], region.
[31]. Further experiments have indicated that real-time
KOD can even achieve centimeter-level accuracy when II. DATAANDMETHODOLOGIES
precise orbit and clock corrections from the IGS RTS are
A. GNSSandLEOData
used [18], [32]. Although LEO satellites cannot generally
In this study, BRD together with HAS and PPP-B2b
receiveRTScorrectionsdirectly,theoperationalavailability
corrections for day of year (DOY) 103–111, 2025 were
oftheGalileoHighAccuracyService(HAS)andtheBDS-3
collected using in-house GNSS receivers and archived
PrecisePointPositioning-B2b(PPP-B2b)nowenableson-
in ASCII format for subsequent analysis. DOY 105 was
boardreceiverstoobtaincorrections[33],[34],[35],open-
excluded because the LT-1A satellite performed attitude
ing new opportunities for high-precision real-time orbit
maneuvers. To evaluate the quality of these products, the
determination.TheaccuracyofHASandPPP-B2bproducts
multi-GNSSfinalpreciseephemeridesfromtheCenterfor
hasbeenexaminedinseveralstudies,andtheirpositioning
OrbitDeterminationinEurope(CODE)wereadoptedasthe
performance is well validated [36], [37], [38]. In broad
reference.GNSSobservationsfromthereceiversaboardLT-
terms,kinematicpositioningaccuracyofabout20cmcan
1Awereadoptedtoinvestigatetheproposedreal-timeKOD
be achieved globally with HAS and 18–22 cm regionally
fusionstrategythatintegratesHASandPPP-B2bwithBRD.
in China with PPP-B2b [39], [40], [41], suggesting that
LT-1A,launchedon26January2022,isanL-bandsynthetic
comparableaccuracymayberealizedforLEOorbitsusing
apertureradarsatellitedesignedforgeologicalmonitoring,
these services. Another study using Sentinel-6A GNSS
landslidedetection,andearthquakeassessment.Itoperates
observationsreportedreal-timeLEOorbiterrorsof7–9cm
inasun-synchronousorbitataround600-kmaltitudewith
withHAScorrections[42],whileBDS-3PPP-B2breduced
◦
an inclination of 97.4 . The dual-constellation receiver
theerrorsfromroughly27to19cm,withnotablegainsover
tracksGPSL1C/AandL2P(Y),BDSB1IandB3Ifromall
the Asia–Pacific region [43]. However, these studies have
nongeostationary Earth orbit BDS-2/3 satellites, and B1C
primarilyemployedtheRODmethod,and,todate,thereare
and B2a from BDS-3, which enables the evaluation of its
no reported demonstrations of real-time KOD using HAS
autonomousnavigationandpositioningperformance[28].
orPPP-B2b.Itis,therefore,urgenttoinvestigateKODwith
theseservices,individuallyorincombination.
B. Real-TimeKODMethodology
While BRD ensure global availability, their accuracy
islimited.HASprovidesglobalcorrections,butitsperfor- The real-time KOD algorithm uses pseudorange and
mance degrades in parts of the Asia–Pacific region, and carrier-phase measurements from GNSS satellites tracked
PPP-B2b delivers high-accuracy corrections but only for by the onboard receiver. Here, we adopt the ionosphere-
China and its surrounding areas. These complementary free (IF) combination. The estimated parameters are the
characteristics make their integration essential to guaran- satellite orbital positions, the receiver clock offset, and
tee both accuracy and robustness in real-time KOD for thecarrier-phaseambiguities.Theobservationequationsfor
LEO missions. Moreover, many GNSS receivers onboard the pseudorange Ps and carrier-phase Ls observations
r,IF r,IF
LIUETAL.:REAL-TIMEKODFORLEOBYINTEGRATINGBRD,GALILEOHAS,ANDBDS-3PPP-B2B 6789
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 3 -->

areasfollows[32]: and phase center variation (PCV) [33], [45]. Then, orbit
(cid:2) (cid:3)
Ps =ρs+c δt −δts +BIF −Bs,IF+εs (1) differences with respect to the reference are computed in
r,IF r (cid:2) r (cid:3) r,P P r,PIF ECEF (r
ECEF
) and transformed to RAC (r
rac
) components
L r s ,IF =ρ r s+c δt r −δts +B r I , F L −B L s,IF+N r s ,IF λ IF +ε r s ,LIF using
(2)
r =Rr =[e e e ]T r . (8)
where ρs is the geometric distance between the LEO re- rac ECEF r a c ECEF
r
ceiverantennaphasecenter(APC)andtheGNSSsatellite 2)SatelliteClockOffset: Ingeneral,HASandCODE
APC;cisthespeedoflight;δt andδtsarethereceiverand clock offsets are derived using dual-frequency IF combi-
r
GNSS satellite clock offsets, respectively; BIF and Bs,IF nations,whilePPP-B2bemploysthesingle-frequencyB3I
r,P P
representthepseudorangehardwaredelaysofthereceiver signal for BDS-3. Specifically, CODE adopts L1W/L2W
andGNSSsatellite,respectively,whileBIF andBs,IF refer for GPS and B2I/B3I for BDS-3, whereas HAS uses
r,L L
totheirrespectivecarrier-phasehardwaredelays;Ns isthe L1C/L2P [39]. To ensure consistency and comparability,
r,IF
integercarrier-phaseambiguity;λ isthewavelengthofthe code bias corrections are applied to unify the frequency
IF
IF combination; and εs and εs denote the unmodeled referencesbeforeevaluatingclockdeviations[33],[46].In
r,PIF r,LIF
errors in the pseudorange and carrier-phase observations, addition, system-dependent biases may exist given their
respectively. different reference standards. To eliminate interproduct
In real-time operations, GNSS satellite position and time scale discrepancies, a double-difference approach is
clock offset are derived from BRD or from real-time adoptedas
ephemeridesprovidedbyHASandPPP-B2b.Thecorrected
(cid:8)N
GNSSsatellitepositionsarecomputedas 1
∇(cid:6)Cj =(cid:6)Cj − (cid:6)Cj (9)
r HAS/B2b =r BRDM +RT·δr rac (3) i i N j=1 i
R
⎧
=[e
r
e
a
e
c
]T (4)
where (cid:6)Cj is the difference between the evaluated and
i
⎪ ⎪ ⎨ e r = |r rB
B
R
R
D
D
M
M
| referenceclockoffsetsforsatellite jatepochi,andNisthe
e =r ×r˙ (5) numberofsatellitesfromthesystem.
⎪ ⎪ c BRDM BRDM 3)SISRE: SISREoffersaunifiedmeasureofthecom-
⎩
e a =e r ×e c binedeffectsoforbitandclockoffsetsonuserpositioning
andisakeyindicatorofephemerisquality[47].Theorbit-
wherer HAS/B2b isthesatellitepositionvectorcorrectedus-
onlyandtotalSISREarecomputedas
ingHASandPPP-B2b;r andr˙ arethesatellitepo-
BRDM BRDM (cid:9)
sitionandvelocitycomputedfromBRD,respectively.Note
(cid:6)A2+(cid:6)C2
E th a a r t th r H -fi A x S/ e B d 2b (E a C nd E r F B ) R f D ra M m a e r . e δ e r xpr i e s s t s h e e d o i r n bi t t h c e o E rr a e r c th ti - o c n en ve te c r t e o d r SISRE orbit = (α(cid:6)R)2+ β (10)
rac (cid:9)
intheradial,along-track,andcross-track(RAC)directions
(cid:6)A2+(cid:6)C2
providedbyHASandPPP-B2b,andRistherotationmatrix SISRE = (α(cid:6)R−c(cid:6)T)2+ (11)
total β
from ECEF to RAC, formed by the unit vectors e , e ,
r a
and e . The GNSS satellite clock offsets are computed as
c where (cid:6)R, (cid:6)A, and (cid:6)C are the orbit errors in the radial,
follows[44]:
along-track, and cross-track directions, respectively, (cid:6)T
δts =δts + δC H s AS (6) is the clock offset, and α and β are the weighting factors
HAS BRDM c followingconstellation-andorbit-type-specificvalues(e.g.,
δCs
GPS:0.98and49;BDS-3mediumEarthorbit(MEO):0.98
δts =δts − B2b (7)
B2b BRDM c and54;andBDS-3inclinedgeosynchronousorbit(IGSO):
whereδts ,δts ,andδts arethesatelliteclockoffsets 0.99and126)[48].
HAS B2b BRDM
(second)correctedbyHAS,PPP-B2b,andcomputedfrom
BRD, respectively, and δCs and δCs are the corre- D. IntegratedEphemerisMethod
HAS B2b
spondingclockcorrections(meter)decodedfromHASand Given the substantial differences in accuracy, spatial
PPP-B2b,respectively. coverage, and service availability among BRD, HAS, and
PPP-B2b, as analyzed in Section III, their contributions
C. EvaluationMetricsforEphemerides
to real-time KOD are inherently heterogeneous. In par-
To assess the accuracy of BRD, HAS, and PPP-B2b ticular, the availability and quality of each product vary
products, we focus on three key metrics of satellite orbit, acrossregionsandovertime,whichmakesafixedorstatic
satelliteclockoffset,andSISRE. integration strategy suboptimal for real-time applications.
1)SatelliteOrbit: Theevaluatedorbitsarereferenced Toaddressthischallenge,weproposeanadaptiveintegra-
totheAPCofeachsatellite,whereastheCODEreference tion method for real-time KOD that dynamically selects
orbits are given at the satellite center of mass (COM). To andintegratesorbitcorrectionsaccordingtotheprevailing
ensureconsistency,weconverttheCOM-referencedorbits serviceconditions,therebybalancingaccuracy,robustness,
toAPCbyapplyingthesatellitephasecenteroffset(PCO) andcontinuity.
6790 IEEETRANSACTIONSONAEROSPACEANDELECTRONICSYSTEMS VOL.62 2026
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 4 -->

Fig.1. Globalsubsatellitegroundtrackscoloredbyorbit-onlySISRE
onDOY111,2025.(a)HAS-GPS.(b)PPP-B2bBDS.
Fig.2. Global1◦×1◦daily-meannumberofvisiblesatellites(elevation
≥7◦)onDOY111,2025.(a)HAS-GPS.(b)PPP-B2bBDS-3.
Todeterminetheoptimalintegrationlogic,wefirstana-
Fig.3. SchematicoftheproposedCCESmethod.
lyzethecharacteristicsofthecorrectionsforHAS-GPSand
PPP-B2b BDS-3 satellites. Fig. 1 presents the subsatellite
groundtracksforHAS-GPSandPPP-B2bBDS-3onDOY
Thereal-timedataharmonizationmainlyaimstoensure
111,2025,coloredbytheirorbit-onlySISRE.Attheglobal
the alignment of asynchronous navigation messages and
scale, the ephemeris accuracy does not show an obvious
correction streams. A short buffer id employed to handle
regionalpattern.Thispossiblysuggeststhatproviderstend latencyandoccasionaldropouts.Timetags((cid:6)t )from
SYS-GPS
to suspend broadcasting corrections when their internally
different systems (t ) are converted to GPS time (t ),
SYS GPS
assessedqualitydegrades.Consequently,region-dependent
andforeachsatellite(s),themostrecentrecordsatisfying
weightingofephemerissourcesisdeemedunnecessaryin
the latency constrain (t ) is selected, whose time tag is
k
thisstudy. Inaddition, Fig.2showsthenumberofvisible denoted as (ts (k)) while the correction age ((cid:6)ts(k)) is
satellites (elevation-cutoff angle ≥7 ◦) for HAS-GPS and eph
tracked
PPP-B2bBDS-3,computedwithineachglobal1 ◦×1 ◦ grid
cell. It can be found that the number of visible satellites
t =t +(cid:6)t (12)
showsconsiderablespatialvariabilityworldwide,suggest- GPS SYS SYS-GPS
ingthattheperformanceofcorrection-basedKODmaybe ts (k)=max{t ≤t } (13)
eph k
degradedinregionswithlimitedsatellitevisibility.There-
fore, the integration strategy should be driven by satellite (cid:6)ts(k)=t −ts (k). (14)
k eph
availabilityratherthanaccuracyweighting.
In real-time KOD without dynamic constraints, the
The constellation mode selection then determines the op-
position is initialized by single point positioning and es-
timal ephemeris source based on availability. For each
timated independently at each epoch under a white-noise satellite (s) at epoch (k), validity screening (vs(k)) is per-
assumption. Under the framework, the mixing usage of
formedbasedonissueofdata,ephemeris(IODE)matching,
different orbit products within a single constellation (e.g.,
timeout,andcontinuitychecks,assummarizedbyabinary
integrating corrected and broadcast ephemerides) leads to
indicator
internal inconsistencies. Such inconsistencies cannot be
fully eliminated by tuning pseudoambiguity random-walk
vs(k)=Is(k)·Ts(k)·Cs(k)∈{0,1} (15)
noise or observation weighting, and they ultimately man-
ifest as residual biases and degraded orbit accuracy [53].
whereIs(k)istheIODEmatchingoutcome.Ts(k)andCs(k)
Toaddressthisissue,weproposeaconstellation-consistent
are the timeout decision and the continuity compliance,
ephemeris selection (CCES) method. As shown in Fig. 3,
respectively.Thenumberofsatelliteswithvalidcorrections
CCESenforcesauniformephemerissourceforallsatellites
(N (k))inconstellation(S )isthencalculatedasfollows:
within each constellation at each epoch to ensure internal sys sys
consistency,andcomprisesthreeprocesses:real-timedata (cid:8)
harmonization, constellation mode selection, and constel- N (k)= vs(k). (16)
sys
lationmodemanagement. s∈Ssys
LIUETAL.:REAL-TIMEKODFORLEOBYINTEGRATINGBRD,GALILEOHAS,ANDBDS-3PPP-B2B 6791
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 5 -->

Fig.5. Global1◦×1◦daily-meanPDOPforHAS-GPSandPPP-B2b
Fig.4. DailyaverageavailabilityofHAS-GPS(blue),PPP-B2bBDS-3 BDS-3onDOY111,2025.(a)HAS-GPS.(b)PPP-B2bBDS-3.
MEO(red),andPPP-B2bBDS-3IGSO(green)overtheentirestudy
period.
mean of 78.4%, consistent with ∼80% reported previ-
The method then selects the constellation-level ephemeris ously [39], [42]. For PPP-B2b BDS-3, the availability of
sourcemode(m (k))usingasingle-thresholdrule MEOsatellites(green)andIGSOsatellites(red)isapprox-
sys
⎧ imately30%and72.2%,respectively,consistentwithprior
⎨ Mode-C N (k)≥N studies[39],[46].Thislimitedavailabilityresultsfromthe
sys 0
m (k)= (17) fact that PPP-B2b is a regional service, restricted to parts
sys ⎩
Mode-B N (k)<N oftheAsia–PacificregioncenteredonChina.
sys 0
Fig.5showsthepositiondilutionofprecision(PDOP)
whereMode-Cisthecorrected-ephemerismodeandMode- ona1 ◦×1 ◦gridforHAS-GPSandPPP-B2bBDS-3onDOY
B is the BRD mode. N is set to 4 here to ensure that 111, 2025, further revealing the availability of HAS-GPS
0
an instantaneous position solution is obtainable using ex- and PPP-B2b BDS-3 in different regions. The computed
clusively corrected ephemerides, thereby prioritizing the global mean PDOP for HAS-GPS is 3.33, with 87.1% of
higher accuracy mode whenever availability permits. As grids having PDOP ≤ 4 and 96.8% having PDOP ≤ 6.
the focus of this study is on the gains from augmenting Although this coverage and geometry generally indicate
BRD with HAS and PPP-B2b, we do not further tune the that four or more GPS satellites are usable for navigation
thresholdhere. worldwide, prior studies and official HAS documentation
Theconstellationmodemanagementprovidesstability havenotedthatitsservicequalityisnotguaranteedinAsia
during ephemeris source transitions. The method main- andadjacentregions[33],[49].TheresultsinFig.5(a)also
tainstheconstellation-levelmodestateand,upondetecting reveal that the mean PDOP is around 2.20 across Europe,
a mode transition, temporarily inflates the random-walk Africa, and the eastern Atlantic (30 ◦W–60 ◦E; 35 ◦S–70 ◦
process noise of the pseudoambiguity states. This mech- N), whereas it degrades to 4.54 in parts of the Asia–
anism allows one to rapidly absorb transient inconsisten- Pacificregion,markedbythewhiterectangle(70 ◦E–170 ◦E;
cies caused by the ephemeris-source switch, ensuring the 10 ◦S–80 ◦N). These results indicate that HAS-GPS is ade-
stabilityofthecontinuousKODsolution. quate for most regions, whereas the Asia–Pacific remains
relatively weak and would benefit from augmentation to
III. COMPARISONANDEVALUATIONOF support robust real-time KOD. As shown in Fig. 5(b),
EPHEMERIDES compared with HAS-GPS, PPP-B2b service coverage is
regionallyconfined,mainlycenteredonChinaanditssur-
Using the CODE Multi-GNSS Experiment final
roundings.WithinthecorrespondingAsia–Pacificdomain
ephemeridesasthereference,weassessthedaily-averaged
(white dashed rectangle), the mean PDOP for PPP-B2b
availability and accuracy of the BRD, and the corrections
BDS-3 is 2.89, indicating a significant improvement in
fromHASandPPP-B2b.AlthoughbothHASandPPP-B2b
geometry for this region compared to HAS-GPS. In other
provideGPScorrections,onlytheHAS-GPSareevaluated
regions,thePDOPiseitherverylarge(e.g.,inAfrica)orno
andusedinthesubsequentexperimentsbecauseHASoffers
satellitesareavailable(e.g.,inSouthAmerica).Therefore,
global coverage, whereas PPP-B2b GPS corrections are
despiteitsregionalnature,PPP-B2bBDS-3providesvalu-
regional and show limited global availability [39], [44].
ableaugmentationinpartsoftheAsia–Pacificregion,par-
Moreover, HAS Galileo corrections are neither evaluated
ticularlyinChinaandsurroundingareas,whereHAS-GPS
norusedfororbitdeterminationbecausetheGNSSreceiver
performance is relatively poor, thereby supporting more
onboardLT-1AtracksonlyGPSandBDSobservations.
robustandaccuratereal-timeorbitdeterminationforLEO
satellites.
A. AvailabilityofHASandPPP-B2bSatellites
The daily-average availability of HAS-GPS and PPP-
B. AnalysisoftheAccuracyofSatelliteEphemerides
B2b BDS-3 (i.e., PPP-B2b corrections for BDS-3) over
the entire study period is illustrated in Fig. 4. For HAS- The performance of HAS and PPP-B2b corrections
GPS satellites (blue), the availability of most satellites was assessed in terms of orbit accuracy and clock-offset
exceeds 75%, with the lowest at 67.7%, and an overall stabilitywithdailystatisticsforthreerepresentativemetrics
6792 IEEETRANSACTIONSONAEROSPACEANDELECTRONICSYSTEMS VOL.62 2026
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 6 -->

TABLEI
AverageAccuracyofOrbit,ClockOffset,andSISREErrorsforGPSandBDS-3(Ratio=(1−HASorB2b/BRD)×100%)
theirspecificservicedesignsandorbitalcharacteristics,in
termsofClock(STD),SISRE(Orbit),andSISRE(debiased).
First,regardingclockstability,PPP-B2bMEOachievesthe
lowest Clock (STD), followed by PPP-B2b IGSO, while
HAS-GPS performs relatively worse. This performance
gapismainlyattributabletothecorrectionupdateinterval.
Forexample,PPP-B2bprovideshigh-rateclockcorrections
every 6 s [51], which effectively suppresses short-term
clock jitters. In contrast, the HAS clock update interval is
10 s [42]. Consequently, despite the global tracking capa-
bility of HAS, the higher update rate of PPP-B2b confers
a significant advantage in capturing high-frequency clock
Fig.6. Dailyaccuracyoforbit,clockoffset,andSISREforGPSand variations, resulting in superior stability for BDS-3 MEO
BDS-3(MEO/IGSO)beforeandafterapplyingHAS/PPP-B2b. andIGSOsatellites.
Conversely,fortheorbit-relatedcomponent,i.e.,SISRE
presented in Fig. 6. First, clock offset stability is evalu- (Orbit), HAS-GPS demonstrates superior accuracy com-
ated using the standard deviation (STD) of clock offset paredtoPPP-B2b.Thisismainlydeterminedbythetracking
residuals, denoted Clock (STD). SISRE is assessed using network geometry. To be specific, HAS corrections are
two metrics: 1) an orbit-only SISRE root mean square generated from a globally distributed Galileo Sensor Sta-
(RMS), denoted SISRE (Orbit); and 2) a debiased total tionnetwork,whichensuresconsistentglobalobservability
SISRE,denotedSISRE(debiased),computedbyremoving and robust orbit determination. PPP-B2b, however, relies
theconstant satellite-dependent clockbiasbeforeforming on a regional tracking network. While dense locally, this
thestatistics[33],[42],[50].Notethat,inthefollowingfig- regionalgeometrylimitstheseparationofalong-trackand
uresandtables,B2bareusedtodenotePPP-B2bcorrections cross-track errors and makes the solution susceptible to
forsimplicity. constellation-levelreferenceframerotationerrors,thereby
To interpret the results in Fig. 6, Table I outlines the inflatingtheglobalorbiterror[37],[38],[39].
overall precision of the Clock (STD), SISRE (Orbit), and Furthermore,withintheBDS-3constellation,PPP-B2b
SISRE(debiased)andillustratestherelativeimprovements IGSO consistently underperforms MEO in orbit-related
over BRD. For GPS, HAS delivers significant enhance- metrics. Unlike the rapidly moving MEO satellites, IGSO
ments across all metrics, with improvements of 67.1%, satellites remain relatively stationary with respect to the
75.6%, and 59.7% in Clock (STD), SISRE (Orbit), and regionalgroundnetwork,leadingtoweakergeometricvari-
SISRE(debiased),respectively,relativetoBRD.ForBDS- ationandpoorerobservability.Inaddition,IGSOsatellites
3,PPP-B2bachievessubstantialbenefits:forMEO,Clock are more sensitive to solar radiation pressure modeling
(STD)improvesby76.9%andSISRE(debiased)by60.1%; deficiencies due to their high altitude [52]. These larger
for IGSO, the corresponding gains are 72.3% and 48.4%. orbit errors propagate into the SISRE (debiased) metric,
Only SISRE (Orbit) for IGSO shows a slight decrease. makingitthehighestamongthecomparedgroupsforIGSO.
Theseimprovementsareprimarilyattributabletothemore Incontrast,PPP-B2bMEObenefitsfromitsexceptionally
accurateclockcorrectionsprovidedbyPPP-B2b. stableclockstomitigateitsmoderateorbiterrors,ultimately
Beyond the overall improvements, Fig. 6 and Table I achievingthebestSISRE(debiased)performance.
alsorevealdistinctperformancedifferencesbetweenHAS- Tobetterhighlighttheorbitimprovements,TableIalso
GPS and PPP-B2b BDS-3, which are mainly driven by reports the radial, along-track, and cross-track orbit RMS
LIUETAL.:REAL-TIMEKODFORLEOBYINTEGRATINGBRD,GALILEOHAS,ANDBDS-3PPP-B2B 6793
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 7 -->

TABLEII
ProcessingConfigurationforReal-TimeStaticPPP
Fig.7. GeographicdistributionoftheselectedIGSstations.
andtheirpercentagechanges(ratio)incomparisontoBRD.
For GPS, the use of HAS reduces the RMS by 66.4%
(radial),88.5%(along-track),and84.6%(cross-track).For
BDS-3 MEO, the use of PPP-B2b decreases the RMS by
9.2% (radial) and 4.5% (along-track), but increases it by
23.6%(cross-track).ForBDS-3IGSO,althoughtheradial
RMS decreases by 2.2%, the along-track and cross-track
RMS increase by 17.4% and 26.9%, respectively. These
results also echo findings from prior studies [29], [38],
TABLEIII
[47],[53].
AverageReal-TimePositioningAccuracyandAvailability
In summary, HAS-GPS and PPP-B2b BDS-3 substan-
tially enhance real-time orbit and clock performance, and
thedebiasedSISREfurtherindicatesthatthesecorrections
effectivelymitigatesystematicclockbiases,leadingtosig-
nificantgainsoverBRD.
C. EvaluationofGround-StationPositioning
Performance
Given that tri-constellation GNSS receivers
(GPS+Galileo+BDS-3) are not yet standard on LEO
platforms, we utilized data from 15 globally distributed
IGSstationstoassessthemulticonstellationperformanceof
HASandPPP-B2b,asillustratedinFig.7.Theexperiment
spans DOY 103–111, 2025, using stations that support
GPS, Galileo, and BDS-3 observations. Furthermore, the
processingconfigurationsaresummarizedinTableII.Note
that,inthereal-timestaticPPPprocessing,twointegration
strategiesweredesigned:1)Strategy1usesHASforGPS
and Galileo, and PPP-B2b for BDS-3; and 2) Strategy 2
usesPPP-B2bforGPSandBDS-3,andHASforGalileo.
Toevaluatethepositioningperformance,thedailypost-
convergencepositioningRMSwascomputedforeachsta-
tion.Convergenceisdefinedastheepochwhenhorizontal
and vertical positioning errors remain within 10 cm for at
least20consecutiveminutes.Referencestationcoordinates
were derived from the IGS Satellite and Instrument Ex-
change Format files. Table III categorizes the stations in
Fig.4intotwosubsetsbasedonwhetherStrategy1orStrat-
egy2yieldsasmaller3-DpositioningRMS.Itsummarizes These stations are typically located within or near the
both positioning accuracy and solution availability, which PPP-B2bserviceregion,wheretheavailabilityofPPP-B2b
isdefinedasthepercentageofepochswithavalidsolution. correctionsforGPSandBDS-3ensuresarobustmulticon-
As shown in Table III, distinct performance patterns stellation geometry. In contrast, for stations where Strat-
emerge. For stations where Strategy 2 outperforms Strat- egy 1 proves superior, most stations are located outside
egy 1, the solution availability consistently exceeds 97%. theeffectivePPP-B2bcoveragearea.Intheseregions,the
6794 IEEETRANSACTIONSONAEROSPACEANDELECTRONICSYSTEMS VOL.62 2026
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 8 -->

numberofPPP-B2b-correctedsatellitesdropssignificantly,
even to zero. Hence, Strategy 2 is, therefore, dominated
by HAS Galileo, resulting in larger 3-D RMS values and
reducedavailabilityinmostcases(e.g.,atstationCUIB).
In terms of positioning accuracy, when the PPP-B2b
service is available, the integrated solution delivers high
precision. For example, at station WUH2, the 3-D RMS
for PPP-B2b-only and HAS-only are 3.12 and 4.92 cm,
respectively.Bycomparison,Strategy1achieves2.62cm,
while Strategy 2 improves further to 2.09 cm. This repre-
sents an improvement of 33.0% over PPP-B2b-only and
57.5% over HAS-only for Strategy 2. However, outside
thePPP-B2bserviceregion,theperformanceofStrategy2
degradesmarkedly.Atmanystations,the3-DRMSexceeds
3.4cm.Forexample,atstationZAMB,thePPP-B2b-only
Fig.8. Dailymeanshareofepochswithexactlyk(=k)andatleast
solution yields a poor 3-D RMS of 6.49 cm with only
k(≥k)correctedsatellitesforHAS-GPSandPPP-B2bBDS-3overthe
20.9%availability,whereastheHAS-onlysolutionachieves
entirestudyperiod.
2.48cmwith96.4%availability.TheintegratedStrategy1,
which relies on HAS for GPS/Galileo, maintains a high
accuracyof2.38cm(96.4%availability).Incontrast,Strat-
egy 2 degrades to 3.22 cm (94.8% availability) as it relies
onthesparsePPP-B2bGPScorrections.
Overall,thisground-basedexperimentconfirmstheben-
efits of exploiting the complementary multiconstellation
capabilitiesofHASandPPP-B2b.Italsoindicatesthatany
uncriticalintegrationisnotagoodpractice,astheselected
strategymustaccountfortheregionalcoveragelimitations
ofPPP-B2btoensureoptimalglobalperformance.
IV. REAL-TIMEKODSTRATEGY
Building on the preceding ephemeris evaluation, this
sectionintroducesthereal-timeKODstrategy,includingthe
ephemeris configurations and the associated measurement
Fig.9. NumberofGPSandBDS-3satellitestrackedbyLT-1Awithand
processingforreal-timeoperation.
withoutHAS/PPP-B2bcorrectionsonDOY104,2025.(a)GPS+BDS-3.
(b)BDS-3.(c)GPS.
A. EphemerisIntegrationStrategiesforReal-TimeKOD
a clear orbital periodicity: the count increases when LT-
To support global high-accuracy, real-time KOD for 1A passes over the Asia–Pacific region, whereas for large
LEOsatellites,weintegrateBRDwithprecisecorrections portions of the day, only a few BDS-3 satellites carry
fromHASandPPP-B2b.Thenecessityofthisintegration PPP-B2bcorrections,andtheremainderrelyonbroadcast.
is motivated by the findings depicted in Fig. 8, which As indicated by Fig. 9(a) and the statistics above, despite
illustrates the daily-mean epochwise percentage of time theglobalcoverageofHAS,thenumberofHAS-corrected
with exactly k(=k) and at least k(≥k) corrected satellites GPS satellites is still fewer than four in roughly 10% of
observedbyLT-1A(GPSL1/L2;BDS-3B1C/B2a)overthe epochs.Bycontrast,Fig.9(c)showsthatintegratingBRD
entirestudyperiod.Notethat,here,kdenotesthenumberof withHAS-GPSandPPP-B2bBDS-3ensuresthatmorethan
satellitesforwhichcorrectionsareavailableinagivenepoch 99.9%ofepochsmeetthevisibilityrequirementofatleast
(86 400 per day). It can be found that the share of epochs fourusablesatellites.Accordingly,weadopttheintegration
withfoursatellitesis86.8%forHAS-GPS(74995epochs) ofHAS+PPP-B2bcorrectionswithBRDtomaintainorbit-
butonly23.8%forPPP-B2bBDS-3(20563epochs).When arccontinuityandenablerobustreal-timeKOD.Thethree
thetwosetsarecombined,91.2%(78796)ofepochsmeet strategiesadoptedinthisstudyarelistedasfollows:
thevisibilityrequirementofatleastfourcorrectedsatellites,
illustrating the rationale and advantages of integrating the 1) BRD-only:UseBRDforbothGPSandBDS-3.
twosetsofreal-timecorrections. 2) BRD+HAS:IntegrateHASwithBRDforGPS,while
Fig.9illustratesthesatellite-counttimeseriesonDOY usingBRDforBDS-3.
104, 2025, comparing the sets corrected by HAS (GPS) 3) BRD+HAS+B2b:CombineHAS-GPSandPPP-B2b
andPPP-B2b(BDS-3)withthoseavailablefromBRD.In BDS-3,withfallbacktoBRDforsatellitesnotcov-
Fig. 9(b), the PPP-B2b-corrected satellite count exhibits eredbytheRTSs.
LIUETAL.:REAL-TIMEKODFORLEOBYINTEGRATINGBRD,GALILEOHAS,ANDBDS-3PPP-B2B 6795
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 9 -->

TABLEIV
ProcessingConfigurationandParameterSettingsforReal-TimeKOD
Fig.10. DailymeanaccuracyfortheLT-1Apostprocessedpreciseorbit
determinationovertheentirestudyperiod.
isgeneratedusinganin-housesoftwarepackage,utilizing
theCODEmulti-GNSSfinalpreciseephemeridesasinputs.
The processing strategy uses a simplified dynamic model
consistent with previous studies [55], [56]. To verify the
internal consistency and accuracy of the reference orbit,
a standard 6-h orbit overlap test was performed on the
selected datasets. As shown in Fig. 10, the mean RMS
errorsintheradial,along-track,andcross-trackdirections
are 0.52, 0.91, and 0.79 cm, respectively, yielding a 3-D
RMS of 1.40 cm. These results confirm that the reference
orbitachievescentimeter-levelaccuracy,whichissufficient
forvalidatingtheperformanceofreal-timeKOD.
V. REAL-TIMEKODEXPERIMENTSANDRESULTS
Inreal-timeKOD,pseudoambiguitiesareintroducedto
B. MeasurementProcessingforReal-TimeOperation absorb ephemeris-induced LOS errors, and the choice of
random-walk noise settings strongly affects orbit stability
Inthekinematicmodel,theorbitandclockparameters
and accuracy. Therefore, it is essential to optimize this
are modeled as white-noise processes and are, therefore,
parameterseparatelyforeachephemeristype(BRD,HAS,
estimatedindependentlyateachepoch.Theambiguitypa-
and PPP-B2b) and satellite system (GPS and BDS-3), as
rameters,usuallytreatedasaconstant,areinsteadmodeled
detailed in Section V-A. Using the optimal random-walk
as a random-walk process to absorb both carrier-phase
noise settings, LEO satellite orbits are then determined
ambiguitiesandslowlyvaryingephemeris-inducedline-of-
undertheBRD-onlyandcombinedstrategies(BRD+HAS
sight(LOS)errors[53],[54].Toensurestableandaccurate
and BRD+HAS+PPP-B2b). The benefits of the integrated
orbitdetermination,theoptimalrandom-walknoisesettings
approach are finally demonstrated through comparisons
reflecting the error characteristics of different ephemeris
againstpostprocessedLEOorbitresults.
sourcesaredeterminedthroughaparametricsearchexperi-
ment,withresultspresentedinSectionV.Forephemerisand
A. DeterminationoftheOptimalPseudoambiguity
clock computation, GPS uses legacy navigation message
Random-WalkNoise
(LNAV) together with HAS-corrected ephemerides, while
BDS-3 uses civil navigation message (CNAV) with PPP- BecausethequalityofGNSSorbitandclockproducts
B2b-correctedephemerides.Differentialcodebiascorrec- variesacrossproviders,theoptimalsettinglikewisediffers
tions are applied whenever the reference signals of the by product [42]. Therefore, we use agreement with the
clockproductsdifferfromthoseusedbytheLEOreceiver postprocessedLT-1Apreciseorbitsasthequalitymetricand
pseudorangemeasurements.Inaddition,theBDS-3antenna identifytheoptimumviaaparametricsearch.UsingBRD
PCO is adjusted (from B3I to the operational frequency) as an example, Fig. 11 shows that when the random-walk
to match the receiver antenna reference with that used in noise is set to zero, the baseline 3-D RMS orbit error for
the ephemerides. Other correction models and parameter GPSisroughlytwicethatforBDS-3.Bycontrast,BDS-3is
settingsfollowstandardpractice,withdetailssummarized moresensitivetoovertuningthanGPS,i.e.,oncethesetting
inTableIV. exceedstheoptimum,theaccuracydegradesmorerapidly,
Sincenoofficialpreciseorbitproductiscurrentlyavail- asalsodemonstratedin[30].
able for the LT-1A satellite, we use postprocessed precise Basedonthestatisticsfromthisparametricsearch,the
orbits as the reference for validation. The reference orbit optimal pseudoambiguity random-walk STD is identified
6796 IEEETRANSACTIONSONAEROSPACEANDELECTRONICSYSTEMS VOL.62 2026
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 10 -->

TABLEV
DeterminedOptimalPseudoambiguity
Random-WalkNoiseSettings
TABLEVI
MeanVisibilityandGeometryMetricsforBRD-Only
Fig.11. Average3-DorbitRMSforGPS-only(blue)andBDS-3-only Real-TimeKODOvertheEntireStudyPeriod
(red)versusthepseudoambiguityrandom-walknoisesettingsoverthe
entirestudyperiod.
TABLEVII
AveragedOrbitRMSandIntegrityfortheBRDBaselineOverthe
EntireStudyPeriod
B. BRD-OnlyResults
Fig.12. Dailymeanreal-timeorbitRMSbefore(left)andafter(right)
applyingtheoptimalpseudoambiguityrandom-walknoise.
BRD processing remains the prevailing method for
√ √ real-time orbit determination; hence, we first examine the
as 35cm/ s for GPS and 2cm/ s for BDS-3, which BRD-only baseline in detail. Combining GPS and BDS-3
deliverthebestorbit-determinationaccuracyunderthetest increases observation redundancy and strengthens the ge-
conditions.Toquantifytheimpactofthesesettings,Fig.12 ometry, thereby improving the accuracy of the combined
compares daily radial, along-track, and cross-track RMS KODsolution.AssummarizedinTableVI,theGPS+BDS-3
errors for GPS-only, BDS-3-only, and GPS+BDS-3 solu- solutionprovidesnear-continuouscoverage:epochswithat
tions, before and after applying the optimal random-walk least four satellites exceed 99.9%. On average, the com-
noisesettings. bined solution uses 14.51 satellites per epoch. Its mean
Fig.12showsthatapplyingtheoptimizedpseudoambi- PDOP value is 1.68, around 37.3% and 52.0% lower than
guityrandom-walknoisesettingsimprovesthedaily-mean GPS-onlyandBDS-3-only,respectively.
orbitaccuracyinallcomponents.Usingtheradialcompo- Buildingontheoptimalpseudoambiguityrandom-walk
nent as an example, for GPS, radial RMS decreases from noise settings established above and the preceding assess-
roughly 50–80 to 30–40 cm. For BDS-3, radial decreases ment of satellite visibility and geometry, we evaluate the
from30–40cmto20–30cm.ForthecombinedGPS+BDS-3 performance of real-time KOD under the GPS+BDS-3
solution,radialdecreasesfrom20–30to15–20cm.These BRD-only configuration. Table VII outlines the averaged
results clearly confirm that tuning the pseudoambiguity orbiterrors:thecombinedsolutionachievesa3-DRMSof
random-walknoisesignificantlyimprovesorbitdetermina- 25.06cm,incomparisonwith53.75cmforGPS-onlyand
tion performance, with the largest relative improvements 37.38cmforBDS-3-only,correspondingtoimprovements
forGPS-only. of 53.4% and 33.0%, respectively. Componentwise, the
Analogous to the BRD case, we perform a parametric dual-system RMS errors are 16.09 cm (radial), 14.82 cm
searchtodeterminetheoptimalpseudoambiguityrandom- (along-track),and11.97cm(cross-track),representingsub-
walk noise for both HAS-GPS and PPP-B2b BDS-3. To- stantial improvements over both single-system solutions.
getherwiththeBRD-basedsettings,theseresults(outlined The solution integrity (percentage of epochs with a valid
in Table V) define the random-walk noise configuration solutionperday)is99.7%forthecombinedsolution,com-
usedforthesubsequentexperiments. paredwith98.7%forGPS-onlyand97.4%forBDS-3-only.
LIUETAL.:REAL-TIMEKODFORLEOBYINTEGRATINGBRD,GALILEOHAS,ANDBDS-3PPP-B2B 6797
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 11 -->

TABLEVIII
AverageReal-TimeOrbitRMSforBRD-Only,BRD+HAS,andBRD+HAS+B2bOvertheEntireStudyPeriod
Fig.14. OrbitaccuracybeforeandafterapplyingtheHAS-GPSand
PPP-B2bBDS-3correctionsonDOY111,2025.
Fig.13. Dailymean3-DorbitRMSforBRD-only,BRD+HAS,and
BRD+HAS+B2bovertheentirestudyperiod.
Overall, the accuracy improvements and better integrity
highlighttherobustnessandeffectivenessofthecombined
solutionunderBRD.
C. Ephemeris-IntegrationResults
Building on the optimal pseudoambiguity random-
walk noise settings and the CCES method proposed in
Section II-D, we then evaluate real-time KOD under the
combined GPS+BDS-3 BRD-only baseline and the pro-
posed integrated configurations. Fig. 13 and Table VIII
presenttheresults.
Fig.13indicatesthatBRD+HAS+B2bachievesthebest
performance, followed by BRD+HAS, while BRD-only
performstheworst.UnderBRD-only,thedailymean3-D
orbitRMSgenerallyliesin20–30cmrange.Incorporating
HAS-GPS reduces this to 15–20 cm, and further adding
PPP-B2b obtains a modest additional gain to 15–18 cm.
This pattern accords with the above analysis of the ac- Fig.15. Dailyground-trackmapsof3-Dorbitaccuracyforthethree
strategiesonDOY111,2025.
curacy and availability characteristics of HAS and PPP-
B2b.TableVIIIquantifiestheseimprovements.Themean
3-D RMS is 25.06 cm for BRD-only and decreases to
D. SpatiotemporalAnalysisofGlobalOrbitAccuracy
18.86 cm with HAS integration (BRD+HAS), indicating
an improvement of 24.7%. With the further integration of After establishing aggregate improvements from the
PPP-B2b (BRD+HAS+B2b), the 3-D RMS decreases to additional integration of HAS and PPP-B2b corrections,
17.09 cm, representing improvements of 31.8% and 9.4% wefurthervalidatetheperformancegainbyexaminingthe
relativetoBRD-onlyandBRD+HAS,respectively.Overall, spatiotemporalbehaviorofthereal-time3-Dorbitaccuracy
the combined use of HAS and PPP-B2b corrections with ofLT-1A.Figs.14and15illustratethetimeseriesandthe
BRDprovidesapracticalandeffectivemethodtoimprove global spatial distribution of the 3-D orbit RMS error for
real-timeKODaccuracy. DOY111,2025,respectively.
6798 IEEETRANSACTIONSONAEROSPACEANDELECTRONICSYSTEMS VOL.62 2026
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 12 -->

Fig.14showsthatapplyingHASandPPP-B2bcorrec-
tions achieve a clear improvement. Specifically, the time
series becomes more stable, the fluctuation amplitude is
reduced,andlargeexcursions(likethoseover30cm)arefar
lessfrequent.Bothcorrectedconfigurationsexhibithigher
accuracyandtightervariabilitythanBRD-only,consistent
with the aggregate statistics above. Quantitatively, over
those common epochs, the fraction for which BRD+HAS
achieveslowerRMSerrorthanBRD-onlyis74.7%,rising
to 84.8% for BRD+HAS+B2b. It is important to note that
while the integration strategy generally outperforms the
baselines,transientdegradationsareobservedfromFig.14
atspecificintervals,suchasaround05:00and23:00.These
typically coincide with the LEO satellite traversing the
boundary of the PPP-B2b service domain. To be clear, in
theseboundaryregions,thenumberofsatelliteswithvalid
Fig.16. Boxplotof3-Dorbitaccuracyfortheglobaldomainandthe
corrections often fluctuates near the selection threshold,
Asia–Pacificregion.Theboxplotshowstheminimum,25th,50th
i.e., N 0 =4. Although the CCES method includes noise (median),and75thpercentiles,andthemaximum.
inflationtomanagetransitions,rapidoscillationbetweenthe
correctedandBRD-onlymodescanintroducetransientin-
effectivenessofintegratingmultiplecorrectionservicesto
stabilities.Specifically,whenavailabilitydropsmarginally
ensurehigh-precisioncoverage.
abovethethreshold,thefilterreliesonageometricallyweak
Taken together, the spatiotemporal analysis confirms
subset of corrected satellites. Conversely, frequent mode
thattheproposedintegratedmethodsignificantlyenhances
switching disturbs the convergence of the pseudoambigu-
real-timeKODperformanceforLEOsatellites,delivering
ity states. These combined factors can, therefore, lead to
highaccuracy,adaptability,androbustnessacrossdifferent
briefperiodswheretheintegratedsolutionexhibitsslightly
service-coverageconditions.
highernoisecomparedtothesmoother,albeitlessaccurate,
BRD-only baseline. Notably, BRD+HAS+B2b uses PPP-
E. ComparativeExperimentsintheAsia–PacificRegion
B2b BDS-3 to offset periods of poor HAS-GPS geometry
(e.g.,around07:00).EvenwhenBRD+HASunderperforms Despite that the global analysis indicated only a 9.4%
BRD-only, adding PPP-B2b typically restores, and often improvement(from18.86to17.09cm)whenaddingPPP-
surpasses,BRD-onlyaccuracy.Overall,thetemporalanal- B2btotheBRD+HASbaseline,thisglobalmeanobscures
ysis indicates that HAS and PPP-B2b corrections main- the specific contribution of PPP-B2b within its service
tain stable accuracy and suppress large excursions, with domain.Toisolatetheregionalimpact,weanalyzedthere-
BRD+HAS+B2b delivering the most stable performance sultsoverasubsetoftheAsia–Pacificregion(70◦E–170◦E;
acrosstheday. 10◦S–80◦N).
Focusing on the spatial distribution of 3-D orbit ac- Fig. 16 shows the statistical distribution of postcon-
curacy, Fig. 15 illustrates that, relative to BRD-only, the vergence 3-D orbit errors for the BRD-only, BRD+HAS,
BRD+HASandBRD+HAS+B2bmapsshifttowardcooler and BRD+HAS+B2b strategies in this region. Virtu-
tones, indicating a global improvement when HAS and ally, both corrected configurations, i.e., BRD+HAS and
PPP-B2bcorrectionsareapplied.Globally,over70%ofgrid BRD+HAS+B2b,outperformtheBRD-onlybaseline.No-
cellsachievelessthan20cm3-DRMSunderbothcorrected tably, compared to BRD+HAS, the BRD+HAS+B2b con-
configurations,andover20%achievelessthan10cm.By figurationshowsalowermedianerrorandareducedupper
contrast,underBRD-only,onlyabout7%andlessthan45% whisker, reflecting a suppression of high-error outliers.
ofcellsreach≤10and≤20cm,respectively.Inaddition,to
In addition, it exhibits a narrower box (i.e., a smaller
illustratethecomplementarycoverageoftheRTSs,Fig.15 interquartile range), indicating improved solution stabil-
marks the regions where the availability of HAS service ity and reduced error dispersion within the Asia–Pacific
is not guaranteed (indicated by solid red rectangles) and subset.
the nominal service area of PPP-B2b (indicated by black TableIXfurtherquantifiestheregionalbenefitinterms
dashed rectangles). It can be found from the figure that of the 3-D orbit RMS. In the selected subset, the 3-D
the PPP-B2b service domain effectively aligns with the RMSimprovesfrom25.47cmundertheBRD-onlysolution
HASnonguaranteedregionintheAsia–Pacific.WhileHAS to 20.57 cm after incorporating HAS (BRD+HAS). The
typicallymaintainspartialavailabilityovertheseareas,the additionalintegrationofPPP-B2b(BRD+HAS+PPP-B2b)
additionofPPP-B2bprovidescriticalaugmentation.Within further reduces the RMS to 16.63 cm. This results corre-
thePPP-B2bservicedomain,theBRD+HAS+B2bconfig- sponds to a 19.2% reduction relative to BRD+HAS in the
urationachievesa3-Dorbiterrorof≤10cmover35%of
Asia–Pacific region, which is substantially larger than the
theareaand≤20cmover90%ofthearea,confirmingthe globalgain(∼9.4%).
LIUETAL.:REAL-TIMEKODFORLEOBYINTEGRATINGBRD,GALILEOHAS,ANDBDS-3PPP-B2B 6799
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 13 -->

TABLEIX
AverageReal-TimeOrbitRMSintheSelectedAsia–PacificSubsetforBRD-Only,BRD+HAS,andBRD+HAS+B2bOverthe
EntireStudyPeriod
Overall, these regional experiments confirm that the dependence of real-time KOD on observation quality and
contributionofPPP-B2bisnotmarginal;instead,itprovides constellation geometry, we propose an integrated method
aclearadditionalimprovementoverBRD+HASwithinits that integrates BRD with HAS and PPP-B2b corrections,
service domain. This validates the capability of the pro- referredtoasCCES.TheCCESmethodachievesaglobal
posed strategy to effectively leverage regional corrections 3-DRMSof17.09cm,representinga31.8%improvement
tocomplementHASinareaswhereitsserviceisrelatively overBRD-onlyanda9.4%reductionrelativetoBRD+HAS
weaker, improving both accuracy and robustness where it (18.86cm).Finally,thetargetedanalysisoftheAsia–Pacific
mattersmost. regionfurthervalidatestheefficacyoftheproposedstrategy.
Inthistypicalregion,theadditionalinclusionofPPP-B2b
VI. CONCLUSION reduces the 3-D RMS from 20.57 cm for BRD+HAS to
16.63 cm. This represents a 19.2% improvement, greatly
The accuracy of real-time KOD for LEO missions is
outperforming the corresponding global average gain and
primarily governed by the quality of GNSS ephemerides
demonstrating the critical role of PPP-B2b in augmenting
and clocks and the constellation geometry of available
globalservicesovertheAsia-Pacificregion.
satellites.Inthisstudy,weincorporateHASandPPP-B2b
In summary, the results show that HAS and PPP-B2b
corrections and develop an integrated method to enhance
materially enhance real-time KOD for LEO satellites and
real-timeKODperformanceforLEOsatellites.
validate the proposed integrated method. The study helps
Applying HAS and PPP-B2b corrections substantially
address limitations in the existing research on BRD-only
improvestheorbitaccuracy.ForBDS-3,however,theim-
real-time KOD and, by analyzing combinations of HAS,
provementsarerelativelysmaller,primarilybecauseBDS-3
PPP-B2b,andBRD,providespracticalguidanceforhigh-
CNAV ephemerides are intrinsically of higher quality. By
precisionautonomousnavigation.However,thisstudystill
contrast,theclockstabilityimprovessignificantlyforboth
has some limitations. First, on the application side, be-
GPS and BDS-3, with debiased RMS variations within
∼10cm.Furthermore,thedebiasedSISRE,evaluatedafter cause tri-system receivers (GPS, Galileo, and BDS-3) are
not yet common on LEO platforms, we do not examine
removingconstantsatellite-dependentclockbiases,shows
Galileo-related products in the onboard experiments. Sec-
clearimprovementsrelativetoBRD.
Consistent with the above assessment, the real-time
ond, this study adopts certain thresholds, i.e., N
0
=4, and
there is a lack of an in-depth investigation of threshold
static PPP results show that the integrated solution deliv-
ers high availability (>97%) and centimeter-level accu- design.Accordingly,adaptivethresholdingisnotaddressed
in this study and remains a topic for future work. Third,
racywhenPPP-B2bcontributeseffectively(e.g.,2.62and
while this study evaluates real-time KOD using HAS and
2.09 cm at WUH2). In contrast, the integration benefit is
PPP-B2bproductswithoutambiguityresolutionduetothe
reducedunderlimitedPPP-B2bcoverage,wherePPP-B2b
lackofphase-biasproductsinthecurrentservices,wealso
correction availability drops markedly and the corrected-
acknowledge that PPP-AR could further enhance perfor-
satellitesetcanevenfalltozero,leavingthesolutionlargely
mance [57], [58]. Our future work will, therefore, investi-
drivenbyHAS.Buildingonthisevidence,wethenevaluate
gatePPP-ARforHASandPPP-B2binadedicatedfollow-
thereal-timeLEOKODstrategiesandproposeanintegrated
on study. Looking ahead, the deployment of multi-GNSS
method.
constellationreceptioncapabilityandtheglobalavailability
Supported by these findings and an LT-1A visibility
ofPPP-B2bcorrectionsshouldmakecentimeter-levelreal-
assessment, we evaluate three KOD strategies, i.e., BRD-
timeKODachievableglobally,enablingtime-criticalappli-
only, BRD+HAS,andBRD+HAS+PPP-B2b.Specifically,
cations in Earth observation, space-environment research,
wefirstidentifytheoptimalpseudoambiguityrandom-walk
andautonomoussatelliteoperations.
noise for each ephemeris source and demonstrate the re-
sulting gains in real-time KOD accuracy. We then ana-
lyze the advantages of the combined GPS+BDS-3 solu-
tion under BRD-only in terms of satellite geometry and REFERENCES
observationavailability.Buildingontheseresults,theBRD-
[1] C. J. Donlon et al., “The Copernicus Sentinel-6 mission: En-
only GPS+BDS-3 solution achieves a 3-D orbit RMS of
hanced continuity of satellite sea level measurements from
25.06 cm, improving on the GPS-only and BDS-3-only space,” Remote Sens. Environ., vol. 258, 2021, Art. no. 112395,
baselines by 53.4% and 33.0%, respectively. Given the doi:10.1016/j.rse.2021.112395.
6800 IEEETRANSACTIONSONAEROSPACEANDELECTRONICSYSTEMS VOL.62 2026
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 14 -->

[2] B.Wangetal.,“Alightweightandadaptiveimageinferencestrategy [22] R. V. Valenzuela et al., “Manoeuvre detection for near-orbiting
forearthobservationonLEOsatellites,”RemoteSens.,vol.17,2025, objects,”inProc.8thEur.Conf.SpaceDebris(Virtual),Darmstadt,
Art.no.1175,doi:10.3390/rs17071175. Germany,Paper238,Apr.20–23,2021.
[3] M.Wermuthetal.,“TerraSAR-Xpreciseorbitdeterminationwith [23] C. Siemes et al., “New thermosphere neutral mass density and
real-time GPS ephemerides,” Adv. Space Res., vol. 50, 2012, crosswind datasets from CHAMP, GRACE, and GRACE-FO,”
pp.549–559,doi:10.1016/j.asr.2012.03.014. J. Space Weather Space Climate, vol. 13, 2023, Art. no. 16,
[4] C. Chang, Q. Zhao, M. Li, and W. Li, “Augmentation mes- doi:10.1051/swsc/2023014.
sagedesignforLEO-enhancedprecisepositioning:In-orbitperfor- [24] A.Jäggietal.,“Swarmkinematicorbitsandgravityfieldsfrom18
manceassessment,”Measurement,vol.243,2025,Art.no.116314, monthsofGPSdata,”Adv.SpaceRes.,vol.57,2016,pp.218–233,
doi:10.1016/j.measurement.2024.116314. doi:10.1016/j.asr.2015.10.035.
[5] S. Xu et al., “Multi-GNSS Precise Point Positioning en- [25] O. Montenbruck, T. van Helleputte, R. Kroes, and E. Gill, “Re-
hanced by the real navigation signals from CENTISPACETM duced dynamic orbit determination using GPS code and carrier
LEO mission,” Adv. Space Res., vol. 73, 2024, pp.4175–4186, measurements,” Aerosp. Sci. Technol., vol. 9, 2005, pp.261–271,
doi:10.1016/j.asr.2024.01.017. doi:10.1016/j.ast.2005.01.003.
[6] Y. Yang, Y. Mao, X. Ren, X. Jia, and B. Sun, “Demand and [26] Y. Yang et al., “Multi-frequency smartphone positioning per-
keytechnologyforaLEOconstellationasaugmentationofsatel- formance evaluation: Insights into A-GNSS PPP-B2b services
lite navigation systems,” Satell. Navig., vol. 5, 2024, Art. no. 11, and beyond,” Satell. Navig., vol. 5, 2024, Art. no. 25,
doi:10.1186/s43020-024-00133-w. doi:10.1186/s43020-024-00146-5.
[7] U. Tancredi, A. Renga, and M. Grassi, “Validation on flight [27] Y.Yang,X.Yue,andA.G.Dempster,“GPS-basedonboardreal-time
data of a closed-loop approach for GPS-based relative navigation orbitdeterminationforLEOsatellitesusingaconsiderKalmanfilter,”
of LEO satellites,” Acta Astronaut., vol. 86, 2013, pp.126–135, IEEE Trans. Aerosp. Electron. Syst., vol. 52, no. 2, pp.769–777,
doi:10.1016/j.actaastro.2013.01.005. Apr.2016,doi:10.1109/TAES.2015.140758.
[8] X.Mietal.,“AbsoluteandrelativePODofLEOsatellitesinforma- [28] X. Sun, C. Han, and P. Chen, “Precise real-time navigation of
tionflying:Undifferencedanduncombinedapproach,”Adv.Space LEOsatellitesusingasingle-frequencyGPSreceiverandultra-rapid
Res.,vol.72,2023,pp.1070–1080,doi:10.1016/j.asr.2023.05.024. ephemerides,” Aerosp. Sci. Technol., vol. 67, 2017, pp.228–236,
[9] Y.Cai,Y.Li,andZ.Wang,“Real-timehigh-precisionbaselinemea- doi:10.1016/j.ast.2017.04.006.
surementofsatelliteformationflyingbasedonGNSS,”Adv.Space [29] W.Zhangetal.,“Precisereal-timenavigationoftheLT-1Asatellite
Res.,vol.73,2024,pp.5171–5187,doi:10.1016/j.asr.2024.02.025. basedonnewBDS-3B1C/B2asignals,”IEEESens.J.,vol.24,no.6,
[10] A.Reichert,T.Meehan,andT.Munson,“Towarddecimeter-level pp.8551–8562,Mar.2024,doi:10.1109/JSEN.2024.3361493.
real-timeorbitdetermination:AdemonstrationusingtheSAC-Cand [30] O. Montenbruck and P. Steigenberger, “The 2024 GPS accuracy
CHAMPspacecraft,”inProc.15thInt.Techn.MeetingSatell.Div. improvementinitiative,”GPSSolutions,vol.29,2024,Art.no.33,
Inst.Navig.,2002,pp.1996–2003. doi:10.1007/s10291-024-01793-6.
[11] O. Montenbruck and P. Ramos-Bosch, “Precision real-time [31] M.Lietal.,“Performanceevaluationofreal-timeorbitdetermination
navigation of LEO satellites using global positioning system forLUTAN-01Bsatelliteusingbroadcastearthorientationparam-
measurements,” GPS Solutions, vol. 12, 2008, pp.187–198, etersandmulti-GNSScombination,”GPSSolutions,vol.28,2023,
doi:10.1007/s10291-007-0080-x. Art.no.52,doi:10.1007/s10291-023-01593-4.
[12] A. Hauschild and O. Montenbruck, “Precise real-time navigation [32] F. Wang, X. Gong, J. Sang, and X. Zhang, “A novel method
ofLEOsatellitesusingGNSSbroadcastephemerides,”Navigation, for precise onboard real-time orbit determination with a stan-
vol.68,2021,pp.419–432,doi:10.1002/navi.416. dalone GPS receiver,” Sensors, vol. 15, 2015, pp.30403–30418,
[13] Z. Wang et al., “Real-time precise orbit determination for LEO doi:10.3390/s151229805.
betweenkinematicandreduced-dynamicwithambiguityresolution,” [33] Z. Wang et al., “Comparison of the real-time precise or-
Aerospace,vol.9,2022,Art.no.25,doi:10.3390/aerospace9010025. bit determination for LEO between kinematic and reduced-
[14] K.Wang,A.El-Mowafy,andX.Yang,“LEOsatelliteclockmodeling dynamic modes,” Measurement, vol. 187, 2022, Art. no. 110224,
anditsbenefitsforLEOKinematicPOD,”RemoteSens.,vol.15, doi:10.1016/j.measurement.2021.110224.
2023,Art.no.3149,doi:10.3390/rs15123149. [34] N. Naciri, D. Yi, S. Bisnath, F. Javier de Blas, and R. Capua,
[15] D. Li, X. Zhou, and K. Li, “Centimeter-level orbit determination “AssessmentofGalileoHighAccuracyService(HAS)testsignals
ofGRACE-CusingIGS-RTSData,”RemoteSens.,vol.15,2023, andpreliminarypositioningperformance,”GPSSolutions,vol.27,
Art.no.1832,doi:10.3390/rs15071832. 2023,Art.no.73,doi:10.1007/s10291-023-01410-y.
[16] R.Zhang,Y.Xiong,S.Xu,W.Chen,X.Li,andB.Zhao,“Assessment [35] X. Wang et al., “An investigation of PPP-B2b coverage
ofswarmkinematicorbitdeterminationusingtwodifferentdouble- and its performance in ZTD estimation and positioning in
difference methods,” Remote Sens., vol. 15, 2023, Art. no. 2669, different regions,” Surv. Rev., vol. 57, pp.258–272, 2024,
doi:10.3390/rs15102669. doi:10.1080/00396265.2024.2401665.
[17] O.Montenbruck,E.Gill,andM.Markgraf,Phoenix-XNS—AMinia- [36] X. Wang et al., “Assessment of BDS-3 PPP-B2b service
tureReal-TimeNavigationSystemforLEOSatellites.Noordwijk: and its applications for the determination of precipitable
TheNetherlands:Eur.SpaceAgency,2006. water vapour,” Atmosphere, vol. 15, 2024, Art. no. 1048,
[18] X. Li, J. Wu, K. Zhang, X. Li, Y. Xiong, and Q. Zhang, “Real- doi:10.3390/atmos15091048.
timekinematicpreciseorbitdeterminationforLEOsatellitesusing [37] I.Fernandez-Hernandezetal.,“Galileohighaccuracyservice:Ini-
zero-differencedambiguityresolution,”RemoteSens.,vol.11,2019, tial definition and performance,” GPS Solutions, vol. 26, 2022,
Art.no.2815,doi:10.3390/rs11232815. Art.no.65,doi:10.1007/s10291-022-01247-x.
[19] K.Kuang,S.Zhang,andJ.Li,“Real-timeGPSsatelliteorbitand [38] Y.Chenetal.,“Real-timeprecisepointpositioningduringoutages
clockestimationbasedonOpenMP,”Adv.SpaceRes.,vol.63,2019, ofthePPP-B2bservice,”RemoteSens.,vol.15,2023,Art.no.784,
pp.2378–2386,doi:10.1016/j.asr.2019.01.009. doi:10.3390/rs15030784.
[20] H. Shim and C. Kee, “Highly efficient real-time kinematic-based [39] H.Kan,Z.Hu,G.Chen,X.Liu,C.Liu,andQ.Zhao,“Performance
precise relative navigation for autonomous rendezvous CubeSat,” comparisonoforbitandclockaugmentationcorrectionsfromPPP-
Navigation, vol. 71, 2024, Art. no. navi.661, doi: 10.33012/navi. B2b,HASandCLAS,”Adv.SpaceRes.,vol.74,pp.668–681,2024,
661. doi:10.1016/j.asr.2024.04.029.
[21] Y.Zhuang,L.Wang,andH.Zhou,“Real-timekinematicorbitdeter- [40] H. Wei, G. Xiao, P. Zhou, P. Li, Z. Xiao, and B. Zhang, “Com-
mination of GRACE d satellite using GPS broadcast ephemeris,” biningGalileoHASandBeidouPPP-B2bwithHelmertcoordinate
in Proc. IEEE Int. Conf. Unmanned Syst., 2023, pp.937–942, transformationmethod,”GPSSolutions,vol.29,2024,Art.no.35,
doi:10.1109/ICUS58632.2023.10318354. doi:10.1007/s10291-024-01789-2.
LIUETAL.:REAL-TIMEKODFORLEOBYINTEGRATINGBRD,GALILEOHAS,ANDBDS-3PPP-B2B 6801
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 15 -->

[41] M.Wu,L.Wang,W.Xie,F.Yue,andB.Cui,“Performanceevaluation DingyiLiureceivedtheB.S.degreeinsurveying
andapplicationfieldanalysisofprecisepointpositioningbasedon engineering from the China University of
differentreal-timeaugmentationinformation,”RemoteSens.,vol.16, Mining and Technology, Xuzhou, China, in
2024,Art.no.1349,doi:10.3390/rs16081349. 2021.HeiscurrentlyworkingtowardthePh.D.
degreewiththeUniversityofChineseAcademy
[42] F. S. Prol et al., “Enabling the Galileo High Accuracy
ofSciences,Beijing,China,andtheAerospace
Service with open-source software: Integration of HASlib
Information Research Institute, Chinese
and RTKLIB,” GPS Solutions, vol. 28, 2024, Art. no. 71, AcademyofSciences,Beijing.
doi:10.1007/s10291-024-01617-7. His main research interests include precise
[43] A. Hauschild, O. Montenbruck, P. Steigenberger, I. Mar- orbitdeterminationforlowEarthorbitsatellites.
tini, and I. Fernandez-Hernandez, “Orbit determination
of Sentinel-6A using the Galileo high accuracy service
test signal,” GPS Solutions, vol. 26, 2022, Art. no. 120,
doi:10.1007/s10291-022-01312-5.
[44] Y.Shi,T.Xu,M.Li,K.Wei,S.Wang,andD.Wang,“Real-time Haobo Li received the first Ph.D. degree in
precise orbit determination of low earth orbit satellites based on geodesy and surveying engineering from the
China University of Mining and Technology,
GPS and BDS-3 PPP B2b service,” Remote Sens., vol. 16, 2024,
Xuzhou,China,in2021,andthesecondPh.D.
Art.no.833,doi:10.3390/rs16050833.
degreeingeospatialsciencefromRMITUniver-
[45] L. Pan and C. Yang, “BDS-3 PPP-B2b and Galileo HAS tightly sity,Melbourne,VIC,Australia,in2021.
integratedreal-timePPP,”GPSSolutions,vol.29,2025,Art.no.162, He was a Postdoctoral Researcher with
doi:10.1007/s10291-025-01925-6. TsinghuaUniversity,Beijing,China.Heiscur-
[46] Y.Yangetal.,“FeaturedservicesandperformanceofBDS-3,”Sci. rentlyaResearchFellowwithRMITUniversity.
Bull.,vol.66,pp.2135–2143,2021,doi:10.1016/j.scib.2021.06.013. HisresearchinterestsincludeGlobalNavigation
[47] W. Zhang, Y. Lou, W. Song, W. Sun, X. Zou, and X. Gong, Satellite System atmospheric monitoring and
“InitialassessmentofBDS-3precisepointpositioningserviceon satellitepositioning,navigation,andtiming.
GEO B2b signal,” Adv. Space Res., vol. 69, 2022, pp.690–700,
doi:10.1016/j.asr.2021.09.006.
[48] Z.DongandS.Zhang,“SISREofBDS-3MEO:Evolutionaswell
as comparison between D1 and B-CNAV (B-CNAV1, B-CNAV2) Jinglei Zhang received the M.S. degree in
navigation messages,” Remote Sens., vol. 16, 2024, Art. no. 484, surveying engineering with specialization in
Global Navigation Satellite System (GNSS),
doi:10.3390/rs16030484.
fromtheChinaUniversityofGeosciences,Bei-
[49] P. Liu, K. V. Ling, H. Qin, and T. Liu, “Performance analysis of
jing,China,in2021.
real-timeprecisepointpositioningwithGPSandBDSstatespace
HeiscurrentlyanAssistantEngineerwiththe
representation,” Measurement, vol. 215, 2023, Art. no. 112880, AerospaceInformationResearchInstitute,Chi-
doi:10.1016/j.measurement.2023.112880. neseAcademyofSciences,Beijing.Hisresearch
[50] “European Union Galileo High Accuracy Service signal-in-space interestsincludeGNSSprecisepositioningand
interfacecontroldocument(HASSISICD),”Issue1.0,2022.[On- GNSSmeteorology.
line].Available:https://www.gsc-europa.eu/sites/default/files/sites/
all/files/Galileo_HAS_Info_Note.pdf
[51] O. Montenbruck, P. Steigenberger, and A. Hauschild, “Multi-
GNSS signal-in-space range error assessment—Methodology
and results,” Adv. Space Res., vol. 61, 2018, pp.3020–3038,
doi:10.1016/j.asr.2018.03.041.
[52] P. Steigenberger, Z. Deng, J. Guo, L. Prange, S. Song, and O. XiaomingWangreceivedthePh.D.degreein
Montenbruck,“BeiDou-3orbitandclockqualityoftheIGSMulti- geodesy (with specialization in Global Navi-
GNSSpilotproject,”Adv.SpaceRes.,vol.71,2023,pp.355–368, gation Satellite System (GNSS) meteorology)
doi:10.1016/j.asr.2022.08.058. fromRMITUniversity,Melbourne,VIC,Aus-
[53] X.Gongetal.,“Precisereal-timenavigationoftheLEOsatellite tralia,in2017.
enhanced by BDS-3 PPP-B2b service,” Adv. Space Res., vol. 75, He is currently a Professor with the
AerospaceInformationResearchInstitute,Chi-
pp.7003–7019,2025,doi:10.1016/j.asr.2025.03.049.
neseAcademyofSciences,Beijing,China,and
[54] X. Gong, J. Sang, F. Wang, and X. Li, “LEO onboard real-
the School of Electronic, Electrical and Com-
time orbit determination using GPS/BDS data with an optimal municationEngineering,UniversityofChinese
stochastic model,” Remote Sens., vol. 12, 2020, Art. no. 3458, AcademyofSciences,Beijing.Hisresearchin-
doi:10.3390/rs12203458. terestsincludeGNSSprecisepositioningandGNSSmeteorology.
[55] O. Montenbruck, S. Hackel, M. Wermuth, and F. Zangerl,
“Sentinel-6A precise orbit determination using a combined
GPS/Galileo receiver,” J. Geodesy, vol. 95, 2021, Art. no. 109,
doi:10.1007/s00190-021-01563-z.
[56] M. Li et al., “Precise orbit determination for the Haiyang-
2D satellite using new onboard BDS-3 B1C/B2a signal mea-
surements,” GPS Solutions, vol. 26, 2022, Art. no. 137, Shu Xu received the B.S. and M.S. degrees
doi:10.1007/s10291-022-01322-3. in photogrammetry from Wuhan University,
[57] J. Tao, G. Zhang, G. Chen, Y. Jiang, and Q. Zhao, “Real-time Wuhan,China,in2016and2019,respectively.
estimationofmulti-frequencyphaseobservable-specificbiasforthe He is currently an Engineer with the
BDS-3PPP-B2bservice,”GPSSolutions,vol.29,2025,Art.no.19, AerospaceInformationResearchInstitute,Chi-
doi:10.1007/s10291-024-01776-7. neseAcademyofSciences,Beijing,China.His
[58] G. Xiao, Z. Xiao, P. Zhou, C. Liu, H. Wei, and P. Li, “Perfor- currentresearchinterestsincluderemotesensing
satellitedataprocessing.
mance evaluation of Galileo high accuracy service for PPP am-
biguity resolution,” GPS Solutions, vol. 29, 2025, Art. no. 96,
doi:10.1007/s10291-025-01852-6.
6802 IEEETRANSACTIONSONAEROSPACEANDELECTRONICSYSTEMS VOL.62 2026
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 16 -->

SuelynnChoyreceivedthePh.D.degreeinpre- ZheLireceivedtheB.S.degreeinsurveyingen-
cisesatellitepositioningfromRMITUniversity, gineeringfromtheChinaUniversityofMining
Melbourne,VIC,Australia,in2009. andTechnology,Xuzhou,China,in2022.Heis
She is currently a Professor of Geospatial currentlyworkingtowardthePh.D.degreewith
Science and Satellite Navigation with RMIT theUniversityofChineseAcademyofSciences,
UniversityandtheDirectoroftheRMITSatellite Beijing,China.
PositioningforAtmosphere,ClimateandEnvi- HisresearchinterestsincludeGlobalNaviga-
ronmentResearchCentre.Herresearchinterests tionSatelliteSystemRadioOccultation.
include precise satellite positioning and navi-
gation,geodesy,andtheuseofgeospatialand
satellite technologies for disaster management
andatmosphericremotesensing.
YingXureceivedthePh.D.degreeinsignalpro-
cessingfromtheBeijingInstituteofTechnology,
Beijing,China,in2009.
She is currently a Research Professor, a
Doctoral Supervisor, and the Director of the
Navigation Technology Research Laboratory,
AerospaceInformationResearchInstitute,Chi-
nese Academy of Sciences, Beijing. Her re-
search interests include satellite navigation
technology and its augmentation technology
andmultisourcefusionlocalizationtheoryand
methods.
LIUETAL.:REAL-TIMEKODFORLEOBYINTEGRATINGBRD,GALILEOHAS,ANDBDS-3PPP-B2B 6803
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:26:14 UTC from IEEE Xplore. Restrictions apply.