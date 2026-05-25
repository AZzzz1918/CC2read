<!-- PAGE: 1 -->

remote sensing
Article
Initial Assessment of BDS PPP-B2b Service: Precision of Orbit
and Clock Corrections, and PPP Performance
ZhixiNie1 ,XiaofeiXu1,* ,ZhenjieWang1 andJunDu2
1 CollegeofOceanographyandSpaceInformatics,ChinaUniversityofPetroleum,Qingdao266580,China;
niezhixi@upc.edu.cn(Z.N.);sdwzj@upc.edu.cn(Z.W.)
2 QingdaoShihuaCrudeOilTerminal,QingdaoPort,Qingdao266500,China;Duj.sh@qdport.com
* Correspondence:b19010058@s.upc.edu.cn
Abstract: On 31 July 2020, the Beidou global navigation satellite system (BDS-3) was officially
announced as being commissioned. In addition to offering global positioning, navigation, and
timing(PNT)services,BDS-3alsoprovidesprecisepointpositioning(PPP)augmentationservices.
Thesatelliteorbitcorrection,clockcorrectionandcodebiascorrectionofBDS-3andotherglobal
navigationsatellitesystems(GNSS)arebroadcastbytheBDS-3geostationaryearthorbit(GEO)
satellitesthroughthePPP-B2bsignal. ThePPP-B2bserviceisavailableforusersinChinaandthe
surrounding area. In this study, an initial assessment of the PPP-B2b service is presented, with
collected 3-day PPP-B2b messages. Based on broadcast ephemeris and PPP-B2b messages, the
precisesatelliteorbitsandclockoffsetscanberecovered.Thisprecisionisevaluatedwiththeprecise
ephemeris from the GeoForschungsZentrum Potsdam (GFZ) analysis center as references. The
resultsindicatethattheaccuracyofBDS-3satelliteorbitsinthedirectionofradial,along-track,and
(cid:1)(cid:2)(cid:3)(cid:1)(cid:4)(cid:5)(cid:6)(cid:7)(cid:8)(cid:1)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:6)(cid:7) cross-trackis0.138,0.131,and0.145m,respectively,andforGPSacorrespondingaccuracyof0.104,
0.160,and0.134m,respectively,couldbeobtained.Theprecisionofclockoffsetscanreachalevel
Citation: Nie,Z.;Xu,X.;Wang,Z.;
ofseveralcentimetersforbothGPSandBDS-3.BoththeperformanceofstaticPPPandkinematic
Du,J.InitialAssessmentofBDS
PPPareevaluatedusingtheobservationsfromfourinternationalGNSSmonitoringassessment
PPP-B2bService:PrecisionofOrbit
service(iGMAS)stations.RegardingstaticPPP,theaverageconvergencetimeis17.7mintoachieve
andClockCorrections,andPPP
Performance.RemoteSens.2021,13, ahorizontalpositioningaccuracyofbetterthan0.3m,andaverticalpositioningaccuracyofbetter
2050. https://doi.org/10.3390/ than0.6m.Theaveragepositioningaccuracyinthedirectionofeast,north,andup-directionsare2.4,
rs13112050 1.6,and2.3cm.AstokinematicPPP,theaverageRMSvaluesofpositioningerrorsinthedirectionof
east,north,andupare8.1cm,3.6cm,and8.0cmafterfullconvergence.
AcademicEditors:JoséFernández
andAliKhenchaf Keywords:GNSS;BDS-3;PPP-B2b;orbitcorrection;clockcorrection
Received:13April2021
Accepted:19May2021
Published:22May2021
1. Introduction
TheBeidounavigationsatellitesystem(BDS)wasindependentlydevelopedbyChina
Publisher’sNote:MDPIstaysneutral
toprovidepositioning,navigation,andtiming(PNT)services[1,2]. Athree-phasestrategy
withregardtojurisdictionalclaimsin
hasbeenadoptedinthebuild-upofBDS,includingtheBeidoudemonstrationnavigation
publishedmapsandinstitutionalaffil-
satellitesystem(BDS-1),Beidouregionalnavigationsatellitesystem(BDS-2),andBeidou
iations.
globalnavigationsatellitesystem(BDS-3). BDS-1andBDS-2havebeenputintousein2000
and2012,respectively[3,4],whiletheconstructionofBDS-3wasinitiatedinNovember
2017[5]. BytheendofJune2020,thewholeconstellationofBDS-3wascompleted,consist-
ingof24mediumearthorbit(MEO)satellites,3geostationaryearthorbit(GEO)satellites,
Copyright: © 2021 by the authors.
and3inclinedgeosynchronousorbit(IGSO)satellites. On31July2020,theBDS-3system
Licensee MDPI, Basel, Switzerland.
was officially announced as being commissioned. BDS-3 can offer PNT, short message
This article is an open access article
communication(SMC),andinternationalsearchandrescue(SAR)services. Besidesthe
distributed under the terms and
aboveservices,BDS-3alsoprovidesaprecisepointpositioning(PPP)service[6,7].
conditionsoftheCreativeCommons
PPPisacrucialhigh-precisionglobalnavigationsatellitesystem(GNSS)positioning
Attribution(CCBY)license(https://
technology[8–10]. Itcanprovidedecimeter-levelorevencentimeter-levelpositioningaccu-
creativecommons.org/licenses/by/
4.0/). racywithastandaloneGNSSreceiver,byutilizingpreciseephemerisproducts. Inthepast
RemoteSens.2021,13,2050.https://doi.org/10.3390/rs13112050 https://www.mdpi.com/journal/remotesensing

<!-- PAGE: 2 -->

