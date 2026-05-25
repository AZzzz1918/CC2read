<!-- PAGE: 1 -->

JournalofGeodesy (2026) 100:19
https://doi.org/10.1007/s00190-026-02039-8
ORIGINAL ARTICLE
Real-time oceanic PWV sensing using BeiDou-3 PPP-B2b and low-cost
GNSS devices
Hongxing Zhang1,2 ·Yunbin Yuan1·Luohong Li1,2·Wei Li1·Wenjian Huang1,2·Yanju Chai1·Dong Ren3
Received:19December2024/Accepted:22January2026
©Springer-VerlagGmbHGermany,partofSpringerNature2026
Abstract
Real-timesensingofprecipitablewatervapor(PWV)usingGNSSiscriticalforatmosphericmonitoring.Conventionalreal-
time precise point positioning (PPP) reliant on the IGS real-time service (RTS) remains limited in oceanic regions due to
terrestrialinternetdependencies.BeiDou’ssatellite-basedPPP-B2bserviceovercomesthislimitation,enablingreal-timePWV
sensingovertheocean.However,itsrelativelyloweraccuracyhashinderedbroaderapplication.Additionally,thepotential
ofcombiningPPP-B2bwithlow-costGNSSdevicesforoceanicPWVsensingremainsinsufficientlyexplored.Thisstudy
presentsapracticalandcost-effectiveapproachforreal-timeoceanicPWVsensingbyjointlyusingPPP-B2bandlow-cost
GNSSdevices.ToaddresstheinherenterrorsinPPP-B2bcorrections,wedeveloparefinedPPPstrategybasedonambiguity
reparameterization and optimized stochastic modeling. Unlike conventional PPP that treats ambiguities as constants, this
methodmodelsthemastime-varyingrandom-walkprocesseswithinanoptimizedrangeofprocess-noisevalues.Thisallows
foradaptiveabsorptionofPPP-B2bcorrectionerrors,therebyimprovingtheaccuracyoftroposphericestimates.Validation
throughland-basedstaticandkinematicexperimentsdemonstratesaccuracyimprovementsof34and24%,respectively,in
troposphericestimates.WhenappliedtoIGS-RTScorrections,therefinedmethodachievesa10%accuracyimprovementin
real-timetroposphericestimation.Twooceaniccampaignsfurthervalidateitsoperationalfeasibility,yieldingaPWVaccuracy
improvementofover30%duringCruise1and47%duringCruise2comparedtoconventionalPPP.Thisframeworkoffers
aseamless,accurateandcost-effectivesolutionforreal-timetroposphericandPWVsensing,benefitingweatherforecasting
andclimatemonitoring.
Keywords BeiDounavigationsatellitesystem·Real·Timeprecisepointpositioning(PPP)·PPP·B2b·Oceanicprecipitable
watervapor·Low·CostGNSSdevices
1 Introduction evaporation (Schmitt et al. 1995). Real-time sensing of
oceanic precipitable water vapor (PWV) is critical for
The ocean is the largest source of atmospheric water preciseandtimelyglobalatmosphericanalyses,particularly
vapor, contributing approximately 86% of global for short-term severe weather forecasting (Huang et al.
2021;Gongetal.2021;Schneideretal.2010;Zhengetal.
B 2022). Several methods for oceanic PWV sensing have
HongxingZhang
caszhx@whigg.ac.cn been developed, utilizing both spaceborne (Du et al. 2014;
Gao et al. 2003; Xu and Liu 2024) and shipborne sensors
YunbinYuan
yybgps@whigg.ac.cn (Fujitaetal.2008;Wangetal.2019),buteachwithitsown
limitations.Forinstance,spacebornemicrowavesensorscan
LuohongLi
li.luohong@whigg.ac.cn offerbroadcoverageofPWVmeasurementsbutareheavily
affectedbyweatherconditions(HeandLiu2019;Jiangetal.
1 StateKeyLaboratoryofPrecisionGeodesy,Innovation
2024).Incontrast,GNSStechnologyofferscontinuous,all-
AcademyforPrecisionMeasurementScienceand
weather PWV observations and is increasingly recognized
Technology,ChineseAcademyofSciences,Wuhan,China
asapromisingmethodforshipbornePWVsensing(Männe
2 CollegeofEarthandPlanetarySciences,Universityof
etal.2021;Shojietal.2016;Wangetal.2019).
ChineseAcademyofSciences,Beijing,China
Using shipborne GNSS for real-time oceanic PWV
3 MinistryofNaturalResources,FourthInstituteof
sensing presents additional challenges compared to
Oceanography,Beihai,China
123
0123456789().: V,-vol

<!-- PAGE: 2 -->

19 Page 2 of 17 H.Zhangetal.
land-based GNSS stations. These challenges stem from forimprovingitsefficiencyandperformance.Additionally,
dynamic positioning conditions, limited telecommunica- the Galileo High Accuracy Service (HAS) offers another
tions infrastructure, and complex observation environment satellite-basedPPPservice,providingprecisecorrectionsfor
in oceanic regions (Rocken et al. 2005; Shoji et al. 2016; GPS and Galileo satellites (Naciri et al. 2023). Researches
Weietal.2023).Nevertheless,previousstudieshavedemon- haveexploredtheintegrationofPPP-B2bandGalileoHASto
stratedthefeasibilityofusingshipborneGNSSforoceanic enhancePPPperformance(Panetal.2025;Weietal.2025).
PWVsensing. Nevertheless, real-time orbit and clock corrections may
Early efforts, such as those by Chadwell et al. (2001), introduce systematic biases that degrade PPP performance
employedtheGPSrelativepositioningtechniques.However, (Hadas et al. 2020; Ji et al. 2023). For PPP-B2b, such
thisapproach’sdependenceonreferencestationslimitedits biasesaretypicallymorepronouncedbecauseitscorrections
application in remote oceanic regions. In contrast, GNSS are generated from a limited tracking network, resulting in
precise point positioning (PPP) strategy, which operates loweraccuracythanthatofIGS-RTS(Tangetal.2022;Xu
independently of reference stations, has become the dom- etal.2023).Whileseveralstudieshaveevaluatedthepoten-
inant method for shipborne PWV sensing. For instance, tial of PPP-B2b for estimating zenith tropospheric delay
Rockenetal.(2005)demonstratedthepotentialofpostpro- (ZTD) and PWV, Yang et al. 2023; Zhou et al. 2024 most
cessedPPPforoceanicPWVsensing,achievinganaccuracy of these investigations have been conducted using post-
of 2.8 mm. Shoji et al. (2016) further explored the PPP processed or simulated real-time configurations, typically
strategy, employing file-based GNSS satellite ephemeris to relyingonland-basedhigh-gradeGNSSstations.Fewstud-
retrieve PWV with an accuracy of 3.4 ~ 5.4 mm when ieshavevalidatedPPP-B2bundertruereal-timeconditions.
compared to radiosonde observations. Wang et al. (2019) Moreover, the relatively lower accuracy of PPP-B2b cor-
extended the application of postprocessed PPP to multi- rections remains a bottleneck for achieving high-quality
GNSSobservationsforshipbornePWVsensing,highlighting real-timePWVretrieval,andthischallengehasnotyetbeen
the advantages of multi-GNSS solutions over GPS-only adequatelyaddressed.Meanwhile,low-costGNSSdevices,
approaches. Männel et al. (2021) leveraged postprocessed idealfordeploymentonlarge-scalemobilemarineplatforms
PPPtoretrievepolarPWVusingshipborneGNSSdata.More suchasbuoys,aregainingpopularityfordensePWVsens-
recently,Wuetal.(2022)exploredtheuseofsimulatedreal- ing(Marutetal.2022).However,theintegrationofPPP-B2b
timePPPforoceanicPWVsensing,achievinganaccuracyof withsuchlow-costdevicesforreal-timeoceanicPWVmon-
4.0mm.Thesefindingscollectivelyunderscoretheevolving itoringremainsinsufficientlyexplored.
capabilities of shipborne GNSS for oceanic PWV sensing Thisstudyaimstoadvancereal-timeoceanicPWVsens-
andestablishafoundationforfurtheradvancementsinreal- ingbyjointlyusingPPP-B2bandlow-costGNSSdevices.To
timeapplications. addressthelimitationsofPPP-B2bcorrectionaccuracy,we
Real-timePPPrequirespreciseGNSSsatelliteorbitand developarefinedPPPmethodthateffectivelymitigatescor-
clockcorrections,whicharetypicallyprovidedbytheInter- rection errors, thereby improving the accuracy of real-time
nationalGNSSService(IGS)real-timeservice(RTS)(Hadas ZTDandPWVsensinginoceanicenvironments.
et al. 2020; Lee et al. 2013; Li et al. 2014; Lu et al. 2015;
Yuanetal.2014).However,therelianceonterrestrialinternet
infrastructurelimitstheapplicabilityofIGS-RTSinremote
2 Methodology
oceanic regions. Some studies have examined the feasibil-
ityofreal-timePPPusingbroadcastephemeris(Carlinetal.
We employed the real-time PPP technique to process real-
2021; Chen et al. 2022; Pan et al. 2024), but the accuracy
time GNSS data streams for estimating real-time ZTD.
achievedisinferiortothatofPPPsolutionsutilizingprecise
TheseZTDestimatesweresubsequentlyconvertedtoPWV
corrections. Satellite-based PPP services, which broadcast
using auxiliary atmospheric parameters, namely, the zenith
precise corrections via satellite, offer a promising solution
hydrostatic delay (ZHD) and weighted mean temperature.
for real-time high-accuracy PWV sensing in areas without
Specifically, ZHD was computed using the Saastamoinen
internetconnectivity.
model,whileweightedmeantemperaturewasderivedfrom
The BeiDou Navigation Satellite System (BDS-3) pro-
the Bevis empirical model (Bevis et al. 1992), with in-situ
videsanovelsatellite-basedPPPservice,knownasPPP-B2b,
pressureandtemperaturemeasurementsasinputs.
which broadcasts real-time precise orbit and clock correc-
tions for GPS and BDS-3 satellites via the B2b signals of
GeostationaryEarthOrbit(GEO)satellites(Tangetal.2022; 2.1 ConventionalPPPmethod
Yangetal.2019).Recently,Taoetal.(2025)presentanew
approachbyextractingphaseobservable-specificbiascom- Weadopttheionosphere-free(IF)combinationforPPP.By
patible with the PPP-B2b service, demonstrating potential leveraging precise satellite orbit and clock products, along
123

