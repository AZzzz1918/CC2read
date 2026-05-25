<!-- PAGE: 1 -->

sensors
Article
Fault-Free Protection Level Equation for CLAS PPP-RTK and
Experimental Evaluations
EuihoKim1,* ,JaeyoungSong2,YujinShin3,SaekyulKim4,Pyo-WoongSon5,6 ,SulgeePark2
andSanghyunPark2
1 DepartmentofMechanical&SystemDesignEngineering,HongikUniversity,Seoul04006,Korea
2 MaritimePNTResearchOffice,KRISO,Daejeon34103,Korea;justin2028@kriso.re.kr(J.S.);
sgpark@kriso.re.kr(S.P.);shpark@kriso.re.kr(S.P.)
3 ResearchInstituteofScienceandTechnology,HongikUniversity,Seoul04006,Korea;syj3558@naver.com
4 DepartmentofMechanicalEngineering,HongikUniversity,Seoul04006,Korea;idea2693@naver.com
5 KoreaResearchInstituteofShipsandOceanEngineering,Daejeon34103,Korea;pwson@kriso.re.kr
6 DepartmentofShipandOceanEngineering,UniversityofScienceandTechnology(UST),
Daejeon34113,Korea
* Correspondence:euihokim@hongik.ac.kr
Abstract:Centimeterlevelaugmentationsystem(CLAS)ofthequasi-zenithsatellitesystem(QZSS)is
thefirstprecisepointpositioning-realtimekinematic(PPP-RTK)augmentationsystemoftheglobal
navigationsatellitesystem(GNSS),whichiscurrentlyprovidingservicesforJapan.CLASbroadcasts
thestate-spacerepresentationofcorrectionmessagesalongwithintegritymessagesregardingsatellite
faultsandthequalityindexofeachcorrection. InotherGNSSaugmentationsystems,suchasthe
space-basedaugmentationsystem(SBAS)ofGNSS,thequalityindicesofcorrectionmessagesareused
togeneratefault-freeprotectionlevelsthatrepresentapositionboundcontainingatrueuserposition
withaprobabilityofmisseddetections. Althoughtheprotectionlevelequationsarewelldefined
fortheSBAS,aprotectionlevelequationfortheCLASPPP-RTKservicehasnotbeenrigorously
discussedintheliterature.Thispaperproposesafault-freeprotectionlevelequationforthePPP-RTK
Citation:Kim,E.;Song,J.;Shin,Y.;
methodsthatconsiderstheprobabilityofcorrectintegerambiguityfixesintheGNSScarrierphase
Kim,S.;Son,P.-W.;Park,S.;Park,S.
measurementsaswellastheCLAScorrectionqualitymessages. Thecomputedprotectionlevels
Fault-FreeProtectionLevelEquation
forCLASPPP-RTKandExperimental withpositionerrorswereexperimentallycomparedbyprocessingtheGNSSmeasurementsfromthe
Evaluations.Sensors2022,22,3570. GNSSEarthObservationNetwork(GEONET)stationsinJapanandtheL6messagesfromtheCLAS
https://doi.org/10.3390/s22093570 broadcastusingthevirtualreferencestation-realtimekinematic(VRS-RTK)techniques.Ourresults,
basedontheGEONETdatasetspanning7days,showedthatthecomputedprotectionlevelsusing
AcademicEditors:YuryYasyukevich,
theproposedequationswerelargerthanthepositionerrorsforallepochs.Inthedataset,theRMS
BaochengZhangandVenkatRatnam
errorsoftheCLASVRS-RTKpositionwere4.6and14cminthehorizontalandverticaldirections,
Received:6April2022 respectively,whereasthehorizontalprotectionlevelsrangedfrom25cmto2.3mandthevertical
Accepted:4May2022 protectionlevelsrangedfrom50cmto5.2mbasedonfault-freeintegrityriskof10−7.
Published:7May2022
Publisher’sNote:MDPIstaysneutral Keywords:GNSSprecisepositioning;protectionlevels;integrity;PPP-RTK
withregardtojurisdictionalclaimsin
publishedmapsandinstitutionalaffil-
iations.
1. Introduction
The performance of the global navigation satellite system (GNSS) is enhanced by
differentialGNSStechniques,includingground-andspace-basedaugmentationsystems
Copyright: © 2022 by the authors.
(GBASandSBAS)oftheglobalpositioningsystem(GPS)[1,2]. TheGBASandSBASwere
Licensee MDPI, Basel, Switzerland.
primarilydevelopedtoguideaircraftnavigation,andtheirdesignapproachandopera-
This article is an open access article
tionalphilosophiescenteredonsystemsafety. ThesafetylevelsofGBASandSBASare
distributed under the terms and
quantizedassystemintegritymeasures,andoneoftheimportantintegritymeasuresisa
conditionsoftheCreativeCommons
protectionlevel[3,4]. Theprotectionlevelrepresentstheboundofthetruepositionerror
Attribution(CCBY)license(https://
creativecommons.org/licenses/by/ attheriskofamissed-detectionprobability. InGBASandSBAS,apositionboundiscom-
4.0/). putedusingthewell-definedprotectionlevelequationsthattransformtherange-domain
Sensors2022,22,3570.https://doi.org/10.3390/s22093570 https://www.mdpi.com/journal/sensors

<!-- PAGE: 2 -->