RemoteSens.2021,13,2050 2of19
decades,PPPtechniqueshavebeenwidelyusedforapplicationsinoceanography[11–13],
geoscience[14,15]andmeteorology[16–18],andprecisionagriculture[19],etc. Theinter-
nationalGNSSservice(IGS)hasbeenofferingreal-timeservice(RTS)throughtheinternet
since 2013 [20,21]. By adopting RTS products, the users can realize the real-time PPP
application. However,thisservicedependsonastandinginternetaccess. Inadditionto
theserviceofferedviainternetcommunication,asatellitebroadcastingservicehasalso
beenreleasedbysomecommercialcompanieswithahigh-costfee,suchasStarFixfrom
Furgo [22], StarFire from NavCom [23], and RTX from Trimble [24]. Additionally, PPP
augmentationservicesbasedonthebasicGNSSconstellationhavealsobeendeveloped.
TheJapaneseQuasi-ZenithSatelliteSystem(QZSS)providesacentimeter-levelaccuracy
augmentationservice(CLAS)forusersinJapan[25,26]. TheEuropeanGalileoconstellation
is also designed to provide a high-precision PPP service worldwide, with an enabled
positioningaccuracyatdecimeter-level[27,28].
BDS-3 is designed to provide a PPP augmentation service, which is an important
innovation for BDS [29]. The satellite orbit correction, clock correction and code bias
correctionofBDS-3/GPS/GLONASS/GALILEOaresupposedtobebroadcastbyBDS-3
GEOsatellitesthroughthePPP-B2bsignal. However,thePPP-B2bserviceonlyprovides
corrections of BDS-3 and GPS satellites at present, and the service is only available for
usersinandaroundChina. AccordingtothestructureofthePPP-B2bmessage,thesize
is486bitsforeachmessage,including6bitsofmessagetype,456bitsofmessagedata,
and24bitsofcycleredundancycheck(CRC).Thedurationofeachmessageis1s. The
messagetypeisdefinedtodistinguishthebroadcastcorrectioncontents. Tomatchwith
thecorrectioncontentsofdifferentmessagetypes,thecorrectiondataareidentifiedwitha
groupofissueofdata(IOD),includingtheissueofdataofspacestaterepresentation(IOD
SSR),issueofdataofpseudo-randomnoisemask(IODP),issueofdataoforbitandclock
correction(IODCorr),andissueofthenavigationdata(IODN).Themessagetypesandthe
correspondingcontentsaresummarizedinTable1[30].
Table1.Themessagetypesandtheircorrectioncontents.
MessageType CorrectionContent
1 Satellitemask
2 Satelliteorbitcorrectionanduserrangeaccuracy
3 Differentialcodebias
4 Satelliteclockcorrection
5 Userrangeaccuracyindex
6 Clockcorrectionandorbitcorrection–combination1
7 Clockcorrectionandorbitcorrection–combination2
8–62 Reserved
63 Null
Inthiscontribution,wecarryoutaninitialassessmentoftheBDSPPP-B2bservice
based on the collected 3-day message data. At first, the availability of PPP-B2b mes-
sagesisanalyzed. Then,theprecisionofPPP-B2borbitcorrectionandclockcorrections
areevaluatedwiththefinalprecisemulti-GNSSephemerisproductsobtainedfromthe
GeoForschungsZentrum Potsdam (GFZ) analysis center as references. Finally, the PPP
positioningperformanceinbothstaticandkinematicmodeisassessed,basedontheobser-
vationsfrom4internationalGNSSmonitoringassessmentservice(iGMAS)stations[31].
Theremainingcontributionisorganizedasfollows. InSection2,themethodtorecover
preciseorbitsandclockoffsetsfromthePPP-B2bmessagesisdescribed. Inaddition,the
strategytoevaluatetheprecisionofPPP-B2borbits/clockoffsets,andpositioningperfor-
mancewiththerecoveredPPP-B2borbits/clockoffsets,arealsointroduced. InSection3,
theprecisionoftherecoveredPPP-B2borbits/clockoffsetsareassessed,withGFZprecise
ephemerisasreference. Atthesametime,thepositioningperformanceisanalyzedbothin
staticandkinematicexperiments. Finally,severalconclusionsaredrawninthelastsection.

<!-- PAGE: 3 -->

RemoteSens.2021,13,2050 3of19
2. Methodology
Inthissection,firstly,themethodtocalculatepreciseorbitsandclockoffsetsbyusing
PPP-B2bcorrectionsispresented. Then,themethodtoevaluatetheprecisionofPPP-B2b
orbits and clock offsets is discussed. Finally, the PPP positioning model, based on the
recoveredPPP-B2borbitsandclockoffsets,isdescribed.
2.1. RecoveryofPreciseOrbitsandClockOffsetswithPPP-B2bCorrections
ThePPP-B2borbitcorrectionmessagecontainstheorbitcorrectionparameters(δO ,
radial
δO , δO )intheradial,along-track,andcross-trackdirections[30],whilethesatellite
along cross
positionscomputedwithbroadcastephemerisaregiveninthe“Earth-centerEarth-fixed”
(ECEF)frame. Hence,theorbitcorrectionsshouldbetransformedtotheECEFframe. This
transformationcanbeexpressedas:
   
δO δO
x radial
(cid:2) (cid:3)
 δO y  = e radial e along e cross · δO along  (1)
δO
z
δO
cross
(cid:2) (cid:3)T
where δO δO δO representstheorbitcorrectionvectorintheECEFframe,and:
x y z


e
e radia
=
l =
r×
| r r|
r .
cross |r×r .|

e =e ×e
along cross radial
.
rdenotesthesatellitepositionvectorandrstandsforthevelocityvector;botharecomputed
withbroadcastephemeris. Byapplyingthesatelliteorbitcorrectiontobroadcastsatellite
positions,theprecisesatellitepositionscanbecalculatedasfollows:
     
X X δO
x
 Y  =  Y  − δO y  (2)
Z Z δO
prec,B2b brdc z
(cid:2) (cid:3)T
where X Y Z denotestheprecisesatellitepositionvectorafterapplyingPPP-
prec,B2b
(cid:2) (cid:3)T
B2borbitcorrectionstothebroadcastorbits;and X Y Z representsthesatellite
brdc
positionvectorcalculatedwiththebroadcastephemeris. ItshouldbenotedthatIODNin
thePPP-B2bmessagemustmatchwiththecorrespondingfieldofbroadcastephemerisin
recoveringapreciseorbit.
ThePPP-B2bclockcorrectionmessagecontainsthecorrectionparameterrelativetothe
clockoffsetofbroadcastephemeris. Thecorrectedprecisesatelliteclockoffsetisgivenby:
C
dtsat = dtsat − 0 (3)
prec,B2b brdc c
where dtsat is the satellite clock offset derived from the broadcast ephemeris; dtsat
brdc prec,B2b
denotestheprecisePPP-B2bclockoffset;C isthePPP-B2bclockcorrectionparameter;and
0
cisthevelocityoflight.
2.2. AssessmentoftheRecoveredPPP-B2bOrbitsandClockOffsets
ThepreciseorbitsrecoveredwithPPP-B2bmessagesarereferredtotheantennaphase
center(APC),whiletheIGSpreciseproductsgivethecenter-of-mass(CoM)ofsatellites[32].
Therefore,thesatelliteAPCpositionsneedtobeconvertedtothesatelliteCoMpositions