<!-- PAGE: 3 -->

Real-timeoceanicPWVsensingusingBeiDou-3 Page 3 of 17 19
withanaprioritroposphericdelaycorrection,theIFpseudo- Oneoptionistoaugmentthestatevectorwithexplicitper-
rangeandcarrier-phaseobservationequationscanbewritten satelliteEs parametersandestimatethemdirectly(Gunning
r
as: et al. 2019; Xu et al. 2023). While effective, this approach
increasesthestatedimensionalitybythenumberoftracked
(cid:2)Ps (cid:2)−es ·dx+c·dt +Ms ·dZ +ν ,
if r r r p satellitesandcomplicatesthefilter.
(1)
(cid:2)(cid:4)s
if
(cid:2)−e
r
s ·dx+c·dt
r
+M
r
s ·dZ +λ
if
·N
i
s
f
+ν (cid:4), An alternative, adopted here and motivated by the cor-
relationanalysisbelow,istoexploitthestructuralcoupling
where(cid:2)Ps and(cid:2)(cid:4)s aretheobservedminuscomputedIF betweenEsandNs(asillustratedinSect.“Correlationanaly-
if if r if
pseudorangeandcarrier-phaseforsatellites;es istheline- sisandtheoreticaljustificationfortherefinedPPPmethod”).
r
of-sight unit vector; dx is the position increment vector; C The Es forsatellites canbedecomposedas:
r
isthespeedoflight;dt isthereceiverclockerror;dZ isthe
r
correction to the a priori zenith tropospheric delay; Ms is Es (cid:2)λ ·(cid:2)Ns +ξ (4)
r r if if res
thetroposphericmappingfunction. Ns istheIFambiguity;
if
λ
if
istheIF-combinationwavelength;andv
p
andv(cid:4) arethe where(cid:2)N
i
s
f
istheambiguity-equivalentcomponentthatcan
measurementnoiseterms. beabsorbedinto Ns,andξ issmallresidual.Substituting
if res
Theunknownvariables,dx,dt ,dZ,andNs,formedastate (4) into (3) yields augmented residual terms and illustrates
(cid:2) (cid:3) r if
vectorX (cid:2) dx, dt r , dZ, N i s f T ,whichisestimatedviaan thattheeffectofE r s canbelargelyrepresentedbypermitting
extendedKalmanfilter(EKF).IntheconventionalPPP,the theambiguitytoevolveasaslowrandomwalk.Hence,rather
ambiguity N i s f istreatedastime-invariantwithzeroprocess thanestimatingE r s explicitly,weallowN i s f tohavenon-zero
noiseintheEKFpredictionstep: processnoise:
⎡ ⎤
⎢ δ dx ⎥ N i s f (k)(cid:2) N i s f (k−1)+ω N i s f (k), ω N i s f ∼N(0, Q N i s f ) (5)
⎢δ ⎥
X k|k−1 (cid:2)(cid:2) k|k−1 ·X k−1 + ⎢ ⎢ ⎣δ d d t Z r⎥ ⎥ ⎦ ·(cid:2)t, withδ N i s f (cid:2)0 (2) w ity i . th Th Q is N r i s f efi tu n n e e d d s t t o oc r h e a fl s e t c ic t m th o e d t e y l p in ic g a l l e E ts r s th te e m E p K o F ra a l d v a a p r t i i a v b e i l l y -
δ N i s f absorbslowlyvaryingE r swithoutincreasingthestatedimen-
sion.Asdemonstratedthroughacomparativeanalysisinthe
where (cid:7) k|k−1 is the state transition matrix, k denotes the Appendix A,thissimplified approach achieves comparable
epochnumber, X k|k−1 isthepredictedstateatepochk;and mitigationperformancetotheexplicitparameterestimation
δ dx δ dtr , δ dz ,andδ N
i
s
f
representtheprocess-noisetermsfor method.
the receiver coordinates, receiver clock error, zenith tropo-
spheric delay, and ambiguity, respectively, with (cid:2)t being 2.3 Correlationanalysisandtheoreticaljustification
thetimeintervalbetweenepochs.Thestateissubsequently fortherefinedPPPmethod
updatedusingtheinnovationvectorwithintheEKFframe-
work. The refined PPP strategy in Sect. “Refined real-time PPP
This conventional PPP formulation implicitly assumes method”implicitlyreliesonakeystructuralpropertyofthe
error-free satellite orbit and clock products, an assumption PPP model, namely, the strong satellite-specific coupling
thatdoesnotholdwhenusingreal-timecorrections. between Ns and Es. This coupling is the theoretical basis
if r
that enables Ns to effectively absorb Es, while preventing
if r
2.2 Refinedreal-timePPPmethod theirleakageintothetroposphericestimatesandotherglobal
parameters.Tosubstantiatethisprerequisite,weconductthe
Real-timeorbitandclockcorrections(e.g.,fromPPP-B2b) followingtwo-partanalysis:
inevitably contain residual errors. These residuals, denoted First, we derive the expected correlation structure from
E r s,typicallyrangefromafewcentimeterstoseveraldecime- the linearized PPP design matrix, demonstrating the inher-
ters (Tang et al. 2022) and exhibit temporal smoothness ently dominant coupling between Ns and Es. Second, to
if r
and satellite-specific variations (Xu et al. 2023). The IF validate the theory under realistic conditions, we conduct
observation equations with imperfect real-time corrections anempiricalcorrelationanalysisusingrealGPSandBDS-3
become: data, in which state-wise correlations are quantified based
onthecovariancematrixofthePPPsolution.Together,these
(cid:2)Ps (cid:2)−es ·dx+c·dt +Ms ·dZ +Es +v ,
if r r r r p analysessubstantiatethetheoreticalbasisoftherefinedPPP
(cid:2)(cid:4)s if (cid:2)−e r s ·dx+c·dt r +M r s ·dZ +λ if ·N i s f +E r s +v (cid:4), method.
(3)
123