Sensors2022,22,3570 2of13
Gaussianerrordistributionsofeachvisiblesatellitetotheposition-domainGaussianerror
distributionsviaauser-to-satellitegeometry. Therange-domainerrordistributionsusedin
theprotectionlevelequationsaredeterminedbytheGBASandSBASserviceprovidersand
arebroadcasttousersasqualityindicatorsassociatedwitheachcorrectionmessage. An
importantcharacteristicoftherangedomainerrordistributionistooverboundtheactual
errordistributionofthecorrectionmessagesinorderfortheprotectionlevels,computed
usingthequalityindicators,tooverboundtheactualuserpositionerrorswithamissed-
detectionprobability.Consequently,studieshavebeenconductedonvariousoverbounding
techniquesbasedonprobabilitydensityfunction(PDF),cumulativedistributionfunction
(CDF),andpairedoverbounding[5–8].
Centimeter level augmentation system (CLAS) of the quasi-zenith satellite system
(QZSS)isaveryrecentGNSSaugmentationsystemofJapan[9–11]. UnliketheGBASand
SBAS,whichprimarilyusetheGNSScodephasemeasurementsasrangingsources,CLAS
isaprecisepointpositioning–real-timekinematic(PPP-RTK)augmentationsystemthat
allowsuserstoresolveintegerambiguitiesincarrierphasemeasurementswithinseveral
minutesbyusingtheCLAScorrectionmessages. Therefore,theCLASuserscanusethe
carrierphaseasarangingsourceandachieveprecisepositioningsimilartothatofRTK.
CLASalsoprovidesqualityindicators(alsocalledintegritymessages)foreachcorrection
messagesothattheuserscancomputetheprotectionlevels. However,theCLASprotocol
currentlydoesnotspecifyanyformsofprotection-levelequations,andqualitymessage
generationschemesarenotwellknown[12,13]. Owingtolackofinformation,theCLAS
usersarenotencouragedtorelyonthequalitymessagesforsafenavigation.
Unfortunately, the protection level equations of GBAS or SBAS cannot be directly
appliedtotheCLASPPP-RTKpositionsolutions,becauseGBASorSBASdonotusethe
carrierphaseasrangingsources. Previousstudieshaveproposedprotection-levelequa-
tionsforPPPandRTKthatusethecarrierphaseasrangingsources[14–19]. Thesestudies
werebasedonreceiverautonomousintegritymonitoring(RAIM)[20],andtheirprotection
levelswerederivedtoprotectagainstthehard-to-detectfaultsinrangingmeasurements
and cycle slips. Feng proposed a Kalman filter-based RAIM for the carrier phase [14].
Inthisapproach,thede-correlatedinnovationsoftheKalmanfilterwereusedtodetect
faults. ProtectionlevelswerecomputedeitherfromthecovariancematrixoftheKalman
filterorfromusingthegeometryofthesatellitewhosefaultswouldbemostdifficultto
detect. References[15,16]proposedisotropy-basedprotectionlevels(IBPL),particularly
designedforthePPPpositionsolutions. Assumptionsregardingthebehaviorofranging
errorsintermsoftheirsize,direction,andprotectionlevelsasderivedfromamultivariate
t-distributionofmeasurementerrorswerenotmadeinIBPL.Ahmedetal. proposedprotec-
tionlevelsforRTK,whichweremodelledinamodifiedformfromthesolution-separation
RAIMmethods[17,18]. Anintegrityriskinthisapproachconsidersthemutuallyexclu-
siveeventsofcorrectandincorrectambiguityresolutionsintheleast-squaresambiguity
decorrelationadjustment(LAMBDA)method,whichwasintroducedin[19]. Although
thesestudiescanbeappliedtoderiveprotectionlevelsfortheCLASPPP-RTKposition
solutions,theirprotectionlevelswouldberelativelylargerbecausetheydonotusethe
CLASintegritymessagesorthefaultmonitoringcapabilityoftheCLASnetwork.
Thispaperproposesaprotection-levelequationforthePPP-RTKservicesbroadcasting
qualitymessages. BecausebothPPP-RTKandSBASbroadcaststatespacerepresentation
(SSR)ofthecorrectionmessages, ourproposedprotectionlevelequationsarebasedon
theSBASprotectionlevelequationsandareextendedtoreflectvirtualreferencestation
(VRS)-RTKpositioningscheme,whichisamethodofprocessingthePPP-RTKcorrection
messagesontheuserside. Additionally,theintegritymessagesoftheCLASserviceare
assumedtohaveastandarddeviationofaGaussiandistribution,similartotheSBAS.This
studycomparedtheprotectionlevelscomputedusingtheCLASintegritymessageswith
theVRS-RTKpositionerrors. FortheVRS-RTKprocess,weusedCLASL6messagesand
GNSSobservationmeasurementsfromtheGNSSEarthObservationNetwork(GEONET)
station in Japan. The L6 integrity messages were only used to compute the protection

<!-- PAGE: 3 -->

Sensors2022,22,3570 3of13
levels, becausetheyweresignificantlyinflated fromthe actualerror distributionofthe
correctionmessages;however,theVRS-RTKprocessusedthecorrectionerrordistributions
used in practice, whose standard deviation was significantly smaller than that of the
integritymessages.
ThispaperprovidesanoverviewofthearchitectureofCLASandbroadcastingmes-
sagesinSection2. Section3discussestheproposedprotection-levelequationsforPPP-
RTK.Section4presentsexamplesofbroadcastintegrityindicesandcomputedhorizontal
and vertical protection levels with the dataset. Finally, the discussion and conclusions
arepresented.
2. OverviewoftheCLASBroadcastMessages
CLASreceivestheGNSSobservationdatafromapproximately1200GEONETstations
and processes the data to generate the correction and integrity messages in a Compact
SSRformat. TheCompactSSRmessagesarebroadcastthroughtheL6bandbytheQZSS
andaredefinedasRTCM3compatibleproprietarymessagetype4073[13]. TheCompact
SSRmessageshave12subtypesconsistingofcorrectionandintegrityinformation,andthe
messagetypesarelistedinTable1[21]. Thecorrectionmessagesfortheorbit,clock,code
bias,andphasebiasarecalledcommoncorrections. Thezenithtroposphericdelayand
slantionosphericdelayforeachGNSSarereferredtoaslocalcorrections.
Table1.CompactSSRmessagetype,nominalvalidityperiod,andnominalupdateinterval.
MessageTypeID
MessageName NominalValidityPeriod[s] NominalUpdateInterval[s]
SubtypeID
CompactSSRMask MT4073,1 1 30
CompactSSRGNSSOrbitCorrection MT4073,2 60 30
CompactSSRGNSSClockCorrection MT4073,3 10 5
CompactSSRGNSSSatelliteCodeBias MT4073,4 60 30
CompactSSRGNSSSatellitePhaseBias MT4073,5 60 30
CompactSSRGNSSSatelliteCodeand
MT4073,6 60 30
PhaseBias
CompactSSRGNSSURA MT4073,7 60 30
CompactSSRSTECCorrection MT4073,8 60 30
CompactSSRGriddedCorrection MT4073,9 60 30
CompactSSRServiceInformation MT4073,10 (N/A) (N/A)
CompactSSRGNSSCombined
MT4073,11 10or60 5or30
Correction
CompactSSRAtmosphericCorrection MT4073,12 60 30
AmongthemessagesubtypeIDs,thequalitymessagesareincludedinsubtypeIDs
7,8,9,and12. SubtypeID7providesaqualityindicatorfortheuserrangeaccuracy(URA)
of each satellite, and others provide a troposphere quality indicator as well as an SSR
slanttotalelectroncontent(STEC)qualityindicator. Thequalityindicatorisrepresented
byacombinationofCLASSandVALUE,thevaluesofwhichrangefrom0to7,asseen
inEquation(1). TheSSRURAandtroposphericqualityindicatorswereconvertedtoa
physicalquantityusingthefollowingEquation[21]:
(cid:18) (cid:19)
VALUE
QualityIndicator[mm] ≤3CLASS 1+ −1[mm] (1)
4
TheSSRSTECphysicalquantitywasreadfromatablerelatingtheSSRSTECquality
indicatorstotheSSRSTECcorrectionuncertainty.
Thetotalrangingerrorforithsatellitecanbeestimatedbythefollowingequation
(cid:115)
σ = (σ )2+(σ /10)2+
(cid:18) 40.3×1016
σ ×100
(cid:19)2
+ (cid:0)(cid:0) σ /10 (cid:1) /sinE (cid:1)2 , (2)
i i,user i,sis f2 i,iono i,trop i

<!-- PAGE: 4 -->