<!-- PAGE: 4 -->

RemoteSens.2021,13,2050 4of19
byapplyingphasecenteroffset(PCO)corrections[33]. Nowtheorbitdifferencescanbe
computedas:
 ∆X   X    X 
 ∆Y  =   Y  +A·dr PCO   − Y  (4)
∆Z Z Z
prec,B2b prec,GFZ
where (cid:2) ∆X ∆Y ∆Z (cid:3)T standsfortheorbiterrorvectorinECEFCartesiancoordinates;
Adenotesthesatelliteattitudematrix;anddr representsthePCOcorrectionvectorfor
PCO
(cid:2) (cid:3)T
thesatellite. X Y Z denotestheprecisepositionvector,calculatedwithGFZ
prec,GFZ
finalproducts.
ThecalculatedorbiterrorscanbetransformedfromECEFCartesiancoordinatesto
thesatelliteradial,along-trackandcross-trackdirections:
 ∆O   ∆X 
radial
 ∆O along  = (cid:2) e radial e along e cross (cid:3) · ∆Y  (5)
∆O ∆Z
cross
where (cid:2) ∆O radial ∆O along ∆O cross (cid:3)T istheorbiterrorvectorinthesatelliteorbitalframe.
TheBDS-3PPP-B2bserviceadoptstheBeidoucoordinatesystem(BDCS)asareference
frame[34],whilethepreciseproductsfromIGSarereferredtotheIGS14frame[35]. In
ordertoeliminatethedifferencebetweenthesetworeferenceframesmentionedabove,a
Helmerttransformationshouldbeapplied.
Incontrasttoorbits,twodifferenttypesofclockoffsetproductscannotbecompared
directly. ThisisduetodifferencesinhardwaredelaysandGNSS-specifictimescales. The
hardwaredelayiscausedbydifferenttrackingmodes. Torealizethesynchronousprocess-
ingatdifferenttrackingmodes,acorrespondingdifferentialcodebias(DCB)correction
needstobeapplied. Thecorrectionalgorithmformulaisshownbelow[30]:
(cid:101)l
sig
= l
sig
−DCB
sig
(6)
where(cid:101)l
sig
isthevalueofsigsignal;l
sig
representstheobservedclockoffset;and DCB
sig
denotestherelatedDCBvalue.
AftertheapplicationofDCBs,thedifferencesbetweentheGNSS-specifictime-scales
mustalsobeeliminated[36]. Typically,adouble-differencemethodisusedtoremovethis
bias[37]. Inthedouble-differencemethod,areferencesatelliteclockischosenfromthe
recoveredPPP-B2bpreciseclockoffsets,andthesingle-differencebetweenthereference
clock and other satellite clocks can be formed. The same single-differences can also be
obtainedbyusingIGSpreciseclockoffsets. Then,thecorrespondingdouble-difference
valuescanbeformedwiththesamesingle-differencepair. Thedouble-differenceclock
offsetcanbeexpressedas:
(cid:16) (cid:17)
∇∆dtsat = dtsat −dt refsat − dtsat −dt refsat (7)
B2b,GFZ prec,B2b prec,B2b prec,GFZ prec,GFZ
where∇∆isadouble-difference(DD)operator.
2.3. PPPPositioningwiththeRecoveredPPP-B2bOrbitsandClocks
TheGNSScodeandphaseobservationsattheithfrequencyreadas[38,39]:

 P
i
= ρ+c·δt
r
−c·δts+T+ f
f
1
2
2 ·I
1
+B
r,i
−B
i
s+ε
Pi
i (8)
 L
i
= ρ+c·δt
r
−c·δts+T− f
f
1 2
2
·I
1
+λ
i
(cid:0) N
i
+b
r,i
−b
i
s(cid:1) +ε
Li
i

<!-- PAGE: 5 -->

RemoteSens.2021,13,2050 5of19
where P andL are raw code/phase observation; ρ represents the receiver-to-satellite
i i
geometrydistance;cstandsforthespeedoflight;δt andδtsareclockoffsetsatthereceiver
r
andthesatellite,respectively;Tstandsforthetroposphericdelay; f isthefrequencyvalue;
i
I denotestheionosphericdelayforL ;λ isthewavelengthandN istheintegerambiguity;
1 1 i i
B andb representcode/phasebiasatthereceiver;Bs andbs denotecode/phasebiasat
r,i r,i i i
thesatellite;andε andε arecode/phaseunmodellederrors,includingthermalnoiseand
Pi Li
multipath. Itisnotedthatexistingmodelsshouldbeappliedtocorrecttherelativisticeffect,
Sagnaceffect,Shapirotimedelay[40],phasewindupeffect[41]andsitedisplacements[42].
Usually, theionospheric-freecombinationisadoptedbyPPPtoeliminatethefirst-
orderionosphericdelay. Thedual-frequencycode/phaseionospheric-freecombinations
canbeexpressedas:
(cid:26) P = αP +(1−α)P = ρ+c·δt −c·δts+T+ε
IF 1 2 r PIF (9)
L = αL +(1−α)L = ρ+c·δt −c·δts+T+λ ·N +ε
IF 1 2 r IF IF LIF
whereα = f2/ (cid:0) f2− f2 (cid:1) ;λ N = αλ (cid:0) N +b −bs(cid:1) +(1−α)λ (N +b −bs);ε =
1 1 2 IF IF 1 1 r,1 1 2 2 r,2 2 PIF
αε +(1−α)ε andε = αε +(1−α)ε . Itiswellknownthatthetroposphericdelay
P1 P2 LIF L1 L2
iscomposedofdryandwetcomponents. TheSaastamoinenmodelcanbeusedtocorrect
forthedrytroposphericdelay,whilethewettroposphericdelayisexpressedastheproduct
ofamappingfunction M andazenithwetdelayzwd,andthezenithwetdelaymustbe
W
estimatedduetoitsvolatility. ByapplyingPPP-B2borbitsandclockoffsets,Equation(9)
canbelinearizedas:
(cid:26)
p = −e·x+c·δt +M ·zwd+ε
IF r W PIF (10)
l = −e·x+c·δt +M ·zwd+λ ·N +ε
IF r W IF IF LIF
whereedenotestheunitvectorinthereceiver-to-satellitedirection,andxisthereceiver
position increment. As we can see from this equation, the unknown parameters only
remainthereceiverpositionincrementvectorx,thereceiverclockoffsetδt ,thezenithwet
r
delayzwdandtheionosphere-freeambiguityλ N . ByadoptingaKalmanfilterscheme,
IF IF
theunknownparameterscanbeexactlyestimated.
3. Experiments,ResultsandDiscussion
ToevaluatetheprecisionoforbitandclockcorrectionsandPPPperformance,PPP-B2b
messagesovera3-dayperiodwerecollectedfrom5October2020to7October2020. The
collected PPP-B2b messages were broadcast from C59 and C60. The PPP-B2b message
types, as well as the corresponding sample rates and nominal validity time, over the
selected3-dayperiodarelistedinTable2. Thereisonlyonemessagebroadcastpersecond.
HencethetotalnumberofPPP-b2bmessagesisexpectedtobe86,400inonedayforeach
GEOsatellite. Wecountedthenumberofreceivedmessagesforeachmessagetype. The
percentageofdifferentmessagetypesispresentedinFigure1. Therewerejust3epochs
ofPPP-B2bmessagesmissing,andonlyPPP-B2bcorrectionsofGPSandBDS-3satellites
werebroadcastduringtheselectedperiod.
Table2.ThePPP-B2bmessageinformation.
MessageType SampleRate(s) NominalValidity(s)
1 48 –
2 48 96
3 48 86,400
4 6 12
63 – –

