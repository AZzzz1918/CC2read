<!-- PAGE: 1 -->

remote sensing
Article
Analysis of BDS-3 PPP-B2b Positioning and Time
Transfer Service
RunzhiZhang1,2,3 ,ZaiminHe4,*,LangmingMa1,3,GongweiXiao4,5,WeiGuang4,YulongGe6,
XiangboZhang1,2,3 ,JihaiZhang1,2,3,JianTang7andXueqingLi1,3
1 NationalTimeServiceCenter,ChineseAcademyofSciences,Xi’an710600,China;
zhangrunzhi@ntsc.ac.cn(R.Z.);malm@ntsc.ac.cn(L.M.);zxiangb@ntsc.ac.cn(X.Z.);zhangntsc@126.com(J.Z.);
lixueqing@ntsc.ac.cn(X.L.)
2 KeyLaboratoryofTimeandFrequencyPrimaryStandards,ChineseAcademyofSciences,Xi’an710600,China
3 UniversityofChineseAcademyofSciences,Beijing100049,China
4 SchoolofCommunicationsandInformationEngineering&SchoolofArtificialIntelligence,
Xi’anUniversityofPostsandTelecommunications,Xi’an710121,China;xiaogongwei@xupt.edu.cn(G.X.);
weiguang@foxmail.com(W.G.)
5 StateKeyLaboratoryofGeodesyandEarth’sDynamics,InnovationAcademyforPrecisionMeasurement
ScienceandTechnology,ChineseAcademyofSciences,Wuhan430077,China
6 SchoolofMarineScienceandEngineering,NanjingNormalUniversity,Nanjing210023,China;
geyulong@njnu.edu.cn
7 CollegeofElectronicEngineering,NationalUniversityofDefenseTechnology,Hefei230037,China;
jian_t@163.com
* Correspondence:hezaimin@xupt.edu.cn;Tel.:+86-139-9287-6519
Abstract:WiththecompletionoftheBeiDouglobalnavigationsatellitesystem(BDS-3),theBeiDou
NavigationSatelliteSystemSignalInSpaceInterfaceControlDocumentPrecisePointPositioning
ServiceSignalPPP-B2b(Version1.0)wasofficiallyannounced,andBDS-3officiallybroadcastPPP-
B2bcorrectiontobroadcastephemeristhroughgeostationaryearthorbit(GEO)satellitestoprovide
precisepointpositioningservicesforusersintheAsia–Pacificregion.Thisstudycomprehensively
Citation:Zhang,R.;He,Z.;Ma,L.;
analyzestheapplicationofthePPP-B2bproducttotimetransferandpositioning.Onadailybasis,
Xiao,G.;Guang,W.;Ge,Y.;Zhang,X.;
thePPP-B2bpositioningaccuracyafterconvergenceiscalculatedusingthefourionosphere-free(IF)
Zhang,J.;Tang,J.;Li,X.Analysisof
combinationsinstaticandsimulatedkinematicmodes:BDSB1I/B3I,BDSB1C/B2a,BDSB1I/B3I+GPS,
BDS-3PPP-B2bPositioningandTime
andBDSB1C/B2a+GPS.ObservationsoftimelaboratoriesincludingtheNationalTimeService
TransferService.RemoteSens.2022,
CenteroftheChineseAcademyofSciences(NTSC)andtheTelecommunicationLaboratories(TL)are
14,2769. https://doi.org/10.3390/
rs14122769 employedtoconductzero-baselinecommonclockdifference(CCD)timecomparisonexperiments
andlong-baselinetimecomparisonexperimentsusingthePPP-B2bproductandtheGBMproduct.
AcademicEditor:AliKhenchaf
TheresultsindicatethatthePPP-B2bpositionaccuracyinstaticmodebyonlyBDSis1.5/2.7/3.9cm,
Received:26April2022 andbyGPS+BDSiswithin1.5/2.5/3.5cminNorth,East,andUpdirections,respectively.Regarding
Accepted:6June2022 simulatedkinematicPPP-B2b,theaveragerootmeansquare(RMS)valuesofthepositionerrorsin
Published:9June2022 theNorth,East,andUpdirectionsforthecombinationofBDSB1I/B3I+GPSandBDSB1I/B3Iare
Publisher’sNote:MDPIstaysneutral 3.4/5.8/7.6cmand3.8/6.6/7.8cm,respectively.Simultaneously,theaverageRMSvaluesofposition
withregardtojurisdictionalclaimsin errorsusingBDSB1C/B2a+GPSandBDSB1C/B2aare3.6/4.9/8.1cmand4/6.1/8.5cm. Inthe
publishedmapsandinstitutionalaffil- timecomparisonstudy,theresultsofzero-baselineCCDusingthePPP-B2bproductandtheGBM
iations. productarewithinthefluctuationrangeof0.1ns,respectively.Particularly,thelong-baselinetime
comparisondifferencebetweenresultsemployingthePPP-B2bproductandtheGBMproductis
withintherangeof±0.5ns.
Copyright: © 2022 by the authors.
Keywords:BDS-3;PPP-B2b;precisepointpositioning;timetransfer
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditionsoftheCreativeCommons
1. Introduction
Attribution(CCBY)license(https://
creativecommons.org/licenses/by/ TheBeiDounavigationsatellitesystem(BDS)independentlyestablishedandoperated
4.0/). byChina,asoneofthefourmajorglobalnavigationsatellitesystems,aimstoprovideglobal
RemoteSens.2022,14,2769.https://doi.org/10.3390/rs14122769 https://www.mdpi.com/journal/remotesensing

<!-- PAGE: 2 -->

RemoteSens.2022,14,2769 2of21
userswithpositioning,navigation,andtimingservices. TheBeiDounavigationsatellite
systemisdevelopedinthreestages,withservicesrangingfromChinatotheAsia–Pacific
region,andfinallytotheworld[1]. InMay2003,thethirdgeostationaryearthorbitsatellite
waslaunched,andtheBeiDoudemonstrationnavigationsystem(BDS-1)wasestablished,
providingChinawithpositioning,timing,andshortmessagecommunicationservices[2].
Bytheendof2012,withthelaunchof14networkedsatellitesincluding5geostationary
earthorbitsatellites,5inclinedgeosynchronousorbit(IGSO)satellites,and4mediumearth
orbit (MEO) satellites, the BeiDou regional navigation system (BDS-2) was established
anditsservicescopewasextendedtotheAsia–Pacificregion. AttheendofJuly2020,it
wasofficiallyannouncedthattheBeiDouglobalnavigationsatellitesystem,comprising
24MEOsatellites,3GEOsatellites,and3IGSOsatellites,wascompleted. Sincethen,BDS-3
has provided global users with positioning, navigation and timing (PNT), global short
messagecommunication(GSMC),andinternationalsearchandrescue(SAR),andprovided
asatellite-basedaugmentationsystem(SBAS),agroundaugmentationsystem(GAS)as
wellasprecisepointpositioning(PPP)andregionalshortmessagecommunication(RSMC)
servicesforusersinChinaanditssurroundingareas[3–8].
PPP[9–11]playsanimportantroleintheglobalnavigationsatellitesystem(GNSS)
high-precisionpositioningapplications. Itreceivescarrierphaseobservationsandpseu-
dorangeobservationsthroughasingleGNSSreceiver,usespreciseproductsandmodel
empiricalformulastocorrecterrors,andusesleastsquares,Kalmanfiltering,andother
methodstodeterminehigh-precisionabsolutecoordinates[11]. Initially,theinternational
GNSSservice(IGS)onlyprovidesprecisesatelliteclockandorbitproductswithacertain
delay,whichlimitsthePPPstudytofocusonpost-processing. Inordertoobtainprecise
products with the shortest possible latency, the IGS launched a real-time pilot project
(RTPP) in 2007. In 2013, real-time data streaming services via Networked Transport of
RTCM(RadioTechnicalCommissionforMaritimeServices)viaInternetProtocol(NTRIP)
wasofficiallyprovided,servinguserswithreal-timeandfreecorrectionproductsrequired
forPPP[12–14]. Theemergenceofreal-timeproductshaspromotedtheresearchofPPP
inpositioningandtimetransfer. Refs.[14–20]demonstratedthatthesimulatedkinematic
positioningaccuracyusingreal-timeproductsisbetterthanonedecimeterandthattime
transfercanachievesub-nanosecondaccuracy. However,theNTRIPprotocolrequiresa
communicationnetwork,makingitimpossibletobeappliedinareaswithlimitednetwork
connections. SomenavigationsystemsprovideuserswithPPPservicesbybroadcasting
correctionstothenavigationephemeristhroughsatellitestosolvetheproblemofreal-time
correctionproducts’dependenceonthecommunicationnetwork. TheQuasi-ZenithSatel-
liteSystem(QZSS)usesanL6signaltoprovidecentimeter-levelaugmentationservices
(CLAS)forusersintheJapanesearea. Currently,theCLASservicessupportGPS,QZSS,
andGalileosystems[21]. Galileoprovidesfreehigh-precisionPPPservicesforGPSand
GalileousersthroughE6-Bsignals[22]. InAugust2020, theChinaSatelliteNavigation
OfficereleasedtheinterfacecontroldocumentdealingwiththePPPservicesignal,PPP-B2b.
ThedocumentpointsoutthatBDS-3usesGEOsatellitestoprovideBDS-3,GPS,GLONASS,
andGALILEOwithsatelliteorbitcorrection,clockcorrection,andmanyothers,providing
decimeter-levelpositioningaccuracyinthekinematicmodeforusersintheAsia–Pacific
region[23]. However,thePPP-B2bservicecurrentlyonlyprovidescorrectionproductsfor
theBDS-3andGPSsystems.
ThePPP-B2bsignalbroadcaststheI-componentandtheQ-componentbutthefirst
threeGEOsatellitesofBDS-3onlybroadcasttheI-component[23]. Table1summarizes
thetypesofmessagesdefinedbythePPP-B2binterfacecontroldocument[23]. Theuser
receivesthePPP-B2bsignalinrealtimetorestoresatelliteorbitcorrection,satelliteclock
correction,anddifferentialcodebias,andfinallycorrectsthebroadcastephemeristoobtain
precisesatelliteorbitandclock,achievingdecimeter-levelpositioningaccuracyinkinematic
modeusingPPP.TheresearchonthePPP-B2bproductandservicesisbecomingahotspot.
Among them, Tao et al. evaluated the PPP-B2b product using the multi-GNSS Wuhan
University(WHU)finalproductasareference. Theirresultsshowthatthesatelliteorbit

<!-- PAGE: 3 -->