Sensors2022,22,3570 4of13
whereσ isauser-specificlocalerror,suchasmultipatherrors. σ isasignalinspace
i,user i,sis
errorrepresentingthecorrectionmessageuncertaintyoftheorbit,clock,code,andcarrier
biases. σ is the ionospheric delay correction uncertainty provided from the STEC
i,iono
correction quality indicator in total electron content unit (TECU). σ represent the
i,trop
tropospheredelaycorrectionuncertainty. f isthefrequencyoftheGNSSsignalandE is
i
thesatelliteelevationangle. Thetotalrangingerroriscalculatedincentimeters,whichis
whyboth σ and σ dividedby10isused, andthesameappliesfor σ . Some
i,sis i,trop i,iono
examplesoftheCLASbroadcastqualityindicatorsarepresentedinSection4.
3. ProposedFault-FreeProtectionLevelEquationsforCLASPPP-RTKService
Todevelopafault-freeprotection-levelequationforaPPP-RTKsystem,thecurrent
protection-levelequationsofSBASareusedasthebaselineequationsbecausebothSBAS
andPPP-RTKbroadcastthecorrectionandqualitymessagesinSSRformats. Thissection
provides an overview of the SBAS fault-free protection level equation, followed by the
proposedPPP-RTKprotectionlevelequation.
3.1. Fault-FreeProtectionLevelEquationsofSBAS
TheSBASL1frequency-onlyprotection-levelequationusesthebroadcastcorrection
messageuncertaintiesanduser-definedmultipathandnoiseuncertainties. Foranindivid-
ualSBASpseudorangeerror,thecombinedrangeerrorvariancefortheithsatellitewas
constructedasfollows:
σ2 = σ2 +σ2 +σ2 +σ2 (3)
i flt,i UIRE,i tropo,i air,i(cid:48)
whereσ2 isthevarianceofthefastandlong-termsatelliteclockerrorcorrections. σ2
flt,i UIRE,i
isthevarianceoftheuserionosphererangeerrorcorrection,andσ2 isthevarianceof
tropo,i
thetroposphericerrorcorrection,andσ2 isthevarianceofthemultipatherrorexcluding
air,i
multipath from ground. It should be noted that each variance is determined from a
zero-mean Gaussian distribution that overbounds a non-ideal Gaussian distribution of
correctionerrors.
ThepseudorangevarianceisusedasaweightingmatrixtocomputeanSBASposition
solutionsuchthat
 1 0 ... 0 
σ2
W=    0 1 σ 1 2 2 ··· 0   . (4)
  . . . . . . ... 0  
 
0 0 ... 1
σn 2
Thedirectionvectorfromausertosatellitecanbeformulatedas
G = [cos(El)sin(Az ) cos(El)cos(Az ) sin(El) 1]. (5)
i i i i i i
Then,thestandarddeviationofthepositionestimateuncertaintyinEast/North/Up
(ENU)coordinatesis
(cid:114)
(cid:16) (cid:17)−1
σ = GTWG . (6)
p
With a missed-detection probability and its corresponding Gaussian tail value of
K ,theverticalprotectionlevel(VPL)boundingverticalpositionerrorsis
ffmd
(cid:115)(cid:20)(cid:16) (cid:17)−1 (cid:21)
VPL = K GTWG . (7)
SBAS ffmd
(3,3)
Similarly,thehorizontalprotectionlevel(HPL)iscomputed.

<!-- PAGE: 5 -->

Sensors2022,22,3570 5of13
3.2. OverviewofLeast-SquaresAmbiguityDecorrelationAdjustment(LAMBDA)
ThePPP-RTKserviceallowstheuseoftheGNSScarrierphaseforrangingmeasure-
mentsinamannersimilartoaVRS-RTKprocess. AVRS-RTKprocesstypicallyresolvesthe
integerambiguitiesincarrierphasemeasurementsusingtheLAMBDAalgorithm[22,23],
anditsupperboundprobabilityofcorrectlyfixingintegerambiguitiesisassessedusing
theintegerbootstrappingmethod[24].
WithGNSSmeasurementsofthetworeceiversatashortbaseline,thebasicobservation
measurementsareasfollows:
∆∇ρ =r+ε , (8)
ρ
∆∇Φ =r+λ
f
N+εΦ, (9)
where ∆∇ρ and ∆∇Φ are the double-difference code and carrier-phase measurements,
respectively. r is the geometric range from a user to a satellite. λ is the f frequency
f
wavelengthofaGNSScarrier. Nisintegerambiguity. εrepresentstheuncorrectedrange
measurementsandnoise. Thelinearizedobservationequationforasetofdouble-difference
codesandcarrier-phasemeasurementsofvisiblesatellitesis
y=Aa+Bb+ε, (10)
whereyisavectorofthedouble-differencecodeandcarrier-phasemeasurements. aisa
vectorofintegerambiguitiesandAisacorrespondingmatrixwithwavelengthsaselements.
Bisasatellitegeometrymatrix,andbistherelativepositionvectorfromaVRSreference
positiontoaGNSSreceiver.
ThepopularLAMBDAmethodresolvesaandcomputestheprecisebintwosteps.
First,anunconstrainedsolutionofEquation(10)iscomputedas
(cid:20) bˆ (cid:21)
=
(cid:18)(cid:20) BT (cid:21)
Q −1(cid:2) B A (cid:3)
(cid:19)−1(cid:20) BT (cid:21)
Q −1y, (11)
aˆ AT y AT y
wherebˆ andaˆ aretheestimatedbaselineandfloat-integerambiguities,respectively. Q is
y
thecovariancematrixofεinEquation(10). Thecovariancematrixofbˆ andaˆ is
(cid:20) (cid:21)
Q Q
Q= bˆ aˆbˆ . (12)
Q Q
bˆaˆ aˆ
ThesecondprocedureofLAMBDAconsistsofthere-parameterizationandsearchfor
a. There-parameterizationoftheintegervectorisimplementedasfollows:
z=Za,zˆ =Zaˆ,Q =ZTQ Z, (13)
zˆ aˆ
whereZisthedecorrelationtransformationmatrix. Then,there-parameterizedinteger
ambiguityissearchedwithrespecttothefollowingobjectivefunction:
min(zˆ−z)T
Q
−1(zˆ−z)
(14)
z zˆ
Onceanoptimalintegerambiguityvector,zˇ,isobtainedfromEquation(14),theorigi-
nalintegerambiguityvectorestimateisobtainedusingtheinverseofthetransformation
suchthat
aˇ =Z −1zˇ. (15)
Thepresumedfixedbaselinevector,bˇ is
bˇ =bˆ −Q Q −1(aˆ −aˇ) (16)
bˆaˆ aˆ

<!-- PAGE: 6 -->