<!-- PAGE: 6 -->

RemoteSens.2021,13,2050 6of19
Figure1.ThepercentagesofdifferentPPP-b2bmessagetypes(5October2020to7October2020).
TwosetsofexperimentswerecarriedouttoassesstheBDSPPP-B2bservice.Firstly,the
precisionofPPP-B2borbitandclockcorrectionswasevaluatedbyusingpreciseproducts
fromGFZ(GBM)asreferences.Secondly,thePPPtests,includingstaticmodeandkinematic
mode,wereconductedtoassesspositioningperformance.
3.1. AssessmentResultsofPPP-B2bOrbit/ClockCorrections
TheavailabilityofBDS-3/GPSsatellites’PPP-B2borbitandclockoffsetcorrections
aredepictedinFigure2. BDSPPP-B2bservicecontains29GPSsatellitesand27BDS-3
satellitesduringtheperiodfrom5October2020to7October2020.
GBMpreciseorbit/clockproductsweredownloadedfromftp://ftp.gfz-potsdam.de/
GNSS/products/mgex/on15December2020andusedasreferences. UptoOctober2020,
GBMpreciseproductsincludeBDS-3satellitesofC19-C30,C32-C46,C60. Theorbitand
clockaccuracyforBDS-3MEOscouldreachcentimeter-level,andthatforBDS-3GEOs
andIGSOsisatdecimeter-level[43]. GiventhattheaccuracyofGBMorbits/clocksfor
BDS-3GEOsandIGSOsisatdecimeter-level,weexcludedBDS-3GEOsandIGSOsfrom
theassessment. ForGPSsatellites,theGBMproductsexhibitanorbit/clockaccuracyat
2–3cm[44].

<!-- PAGE: 7 -->

RemoteSens.2021,13,2050 7of19
Figure2.TheavailabilityofPPP-B2borbit/clockcorrectionsforBDS-3/GPSsatellitesfrom5October
2020to7October2020.
Firstly,werecoveredthePPP-B2bpreciseorbitsandclockoffsetsata30-ssampling
rate by using PPP-B2b messages and broadcast ephemeris data. At the same time, the
GBMpreciseephemeriswereinterpolatedtothesamesampleaccordingtothealgorithm
describedin[45]. ThesatellitePCOswerecorrectedaccordingtoEquation(4). Considering
thattherewasonlyathree-daydataarc,theHelmerttransformationparameters,obtained
fromtheChinasatellitenavigationoffice(CSNO)[30],weredirectlyadoptedinsteadof
estimated. Theclockdifferencescausedbydifferentsignalswerealsocorrectedaccording
to Equation (6). Subsequently, the orbit/clock errors were calculated as described in
Section2. Theorbiterrorsinthedirectionofalong-track,cross-trackandradial,aswell
astheclockoffseterrors,areshowninFigures3and4. MostofthePPP-B2borbiterrors
arewithintherangeof±0.5m. TheGPSsatellitesshowlargererrorsinthealong-track
componentcomparedtothecross-track/radialcomponents. ForBDS-3satellites,theerrors
inthecross-trackcomponentseemtobelargerthanfortheothertwodirections.

<!-- PAGE: 8 -->

RemoteSens.2021,13,2050 8of19
Figure3.GPSPPP-B2borbitandclockerrorsfrom5October2020to7October2020.

<!-- PAGE: 9 -->

RemoteSens.2021,13,2050 9of19
Figure4.BDSPPP-B2borbitandclockerrorsfrom5October2020to7October2020.
Therootmeansquare(RMS)ofPPP-B2borbiterrorswascountedtoassessthepreci-
sionofPPP-B2bpreciseorbitcorrections. Consideringthatacommonconstantofclock
offseterrorscanbeabsorbedintothereceiverclockoffsetparameter,thestandarddevia-
tion(STD)ofPPP-B2bpreciseclockoffseterrorswasadoptedtoevaluatetheprecisionof
PPP-B2bclockoffsetcorrections. Figures5and6showtheRMSvaluesofPPP-B2borbit
errors,andtheSTDvalueofPPP-B2bclockoffseterrorsoveraperiodof3days. Table3fur-
therpresentstheaverageRMSvaluesoforbiterrorsinthealong-track/cross-track/radial
components,andtheaverageSTDvaluesofclockoffseterrors. Ingeneral,theaccuracy

<!-- PAGE: 10 -->

RemoteSens.2021,13,2050 10of19
ofthePPP-B2borbitscanreachdecimeterlevelforGPSsatellitesandBDS-3MEOs. The
accuracyofthePPP-B2bclockoffsetsisbetterthan3.0cm.
Figure5.RMSvaluesofGPSPPP-B2borbiterrorsandSTDvaluesofclockerrors.
Figure6.RMSvaluesofBDSPPP-B2borbiterrorsandSTDvaluesofclockerrors.
Table3.TheaverageSTDandRMSofBDS-3/GPSPPP-B2borbitsandclockerrors(unit:cm).
RMS-A1 RMS-C2 RMS-R3 STD-CLK4
GPS 16.0 13.4 10.4 2.7
BDS 13.1 14.5 13.8 2.2
1RMS-AdenotestheaverageRMSvalueoforbiterrorsinthedirectionofalong-track. 2RMS-Cdenotesthe
averageRMSvalueoforbiterrorsinthedirectionofcross-track.3RMS-RdenotestheaverageRMSvalueoforbit
errorsinthedirectionofradial.4STD-CLKstandsfortheaverageSTDvalueofclockoffseterrors.
3.2. PPPTests
To investigate the positioning performance with the PPP-B2b service, PPP tests in
static and kinematic mode were carried out. For comparison, the static and kinematic