<!-- PAGE: 4 -->

19 Page 4 of 17 H.Zhangetal.
2.3.1 (a)TheoreticalcorrelationcharacteristicsamongE r s tionderivedfromrealGNSSobservations.Afull-daydataset
andPPPparameters. collected at the DHSP station on 17 November 2025 was
processed using a modified PPP model in which the Es
r
From the linearized phase observation equation with Es parameters were explicitly estimated. The state covariance
r
(Eq.(3)): matrixP atthefinalepoch wasthenextracted foranalysis.
Theinterpretedstatevectorisgivenby:
(cid:2)(cid:4) i s f (cid:2)−e r s·dx+c·dtr +M r s·dZ+λ if ·N i s f +E r s+v (cid:4), ⎡
(6)
⎢
X(cid:2)⎣dx,dy,dz,dtrg,dtrc,dZ,
(cid:13)
NG1 ···NGm(cid:14) ,
(cid:15)
NC1 ···NCm(cid:16) ,
Thesensitivitiesoftheobservationto Ns and Es are:
if r GPS/BDS-3ambiguities
⎤
T
∂(cid:2)(cid:4) ∂(cid:2)(cid:4)
∂Ns if (cid:2)λ if , ∂Es if (cid:2)1 (7) (cid:13) EG1 ···EGm(cid:14) , (cid:15) EC1 ···ECm(cid:16) ⎥ ⎦ (11)
if r
GPS/BDS-3Es
r
i.e., both are additive, satellite-specific terms that enter the
equation with constant coefficients. Consequently, the cor- Thecorrespondingcorrelationmatrixwascomputedas:
responding columns of the PPP design matrix are nearly
P
collinear,resultinginanear-perfectcorrelationbetween Ns ρ (cid:2) (cid:17) ij (12)
if ij
and Es. Therefore, the correlation coefficient ρ between P ii P jj
r
thesetwoparametersisapproximately:
Figure 1 presents the resulting heatmap. A pronounced
(cid:10) (cid:11) (cid:12)(cid:10)
(cid:10)ρ Ns, Es (cid:10)≈1 (8) satellite-wise diagonal pattern is evident, indicating strong
if r correlations between each ambiguity parameter Ns and
if
its corresponding Es. This is consistent with the theoreti-
Incontrast,otherPPPparameters,includingreceivercoor- r
dinates(dxs),receiverclocks(dt ),andtroposphericdelays cal collinearity in Eq. (7) and (8). In contrast, coordinate
r r
and tropospheric delay parameters exhibit relatively weak
(dZ),affecttheobservationsthroughgeometryormapping
correlations with Es, reflecting their global and geometry-
factors: r
dependent nature, as described in Eq. (9) and (10). These
∂(cid:2)(cid:4) ∂(cid:2)(cid:4) ∂(cid:2)(cid:4)
if (cid:2)−es, if (cid:2)c, if (cid:2) Ms (9) empiricalobservationsalignwiththetheoreticalanalysisin
∂dx r ∂dt ∂dZ r Sect. “Correlation analysis and theoretical justification for
r
therefinedPPPmethod”(a)andconfirmingthatambiguity
These columns vary across satellites through e r s or M r s, parametersareprimarilyresponsibleforabsorbing Es.
r
representingglobalorgeometry-dependentsignaturesrather
than satellite-specific offsets. Consequently, the structural 2.4 Real-timePPPprocessingstrategies
collinearity that exists between Es and Ns does not exist
r if
between Es and dx or dZ; their correlations are therefore
r The success of the refined PPP method depends on select-
inherentlyweaker,yielding: ing an appropriate process-noise δ Ns for the ambiguity. To
(cid:10)
(cid:10)ρ
(cid:11)
dx, E r s
(cid:12)(cid:10)
(cid:10) (cid:5) (cid:5) (cid:10) (cid:10)
(cid:10)
(cid:10) ρ ρ (cid:11)
(cid:11)
N N i s s f , , E E r s s
(cid:12)
(cid:12)
(cid:10)
(cid:10) (cid:10) (cid:10) , , (cid:10) (cid:10)ρ
(cid:10)
(cid:10)ρ (cid:11)
(cid:11)
d d Z t r , , E E s r s (cid:12)
(cid:12)
(cid:10) (cid:10)
(cid:10)
(cid:10) (cid:5) (cid:10) (cid:10)ρ (cid:11) Ns, Es (cid:12)(cid:10) (cid:10)
i
y
n
s
v
is
es
b
t
y
ig
v
a
√ a
te
ry
t
i
h
n
i
g
s,
δ
w
N
e
i s f
c
fr
o
o
n
m
du
0
ct
t
e
o
d
2
a
1
n
.0
e
m
m if
m
pi
/
r√ica
h
l
i
s
n
en
in
s
c
it
r
i
e
v
m
ity
en
a
t
n
s
a
o
l-
f
if r r if r 3.0mm/ h.Eightschemes(S0-S7)weretested,withS0√rep-
(10) resentingtheconventionalPPPmethod(δ Ns (cid:2)0.0mm/ h).
if
The scheme designations are summarized in Table 1. This
Thisstructuralreasoningjustifiesthechoiceofabsorbing
designenablesacomparativeevaluationoffilterperformance
Es predominantlyintotheambiguitystatesviamodestnon-
r underdifferentstochasticassumptions.
zeroprocessnoise.
Thedetailedconfigurationsadoptedforreal-timePPPpro-
cessinginbothstaticandkinematicmodesaresummarized
2.3.2 (b)CorrelationanalysisusingrealPPPcovariance
inTable2.Notably,thetroposphericgradientmodelofChen
matrix
et al. (1997) is applied only in static mode, as azimuthal
asymmetriesinthetropospherecannotbereliablyestimated
To empirically validate the above theoretical analysis, we
whentheantennaisinmotion.
further investigated the covariance structure of a PPP solu-
123

<!-- PAGE: 5 -->