Sensors2022,22,3570 6of13
Inaddition,thecovariancematrixofbˇ isasfollows:
Q =Q −Q Q −1Q
bˇ bˆ bˆaˆ aˆ aˆbˆ
(cid:16) (cid:16) (cid:17) (cid:17)−1 , (17)
= BT Q −1+Q −1 B
Φ ρ
whereQ
ρ
andQΦ arethecovariancematricesofthedouble-differencecodeandthecarrier-
phasemeasurements,respectively.
3.3. ProposedFault-FreePPP-RTKProtectionLevelEquation
TheintegerambiguityresolutionthroughLAMBDAisastochasticsearchprocess,and
basedonthebias-freeestimatesoffloatambiguities,itsupperboundprobabilityofcorrect
integerfixesis[24]
(cid:32) (cid:32) (cid:33) (cid:33)
∏n 1
Prob(aˇ =a) = CDF −1 (18)
i=1 2σ
aˆ i|I
where aˆ is the conditional least-squares estimate of integer ambiguity. Because the
i|I
correctnessofthefixedintegerambiguitiesmaysignificantlyaffectthepositionerrors,the
probabilityofEquation(18)mustbeconsideredinaprotection-levelequation. Aprotection
level(XPL)andgivenfault-freeriskprobability(I )canbeexpressedasfollows:
H0req
(cid:26)(cid:12) (cid:12) (cid:27)
(cid:12)^ (cid:12)
Prob (cid:12)x−x(cid:12) >XPL
H0
= I
H0req
, (19)
(cid:12) (cid:12)
^
wherexandxdenotetheestimatedpositionandtrueposition,respectively,inthehorizontal
orverticaldirections. XPL referstothehorizontalorverticalprotectionlevels. Because
H0
the position error may exceed XPL with correctly fixed (CF) or incorrectly fixed (IF)
H0
integerambiguities, Equation(19)canbeexpandedtotwoconditionalprobabilities, as
follows[9]:
(cid:26)(cid:12) (cid:12) (cid:27) (cid:26)(cid:12) (cid:12) (cid:12) (cid:27)
(cid:12)^ (cid:12) (cid:12)^ (cid:12) (cid:12)
Prob (cid:12)x−x(cid:12) >XPL
H0
=Prob (cid:12)x−x(cid:12) >XPL H0(cid:12)CF PCF
(cid:12) (cid:12) (cid:12) (cid:12) (cid:12)
(cid:26)(cid:12) (cid:12) (cid:12) (cid:27) (20)
(cid:12)^ (cid:12) (cid:12)
+Prob (cid:12)x−x(cid:12) >XPL H0(cid:12)IF PIF
(cid:12) (cid:12) (cid:12)
wherePCFistheprobabilityofthecorrectfix,whichcanbeestimatedfromEquation(18).
PIFistheprobabilityofincorrectfixandPCFequalsto1−PIF.
(cid:26)(cid:12) (cid:12) (cid:12) (cid:27)
(cid:12)^ (cid:12) (cid:12)
ConsideringProb (cid:12)x−x(cid:12) >XPL H0(cid:12)IF = 1asaconservativeapproach,thefault-
(cid:12) (cid:12) (cid:12)
freeriskprobabilitypresumingthatintegerambiguitiesarecorrectlyfixedis
(cid:26)(cid:12) (cid:12)^ (cid:12) (cid:12) (cid:12) (cid:12) (cid:27) I H0req −PIF
Prob (cid:12)
(cid:12)
x−x(cid:12)
(cid:12)
>XPL H0(cid:12)
(cid:12)
CF =
1−PIF
. (21)
Assuming that the position error follows a zero-mean Gaussian distribution, the
correspondingtailvalueofEquation(21)wasusedastheK factorinEquation(7).
ffmd
Using the total range error of CLAS, σ, in Equation (2), a weighting matrix for a
i
single-differencedrangingsourcecanbesimilarlyconstructedasinEquation(4). Because
VRS-RTK uses double-difference code and carrier phase measurements, Q
ρ
and QΦ in
Equation(17)canbeexpressedas
Q ρ =DW − ρ 1DT andQΦ =DW − Φ 1DT, (22)

<!-- PAGE: 7 -->

Sensors2022,22,3570 7of13
Sensors 2022, 22, x FOR PEER REVIEW 7 of 13
where D is the double-difference matrix. Using the K derived from Equation (21)
ffmd
and substituting Equation (23) into Equation (17), the fault-free horizontal and vertical
protectionlevHePlLeq=u𝐾ationswe𝜎re computedasfollows:
(cid:3033)(cid:3033)(cid:3040)(cid:3031),(cid:2892)(cid:2900)(cid:2896) (cid:3009)
HPL = = = 𝐾 (cid:3033) K K (cid:3033)(cid:3040) f (cid:3031) fm ,(cid:2892) d (cid:2900) ,H (cid:2896) (cid:3497) PL𝑸 (cid:118) (cid:117) (cid:117) (cid:116) σ (cid:3029)(cid:3544) H ((cid:2869) Q ,(cid:2869) bˇ ) (1 + , 2 1) + 𝑸 Q (cid:3029)(cid:3544) bˇ ( ( (cid:2870) 2 , , (cid:2870) 2) ) + + (cid:3496)(cid:115)(cid:3436) (cid:18) 𝑸 Q (cid:3029)(cid:3544)( bˇ (cid:2869) ( , 1 (cid:2869) ,1 ) ) − − 2 Q 𝑸 bˇ( (cid:3029) 2 (cid:3544) , ( 2 (cid:2870) ) , (cid:19) (cid:2870)) 2 (cid:3440) (cid:2870) + + Q 𝑸 2 (cid:3029) (cid:2870) (cid:3544)((cid:2869),(cid:2870)) (2 (2 3 3 ) )
ffmd,HPL 2 2 bˇ(1,2)
VPL=𝐾 (cid:3033)(cid:3033)(cid:3040)(cid:3031),(cid:2906)(cid:2900)(cid:2896) 𝜎 (cid:3023) =𝐾 (cid:3033)(cid:3033)(cid:3040)(cid:3031),(cid:2906)(cid:2900)(cid:2896)(cid:3493)𝑸 (cid:3029)(cid:3544)((cid:113)(cid:2871),(cid:2871)) .
VPL= K σ = K Q .
ffmd,VPL V ffmd,VPL bˇ(3,3)
In Equation (23), 𝑸 (cid:3029)(cid:3544) is evaluated in ENU coordinates.
InEquation(23),Q isevaluatedinENUcoordinates.
bˇ
4. Evaluation of the Proposed Protection Levels for PPP-RTK
4. EvaluationoftheProposedProtectionLevelsforPPP-RTK
This section discusses the GNSS observation data and parsing process of the CLAS
L6 broTahdicsassetc mtioenssdaigsecsu ussseesdt hine tGhNis SsStuodbys.e Srvuabtsieoqnudeanttalya,n tdhep raerssuinltgapntr opcoessistioofntihneg CerLrAorS oLf6
thbero VadRcSa-RstTmKe pssoasgiteisonuisnegd ainndth ciosmstpuudtye.dS upbroseteqcuteionntl yle,vtheelsr aerseu lptraenstepnotesdit.i oningerrorofthe
VRS-RTKpositioningandcomputedprotectionlevelsarepresented.
4.1. Experimental Data Processing
4.1. ExperimentalDataProcessing
To evaluate the performance of the proposed protection level, we used the GNSS
To evaluate the performance of the proposed protection level, we used the GNSS
observation data provided by the website of the Geospatial Information Authority of
observation data provided by the website of the Geospatial Information Authority of
Japan [25] and the L6 data provided by the website of the QZSS [26]. CLASLIB, an open-
Japan[25]andtheL6dataprovidedbythewebsiteoftheQZSS[26]. CLASLIB,anopen-
source software tool [26], was used to extract quality messages from the L6 broadcast data
sourcesoftwaretool[26],wasusedtoextractqualitymessagesfromtheL6broadcastdata
and generate the GNSS measurements for the VRS-RTK process.
andgeneratetheGNSSmeasurementsfortheVRS-RTKprocess.
CLASLIB is an open-source library that parses the CLAS L6 messages, and the
CLASLIBisanopen-sourcelibrarythatparsestheCLASL6messages,andtheprocess
process is shown in Figure 1. It converts the CLAS L6 messages to the observation space
isshowninFigure1. ItconvertstheCLASL6messagestotheobservationspacerepresenta-
representation of correction messages or provides parsed L6 message Type 4073 in
tionofcorrectionmessagesorprovidesparsedL6messageType4073incomma-separated
comma-separated value formats. CLASLIB can also generate VRS-RTK GNSS observation
valueformats. CLASLIBcanalsogenerateVRS-RTKGNSSobservationdatafromthegiven
data from the given GNSS navigation data and the corresponding L6 broadcast messages.
GNSSnavigationdataandthecorrespondingL6broadcastmessages.
FFigiguurere 11. .DDaatata exextrtaractcitoionn oof fCCLLAASS LL66 bbroroaaddccaasst tmmeessssaaggeess uussiningg CCLLAASSLLIBIB. .
Toevaluatetheproposedprotection-levelequations,GNSSdatawereobtainedfroma
To evaluate the proposed protection-level equations, GNSS data were obtained from
GEONETbasestationlocatedinChiyodaCity,Tokyo,Japan,asshowninFigure2. Thetest
a GEONET base station located in Chiyoda City, Tokyo, Japan, as shown in Figure 2. The
siteislocatedwithintheCLASservicevolume. TheGNSSdatasetconsistedoftheGPS
test site is located within the CLAS service volume. The GNSS dataset consisted of the
andGalileoRINEXobservationandnavigationfilescollectedover7daysfrom00:00:00
GPS and Galileo RINEX observation and navigation files collected over 7 days from
on11April2021,to23:59:30on17April2021,with30sintervals. Thebasestationuses
00:00:00 on 11 April 2021, to 23:59:30 on 17 April 2021, with 30 s intervals. The base station
a Trimble NETR9 receiver and a Trimble TPSCR.G5C antenna. The numbers of visible
uses a Trimble NETR9 receiver and a Trimble TPSCR.G5C antenna. The numbers of
GPSandGalileosatellitesduringthisperiodareshowninFigure3. Becausethesatellite
visible GPS and Galileo satellites during this period are shown in Figure 3. Because the
constellationexhibitsatrendsimilartothatofadailycycle, onlythenumberofvisible
satellite constellation exhibits a trend similar to that of a daily cycle, only the number of
satellitesin1dayisshown. Figures4and5showthetimeseriesoftheσ andσ ,
i,iono i,tropo
vriessibpleec stiavteellyli,teesx tirna c1t eddayfr iosm shtohwedna. tFaisgeutr.eFsi g4u arned6 5s hsohwows tthhee ttiimmees seerrieiesso offt htheeσ σ fo arnthde
i,sii,siono
σGPSa
,
n
re
d
sp
G
e
a
c
l
t
i
i
l
v
eo
el
s
y
a
,
t
e
e
x
ll
t
i
r
t
a
e
c
s
t
.
e
T
d
h
f
e
ro
u
m
se
t
r
h
r
e
e c
d
e
a
i
t
v
a
e
s
r
e
m
t. F
u
i
l
g
ti
u
p
r
a
e
t h
6
a
sh
n
o
d
w
n
s
o i
t
s
h
e
e
u
ti
n
m
ce
e
r
s
ta
er
in
ie
t
s
y
o
o
f
f
t
t
h
h
e
e σcode
i,tropo i,sis
for the GPS and Galileo satellites. The user receiver multipath and noise uncertainty of the