<!-- PAGE: 11 -->

RemoteSens.2021,13,2050 11of19
PPP solutions were also obtained by using GBM products. We collected BDS-3/GPS
observations from 4 iGMAS stations. The geographical distribution of the 4 selected
iGMASstations,locatedbetween20◦N–40◦Nand100◦E–130◦E,isshowninFigure7. The
dailyobservationfilesweresplitinto4-hsessions,andthePPPprocessingwasrestarted
every4h.Oncethedataoutagewaslargerthan1min,thecorresponding4-hsessionwould
notbeprocessed. Table4summarizedourPPPprocessingstrategies. Noticethatkinematic
PPPwassimulatedbyestimatingpositionsindependentlyepoch-by-epoch,whichissimilar
totheestimationofthepositioninthekinematicPPPmode. Thecoordinatesobtained
fromtheiGMASweeklySINEXsolutionfilewereusedasreferences[46].
Figure7.Locationof4selectediGMASstations.
Table4.StrategiesofPPPprocessing.
Item Models/Strategies
GNSSSystem GPSandBDS-3
Signalselection GPS:L1/L2andBDS-3:B1C/B2a
Observables Dual-frequencycode/phaseionosphere-freecombinations
Samplingrate 30s
Cutoffelevation 10◦
Rawcode:0.5minzenithdirection
Observablenoise
Rawphase:0.005minzenithdirection
Weightmethod Elevationdependentweight[38]
Phasewindup Corrected[41]
Relativisticeffect Corrected[40]
Sagnaceffect Corrected[40]
Shapirotimedelay Corrected[40]
Solidtide,oceanloadingandpoletidewerecorrectedaccording
Tidaleffect
toIERSConventions2010[42]
Zenithdrydelay:correctedwithSaastamoinenmodel,while
meteorologicalparameterswerecalculatedbyapplyingglobal
pressureandtemperature(GPT)model[47]
Troposphere
Zenithwetdelay:estimatedforeachepochasarandomwalk
noisewithaprocessnoiseof2cm/sqrt(h)
Mappingfunction:globalmappingfunction(GMF)[48]
PhaseAmbiguity Estimatedasafloatconstantforeachambiguityarc
Estimator Kalmanfilter

<!-- PAGE: 12 -->

RemoteSens.2021,13,2050 12of19
3.2.1. StaticMode
TheRMSvaluesofpositioningerrorsofthefinal10minwerecountedtoassessthe
positioningaccuracyinthestaticmode. Figures8–11showthePPPpositioningaccuracy
atthestationsofBJF1,KUN1,SHA1,andWUH1. Amongthesefigures,severalsessions‘
positioningaccuracyarenotprovidedbecauseoftheGNSSdataoutage. Ingeneral,the
staticPPPperformancewiththePPP-B2bserviceisslightlyworsethanthatwithGBM
products. ThepositioningaccuracywiththePPP-B2bserviceinthenorthcomponentis
betterthanthoseintheeast/upcomponents. ThepositioningaccuracywiththePPP-B2b
serviceinthenorthcomponentisbetterthan3.5cm,whileapositioningaccuracyofbetter
than4.5cmcanbeachievedinthenorth/upcomponents. Thepositioningaccuracywith
the PPP-B2b service of all sessions is at the centimeter level. The positioning accuracy
withGBMproductsisbetterthan3.5cmintheeast/north/upcomponents. Forallfour
stations,theaveragepositioningaccuracywithPPP-B2bservicevariesby2.5–3.1cmin
thehorizontalcomponent,and1.9–2.5cmintheverticalcomponent. Whiletheaverage
positioningaccuracywithGBMproductsvariesby1.5–1.8cminthehorizontal,and1.1–1.6
cmintheverticaldirection. ThedetailedstatisticsarepresentedinTable5.
Table5.Theaveragepositioningaccuracyatthefourstations(unit:cm).
PPP-B2bService GBMProducts
E1 N2 U3 H4 3D5 E1 N2 U3 H4 3D5
BJF1 2.2 1.8 2.4 2.8 3.7 1.1 1.4 1.3 1.8 2.2
KUN1 2.1 1.3 2.2 2.5 3.3 1.1 1.0 1.1 1.5 1.9
SHA1 2.7 1.4 2.5 3.0 3.9 1.2 1.1 1.6 1.6 2.3
WUH1 2.4 1.8 1.9 3.0 3.6 1.0 1.4 1.5 1.7 2.3
1E/2N/3UStandsforthedirectionsofeast,northandup;4H/53Ddenotehorizontaland3-dimensional.
Figure8.PositioningaccuracyofstaticPPPwithdifferentdatasessionsatWUH1station.

<!-- PAGE: 13 -->

RemoteSens.2021,13,2050 13of19
Figure9.PositioningaccuracyofstaticPPPwithdifferentdatasessionsatBJF1station.
Figure10.PositioningaccuracyofstaticPPPwithdifferentdatasessionsatKUN1station.

<!-- PAGE: 14 -->

RemoteSens.2021,13,2050 14of19
Figure11.PositioningaccuracyofstaticPPPwithdifferentdatasessionsatSHA1station.
Convergencetime(CT)isalsoacrucialfactortoassessthestaticPPPperformance. As
describedintheofficialdocument[7],thepositioningperformancewithPPP-B2bservice
is better than 30 cm in the horizontal component and better than 60 cm in the vertical
component with a confidence level of 95%. Hence, the convergence time was defined
toachievethehorizontalpositioningaccuracybetterthan30cm,theverticalpositioning
accuracybetterthan60cm,andkeepsuchapositioningaccuracyatleast5mininthispaper.
TheconvergencetimeofstaticPPPateachiGMASstationisshowninFigure12. Asvisible,
theconvergencetimewithPPP-B2bserviceis18.0/17.0/18.8/16.9minat4iGMASstations.
WhenGBMproductsareused,theconvergencetimeis8.2/11.8/10.6/9.8min,respectively.
Figure12.ConvergencetimeofstaticPPPatdifferentdatasessions.