Real-timeoceanicPWVsensingusingBeiDou-3 Page 5 of 17 19
Fig.1 Correlation matrix derived from the final-epoch covariance of coordinates,receiverclocks,ZWD,ambiguityparametersandsatellite-
the full-day real-time PPP solution. The matrix includes receiver specificEs terms.AcleardiagonalstructureofstrongNs-Es correla-
r if r
tionsispresent,whereascorrelationsofEswithZWDandcoordinates
r
areweak
Table1 Schemedesignation
Scheme S0 S1 S2 S3 S4 S5 S6 S7
√
δ Ns (mm/ h) 0.0 3.0 6.0 9.0 12.0 15.0 18.0 21.0
if
Table2 Real-timePPP
processingstrategies Item Strategies
Observations GPS(L1/L2)andBDS-3(B1/B3)codeandphase(real-timestream)
Orbit/clockcorrections PPP-B2b/IGS-RTS(SSRA00WHU0)
Phase/codeweights 0.003m(phase),0.6m(code)
Elevationcut-off 7°
PCO/PCV Correctedusingigs20.atxRebischungandSchmid(2016)
Phasewind-up Corrected(Wuetal.1993)
√ √
Receivercoordinates Randomwalk:0m/ hforstatic;1×106m/ hforkinematic
√
Receiverclocks Randomwalk:1×109m/ h
ZHDmodel UNB3m
√
ZWDestimation Randomwalk:4.0mm/ h;GMFmappingfunction
Troposphericgradients Chenetal.(1997)model(staticmodeonly)
Ambiguities Randomwalkwithvaryingδ Ns accordingtoTable1
if
123

<!-- PAGE: 6 -->

19 Page 6 of 17 H.Zhangetal.
3 Datadescription 3.1.2 Oceanicscenario
3.1 GNSSdata Oceanic experiments were conducted during two research
cruises in the warm season, characterized by high and
To assess the efficacy of the refined method, experiments strongly variable PWV conditions, which pose significant
wereconductedintwodistinctscenarios:aland-basedsce- challengesfortroposphericsensing.
nario and an oceanic scenario. All experiments relied on
true real-time GNSS data streams, including raw observa-
tions, real-time orbit and clock corrections, and broadcast
1. Cruise 1 (September 21–25, 2023): covering the South
ephemeris, rather than postprocessed data files, to accu-
ChinaSea,EastChinaSea,andYellowSea.
rately reflect true real-time operational conditions. In both
2. Cruise2(August20,2024):conductedintheBeibuGulf,
scenarios, multiple PPP schemes were executed in paral-
asub-regionoftheSouthChinaSea.
lel,eachconfiguredwithadifferentambiguityprocess-noise
setting.Thisparallel-processingdesignenablesanunbiased
assessmentofhowambiguitystochasticmodelinginfluences
Across the two cruises, the vessel traveled more than
real-time PPP performance under identical data-streaming
2000 km. A low-cost mosaic-X5 receiver was mounted
conditions.
on the vessel to collect real-time GNSS streams, includ-
ing PPP-B2b corrections. Both conventional and refined
PPP methods were applied to the real-time data during the
3.1.1 Land-basedscenario
cruises.
For benchmarking, a high-grade Septentrio PolaRx5TR
Real-timeGNSSdatastreamswerecollectedsimultaneously
devicewasalsodeployedonthesameship,positionedless
fromtwocollocatedstations,DHSPandSEPT,deployedat
than2mfromthemosaic-X5antenna.Itsdatawererecorded
the Donghu Campus of the Innovation Academy for Preci-
andpostprocessedtogeneratehigh-precisionreferencesolu-
sionMeasurementScienceandTechnologyinWuhan,China
tions. Cruise trajectories are illustrated in Fig. 2, and the
(Fig. 2). DHSP was equipped with a low-cost Septentrio
keycharacteristicsofallGNSSdatasetsaresummarizedin
mosaic-X5 GNSS device, while SEPT employed a high-
Table3.
grade Septentrio PolaRx5TR GNSS device. Notably, the
costofthemosaic-X5islessthan5.0%ofthePolaRx5TR,
enabling a direct evaluation of low-cost versus high-grade
3.2 ZTDandPWVreferencedata
hardwareforreal-timetroposphericsensingunderidentical
environmentalconditions.
Forvalidatingreal-timeZTDestimates,referenceZTDswere
Both conventional and refined PPP methods were used
generated using postprocessed PPP with ambiguity resolu-
toprocessthereal-timedatastreamsfromthetwostations.
tion(PPP-AR)appliedtothecollocatedPolaRx5TRreceiver.
Real-timeorbitandclockcorrectionswereobtainedfromtwo
These solutions were produced through the Canadian Spa-
sources:PPP-B2b,recordeddirectlybyGNSSreceivers,and
tial Reference System (CSRS) PPP-AR service (Banville
IGS-RTS,providedbytheWuhanUniversityAnalysisCen-
et al. 2021), which uses postprocessed precise orbit, clock,
ter,amajorcontributortotheIGS-RTS.Thisconfiguration
and phase-bias products from Natural Resources Canada
allows a systematic comparison of PPP-B2b and IGS-RTS
(NRCan).
performancewithintherefinedPPPframework.
For the validation of oceanic PWV estimates, PWV
Twodatasetswereutilized:
derived from the ERA5 reanalysis was used as the pri-
mary reference. Additionally, during Cruise 1, the vessel
passed within 45 km of the Qingdao radiosonde station
1. Dataset 1 (June 20-July 6, 2025): Used for comparing
(ID 54857) at 00:00 UTC on September 25, 2023. PWV
PPP-B2b and IGS-RTS performance in real-time tro-
derivedfromthisradiosonde,verticallyadjustedtotheGNSS
pospheric estimation, and for benchmarking low-cost
antenna height, was incorporated as an independent refer-
versushigh-gradereceivers.
ence.
2. Dataset2(March27-April26,2025):Usedtoassessthe
To ensure the reliability, only converged real-time PPP
refinedPPPmethodunderbothstaticandkinematicPPP
estimateswereusedinthevalidationanalyses.Collectively,
configurationsusingPPP-B2bcorrections.
thesereferencedatasetsenablearigorousassessmentofreal-
time ZTD and PWV sensing performance using PPP-B2b
correctionsacrossboththeland-basedandoceanicscenarios.
123

<!-- PAGE: 7 -->

Real-timeoceanicPWVsensingusingBeiDou-3 Page 7 of 17 19
Fig.2 Locationsofthe
land-basedGNSSstations
(DHSPwithlow-costGNSS
device,redtriangle;SEPTwith
high-gradeGNSSdevice,blue
dot)andtheradiosondestation
(ID54857,redpentagram),
alongsidethetrajectoriesofthe
twoshipborneexperiments
(Cruise1andCruise2).The
DHSPandSEPTstationsare
collocated
Table3 CharacteristicsoftheGNSSdata
Scenario Stations GNSSreceiver Real-timecorrections Timeperiod Nearbyhigh-gradereceiver
/Cruises
Land-based SEPT PolaRx5TR PPP-B2b/IGS-RTS June20-July6,2025 None
DHSP Mosaic-×5(low-cost) PPP-B2b/IGS-RTS March27-April26,2025; PolaRx5TR
June20-July5,2025
Oceanic Cruise1 Mosaic-×5(low-cost) PPP-B2b September21–25,2023 PolaRx5TR
Cruise2 Mosaic-×5(low-cost) PPP-B2b August20,2024 PolaRx5TR
4 Resultsanddiscussion and stability of the IGS-RTS products. In contrast, PPP-
B2b-basedZTDestimatesdisplaylargerandmorefrequent
4.1 Conventionalreal-timeZTDestimationusing discrepancies,consistentwiththecomparativelyloweraccu-
PPP-B2bandIGS-RTS racy and stronger temporal noise of PPP-B2b corrections.
TheseresultsclearlyindicatethattheconventionalPPPstrat-
To motivate the development of a refined PPP strategy, we egy is more sensitive to correction errors, underscoring the
firstassesstheperformanceofPPP-B2bandIGS-RTSincon- necessityofarefinedPPPmethodforrobustreal-timeZTD
ventional real-time ZTD estimation. Real-time GNSS data estimationunderlower-accuracycorrectionconditionssuch
streamsfromtheDHSPstationwereprocessedinstaticPPP asPPP-B2b.
mode using the conventional PPP method, with real-time
orbit and clock corrections provided by both PPP-B2b and 4.2 Land-basedvalidationoftherefinedPPP
IGS-RTS.Figure3showstheresulting72hZTDtimeseries method
during a period characterized by pronounced tropospheric
variability.
Two land-based experiments were conducted to evaluate
AsshowninFig.3,real-timeZTDestimatesderivedfrom
therefinedPPPmethodacrossdifferentcorrectionsources,
bothcorrectionsourcesdeviatefromthereferences,reflect-
receivergrades,andprocessingmodes:
ing the limitations of real-time orbit and clock products.
Nevertheless,ZTDsobtainedusingIGS-RTSexhibitconsis-
1 Experiment 1: A 16-day dataset from both the low-cost
tentlysmallerdeviations,attributabletothehigheraccuracy
DHSPstationandhigh-gradeSEPTstationwasprocessed
usingPPP-B2bandIGS-RTScorrectionsinstaticmode.
123