<!-- PAGE: 8 -->

Sensors 2022, 22, x FOR PEER REVIEW 8 of 13
SSenensosrosrs2 022022,22, 22,23, 5x7 F0OR PEER REVIEW 88o off1 133
code and carrier-phase measurements are modelled as
σ =15
in centimeters and
acnoddec aarnrdie cr-aprrhiaesre-pmhaesaes umreeamsuenretms aernetsm aored melloeddelalsedσ asus eσr,code = =sin(11E55l) in inc ecnetnitmimeteetresrsa anndd
σ uσseσ u r, s c u e a s r r e r , r i c e , r a ca r r = r r i ie e r r 3 s=i=n(E3l ss ) ini n( i E n ( 3 lE) m l ) in i i l nm lim mill e iil t ml e im r e s te , e t r re e sr s ,s p r,e e rs c ep t s i ep v ce e tc l i y tvi , ev a ley n l,y d ,a an a n r d e d a t ar h u er e s e t e t r ht y , h c e p ou e ds t i ee y c r t , y a p co l p d i l e c y iac s a u l in lly s ( l e y Es i u n d l() us E v l es ) ed a d l u vv e aa s lu . l ueess. .
Figure 2. GNSS data obtained from a GEONET base station located at Chome-1 Nagatacho, Chiyoda
Figure 2. GNSS data obtained from a GEONET base station located at Chome-1 Nagatacho, Chiyoda
CitFyi,g Tuorkey2o. G10N0S-0S0d14a,t aJaopbatnai n(3e5d.6f7ro7°m laatiGtuEdOe NanEdT 1b3a9s.e74st8a°t iloonngloitcuadteed) [a2t7C].h ome-1Nagatacho,Chiyoda
C
C
it
i
y
ty
,T
,
o
T
k
o
y
k
o
yo
1 0
1
0
0
-
0
0
-
0
0
1
0
4
1
,
4
J
,
a
J
p
a
a
p
n
an
(3
(
5
3
.
5
6
.
7
6
7
7◦7°
la
l
t
a
i
t
t
i
u
tu
d
d
e
e
a n
an
d
d
1 3
1
9
3
.
9
7
.
4
7
8
4◦8°
l o
lo
n
n
g
g
it
i
u
tu
d
d
e
e
)
)
[ 2
[2
7
7
].
].
8
8
GPS
7.5 GALGPS
7.5 GAL
7
7
6.5
6.5
6
6
5.5
5.5
5
5
4.5
4.5
4
4
3.5
3.5
3
3 500 1000 1500 2000 2500
500 1000 1500 2000 2500
Epoch [30 s]
Epoch [30 s]
FigFuigreu r3e. N3.uNmubmerb oerf voifsvibisleib GlePGS PaSndan GdaGlilaeloil esoatsealltietlelsit edsudriunrgin ag daady aiyn itnhet h7e-d7a-dy apyeprieordio. d.
Figure 3. Number of visible GPS and Galileo satellites during a day in the 7-day period.
4.2. ComparisonoftheVRS-RTKPositionErrorsandComputedProtectionLevels
Figure 7 shows the resultant ENU position errors of zero-baseline VRS-RTK using
dual-frequency GPS and Galileo satellites with the test dataset. To determine the fixed
integers,aconventionaltestvalueratio,above3,wasused. TheRMSofthepositioning
errors with the fixed integers is 4, 2, and 14 cm in the East, North, and up directions,
respectively. Atcertainepochs,ourVRS-RTKsoftwarefailedtoresolvefixedintegersdue
tocycleslips. Forthisparticulartest,2.5%ofthedatacontainedafloatsolution.

<!-- PAGE: 9 -->

Sensors 2022, 22, x FOR PEER REVIEW 9 of 13
Sensors 2022, 22, x FOR PEER REVIEW 9 of 13
Sensors2022,22,3570 9of13
GPS L1
Iono
GPS L1
0.35 Iono
0.35
0.3
0.3
0.25
0.25
0.2
0.2
0.15
0.15
0.1
0.1
0.05
0.05
0
0 500 1000 1500 2000 2500
500 1000Epoch1 [53000 s] 2000 2500
Epoch [30 s]
Figure 4. Time series of the Ionospheric correction quality, σ , in meters.
iono
FFiigguurree 44.. TTiimmees seerireiseso fotfh tehIeo nIoonspohsperhicerciocr rceocrtrioenctqiounal iqtyu,aσlity, ,σinm,e tienr sm. eters.
iono iono
Fi F g i u gu re re 5 5 . . T T i i m m e e s se e r r i i e e s s o o f f t h th e e T r T o r p o o p s o p s h p e h re e c r o e r c re o c r t r i e o c n ti q o u n a l q it u y, a σ littroyp,o 𝜎 ,inm , e i t n er m s. eters.
tropo
Figure 5. Time series of the Troposphere correction quality, 𝜎 , in meters.
Figures8and9showthecomputedprotectionlevelsatnrodpot hepositionerrorsforthe
fixedintegerscaseswithafault-freeriskprobability(I )of10−7. Ifthetestvalueratio
H0req
was less than 3, that is, float solutions, no protection levels were computed. As shown
in Figures 8 and 9, all of the computed HPL and VPL were larger than the horizontal
positioningerrors(HPE)andverticalpositioningerrors(VPE),respectively. TheRMSof
theHPEwas4.6cmwhereasthatoftheHPLrangedfrom25cmto2.3m. TheRMSofthe
VPEwas14cm,whereastheVPLrangedfrom50cmto5.2m. Atcertainepochs,thereare
largepeaksintheHPLandVPL,andthesepeaksoccurwhenthereisajumpinquality
indices. TheselargeprotectionlevelsoccurredatverysmallpercentagessuchthatHPL
waslessthan1min99.4%andVPLwaslessthan3min99.6%ofthedataset,respectively.