RemoteSens.2022,14,2769 3of21
errorofthePPP-B2bproductis0.1minboththeBDS-3andGPSintheradialcomponent,
and the error in the along-track and cross-track components is three to four times the
radialcomponent,respectively[24]. Meanwhile,thestandarddeviation(STD)ofsatellite
clockerrorfortheGPSandBDS-3PPP-B2bclockproductis0.13and0.11ns[24]. Xuetal.
reportedthattheaccuracyoftheBDS-3satelliteorbitcorrectedbythePPP-B2bproduct
intheradial,along-track,andcross-trackdirectionsis6.8,33.4,and36.6cm,respectively,
andtheclockproductreachesanaccuracyof0.2ns,improvedbyabout85.1%compared
to the broadcast clock [25]. Nie et al. define that PPP positioning utilizing PPP-B2b
correctionsconvergesafter10consecutiveepochstoanaccuracyofbetterthan0.6min
theverticalcomponentandbetterthan0.3minthehorizontalcomponent. Theirresults
showedthatPPPaverageconvergencetimeis17.7minutilizingthePPP-B2bsignal[26].
PositioningaccuracyusingthePPP-B2bproductcanreachdecimeter-levelbyMulti-GNSS
PPP-B2binsimulatedkinematicmodeinChina[24–26].Meanwhile,PPP-B2baugmentation
informationavailabilityforGPSandBDSsatellitesis91.5%and97.5%,respectively[24].
ThesestudiesfocusontheevaluationofthePPP-B2bproduct,andthepositioningresearch
mainlyfocusesontheuseofB1I/B3IobservationsforstationswithinChina. Therearefew
studiesonPPP-B2bpositioningaccuracyinstaticandsimulatedkinematicmodesusingthe
BDS-3B1CandB2anewsignals,andalackofresearchontheapplicationofthePPP-B2b
producttotimetransfer.
Table1.Definedmessagetypes.
MessageTypes(inDecimal) InformationContent
1 Satellitemask
Satelliteorbitcorrectionanduserrange
2
accuracyindex
3 Differentialcodebias
4 Satelliteclockcorrection
5 Userrangeaccuracyindex
Clockcorrectionandorbit
6
correction–combination1
Clockcorrectionandorbit
7
correction–combination2
8–62 Reserved
63 Nullmessage
Inthiscontribution,stationswithuniformdistributionintheAsia–Pacificregionwere
selected,andthedailyRMSvaluesofthePPP-B2bpositioningerrorsusingBDSB1I/B3Iand
BDSB1C/B2awerecalculatedinstaticandsimulatedkinematicmodes. Meanwhile,the
PPP-B2btimecomparisonoftwointernationalatomictime(TAI)timekeepinglaboratories
in the Asia–Pacific region was studied, including the National Time Service Center of
the Chinese Academy of Sciences and the Telecommunication Laboratories. Based on
the 10-day observation data of 8 IGS/international GNSS monitoring and assessment
system (IGMAS) stations in the Asia–Pacific region from day of year (DoY) 67 to 76 in
2022,theRMSvaluesofthePPP-B2bpositioningerrorsinNorth,East,andUp(N,E,and
U) directions employing four combinations of BDS B1I/B3I + GPS, BDS B1I/B3I, BDS
B1C/B2a+GPS,andBDSB1C/B2awereanalyzedinstaticandsimulatedkinematicmodes.
Inaddition, twobaselinetimelinkswereusedtoinvestigatetheaccuracyandstability
ofPPP-B2btimecomparison,takingtheGeoForschungZentrum(GFZ)multi-GNSSfinal
product(GBM)asareference,includingtheNTSCzero-baselinecommonclockdifference
and NTSC-TL long-baseline. The rest of the article is arranged as follows. Section 2
introducesthematchingstrategyofPPP-B2bcorrectioninformationandthemethodof
usingthePPP-B2bproducttorestoreprecisesatelliteorbitandsatelliteclock; secondly,
theoriesofPPPandPPPtimetransferareintroduced. Section3predominatelycoversthe
experimentaldata,methodology,experimentalresults,andanalysisdiscussion. Section4
presentsseveralconclusions.

<!-- PAGE: 4 -->

RemoteSens.2022,14,2769 4of21
2. MaterialsandMethods
2.1. MatchingStrategy
The connection between PPP-B2b message types is identified by the issue of data
(IOD),whichconsistsofIODSSR(issueofdata,statespacerepresentation),IODP(issueof
data,PRNmask),IODN(issueofdata,navigation),andIODCorr(issueofdata,orbitand
clockcorrection). Table2liststheIODcontainedinthemessagetypes. Currently,thefirst
fourmessagetypesofthePPP-B2bproductcanbecombinedintoacompletecorrection
messageversion. TheIODSSRplaysadecisiveroleintheconnectionofdifferentmessage
types,anddifferentmessagetypesofthesameIODSSRcanbematched. IODPindicates
theissuenumberofthesatellitemaskwheretheidentificationpositionof“1”denotesthat
thedifferentialinformationofthesatellitebroadcastephemeriscorrectedbythePPP-B2b
product is provided. Meanwhile, the message type 4 arranges satellite clock products
intheorderofslotlocationswiththemaskof“1”inthemessagetype1. Satelliteclock
andsatelliteorbitcorrectionscanonlybeusediftheIODCorrofthesatelliteorbitand
satelliteclockwasconsistent. IODNmatchesIODE(issueofdata,ephemeris)ofdifferent
navigationmessages,establishesaconnectionbetweenthenavigationmessagesandthe
PPP-B2bIOD,andthematchednavigationmessagesarecorrectedbythePPP-B2bproduct
toobtainprecisesatelliteorbitandclock. Thecorrectednavigationmessagediffersdueto
thenavigationsystem. ForBDS-3PPP-B2b,theCNAV1navigationmessagecarriedbythe
B1Csignaliscorrected,whereastheLNAVnavigationmessageiscorrectedforGPS.
Table2.Definedissueofdata.
IssueofData MessageTypes
IODSSR 1,2,3,4,5,6,7
IODP 1,4,5,6
IODN 2,6,7
IODCorr 2,4,6,7
EachPPP-B2bmessagehastwotimestamps: thetimewhenthereceiverreceivesthe
PPP-B2bcorrectioninformation(markedastimea)andthetimecarriedbytheepochtime
fieldinthePPP-B2bcorrectionsignalframe(markedastimeb). Therearetwooptions
forthereferencetimeforupdatingthePPP-B2bmessageinpost-processing. Iftimebis
selected,theIODCorrofthesatelliteorbitandclockwillbemismatchedwhenmessage
type2andmessagetype4match[25]. Figure1showstheBDSC23orbitandclockIOD
Correverysecondwithtimebasthereferenceforupdatingthecorrectionproduct. Attime
t1,theIODCorrofthesatelliteclockisupdated,andtheIODCorrofthesatelliteorbitis
updatedatt2,andthereisashortIODCorrmismatchfromt1tot2. Figure2showsthe
BDSC23orbitandclockIODCorrevery1sandevery2swithtimeaasthereferencetime
forupdatingthecorrectionproduct. Usingtimeaasthereferencetimeforupdatingthe
correctioninformationcanweakenthemismatchphenomenon,andtheoccurrencerateof
thismismatchissignificantlyreducedwhenupdatingevery2sbecausethereisarandom
lagbetweentimeaandtimeb. Thismismatchcanbeeliminatedusingtheobservationdata
withanintervalof30sinpost-processing,usingtimeaasthereferencetimeforupdating
thecorrectioninformation.

<!-- PAGE: 5 -->

Remote Sens. 2022, 14, x FOR PEER REVIEW 5 of 21
RemoteSens.2022,14,2769 5of21
Figure 1. Take time b as reference to update IOD Corr (C23, 8 March 2022).
8
6 6.0
4
5.5
2
5.0
0 208,846 208,848 208,850 208,852 208,854 208,856 208,858
190,000 200,000 210,000
Figure 2. Take time a as reference to update IOD Corr (C23, 8 March 2022).
2.2. Correction Algorithm
2.2.1. Differential Code Bias Correction
The pseudorange observations generated using different tracking methods contain
hardware delay deviations [27]. The PPP-B2b product provides a differential code bias,
which can be used to correct the satellite hardware delay of pseudorange observations.
Taking RINEX3.05 as a reference, the PPP-B2b product currently provides the hardware
delay correction product for signals such as BDS C2I, C2Q, C1P, etc., but does not pro-
vide hardware delay correction of BDS C1X and C5X. The pseudorange hardware delay
correction algorithm [23] can be applied according to (1):
 = −
l l DCB
(1)
sig sig sig

l denotes the pseudorange observation value in meters corrected by the PPP-B2b
sig
differential code bias product, l denotes the pseudorange observation value in me-
sig
ters directly obtained by the GNSS receiver, DCB denotes the correction in meters
sig
of the pseudorange observation in the sig tracking mode.
2.2.2. Recovery of Precise Satellite Orbit
Equation (2) is the algorithm for recovering a precise satellite position from broad-
cast ephemeris [23].
rroC
DOI
Remote Sens. 2022, 14, x FOR PEER REVIEW 5 of 21
Figure 1. Take time b as reference to update IOD Corr (C23, 8 March 2022).
Figure1.TaketimebasreferencetoupdateIODCorr(C23,8March2022).
8
clock_1s
orbit_1s
6 clock_2s 6.0
orbit_2s clcok_1s t3 t4 orbit_1s
clock_2s
orbit_2s
4
5.5
2
5.0
0 208,846 208,848 208,850 208t1,852t2208,854 208,856 208,858
Seconds of Week(GPST)
190,000 200,000 210,000
Seconds of Week(GPST)
Figure 2. Take time a as reference to update IOD Corr (C23, 8 March 2022).
2.2. Correction Algorithm
2.2.1. Differential Code Bias Correction
The pseudorange observations generated using different tracking methods contain
hardware delay deviations [27]. The PPP-B2b product provides a differential code bias,
which can be used to correct the satellite hardware delay of pseudorange observations.
Taking RINEX3.05 as a reference, the PPP-B2b product currently provides the hardware
delay correction product for signals such as BDS C2I, C2Q, C1P, etc., but does not pro-
vide hardware delay correction of BDS C1X and C5X. The pseudorange hardware delay
correction algorithm [23] can be applied according to (1):
 = −
l l DCB
(1)
sig sig sig

l denotes the pseudorange observation value in meters corrected by the PPP-B2b
sig
differential code bias product, l denotes the pseudorange observation value in me-
sig
ters directly obtained by the GNSS receiver, DCB denotes the correction in meters
sig
of the pseudorange observation in the sig tracking mode.
2.2.2. Recovery of Precise Satellite Orbit
Equation (2) is the algorithm for recovering a precise satellite position from broad-
cast ephemeris [23].
rroC
DOI
clock_1s
orbit_1s
clock_2s
orbit_2s clcok_1s t3 t4 orbit_1s
clock_2s orbit_2s
t1 t2
Seconds of Week(GPST)
Seconds of Week(GPST)
Figure2.TaketimeaasreferencetoupdateIODCorr(C23,8March2022).
2.2. CorrectionAlgorithm
2.2.1. DifferentialCodeBiasCorrection
Thepseudorangeobservationsgeneratedusingdifferenttrackingmethodscontain
hardwaredelaydeviations[27]. ThePPP-B2bproductprovidesadifferentialcodebias,
which can be used to correct the satellite hardware delay of pseudorange observations.
TakingRINEX3.05asareference,thePPP-B2bproductcurrentlyprovidesthehardware
delay correction product for signals such as BDS C2I, C2Q, C1P, etc., but does not pro-
videhardwaredelaycorrectionofBDSC1XandC5X.Thepseudorangehardwaredelay
correctionalgorithm[23]canbeappliedaccordingto(1):
(cid:101)l sig = l sig −DCB sig (1)
(cid:101)l
sig
denotesthepseudorangeobservationvalueinmeterscorrectedbythePPP-B2b
differentialcodebiasproduct,l denotesthepseudorangeobservationvalueinmeters
sig

<!-- PAGE: 6 -->

RemoteSens.2022,14,2769 6of21
directly obtained by the GNSS receiver, DCB denotes the correction in meters of the
sig
pseudorangeobservationinthesigtrackingmode.
2.2.2. RecoveryofPreciseSatelliteOrbit
Equation(2)isthealgorithmforrecoveringaprecisesatellitepositionfrombroadcast
ephemeris[23].
     