<!-- PAGE: 8 -->

19 Page 8 of 17 H.Zhangetal.
Fig.3 Time-seriescomparisonof
real-timeZTDsestimatedatthe
DHSPstationusingPPP-B2b
(red)andIGS-RTS(blue)
correctionsbasedonthe
conventionalPPPmethod.
PostprocessedCSRSPPP-AR
ZTDsfromthecollocated
high-gradeSEPTstationserveas
reference.RMSstatistics
quantifydiscrepanciesrelativeto
thereference
ThegoalwastoexaminetherefinedPPPmethodacross ofZTDestimation,whereasexcessivenoiseamplifiesambi-
bothcorrectionsourcesandreceivergrades. guity variability and degrades parameter estimation. This
2 Experiment 2: A 30-day dataset from the DHSP station highlights the existence of an optimal process-noise level.
was processed using PPP-B2b corrections in both static Third, the optimal process noise for PPP-B2b is notably
andkinematicmodes.Thegoalwastoexaminetherefined largerthanthatforIGS-RTS.Thisdifferencereflectsthedis-
PPPmethodacrossdifferentprocessingmodes. tinctqualityofthecorrectionproducts:PPP-B2bcorrections
exhibit larger errors and stronger temporal variability than
IGS-RTS, thereby requiring a higher level of process noise
toeffectivelyabsorbcorrection-inducederrors.
Figure 5 provides a detailed comparison of ZTD time
4.2.1 Experiment1:RefinedPPPwithPPP-B2bandIGS-RTS
seriesestimatedusingPPP-B2bandIGS-RTSwithboththe
forlow-costandhigh-gradereceivers
conventional and the optimal refined PPP method. The left
panel displays the ZTD time series and precipitations with
Figure 4 summarizes the RMS errors obtained from eight
statistical results of ZTD errors, including RMS, standard
processing schemes, where S0 represents the conventional
deviation (STDV) and bias, while the right panels present
PPPmethodandS1-S7correspondtorefinedPPPmethods
boxplotsofZTDerrorsforbothmethods.
employingprogressivelyincreasingambiguityprocess-noise
ThreekeyobservationsemergedfromFig.5:First,severe
levels.The16-dayevaluationperiodcoincidedwiththeEast
weather during the 16-day period introduced pronounced
Asianplumrainseason,characterizedbyintenseprecipita-
ZTD variability, yet both PPP-B2b and IGS-RTS ZTD
tionandrapidtroposphericfluctuations.
solutions captured short-term atmospheric fluctuations rea-
Three key observations can be drawn from Fig. 4. First,
sonablywell.Second,atafinerscale,PPP-B2bZTDsexhibit
acrossallschemesandcorrectionsources,RMSdifferences
visiblynoisierbehavior,particularlyundertheconventional
between DHSP and SEPT remain below 0.5 mm, demon-
scheme, reaffirming that IGS-RTS offers superior accuracy
strating that low-cost receivers can achieve ZTD accuracy
forreal-timetroposphericestimation.Third,therefinedPPP
comparabletohigh-gradeequipmentunderreal-timecondi-
methodimprovedZTDaccuracyforbothcorrectionsources,
tions. Second, for both PPP-B2b and IGS-RTS, ZTD RMS
reducing RMS errors by approximately 23% for PPP-B2b
errorsinitiallydecreaseandthenincreaseastheprocessnoise
and 10% for IGS-RTS. These improvements, visually sup-
assigned to ambiguity parameters grows. This pattern con-
ported by reduced error magnitudes and variability in the
firmsthecoreconceptoftherefinedmethod:introducinga
moderatelevelofambiguityprocessnoiseimprovesaccuracy
123

<!-- PAGE: 9 -->

Real-timeoceanicPWVsensingusingBeiDou-3 Page 9 of 17 19
Fig.4 RMSerrorsofreal-timeZTDestimatesforeightschemes(S0–S7)attheDHSP(low-cost)andSEPT(high-grade)stationsutilizingPPP-B2b
(red)andIGS-RTS(blue)real-timecorrections.PostprocessedCSRSPPP-ARZTDsserveasreferences
right-panelboxplots,confirmtheeffectivenessoftherefined fromSchemeS0tosubsequentschemes,reachaminimum,
method. andthenincrease,indicatinganoptimalprocessnoisewithin
theS1–S7rangeforeachmode.Notably,theoptimalprocess-
noiseleveldiffersbetweenstaticandkinematicmodes,with
4.2.2 Experiment2:Staticvs.kinematicperformanceusing
thekinematicmodefavoringasmallervalue.Thisdifference
PPP-B2b
isattributedtothedistincterrorabsorptionmechanisms.In
staticmode,thecoordinatesaretightlyconstrained,forcing
Unlike static GNSS stations, oceanic GNSS platforms typ-
the ambiguities to absorb most PPP-B2b correction errors,
ically operate in kinematic mode. To assess the refined
thusnecessitatingalagerprocessnoise.Incontrast,inkine-
PPP method in a kinematic mode, real-time GNSS data
matic mode, freely estimated coordinates partially absorb
streamsfromtheDHSPstation,collectedoveracontinuous
these errors, necessitating a smaller noise to avoid over-
30-day period from March 27 to April 26, 2025, were pro-
parameterizationandnoisepropagationintoZTDestimates.
cessedusingPPP-B2bcorrectionsinasimulatedkinematic
Figure 7 provides a detailed comparison of 30-day real-
mode, with static mode results included for comparison.
time ZTD time series derived from PPP-B2b corrections,
BothconventionalPPPmethodandrefinedPPPmethodwere
processedinstaticandkinematicmodesusingboththecon-
implemented.Figure6summarizestheRMSerrorsofreal-
ventionalPPPmethodandtherespectiveoptimalrefinedPPP
timeZTDestimatesoverthisperiodforbothmodes.
schemes.Theleftpanels(a,c)presenttheZTDtimeseries
AnalysisofFig.6revealsfollowingkeyfindings.Across
alongside error statistics, including RMS, STDV, and bias,
all schemes, the kinematic mode consistently yields higher
whiletherightpanels(b,d)displayboxplotsofZTDerrors
RMS errors than static mode, as expected, due to the addi-
forbothmethods.Theresultshighlightthatkinematic-mode
tional uncertainty introduced by estimating time-varying
ZTDtimeseriesexhibitgreatervariabilityandnoiserelative
receivercoordinatesinkinematicsolutions.Acleartrendis
observedinbothmodes:ZTDRMSerrorsinitiallydecrease
123

<!-- PAGE: 10 -->