<!-- PAGE: 15 -->

RemoteSens.2021,13,2050 15of19
3.2.2. KinematicMode
ThekinematicPPPpositioningerrorsatthestationsofBJF1,KUN1,SHA1andWUH1
arepresentedinFigures13–16,respectively. Similarly,thereisalsoalackofsomesessions‘
positioningresults,duetoGNSSdataoutage. Onecanseethatthepositioningaccuracy
withthePPP-B2bserviceintheeast/north/upcomponentsisallwithinonedecimeter
afterconvergence.
Figure13.KinematicPPPpositioningerrorsattheBJF1station(toppanelforPPP-B2bandbottom
panelforGBM).
Figure14.KinematicPPPpositioningerrorsattheKUN1station(toppanelforPPP-B2bandbottom
panelforGBM).

<!-- PAGE: 16 -->

RemoteSens.2021,13,2050 16of19
Figure15.KinematicPPPpositioningerrorsattheSHA1station(toppanelforPPP-B2bandbottom
panelforGBM).
Figure16.KinematicPPPpositioningerrorsattheWUH1station(toppanelforPPP-B2bandbottom
panelforGBM).
TheRMSvaluesofpositioningerrorswerecountedfor4iGMASstations,andthe
resultsarepresentedinTable6. Itshouldbenotedthatthepositioningerrorsofthefirst
30 min at each session have been removed, in order to exclude the positioning results
beforefullconvergence. Forbothtypesofproducts,thepositioningaccuracyinthenorth
componentisapparentlybetterthanthoseintheothertwocomponents. IntermofPPP
performancewiththePPP-B2bservice,thehorizontalpositioningaccuracyrangesfrom8.0
to9.6cm,withanaveragevalueof8.9cm,andthe3-dimensionalpositioningaccuracyis
allwithin13cm,withanaveragevalueof11.8cm. WhenusingtheGBMproducts,the
averagehorizontalpositioningaccuracycanreach4.2cm,andtheaverage3-dimensional
positioningaccuracyis5.7cm.

<!-- PAGE: 17 -->

RemoteSens.2021,13,2050 17of19
Table6.ThepositioningaccuracyofkinematicPPPatallfourstations(unit:cm).
PPP-B2bService GBMProducts
E N U H 3D E N U H 3D
BJF1 8.0 3.8 8.6 8.8 12.3 3.3 2.5 3.5 4.1 5.4
KUN1 9.2 3.1 8.3 9.6 12.7 3.9 1.5 4.3 4.2 6.0
SHA1 7.1 3.6 7.5 8.0 10.9 3.5 2.4 4.5 4.2 6.2
WUH1 8.1 4.0 7.5 9.0 11.3 3.4 2.2 3.0 4.1 5.0
4. Conclusions
Atpresent,thePPP-B2bserviceisavailableforusersinandaroundChina. Inthis
study, an initial assessment of the BDS PPP-B2b service was carried out based on the
collected3-daydata. Firstly,theavailabilityofPPP-B2bmessageswasanalyzed. ThePPP-
B2bserviceonlyprovidedthesatelliteorbitcorrection,clockcorrection,anddifferential
code bias of BDS-3/GPS. The availability of PPP-B2b messages was near to 100%; the
missingnumberofPPP-B2bmessageswasonly3epochsduringthe3-dayperiod. With
GBMpreciseephemerisproductsasreferences,theprecisionofPPP-B2borbitandclock
corrections were evaluated. The accuracy of PPP-B2b orbits in the direction of radial
along-trackandcross-trackwere0.104/0.169/0.134mforGPS.Thecorrespondingaccuracy
obtainedforBDS-3MEOswas0.138/0.131/0.145m. Generally,thestandarddeviationof
B2bclockoffsetswasbetterthan3.0cm.
PPPtests,bothinstaticandkinematicmode,werealsoconductedtofurtherevaluate
thepositioningperformanceofthePPP-B2bservice. RegardingstaticPPP,theconvergence
timewasabout17.7min, andtheaveragepositioningaccuracyinthedirectionofeast,
north and up were 2.4/1.6/2.3 cm, respectively. As for simulated kinematic PPP, the
average positioning accuracies were 8.1/3.6/8.0 cm in the east/north/up components,
respectively. TheresultsofPPPtestsdemonstratedthatthepositioningaccuracycould
reach centimeter-level for static applications, and decimeter-level positioning accuracy
couldbeachievedforkinematicapplications.
AuthorContributions: Conceptualization,Z.N.andZ.W.;methodology,Z.N.andX.X.;software,
Z.N. and X.X.; validation, X.X. and J.D.; formal analysis, X.X. and J.D.; writing—original draft
preparation,X.X.;writing—reviewandediting,Z.N.;visualization,X.X.andJ.D.;supervision,Z.W.;
projectadministration,Z.W.;fundingacquisition,Z.NandZ.W.Allauthorshavereadandagreedto
thepublishedversionofthemanuscript.
Funding: This study was funded by the National Key Research and Development Program of
China (Nos. 2019YFC1509205, 2019YFC1509204), China Postdoctoral Science Foundation (No.
2020M672168),theFundamentalResearchFundsfortheCentralUniversities(No.20CX06044A)and
QingdaoPostdoctoralApplicationResearchProject(No.QDYY20190077).
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement: ThedatasetsanalyzedinthisstudyaremanagedbytheCollegeof
OceanographyandSpaceInformatics,ChinaUniversityofPetroleum,Qingdao,Chinaandcanbe
availableonrequestfromthecorrespondingauthor.
Acknowledgments:WegreatlyappreciateiGMASandGFZforprovidingmulti-GNSSobservation
dataandproducts.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Yang,Y.;Li,J.;Xu,J.;Tang,J.;Guo,H.;He,H.ContributionoftheCompasssatellitenavigationsystemtoglobalPNTusers.
Chin.Sci.Bull.2011,56,2813–2819.[CrossRef]
2. ChinaSatelliteNavigationOffice. DevelopmentoftheBeiDouNavigationSatelliteSystem(Version4.0). Availableonline:
http://www.beidou.gov.cn/xt/gfxz/201912/P020191227430565455478.pdf(accessedon30September2020).

<!-- PAGE: 18 -->