X X δx
pre brd
Y pre = Y brd−δy (2)
Z Z δz
pre brd
(cid:0) (cid:1)
where X ,Y ,Z is the precise satellite coordinate vector in earth-centered-earth
pre pre pre
fixed(ECEF),(X ,Y ,Z )representssatelliteECEFcoordinatevectorcalculatedfrom
brd brd brd
thebroadcastephemeris,and(δx,δy,δz)denotescorrectionsinthex,y,andzdirectionsof
thesatelliteintheECEFframe.
Theorbitcorrectionvector(δO ,δO ,δO )broadcastedbythePPP-B2bproductcon-
r a c
tainsthecorrectionparametersinradial,along-track,andcross-trackcomponents.Itshould
betransformedintotheECEFcoordinatesystemusingFormulas(3)and(4).
    
δx δO
r
δy= [e radical e along e cross·δO a (3)
δz δO
c


e c
e
r
r
o
a
s
d
s
ia
=
l =
| r r × ×
|r r |
r r . .| (4)
e
=e ×e
along cross radial
.
where r = (X ,Y ,Z ) is the broadcast ephemeris satellite position vector and r
brd brd brd
representsthebroadcastephemerissatellitevelocityvector.
2.2.3. RecoveryofPreciseSatelliteClock
ThebroadcastsatelliteclockrecoversthepreciseclockthroughFormula(5).
C
t = t − 0 (5)
pre brd c
wheret isthesatelliteclockoffsetinsecondscalculatedfromthebroadcastephemeris,
brd
t representsthesatelliteclockoffsetinsecondscorrectedbythePPP-B2bclockcorrection
pre
product,cdenotesthespeedoflight,andC isthePPP-B2bproductsatelliteclockcorrection
0
inmeters.
2.3. PPPModel
The GNSS observation equations are expressed as Equations (6)–(8) [28] after the
Sagnaceffect[29],relativisticeffect,phasewindupeffect[30],andreceiverandsatellite
antennaphasecentersarecorrected.
Ps = ρ+c(dt −dts)+Ts+γ ·Is +c(ds −ds)+εs (6)
r,j r r j r,1 r,j j r,j
Ls = ρ+c(dt −dts)+Ts−γ ·Is +λs(Ns +bs −bs)+ξs (7)
r,j r r j r,1 j r,j r,j j r,j
f2
γ = 1 (8)
j f2
j
whererandsrefertoreceiver-related,satellite-related,respectively;subscriptjrepresents
the band number of the satellite signal, L1 and L2 of GPS refer to 1 and 2, respectively,
whileB1I,B3I,B1C,andB2aofBDSreferto2,6,1,and5,respectively;PandLrepresent
rawcodeandcarrierphaseobservationsinmeters;ρrepresentsgeometricdistancefrom

<!-- PAGE: 7 -->

RemoteSens.2022,14,2769 7of21
thesatellitetoareceiverinmeters. cisthespeedoflight,dt anddts denoteclockoffset
r
oftheGNSSreceiverandsatellite; Ts istroposphericdelay(m); γ denotesafrequency-
r j
dependentscalingfactor, Is representstheionosphericdelayinmetersatfrequencyj =1;
r,1
ds and ds denote uncalibrated code delays (UCD) at the receiver and satellite; εs and
r,j j r,j
ξs represent the error in the pseudorange and carrier phase measurements; bs and bs
r,j r,j j
represent uncalibrated phase delays (UPD) at the receiver and satellite; λs denotes the
j
carrierwavelengthatthe frequency j ofsatellite s, Ns istheinteger ambiguity ofthe j
r,j
frequencysignalfromsatellitestoreceiverr.
Forconvenience,Equation(9)isdefined,ρcanbelinearizedtothecalculatedsatellite-
receiverdistance ρ and µs∆x. µs representsthereceiver-to-satelliteunitvectorand ∆x
0 r r
representsthevectorofreceiverpositionincrements.


ds = α
α
d
ij
s
=
+β
f
i
2−
f i 2
d
f
s
j
2
,
,
d
β
s
ij
=
=
−
α
f
i
2−
f
d
j 2
s
f
j
2
+β ds i (cid:54)= j
IFij ij i ij j r,IFij ij r,i ij r,j (9)
 DCB
P
s
iPj
= d
i
s
ρ
−
=
ds
ρ
j
,D
+
C
µ
B
s
r
s
∆
,Pi
x
Pj
= d
r
s
,i
−d
r
s
,j
0 r
TheGPSbroadcastclockoffsetreferstoaP1andP2hardwaredelaylinearcombination,
whiletheBDSbroadcastclockoffsetintroducesaB3Ihardwaredelay[27]
cdts = cdts+cds (10)
IF12 IF12
cdts = cdts+cds (11)
brd 6
In this study, Equations (12)–(15) express the dual-frequency ionospheric-free (IF)
combinationofL1andL2observationsoftheGPS.
Ps = α Ps +β Ps
r,IF12 12 r,1 12 r,2 (12)
= ρ+cdt −cdts +Ts+εs
r,IF12 IF12 r r,IF12
Ls = α Ls +β Ls
r,IF = 12 ρ+c 1 d 2 t r,1 − 1 c 2 dt r s ,2 +Ts+λ N s +ξs (13)
r,IF12 IF12 r IF12 r,IF12 r,IF12
λ N s = α λs(Ns +bs −bs)+β λs(Ns +bs −bs)−cds +cds (14)
IF12 r,IF12 12 1 r,1 r,1 1 12 2 r,2 r,2 2 r,IF12 IF12
cdt = cdt +cds (15)
r,IF12 r r,IF12
Replacedts inEquations(12)and(13)withthebroadcastedsatelliteclockcorrected
IF12
byPPP-B2b,andtheunknownparametersareexpressedasavector[∆x,cdt ,Ts,N s ].
r,IF12 r r,IF12
Equations(16)–(19)expressthedual-frequencyionospheric-freecombinationofthe
BDSB1I/B3IandtheBDSB1C/B2a.
Ps = α Ps +β Ps
r,IFij ij r,i ij r,j
(16)
= ρ+cdt +Ts+cα DCBs +cβ DCBs −cdts +εs
r,IFij r ij p6pi ij p6pj brd r,IFij
Ls = α Ls +β Ls
r = ,IFi ρ j +cd ij t r,i +T ij s− r,j cdts +λ N s +ξs (17)
r,IFij r brd IFij r,IFij r,IFij
λ N s = α λs(Ns +bs −bs)+β λs(Ns +bs −bs)−cds +cds (18)
IFij r,IFij ij i r,i r,i i ij j r,j r,j j r,IFij 6
cdt = cdt +cds (19)
r,IFij r r,IFij
Replace dts in Equations (16) and (17) with the broadcasted satellite clock cor-
brd
rectedbythePPP-B2bproduct,andtheunknownparametersareexpressedasavector
[∆x,cdt ,Ts,N s ].
r,IFij r r,IFij

<!-- PAGE: 8 -->

RemoteSens.2022,14,2769 8of21
2.4. PPPTimeTransfer
Thereceiverclockoffsett ofastationisthedifferencebetweenthelocaltime
offset,a
t of a station and the GNSS reference clock t , as shown in Equation (20). The
local,a ref
differenceinthereceiverclockoffsetofthetwostationsfortimetransfereliminatest ,
ref
which is equivalent to the difference in the local time of the two stations, as shown in
Equation(21). OnlytwoGNSSreceiversarerequired,andtheall-weather,long-distance
andhigh-precisiontimetransfercanbeachievedusingPPP.Equations(15)and(19)show
that the receiver clock offset introduces a hardware delay which must be calibrated in
engineeringapplications[31].
t = t −t (20)
offset,a local,a ref
∆t = t −t = (t −t )−(t −t ) = t −t (21)
offset,1 offset,2 local,1 ref local,2 ref local,1 local,2
Remote Sens. 2022, 14, x FOR PEER REVIEW3. E xperiments,Results,andDiscussion 9 of 21
3.1. Dataset
Figure3shows8IGMAS/IGSstationsequippedwithBDS-3andGPSreceiversin
the Asia–Pacific region participating in our analysis of PPP-B2b in the static and simu-
lated kinematic mode. SINO K803 kit which is a multi-GNSS receiver with a PPP-B2b
B1I/B3I and GPS L1/L2 dual-system IF combination (abbreviated as BDS B1I/B3I + GPS),
signalreceivingmoduleisusedtocollecttheoriginalbinaryPPP-B2bcorrectionnumber
BDSin Bfo1rmCa/tBio2naw IhFic hcoismaubtoimnaattiicoalnly (oardbebrerdevanidatseavde dasin tBoDfilSes Bby1Cth/eBd2ataa)c, oallnecdti oBnDS B1C/B2a and GPS
program in daily bins for 10 days from DoY 67 to 76 in 2022. The static and simulated
L1/L2 dual-system IF combination (abbreviated as BDS B1C/B2a + GPS). Because the
kinematicPPP-B2bpositioninganalysisinthisstudyisdividedintofourcasesbymodel
PPPa-nBd2obb sperrvoatdiounctyt pde:oBeDsS nB1oIt/ Bc3oInIFtcaoimnb tinhaeti odni(fafbebrreevniattieadl acsoBdDeS Bb1iI/aBs3 Ic),oBrDreSction products of the
C1XB 1aIn/Bd3 ICan5dXG PoSbLs1e/rLv2adtuiaol-nsyss toemf JIFFcNomGb inaantidon U(abLbArevBia stetdaatisoBnDsS,B B1ID/BS3I B+1GCPS/)B, 2a and BDS B1C/B2a
BDSB1C/B2aIFcombination(abbreviatedasBDSB1C/B2a),andBDSB1C/B2aandGPS
+ GPS use 6 stations except JFNG and ULAB for PPP-B2b positioning experiments in
L1/L2 dual-system IF combination (abbreviated as BDS B1C/B2a + GPS). Because the
statiPcP Pa-Bn2bdp rosdimuctudloaetsendot ckonitnaienmthaetdiicff ermentoiadlceosd.e bPiaPsPco rrwectaiosn pprordoucctessosfethde Cu1Xsing the open-source
and C5X observations of JFNG and ULAB stations, BDS B1C/B2a and BDS B1C/B2a +
MG_APP software [32].
GPSuse6stationsexceptJFNGandULABforPPP-B2bpositioningexperimentsinstatic
and simulated kinematic modes. PPP was processed using the open-source MG_APP
software[32].
Figure3.Distributionoftheeightstationsforexperiments.
Figure 3N. TDSiCstarnibduTtLioanre othf ethtwe oeitigmhet lsatbaotriaotonrsie fsoirn ethxepAersiiam–Peanctifisc. region involved in
maintainingTAI.Table3liststheGNSSreceiver’sinformationforthePPP-B2btimecom-
NTSC and TL are the two time laboratories in the Asia–Pacific region involved in
maintaining TAI. Table 3 lists the GNSS receiver’s information for the PPP-B2b time
comparison. NTTS and NT07 are GNSS receivers with a common atomic clock and an-
tenna in the NTSC laboratory. NTSC-TL represents a pair of long-baseline time compar-
ison links in the Asia–Pacific region. NTTS, NT07, and TLM2 are all connected to local
UTC (k). Using the 12-day observation data from DoY 85 to 96 in 2022, the BDS IF com-
bination PPP-B2b time comparison using B1I/B3I and the reference GBM product BDS
PPP time comparison were conducted simultaneously. Table 4 lists the time links par-
ticipating in the time comparison.
Table 3. Receiver information.
Receiver ID Time Laboratory Receiver (Firmware Version)
NTTS NTSC SEPT POLARX5TR(5.4.0)
NT07 NTSC SEPT POLARX5TR(5.4.0)
TLM2 TL SEPT POLARX5TR(5.4.0)
Table 4. Time links.
Time Link Region Approximate Distance (km)
NTTS-NT07 Asia 0
NTTS-TLM2 Asia 1551.5
3.2. PPP-B2b Strategy
Table 5 summarizes the processing strategies for PPP. Daily PPP-B2b position solu-
tions in four combinations in the static and simulated kinematic modes are conducted.
Because the kalman filter must converge when calculating the positioning errors RMS of
the N, E, and U directions, the first 25 min of data are removed from the daily data used

<!-- PAGE: 9 -->

RemoteSens.2022,14,2769 9of21
parison. NTTSandNT07areGNSSreceiverswithacommonatomicclockandantennain
theNTSClaboratory. NTSC-TLrepresentsapairoflong-baselinetimecomparisonlinks
in the Asia–Pacific region. NTTS, NT07, and TLM2 are all connected to local UTC (k).
Using the 12-day observation data from DoY 85 to 96 in 2022, the BDS IF combination
PPP-B2btimecomparisonusingB1I/B3IandthereferenceGBMproductBDSPPPtime
comparisonwereconductedsimultaneously. Table4liststhetimelinksparticipatinginthe
timecomparison.
Table3.Receiverinformation.
ReceiverID TimeLaboratory Receiver(FirmwareVersion)
NTTS NTSC SEPTPOLARX5TR(5.4.0)
NT07 NTSC SEPTPOLARX5TR(5.4.0)
TLM2 TL SEPTPOLARX5TR(5.4.0)
Table4.Timelinks.
TimeLink Region ApproximateDistance(km)
NTTS-NT07 Asia 0
NTTS-TLM2 Asia 1551.5
3.2. PPP-B2bStrategy
Table5summarizestheprocessingstrategiesforPPP.DailyPPP-B2bpositionsolutions
infourcombinationsinthestaticandsimulatedkinematicmodesareconducted. Because
the kalman filter must converge when calculating the positioning errors RMS of the N,
E, and U directions, the first 25 min of data are removed from the daily data used in
positioning. Meanwhile, the 12-day data were solved continuously to determine the
accuracyandstabilityofthetimetransferofthePPP-B2bproduct.
Table5.DataprocessingstrategiesforPPP-B2b.
Items Models
Constellations BDS,GPS
Cutoffangle 10◦
Estimator Kalmanfilter
Ionospheric-freelinearcombinationcodeand
Observations
carrier-phasemeasurements
Datainterval 30s
Drycomponent:correctedwithSaastamoinen
model[33]Wetcomponent:estimatedasa
Troposphericdelay
random-walkprocess;GMFMappingfunctionis
applied[34].
Phasewind-up Corrected[30]
Receiverantennaphasecenter PCOiscorrectedbythe“atx”file
BDS:B1CCNAV1broadcastephemeris+BDS-3
Satelliteorbitandclock PPP-B2b.GPS:LNAVbroadcastephemeris+
BDS-3PPP-B2b.
SatelliteDCB CorrectedusingthePPP-B2bproduct[23]
Estimatedasconstantforthestaticmode,
Stationcoordinates Estimatedaswhitenoiseforthesimulated
kinematicmode
Receiverclockoffset Estimatedaswhitenoise
Estimatedasfloating-pointconstanteach
Phaseambiguities
continuousepoch

<!-- PAGE: 10 -->

RemoteSens.2022,14,2769 10of21
3.3. ConvergenceTime
Accordingtotheofficialdocument[35],theprecisepointpositioningperformance
usingthePPP-B2bproductwiththeBDSsingle-systemandtheBDS+GPSdual-system
isbetterthan30cm,20cminthehorizontalcomponentwithaconfidencelevelof95%,
respectively,whilepositionaccuracyisbetterthan60cm,40cmintheverticalcomponent,
respectively. To guarantee a 95% confidence level, the convergence time was defined
to achieve accuracy prescribed in the official document, and to keep such a converged
positioningaccuracyforfiveminutes. Figure4showstheaverageconvergencetimeper
station from DoY 67 to 76 and from DoY 85 to 96 in 2022. Average convergence time
Remote Sens. 2022, 14, x FOR PEER REVIEW 11 of 21
usingthePPP-B2bproductwithBDSB1I/B3I+GPS,BDSB1C/B2a+GPS,BDSB1I/B3I,
BDSB1C/B2ais15.1/17.8/17.3/20.5min. Althoughtheconvergencetimeislongusing
B1C/B2a,italsomeetstheofficialdocumentrequirementsoflessthan30minfortheBDS
single-systemandlessthan20minfortheBDS+GPSdual-system.
25
20
15
10
5
0
KUN1 BJF1 USUD GAMG CHU1 GUA1 ULAB JFNG
Figure 4. Average convergence time from DoY 67 to 76 and from 85 to 96 in 2022.
3.4. Static Positioning of PPP-B2b
Figure 5 shows the average number of satellites participating in the PPP-B2b solu-
tion from DoY 67 to 76 in 2022. The average number of GPS and BDS satellites partici-
pating in the PPP-B2b calculation per epoch is 5.68 and 8.56, respectively. Considering
the influence of the number of GPS satellites, the PPP-B2b positioning accuracy is inves-
tigated using the BDS and GPS dual-system rather than GPS single-system. The USUD
station has the fewest satellites of the eight stations, resulting in poor PPP-B2b position-
ing accuracy in both static and simulated kinematic modes.
Figure 5. Average number of satellites from DoY 67 to 76 in 2022.
)setunim(emiT
ecnegrevnoC
BDS B1I/B3I+GPS
BDS B1C/B2a+GPS
25
20
15
10
5
0
KUN1 BJF1 USUD GAMG CHU1 GUA1 ULAB JFNG
Stations
)setunim(emiT
ecnegrevnoC
BDS B1I/B3I
BDS B1C/B2a
16
14
12
10
8
6
4
2
0
BJF1 GAMG JFNG KUN1 ULAB USUD CHU1 GUA1
etilletas
fo
rebmun
Figure4.AverageconvergencetimefromDoY67to76andfrom85to96in2022.
3.4. StaticPositioningofPPP-B2b
Figure5showstheaveragenumberofsatellitesparticipatinginthePPP-B2bsolution
fromDoY67to76in2022. TheaveragenumberofGPSandBDSsatellitesparticipatingin
thePPP-B2bcalculationperepochis5.68and8.56,respectively. Consideringtheinfluence
ofthenumberofGPSsatellites,thePPP-B2bpositioningaccuracyisinvestigatedusing
theBDSandGPSdual-systemratherthanGPSsingle-system. TheUSUDstationhasthe
fewestsatellitesoftheeightstations,resultinginpoorPPP-B2bpositioningaccuracyin
bothstaticandsimulatedkinematicmodes.
BDS
BDS+GPS
Station

<!-- PAGE: 11 -->

Remote Sens. 2022, 14, x FOR PEER REVIEW 11 of 21
25
20
15
10
5
0
KUN1 BJF1 USUD GAMG CHU1 GUA1 ULAB JFNG
Figure 4. Average convergence time from DoY 67 to 76 and from 85 to 96 in 2022.
3.4. Static Positioning of PPP-B2b
Figure 5 shows the average number of satellites participating in the PPP-B2b solu-
tion from DoY 67 to 76 in 2022. The average number of GPS and BDS satellites partici-
pating in the PPP-B2b calculation per epoch is 5.68 and 8.56, respectively. Considering
the influence of the number of GPS satellites, the PPP-B2b positioning accuracy is inves-
tigated using the BDS and GPS dual-system rather than GPS single-system. The USUD
RemoteSens.2022,14,2769 station has the fewest satellites of the eight stations, resulting in poor PPP-B2b posit1io1nof-21
ing accuracy in both static and simulated kinematic modes.
Figure 5. Average number of satellites from DoY 67 to 76 in 2022.
)setunim(emiT
ecnegrevnoC
BDS B1I/B3I+GPS
BDS B1C/B2a+GPS
25
20
15
10
5
0
KUN1 BJF1 USUD GAMG CHU1 GUA1 ULAB JFNG
Stations
)setunim(emiT
ecnegrevnoC
BDS B1I/B3I
BDS B1C/B2a
16
14
12
10
8
6
4
2
0
BJF1 GAMG JFNG KUN1 ULAB USUD CHU1 GUA1
etilletas
fo
rebmun
BDS
BDS+GPS
Remote Sens. 2022, 14, x FOR PEER REVIEW 12 of 21
Station
FigurAe5s. aAnve eraxgaemnupmleb,e rtaokfisnatge llsitteastfiroonm GDAoYM67Gt oo7n6 iDno20Y2 27.2 in 2022 the static positioning re-
sults in the N, E, and U directions (green-N, red-E, and blue-U, respectively) over time
Asanexample,takingstationGAMGonDoY72in2022thestaticpositioningresults
are shown in Figure 6, which displays four sequences (BDS B1I/B3I + GPS, BDS B1C/B2a
intheN,E,andUdirections(green-N,red-E,andblue-U,respectively)overtimeareshown
+ GPS, BDS B1I/B3I, and BDS B1C/B2a) of static position error in N, E, and U directions
inFigure6,whichdisplaysfoursequences(BDSB1I/B3I+GPS,BDSB1C/B2a+GPS,BDS
from top to bottom. The vertical orange line daily at 0:25 h separates the converged
B1I/B3I,andBDSB1C/B2a)ofstaticpositionerrorinN,E,andUdirectionsfromtopto
PPP-B2b static positioning results from the non-converged positioning results. The con-
bottom. Theverticalorangelinedailyat0:25hseparatestheconvergedPPP-B2bstatic
vpeorsgiteionnt ipngosrietsiuolntsinfrgo merrthoer nRoMn-Sco vnavleuregse dinp tohsiet iNon, iEng, arensdu lUts .dTihreecctoionnvesr fgoern t2p83o0si teiopnoicnhgs of 30 s
ienrtreorrvRaMls Sovna DluoesYi n67th ienN 2,0E2,2a nisd cUaldcuirleactteiodn. sTfhore 2p8o30sietipoonc hesrorofr3 0osf itnhteer vfoaulsro cnoDmobYinations
f6lu7cintu2a0t2e2s iwsciathlciunl athteed .raTnhgeep oosfi t±i0o.n05er mror aofftethr ethfoeu PrPcoPm-Bb2ibna sttioantisc flpuocstiutaiotensinwgit hoifn tthhee GAMG
srtaantigoeno cfo ± n0v.0e5rgmes.a fTtehret hpeosPiPtiPo-nB 2ebrrsotra tRicMpSo switiaosn ainbgouoft t2h cemG AfoMr Gthset ahtoiornizcoonntvale rcgoems.ponent
ThepositionerrorRMSwasabout2cmforthehorizontalcomponentand4cmforthe
and 4 cm for the vertical component.
verticalcomponent.
FFiigguurree 66.. PPPPPP--BB22bbp posoistiiotinoenr reorrroforr fGorA GMAGMinGt hien stthaeti cstmatoidc em(8odMea r(c8h M20a2r2c)h. 2022).
The RMS values of the station’s static PPP-B2b positioning in N, E, and U directions
from DoY 67 to 76 in 2022 are shown in form of box plots in Figures 7 and 8. Figures 7
and 8 show the 25–75% range, mean, and outliers of 10-day static position errors RMS
using the PPP-B2b product in the N, E, and U directions. In addition, Tables 6 and 7 list
the average RMS values of the position errors of the BDS B1I/B3I + GPS, BDS B1I/B3I,
BDS B1C/B2a + GPS, and BDS B1C/B2a in N, E, and U directions. Figures 7 and 8 show
that the RMS values of the position errors in the N direction for the four positioning
combinations are less than 2 cm of most test days, with a minimum value of less than 1
cm, and the accuracy in E and U directions is poor and concentrated within 3 and 4 cm,
respectively. Due to the number of satellites, USUD and GUA1 deliver a poor position-
ing accuracy compared with other stations. The average RMS values of the PPP-B2b
static positioning of the BDS + GPS dual-system in the N direction concentrate around
1.5 cm, which is better than 2.5 cm in the E direction and 3.6 cm in the U direction. Ta-
bles 6 and 7 show that the average RMS values of the BDS PPP-B2b static positioning in
the N, E, and U directions are 1.5/2.7/3.9 cm, respectively.

<!-- PAGE: 12 -->

RemoteSens.2022,14,2769 12of21
TheRMSvaluesofthestation’sstaticPPP-B2bpositioninginN,E,andUdirections
fromDoY67to76in2022areshowninformofboxplotsinFigures7and8.Figures7and8
show the 25–75% range, mean, and outliers of 10-day static position errors RMS using
the PPP-B2b product in the N, E, and U directions. In addition, Tables 6 and 7 list the
averageRMSvaluesofthepositionerrorsoftheBDSB1I/B3I+GPS,BDSB1I/B3I,BDS
B1C/B2a+GPS,andBDSB1C/B2ainN,E,andUdirections. Figures7and8showthatthe
RMSvaluesofthepositionerrorsintheNdirectionforthefourpositioningcombinations
are less than 2 cm of most test days, with a minimum value of less than 1 cm, and the
accuracyinEandUdirectionsispoorandconcentratedwithin3and4cm,respectively.
Due to the number of satellites, USUD and GUA1 deliver a poor positioning accuracy
comparedwithotherstations. TheaverageRMSvaluesofthePPP-B2bstaticpositioningof
theBDS+GPSdual-systemintheNdirectionconcentratearound1.5cm,whichisbetter
Remote Sens. 2022, 14, x FOR PEER REVtIhEaWn 2.5cmintheEdirectionand3.6cmintheUdirection. Tables6and7showthatthe 13 of 21
averageRMSvaluesoftheBDSPPP-B2bstaticpositioningintheN,E,andUdirectionsare
1.5/2.7/3.9cm,respectively.
0.08
0.06
0.04
0.02
0.00
Figure 7. (a) Static position errors RMS using PPP-B2b BDS B1I/B3I + GPS; (b) static position errors
RMS using PPP-B2b BDS B1C/B2a + GPS.
Table 6. Mean RMS values of PPP-B2b static positioning of each station using B1I/B3I.
BDS B1I/B3I + GPS BDS B1I/B3I
Station
N (cm) E (cm) U (cm) N (cm) E (cm) U (cm)
KUN1 1.7 2.9 2.9 1.7 2.6 3.5
BJF1 1.0 2.1 3.1 0.9 2.1 3.5
USUD 1.7 2.8 3.9 2.1 2.8 4.3
GAMG 1.5 1.9 3.7 1.5 2.7 4.2
CHU1 1.3 2.7 3.3 1.3 3.3 3.4
GUA1 1.3 3.1 3.0 1.2 3.2 3.9
ULAB 1.5 2.7 3.2 1.5 3.6 3.6
JFNG 0.9 1.8 3.6 0.9 1.2 4.0
MEAN 1.4 2.5 3.3 1.4 2.7 3.8
Table 7. Mean RMS values of PPP-B2b static positioning of each station using B1C/B2a.
BDS B1C/B2a + GPS BDS B1C/B2a
Station
N (cm) E (cm) U (cm) N (cm) E (cm) U (cm)
KUN1 1.7 2.6 3.1 1.2 2.3 3.7
BJF1 1.3 1.5 2.7 1.3 1.5 3.4
USUD 1.5 2.4 4.0 1.8 2.4 4.0
GAMG 1.4 2.1 3.7 1.2 2.0 4.1
CHU1 1.7 2.4 3.9 1.8 2.2 4.0
GUA1 1.5 2.2 4.3 1.6 2.8 4.2
)m(N
25%~75%
Range within 1.5IQR
Mean Line
Outliers
0.08
0.06
0.04
0.02
0.00
)m(E
0.08
0.06
0.04
0.02
0.00
ULAB KUN1 BJF1 JFNG USUD GAMG CHU1 GUA1
(a)
)m(U
0.08
0.06
0.04
0.02
0.00
)m(N
0.08
0.06
0.04
0.02
0.00
)m(E
0.08
0.06
0.04
0.02
0.00
KUN1 BJF1 USUD GAMG CHU1 GUA1
(b)
)m(U
Figure7.(a)StaticpositionerrorsRMSusingPPP-B2bBDSB1I/B3I+GPS;(b)staticpositionerrors
RMSusingPPP-B2bBDSB1C/B2a+GPS.

<!-- PAGE: 13 -->

Remote Sens. 2022, 14, x FOR PEER REVIEW 14 of 21
RemoteSens.2022,14,2769 13of21
MEAN 1.5 2.2 3.6 1.5 2.2 3.9
0.08
0.06
0.04
0.02
0.00
Figure 8. (a) Static position errors RMS using PPP-B2b BDS B1I/B3I; (b) static position errors RMS
using PPP-B2b BDS B1C/B2a.
3.5. Kinematic Positioning of PPP-B2b
Figure 9 shows the position errors of the GAMG station using four combinations in
simulated kinematic mode in N, E, and U directions (green-N, red-E, and blue-U, re-
spectively) on DoY 72 in 2022 from top to bottom, BDS B1I/B3I + GPS, BDS B1C/B2a +
GPS, BDS B1I/B3I, and BDS B1C/B2a. The vertical orange line daily at 0:25 h separates
the converged PPP-B2b simulated kinematic positioning results from the non-converged
positioning results. After convergence, the errors in the N and E directions fluctuate
within the range of ±10 cm, and the RMS is 3 and 5 cm, respectively. The U direction is
poor, and most of the epoch position errors fluctuate within the range of ±15 cm. Some
epochs can reach up to 20 cm but cannot increase further. The RMS value of the B1C/B2a
combination in the U direction is the worst at 8 cm, while the other three combinations
are 7 cm. Using only the BDS single-system has a longer convergence time and a lower
convergence accuracy than the BDS + GPS dual-system.
)m(N
25%~75%
Range within 1.5IQR
Mean Line
Outliers
0.08
0.06
0.04
0.02
0.00
)m(E
0.08
0.06
0.04
0.02
0.00
ULAB KUN1 BJF1 JFNG USUD GAMG CHU1 GUA1
(a)
)m(U
0.08
0.06
0.04
0.02
0.00
)m(N
0.08
0.06
0.04
0.02
0.00
)m(E
0.08
0.06
0.04
0.02
0.00
KUN1 BJF1 USUD GAMG CHU1 GUA1
(b)
)m(U
Figure8.(a)StaticpositionerrorsRMSusingPPP-B2bBDSB1I/B3I;(b)staticpositionerrorsRMS
usingPPP-B2bBDSB1C/B2a.
Table6.MeanRMSvaluesofPPP-B2bstaticpositioningofeachstationusingB1I/B3I.
BDSB1I/B3I+GPS BDSB1I/B3I
Station
N(cm) E(cm) U(cm) N(cm) E(cm) U(cm)
KUN1 1.7 2.9 2.9 1.7 2.6 3.5
BJF1 1.0 2.1 3.1 0.9 2.1 3.5
USUD 1.7 2.8 3.9 2.1 2.8 4.3
GAMG 1.5 1.9 3.7 1.5 2.7 4.2
CHU1 1.3 2.7 3.3 1.3 3.3 3.4
GUA1 1.3 3.1 3.0 1.2 3.2 3.9
ULAB 1.5 2.7 3.2 1.5 3.6 3.6
JFNG 0.9 1.8 3.6 0.9 1.2 4.0
MEAN 1.4 2.5 3.3 1.4 2.7 3.8

<!-- PAGE: 14 -->

RemoteSens.2022,14,2769 14of21
Table7.MeanRMSvaluesofPPP-B2bstaticpositioningofeachstationusingB1C/B2a.
BDSB1C/B2a+GPS BDSB1C/B2a
Station
N(cm) E(cm) U(cm) N(cm) E(cm) U(cm)
KUN1 1.7 2.6 3.1 1.2 2.3 3.7
BJF1 1.3 1.5 2.7 1.3 1.5 3.4
USUD 1.5 2.4 4.0 1.8 2.4 4.0
GAMG 1.4 2.1 3.7 1.2 2.0 4.1
CHU1 1.7 2.4 3.9 1.8 2.2 4.0
GUA1 1.5 2.2 4.3 1.6 2.8 4.2
MEAN 1.5 2.2 3.6 1.5 2.2 3.9
3.5. KinematicPositioningofPPP-B2b
Figure9showsthepositionerrorsoftheGAMGstationusingfourcombinationsin
simulatedkinematicmodeinN,E,andUdirections(green-N,red-E,andblue-U,respec-
tively)onDoY72in2022fromtoptobottom,BDSB1I/B3I+GPS,BDSB1C/B2a+GPS,
BDS B1I/B3I, and BDS B1C/B2a. The vertical orange line daily at 0:25 h separates the
convergedPPP-B2bsimulatedkinematicpositioningresultsfromthenon-convergedposi-
tioningresults. Afterconvergence,theerrorsintheNandEdirectionsfluctuatewithinthe
rangeof±10cm,andtheRMSis3and5cm,respectively. TheUdirectionispoor,andmost
oftheepochpositionerrorsfluctuatewithintherangeof±15cm. Someepochscanreach
upto20cmbutcannotincreasefurther. TheRMSvalueoftheB1C/B2acombinationinthe
Remote Sens. 2022, 14, x FOR PEER REVIEW 15 of 21
Udirectionistheworstat8cm,whiletheotherthreecombinationsare7cm. Usingonly
theBDSsingle-systemhasalongerconvergencetimeandalowerconvergenceaccuracy
thantheBDS+GPSdual-system.
FFiigguurree9 9..P PPPP-PB-2Bb2pbo psiotisointieornro ersrrfoorrsG fAoMr GGAinMthGe siinm tuhleat esdimkuinleamteadti ckminoedmea(8tiMc marcohd2e0 (282 )M. arch 2022).
TheRMSvaluesofthekinematicPPP-B2berrorsintheN,E,andUdirectionsfrom
The RMS values of the kinematic PPP-B2b errors in the N, E, and U directions from
DoY67to76in2s022areshowninformofboxplotsinFigures10and11,andtheaverage
DoY 67 to 76 in 2s022 are shown in form of box plots in Figures 10 and 11, and the aver-
RMSvaluesofpositionerrorsarerecordedinTables8and9.Figures10and11showthatthe
age RMS values of position errors are recorded in Tables 8 and 9. Figures 10 and 11 show
bestsimulatedkinematicpositioningresultsareintheNdirection,whichisconcentrated
that the best simulated kinematic positioning results are in the N direction, which is
concentrated at 2–4 cm; the simulated kinematic positioning results are concentrated at
3–7 cm using the BDS + GPS dual-system in the E direction, and at 6–9 cm using the sin-
gle BDS system; the kinematic positioning results in the U direction are the worst, with
the largest RMS value being 0.1181 m. The average RMS line positions in Figures 10 and
11 show that the mean RMS line in the E direction of the dual-system is lower than that
in the single system; using B1I and B3I is higher in the E direction than B1C and B2a, and
lower in the U direction. Table 8 shows that the average RMS values of the position er-
rors of the combination of BDS B1I/B3I + GPS and BDS B1I/B3I in the N, E, and U direc-
tions are 3.4/5.8/7.6 cm and 3.8/6.6/7.8 cm, respectively. The average RMS values of the
position errors of BDS B1C/B2a + GPS and BDS B1C/B2a in the N, E, and U directions are
3.6/4.9/8.1 cm and 4/6.1/8.5 cm, respectively. Compared with B1C/B2a, the positioning
accuracy of PPP-B2b using B1I/ B3I observations is improved by 5–7 mm in the U direc-
tion but decreased by 5–9 mm in the E direction. Compared with the BDS single-system,
the dual-system PPP-B2b improved by nearly 1 cm in the E direction.

<!-- PAGE: 15 -->

RemoteSens.2022,14,2769 15of21
at2–4cm;thesimulatedkinematicpositioningresultsareconcentratedat3–7cmusingthe
BDS+GPSdual-systemintheEdirection,andat6–9cmusingthesingleBDSsystem;the
kinematicpositioningresultsintheUdirectionaretheworst,withthelargestRMSvalue
being0.1181m. TheaverageRMSlinepositionsinFigures10and11showthatthemean
RMSlineintheEdirectionofthedual-systemislowerthanthatinthesinglesystem;using
B1IandB3IishigherintheEdirectionthanB1CandB2a,andlowerintheUdirection.
Table8showsthattheaverageRMSvaluesofthepositionerrorsofthecombinationof
BDS B1I/B3I + GPS and BDS B1I/B3I in the N, E, and U directions are 3.4/5.8/7.6 cm
and3.8/6.6/7.8cm,respectively. TheaverageRMSvaluesofthepositionerrorsofBDS
B1C/B2a+GPSandBDSB1C/B2aintheN,E,andUdirectionsare3.6/4.9/8.1cmand
4/6.1/8.5cm,respectively. ComparedwithB1C/B2a,thepositioningaccuracyofPPP-B2b
Remote Sens. 2022, 14, x FOR PEER REVIEW 16 of 21
using B1I/ B3I observations is improved by 5–7 mm in the U direction but decreased
by 5–9mm in the E direction. Compared with the BDS single-system, the dual-system
PPP-B2bimprovedbynearly1cmintheEdirection.
0.12
0.09
0.06
0.03
0.00
Figure 10. (a) PPP-B2b position error RMS values using BDS B1I/B3I + GPS in the simulated kine-
matic mode; (b) PPP-B2b position error RMS values using BDS B1C/B2a + GPS in the simulated
kinematic mode.
Table 8. Mean RMS values of PPP-B2b kinematic positioning at each station using B1I/B3I.
BDS B1I/B3I + GPS BDS B1I/B3I
Station
N (cm) E (cm) U (cm) N (cm) E (cm) U (cm)
KUN1 3.2 6.8 7.3 3.8 7.4 7.9
BJF1 3.8 5.4 7.3 3.9 6.6 7.2
USUD 4.4 5.3 8.2 3.8 6.5 8.9
GAMG 3.1 4.7 7.9 4.3 6.2 7.9
CHU1 3.4 6.3 7.6 3.3 6.8 7.4
GUA1 3.4 6.5 7.7 3.3 6.1 7.3
ULAB 3.5 6.8 7.0 4.3 6.4 8.3
JFNG 2.7 4.7 7.6 3.4 6.6 7.3
MEAN 3.4 5.8 7.6 3.8 6.6 7.8
Table 9. Mean RMS values of PPP-B2b kinematic positioning at each station using B1C/B2a.
BDS B1C/B2a + GPS BDS B1C/B2a
Station
N (cm) E (cm) U (cm) N (cm) E (cm) U (cm)
KUN1 3.1 5.9 7.6 3.8 7.1 9.9
BJF1 4.3 5.6 8.4 4.0 7.1 8.3
USUD 3.6 3.5 8.6 4.7 5.0 8.0
GAMG 3.4 5.0 8.0 3.5 5.3 7.5
CHU1 3.6 4.7 8.2 4.6 6.2 8.6
)m(N
25%~75%
Range within 1.5IQR
Mean Line
Outliers
0.12
0.09
0.06
0.03
0.00
)m(E
0.12
0.09
0.06
0.03
0.00
ULAB KUN1 BJF1 JFNG USUD GAMG CHU1 GUA1
(a)
)m(U
0.12
0.09
0.06
0.03
0.00
)m(N
0.12
0.09
0.06
0.03
0.00
)m(E
0.12
0.09
0.06
0.03
0.00
KUN1 BJF1 USUD GAMG CHU1 GUA1
(b)
)m(U
Figure 10. (a) PPP-B2b position error RMS values using BDS B1I/B3I + GPS in the simulated
kinematicmode;(b)PPP-B2bpositionerrorRMSvaluesusingBDSB1C/B2a+GPSinthesimulated
kinematicmode.

<!-- PAGE: 16 -->

Remote Sens. 2022, 14, x FOR PEER REVIEW 17 of 21
GUA1 3.3 4.5 8.0 3.6 5.8 8.4
RemoteSens.2022,14,2769 16of21
MEAN 3.6 4.9 8.1 4.0 6.1 8.5
0.12
0.09
0.06
0.03
0.00
Figure 11. (a) PPP-B2b position error RMS values using BDS B1I/B3I in the simulated kinematic
mode; (b) PPP-B2b position error RMS values using BDS B1C/B2a in the simulated kinematic
mode.
3.6. Time Transfer
CCD is often used to analyze the noise level of time comparison [36–38]. Consecu-
tive days with CCD can reflect the uncertainty of receiver noise and time comparison.
Figure 12 shows the zero-baseline CCD time comparison results of NTTS and NT07 us-
ing the GBM product and the PPP-B2b product from DoY 85 to 96 in 2022. A hardware
delay is absorbed in the receiver clock offset, and the results of the time comparison
have systematic deviations. Figure 12 shows that the PPP time comparison noise using
the GBM and PPP-B2b products fluctuates within the range of 0.1 ns, the standard devi-
ation of time comparison is 0.0167 and 0.024, respectively, which are consistent, and the
time comparison of the two products has good continuity.
)m(N
25%~75%
Range within 1.5IQR
Mean Line
Outliers
0.12
0.09
0.06
0.03
0.00
)m(E
0.12
0.09
0.06
0.03
0.00
ULAB KUN1 BJF1 JFNG USUD GAMG CHU1 GUA1
(a)
)m(U
0.12
0.09
0.06
0.03
0.00
)m(N
0.12
0.09
0.06
0.03
0.00
)m(E
0.12
0.09
0.06
0.03
0.00
KUN1 BJF1 USUD GAMG CHU1 GUA1
(b)
)m(U
Figure11. (a)PPP-B2bpositionerrorRMSvaluesusingBDSB1I/B3Iinthesimulatedkinematic
mode;(b)PPP-B2bpositionerrorRMSvaluesusingBDSB1C/B2ainthesimulatedkinematicmode.
Table8.MeanRMSvaluesofPPP-B2bkinematicpositioningateachstationusingB1I/B3I.
BDSB1I/B3I+GPS BDSB1I/B3I
Station
N(cm) E(cm) U(cm) N(cm) E(cm) U(cm)
KUN1 3.2 6.8 7.3 3.8 7.4 7.9
BJF1 3.8 5.4 7.3 3.9 6.6 7.2
USUD 4.4 5.3 8.2 3.8 6.5 8.9
GAMG 3.1 4.7 7.9 4.3 6.2 7.9
CHU1 3.4 6.3 7.6 3.3 6.8 7.4
GUA1 3.4 6.5 7.7 3.3 6.1 7.3
ULAB 3.5 6.8 7.0 4.3 6.4 8.3
JFNG 2.7 4.7 7.6 3.4 6.6 7.3
MEAN 3.4 5.8 7.6 3.8 6.6 7.8

<!-- PAGE: 17 -->

RemoteSens.2022,14,2769 17of21
Table9.MeanRMSvaluesofPPP-B2bkinematicpositioningateachstationusingB1C/B2a.
BDSB1C/B2a+GPS BDSB1C/B2a
Station
N(cm) E(cm) U(cm) N(cm) E(cm) U(cm)
KUN1 3.1 5.9 7.6 3.8 7.1 9.9
BJF1 4.3 5.6 8.4 4.0 7.1 8.3
USUD 3.6 3.5 8.6 4.7 5.0 8.0
GAMG 3.4 5.0 8.0 3.5 5.3 7.5
CHU1 3.6 4.7 8.2 4.6 6.2 8.6
GUA1 3.3 4.5 8.0 3.6 5.8 8.4
MEAN 3.6 4.9 8.1 4.0 6.1 8.5
3.6. TimeTransfer
CCDisoftenusedtoanalyzethenoiseleveloftimecomparison[36–38]. Consecutive
dayswithCCDcanreflecttheuncertaintyofreceivernoiseandtimecomparison. Figure12
showsthezero-baselineCCDtimecomparisonresultsofNTTSandNT07usingtheGBM
productandthePPP-B2bproductfromDoY85to96in2022. Ahardwaredelayisabsorbed
inthereceiverclockoffset,andtheresultsofthetimecomparisonhavesystematicdevia-
tions. Figure12showsthatthePPPtimecomparisonnoiseusingtheGBMandPPP-B2b
Remote Sens. 2022, 14, x FOR PEER REVpIrEoWdu ctsfluctuateswithintherangeof0.1ns,thestandarddeviationoftimecomparisonis 18 of 21
0.0167and0.024,respectively,whichareconsistent,andthetimecomparisonofthetwo
productshasgoodcontinuity.
Figure12.CCDtimecomparisonusingthePPP-B2bproductandtheGBMproductbetweenNTTS
Figure 12. CCD time comparison using the PPP-B2b product and the GBM product between NTTS
andNT07.
and NT07.
Figure13showsthelong-baselineBDS-3PPPtimecomparisonresultsofNTTSand
TLMF2iugsuinreg t1h3e sGhBoMwps rtohdeu clotnangd-bthaesePlPinPe-B B2bDpSr-o3d PuPctPfr toimmDe ocYom85ptaor9i6soinn 2r0e2s2u.lUtss ionfg NTTS and
TtLhMed2if fuesreinncge tihnet hGeBNMTT pS-rToLdMu2ctt iamnedc otmhep aPrPisPon-Br2esbu lptsrobdetuwcete fnrothme GDBoMYp 8r5od tuoc t9a6n idn 2022. Us-
thePPP-B2bproduct,theresidualsequenceofNTTS-TLM2BDS-3PPPtimecomparisonis
ing the difference in the NTTS-TLM2 time comparison results between the GBM product
obtainedinFigure14. Theresidualofthetimecomparisonofthetwoproductsfluctuates
and the PPP-B2b product, the residual sequence of NTTS-TLM2 BDS-3 PPP time com-
withintherangeof±0.5nsafterconvergence,demonstratingtheuncertaintyofthetime
parison is obtained in Figure 14. The residual of the time comparison of the two prod-
comparisonofthetwoproductswithin±0.5ns. Meanwhile,Figure15showstheAllan
uvcatrsi afnlucectoufathteesG wBMithpirno dtuhcet arnadngthee oPfP ±P0-B.52 bnpsr oadftuecrt tcimonevtrearngsefnerc.e, demonstrating the uncer-
tainty of the time comparison of the two products within ±0.5 ns. Meanwhile, Figure 15
shows the Allan variance of the GBM product and the PPP-B2b product time transfer.
Figure 13. Clock difference of UTC(NTSC)-UTC(TL) using the PPP-B2b product and the GBM
product via PPP.
Figure 14. The difference in NTSC-TL time comparison between the PPP-B2b product and the GBM
product via PPP.

<!-- PAGE: 18 -->

Remote Sens. 2022, 14, x FOR PEER REVIEW 18 of 21
Remote Sens. 2022, 14, x FOR PEER REVIEW 18 of 21
Figure 12. CCD time comparison using the PPP-B2b product and the GBM product between NTTS
and NT07.
Figure 12. CCD time comparison using the PPP-B2b product and the GBM product between NTTS
and FNigTu07r.e 13 shows the long-baseline BDS-3 PPP time comparison results of NTTS and
TLM2 using the GBM product and the PPP-B2b product from DoY 85 to 96 in 2022. Us-
ing theF idgiuffreer e1n3c seh ionw ths et hNe TloTnSg-T-bLaMse2l itnime Be DcoSm-3p PaPriPs otinm ree scuolmts pbaertiwsoene nr etshuel tGs BoMf N pTrTodS uacntd
anTdL Mth2e uPsPinPg-B t2hbe pGrBoMdu pctr,o tdhuec tr easniddu tahle sPePquPe-Bn2cbe pofr oNdTuTctS f-rToLmM D2 oBYD 8S5-3 t oP P9P6 itnim 2e0 2c2o. mU-s-
pianrgis othne ids ioffbetraeinnceed i nin t hFeig NuTreT 1S4-T. LTMhe2 rteimsideu caolm opf atrhieso tnim rees cuoltms pbeatrwisoeenn o tfh teh Ge BtwMo p proroddu-ct
uactnsd f ltuhcet uPaPtePs- Bw2bit hpinro tdhuec tr,a nthgee roefs i±d0u.5a ln sse qafuteenr cceo novf eNrgTeTnSc-eT, LdMem2 oBnDstSr-a3t iPnPgP t hteim uen cceorm--
tapinartyis oonf tihs eo tbimtaien ceodm inp aFriigsounre o 1f 4t.h Te htew roe spirdoudaul cotsf wthiet htiinm ±e0 c.5o mnsp. aMriseoann wohf itlhee, Ftwigou rper 1o5d -
shuocwts sf ltuhcet Aualltaens vwairtihainnc teh oef rtahneg Ge BoMf ± p0r.5o dnusc ta fatnerd ctohne vPePrPge-Bn2cbe, pdreomduocnts ttirmatein tgra tnhsef eur.n cer-
tainty of the time comparison of the two products within ±0.5 ns. Meanwhile, Figure 15
RemoteSens.2022,14,2769 18of21
shows the Allan variance of the GBM product and the PPP-B2b product time transfer.
Figure 13. Clock difference of UTC(NTSC)-UTC(TL) using the PPP-B2b product and the GBM
product via PPP.
Figure13.ClockdifferenceofUTC(NTSC)-UTC(TL)usingthePPP-B2bproductandtheGBMproduct
Figure 13. Clock difference of UTC(NTSC)-UTC(TL) using the PPP-B2b product and the GBM
viaPPP.
product via PPP.
Remote Sens. 2022, 14, x FOR PEER REVIEW 19 of 21
Figure14.ThedifferenceinNTSC-TLtimecomparisonbetweenthePPP-B2bproductandtheGBM
Figure 14. The difference in NTSC-TL time comparison between the PPP-B2b product and the GBM
pro
p
d
ro
u
d
c
u
t
c
v
t
i
v
a
i a
P
P
P
P
P
P
.
.
Figure 14. The difference in NTSC-TL time comparison between the PPP-B2b product and the GBM
product via PPP.
Figure15.TheAllanofNTSC-TLtimecomparisonusingthePPP-B2bproductandtheGB Mproduct
Figurev i1a5P. PTPh. e Allan of NTSC-TL time comparison using the PPP-B2b product and the GBM
product via PPP.
4. Conclusions
The BDS-3 can provide PPP services to the Asia–Pacific region via GEO satellites
following the official announcement of the PPP-B2b signal document. In this contribu-
tion, by employing distributed IGS/IGMAS stations in the Asia–Pacific region, a com-
prehensive analysis of the time transfer and positioning accuracy using the PPP-B2b
product was undertaken. Initially, the matching strategy of the PPP-B2b product was
discussed. The post-processing observations were updated at the rate of 1 s, and the
epoch time field in the PPP-B2b information frame was used as a reference for updating
the PPP-B2b correction product. The IOD Corr of the satellite orbit and clock were mis-
matched when the message type 2 and message type 4 match. Using the time when the
receiver gets the PPP-B2b correction message as the reference time, and updating the
observation value at 1 s intervals, the mismatch between the PPP-B2b satellite clock and
orbit products will be significantly reduced. When the observation update interval is in-
creased to 2 s, the probability of mismatch occurrence is significantly reduced. In this
study, the observation value update interval in PPP-B2b positioning was investigated
with a time comparison of 30 s.
The PPP-B2b positioning study was analyzed using the four IF combinations in
static and simulated kinematic mode: BDS B1I/B3I, BDS B1C/B2a, BDS B1I/B3I + GPS,
and BDS B1C/B2a + GPS. According to the official document, the average convergence
time was analyzed. Average convergence time using the PPP-B2b product with BDS
B1I/B3I + GPS, BDS B1C/B2a + GPS, BDS B1I/B3I, BDS B1C/B2a was 15.1/17.8/17.3/20.5
min, respectively. Regarding the PPP-B2b static position results, the average RMS values
in the N, E, and U directions of only BDS PPP-B2b were within 1.5/2.7/3.9 cm, respec-
tively, and the positioning accuracies in the E and U directions can be improved to
2.5/3.5 cm using BDS and GPS dual-system. Compared with BDS B1C/B2a, BDS B1I/B3I
has comparable positioning accuracy in the N direction, and the accuracy in the U direc-
tion can be improved by 3-4 mm. In the PPP-B2b simulated kinematic positioning study,
the average RMS values of the positioning errors in the N, E, and U directions for the
combination of BDS B1I/B3I + GPS and BDS B1I/B3I were 3.4/5.8/7.6 and 3.8/6.6/7.8 cm,
respectively. Meanwhile, the RMS values of the position errors using BDS B1C/B2a +

<!-- PAGE: 19 -->

RemoteSens.2022,14,2769 19of21
4. Conclusions
The BDS-3 can provide PPP services to the Asia–Pacific region via GEO satellites
followingtheofficialannouncementofthePPP-B2bsignaldocument. Inthiscontribution,
byemployingdistributedIGS/IGMASstationsintheAsia–Pacificregion,acomprehensive
analysis of the time transfer and positioning accuracy using the PPP-B2b product was
undertaken. Initially,thematchingstrategyofthePPP-B2bproductwasdiscussed. The
post-processingobservationswereupdatedattherateof1s,andtheepochtimefieldinthe
PPP-B2binformationframewasusedasareferenceforupdatingthePPP-B2bcorrection
product. TheIODCorrofthesatelliteorbitandclockweremismatchedwhenthemessage
type 2 and message type 4 match. Using the time when the receiver gets the PPP-B2b
correctionmessageasthereferencetime,andupdatingtheobservationvalueat1sintervals,
themismatchbetweenthePPP-B2bsatelliteclockandorbitproductswillbesignificantly
reduced. When the observation update interval is increased to 2 s, the probability of
mismatchoccurrenceissignificantlyreduced. Inthisstudy,theobservationvalueupdate
intervalinPPP-B2bpositioningwasinvestigatedwithatimecomparisonof30s.
ThePPP-B2bpositioningstudywasanalyzedusingthefourIFcombinationsinstatic
andsimulatedkinematicmode: BDSB1I/B3I,BDSB1C/B2a,BDSB1I/B3I+GPS,andBDS
B1C/B2a+GPS.Accordingtotheofficialdocument,theaverageconvergencetimewas
analyzed. AverageconvergencetimeusingthePPP-B2bproductwithBDSB1I/B3I+GPS,
BDSB1C/B2a+GPS,BDSB1I/B3I,BDSB1C/B2awas15.1/17.8/17.3/20.5min,respec-
tively. Regarding the PPP-B2b static position results, the average RMS values in the N,
E,andUdirectionsofonlyBDSPPP-B2bwerewithin1.5/2.7/3.9cm,respectively,and
thepositioningaccuraciesintheEandUdirectionscanbeimprovedto2.5/3.5cmusing
BDSandGPSdual-system. ComparedwithBDSB1C/B2a,BDSB1I/B3Ihascomparable
positioning accuracy in the N direction, and the accuracy in the U direction can be im-
provedby3-4mm. InthePPP-B2bsimulatedkinematicpositioningstudy, theaverage
RMSvaluesofthepositioningerrorsintheN,E,andUdirectionsforthecombinationof
BDSB1I/B3I+GPSandBDSB1I/B3Iwere3.4/5.8/7.6and3.8/6.6/7.8cm,respectively.
Meanwhile, theRMSvaluesofthepositionerrorsusingBDSB1C/B2a+GPSandBDS
B1C/B2awere3.6/4.9/8.1and4/6.1/8.5cm,respectively. Theresultsshowthat(1)the
PPP-B2bpositioningaccuracyusingB1I/B3IandB1C/B2acanapproachcentimeter-level
inthestaticmodeanddecimeter-levelinthesimulatedkinematicmode;and(2)compared
withB1I/B3IIFcombination,thepositioningaccuracyisimprovedintheEdirectionbut
reducedintheUdirectionatmillimeter-level.
InthePPP-B2btimetransferstudy,observationsofNTSCandTLtimelaboratoriesin
theAsia–PacificregioninvolvedinmaintainingTAIwereused. Thezero-baselineCCD
wasusedtoevaluatetheuncertaintyofreceivernoiselevelandtimecomparisonusing
preciseproducts. Theresultsshowthat(1)thezerobaselineCCDtimecomparisonnoise
level using the GBM product and the PPP-B2b product is within the fluctuation range
of0.1ns,respectively; (2)thelong-baselinetimecomparisondifferencebetweenresults
using the PPP-B2b product and the GBM product is within the range of ±0.5 ns; and
(3)accordingtotheAllan’scalculations,thetimecomparisonofthetwoproductsexhibits
consistentstability.
AuthorContributions:Conceptualization,Z.H.,L.M.andX.Z.;methodology,R.Z.andY.G.;software,
R.Z.,G.X.,W.G.andY.G.;validation,R.Z.,J.Z.,J.T.andX.L.;formalanalysis,R.Z.;resources,R.Z.and
J.Z.;datacuration,R.Z.,J.T.andX.L.;writing—originaldraftpreparation,R.Z.;writing—reviewand
editing,R.Z.,Z.H.,L.M.,G.X.,W.G.andX.Z.;supervision,Z.H.andL.M.Allauthorshavereadand
agreedtothepublishedversionofthemanuscript.
Funding: ThisresearchwasfundedbytheNationalNaturalScienceFoundationofChina,grant
number42104014;theWesternYouthScholarFoundationofChineseAcademyofSciences,grant
numberXAB2021YN26;theStateKeyLaboratoryofGeodesyandEarth’sDynamics,grantnumber
SKLGED2022-3-3.

<!-- PAGE: 20 -->

RemoteSens.2022,14,2769 20of21
DataAvailabilityStatement: Thedatasetsanalyzedareavailablefromthecorrespondingauthor
uponreasonablerequest.
Acknowledgments:TheauthorsacknowledgetheIGS,IGMAS,andGFZforsupportingobservation
dataandpreciseproducts.Meanwhile,wearegratefultoTLforprovidingtheobservationdata.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. ChinaSatelliteNavigationOffice. DevelopmentoftheBeiDouNavigationSatelliteSystem(Version4.0). Availableonline:
http://www.beidou.gov.cn/xt/gfxz/201912/P020191227430565455478.pdf(accessedon24April2022).
2. Yang,Y.X.Progress,contribution,andchallengesofCOMPASS/BeiDousatellitenavigationsystem.ActaGeod.Cartogr.Sin.2010,
39,1–6.
3. Yang,Y.X.;Gao,W.G.;Guo,S.R.;Mao,Y.;Yang,Y.F.IntroductiontoBeiDou-3navigationsatellitesystem.Navigation2019,66,
7–18.[CrossRef]
4. Yang,Y.X.;Mao,Y.;Sun,B.J.BasicperformanceandfuturedevelopmentsofBeiDouglobalnavigationsatellitesystem.Satell.
Navig.2020,1,1–8.[CrossRef]
5. Yang,Y.X.;Ding,Q.;Gao,W.G.;Li,J.L.;Xu,Y.Y.;Sun,B.J.PrincipleandperformanceofBDSBASandPPP-B2bofBDS-3.Satell.
Navig.2022,3,5.[CrossRef]
6. ChinaSatelliteNavigationOffice. TheApplicationServiceArchitectureofBeiDouNavigationSatelliteSystem(Version1.0).
Availableonline:http://www.beidou.gov.cn/xt/gfxz/201912/P020191227333024390305.pdf(accessedon24April2022).
7. ChinaSatelliteNavigationOffice.BeiDouNavigationSatelliteSystemSignalinSpaceInterfaceControlDocumentSatelliteBased
AugmentationSystemServiceSignalBDSBAS-B1C(Version1.0).Availableonline:http://www.beidou.gov.cn/xt/gfxz/202008
/P020200803362065480963.pdf(accessedon24April2022).
8. Chen,J.P.;Wang,A.H.;Zhang,Y.Z.;Zhou,J.H.;Yu,C.BDSSatellite-BasedAugmentationServiceCorrectionParametersand
PerformanceAssessment.RemoteSens.2020,12,766.[CrossRef]
9. Héroux,P.;Kouba,J.GPSprecisepointpositioningwithadifference.Geomatics1995,95,13–15.
10. Zumberge,J.F.;Heflin,M.B.;Jefferson,D.C.;Watkins,M.M.;Webb,F.H.Precisepointpositioningfortheefficientandrobust
analysisofGPSdatafromlargenetworks.J.Geophys.Res.-SolidEarth1997,102,5005–5017.[CrossRef]
11. Kouba,J.;Héroux,P.PrecisePointPositioningUsingIGSOrbitandClockProducts.GPSSolut.2001,5,12–28.[CrossRef]
12. RTCMSpecialCommittee.RTCMStandard10403.3DifferentialGNSS(GlobalNavigationSatelliteSystems)Services-Version3;No.104;
RTCM:Arlington,TX,USA,2016.
13. Weber,G.;Mervart,L.;Lukes,Z.;Rocken,C.;Dousa,J.Real-timeclockandorbitcorrectionsforimprovedpointpositioningvia
NTRIP.InProceedingsoftheIONGNSS20thInternationalTechnicalMeetingoftheSatelliteDivision,FortWorth,TX,USA,
25–28September2007.
14. Wang,Z.;Li,Z.;Wang,L.;Wang,X.;Yuan,H.AssessmentofMultipleGNSSReal-TimeSSRProductsfromDifferentAnalysis
Centers.IJGI2018,7,85.[CrossRef]
15. Elsobeiey,M.;Al-Harbi,S.Performanceofreal-timePrecisePointPositioningusingIGSreal-timeservice.GPSSolut.2016,20,
565–571.[CrossRef]
16. Wang,L.;Li,Z.S.;Ge,M.R.;Neitzel,F.;Wang,Z.Y.;Yuan,H.ValidationandAssessmentofMulti-GNSSReal-TimePrecisePoint
PositioninginSimulatedKinematicModeUsingIGSReal-TimeService.RemoteSens.2018,10,337.[CrossRef]
17. Li,X.X.;Ge,M.R.;Dai,X.L.;Ren,X.D.;Fritsche,M.;Wickert,J.;Schuh,H.Accuracyandreliabilityofmulti-GNSSreal-timeprecise
positioning:GPS,GLONASS,BeiDou,andGalileo.J.Geod.2015,89,607–635.[CrossRef]
18. Shi,J.B.;Yuan,X.X.;Cai,Y.;Wang,G.J.GPSreal-timeprecisepointpositioningforaerialtriangulation. GPSSolut. 2017,21,
405–414.[CrossRef]
19. Ge, Y.L.; Chen, S.X.; Wu, T.; Fan, C.M.; Qin, W.J.; Zhou, F.; Yang, X.H. An analysis of BDS-3 real-time PPP: Time transfer,
positioning,andtroposphericdelayretrieval.Measurement2021,172,108871.[CrossRef]
20. Ge,Y.L.;Zhou,F.;Liu,T.J.;Qin,W.J.;Wang,S.L.;Yang,X.H.Enhancingreal-timeprecisepointpositioningtimeandfrequency
transferwithreceiverclockmodeling.GPSSolut.2019,23,20.[CrossRef]
21. TheCabinetOffice,GovernmentofJapan.Quasi-ZenithSatelliteSystemInterfaceSpecificationCentimeterLevelAugmentation
Service(IS-QZSS-L6-004). Availableonline: https://qzss.go.jp/en/technical/download/pdf/ps-is-qzss/is-qzss-l6-004.pdf
(accessedon24April2022).
22. European Global Navigation Satellite Systems Agency. Galileo High Accuracy Service (HAS) Info Note. Available online:
https://www.gsc-europa.eu/sites/default/files/sites/all/files/Galileo_HAS_Info_Note.pdf(accessedon24April2022).
23. ChinaSatelliteNavigationOffice.BeiDouNavigationSatelliteSystemSignalinSpaceInterfaceControlDocumentPrecisePoint
PositioningServiceSignalPPP-B2b(Version1.0).Availableonline:http://www.beidou.gov.cn/xt/gfxz/202008/P0202008033620
62482940.pdf(accessedon24April2022).
24. Tao,J.;Liu,J.N.;Hu,Z.G.;Zhao,Q.L.;Chen,G.;Ju,B.X.InitialAssessmentoftheBDS-3PPP-B2bRTSComparedwiththeCNES
RTS.GPSSolut.2021,25,131.[CrossRef]

<!-- PAGE: 21 -->

RemoteSens.2022,14,2769 21of21
25. Xu,Y.Y.;Yang,Y.X.;Li,J.L.PerformanceevaluationofBDS-3PPP-B2bprecisepointpositioningservice.GPSSolut.2021,25,142.
[CrossRef]
26. Nie,Z.X.;Xu,X.F.;Wang,Z.J.;Du,J.InitialAssessmentofBDSPPP-B2bService:PrecisionofOrbitandClockCorrections,and
PPPPerformance.RemoteSens.2021,13,2050.[CrossRef]
27. Guo,F.;Zhang,X.H.;Wang,J.L.TiminggroupdelayanddifferentialcodebiascorrectionsforBeiDoupositioning.J.Geod.2015,
89,427–445.[CrossRef]
28. Zhou,F.;Dong,D.A.;Ge,M.R.;Li,P.;Wickert,J.;Schuh,H.SimultaneousestimationofGLONASSpseudorangeinter-frequency
biasesinprecisepointpositioningusingundifferencedanduncombinedobservations.GPSSolut.2018,22,19.[CrossRef]
29. Wei, P.; Yang, C.Z.; Yang, X.H.; Cao, F.; Hu, Z.Y.; Li, Z.G.; Guo, J.; Li, X.H.; Qin, W.J. Common-View Time Transfer Using
GeostationarySatellite.IeeeTrans.Ultrason.Ferroelectr.Freq.Control.2020,67,1938–1945.
30. Wu,J.T.;Wu,S.C.;Hajj,G.A.;Bertiger,W.I.;Lichten,S.M.EffectsofantennaorientationonGPScarrierphase. Manuscr. Geod.
1993,18,91–98.
31. Rovera,G.D.;Torre,J.M.;Sherwood,R.;Abgrall,M.;Courde,C.;Laas-Bourez,M.;Uhrich,P.Linkcalibrationagainstreceiver
calibration:AnassessmentofGPStimetransferuncertainties.Metrologia2014,51,476–490.[CrossRef]
32. Xiao,G.W.;Liu,G.Y.;Ou,J.K.;Liu,G.L.;Wang,S.L.;Guo,A.Z.MG-APP:Anopen-sourcesoftwareformulti-GNSSprecisepoint
positioningandapplicationanalysis.GPSSolut.2020,24,66.[CrossRef]
33. Saastamoinen,J.H.AtmosphericCorrectionfortheTroposphereandtheStratosphereinRadioRangingSatellites.UseArtif.Satell.
Geod.1972,15,247–251.
34. Boehm,J.;Niell,A.;Tregoning,P.;Schuh,H.GlobalMappingFunction(GMF):Anewempiricalmappingfunctionbasedon
numericalweathermodeldata.Geophys.Res.Lett.2006,33,3–6.[CrossRef]
35. ChinaSatelliteNavigationOffice.BeiDouNavigationSatelliteSystemOpenServicePerformanceStandard(Version3.0).Available
online:http://www.beidou.gov.cn/xt/gfxz/202105/P020210526216231136238.pdf(accessedon28May2022).
36. Guang,W.;Dong,S.W.;Wu,W.J.;Zhang,J.H.;Yuan,H.B.;Zhang,S.G.ProgressofBeiDoutimetransferatNTSC.Metrologia2018,
55,175–187.[CrossRef]
37. Liang,K.;Arias,F.;Petit,G.;Jiang,Z.H.;Tisserand,L.;Wang,Y.;Yang,Z.Q.;Zhang,A.M.EvaluationofBeiDoutimetransferover
multipleinter-continentalbaselinestowardsUTCcontribution.Metrologia2018,55,513–525.[CrossRef]
38. Guang,W.;Zhang,J.H.;Yuan,H.B.;Wu,W.J.;Dong,S.W.AnalysisonthetimetransferperformanceofBDS-3signals.Metrologia
2020,57,065023.[CrossRef]