19 Page 10 of 17 H.Zhangetal.
Fig.5 ComparisonofPPP-B2bandIGS-RTSZTDtimeseriesusingtheconventionalmethodandtheoptimalrefinedmethod.Left:ZTDtime
series,precipitation,anderrorstatistics(RMS,STDV,bias).Right:boxplotsofZTDerrors
Fig.6 RMSerrorsofreal-time
ZTDestimatesforeight
processingschemes(S0–S7)at
DHSPstation,utilizingPPP-B2b
inbothstaticandkinematic
modes.PostprocessedZTD
solutionsfromCSRSPPP-AR
servedasthereference
123

<!-- PAGE: 11 -->

Real-timeoceanicPWVsensingusingBeiDou-3 Page 11 of 17 19
Fig.7 Comparisonof30-dayZTDtimeseriesfromstaticandkinematicPPPusingconventionalandoptimalrefinedmethods.Left:ZTDtime
seriesanderrorstatistics.Right:boxplotsofZTDerrors
tostaticmode.Nevertheless,therefinedPPPmethodconsis- environments.Second,therefinedschemes(S1–S4)demon-
tently outperforms the conventional method in both modes strateclearsensitivitytotheambiguityprocess-noisesetting
by suppressing noise and improving agreement with the andconsistentlyoutperformS0,confirmingthatintroducing
references. In kinematic mode, the optimal refined method amoderatelevelofprocessnoiseisessentialforimproving
reducestheRMSerrorfrom13.0mm(conventionalPPP)to ZTD estimation in oceanic environments. Third, the opti-
9.9mm,correspondingtoa24%improvement.Theseresults mal process-noise level observed in Cruise 1 is consistent
demonstratethattherefinedPPPmethodiseffectivenotonly withthatobtainedfromtheland-basedexperiments,demon-
forstaticmodebutalsoforkinematicmode. stratingtherobustnessoftherefinedmethodacrossdifferent
platformsandatmosphericconditions.
To further evaluate the refined method for real-time
4.3 Oceanicvalidationofreal-timePWVsensing
oceanic PWV sensing, we retrieved PWVs from the real-
withrefinedPPPmethod
time ZTDs estimated by the conventional method (S0) and
theoptimalrefinedmethod(S3).Figure9presentstheresult-
Intheoceanicscenario,real-timeGNSSdatastreamsfrom
ingreal-timePWVtimeseriesduringCruise1overthesame
a shipborne low-cost GNSS device were processed in a
21h(Fig.9a)and60h(Fig.9b)periods.PWVsderivedfrom
true real-time kinematic mode during two research cruises.
ERA5andradiosondemeasurementsareusedasreferences.
Figure 8 presents the real-time ZTDs estimated by the five
The error bars for PWV values obtained from S0 and S3,
schemes (S0-S4) during Cruise 1, covering two represen-
comparedtoERA5-PWV,arepresentedin(c).
tative periods of 21 h (Fig. 8a) and 60 h (Fig. 8b). The
Analysis of Fig. 9 reveals that although the conven-
corresponding RMS and bias statistics of ZTD errors are
tional and refined methods capture similar temporal PWV
summarizedinFig.8c,d.
variations,therefinedmethodyieldssignificantlyimproved
Three key observations can be made from Fig. 8. First,
agreementwiththereferences.Overbothperiods,therefined
in the shipborne experiment, ZTDs from the conventional
method reduces the PWV RMS error from 3.7 mm (con-
method (S0) exhibit greater noise compared to the refined
ventional PPP) to 2.5 mm, corresponding to an accuracy
methods (S1–S4), highlighting the limitations of conven-
improvement exceeding 30%. For example, at 00:00 on
tionalPPPforreal-timeZTDestimationinoceanickinematic
123

<!-- PAGE: 12 -->

19 Page 12 of 17 H.Zhangetal.
Fig.8 TimeseriesofZTDestimatedbyfiveschemesduringCruise1 CSRSPPP-ARZTDsolutionsfromnearbyhigh-gradeGNSSdevices
overtwoperiods:21h(a)and60h,(b)startingat03:00onSeptember areshownasreferences(ingray).RMSandbiasstatisticsofZTDerrors
24,2023and00:00onSeptember21,2023,respectively.Postprocessed areshownin(c,d)
September 25, 2023, the conventional method exhibits a achievinganRMSof11.9mm,whichrepresentsanimprove-
PWVerrorofapproximately2.0mmrelativetobothERA5 mentofmorethan61%relativetotheconventionalmethod.
and radiosonde measurements, whereas the refined method Similarly, for real-time PWV, the refined method produces
reducesthiserrortoapproximately0.1mm,clearlydemon- estimates that closely follow ERA5-derived values in both
stratingitseffectiveness. magnitude and variability, reducing RMS error from 6.2 to
Figure 10 presents the real-time ZTD and PWV solu- 3.3mm,correspondingtoa47%improvement.Theseresults
tions obtained during Cruise 2. For the real-time ZTD, the collectivelydemonstratetherobustnessandsuperiorperfor-
refinedmethodexhibitscloseralignmentwiththereferences, mance of the refined PPP method for real-time ZTD and
PWVsensinginoceanicenvironments.
123

<!-- PAGE: 13 -->

Real-timeoceanicPWVsensingusingBeiDou-3 Page 13 of 17 19
Fig.9 Comparativetimeseriesofreal-timePWVover21h(a)and60h andradiosondemeasurementsserveasreferences.Statisticalresultsof
(b)duringCruise1,retrievedusingtheconventionalmethod(S0)and PWVerrorsofS0andS3arepresented.PWVerrorstatisticsforS0and
the optimal refined method (S3), starting at 03:00 on September 24, S3relativetoERA5areshownin(c)
2023and00:00onSeptember21,2023,respectively.PWVfromERA5
5 Conclusions modes,theoptimalstochasticsettingsdiffer:instaticmode,
a larger process noise assigned to ambiguities yields up to
This study presents a practical and cost-effective frame- a 34% improvement in ZTD accuracy, while in kinematic
work for real-time oceanic PWV sensing by integrating mode,theimprovementreachesapproximately24%witha
BeiDou’s satellite-based PPP-B2b service with a low-cost moremoderatesetting.Therefinedmethodalsoprovesadapt-
GNSS receiver. To address the inherent errors in PPP-B2b able to IGS-RTS corrections, yielding an ~ 10% accuracy
orbit and clock corrections, a refined PPP method based improvement in real-time ZTD estimation, although opti-
on ambiguity reparameterization and optimized stochastic malsettingsdifferduetothedifferenterrorcharacteristicsof
modeling is developed. By allowing ambiguity parameters PPP-B2bandIGS-RTScorrections.Inoceanicexperiments,
toadaptivelyabsorbreal-timecorrectionerrors,therefined the refined method improves real-time oceanic PWV sens-
methodsignificantlyimprovestheaccuracyoftropospheric ingaccuracybyover30%duringCruise1and47%during
estimation. Experiments demonstrate that the refined PPP Cruise2,comparedtoconventionalPPPmethod.
method,whenappliedwithalow-costreceiver,achievesZTD A key advantage of the refined PPP method is its
accuracycomparabletohigh-gradereceiverswhilesubstan- simplicity: it retains full compatibility with the conven-
tiallyreducinghardwarecosts,addressingbothprecisionand tional PPP framework and requires only an adjustment to
cost-effectiveness. the ambiguity process-noise setting, without any modifi-
Comprehensiveland-basedandoceanicexperimentscon- cation to the observation equations or parameterization.
firm the robustness of the proposed method. In land-based This ease of implementation, coupled with demonstrated
scenarios, the refined PPP method consistently improves performance improvements, underscores its potential for
real-timeZTDestimationinbothstaticandkinematicmodes. wide-scaledeploymentincost-effectiveoceanictropospheric
Owing to the different degrees of freedom in these two sensing. Ongoing efforts aim to integrate these capabilities
123

<!-- PAGE: 14 -->