<!-- PAGE: 10 -->

Sensors 2022, 22, x FOR PEER REVIEW 10 of 13
GPS GAL
sis sis
0.25 0.25
0.2 0.2
Sensors 2022, 22, x FOR PEER REVIEW 10 of 13
Sensors2022,22,3570 0.15 0.15 10of13
GPS GAL
0.1 0.1
sis sis
0.25 0.25
0.05 0.05
0.2 0.2
0 0
500 1000150020002500 500 1000150020002500
0.15 0.15
Epoch [30 s] Epoch [30 s]
Figure 6. Time series of the Signal in Space correction quality, 𝜎 , for GPS and Galileo satellites.
sis
0.1 0.1
4.2. Comparison of the VRS-RTK Position Errors and Computed Protection Levels
Figure 7 shows the resultant ENU position errors of zero-baseline VRS-RTK using
0.05 0.05
dual-frequency GPS and Galileo satellites with the test dataset. To determine the fixed
integers, a conventional test value ratio, above 3, was used. The RMS of the positioning
errors wit0h the fixed integers is 4, 2,0 and 14 cm in the East, North, and up directions,
500 1000150020002500 500 1000150020002500
respectively. At certain epochs, our VRS-RTK software failed to resolve fixed integers due
Epoch [30 s] Epoch [30 s]
to cycle slips. For this particular test, 2.5% of the data contained a float solution.
FigFuigruer e6.6 .TTiimmees sereiresieosf tohfe tShigen aSliignnSapal cienc oSrpreacctieon cqourarleitcy,tiσosins , qfouraGlPitSya,n 𝜎d
s
G
is
a ,l ifleoor sGatePllSit easn. d Galileo satellites.
4.2. Comparison of the VRS-RTK Position Errors and Computed Protection Levels
Figure 7 shows the resultant ENU position errors of zero-baseline VRS-RTK using
dual-frequency GPS and Galileo satellites with the test dataset. To determine the fixed
integers, a conventional test value ratio, above 3, was used. The RMS of the positioning
errors with the fixed integers is 4, 2, and 14 cm in the East, North, and up directions,
respectively. At certain epochs, our VRS-RTK software failed to resolve fixed integers due
to cycle slips. For this particular test, 2.5% of the data contained a float solution.
Figure7.VRS−RTKpositionerrorsforfloatandfixedintegercaseswiththetestdataset.
Figure 7. VRS−RTK position errors for float and fixed integer cases with the test dataset.
Figures 8 and 9 show the computed protection levels and the position errors for the
fixed integers cases with a fault-free risk probability (𝐼 ) of 10−7. If the test value ratio
(cid:3009)(cid:2868)(cid:3045)(cid:3032)(cid:3044)
was less than 3, that is, float solutions, no protection levels were computed. As shown in
Figures 8 and 9, all of the computed HPL and VPL were larger than the horizontal
positioning errors (HPE) and vertical positioning errors (VPE), respectively. The RMS of
the HPE was 4.6 cm whereas that of the HPL ranged from 25 cm to 2.3 m. The RMS of the
VPE was 14 cm, whereas the VPL ranged from 50 cm to 5.2 m. At certain epochs, there are
laFrigguer pe e7a. kVsR Sin− RthTKe HpoPsLit ioann der VroPrsL f,o arn fldo atth aensde fpixeeadk sin otecgceurr c awsehse wn itthh etrhee itse sat djuamtaspe ti.n quality
Figures 8 and 9 show the computed protection levels and the position errors for the
fixed integers cases with a fault-free risk probability (𝐼 ) of 10−7. If the test value ratio
(cid:3009)(cid:2868)(cid:3045)(cid:3032)(cid:3044)
was less than 3, that is, float solutions, no protection levels were computed. As shown in
Figures 8 and 9, all of the computed HPL and VPL were larger than the horizontal
positioning errors (HPE) and vertical positioning errors (VPE), respectively. The RMS of
the HPE was 4.6 cm whereas that of the HPL ranged from 25 cm to 2.3 m. The RMS of the
VPE was 14 cm, whereas the VPL ranged from 50 cm to 5.2 m. At certain epochs, there are
large peaks in the HPL and VPL, and these peaks occur when there is a jump in quality

<!-- PAGE: 11 -->