RemoteSens.2021,13,2050 18of19
3. ChinaSatelliteNavigationOffice.China’sBeiDouNavigationSatelliteSystem.Availableonline:http://www.beidou.gov.cn/xt/
gfxz/201712/P020171221333863515306.pdf(accessedon30September2020).
4. Yang,Y.;Li,J.;Wang,A.;Xu,J.;He,H.;Guo,H.;Shen,J.;Dai,X.Preliminaryassessmentofthenavigationandpositioning
performanceofBeiDouregionalnavigationsatellitesystem.Sci.ChinaEarthSci.2014,57,144–152.[CrossRef]
5. Li,X.; Li,X.; Liu,G.; Yuan,Y.; Freeshah,M.; Zhang,K.; Zhou,F.BDSmulti-frequencyPPPambiguityresolutionwithnew
B2a/B2b/B2a+bsignalsandlegacyB1I/B3Isignals.J.Geod.2020,94,1–15.[CrossRef]
6. Yang,Y.;Mao,Y.;Sun,B.BasicperformanceandfuturedevelopmentsofBeiDouglobalnavigationsatellitesystem.Satell.Navig.
2020,1,1–8.[CrossRef]
7. ChinaSatelliteNavigationOffice. TheApplicationServiceArchitectureofBeiDouNavigationSatelliteSystem(Version1.0).
Availableonline:http://www.beidou.gov.cn/xt/gfxz/201912/P020191227333024390305.pdf(accessedon30September2020).
8. Zumberge,J.F.;Heflin,M.B.;Jefferson,D.C.;Watkins,M.M.;Webb,F.H.Precisepointpositioningfortheefficientandrobust
analysisofGPSdatafromlargenetworks.J.Geophys.Res.SolidEarth1997,102,5005–5017.[CrossRef]
9. Kouba,J.;Héroux,P.PrecisePointPositioningUsingIGSOrbitandClockProducts.GPSSolut.2001,5,12–28.[CrossRef]
10. Zhang,B.;Chen,Y.;Yuan,Y.PPP-RTKbasedonundifferencedanduncombinedobservations:Theoreticalandpracticalaspects.
J.Geod.2019,93,1011–1024.[CrossRef]
11. Geng,J.;Teferle,F.N.;Meng,X.;Dodson,A.H.Kinematicprecisepointpositioningatremotemarineplatforms.GPSSolut.2010,
14,343–350.[CrossRef]
12. Alkan,R.M.;Saka,M.H.;Ozulu,M.;I˙lçi,V.KinematicprecisepointpositioningusingGPSandGLONASSmeasurementsin
marineenvironments.Measurement2017,109,36–43.[CrossRef]
13. Nie,Z.;Wang,B.;Wang,Z.;He,K.Anoffshorereal-timeprecisepointpositioningtechniquebasedonasinglesetofBeiDou
short-messagecommunicationdevices.J.Geod.2020,94,1–11.[CrossRef]
14. Rocken,C.;Johnson,J.;VanHove,T.;Iwabuchi,T.Atmosphericwatervaporandgeoidmeasurementsintheopenoceanwith
GPS.Geophys.Res.Lett.2005,32,1–3.[CrossRef]
15. Xu,P.;Shi,C.;Fang,R.;Liu,J.;Niu,X.;Zhang,Q.;Yanagidani,T.High-rateprecisepointpositioning(PPP)tomeasureseismic
wavemotions:AnexperimentalcomparisonofGPSPPPwithinertialmeasurementunits.J.Geod.2013,87,361–372.[CrossRef]
16. Yigit,C.O.;Gurlek,E.Experimentaltestingofhigh-rateGNSSprecisepointpositioning(PPP)methodfordetectingdynamic
verticaldisplacementresponseofengineeringstructures.Geomat.Nat.HazardsRisk2017,8,893–904.[CrossRef]
17. Li,X.;Zus,F.;Lu,C.;Ning,T.;Dick,G.;Ge,M.;Wickert,J.;Schuh,H.Retrievinghigh-resolutiontroposphericgradientsfrom
multiconstellationGNSSobservations.Geophys.Res.Lett.2015,42,4173–4181.[CrossRef]
18. Li,X.; Dick,G.; Ge,M.; Heise,S.; Wickert,J.; Bender,M.Real-timeGPSsensingofatmosphericwatervapor: Precisepoint
positioningwithorbit,clock,andphasedelaycorrections.Geophys.Res.Lett.2014,41,3615–3621.[CrossRef]
19. Guo,J.;Li,X.;Li,Z.;Hu,L.;Yang,G.;Zhao,C.;Fairbairn,D.;Watson,D.;Ge,M.Multi-GNSSprecisepointpositioningfor
precisionagriculture.Precis.Agric.2018,19,895–911.[CrossRef]
20. Weber,G.;Mervart,L.;Lukes,Z.;Rocken,C.;Dousa,J.Real-timeclockandorbitcorrectionsforimprovedpointpositioningvia
NTRIP.InProceedingsoftheIONGNSS2007,FortWorth,TX,USA,23–35September2007;pp.1992–1998.
21. El-diasty,M.DevelopmentofReal-TimePPP-BasedGPS/INSIntegrationSystemUsingIGSReal-TimeServiceforHydrographic
Surveys.J.Survey.Eng.2016,142,1–8.[CrossRef]
22. Tegedor, J.; Lapucha, D.; Ørpen, O.; Vigen, E.; Melgard, T.; Strandli, R. The new G4 service: Multi-constellation precise
pointpositioningincludingGPS,GLONASS,GalileoandBeiDou. InProceedingsoftheIONGNSS+2015,Tampa,FL,USA,
14–18September2015;pp.1089–1095.
23. Dai, L.; Chen, Y.; Lie, A.; Zeitzew, M.; Zhang, Y.StarFireSF3: Worldwidecentimeter-accuraterealtimeGNSSpositioning.
InProceedingsoftheIONGNSS+2016,Portland,OR,USA,12–16September2016;pp.3295–3320.
24. Leandro,R.;Landau,H.;Nitschke,M.;Glocker,M.;Seeger,S.;Chen,X.;Deking,A.;BenTahar,M.;Zhang,F.;Ferguson,K.;etal.
RTXpositioning:Thenextgenerationofcm-accuratereal-timeGNSSpositioning.InProceedingsoftheIONGNSS2011,Portlan,
OR,USA,20–23September2011;pp.1460–1475.
25. Fujita,S.;Sato,Y.;Miya,M.;Ota,K.;Hirokawa,R.;Takiguchi,J.DesignofIntegrityFunctiononCentimeterLevelAugmentation
Service(CLAS)inJapaneseQuasi-ZenithSatelliteSystem. InProceedingsoftheIONGNSS+2016,Portland,OR,USA,12–
16September2016;pp.3258–3263.
26. Namie,H.;Okamoto,O.;Kubo,N.;Yasuda,A.Initialperformanceevaluationofcentimeter-classaugmentationsystemusing
Quasi-ZenithSatelliteSystem.Electron.Commun.Jpn.2018,101,3–10.[CrossRef]
27. Fernandez-Hernandez,I.;Rodríguez,I.;Tobías,G.;Calle,J.D.;Carbonell,E.;Seco-Granados,G.;Simón,J.;Blasi,R.TestingGNSS
highaccuracyandauthentication-galileo’scommercialservice.Insid.GNSS2015,10,37–48.
28. Susi,M.; Borio,D.KalmanfilteringwithnoncoherentintegrationsforGalileoE6-Btracking. Navig. J.Inst. Navig. 2020,67.
[CrossRef]
29. Liu,C.;Gao,W.;Liu,T.;Wang,D.;Yao,Z.;Gao,Y.;Nie,X.;Wang,W.;Li,D.;Zhang,W.;etal.Designandimplementationofa
BDSprecisepointpositioningservice.Navig.J.Inst.Navig.2020,67,875–891.[CrossRef]
30. ChinaSatelliteNavigationOffice.BeiDouNavigationSatelliteSystemSignalinSpaceInterfaceControlDocumentPrecisePoint
PositioningServiceSignalPPP-B2b(BetaVersion).Availableonline:http://www.beidou.gov.cn/xt/gfxz/201912/P02019122733
1847498839.pdf(accessedon30September2020).