19 Page 14 of 17 H.Zhangetal.
Fig.10 Timeseriesofreal-timeZTD(a)andPWV,(b)obtainedusing PPP-B2b-derivedreal-timeZTDandPWVareshown.Postprocessed
theconventionalmethod(S0)andtheoptimalrefinedmethod(S3)dur- CSRSPPP-ARZTDsandERA5-derivedPWVsareusedasreferences
ingCruise2,from00:00to24:00onAugust20,2024.RMSerrorsof
withBeiDou’ssatellite-basedshort-messagecommunication Tofurtherenhancethegeneralityoftheevaluation,anew
service,enabling directtransmissionofoceanic PWVs and GNSSstation(GZSP)locatedinGuangzhou,approximately
furtherenhancingreal-timemonitoringcapabilities. 1000 km from the DHSP station in Wuhan and exhibiting
distinctgeographicandclimaticcharacteristics,wasincluded
intheanalysis.Sixconsecutivedaysofreal-timedatastreams
AppendixAEquivalenceofthe Es-absorbed (November11–16,2025)wereprocessedinstaticPPPmode,
r
and Es-estimatedmethods. withpostprocessedCSRSPPP-ARZTDsolutionsservingas
r
thereference.TheresultsareshowninFig.11.
To directly assess whether the proposed ambiguity-based Acrossthe13testedschemes,bothmethodsexhibitcon-
Es absorptionstrategyisequivalenttoexplicitlyestimating sistent sensitivity patterns: the ZTD RMS errors initially
r
Es parameters, we conducted an additional experiment in decrease as the process noise increases, reach a minimum,
r
whichsatellite-specificEstermswereintroducedasrandom- andthenincreaseoncethenoiseexceedstheoptimallevel.
r
walkstatesinthereal-timePPP.For afaircomparison,the Notably, the two methods attain their optimal performance
Es-estimatedmethodusedthesameprocess-noiseconfigura- atnearly √ thesameprocess-noiserange(approximately12~
r
tionsemployedinthe E r s-absorbedmethod.Inaddition,the 15 mm/ h). Compared with the E r s-estimated method, the
ambiguity process-noise grid was densified, expanding the E r s-absorbed method shows higher sensitivity to process-
number of schemes from 8 to 13, thereby enabling a more noise variations beyond its optimal value and reaches its
precisecharacterizationofperformancevariationsaroundthe optimumataslightlysmallernoiselevel.Nevertheless,the
optimalnoiselevel. ZTDaccuracyachievedateachmethod’srespectiveoptimum
123

<!-- PAGE: 15 -->

Real-timeoceanicPWVsensingusingBeiDou-3 Page 15 of 17 19
Fig.11 (a)ComparisonofPPP-B2b-derivedreal-timeZTDtimeseries methodsacrossall13ambiguityprocess-noiseschemes.CSRSPPP-AR
overaconsecutive144-hperiodestimatedwithconventionalmethod ZTDsolutionsareusedasreferences
(S0),Es-absorbedmethod(S4)andEs-estimatedmethod(S4).(b)Sta-
r r
tisticalcomparisonofZTDerrorsfortheEs-absorbedandEs-estimated
r r
isessentiallyequivalent.Theseresultsconfirmthatthe Es- results;allauthorsreviewedthemanuscriptandcontributedindividually
r
absorbedmethoddeliversaccuracycomparabletothemore tothewriting.
complex Es-estimatedmethod,whilemaintainingasimpler
r Funding This work was funded by National Natural Science Foun-
modelstructureandsignificantlylowercomputationalcost.
dation of China, 42274043, Hongxing Zhang, Wuhan Natural Sci-
enceFoundationExplorationProgram,2024040801020244,Hongxing
Acknowledgements ThisworkwassupportedbytheNationalNatu-
Zhang. The National Key Research &amp; Development Program,
ralScienceFoundationofChina(No.42274043),theWuhanNatural
2023YFA1009100,HongxingZhang.
ScienceFoundationExplorationProgram(ChenGuangProgram,No.
2024040801020244), and the marine data from scientific innovation
Dataavailability TheERA5hourlydataareavailablefromtheCoper-
projectundertheWenhaiPlan(LSKJ202205100).Thefirstauthorwas
nicus Climate Data Store at https://doi.org/10.24381/cds.bd0915c6.
supportedbytheWuhanTalentsPlan(2023).
The radiosonde data are available from Weather Data for Wyoming
athttp://weather.uwyo.edu/upperair/bufrraob.shtml.NaturalResources
Authorcontributions HXZproposedthegeneralidea;HXZ,YBY,and
Canada’sCanadianSpatialReferenceSystem(CSRS)PPP Webser-
LHLdiscussedthemethodology;HXZandLHLdevelopedthesoftware
viceisavailableathttps://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/to
andpreparedthedraftmanuscript.WLandYBYreviewedandimproved
ols-outils/ppp.php(Banvilleetal.2021).Thereal-timeIGS-RTSGNSS
themanuscript;LHL,WJH,YJC,andDRcollectedandanalyzedthe
precisesatelliteorbitandclockcorrectionstreamscanbeobtainedfrom
https://igs.org/rts/.
123

<!-- PAGE: 16 -->