Sensors 2022, 22, x FOR PEER REVIEW 11 of 13
Sensors 2022, 22, x FOR PEER REVIEW 11 of 13
indices. These large protection levels occurred at very small percentages such that HPL
was less than 1 m in 99.4% and VPL was less than 3 m in 99.6% of the dataset, respectively.
indices. These large protection levels occurred at very small percentages such that HPL
Sensors2022,22,3570 11of13
was less than 1 m in 99.4% and VPL was less than 3 m in 99.6% of the dataset, respectively.
2.5
HPE
2.5 HPL
HPE
2 HPL
2
1.5
1.5
1
1
0.5
0.5
0
00 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
0 0.2 0.4 0.6 0E.8poch1 [301 .s2] 1.4 1.6 1.8 1204
Epoch [30 s] 104
Figure 8. Comparison of the horizontal protection levels and horizontal position errors from the test
Figure 8. Comparison of the horizontal protection levels and horizontal position errors from the test
dataFsiegtu. re 8. Comparison of the horizontal protection levels and horizontal position errors from the
dataset.
testdataset.
6
6
VPE
VPVEPL
VPL
5
5
4
4
33
22
11
00
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
E E p p o o c c h h [ [ 3 3 0 0 s s ] ] 10 1 4 04
Figure 9. Comparison of the vertical protection levels and vertical position errors from the test
FiguFrieg u9r.e C9o.mpCaormisopna roisfo tnheo fvetrhteicavle rptriocatelcptiroont elcetvioenls laenvde lsvearntidcalv eprotsicitailonp oesrirtoiorsn ferorrmo rtshefr otemst the
dataset.
dataset.
testdataset.
5. Discussion
5. D5i.sDcuisssciuosns ion
σ
The broadcast of the correction messages in SBAS or CLAS is typically much
The
T
b
h
r
e
o
b
a
r
d
o
c
a
a
d
s
c
t
aσstiσ
io
o
f
f
t
t
h
h
e
e
c
c
o
o
r
r
r
r
e
e
c
c
t
t
i
i
o
on
n
m
m
e
e
s
s
s
s
a
a
g
g
e
e
s
s
in
in
S
S
B
B
A
A
S
S
o r
o
C
r
L
C
A
L
S
A
i
S
s t
is
y p
ty
ic
p
a
i
l
c
ly
al
m
ly
u
m
ch
u
l
c
a
h
r ger
lartghearn tthhaena tchteu aalcctuoarrl e iccotirorencetirorno redrriostrr idbiusttrioibnubtieocna ubseecaituisse initt eisn itniotennatliloynianlfllya tiendfltaoteodv etor bound
larger than the actual correction error distribution because it is intentionally inflated to
ovtehreboreusnidd uthael ererrsoidrusainl errarnorgse inm reaansguer emmeeansutsresmucehnttsh sautcthh ethpart othteec ptiroontelcetvioenls laevlseolso avlseorb ound
overbound the residual errors in range measurements such that the protection levels also
ovtehrebopuonsdit itohne eprorsoirtisoanf teerrroarps palfyteinr gapthpelycinogrr tehceti oconrrmecetsiosang mese.sIsnagVesR. SI-nR VTRKS,-tRhTeKu,n tcheer tainty
overbound the position errors after applying the correction messages. In VRS-RTK, the
unocferthtaeindtoyu obfl eth-de idffoeurebnlec-edcifofdereenanced ccoadreri earndp hcaasreriemr epahsausree mmeenast,uQre
ρ
maenndt, QQ Φρ, arensdp eQc
Φ
ti,v ely,is
uncertainty of the double-difference code and carrier phase measurement, Q and Q ,
resupseecdtitvoelsyo,l vise uthseedfl tooa tsoblavsee ltihnee falnoadt ibnatesgeleirnea manbdig iunitteiegse.r Tahmebni,gtuhietifleso.a Tthinetne,g tehρrea fmlobaitg Φuities
reinsptaeengcdetirvt heaelmyir,b aiisgs suuoistcieieadst etaodn scdoo lvtvhaere iitarh neac sefslomoacaita tbtreiacdse eslciaonrveea aruinasdend cieni ntmetghaeterr ircaeem-sp baairgraeum itueiestsee.dr iT zhiante inot,nh teha ner def-lsoeaat rch
inptaeprgareomrc eeatdemruibrzeaigtfiuooirnti ienastn edga nesrde aarmtchhbe iigrp uroaitcsiesedosc.uirIaeft eQfdoρ r acinonvdtaeQgrieaΦrn acareme bcmioganutsrittiirceuessc. teIafd reQu s
ρ
uin sagenddt h ieQnb
Φ
rto haaerd e craes-ted
parσaimfreotemrizCaLtiAonS ,tahnedL AseMarBchD Aprporcoecdeusrseh afosra ivnetreygelar rgaemsbeiagrucihtiseps.a cIef aQnd
ρ
aanhdig hQc
Φ
ha anrcee of
findingincorrectintegerambiguities. Therefore,therealisticvaluesofQ
ρ
andQΦ should
beusedtosuccessfullyresolvetheintegerambiguitiesinLAMBDA.
In the test results, the RMS errors in the up direction are relatively larger than in
theEastandNorthdirections. Themeanvalueoftheverticalpositionerrorshadabias
of approximately 12 cm. We also observed a similar bias from zero-baseline VRS-RTK
positionerrorswiththesamedatasetusinganopen-sourcesoftwaretool[28]. Therefore,

<!-- PAGE: 12 -->

Sensors2022,22,3570 12of13
itispresumedthattherewasabiasinthereportedtrueantennapositionsoftheGNSS
datasetusedinthetest. Thisissuewillbeinvestigatedfurther.
Infact,whetherthereceivermovesornot,protectionlevelscanbecomputedinthe
samewayaslongthePPP-RTKprocessisadequatelyimplemented. However,adynamic
receivermaysufferfromafrequentlossandinclusionofsatellites,whichmayoveralllower
thePCFofintegerambiguitiesandresultinincorrectintegerambiguities. Theresearchon
thisissuewillalsobecarriedoutasfuturework.
6. Conclusions
This paper presents a fault-free protection level equation for the CLAS PPP-RTK
servicethatbroadcastedcorrectionqualitymessages. Theperformanceoftheproposed
protectionlevelequationswastestedusing7daysoftheGNSSobservationdataandthe
CLASL6messagesobtainedatabasestationinTokyo,Japan,whichwaslocatedwithin
the CLAS service region. The test results with 7 days of GNSS data showed that the
HPLandVPLwerealwayslargerthantheHPEandVPEofthezero-baselineVRS-RTK
solution. Furthermore,fault-freeprotection-levelviolationswerenotobserved. Itshould
be noted that most HPL and VPL values were less than 1 and 3 m, respectively. Since
arailautomation, whichisaverydemandingproblemfromanintegritypointofview,
requiresHorizontalAlertLimitof1m[29],theproposedprotectionlevelwouldbeable
to fulfill stringent integrity and availability requirements for many applications using
PPP-RTKservices.
AuthorContributions:Protection-levelequationdevelopment,E.K.;GNSSandCLASdataprocess-
ing,J.S.,Y.S.andS.K.;validation,P.-W.S.,S.P.(SulgeePark)andS.P.(SanghyunPark).Allauthors
havereadandagreedtothepublishedversionofthemanuscript.
Funding: Thisresearchwaspartoftheprojecttitled“DevelopmentofGround-basedCentimeter-
levelMaritimePrecisePNTTechnologies”,fundedbytheMinistryofOceansandFisheries,Korea
(No.PMS5110).ThisworkwasalsosupportedbyaNationalResearchFoundationofKorea(NRF)
grantfundedbytheKoreangovernment(MSIT)(No.2020R1A2C2006028).
Acknowledgments:TheauthorsthankChanheeLeeforhishelpwiththepreparationofthispaper.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Pervan,B.Ground-BasedAugmentationSystem.InPosition,Navigation,andTimingTechnologiesinthe21stCentury:Integrated
SatelliteNavigation,SensorSystems,andCivilApplications,Volume1;Wiley:Hoboken,NJ,USA,2020;pp.259–276.
2. Walter,T.SatelliteBasedAugmentationSystems. InSpringerHandbookofGlobalNavigationSatelliteSystems;Springer: Cham,
Switzerland,2017;pp.339–361.
3. Pullen, S.; Walter, T.; Enge, P. SBAS and GBAS Integrity for Non-Aviation Users: Moving Away from “Specific Risk”. In
Proceedingsofthe2011InternationalTechnicalMeetingofTheInstituteofNavigation,SanDiego,CA,USA,24–26January2011;
pp.533–545.
4. Pullen,S.AugmentedGNSS:FundamentalsandKeystoIntegrityandContinuity.Availableonline:http://www-leland.stanford.
edu/~{}spullen/ION12_tutorial.pdf(accessedon25March2022).
5. DeCleene,B.DefiningPseudorangeIntegrity-Overbounding.InProceedingsofthe13thInternationalTechnicalMeetingofthe
SatelliteDivisionofTheInstituteofNavigation(IONGPS2000),SaltLakeCity,UT,USA,19–22September2000;pp.1916–1924.
6. Rife,J.;Pullen,S.;Pervan,B.;Enge,P.PairedOverboundingandApplicationtoGPSAugmentation.InProceedingsofthePLANS
2004. PositionLocationandNavigationSymposium(IEEECat. No.04CH37556),Monterey,CA,USA,26–29April2004;pp.
439–446.
7. Rife,J.;Pullen,S.;Pervan,B.CoreOverboundingandItsImplicationsforLAASIntegrity.InProceedingsofthe17thInternational
Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS 2004), Long Beach, CA, USA, 21–24
September2004;pp.2810–2821.
8. Walter,T.;Blanch,J.;Rife,J.TreatmentofBiasedErrorDistributionsinSBAS.J.Glob.Position.Syst.2004,3,265–272.[CrossRef]
9. Miya,M.;Fujita,S.;Sato,Y.;Ota,K.;Hirokawa,R.;Takiguchi,J.CentimeterLevelAugmentationService(CLAS)inJapanese
Quasi-ZenithSatelliteSystem,ItsUserInterface,DetailedDesign,andPlan.InProceedingsofthe29thInternationalTechnical
MeetingoftheSatelliteDivisionofTheInstituteofNavigation(IONGNSS+2016),Portland,OR,USA,12–16September2016;pp.
2864–2869.