<!-- PAGE: 19 -->

RemoteSens.2021,13,2050 19of19
31. Chen,Q.;Song,S.;Zhou,W.AccuracyAnalysisofGNSSHourlyUltra-RapidOrbitandClockProductsfromSHAOACof
iGMAS.RemoteSens.2021,13,1022.[CrossRef]
32. Montenbruck,O.;Steigenberger,P.;Hauschild,A.Broadcastversuspreciseephemerides:Amulti-GNSSperspective.GPSSolut.
2015,19,321–333.[CrossRef]
33. Steigenberger,P.;Montenbruck,O.ConsistencyofMGEXOrbitandClockProducts.Engineering2020,6,898–903.[CrossRef]
34. Zhang,Y.;Kubo,N.;Chen,J.;Chu,F.Y.;Wang,A.;Wang,J.ApparentclockandTGDbiasesbetweenBDS-2andBDS-3.GPSSolut.
2020,24,1–15.[CrossRef]
35. Lv,Y.;Geng,T.;Zhao,Q.;Xie,X.;Zhou,R.InitialassessmentofBDS-3preliminarysystemsignal-in-spacerangeerror.GPSSolut.
2020,24,1–13.[CrossRef]
36. Steigenberger,P.;Hugentobler,U.;Loyer,S.;Perosanz,F.;Prange,L.;Dach,R.;Uhlemann,M.;Gendt,G.;Montenbruck,O.Galileo
orbitandclockqualityoftheIGSMulti-GNSSExperiment.Adv.SpaceRes.2015,55,269–281.[CrossRef]
37. Guo,J.;Xu,X.;Zhao,Q.;Liu,J.Preciseorbitdeterminationforquad-constellationsatellitesatWuhanUniversity:Strategy,result
validation,andcomparison.J.Geod.2016,90,143–159.[CrossRef]
38. Leick,A.;Rapoport,L.;Tatarnikov,D.GPSSatelliteSurveying,4thed.;JohnWiley&Sons:Hoboken,NJ,USA,2015.
39. Zhang,B.;Hou,P.;Liu,T.;Yuan,Y.Asingle-receivergeometry-freeapproachtostochasticmodelingofmulti-frequencyGNSS
observables.J.Geod.2020,94,1–21.[CrossRef]
40. Ashby,N.RelativityintheGlobalPositioningSystemImprint/TermsofUse.LivingRev.Relativ.2003,6,1–42.[CrossRef]
41. Wu,J.-T.;Wu,S.C.;Hajj,G.A.;Bertiger,W.I.;Lichten,S.M.EffectsofantennaorientationonGPScarrierphase.InProceedingsof
theAAS/AIAAAstrodynamicsConference,Durango,CO,USA,19–22August1991;pp.1647–1660.
42. Petit, G.; Luzum, B. IERS Conventions (2010); Bureau International Des Poids et Mesures Sevres: Frankfurt am Main, Ger-
many,2010.
43. Sakic,P.;Mansur,G.;Mannel,B.Aprototypeforamulti-GNSSorbitcombination.InProceedingsoftheEuropeanNavigation
Conference,Bonn,Germany,23–24November2020;pp.1–11.
44. Montenbruck,O.;Steigenberger,P.;Prange,L.;Deng,Z.;Zhao,Q.;Perosanz,F.;Romero,I.;Noll,C.;Stürze,A.;Weber,G.;etal.
TheMulti-GNSSExperiment(MGEX)oftheInternationalGNSSService(IGS)–Achievements,prospectsandchallenges.Adv.Space
Res.2017,59,1671–1697.[CrossRef]
45. Nie,Z.;Zhou,P.;Liu,F.;Wang,Z.;Gao,Y.Evaluationoforbit,clockandionosphericcorrectionsfromfivecurrentlyavailable
SBASL1services:Methodologyandanalysis.RemoteSens.2019,11,411.[CrossRef]
46. Cai, H.; Chen, G.; Jiao, W.; Chen, K.; Xu, T.; Wang, H. An Initial Analysis and Assessment on Final Products of iGMAS.
In Proceedings of the China Satellite Navigation Conference (CSNC) 2016 Proceeding, Changsha, China, 18–20 May 2016;
pp.515–527.
47. Boehm,J.;Heinkelmann,R.;Schuh,H.Shortnote:Aglobalmodelofpressureandtemperatureforgeodeticapplications.J.Geod.
2007,81,679–683.[CrossRef]
48. Boehm,J.;Niell,A.;Tregoning,P.;Schuh,H.GlobalMappingFunction(GMF):Anewempiricalmappingfunctionbasedon
numericalweathermodeldata.Geophys.Res.Lett.2006,33,3–6.[CrossRef]