19 Page 16 of 17 H.Zhangetal.
References MännelB,ZusF,DickG,GlaserS,SemmlingM,BalidakisK,Wickert
J,MaturilliM,DahlkeS,SchuhH(2021)GNSS-basedwatervapor
BanvilleS,HassenE,LamotheP,FarinaccioJ,DonahueB,Mireault estimationandvalidationduringtheMOSAiCexpedition.Atmos
Y,GoudarziMA,CollinsP,Ghoddousi-FardR,KamaliO(2021) MeasTech14:5127–5138
EnablingambiguityresolutioninCSRS-PPP.NAVIGJInstNavig MarutG,HadasT,KaplonJ,TrzcinaE,RohmW(2022)Monitoring
68:433–451 thewatervaporcontentathighspatio-temporalresolutionusing
BevisM,BusingerS,HerringTA,RockenC,AnthesRA,WareRH anetworkoflow-costmulti-GNSSreceivers.IEEETransGeosci
(1992) GPS meteorology: remote sensing of atmospheric water RemoteSens60:1–14
vaporusingtheglobalpositioningsystem.JGeophysResAtmos NaciriN,YiD,BisnathS,deBlasFJ,CapuaR(2023)Assessmentof
97:15787–15801.https://doi.org/10.1029/92JD01517 Galileohighaccuracyservice(HAS)testsignalsandpreliminary
CarlinL,HauschildA,MontenbruckO(2021)Precisepointpositioning positioningperformance.GPSSolut27(2):73
withGPSandGalileobroadcastephemerides.GPSSolut25:77. PanL,YangC(2025)BDS-3PPP-B2bandGalileoHAStightlyinte-
https://doi.org/10.1007/s10291-021-01111-4 gratedreal-timePPP.GPSSolut29:162.https://doi.org/10.1007/
Chadwell CD, Bock Y (2001) Direct estimation of absolute precip- s10291-025-01925-6
itablewaterinoceanicregionsbyGPStrackingofacoastalbuoy. PanL,DengM,ChenB(2024)Real-timeGNSSmeteorology:apromis-
GeophysResLett28:3701–3704 ingalternativeusingreal-timePPPtechniquebasedonbroadcast
ChenG,HerringTA(1997)Effectsofatmosphericazimuthalasym- ephemeridesandtheopenserviceofGalileo.GPSSolut28:113.
metry on the analysis of space geodetic data. J Geophys Res https://doi.org/10.1007/s10291-024-01659-x
102(B9):20489–20502 RebischungP,SchmidR(2016)IGS14/igs14atxanewframeworkfor
ChenG,WeiN,LiM,ZhaoQ,ZhangJ(2022)BDS-3andGPS/Galileo theIGSproducts.AGUFallMeeting.SanFrancisco
integratedPPPusingbroadcastephemerides.GPSSolut26:129. Rocken C, Johnson J, Van Hove T, Iwabuchi T (2005) Atmospheric
https://doi.org/10.1007/s10291-022-01311-6 watervaporandgeoidmeasurementsintheopenoceanwithGPS.
DuJ,KimballJS,JonesLA(2014)Satellitemicrowaveretrievaloftotal GeophysResLett.https://doi.org/10.1029/2005GL022573
precipitablewatervaporandsurfaceairtemperatureoverlandfrom SchmittRW(1995)Theoceancomponentoftheglobalwatercycle.
AMSR2.IEEETransGeosciRemoteSens53:2520–2531 RevGeophys33:1395–1409
FujitaM,KimuraF,YoneyamaK,YoshizakiM(2008)Verificationof Schneider T, O’Gorman PA, Levine XJ (2010) Water vapor and the
precipitablewatervaporestimatedfromshipborneGPSmeasure- dynamics of climate changes. Rev Geophys. https://doi.org/10.
ments.GeophysResLett.https://doi.org/10.1029/2008gl033764 1029/2009RG000302
Gao BC, Kaufman YJ (2003) Water vapor retrievals using moder- Shoji Y,Sato K, Yabuki M, Tsuda T(2016) PWV retrieval over the
ateresolutionimagingspectroradiometer(MODIS)near-infrared oceanusingshipborneGNSSreceiverswithMADOCAreal-time
channels.JGeophysRes:Atmos108:13 orbits.SOLA12:265–271
GongY,LiuZ,FosterJH(2021)Evaluatingtheaccuracyofsatellite- TangC,HuX,ChenJ,LiuL,ZhouS,GuoR,LiX,HeF,LiuJ,Yang
based microwave radiometer PWV products using shipborne J(2022)Orbitdetermination,clockestimationandperformance
GNSSobservationsacrossthePacificOcean.IEEETransGeosci evaluationofBDS-3PPP-B2bservice.JGeod96:60
RemoteSens60:1–10 Tao J, Zhang G, Chen G, Jiang Y, Zhao Q (2025) Real-time esti-
Gunning K, Blanch J, Walter T (2019) SBAS corrections for PPP mationofmulti-frequencyphaseobservable-specificbiasforthe
integritywithsolutionseparation.In:ProceedingsoftheIONITM, BDS3PPP-B2bservice.GPSSolut29:19.https://doi.org/10.1007/
RestonInstituteofNavigation.USA,707–719. s10291-024-01776-7
HadasT,HobigerT,HordyniecP(2020)Consideringdifferentrecent Wang J, Wu Z, Semmling M, Zus F, Gerland S, Ramatschi M, Ge
advancementsinGNSSonreal-timezenithtroposphereestimates. M, Wickert J, Schuh H (2019) Retrieving precipitable water
GPSSolut24(4):99 vaporfromshipbornemulti-GNSSobservations.GeophysResLett
HeJ,LiuZ(2019)Comparisonofsatellite-derivedprecipitablewater 46:5000–5008
vaporthroughnear-infraredremotesensingchannels.IEEETrans Wei J, Shu Y, Liu Y, Fang R, Qiao L, Ding D, Li G, Liu J (2023)
GeosciRemoteSens57:10252–10262 Retrieving accurate precipitable water vapor based on GNSS
HuangL,MoZ,XieS,LiuL,ChenJ,KangC,WangS(2021)Spa- multi-antennaPPPwithanocean-baseddynamicexperiment.Geo-
tiotemporal characteristics of GNSS-derived precipitable water physResLett50:e2023GL102982
vaporduringheavyrainfalleventsinGuilin,China.SatellNavig Wei H, Xiao G, Zhou P, Li P, Xiao Z, Zhang B (2025) Combining
2(1):13 GalileoHASandBeidouPPP-B2bwithHelmertcoordinatetrans-
JiR,JiangX,ChenX,ZhuH,GeM,NeitzelF(2023)Qualitymon- formation method. GPS Solut 29:35. https://doi.org/10.1007/s1
itoring of real-time GNSS precise positioning service system. 0291-024-01789-2
Geo-SpatialInfSci26:1–15 WuJ,WuS,HajjG,BertigerW,LichtenS(1993)Effectsofantenna
Jiang N, Wu Y, Li S, Xu Y, Wang Y, Xu T (2024) First PWV orientationonGPScarrierphase.ManuscrGeod18(2):91–98
retrieval using MERSI-LL onboard FY-3E and cross validation WuZ,LuC,LyuH,HanX,ZhengY,LiuY,LiuY,JinK(2022)Sensing
withco-platformoccultationandgroundGNSS.GeophysResLett real-timewatervaporoveroceanswithlow-costGNSSreceivers.
51:e2024GL108681 IEEETransGeosciRemoteSens60:1–8
LeeS-W,KoubaJ,SchutzB,KimDH,LeeYJ(2013)Monitoringpre- Xu J, Liu Z (2024) A novel machine learning-based approach for
cipitablewatervaporinreal-timeusingglobalnavigationsatellite improvingglobalcorrectionofAIRS-derivedwatervaporsatel-
systems.JGeod87:923–934 liteproduct.IntJApplEarthObsGeoinf128:103787
LiX,DickG,GeM,HeiseS,WickertJ,BenderM(2014)Real-time XuX,NieZ,WangZ,ZhangY,DongL(2023)AnimprovedBDS-3
GPSsensingofatmosphericwatervapor:precisepointpositioning PPP-B2bpositioningapproachbyestimatingsignalinspacerange
withorbit,clock,andphasedelaycorrections.GeophysResLett errors.GPSSolut27:110
41:3615–3621 YangY,GaoW,GuoS,MaoY,YangY(2019)IntroductiontoBeiDou-3
LuC,LiX,NilssonT,NingT,HeinkelmannR,GeM,GlaserS,Schuh navigationsatellitesystem.Navigation66:7–18
H(2015)Real-timeretrievalofprecipitablewatervaporfromGPS YangH,HeX,FerreiraV,JiS,XuY,SongS(2023)Assessmentof
andBeiDouobservations.JGeod89:843–856 precipitablewatervaporretrievedfromprecisepointpositioning
123

<!-- PAGE: 17 -->

Real-timeoceanicPWVsensingusingBeiDou-3 Page 17 of 17 19
withPPP-B2bservice.EarthSciInf16:315–328.https://doi.org/
10.1007/s12145-023-00939-3
YuanY,ZhangK,RohmW,ChoyS,NormanR,WangCS(2014)Real-
timeretrievalofprecipitablewatervaporfromGPSprecisepoint
positioning.JGeophysResAtmos119:10044–10057
Zheng Y, Lu C, Wu Z, Liao J, Zhang Y, Wang Q (2022) Machine
learning-basedmodelforreal-timeGNSSprecipitablewatervapor
sensing.GeophysResLett49:e2021GL096408
ZhouP,ZhangZ,LiuZ,LyuD,XiaoG,XiaoK,DuL(2024)Real-time
precisezenithtroposphericdelayestimationwithBDSPPP-B2b,
Galileo HAS, and QZSS MADOCA-PPP services. IEEE Trans
GeosciRemoteSens.https://doi.org/10.1109/tgrs.2024.3443884
SpringerNatureoritslicensor(e.g.asocietyorotherpartner)holds
exclusiverightstothisarticleunderapublishingagreementwiththe
author(s)orotherrightsholder(s);authorself-archivingoftheaccepted
manuscriptversionofthisarticleissolelygovernedbythetermsofsuch
publishingagreementandapplicablelaw.
123