<!-- PAGE: 13 -->

Sensors2022,22,3570 13of13
10. Miya,M.;Fujita,S.;Sato,Y.;Kaneko,K.;Shima,Y.;Hirokawa,R.;Sone,H.;Takiguchi,J.CentimeterLevelAugmentationService
(CLAS)inJapaneseQuasi-ZenithSatelliteSystem,DesignforSatelliteBasedRTK-PPPServices. InProceedingsofthe28th
InternationalTechnicalMeetingoftheSatelliteDivisionofTheInstituteofNavigation(IONGNSS+2015),Tampa,FL,USA,14–18
September2015;pp.1958–1962.
11. Miya,M.;Sato,Y.;Fujita,S.;Motooka,N.;Saito,M.;Takiguchi,J.CentimeterLevelAugmentationService(CLAS)inJapaneses
Quasi-ZenithSatelliteSystem,ItsPreliminaryDesignandPlan.InProceedingsofthe27thInternationalTechnicalMeetingofthe
SatelliteDivisionofTheInstituteofNavigation(IONGNSS+2014),Tampa,FL,USA,8–12September2014;pp.645–652.
12. Fujita,S.;Sato,Y.;Miya,M.;Ota,K.;Hirokawa,R.;Takiguchi,J.DesignofIntegrityFunctiononCentimeterLevelAugmentation
Service(CLAS)inJapaneseQuasi-ZenithSatelliteSystem. InProceedingsofthe29thInternationalTechnicalMeetingofthe
SatelliteDivisionofTheInstituteofNavigation(IONGNSS+2016),Portland,OR,USA,12–16September2016;pp.3258–3263.
13. Hirokawa,R.;Sato,Y.;Fujita,S.;Miya,M.CompactSSRMessageswithIntegrityInformationforSatelliteBasedPPP-RTKService.
InProceedingsofthe29thInternationalTechnicalMeetingoftheSatelliteDivisionofTheInstituteofNavigation(IONGNSS+
2016),Portland,OR,USA,12–16September2016;pp.3372–3376.
14. Feng,S.;Ochieng,W.;Moore,T.;Hill,C.;Hide,C.CarrierPhase-BasedIntegrityMonitoringforHigh-AccuracyPositioning.GPS
Solut.2009,13,13–22.[CrossRef]
15. Madrid, P.; Saenz, M.; Varo, C.; Schortmann, J. Computing Meaningful Integrity Bounds of a Low-Cost Kalman-Filtered
NavigationSolutioninUrbanEnvironments.InProceedingsofthe28thInternationalTechnicalMeetingoftheSatelliteDivision
ofTheInstituteofNavigation(IONGNSS+2015),Tampa,FL,USA,14–18September2015;pp.2914–2925.
16. Azaola,M.;Calle,D.;Mozo,A.;Piriz,R.AutonomousIsotropy-BasedIntegrityUsingGPSandGLONASS.InProceedingsofthe
23rdInternationalTechnicalMeetingoftheSatelliteDivisionofTheInstituteofNavigation(IONGNSS2010),Portland,OR,USA,
21–24September2010;pp.2135–2147.
17. El-Mowafy, A.; Kubo, N. Integrity Monitoring of Vehicle Positioning in Urban Environment Using RTK-GNSS, IMU and
Speedometer.Meas.Sci.Technol.2017,28,055102.[CrossRef]
18. Blanch,J.;Walter,T.;Enge,P.;Wallner,S.;Fernandez,F.;Dellago,R.;Ioannides,R.;Hernandez,I.;Belabbas,B.;Spletter,A.;etal.
CriticalElementsforaMulti-ConstellationAdvancedRAIM.Navig.J.Inst.Navig.2013,60,53–69.[CrossRef]
19. Khanafseh,S.;Pervan,B.NewApproachforCalculatingPositionDomainIntegrityRiskforCycleResolutioninCarrierPhase
NavigationSystems.IEEETrans.Aerosp.Electron.Syst.2010,46,296–307.[CrossRef]
20. Zabalegui,P.;DeMiguel,G.;Perez,A.;Mendizabal,J.;Goya,J.;Adin,I.AReviewoftheEvolutionoftheIntegrityMethods
AppliedinGNSS.IEEEAccess2020,8,45813–45824.[CrossRef]
21. JapanCabinetOffice.Quasi-ZenithSatelliteSystemInterfaceSpecification:CentimeterLevelAugmentationService(IS-QZSS-L6-
004),July2021.Availableonline:https://qzss.go.jp/en/technical/download/pdf/ps-is-qzss/is-qzss-l6-004.pdf(accessedon25
March2022).
22. deJonge,P.;Tiberius,C.IntegerAmbiguityEstimationwiththeLambdaMethod.InGPSTrendsinPreciseTerrestrial,Airborne,and
SpaceborneApplications;Springer:Berlin/Heidelberg,Germany,1996;pp.280–284.
23. Teunissen,P.J.G.Least-SquaresEstimationoftheIntegerGPSAmbiguities.Availableonline:https://gnss.curtin.edu.au/wp-
content/uploads/sites/21/2016/04/Teunissen1993Least.pdf(accessedon25March2022).
24. Teunissen,P.J.G.SuccessProbabilityofIntegerGPSAmbiguityRoundingandBootstrapping.J.Geod.1998,72,606–612.[CrossRef]
25. WelcometoGSI|GSIHOMEPAGE.Availableonline:https://www.gsi.go.jp/ENGLISH/(accessedon21March2022).
26. Centimeter Level Augmentation Service (CLAS)|Service Overview|QZSS (Quasi-Zenith Satellite System)—Cabinet Office
(Japan).Availableonline:https://qzss.go.jp/en/overview/services/sv06_clas.html(accessedon21March2022).
27. EarthExplorer.Availableonline:https://earthexplorer.usgs.gov/(accessedon6May2022).
28. Takasu,T.;Yasuda,A.DevelopmentoftheLow-CostRTK-GPSReceiverwithanOpenSourceProgramPackageRTKLIB.In
ProceedingsoftheInternationalsymposiumonGPS/GNSS,Seogwipo,Korea,4–6November2009.
29. Rispoli,F.;Enge,P.;Neri,A.;Senesi,F.;Ciaffi,M.;Razzano,E.GNSSforRailAutomation&DriverlessCars:AGiveandTake
Paradigm.InProceedingsofthe31stInternationalTechnicalMeetingoftheSatelliteDivisionofTheInstituteofNavigation(ION
GNSS+2018),Miami,FL,USA,24–28September2018;pp.1468–1482.[CrossRef]