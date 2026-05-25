<!-- PAGE: 1 -->

remote sensing
Article
Low-Cost IMU and Odometer Tightly Augmented
PPP-B2b-Based Inter-Satellite Differenced PPP in
Urban Environments
YuMin1,2 ,ZhouzhengGao1,* ,JieLv1,RuohuaLan1,QiaozhuangXu1andChengYang1
1 SchoolofLandScienceandTechnology,ChinaUniversityofGeosciencesBeijing,Beijing100083,China
2 AerospaceInformationResearchInstitute,ChineseAcademyofSciences,Beijing100094,China
* Correspondence:zz.gao@cugb.edu.cn;Tel.:+86-186-2791-5172
Abstract: Since 23 June 2020, BDS-3 has been entirely operated and obtained the ability of global
PNT(Positioning,Navigation,andTiming)services. Afterward,real-timePrecisePointPositioning
(PPP)serviceisavailableinChina’ssurroundingareasviaBDS-3PPP-B2bsignal. However, such
areal-timePPPservicecannotmaintainthehighaccuracyandcontinuityofpositioningsolutionsin
challengingenvironments,suchasurbanenvironments.Forthat,wecarriedoutamodelbyintegrating
between-satellite single-differenced (BSSD) PPP, a low-cost Inertial Navigation System (INS), and
anodometerviaanextendedKalmanfilter.Theperformanceofthisintegrationmodelwasassessed
withvehicle-bornedata.Resultsdemonstratedthat(1)thepositionRMS(RootMeanSquare)ofBSSD
PPPare64.33cm,53.47cm,and154.11cm.ComparedwithBSSDPPP,about31.2%,23.3%,and27.3%
positionimprovementscanbeachievedbyusingINS.FurtherenhancementsofpositionRMSbenefiting
fromtheodometerare1.34%,1.41%,and1.73%inthethreedirections. (2)Anyway,theaccuracyof
BSSDPPP/INS/Odometertightlycoupledintegrationisslightlyhigherthanthatofundifferenced
PPP/INS/Odometerintegration,withaverageimprovementpercentagesof7.71%,3.09%,and0.27%.
Meanwhile,theperformanceofBSSDPPP/INS/Odometerintegrationduringtheperiodswithsatellite
outagesisbetterthantheundifferencedPPP-basedsolutions.(3)Theimprovementsinattitudesfrom
anodometeraremoresignificantonheadinganglethantheothertwoattitudes,withpercentagesof
25.00%.(4)DuringfrequentGNSSoutageperiods,thereductioninaveragemaximumpositiondrifts
Citation:Min,Y.;Gao,Z.;Lv,J.;Lan,
providedbyINSare18.01%,8.95%,and20.74%.Afterintegratingwithanodometer,thedriftscanbe
R.;Xu,Q.;Yang,C.Low-CostIMU
furtherlydecreasedby25.11%,15.96%,and20.69%. Forattitude,about41.67%reductioninaverage
andOdometerTightlyAugmented
maximumdriftsofheadinganglesisobtained.
PPP-B2b-BasedInter-Satellite
DifferencedPPPinUrban
Keywords:real-timePrecisePointPositioning(RT-PPP);InertialNavigationPystem(INS);odometer;
Environments.RemoteSens.2023,15,
PPP-B2bservice;tightlycoupledintegration
199. https://doi.org/10.3390/
rs15010199
AcademicEditor:XiaogongHu
1. Introduction
Received:17November2022
Revised:15December2022 ChinabegantobuildBeiDouNavigationSatelliteSystem(BDS)attheendofthe20th
Accepted:26December2022 centuryaccordingtothethree-stepdevelopmentstrategies[1].Asplanned,thefirst-generation
Published:30December2022 BDS(BDS-1),thesecond-generationBDS(BDS-2),andthethird-generationBDS(BDS-3)were
completedsuccessivelyin2003,2012,and2020,withthecorrespondingsatelliteconstellations
of3GeostationaryOrbit(GEO)satellites,5GEOsatellites+5IGSO(InclinedGeosynchronous
Orbit)satellites+4MEO(MediumEarthOrbit)satellites,and3GEO+3IGSO+24MEOsatellites,
Copyright: © 2022 by the authors.
respectively.Currently,theglobalPositioning,Navigation,andTiming(PNT)servicesofBDSare
Licensee MDPI, Basel, Switzerland.
supportedbysignalsonfrequenciesB1I(1561.098MHz),B2I(1207.14MHz),B3I(1268.52MHz),
This article is an open access article
B1C(1575.42MHz),B2a(1176.45MHz),andB2b(1207.14MHz)[2–7].Amongtheseservices,
distributed under the terms and
thePrecisePointPositioning(PPP)-B2benhancementserviceisofgreatsignificance,andalsoit
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// isconsideredtobethecoresupportforsmartcitydevelopmentinChina.
creativecommons.org/licenses/by/ PPP,whichwasproposedbyZumbergeretal.[8]in1997,isthefavoredtechnologyfor
4.0/). high-accuracypositioningapplications.Thecorrespondingmodelwasfurtherlydeveloped
RemoteSens.2023,15,199.https://doi.org/10.3390/rs15010199 https://www.mdpi.com/journal/remotesensing

<!-- PAGE: 2 -->

RemoteSens.2023,15,199 2of20
intheworks[8–10]. PPPcanprovideanaccuratepositioningsolutionusingonlyasingle
GNSSreceiverbyutilizingprecisesatelliteproductswithabouttwoweeksdelay[11–13].
Consequently,PPPismainlyforapplicationsinpost-processingcurrently[14,15].Tosatisfythe
demandsofreal-timePPP,BDS-3transmitstheorbit/clockcorrectionsofbroadcastephemeris
by B2b signal [16–19]. Multi-GNSS Experiment (MGEX)/iGMAS stations were adopted
in[17]toverifythereal-timePPPpositioningperformanceusingPPP-B2bserviceinstaticand
simulated-kinematicmodesbycomparingwiththesolutionsbasedonGeodeticBenchmark
(GBM)finalproducts.Itisshownthatthepositioningperformanceofreal-timePPPisslightly
worsethanthepost-processingPPPingeneral,accordingtothestatisticalresults.However,
theconvergencetimeofreal-timePPPisslightlyshorterfortheBDS-onlyinastaticmodel.
Taoetal.[16]comparedPPP-B2bservicewithReal-TimeService(RTS)providedbyCentre
Nationald’EtudesSpatiales(CNES).Basedontheanalysisfromsixstationsdistributedin
China,thepositioningaccuracyofBDS-3-onlyPPPwithPPP-B2bserviceinkinematicmode
canachievedecimeter-levelpositioningresults,whichisconsistentwiththeaccuracyofGPS
PPPusingproductsofCNES.
However,suchaPPP-B2bservice-basedPPPcannotmaintainpositioningaccuracy
and continuity in urban environments [20,21], such as under bridges or trees, etc. In
ordertoovercometheshortcomingsofPPPinthosecircumstances,anInertialNavigation
System (INS) is integrated. INS is capable of providing position, velocity, and attitude
resultsbyusingmeasurementsfromInertialMeasurementUnits(IMU)withoutexternal
observations. However,thepositionerrorsofINSwillaccumulaterapidlyovertime[22,23].
Meanwhile,integratingPPPandINScanestimateandcompensateIMUerrorstorestrain
thedivergence[20,22,24]. Accordingtopreviousworks,morereliablepositionresultscan
beobtainedbyPPP/INS[20,21,25–29].
Leetal.[25]investigatedtheLooselyCoupledIntegration(LCI)ofSingleFrequency
(SF)PPP/INS,whichwasvalidatedbyaflightexperiment.ResultsshowedthattheSF-PPP-
onlypositioningperformanceisvisiblyimprovedinthehorizontalandverticalcomponents.
LCI mode cannot work when there are not enough GNSS observations. Martell in [26]
furtherappliedtheTightlyCoupledIntegration(TCI)ofPPPandINSusingdifferentgrade
IMUsanddifferentcut-offsatelliteangles. Theresultsshowedthatreliableresultscould
be obtained even if the number of satellites is less than 4. In [27], TCI was compared
with LCI by using a tactical-grade IMU to illustrate the benefits of TCI. The position
differencesofTCIarewithin1.0m,andsucherrorsofLCIarewithin5.0m. Thestudies
abovearemainlybasedonundifferencedGNSSobservations. TheDualFrequency(DF)
PPP/INSintegrationusingSingle-DifferenceBetween-Satellites(BSSD)GPSobservations
was applied in [28]. During the simulated outages of 10 s~30 s, the position accuracy
ofBSSDPPP/INSTCIcanbedecimeter-level. Suchaccuracyishigherthanthoseusing
undifferencedobservations. Owingtotheevolutionofmulti-constellationGNSS(multi-
GNSS),moreavailableobservationscanbeadoptedtoenhancetheintegrationperformance.
Gao et al. [21] developed the multi-constellation (GLONASS, BDS, and GPS) TCI of SF
PPP/INS, and it was verified by a set of land-borne experiment data. Results showed
that significant positum improvements in terms of accuracy, continuity, and reliability
couldbeobtainedbyINSaiding. Anyway,theperformanceofconventionalGPSSF-PPP
can be improved by utilizing the multi-GNSS observation. The enhancement of multi-
GNSS on PPP/INS is also illustrated in [29]. According to the results, the positioning
andconvergenceperformanceofPPPisenhancedsignificantlybymulti-GNSSandINS.
However,suchimpactsintermsofvelocityandattitudeareinvisible.
Basedontheworksin[20–29],continuoussolutionswithhighaccuracycanbepro-
videdbythePPP/INSintegrationduringGNSSoutages. However,thepositioningerrors
ofPPP/INSstillaccumulaterapidly,especiallyforalow-costIMUwhentheGNSSsignal
seriously deteriorates, even interrupts completely around high buildings or under tun-
nels[30,31]. Suchacircumstancecanbefacilitatedbyusingthevelocityinformationfrom
anodometer. In[31],GPS+GLONASSDF-PPPwasintegratedwithINSandodometer,
and simulated GNSS outages were utilized to evaluate the performance in challenging

<!-- PAGE: 3 -->

RemoteSens.2023,15,199 3of20
circumstances. Accordingtotheresults,thepositionaccuracywasfurtherlyameliorated
bytheodometer.
Inthispaper,weimpliedPPP/INS/odometertightlycoupledintegrationmodel. In
comparison with previous works, the contribution of this paper is that such a tightly
coupledintegrationisbasedontheBSSDmodelandtheBDS-3PPP-B2borbit/clockcor-
rections. Inordertoassesstheperformanceofthisalgorithm,vehicle-bornedataacquired
inurbanenvironmentsareprocessedandanalyzed. Theenhancementsofalow-costINS,
BSSDBDS-3PPPmodel,andanodometeronpositioningandattitudedeterminationare
discussedindetail.
2. Methodology
Inthissection,themethodtorecoverpreciseorbitandclockoffsetsbyusingthePPP-
B2bserviceisdiscussedfirst. Then,themodelsofPPP/INSTCIandPPP/INS/odometer
TCIbasedontherecoveredPPP-B2borbit/clockoffsetsandBSSDobservationarepresented
indetail.
2.1. RecoveryofPreciseSatelliteOrbit/ClockwithPPP-B2b
TheinformationprovidedbythePPP-B2bserviceincludestheorbitandsatelliteclock
offsetcorrectionsofbroadcastproductsinthesatellite-fixedframe(radial,along,andcross
directions),whichcannotbeuseddirectlyinpositioning. Thus,toapplythecorrections
in PPP, the precise orbit and clock offsets need to be recovered. The satellite positions
computedbybroadcastephemerisaregivenintheEarth-CenteredEarth-Fixedreference
(ECEF)frame(e-frame). Therefore,theorbitcorrectionsmustbetransformedintotheECEF
frameby[32]
   
δO δO
x radial
(cid:2) (cid:3)
δO y = e radial e along e cross δO along (1)
δO
z
δO
cross
With

e =r/|r|
 radial . (cid:12) .(cid:12)
e cross = (r×r)/(cid:12)r×r(cid:12) (2)
e = e ×e
along radial cross
(cid:2) (cid:3)T
where δO radial δO cross δO along istheorbitcorrectionvectorinthesatellite-fixedframe;
(cid:2) (cid:3)T
δO δO δO representstheorbitcorrectionvectorinthee-frame; r isthesatellite
x y z
.
positionvectorandr representsthesatellitevelocityvector,whichcanbecomputedby
broadcastephemeris.
ByapplyingthecorrectionsinEquation(1)tobroadcastephemeris,precisesatellite
positionscanbecalculatedby
     
X X δO
x
Y = Y −δO y (3)
Z Z δO
prec,B2b brdc z
(cid:2) (cid:3)T
where X Y Z denotes the vector of precise satellite positions after using the
prec,B2b
(cid:2) (cid:3)T
correctionsprovidedbyPPP-B2bservice; X Y Z isthevectorofsatellitepositions
brdc
calculatedbybroadcastephemeris.
PPP-B2bservicealsoprovidesthecorrectionofsatelliteclockoffset. Thepreciseclock
offsetscanbeobtainedby
C
dts = dts − 0 (4)
prec,B2b brdc c
wheredts isthepreciseclockoffsetcalculatedbyusingtheclockoffsetderivedfrom
prec,B2b
broadcastephemeris(dts )andthePPP-B2bclockcorrectionparameter(C );cdenotes
brdc 0
thevelocityoflight.

<!-- PAGE: 4 -->

RemoteSens.2023,15,199 4of20
2.2. Single-Differencebetween-SatellitesObservationalModel
The linearized undifferenced Ionosphere-Free (IF) model of the satellite (k) can be
writtenas
Pk −ρk−∆ρk = e δx +e δy +e δz +ct +m δd +ε (5)
IF P,IF 1 r 2 r 3 r r wet wet P,IF
Lk −ρk−∆ρk = e δx +e δy +e δz +ct +m δd −λ Nk +ε (6)
IF L,IF 1 r 2 r 3 r r wet wet IF IF L,IF
where Pk = αP −βP and Lk = αL −βL are IF pseudorange and carrier-phase,
IF 1 2 IF 1 2
whereinα = f2/(f2− f2)andβ = f2/(f2− f2)areIFcombinationcoefficientsbasedon
1 1 2 2 1 2
frequencies f and f ;randkrepresentreceiverandsatellite;ρk isthegeometricdistance
1 2
betweenreceiverandsatellite;t representsthereceiverclockoffset;m isthetropospheric
r wet
(cid:2) (cid:3)T
wetdelaymappingfunction;δd isthecorrectionsofzenithwetdelay;E = e e e
is the orientation cosine vector w ; et δpe = (cid:2) δx δy δz (cid:3) represents receiv 1 er p 2 ositi 3 on
GNSS r r r
correctionine-frame; λ istheIFwavelength; Nk istheIFfloatambiguity[13]; ∆ρk
IF IF L,IF
and ∆ρk are the errors sum of carrier-phase and pseudorange; ε and ε are the
P,IF L,IF P,IF
measurementnoiseofcarrier-phaseandpseudorange[33].
Inadditiontothepseudorangeandcarrier-phasemeasurements,theDopplermeasure-
mentsareessentialforcalculatingreceivervelocity. Thelinearizedobservationequationof
Dopplercanbeexpressedas
Dk −ρ .k−∆ρ .k = e δv +e δv +e δv +ct . +ε (7)
IF D,IF 1 x,r 2 y,r 3 z,r r D,IF
whereDk = αDk−βDkistheDopplermeasurementinmeters;jrepresentsfrequency;the
IF 1 2
dotabovethesymbolindicatesthevariation. Ingeneral,exceptforthevariationofreceiver
. .k
clocks(t ),satelliteclocks,andgeometricdistance(ρ ),othererrors’variationsareclose
r
tozeroandareignored. δve = (cid:2) δv δv δv (cid:3) arethevectorofreceivervelocity
GNSS x,r y,r z,r
corrections;∆ρ .k denotesthesumofDopplererrors;ε isDopplernoise.
D,IF D
Compared to the undifferenced model, the BSSD model has the advantage that
receiver-relatederrorssuchasthereceiverclock,receiverhardwaredelay,andunmodelled
errorscanbeeliminated[28,34]. TheBSSDIFmodelcanbeobtainedby
∆Pkm−∆ρkm−∆ρkm = ekmδx +ekmδy +ekmδz +mkmδd +εkm (8)
IF P,IF 1 r 2 r 3 r wet wet P,IF
∆Lkm−∆ρkm−∆ρkm = ekmδx +ekmδy +ekmδz +mkmδd −λ δNkm+εkm (9)
IF L,IF 1 r 2 r 3 r wet wet IF IF L,IF
∆Dkm−∆ρ .km−∆ρ .km = ekmδv +ekmδv +ekmδv +εkm (10)
IF D,IF 1 x,r 2 y,r 3 z,r D,IF
where ∆Lkm = Lm − Lk ; ∆Pkm = Pm −Pk ; ∆Dkm = Dm −Dk ; ∆ρkm = ρm −ρk;
IF IF IF IF IF IF IF IF IF
∆ρ .km = ρ .m−ρ .k ; δNkm = δNm −δNk ; superscripts k and m represent satellite and the
IF IF IF
referencesatellite. Inthispaper,GPSandBDSseparatelychoosethereferencesatellite.
2.3. BSSDPPP/INSTightlyCoupledIntegration
TheinnovationvectorofTCIisbasedonthedifferencebetweenGNSSobservations
(pseudorange, carrier-phase, and doppler) and the corresponding values predicted by
INS[20,21,28]. Thestateequationandobservationequationcanbeexpressedas
X TCI,k = φ TCI,k,k−1 X TCI,k−1 +µ TCI,k−1 ,µ TCI,k−1 ∼ (0,Q TCI,k ) (11)
Z = H X +η ,η ∼ N(0,R ) (12)
TCI,k TCI,k TCI,k TCI,k TCI,k TCI
   
P −P Z
GNSS,IF INS,IF PIF
Z TCI,k = L GNSS,IF −L INS,IF = Z LIF  (13)
D −D Z
GNSS,IF INS,IF DIF

<!-- PAGE: 5 -->

RemoteSens.2023,15,199 5of20
where φ TCI,k,k−1 is the system transform matrix from epoch k−1 to epoch k; µ TCI,k−1
represent the state noise with the covariance of Q ; Z , Z , and Z represent
TCI,k PIF LIF DIF
theinnovationvectorofpseudorange, carrier-phase, anddoppler, respectively; P ,
INS,IF
L , and D are the INS-predicted values; P , L , D are the
INS,IF INS,IF GNSS,IF GNSS,IF GNSS,IF
GNSSmeasurement;η representsobservationnoisewiththepriorcovarianceofR .
TCI,k TCI
InordertoobtaintheINS-predictedvaluescorrespondingtoGNSSmeasurements,the
positionandvelocityofthereceiverupdatedbyINSmechanizationarerequired. However,
thereferencecentersoftheINSandGNSSantennaaredifferentfromeachother,which
results in a lever-arm system offset. Therefore, the linearization functions Z after
TCI,k
consideringtheleverarmcanbewrittenas[22,29]
 (cid:16) (cid:16) (cid:17) (cid:17) 
 δZ  C 1 δpn INS + C b nlb× δψ +cδt r −m wet d wet
PIF  (cid:16) (cid:16) (cid:17) (cid:17) 
δZ TCI,k = δZ LIF  =   C 1 δpn INS + C b nlb× δψ +cδt r −m wet d wet +δN IF λ IF   (14)
δZ DIF  C
2
D−1δpn
INS
+C
n
eH
ψ
δψ+C
n
eδvn
INS
+C
n
eC
b
n (cid:16) lb× (cid:17) δω
i
b
b
+cδt .
r

 
1/(R +h) 0 0
M
D −1 =  0 1/(R N +h)cos(B) 0  (15)
0 0 −1
whereδZ ,δZ ,andδZ representthedifferentialformofinnovationvector;n,b,and
PIF LIF DIF
j
iarethenavigationframe(n),thebodyframe(b),andtheinertialframe(i);C (k=nandb,
k
j=eandn)representtherotationmatrixfromthek-frametothej-frame;lb isthelever-arm;
δpn ,δvn ,andδψarethecorrectionsofposition,velocity,andattitudeatIMUcenter
INS INS
.
inn-frame;δt andδt representthecorrectionsofreceiverclockoffsetanddrift;C isthe
r r 1
rotationmatrixofpositioncorrectionsfrome-frameton-frame;C isthedifferentialform
2
ofCe;δωb meansgyroscopeerrors[22,29].
n ib
BasedonEquation(12),thesatellitesingle-differencematrix(SSDM)canbeexpressed
as[28]
(cid:20) (cid:21)
SSDM 0
SSDM = G (16)
0 SSDM
B 3h×2m
 
1 0 ··· −1 0 0 ··· 0
 0 ... 0 −1 . . . . . . 0 . . .  
 
. . . . .
. . 0 1 −1 . . . . . . . .
 
. . . . . . . .
. . . . . . . . . . . . . . . .
SSDM =   (17)
B . . .
. . . . 0 −1 1 0 ··· . .
 
   . . . . . . . . . −1 . . . ... 0 . . .   
. . 
  . . 0 . . −1 0 ··· 1 0  
0 ··· 0 −1 0 0 ··· 1
h2 ×m
whereSSDM isobtainedreferringtoSSDM ;h andh (h = h +h )arethetotalnumber
G B 1 2 1 2
ofGPSandBDSavailablesatellites;mrepresentsthenumberofestimatedparametersfor
theBSSDmodel. BSSDcoefficientmatrix H andinnovationvector Z
BSSD,TCI,k BSSD,TCI,k
canbecalculatedby
H = SSDM×H ×SSDMT (18)
BSSD,TCI,k TCI,k
Z = SSDM×Z ×SSDMT (19)
BSSD,TCI,k TCI,k
R = SSDM×R ×SSDMT (20)
BSSD,TCI TCI

<!-- PAGE: 6 -->

RemoteSens.2023,15,199 6of20
Inaddition,thereisInter-SystemBias(ISB)betweenGPSandBDS[35,36].Tosolvethis
problem,weconsiderthereceiverclockoffsetofdifferentGNSSasindependentparameters
andestimatethemseparately. Thismethodispresentedindetailintheworksof[37,38].
Anyway,therearetwoothermethodstoprocessISB[6,36,39]. Itisworthmentioningthat
thereceiverclockoffset,anddriftcanberemovedintheBSSDPPP/INSTCImodel,with
thestatevectorof
X = (cid:2) δpn δvn δψ δB δB δS δS δd δNkm(cid:3) (21)
BSSD,TCI,k INS INS a g a g wet IF
where δpn , δvn , and δψ represent the corrections of position, velocity, and attitude;
INS INS
δS and δB represent the scale factor and bias of gyroscope; δS and δB represent the
g g a a
scalefactorandbiasofaccelerometers[40];δd isawetcomponentoftroposphericzenith
wet
delay,andδN representsambiguity.
IF
2.4. Odometer-AidedBSSDPPP/INSTightly-CoupledIntegration
Inmotionscenarios,thevehicledoesnotslipsidewaysandupward,whichmeans
thatthevelocityonlateralandverticalwillbeclosetozeroandonlytheforwardspeed
exists[31,32]. Meanwhile,theforwardvelocityobtainedfromanodometercanbeusedas
apseudo-measurement. However,theodometer-measuredvelocitywillbeinfluencedby
thescalefactorerror
v ≈ (cid:2) vv/(1+S ) 0 0 (cid:3)T (22)
o o o
wherevv istheforwardvehiclevelocitymeasuredbytheodometerinthevehicleframe(v);
o
S representthescalefactorwhichcanbemodeledasarandomwalkprocess.
o
Theinnovationvectoroftheodometercanbecalculatedbythedifferencebetween
thevelocitymeasuredbytheodometerandpredictedbyINSpredictedone. However,the
v-frameandtheb-framearenotusuallyalignedtheoretically. Therefore,theinnovation
vector(Z )canbedescribedby
o
 vv/(1+S )   vF 
o o INS
Z o = vv o −C b vvb INS ≈  0 −vR INS +η,η ∼ N(0,σ o 2) (23)
0 vD
INS
whereCv denotestherotationmatrixfromb-frametov-frame;ηisthevectorofodometer
b
innovationnoisewiththepriorvarianceofσ2.
o
AccordingtoEquation(11),Z canbefurtherlyexpressedas
BSSD,TCI,k
(cid:20)
SSDM×Z
×SSDMT(cid:21)
Z = TCI,k (24)
BSSD,TCI,k vv−Cvvb
o b INS
withthelinearizedformof
(cid:16) (cid:16) (cid:17) (cid:17)
δZ = vvδS −Cv Cbδvn −Cb(vn ×)δψ− lb× ωbδS (25)
o o o b n INS n INS o ib g
whereδS isthecorrectionoftheodometerscalefactor;lb denotesthelever-armbetween
o o
thereferencecenteroftheodometerandIMUintheb-frame. ThecorrespondingBSSD
statevectorcanbeexpressedas
X = (cid:2) δpn δvn δψ δB δB δS δS δS δd δNkm(cid:3) (26)
BSSD,TCI,k INS INS a g a g o wet IF
thestatevectorcanbeestimatedbytheEKF[41,42]
X BSSD,TCI,k = X BSSD,TCI,k,k−1 +K k (Z BSSD,TCI,k −H BSSD,TCI,k X BSSD,TCI,k,k−1 ) (27)
P BSSD,TCI,k = (I−K k H BSSD,TCI,k )P BSSD,TCI,k,k−1 (I−K k H BSSD,TCI,k )T+K k R BSSD,TCI K k T (28)

<!-- PAGE: 7 -->

RemoteSens.2023,15,199 7of20
Remote Sens. 2023, 15, x FOR PEER REVIEW 8 of 22
ThealgorithmstructureofPPP/INS/ODOTCIisshowninFigure1.
Figure 1. Algorithm of BSSD PPP/INS/ODO TCI structure.
Figure1.AlgorithmofBSSDPPP/INS/ODOTCIstructure.
33..T Teesststs,,R Reessuultlsts,,a annddD Disisccuussssioionn
IInno orrddeerrt tooe evvaaluluaatteet thheep peerrffoorrmmaanncceeo offt thheep prrooppoosseeddm mooddeel,l,a as seetto offl alanndd--bboorrnneed daattaa
wwaassp prroocceesssseedda anndda annaalylyzzeedd.. TThhiiss fifrirsstts suubbsseeccttiioonn ddeemmoonnssttrraatteess tthhee eexxppeerriimmeenntt ddeettaaiillss,,
ininccluluddininggt thheee exxppeerriimmeennttaalle eqquuiippmmeenntt,, ssaatteelllliittee aavvaaiillaabbiilliittyy,,a anndd ddaattaa pprroocceessssiinngg sscchheemmeess..
TThhees seeccoonndds usubbsescetcitoinona sassessessessetsh tehaec accucruarcaycoyf otfh ethPeP PPP-BP2-Bb2cbo rcroercrteioctnisonans danthde thpeo spitoiosintiionng-
pienrgf oprmerafonrcmeoanfcBeS SoDf BPSPSPD.T hPePPth. irTdhseu tbhsiercdt iosunbvsaelcitdiaotne svtahleidiamtepsa ctthseo ifmINpSac,ttsh eoof dINomS,e ttehre
oondPoPmPetpeor sointi oPnPiPn gp,oasnitdiotnhiengef, faencdto tfhteh eeffBeSctS Dof mthoed BeSlSoDn mthoedpeol sointi othnein pgospietirofonrinmga pnecrefoorf-
BmSSaDncPe PoPf/ BINSSSD/O PDPOP/TINCSI./OThDeOla sTtCsuI.b Tsehcet iolansta nsaulbyszeecstitohne iannflaulyenzeces stohfet hinefoludeonmceeste orfa nthde
BoSdSoDmmetoedr ealnodn BaSttSiDtu dmeoddeetle ormn ainttaittiuodne. determination.
3.1. DataCollection
3.1. Data Collection
ThetestvehiclewasequippedwithaNovAtelGNSSreceiver,alow-costINS616IMU,and
The test vehicle was equipped with a NovAtel GNSS receiver, a low-cost INS616
anodometerinBeijingon23December2021.ThesamplingratesofGNSS,IMU,andodometer
IMU, and an odometer in Beijing on 23 December 2021. The sampling rates of GNSS, IMU,
measurementsweresetto1Hz,125Hz,and100Hz,respectively. Thedesignedtestroute,
and odometer measurements were set to 1 Hz, 125 Hz, and 100 Hz, respectively. The de-
availablesatellitenumber,andPDOP,alongwiththetrajectory,areshowninFigures2and3.
signed test route, available satellite number, and PDOP, along with the trajectory, are
The trajectory is mainly on urban environments with many buildings on both sides of the
shown in Figures 2 and 3. The trajectory is mainly on urban environments with many
road. TheaveragenumberofsatellitesofGPS,BDS-3,andBDS-3/GPSare6.1,8.5,and14.5.
buildings on both sides of the road. The average number of satellites of GPS, BDS-3, and
ThecorrespondingPDOPare2.3, 2.1, and1.4, respectively. Asisshown, thecontinuityof
BDS-3/GPS are 6.1, 8.5, and 14.5. The corresponding PDOP are 2.3, 2.1, and 1.4, respec-
thistestispoor,especiallyforGPS-onlyandBDS-only. ThecombinationofGPSandBDS-3
tively. As is shown, the continuity of this test is poor, especially for GPS-only and BDS-
canimproveit,buttherearestillmanyperiodswithGNSSoutages. Forexample,the1500s
only. The combination of GPS and BDS-3 can improve it, but there are still many periods
to2500sandthe6500sto7500sarethemosttypicalscenes. Basedontheprecisesatellite
with GNSS outages. For example, the 1500 s to 2500 s and the 6500 s to 7500 s are the most
orbit/clockrecoveredbythecorrectionsobtainedbyBDSPPP-B2bservice,sixdataprocessing
typical scenes. Based on the precise satellite orbit/clock recovered by the corrections ob-
strategies,namelyundifferencedPPP,BSSDPPP,BSSDPPP/INSTCI,BSSDPPP/INSTCI,BSSD
tained by BDS PPP-B2b service, six data processing strategies, namely undifferenced PPP,
PPP/INS/ODOTCI,andundifferencedPPP/INS/ODOTCIwillbeimplied.Theresultswill
BSSD PPP, BSSD PPP/INS TCI, BSSD PPP/INS TCI, BSSD PPP/INS/ODO TCI, and undif-
becomparedtothesolutionsofRTK/INSTCIcalculatedbytheInertialExplorer(IE)software.
ferenced PPP/INS/ODO TCI will be implied. The results will be compared to the solutions
of RTK/INS TCI calculated by the Inertial Explorer (IE) software.

<!-- PAGE: 8 -->

Remote Sens. 2023, 15, x FOR PEER REVIEW 9 of 22
Remote Sens. 2023, 15, x FOR PEER REVIEW 9 of 22
RemoteSens.2023,15,199 8of20
Figure 2. The available satellites number of different GNSS al ong with the test trajectory.
Figure2.TheavailablesatellitesnumberofdifferentGNSSalongwiththetesttrajectory.
Figure 2. The available satellites number of different GNSS along with the test trajectory.
Figure3.PDOPofdifferentGNSSalongwiththetesttrajectory.
Figure 3. PDOP of different GNSS along with the test trajecto ry.
3.2. AccuracyofPPP-B2bCorrectionsandBSSDPPP
Figure 3. PDOP of different GNSS along with the test trajectory.
3.2. AccPurercaicsye oofr bPitPaPn-dB2clbo cCkoorfrfescettiopnrosd auncdts BreScSoDve rPePdPb y the corrections from the PPP-
B2b service are utilized to process the satellite’s orbit/clock errors. In order to assess
3.2. PArceccuirsaec oy robf iPt aPnPd-B c2lob cCko orrffescetito pnrso adnudc BtsS rSeDco PvPePre d by the corrections from the PPP-B2b
theaccuracyofreal-timeorbit/clockproductsobtainedbythePPP-B2bservice,thefinal
service are utilized to process the satellite’s orbit/clock errors. In order to assess the accu-
prodPurcetcsipsreo ovirdbeidt abnydW cHloUcakr eoaffdsoeptt pedroadsruecfetrse rnecceos.vFeigreudre sb4y atnhde 5coderpreicctttihoenRs MfrSoomf the PPP-B2b
r s a e cGr y vP o iSc f ea rn e ada re lB- Dt u iSm ti-l3e izc oleor dcbk t it oo/f c pflso reotck caen p sds ro o trd hbe uit c set arsrt oe orl bsl.i t t aTe ih’ n se e oadvr bebri yat/g c teh looe cr bP ki Pte PRrrM- o BSr 2 s bo.f I sGn eP r o vSr iad cne ed, r tBt h oDe Sa f-s i3n se a s l s p t r h o e d a u c c c t u s -
proavreidliestded biyn WTaHbleU1 .arAes asdhoowpnte,dth aesa vreerfaegreenRcMesS. oFfiGguPSreosr b4i tasnadre 51 3d.9e5pcicmt, t2h0e.5 R1McmS, of GPS and
racy of real-time orbit/clock products obtained by the PPP-B2b service, the final products
BDaSn-d3 1c9l.o5c7kc mofifnsetth eanradd ioarl,bailto enrgr,oarnsd. Tcrhoess advireercatigoen so,rabnidt RthMatSo foBfD GSP-3S( ManEdO +BIDGSSO-3) are listed in
provided by WHU are adopted as references. Figures 4 and 5 depict the RMS of GPS and
orbits are 10.33 cm, 20.31 cm, and 27.00 cm. The accuracy on the radial component for
Table 1. As shown, the average RMS of GPS orbits are 13.95 cm, 20.51 cm, and 19.57 cm in
BDboSt-h3G cPloScaknd oBffDsSe-t3 aisnhdi gohrebritth aenrrtohreso.t hTehretw aovecormagpeo noernbtsitF RorMsaSte ollift eGcPloSc kaonfdfs eBtsD,tSh-e3 are listed in
the radial, along, and cross directions, and that of BDS-3 (MEO+IGSO) orbits are 10.33 cm,
TaRbMleS 1o.f tAhes GshPoSwclonc,k tohfefs eatviesr3a.2g7en Rs,ManSd othfa GtoPfSB DoSr-b3it(Ms aErOe+ 1IG3.S9O5) camre,1 2.905.n5s1. cUmsu,a allny,d 19.57 cm in
20.o3r1b ictmac,c aunradc y27in.0r0a dcimal.c Tomhep oancecnutsraacnyd oclno ctkhea crcaudraiacyl caoremthpeomneanjotr ffoacrt obrosthaf fGecPtiSn gand BDS-3 is
the radial, along, and cross directions, and that of BDS-3 (MEO+IGSO) orbits are 10.33 cm,
higphoesirt itohnainng tahcec uortahcey.r Ttwhuos ,ctohemppoosintieonntsso Fluotiro snawteilthlithei gchloacckcu oraffcsyectasn, tbheeo RbtMainSe odfb tyhe GPS clock
20.31 cm, and 27.00 cm. The accuracy on the radial component for both GPS and BDS-3 is
usingtheorbit/clockcorrectionsfromthePPP-B2bservice,whichcanalsobeillustratedin
offset is 3.27 ns, and that of BDS-3 (MEO+IGSO) are 1.95 ns. Usually, orbit accuracy in
higher than the other two components For satellite clock offsets, the RMS of the GPS clock
theworks[17–19].
radial components and clock accuracy are the major factors affecting positioning accuracy.
offset is 3.27 ns, and that of BDS-3 (MEO+IGSO) are 1.95 ns. Usually, orbit accuracy in
T r h aTu das iba ,l el t h c1.o eMm peap ons oRi n tMi e oSn not fs so a orbn liutdet ri cro loo nrsc aw kn da it cchlco uchkr ioa gfcfhsye t a aoc rfc erue tar hla-teicm m ye a cparjoo ndr u b fcatesc rt oeocbor tvs ae arien fdf e ebd cy tPb inPyPg -u Bp2s obin ssei grtvi oitch ne.e in o g r b ac it c / u cl r o a c c k y .
corrections from the PPP-B2b service, which can also be illustrated in the works [17–19].
Thus, the position solution with high aOcrcbuitr(acmcy) can be obtained Cblyoc ku(snisn)g the orbit/clock
corrections from the PPP-B2b service, which can also be illustrated in the works [17–19].
RMS-R RMS-A RMS-C RMS
GPS 13.95 20.51 19.57 3.27
BDS-3(MEO+IGSO) 10.33 20.31 27.00 1.95

<!-- PAGE: 9 -->

Remote Sens. 2023, 15, x FOR PEER REVIEW 10 of 22
Remote Sens. 2023, 15, x FOR PEER REVIEW 10 of 22
RemoteSens.2023,15,199 9of20
Figure 4. RMS of GPS clock offset, and orbit errors of real-time products recovered by P PP-B2b
service.
FigFuigreu r4e.4 R.RMMSS ooff GGPPSScl occlkocokff soetf,fasnedt, oarbnidte rorrobrsito ferreraol-rtsim oef prreoadlu-cttismreec opvreoreddubcytsP PrePc-Bo2vbesreerdvi cbey. PPP-B2b
service.
FigFuirgeu r5e. 5R.RMMSS ooff BBDDSS-3-3cl occlkocokff soetffasnedt oarnbidte orrrobrsito efrreraolr-tsim oef prreoadlu-tcitmsreec opvreordedubcytsP rPePc-Bo2vbesreerdv icbey. P PP-B2b
service.
Figure 5. RMS of BDS-3 clock offset and orbit errors of real-time products recovered by PPP-B2b
BasedonthePPP-B2bservice,thepositiondifferencesofBSSDPPPsolutionsinthe
service.
north,east,andverticalwithdifferentGNSSsystemsareshowninFigure6,andthecorre-
Table 1. Mean RMS of orbit errors and clock offset of real-time products recovered by PPP-B2b
spondingRMSarelistedinTable2. AfterintegratingBDS-3andGPS,theimprovements
service.
Table 1. Mean RMS of orbit errors and clock offset of real-time products recovered by PPP-B2b
ofpositionRMSofBSSDBDS-3PPPare3.24%,22.25%,and49.50%inthenorth,east,and
service.
downdirec tions. Suchimprovementsare12.97O%r,b5i0t. 5(0c%m,)a nd62.45%inthreecompoCnleonctks (ns)
forBSSDGPSPPP.Theimprovementsareduetotheimprovedsatellitespatialdistribution,
RMS-R ORrbMitS (-cAm ) RMS-C CloRcMk S(n s)
whichisalsoverifiedinworks[43–46]. Moreover,comparedwithundifferencedPPP,the
GP S R1M3.S95-R R2M0.S51-A R1M9.S57-C R3M.27S
averagepositionRMSimprovedby13.17%,2.64%,and11.21%inthreecomponents,which
BdDueS-to3 t(hMGeErPeOSce +ivIGerS-rOel)a tederror11s03,..c39a35n beeliminat22e00d..35b11y theBSSDm21o79d..05e0l7. 13..9257
BDS-3 (MEO+IGSO) 10.33 20.31 27.00 1.95
Based on the PPP-B2b service, the position differences of BSSD PPP solutions in the
northB, aesaesdt, oann dth vee PrtPicPa-lB w2bit hse drvififceer,e tnhte G pNoSsiSti soyns tdeimffesr aernec eshs oowf BnS iSnD F iPgPuPre s 6o,l uatniodn tsh ein c tohre-
rneosrptohn, deainstg, RanMdS v aerret ilciastle wd iitnh Tdaifbfleer 2en. At GfteNrS inS tseygsrtaetminsg aBrDe Ssh-3o awnnd iGn PFSig, tuhree i6m, panrodv tehme ecnotrs-
oref sppoosnitdioinng R RMMSS o afr Be SliSsDte dB DinS T-3a bPlPeP 2 .a Aref t3e.r2 4in%te, g2r2a.2ti5n%g ,B aDnSd- 439 a.n50d% G iPnS t, hthe en iomrtphr,o evaesmt, eanntds
doof wpons ditiiroenc tRioMnSs. oSfu BchSS iDm pBrDoSv-e3m PePnPts a arree 3 1.224.9%7%, 2,2 5.02.55%0%, a, nadn d4 96.25.04%5% in in th the rneoer ctohm, epaostn, eanntds
fdoorw BnS dSiDre cGtioPnSs .P SPuPch. iTmhper oivmepmroenvtesm aeren t1s2 .9a7re% ,d 5u0e.5 0t%o , athned 6im2.4p5r%ov iend t hsraetee clloitme psopnaetniatsl
for BSSD GPS PPP. The improvements are due to the improved satellite spatial

<!-- PAGE: 10 -->

Remote Sens. 2023, 15, x FOR PEER REVIEW 11 of 22
Remote Sens. 2023, 15, x FOR PEER REVIEW 11 of 22
distribution, which is also verified in works [43–46]. Moreover, compared with undiffer-
distribution, which is also verified in works [43–46]. Moreover, compared with undiffer-
enced PPP, the average position RMS improved by 13.17%, 2.64%, and 11.21% in three
enced PPP, the average position RMS improved by 13.17%, 2.64%, and 11.21% in three
components, which due to the receiver-related errors, can be eliminated by the BSSD
RemoteSens.2023,15,199 components, which due to the receiver-related errors, can be eliminated by the1 0BoSfS2D0
model.
model.
Figure 6. Positioning errors of undifferenced PPP (left) and BSSD PPP (right) with different GNSS.
Figure 6. Positioning errors of undifferenced PPP (left) and BSSD PPP (right) with different GNSS.
Figure6.PositioningerrorsofundifferencedPPP(left)andBSSDPPP(right)withdifferentGNSS.
Table 2. Positioning errors of undifferenced PPP and BSSD PPP with different GNSS.
Table 2. Positioning errors of undifferenced PPP and BSSD PPP with different GNSS.
Table2.PositioningerrorsofundifferencedPPPandBSSDPPPwithdifferentGNSS.
BSSD PPP Undifferenced PPP
BSSD PPP Undifferenced PPP
BSSDPPP UndNifofretrhe ncedPPP Down
North Down
North (cm) East (cm) Down (cm) East (cm)
North (cm) East (cm) Down (cm) East (cm)
North(cm) East(cm) Down(cm) North(cm) (cEmas)t (cm) Dow(ncm(c)m )
(cm) (cm)
GPS 69.68 GP G S P S 75.25 69 6 .6 9 8 .6 8 218.1875 7 .2 5 5 .2 5 952.162 851 .1 8 8 .1 8 95 9 .675 56.6 .753 76 7 .7 6 3 .7 3 221182.871 .77 8 7 .7 7
BDS-3 62.67 BDS-3 47.91 62.67 162.2347.91 631.6829.23 63.8499 .97 49.97 11886.60.707
BDS-3 62.67 47.91 162.23 63.89 49.97 186.07
BDS-3/GPS 60.64 37.25 81.93 62.73 38.05 103.12
BDS-3/GPS 60.64 37.25 81.93 62.73 38.05 103.12
BDS-3/GPS 60.64 37.25 81.93 62.73 38.05 103.12
3.33..3 P.ePrfeorrfomrmanacnec oef oBfSBSSDSD PPPPP/PIN/INS STCTIC I
3.3. Performance of BSSD PPP/INS TCI
InI ncocmompapraisroisno nwwithit hBSBSSDSD PPPPP,P p,opsoistiiotino nererrorrosr scacna nbeb ererdeudcuecde dvivsiisbilbyl ybyb ythteh aedaddidtiiotino n
In comparison with BSSD PPP, position errors can be reduced visibly by the addition
ofo IfNINS Sini nalal ltlhtrheree ecocmompopnoennetnst (ss(hsohwown nini nFiFgiugruer e7)7. )T.hTeh aevaevreargaeg iemimprporvoevmemenetnst psrporvoivdiedde d
of INS in all three components (shown in Figure 7). The average improvements provided
byb yBSBSSDSD PPPPP/PIN/ISN TSCTIC aIrea r3e13.214.2%4,% 2,32.335.3%5,% a,nadn 2d72.378.3%8 %in itnhteh tehtrheere deidreirceticotniosn (sT(aTbalbel 3e)3. ).
by BSSD PPP/INS TCI are 31.24%, 23.35%, and 27.38% in the three directions (Table 3).
FiFgiugruer 7e. 7P.oPsoitsiiotnioinnign egrerorrrosr osfo BfSBSSDS DPPPPP/PIN/ISN TSCTI CwIiwthi tdhifdfeifrfeenret nGtNGSNSS. S.
Figure 7. Positioning errors of BSSD PPP/INS TCI with different GNSS.
Table3.PositionRMSofBSSDPPPandBSSDPPP/INSTCIwithdifferentGNSS.
Table 3. Position RMS of BSSD PPP and BSSD PPP/INS TCI with different GNSS.
Table 3. Position RMS of BSSD PPP and BSSD PPP/INS TCI with different GNSS.
BSSDPPP/INSTCI
BSSD PPP/INS TCI
BSSD PPP/INS TCI
NoNrthor (thcm(c)m ) EastE (acsmt()c m) DoDwonw (ncm(c)m )
North (cm) East (cm) Down (cm)
GPGSP S 55.0556. 06 60.5600 .50 2032.0534. 54
GPS 55.06 60.50 203.54
BDS-3 42.69 34.48 119.96
BDS-3 42.69 34.48 119.96
BDS-3 42.69 34.48 119.96
BDS-3/GPS 35.87 28.90 41.49
BDS-3/GPS 35.87 28.90 41.49
BDS-3/GPS 35.87 28.90 41.49
Figure8showsthepositiondifferencesbetweenBSSDPPPandBSSDPPP/INSTCI.
Significantly,theaccuracyofPPPissimilartothatofPPP/INSTCIwhentherearesufficient
satellites. ThatisbecausetheabsolutepositionaccuracymainlydependsonPPP.However,
suchdifferencesaresignificantduringtheperiodswithfrequentGNSSoutages,primarily
fromthe1500sto2500sand6500sto7500s. ThatisbecausePPP/INSTCIcanstillprovide
high-accuracypositionresultswhenthenumberofsatellitesislessthan4,evenifthereis

<!-- PAGE: 11 -->

Remote Sens. 2023, 15, x FOR PEER REVIEW 12 of 22
Rem ote Sens. 2023, 15, x FOR PEER REVIEW 12 of 22
Figure 8 shows the position differences between BSSD PPP and BSSD PPP/INS TCI.
Figure 8 shows the position differences between BSSD PPP and BSSD PPP/INS TCI.
Significantly, the accuracy of PPP is similar to that of PPP/INS TCI when there are suffi-
Significantly, the accuracy of PPP is similar to that of PPP/INS TCI when there are suffi-
cient satellites. That is because the absolute position accuracy mainly depends on PPP.
cient satellites. That is because the absolute position accuracy mainly depends on PPP.
However, such differences are significant during the periods with frequent GNSS outages,
However, such differences are significant during the periods with frequent GNSS outages,
primarily from the 1500 s to 2500 s and 6500 s to 7500 s. That is because PPP/INS TCI can
RemoteSens.2023,15,199 primarily from the 1500 s to 2500 s and 6500 s to 7500 s. That is because PPP/INS TCI1 c1aonf2 0
still provide high-accuracy position results when the number of satellites is less than 4,
still provide high-accuracy position results when the number of satellites is less than 4,
even if there is no available satellite in short-term time. The frequent GNSS outages be-
even if there is no available satellite in short-term time. The frequent GNSS outages be-
tween the 1500 s and 2500 s are displayed in Figure 9, from which we can see about ten
twneoenav tahiela 1b5l0e0s ast aenlldit e2i5n00s hso arrt-et edrimspltaimyeed. Tinh eFifgreuqreu e9n, tfrGoNmS wShoiuctha gwees cbaentw seeee nabthoeut1 5te0n0 s
partial and complete outages with the time last 1 s to 32 s happened. The details about the
paarntidal2 a5n00d scoarmepdliestpel aoyuetdagiensF wigiuthre th9e, ftriomme wlahsti c1h sw toe 3c2a ns hseaepapbeonuetdt.e Tnhpea drteitaalialsn adbcooumt tphleet e
outage time and the average number of available satellites during these periods are listed
ouotuatgaeg teismwe iatnhdt htheet iamveerlaagset n1usmtobe3r2 osf ahvaapiplaebnleed s.atTehlleitedse dtauilrsinagb tohuetsteh peeoriuotdasg eartei mliseteadn d
in Table 4. As is shown, the maximum outage time for BDS-3, GPS, and BDS-3+GPS are 28
int hTeabalve e4r.a Ages ins usmhobwern,o tfhaev maialaxbimleusmat eolulittaegsed tuimrien gfotrh BeDseS-p3e, rGioPdSs, aanredl BisDteSd-3i+nGTPaSb laere4 .28A s
s, 32 s, and 26 s, respectively. During these periods, although a few satellites are still avail-
s, i3s2s sh,o awndn ,2t6h se, mreaspxiemctuivmelyo.u Dtaugreintgim theefsoer pBeDriSo-d3s,,G aPltSh,oaungdh Ba DfeSw-3 s+aGtePllSitaesre ar2e8 sst,il3l 2avs,aailn-d
able, the number does not meet the minimum requirement of positioning both for single
ab2l6e, st,hree snpuemctbivere ldy.oeDsu nroint gmteheets tehep emriiondims,uamlth roeuqguhireamfeewnt soaft pelolistietisoanriengst biloltahv faoilra sbilneg,lteh e
and dual systems PPP calculation. However, these available satellites can be used in BSSD
anndu dmubaelr sdysoteesmnso PtPmPe ceatltchuelamtiionnim. Huomwreevqeur,i rtehmeseen atvoafilpaobsliet isoanteinllgitebso cthanf obres uinsegdle inan BdSSdDua l
PPP/INS TCI mode. The corresponding position differences of PPP and PPP/INS TCI dur-
PPsyPs/ItNemSs TPCPIP mcoadlceu. lTathieo nc.oHrreoswpeovnedr,inthge pseosaivtiaoinla dblieffesaretenlclietse sofc aPnPbPe aunsde PdPinP/BINSSSD TPCPI Pd/uIrN-S
ing the 1500 s to 2500 s are shown in Figure 10. Visibly, BSSD PPP cannot provide position
inTgC thIem 1o5d00e. sT toh e25c0o0r rse aspreo snhdoinwgnp ino sFiitgiounred 1if0f.e Vreinsicbelsy,o BfSPSPDP PaPnPd cPaPnPn/oItN pSroTvCidIed puorsinitgiotnh e
results, but BSSD PPP/INS TCI can work in partial outage periods. The divergence of po-
re1s5u0lt0s,s btout2 B50S0SDs aPrPePsh/IoNwSn TiCnIF ciagnu rweo1r0k. Vini spibalryt,iaBlS oSuDtaPgPeP pcearinondost. pTrhoev didiveeprogseinticoen orfe psuol-ts,
sition error can also be restrained in short-term outages. The average maximum drifts of
sitbiount BeSrrSoDr cPaPnP a/lIsNo SbeT rCeIstcraaninwedo rikn isnhopratr-tteiarlmo uotuatgaegepse. rTiohde sa.vTehraegdei vmearxgiemnucemo dfrpioftssi toiof n
position decreased from 107.96 cm, 59.90 cm, and 78.22 cm to 88.52 cm, 54.54 cm, and
poesrirtoiornca dneaclrseoabseedr efsrtormain 1e0d7i.9n6s hcomr,t -5te9r.m90 ocumta, gaensd. T7h8e.2a2v ecrmag teo m88a.x5i2m cumm, d5r4i.f5ts4 ocfmp,o asintido n
62.00cm after integrating with INS. Therefore, PPP/INS TCI can provide the position re-
decreasedfrom107.96cm,59.90cm,and78.22cmto88.52cm,54.54cm,and62.00cmafter
62.00cm after integrating with INS. Therefore, PPP/INS TCI can provide the position re-
sult with better continuity and accuracy. Nevertheless, in cases where the duration of
integratingwithINS.Therefore,PPP/INSTCIcanprovidethepositionresultwithbetter
sult with better continuity and accuracy. Nevertheless, in cases where the duration of
complete outages is too long, such as outages 7 and 8, a divergence of the position results
continuityandaccuracy. Nevertheless,incaseswherethedurationofcompleteoutages
complete outages is too long, such as outages 7 and 8, a divergence of the position results
still can be found because INS would drift rapidly along with time.
istoolong,suchasoutages7and8,adivergenceofthepositionresultsstillcanbefound
still can be found because INS would drift rapidly along with time.
becauseINSwoulddriftrapidlyalongwithtime.
Figure 8. Positioning differences between BSSD PPP and BSSD PPP/INS TCI with different GNSS.
FiFgiugruer 8e. 8P.oPsoitsiiotnioinngin dgidffiefrfeernecnecse bsebtwetweeene nBSBSSDS DPPPPP Panadn dBSBSSDS DPPPPP/PIN/ISN TSCTIC wIiwthi tdhifdfeifrfeenret nGtNGSNSS. S.
FFiigguurree 99.. SSaatteelllliittee nnuummbbeerrss aanndd oouuttaaggeess ttiimmee bbeettwweeeenn tthhee 11550000 ss aanndd 22550000 ss..
Figure 9. Satellite numbers and outages time between the 1500 s and 2500 s.
Table4.ThenumberofavailablesatellitesandtheGNSSoutagestime.
OutagesScenes 1 2 3 4 5 6 7 8 9 10
GPS 16 4 2 9 14 3 32 26 8 1
Outagestime(s) BDS-3 19 1 2 7 11 2 28 22 3 1
GPS/BDS-3 17 1 2 6 11 2 26 22 2 1
GPS 0.6 2.3 0.5 1.4 0.9 1 0.4 0.3 1.3 3
Satellitenumber BDS-3 0.3 2 1.5 1.3 0.9 0.5 0.2 2.4 1.7 1
GPS/BDS-3 0.5 4 2 2.5 1.2 0.5 0.5 2.5 1.5 4

<!-- PAGE: 12 -->

Remote Sens. 2023, 15, x FOR PEER REVIEW 13 of 22
Table 4. The number of available satellites and the GNSS outages time.
Outages Scenes 1 2 3 4 5 6 7 8 9 10
GPS 16 4 2 9 14 3 32 26 8 1
Outages
BDS-3 19 1 2 7 11 2 28 22 3 1
time(s)
GPS/BDS-3 17 1 2 6 11 2 26 22 2 1
GPS 0.6 2.3 0.5 1.4 0.9 1 0.4 0.3 1.3 3
Satellite
BDS-3 0.3 2 1.5 1.3 0.9 0.5 0.2 2.4 1.7 1
number
RemoteSens.2023,15,1G9P9S/BDS-3 0.5 4 2 2.5 1.2 0.5 0.5 2.5 1.5 124o f20
FFigiguurere1 100..P Poosistiitoionniningge errrororsrso offB BSSSSDDP PPPPP( l(elfetf)t)a nadndB SBSSDSDP PPPP/PI/INNSST TCCII( r(rigighht)t)b beetwtweeeennt hthee1 1550000s s
aanndd2 2550000s .s.
3.4. BSSDPPP/INS/ODOTCIPositioning
3.4. BSSD PPP/INS/ODO TCI Positioning
Inthecaseofacompleteoutageforalongtime,positionerrorsofPPP/INSTCIcould
In the case of a complete outage for a long time, position errors of PPP/INS TCI could
accumulaterapidly.Therefore,constraintinformationishelpful.Anodometercanmeasure
accumulate rapidly. Therefore, constraint information is helpful. An odometer can meas-
the forward velocity of the vehicle. Based on such velocity and motion constraints, the
ure the forward velocity of the vehicle. Based on such velocity and motion constraints, the
problem above can be restrained by Equation (23). Figure 11 depicts the position errors
problem above can be restrained by Equation (23). Figure 11 depicts the position errors of
of BSSD PPP/INS/ODO TCI with different GNSS, and the corresponding RMS for the
BSSD PPP/INS/ODO TCI with different GNSS, and the corresponding RMS for the com-
commonperiodswithBSSDPPP/INSTCIarecalculatedinTable5.Accordingly,theposition
mon periods with BSSD PPP/INS TCI are calculated in Table 5. Accordingly, the position
improvementscausedbytheadditionofanodometeronaverageare1.34%,1.41%,and1.73%.
improvements caused by the addition of an odometer on average are 1.34%, 1.41%, and
SuchinvisibleenhancementsarebecausetheimpactoftheodometeronPPP/INSintegration
1.73%. Such invisible enhancements are because the impact of the odometer on PPP/INS
mainlyaffectstheseperiodswithpoororwithoutGNSSobservability.Whilethereareenough
integration mainly affects these periods with poor or without GNSS observability. While
satellites,theweightoftheodometerobservationfunctionismuchsmallerthanthatofGNSS
there are enough satellites, the weight of the odometer observation function is much
observationswhichcanbeobtainedbymakingacomparisonbetweenEquations(14)and(23).
smaller than that of GNSS observations which can be obtained by making a comparison
ThecorrespondingpositiondifferencesbetweenBSSDPPP/INSTCIandPPP/INS/ODO
between Equations (14) and (23). The corresponding position differences between BSSD
TCIareplottedinFigure12. Significantly,theperiodswithsufficientsatelliteshavesmall
PPP/INS TCI and PPP/INS/ODO TCI are plotted in Figure 12. Significantly, the periods
differences,andsignificantdifferencesemergealongwithlong-termoutages.Figure13depicts
with sufficient satellites have small differences, and significant differences emerge along
thepositiondifferenceofBSSDPPP/INS/ODOTCIfrom1500sto2500s.Accordingly,the
with long-term outages. Figure 13 depicts the position difference of BSSD PPP/INS/ODO
averagepositionRMSsfrom1500sto2500sisreducedfrom50.00cm,27.08cm,and37.42cm
TCI from 1500 s to 2500 s. Accordingly, the average position RMSs from 1500 s to 2500 s
to44.40cm,26.85cm,and34.96cm.Theaverageofmaximumpositioningdriftswithdifferent
is reduced from 50.00 cm, 27.08 cm, and 37.42 cm to 44.40 cm, 26.85 cm, and 34.96 cm. The
GNSSduringasatelliteoutageareplottedinFigure14.Theaveragesofmaximumpositioning
average of maximum positioning drifts with different GNSS during a satellite outage are
driftsarereducedfrom88.52cm,54.54cm,and62.00cmto66.29cm,45.84cm,and49.17cm,
plotted in Figure 14. The averages of maximum positioning drifts are reduced from 88.52
Remote Sens. 2023, 15, x FOR PEER REVwIEitWh amaximumdiminutionof74.94%,33.0%,and51.56%.Hence,thepositionperfo14r mofa n22c e
cm, 54.54 cm, and 62.00 cm to 66.29 cm, 45.84 cm, and 49.17 cm, with a maximum diminu-
ofBSSDPPP/INSTCIcanbefurtherenhanced,especiallyinchallengingenvironments,by
tion of 74.94%, 33.0%, and 51.56%. Hence, the position performance of BSSD PPP/INS TCI
usinganodometer.
can be further enhanced, especially in challenging environments, by using an odometer.
FiFgiugurer e111.1 P.oPsiotsioitnioinngin egrreorrrso rosf oBfSSBDSS PDPPP/PINP/SI/NOSD/OO TDCOI wTCitIh wdiitfhferdeinffte GreNntSSG NbyS Susbinygu PsiPnPg-BP2PbP -
coBr2rbecctoiornresc. tions.
Table 5. Position RMS of BSSD PPP/INS/ODO TCI with different GNSS.
BSSD PPP/INS/ODO TCI Undifferenced PPP/INS/ODO
North (cm) East (cm) Down (cm) North (cm) East (cm) Down (cm)
GPS 55.23 60.29 202.20 55.69 61.92 207.96
BDS-3 41.78 33.47 113.43 44.50 34.38 108.16
GPS/BDS-3 35.02 28.63 40.86 42.90 29.98 41.33
Figure 12. Positioning differences between BSSD PPP/INS TCI and BSSD PPP/INS/ODO TCI with
different GNSS.
Figure 13. Positioning errors of BSSD PPP/INS/ODO TCI with frequent GNSS outages.

<!-- PAGE: 13 -->

Remote Sens. 2023, 15, x FOR PEER REVIEW 14 of 22
Remote Sens. 2023, 15, x FOR PEER REVIEW 14 of 22
Figure 11. Positioning errors of BSSD PPP/INS/ODO TCI with different GNSS by using PPP-B2b
RemoteSens.2023,15,199 13of20
Ficgourrree c1t1io. nPso. sitioning errors of BSSD PPP/INS/ODO TCI with different GNSS by using PPP-B2b
corrections.
Table 5. Position RMS of BSSD PPP/INS/ODO TCI with different GNSS.
Table5.PositionRMSofBSSDPPP/INS/ODOTCIwithdifferentGNSS.
Table 5. Position RMS of BSSD PPP/INS/ODO TCI with different GNSS.
BSSD PPP/INS/ODO TCI Undifferenced PPP/INS/ODO
BSSD P PP/INSN/OoDBrtOShS T(DcCm IP)P PE/aIsNt S(c/OmD) OD ToCwIn (cm)U nNUdoinfrftdehri ef(fncecmreed)n PcPEePda/s IPtN P(ScPm//OI)ND OSD/OowDnO (cm)
North(cm) G PSE astN(cmor)th55 (.c2m3 ) DEoawsnt6 (0(cc.mm29)) Dow2Nn0o 2(rc.t2hm0( )c mN)orth55 (.c6m9E )a stE(camst)6 (1c.m92) DDooww2nn0 7((cc.9mm6) )
GBPDSS -3 554.213.7 8 603.239.4 7 20121.230.4 3 554.649.5 0 613.942.3 8 20170.986.1 6
GPS 55.23 60.29 202.20 55.69 61.92 207.96
BDS-3 41.78 GBPDSS/B-3D S3-33. 47 413.758.0 2 131332..44837.6 3 1134.044.384 6.5 0 444.520.9 0 34.38342.398.9 8 1100848..111.663 3
GPS/BDS-3 35.02 GPS/BDS-32 8.63 35.02 4208.8.663 40.8642 .90 42.90 29.9829.98 4411..3333
Figure 12. Positioning differences between BSSD PPP/INS TCI and BSSD PPP/INS/ODO TCI with
Figure12.PositioningdifferencesbetweenBSSDPPP/INSTCIandBSSDPPP/INS/ODOTCIwith
Fidguifrfeer 1e2n.t PGoNsiStiSo.n ing differences between BSSD PPP/INS TCI and BSSD PPP/INS/ODO TCI with
differentGNSS.
different GNSS.
Remote Sens. 2023, 15, x FOR PEER REVIEW 15 of 22
FFiigguurree 1133.. PPoossiittiioonniinngg eerrrroorrss ooff BBSSSSDD PPPPPP//ININSS/O/ODDOO TCTIC wI withit hfrefrqeuqeunetn GtGNNSSS Souotuatgaegse. s.
Figure 13. Positioning errors of BSSD PPP/INS/ODO TCI with frequent GNSS outages.
Figure 14. Average maximum position drifts of different GNSS for BSSD PPP/INS TCI (left) and
Figure14. AveragemaximumpositiondriftsofdifferentGNSSforBSSDPPP/INSTCI(left)and
PPP/INS/ODO TCI (right) on different GNSS outage scenes.
PPP/INS/ODOTCI(right)ondifferentGNSSoutagescenes.
In addition, to analyze the impact of the BSSD model on PPP/INS integration, the
Inaddition,toanalyzetheimpactoftheBSSDmodelonPPP/INSintegration,the
timtimeese sreiersieosf opfo psiotsioitnioenr reorrrsoorsf uonf duinffdeirfefnecreendcPePdP P/PINP/SI/NOSD/OODTOC TIiCsIs hiso swhnowinnF iing uFrieg1u5r.e I1n5.
coInnt craosntt,rtahset,B tShSeD BmSSoDd emlpordoevli dperdovaibdoeudt a7b.7o1u%t ,73..7019%%,, 3a.n0d9%0.,2 a7n%di n0.t2h7e%th irne ethdei rtehcrteioen dsiorenc-
avtieornasg eo,na cacvoerrdaigneg, taoccRoMrdSisnlgis ttoed RiMnTSas blilset5e.dI tinc aTnabbeles 5e.e nIt tchaant tbhee speoesni ttihoanta tchceu rpaocsyitoiofnth aec-
BScuSDracmyo odfe lt-hbea sBeSdSiDn tmegordateilo-nbamseodd einitsecglroasteioton tmheoduen disif fcelroesnec teod tmheo duenl-dbiaffseerdenincetedg rmatoiodnel-
based integration in the time series in general but is slightly higher in position statistics.
It is due to the reason that the BSSD model can remove the receiver-depended errors (i.e.,
receiver clock offset, receiver time delays on pseudorange and carrier-phase, unmodelled
receiver errors, etc.) that impact initial convergence or re-convergence of PPP after satellite
signal outages. Such a character is illustrated in Figure 16, which depicts the differences
between the BSSD-based solutions and the undifferenced PPP-based solutions. The visible
differences emerge during the periods of re-convergence caused by satellite outages,
while the differences are invisible in periods with sufficient available satellites. Figure 17
shows the average maximum positioning drifts calculated by the odometer-aided
PPP/INS TCI based on the BSSD model and the undifferenced PPP model in the satellite
outage periods from 1500 s to 2500 s. The position drifts of the solutions based on the BSSD
model are 66.29 cm, 45.84 cm, and 49.17 cm, which are smaller than those solutions based
on the undifferenced model (82.38cm, 50.66 cm, and 52.30 cm). It means that the BSSD
model can provide visible enhancements in demanding user environments.
Figure 15. Positioning errors of undifferenced BSSD PPP/INS/ODO TCI with different GNSS using
PPP-B2b correction.

<!-- PAGE: 14 -->

Remote Sens. 2023, 15, x FOR PEER REVIEW 15 of 22
Figure 14. Average maximum position drifts of different GNSS for BSSD PPP/INS TCI (left) and
PPP/INS/ODO TCI (right) on different GNSS outage scenes.
In addition, to analyze the impact of the BSSD model on PPP/INS integration, the
time series of position errors of undifferenced PPP/INS/ODO TCI is shown in Figure 15.
RemoteSens.2023,15,199 In contrast, the BSSD model provided about 7.71%, 3.09%, and 0.27% in the three direc-14of20
tions on average, according to RMSs listed in Table 5. It can be seen that the position ac-
curacy of the BSSD model-based integration mode is close to the undifferenced model-
based integration in the time series in general but is slightly higher in position statistics.
in the time series in general but is slightly higher in position statistics. It is due to the
It is due to the reason that the BSSD model can remove the receiver-depended errors (i.e.,
reasonthattheBSSDmodelcanremovethereceiver-dependederrors(i.e.,receiverclock
receiver clock offset, receiver time delays on pseudorange and carrier-phase, unmodelled
offset,receivertimedelaysonpseudorangeandcarrier-phase,unmodelledreceivererrors,
receiver errors, etc.) that impact initial convergence or re-convergence of PPP after satellite
etc.) thatimpactinitialconvergenceorre-convergenceofPPPaftersatellitesignaloutages.
signal outages. Such a character is illustrated in Figure 16, which depicts the differences
SuchacharacterisillustratedinFigure16,whichdepictsthedifferencesbetweentheBSSD-
between the BSSD-based solutions and the undifferenced PPP-based solutions. The visible
basedsolutionsandtheundifferencedPPP-basedsolutions. Thevisibledifferencesemerge
differences emerge during the periods of re-convergence caused by satellite outages,
during the periods of re-convergence caused by satellite outages, while the differences
while the differences are invisible in periods with sufficient available satellites. Figure 17
areinvisibleinperiodswithsufficientavailablesatellites. Figure17showstheaverage
shows the average maximum positioning drifts calculated by the odometer-aided
maximumpositioningdriftscalculatedbytheodometer-aidedPPP/INSTCIbasedonthe
PPP/INS TCI based on the BSSD model and the undifferenced PPP model in the satellite
BSSDmodelandtheundifferencedPPPmodelinthesatelliteoutageperiodsfrom1500sto
outage periods from 1500 s to 2500 s. The position drifts of the solutions based on the BSSD
2500s. ThepositiondriftsofthesolutionsbasedontheBSSDmodelare66.29cm,45.84cm,
model are 66.29 cm, 45.84 cm, and 49.17 cm, which are smaller than those solutions based
and49.17cm,whicharesmallerthanthosesolutionsbasedontheundifferencedmodel
on the undifferenced model (82.38cm, 50.66 cm, and 52.30 cm). It means that the BSSD
(82.38 cm, 50.66 cm, and 52.30 cm). It means that the BSSD model can provide visible
model can provide visible enhancements in demanding user environments.
enhancementsindemandinguserenvironments.
Remote Sens. 2023, 15, x FOR PEER REVIEW 16 of 22
Remote Sens. 2023, 15, x FOR PEER REFViFIgEiuWgrue r 1e51. 5P.oPsiotisoitniionngi negrreorrrso orfs uonfduinffderifefnecreendc BeSdSBDS PSPDPP/IPNPS//OINDSO/ OTCDIO wTitChI dwififtehredni1tf 6fG eorNfe Sn2S2t GusNinSgS using
PPP-B2b correction.
PPP-B2bcorrection.
FFiiF ggu iug rre ue r 1 e166. .1 P 6Po . soistiiotiP noi onn signi tgd io idf n fie ifn rfeeg nrcee dnsci feb fse e t rbw een etewc n ee s uenn b d eui t fnf w edr eiefefnen creed un ncPed PdP i f /Pf I e NPrPS e / n/OIcND eSd O/O T PDC POI P a /Tn ICd N IB SaS /nS O Dd D BP OSPSPD/ T IN CPSPI Pa/InNdS BSSD
T T C C I I / / O O D D O O . .
PPP/INSTCI/ODO.
FiFguigreu r1e7. 1M7.eaMn meaanximmuamxi mpousmitiopno dsriitfitos nofd driiffftesreonft GdiNffSeSr efonrt BGSNSDS SPP fPo/rINBSS/SODDOP PTPC/I IaNndS /uOn-DOTCIand
d F i iuf g fne u rdr e einf cf1ee 7 dr.e P MnPce Pead/ n IN Pm SP/ aPO x/D imIONu TSm C/ OI p . oDsOitioTnC dI.rifts of different GNSS for BSSD PPP/INS/ODO TCI and un-
differenced PPP/INS/ODO TCI.
3.5. BSSD PPP/INS/ODO TCI Attitude Determination
The attitude errors of BSSD PPP/INS TCI with and without odometer aid are shown
3.5. BSSD PPP/INS/ODO TCI Attitude Determination
in Figure 18. The results of the roll, pitch, and heading angles in the first 500 s are signifi-
The attitude errors of BSSD PPP/INS TCI with and without odometer aid are shown
cantly different from the results in other periods. That is because the vehicle kept static in
in Figure 18. The results of the roll, pitch, and heading angles in the first 500 s are signifi-
the first 500 s, which provided no observabilities for gyroscopes. Then, the accuracy of
cantly different from the results in other periods. That is because the vehicle kept static in
attitude determination during these times mainly depended on the accuracy of initial at-
ttihtued feisr.s tW 5h0i0le s t,h we hveichhic lper movoivdeedd anhoe aodb, stherev maboitliiotiness infocrr egayserdo stchoep oebss. eTrvhaebni,l itthiees aocf cguyr-acy of
raotstcitoupdees adnedte urpmgirnaadteiodn th deu arcicnugr atchye soef atitmtiteusd mes.a Ainclcyo rddeipnegn tdo ethde o snta tthiseti casc icnu Traacbyle o 6f, itnhiet ial at-
atviteurdagese. R WMhSisl eo ft BhSeS vDe hPiPcPle/I NmSo TveCdI aarhe e0a.0d2,5 t°h, e0 .m04o9t°i,o annsd i n0.c1r8e4a°s eidn rtohlel, opbitscehr, vaanbdi lhietiaeds- of gy-
irnogs caonpgeless a, nreds puepcgtirvaedlye.d V tihseib alyc,c uthrea cayc coufr aatctiietsu odfe sro. All cacnodr dpiintcgh taon tghlee ss taartei smtiocsr ei np Treacbislee 6, the
° ° °
tahvaenr hageaed RinMgS asn ogfl eBsS bSeDca PuPseP o/IfN thSe T pCoIo ar roeb 0s.e0r2v5ab,i l0it.y0 4o9f h,e aanddin 0g. 1a8n4gle sin m reoalls,u prietdc hb,y a tnhde head-
ginyrgo ascnogplee si,n r tehsep veecrtitviceally d. iVreicstiibolny ,[ 4t3h]e. Fauccrtuhrearcmieosr eo,f a rtotiltlu adne dR MpiStcsh c aalncugllaetse da rues mingo rdei fp-recise
ftehraennt h GeNadSiSn agr ae ncglolsees tboe ecaacuhs eo tohfe trh. eT hpaoto irs obebcsaeurvsea bthilei tayt toitfu hdeeasd airneg m aanjogrlleys dmeetearsmuirneedd b y the
bgyy trhoes cgoyproes icno pthee a nvder atircea sll idgihretlcyt iaofnfe c[4te3d]. b Fyu GrtNheSrSm poosreit,i oanttiintgu dacec RurMacSys wcahlicleu lGaNteSdS u osbin-g dif-
servations are available [28]. Therefore, the attitude solutions obtained by using different
ferent GNSS are close to each other. That is because the attitudes are majorly determined
GNSS systems are somewhat different in accuracy.
by the gyroscope and are slightly affected by GNSS positioning accuracy while GNSS ob-
servations are available [28]. Therefore, the attitude solutions obtained by using different
GNSS systems are somewhat different in accuracy.

<!-- PAGE: 15 -->

RemoteSens.2023,15,199 15of20
3.5. BSSDPPP/INS/ODOTCIAttitudeDetermination
TheattitudeerrorsofBSSDPPP/INSTCIwithandwithoutodometeraidareshownin
Figure18. Theresultsoftheroll,pitch,andheadinganglesinthefirst500saresignificantly
differentfromtheresultsinotherperiods. Thatisbecausethevehiclekeptstaticinthe
first500s,whichprovidednoobservabilitiesforgyroscopes. Then,theaccuracyofattitude
determination during these times mainly depended on the accuracy of initial attitudes.
Whilethevehiclemovedahead,themotionsincreasedtheobservabilitiesofgyroscopes
andupgradedtheaccuracyofattitudes. AccordingtothestatisticsinTable6,theaverage
RMSsofBSSDPPP/INSTCIare0.025◦,0.049◦,and0.184◦inroll,pitch,andheadingangles,
respectively. Visibly,theaccuraciesofrollandpitchanglesaremoreprecisethanheading
anglesbecauseofthepoorobservabilityofheadinganglesmeasuredbythegyroscopein
theverticaldirection[43]. Furthermore,attitudeRMSscalculatedusingdifferentGNSSare
closetoeachother. Thatisbecausetheattitudesaremajorlydeterminedbythegyroscope
Remote Sens. 2023, 15, x FOR PEER aRnEVdIEaWre slightly affected by GNSS positioning accuracy while GNSS observation1s7 aorfe 22
available[28]. Therefore,theattitudesolutionsobtainedbyusingdifferentGNSSsystems
aresomewhatdifferentinaccuracy.
FiFgiugruer1e8 1.8A. tAtitttuitduedeer reorrrsorosf oBfS SBDSSPDP PPP/PIN/ISNTS CTIC(lIe (flte)fat)n danBdS SBDSSPDP PP/PIPN/ISN/SO/ODDOOT CTCI(Ir i(grihgth)tw) iwthith
different GNSS.
differentGNSS.
TaTbalebl6e. 6A. tAtitttuitduedReM RMSoSf oBfS BSSDSDPP PPP/PIN/INSST CTCIwI withitha nadndw withitohuotuot doodmometeetrear iadi.d.
BSSD PPP/INS TCI BSSD PPP/INS/ODO TCI
BSSDPPP/INSTCI BSSDPPP/INS/ODOTCI
° ° ° ° ° °
Roll(◦) Pitch(◦) Roll ( ) H ead P i i n tc g h ( ◦( ) ) Hea R d o i l n l( g◦ ) ( ) Roll ( Pi ) t ch P (◦it ) ch ( ) He H ad e i a n d g in (◦g ) ( )
GPS 0.025 0.050 0.178 0.025 0.049 0.137
GPS 0.025 0.050 0.178 0.025 0.049 0.137
BDS-3 0.027 0.049 0.194 0.028 0.048 0.140
BDS-3 0.027 0.049 0.194 0.028 0.048 0.140
GPS/BDS-3 0.024 GPS/BD0S.-034 8 0.024 0.1081.048 00.1.08215 0.025 0.0480.048 0.103.8138
According to the RMSs of BSSD PPP/INS/ODO TCI listed in Table 6, the average
AccordingtotheRMSsofBSSDPPP/INS/ODOT°CIlisted°inTable6,th°eaverageRMSs
RMSs of roll, pitch, and heading angles are 0.026 , 0.048 , and 0.138 . In contrast, the
ofroll,pitch,andheadinganglesare0.026◦,0.048◦,and0.138◦. Incontrast,theodometer
odometer provides about 25.00% in heading angle and invisible enhancements in roll and
providesabout25.00%inheadingangleandinvisibleenhancementsinrollandpitchangles.It
pitch angles. It is due to the observability improvement on the vertical gyroscope by add-
isduetotheobservabilityimprovementontheverticalgyroscopebyaddinganodometer.To
ing an odometer. To assess the impact of the odometer on attitude determination at each
assesstheimpactoftheodometeronattitudedeterminationateachepoch,wealsoprovided
epoch, we also provided the differences between the solutions with and without the
thedifferencesbetweenthesolutionswithandwithouttheodometerinFigure19.Fromit,
odometer in Figure 19. From it, there are visible differences in the three directions at every
therearevisibledifferencesinthethreedirectionsateveryepoch.Itmeansthattheodometer
epoch. It means that the odometer affects the estimation of roll, pitch, and heading angles.
affectstheestimationofroll,pitch,andheadingangles.Sucheffectsonpitchandrollwould
Such effects on pitch and roll would become invisible after using the statistic index (i.e.,
becomeinvisibleafterusingthestatisticindex(i.e., RMS).Anyway, tofurtherlyillustrate
RMS). Anyway, to furtherly illustrate the influence of the odometer on attitude determi-
theinfluenceoftheodometeronattitudedeterminationunderGNSSoutages.Theattitude
nation under GNSS outages. The attitude differences of BSSD PPP/INS and BSSD
differencesofBSSDPPP/INSandBSSDPPP/INS/ODOduringthe1500sand2500sare
PPP/INS/ODO during the 1500 s and 2500 s are plotted in Figure 20. It can be seen that the
plottedinFigure20.Itcanbeseenthatthehumpsofheadinganglesappearingattheprofile
humps of heading angles appearing at the profile of attitudes errors of PPP/INS TCI can
ofattitudeserrorsofPPP/INSTCIcanberestrainedeffectivelybytheadditionofanodometer.
be restrained effectively by the addition of an odometer. According to the average attitude
AccordingtotheaverageattitudeRMSsinFigure21,thereductioninattitudedriftscanbe
RMSs in Figure 21, the reduction in attitude drifts can be significantly constrained by us-
significantlyconstrainedbyusinganodometer.
ing an odometer.
Figure 19. Attitude differences between BSSD PPP/INS TCI and BSSD PPP/INS/ODO with different
GNSS.

<!-- PAGE: 16 -->

Remote Sens. 2023, 15, x FOR PEER REVIEW 17 of 22
Figure 18. Attitude errors of BSSD PPP/INS TCI (left) and BSSD PPP/INS/ODO TCI (right) with
different GNSS.
Table 6. Attitude RMS of BSSD PPP/INS TCI with and without odometer aid.
BSSD PPP/INS TCI BSSD PPP/INS/ODO TCI
° ° ° ° ° °
Roll ( ) Pitch ( ) Heading ( ) Roll ( ) Pitch ( ) Heading ( )
GPS 0.025 0.050 0.178 0.025 0.049 0.137
BDS-3 0.027 0.049 0.194 0.028 0.048 0.140
GPS/BDS-3 0.024 0.048 0.181 0.025 0.048 0.138
According to the RMSs of BSSD PPP/INS/ODO TCI listed in Table 6, the average
° ° °
RMSs of roll, pitch, and heading angles are 0.026 , 0.048 , and 0.138 . In contrast, the
odometer provides about 25.00% in heading angle and invisible enhancements in roll and
pitch angles. It is due to the observability improvement on the vertical gyroscope by add-
ing an odometer. To assess the impact of the odometer on attitude determination at each
epoch, we also provided the differences between the solutions with and without the
odometer in Figure 19. From it, there are visible differences in the three directions at every
epoch. It means that the odometer affects the estimation of roll, pitch, and heading angles.
Such effects on pitch and roll would become invisible after using the statistic index (i.e.,
RMS). Anyway, to furtherly illustrate the influence of the odometer on attitude determi-
nation under GNSS outages. The attitude differences of BSSD PPP/INS and BSSD
PPP/INS/ODO during the 1500 s and 2500 s are plotted in Figure 20. It can be seen that the
humps of heading angles appearing at the profile of attitudes errors of PPP/INS TCI can
be restrained effectively by the addition of an odometer. According to the average attitude
RemoteSens.2023,15,199 RMSs in Figure 21, the reduction in attitude drifts can be significantly constrained 1b6yo fu2s0-
ing an odometer.
Remote Sens. 2023, 15, x FOR PEER REVIEW 18 of 22
Remote Sens. 2023, 15, x FOR PEER REVIEW 18 of 22
FFiigguurree 1199.. AAtttittiutudde edidffieffreernecnecse bsebtwetewene eBnSSBDS SPDPPP/IPNPS/ ITNCSI aTnCdI BaSnSdD BPSPSPD/INPSP/PO/DINOS w/iOthD dOiffwerietnht
dGifNfeSreSn. tGNSS.
Figure 20. Attitude errors of BSSD PPP/INS TCI (left) and BSSD PPP/INS/ODO TCI (right) with
FiguFrieg u2r0e. 2A0t.tiAtuttditeu edreroerrsr oorfs BoSfSBDS SPDPPP/PIPN/SI NTCSIT (CleIf(tl)e aftn)da nBdSSBDSS PDPPPP/IPN/SI/NOSD/OO DTCOI T(rCigIh(rti)g whti)thw ith
frequent GNSS outages in the periods between the 1500 s and 2500 s.
frequent GNSS outages in the periods between the 1500 s and 2500 s.
frequentGNSSoutagesintheperiodsbetweenthe1500sand2500s.
Figure 21. Average of Maximum attitude drifts of different GNSS for BSSD PPP/INS TCI (left) and
Figure 21. Average of Maximum attitude drifts of different GNSS for BSSD PPP/INS TCI (left) and
PPP Fi /I g N ur S e /O 21 D . OA vTeCrIa g(reigohftM) oanx idmifufemreanttt iGtuNdSeSd oriufttsagoef dscifefneeres.n tGNSSforBSSDPPP/INSTCI(left)and
PPP/INS/ODO TCI (right) on different GNSS outage scenes.
PPP/INS/ODOTCI(right)ondifferentGNSSoutagescenes.
Similarly, the differences between the attitudes calculated by the undifferenced PPP-
Similarly, the differences between the attitudes calculated by the undifferenced PPP-
Similarly,thedifferencesbetweentheattitudescalculatedbytheundifferencedPPP-
based integration (Figure 22) and the BSSD PPP-based integration are plotted in Figure
based integration (Figure 22) and the BSSD PPP-based integration are plotted in Figure
basedintegration(Figure22)andtheBSSDPPP-basedinte°gration°areplotted°inFigure23.
23. The attitudes RMSs based on undifferenced PPP are 0.031° , 0.048° , and 0.135° in three
23.
T
Th
h
e
e
a
a
t
t
t
t
i
i
t
t
u
u
d
d
e
e
s
s
R
R
M
M
S
S
s
s
b
b
a
a
se
s
d
ed
on
o n
un
u
d
n
i
d
ff
i
e
ff
r
e
e
r
n
e
c
n
e
c
d
e
P
d
P
P
P
P
a
P
re
a
0
re
.0
0
3
.
1
03
,
1
0◦.
,
04
0
8
.04
,
8
a◦n
,
d
a n
0.
d
13
0
5
.13
i
5
n◦ t
i
h
n
re
th
e
ree
components, which are close to the solutions based on BSSD PPP. As the result shows, the
components, which are close to the solutions based on BSSD PPP. As the result shows, the
components, which are close to the solutions based on BSSD PPP. As the result shows,
two solutions are close to each other actually in terms of statistics index (RMS) but differ-
two solutions are close to each other actually in terms of statistics index (RMS) but differ-
the two solutions are close to each other actually in terms of statistics index (RMS) but
ent in time series, which is due to the accuracies of attitudes being mainly determined by
ent in time series, which is due to the accuracies of attitudes being mainly determined by
differentintimeseries,whichisduetotheaccuraciesofattitudesbeingmainlydetermined
IMU ([28,46]). However, the GNSS data processing strategy would affect the estimation
IMU ([28,46]). However, the GNSS data processing strategy would affect the estimation
byIMU([28,46]). However,theGNSSdataprocessingstrategywouldaffecttheestimation
of attitudes at each epoch by Equation (14). A similar conclusion can also be obtained from
of aottfitauttditeusd aets eaatchea ecphoecpho bcyh EbqyuEaqtiuoant i(o1n4)(.1 A4) s.iAmsiliamr icloarnccolunscilouns icoannc aalnsoa blseo obbetaoibnteadin ferdomfr om
the average maximum attitude drifts of the two methods from 1500 s to 2500 s with GNSS
the tahveearavgeera mgeaxmimaxuimmu amttitauttditeu ddreifdtsr ioftfs thofe tthweot wmoetmhoetdhso fdrosmfro 1m50105 s0 t0os 2t5o0205 s0 w0sithw GithNGSSN SS
outages in Figure 24.
outoaguetas gines FiinguFrigeu 2r4e. 2 4.
Figure 22. Attitude errors of undifferenced PPP/INS/ODO TCI with different GNSS.
Figure 22. Attitude errors of undifferenced PPP/INS/ODO TCI with different GNSS.

<!-- PAGE: 17 -->

Remote Sens. 2023, 15, x FOR PEER REVIEW 18 of 22
Figure 20. Attitude errors of BSSD PPP/INS TCI (left) and BSSD PPP/INS/ODO TCI (right) with
frequent GNSS outages in the periods between the 1500 s and 2500 s.
Figure 21. Average of Maximum attitude drifts of different GNSS for BSSD PPP/INS TCI (left) and
PPP/INS/ODO TCI (right) on different GNSS outage scenes.
Similarly, the differences between the attitudes calculated by the undifferenced PPP-
based integration (Figure 22) and the BSSD PPP-based integration are plotted in Figure
° ° °
23. The attitudes RMSs based on undifferenced PPP are 0.031 , 0.048 , and 0.135 in three
components, which are close to the solutions based on BSSD PPP. As the result shows, the
two solutions are close to each other actually in terms of statistics index (RMS) but differ-
ent in time series, which is due to the accuracies of attitudes being mainly determined by
IMU ([28,46]). However, the GNSS data processing strategy would affect the estimation
of attitudes at each epoch by Equation (14). A similar conclusion can also be obtained from
RemoteSens.2023,15,199 the average maximum attitude drifts of the two methods from 1500 s to 2500 s with G17NofS2S0
outages in Figure 24.
Remote Sens. 2023, 15, x FOR PEER REVIEW 19 of 22
Remote Sens. 2023, 15, x FOR PEER REVIEW 19 of 22
Figure22.AttitudeerrorsofundifferencedPPP/INS/ODOTCIwithdifferentGNSS.
Figure 22. Attitude errors of undifferenced PPP/INS/ODO TCI with different GNSS.
Figure 23. Attitudes differences between undifference d PPP/INS/ODO TCI and BSSD
Figure 23. Attitudes differences between undifferenced PPP/INS/ODO TCI and BSSD
PPP/INS/ODO TCI.
Figure 23. Attitudes differences between undifferenced PPP/INS/ODO TCI and BSSD
PPP/INS/ODOTCI.
PPP/INS/ODO TCI.
Figure 24. Mean maximumattitude driftsof different GNSSfor BSSDPPP/INS/ODO TCIand
Fuingudrifef e2r4e.n MceedaPnP mPa/xINimSu/mO DaOttitTuCdIe. drifts of different GNSS for BS SD PPP/INS/ODO TCI and un-
differenced PPP/INS/ODO TCI.
Figure 24. Mean maximum attitude drifts of different GNSS for BSSD PPP/INS/ODO TCI and un-
4. Discussion
differenced PPP/INS/ODO TCI.
4. DisBcaussesdioonn the BDS-3 PPP-B2b service, real-time PPP can be used via B2b signals.
H4. oDwiBseacvsueesrds, iiootnni st hseti BllDchS-a3ll PenPgPi-nBg2bin searnviucerb, raenale-ntivmireo PnPmPe cnatn. Abec cuosreddi nvgia tBo2tbh seiganssaelss.s Hmoewnt-s
eavbeorv, Bieta aissn e dsdt it olhln ec thr h eae sl lB ueD lntsgSi- sn3 ug P m iPnm P a- a Bnri 2 zub er s dbeai rnn v ieT cna ev, b rilre eoa 7nl , -mt t i h meenetp .P oAP s P ictc i coo arn ndi nibng eg u p ts eoe r d ftoh v rem i aa sa Bsn 2ec bses smo ig fen Bna StlsS s .aD HbPoovP weP -
ac ena vdn e rtb ,h e iet e irn se hssua ti nlltl cs c e sh duamv ll i e smn ib galri y nizg be ydin ti hna e n T a uadbr d blei a t n i7o ,e ntnho vef i rpI o NonsS mitaieon nnd ti.n o Agd c opc meorr efdote irn rm, g e at sno pc e teh c oi e a fa l lBs y sSe iSn sDs p m Pe e rPn iPo t d sc saanb w o bi v teh e
ef anr n ehd qa unth ecn ee dt r G evsiN usil Sbt S sl ys o ubu myta tm gheea s ra. idz T edh diet ii monn e T oa a nfb Il pNe o S7 s , ia t tni h ode n op Rdo Mosmit S ieo otn feirB n, S geS sp Dpeer Pcfio Par Plmlyis ainn 6 c 4pe .e3 or3ifoc Bdm Ss, S w5 D 3i t. P 4h7 P fPrcem cqau, n ae nnb dte
G1 e 5 nN4 hS. a 1Sn 1 oc cue m dta vgin iessi t b.h Tl r y eh e bey cmo th meae pn a o dpn doe isn tiitt oison bn o a Rf s e IMN dSS o on afn PBd PS o PSdD-B o m 2PbPePt s e e ir rs, v e6i s c4p e.3. e3c B icy amll i y n, 5t i e n3g. 4p r7a e r tci imn o g d, saI NnwdS it ,1h t5 h f4r e.e1q m1u ecema n n t
ip Gno Ntshi S trS ieo eo n ucR toamM gepS so. c nT aeh nnetb sm e be iam asnep dp r o oov sni e t d iPonPb Py R-MB312S .b2 o %sfe , Br2vS 3 Sic. D 3e%. PB, Pya P n iind st 6e2 4g7 .r. 3 3a3 %t icn. mgS , Iu 5N3 cSh .4, 7 pt hc e m rec , em a nen taa dng 1 ep5 s 4oc .s1 ai1 nti oc b mne
furtherly increased by 1.34%, 1.41%, and 1.73% after using an odometer. The test data
RinM tSh creaen cboem impopnroevnetsd bbays e3d1 .2o%n , P2P3P.3-%B2, ba nsde r2v7i.c3e%. B. Syu icnht epgerracteinngta gINesS ,c athne b em feuarnth peorlsyi tiino-n
from1500sto2500sareadoptedtovalidatetheperformanceintheperiodswithfrequent
cRreMasSe cda bny b 1e. 3im4%pr, o1v.4e1d% b, ya n3d1. 21%.73, %23 .a3f%te,r a unsdin 2g7 .a3n% o. dSoumche tpeerr. cTehnet atgesets dcaanta bfero fmur t1h5e0r0l ys itno-
GNSSoutages. Themeanpositionmaximumdriftsduringtheseperiodsdecreasedfrom
2c5r0e0a sse dar bey a 1d.o3p4%te,d 1 t.4o1 v%a,l iadnadte 1 t.7h3e% p earfftoerr musainncge ainn othdeo mpeertieord. sT hwei tthes ftr deqautae nfrto GmN 1S5S0 0o su tt-o
107.96cm,59.90cm,and78.22cmofBSSDPPPto88.52cm,54.54cm,and62.00cmofBSSD
a2g5e0s0. Ts haer em aedaonp pteodsi ttioo nv amliadxaitme uthme dpreirfftso rdmuarinncge tihne sthe ep pereiroidods sd ewcirteha sferedq furoenmt 1G0N7.S9S6 comut,-
PPP/INSTCI.Afteraddinganodometer,suchvaluesare66.29cm,45.84cm,and49.17cm.
5a9g.9e0s. cTmh,e a mndea 7n8 .p2o2s cimtio onf mBSaSxDim PuPmP dtor i8ft8s. 5d2u crmin,g 5 t4h.5e4se c pme,r aiondds 6 d2e.0c0re camse odf fBroSmSD 1 P07P.P96/I NcmS ,
T5C9.I9. 0A cfmte,r aanddd i7n8g.2 a2n c mod oofm BeStSeDr, sPuPcPh tvoa 8lu8.e5s2 a crme ,6 564.2.594 c cmm, ,4 a5n.8d4 6c2m.0, 0a cnmd 4o9f .B17S ScDm .P P P/INS
TCI.A Anfytewr aayd,d tihneg paons oitdioonm aectecru,r sauccyh o vf aPluPePs/ IaNreS /6O6.D29O c mTC, I4 5b.a8s4e cdm o, na nthde 4 9B.S1S7D cm m. o del is
slightAlyn hyiwghaeyr, tthhaen p tohsei tsioolnu taicocnusr bacayse odf oPnP tPh/eIN uSn/dOifDfeOre TncCeId b masoedde lo. nC tohme pBaSrSeDd wmiothd euln i-s
dsilfifgehrtelnyc heidg hPePrP t/hINanS t/hOeD sOol uTtCioIn, sth bea smedea onn pthoesi utinodn ifRfeMreSn ocef dB mSSoDd ePl.P CPo/ImNpSa/OreDdO w TitCh Iu ins-
idmifpfreorevnecde dby P 7P.P71/I%N,S 3/.O09D%O, aTnCdI , 0t.h2e7 %m. eTahne pmoesiatnio mn aRxMimSu omf BdSrSifDts PcaPnP /bIeN rSe/dOuDcOed T fCroIm is
8i2m.3p8r ocmve,d 5 0b.6y6 7 c.7m1,% a,n 3d. 0592%.3,0 acnmd t0o. 2676%.29. Tcmhe, 4m5e.8a4n c mma, xainmdu 4m9.1 d7r cifmts bcya nu tbileiz riendgu tcheed B fSrSoDm
m82o.d38e lc. m, 50.66 cm, and 52.30 cm to 66.29 cm, 45.84 cm, and 49.17 cm by utilizing the BSSD
° °
modFeol.r attitude determination, the mean attitude RMS of PPP/INS TCI is 0.025 , 0.049
° ° °
, and F0o.1r8 a4tti tuind eth dreeete crmominpaotinoenn,t tsh. eT mhee aand daitttiiotund oef RaMn So doof mPPePte/rI NbSri nTgCsI ais 205.0%2 5im,p 0r.o0v49e-
° °
m, aenndt t0o. 1th84e R Min St horfe he ecaodminpgo nanengltes.s Tahned ardedduitcioesn tohfe a mn eoadno mmaexteimr burmin gdsr iaft s2 5fr%o mim 0p.3ro13ve-
° °
tmo e0n.1t7 t4o t. hTeh Re MreSsu olft sh oefa dthine go tahnegrl etws aon cdo mrepdounceens ttsh aer me ceoamn pmaarxabimleu. mM odrreioftvse frr,o tmhe 0a.3cc1u3-
°
rtaoc y0 .o17f 4PP.P T/IhNe Sr/eOsuDlOts TofC tIh we iothth aenr dtw woi tchoomutp tohnee BnStsS Dar em coodmelp iasr saibmlei.l aMr toor eeoavcher o, tthheer a. ccu-
racy of PPP/INS/ODO TCI with and without the BSSD model is similar to each other.

<!-- PAGE: 18 -->

RemoteSens.2023,15,199 18of20
Table7.Statisticofpositionandattitudeerrors.
MeanRMS(cm) MeanMaximumDrifts(cm)
Positioning North East Down North East Down
BSSDPPP 64.33 53.47 154.11 107.96 59.90 78.22
BSSDPPP/INSTCI 44.54 41.29 121.66 88.52 54.54 62.00
BSSDPPP/INS/ODOTCI 44.01 40.79 118.83 66.29 45.84 49.17
UndifferencedPPP/INS/ODOTCI 47.69 42.09 119.15 82.38 50.66 52.30
MeanRMS(◦) MeanMaximumDrifts(◦)
Attitude Roll Pitch Heading Roll Pitch Heading
BSSDPPP/INSTCI 0.025 0.049 0.184 0.047 0.077 0.313
BSSDPPP/INS/ODOTCI 0.026 0.048 0.138 0.049 0.076 0.174
UndifferencedPPP/INS/ODOTCI 0.031 0.048 0.135 0.058 0.082 0.163
Anyway,thepositionaccuracyofPPP/INS/ODOTCIbasedontheBSSDmodelisslightly
higherthanthesolutionsbasedontheundifferencedmodel. Comparedwithundifferenced
PPP/INS/ODOTCI,themeanpositionRMSofBSSDPPP/INS/ODOTCIisimprovedby
7.71%,3.09%,and0.27%.Themeanmaximumdriftscanbereducedfrom82.38cm,50.66cm,
and52.30cmto66.29cm,45.84cm,and49.17cmbyutilizingtheBSSDmodel.
Forattitudedetermination,themeanattitudeRMSofPPP/INSTCIis0.025◦,0.049◦,
and0.184◦ inthreecomponents. Theadditionofanodometerbringsa25%improvement
totheRMSofheadinganglesandreducesthemeanmaximumdriftsfrom0.313◦ to0.174◦.
The results of the other two components are comparable. Moreover, the accuracy of
PPP/INS/ODOTCIwithandwithouttheBSSDmodelissimilartoeachother.
5. Conclusions
Inthiscontribution,weimpliedthetightlycoupledintegrationofBDS-3/GPS,low-cost
IMU,andodometerbasedontheinter-satellitedifferencedPPPmodelandtheorbit/clock
correctionsofPPP-B2b. Avehicleexperimentinurbancircumstanceswasimplementedto
validatetheperformanceofpositioningandattitudedeterminationofthedevelopedmodel.
Thefollowingconclusionscanbeobtained. (1)WiththeadditionofINS,theimprovements
ofBSSDPPPpositionaccuracyonaveragearemorethan31.2%,23.3%,and27.3%inthe
north,east,anddowndirections. Furtherenhancementsinpositionaccuracyareachievable
withtheaidofanodometer, especiallywhilesufferingGNSSoutages. (2)Byusingthe
odometer,theaccuraciesofpitchandheadinganglesareimprovedbyabout2.04%and
25%. (3) In comparison with the PPP/INS/ODO TCI based on the undifferenced PPP
model,thedevelopedBSSDmodelcanprovideresultswithhigheraccuracy,especiallyin
there-convergenceperiods. Forattitudedetermination,comparableresultscanbeobtained
byboththeBSSDmodelandtheundifferencedmodel.
AuthorContributions:Conceptualization,Y.M.andZ.G.;datacuration,Y.M.,Q.X.andR.L.;funding
acquisition,C.Y.andZ.G.;investigation,Y.M.andZ.G.;software,Y.M.andZ.G.;visualization,Y.M.
andJ.L.;writing—originaldraftpreparation,Y.M.;writing—reviewandediting,Y.M.,Z.G.andC.Y.
Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding: This research was partly supported by the National Key Research and Development
ProgramofChina(GrantNo. 2021YFB3901301)andtheNationalNaturalScienceFoundationof
China(NSFC)(GrantNo.42274022).
DataAvailabilityStatement:ThedatasetsadoptedinthispaperaremanagedbytheSchoolofLand
ScienceandTechnology,ChinaUniversityofGeosciencesBeijingandcanbeavailableonrequest
fromthecorrespondingauthor.
Acknowledgments: The authors would like to thank anonymous reviewers who gave valuable
suggestionsthathelpedtoimprovethequalityofthemanuscripts.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

<!-- PAGE: 19 -->

RemoteSens.2023,15,199 19of20
References
1. Yang,Y.;Xu,Y.;Li,J.;Yang,C.ProgressandPerformanceEvaluationofBeiDouGlobalNavigationSatelliteSystem:DataAnalysis
BasedonBDS-3DemonstrationSystem.Sci.ChinaEarthSci.2018,61,614–624.[CrossRef]
2. Yang,Y.;Li,J.;Wang,A.;Xu,J.;He,H.;Guo,H.;Shen,J.;Dai,X.Preliminaryassessmentofthenavigationandpositioning
performanceofBeiDouregionalnavigationsatellitesystem.Sci.ChinaEarthSci.2014,57,144–152.[CrossRef]
3. Yang, Y.; Tang, J.; Montenbruck, O. Chinese navigation satellite systems. In Handbook of Global Navigation Satellite Systems;
Teunissen,M.,Ed.;Springer:Cham,Switzerland,2017;Chapter10;pp.273–304.
4. Lv,J.;Gao,Z.;Kan,J.;Lan,R.;Li,Y.;Lou,Y.;Yang,H.;Peng,J.ModelingandAssessmentofMulti-FrequencyGPS/BDS-2/BDS-3
KinematicPrecisePointPositioningBasedonVehicle-BorneData.Measurement2022,189,110453.[CrossRef]
5. Shi,C.;Wu,X.;Zheng,F.;Wang,X.;Wang,J.ModelingofBDS-2/BDS-3Single-FrequencyPPPwithB1IandB1CSignalsand
PositioningPerformanceAnalysis.Meas.J.Int.Meas.Confed.2021,178,109355.[CrossRef]
6. Jiao,G.;Song,S.;Jiao,W.ImprovingBDS-2andBDS-3JointPrecisePointPositioningwithTimeDelayBiasEstimation.Meas.Sci.
Technol.2019,31,25001.[CrossRef]
7. Lu,M.;Li,W.OverviewofBDSIIINewSignals.Navigation2019,66,19–35.[CrossRef]
8. Zumberge,J.F.;Heflin,M.B.;Jefferson,D.C.;Watkins,M.M.;Webb,F.H.PrecisePointPositioningfortheEfficientandRobust
AnalysisofGPSDatafromLargeNetworks.J.Geophys.Res.SolidEarth1997,102,5005–5017.[CrossRef]
9. Gao,Y.;Shen,X.ANewMethodforCarrier-Phase-BasedPrecisePointPositioning.Navigation2002,49,109–116.[CrossRef]
10. Li,X.;Ge,M.;Zhang,H.;Wickert,J.AMethodforImprovingUncalibratedPhaseDelayEstimationandAmbiguity-Fixingin
Real-TimePrecisePointPositioning.J.Geod.2013,87,405–416.[CrossRef]
11. Elsobeiey,M.;El-Rabbany,A.EfficientBetween-SatelliteSingle-DifferencePrecisePointPositioningModel.J.Surv.Eng.2014,
140,04014007.[CrossRef]
12. Kouba,J.AGuidetoUsingInternationalGNSSService(IGS)Products.IGS.2015.Availableonline:http://igscb.jpl.nasa.gov/
igscb/resource/pubs/UsingIGSProductsVer21.pdf(accessedon9September2022).
13. Kouba,J.;Héroux,P.PrecisePointPositioningUsingIGSOrbitandClockProducts.GPSSolut.2001,5,12–28.[CrossRef]
14. Zhang,W.;Lou,Y.;Song,W.;Sun,W.;Zou,X.;Gong,X.InitialAssessmentofBDS-3PrecisePointPositioningServiceonGEO
B2bSignal.Adv.Sp.Res.2022,69,690–700.[CrossRef]
15. Nie,Z.;Xu,X.;Wang,Z.;Du,J.InitialAssessmentofBDSPPP-B2bService:PrecisionofOrbitandClockCorrections,andPPP
Performance.RemoteSens.2021,13,2050.[CrossRef]
16. Tao,J.;Liu,J.;Hu,Z.;Zhao,Q.;Chen,G.;Ju,B.InitialAssessmentoftheBDS-3PPP-B2bRTSComparedwiththeCNESRTS.
GPSSolut.2021,25,131.[CrossRef]
17. Ren,Z.;Gong,H.;Peng,J.;Tang,C.;Huang,X.;Sun,G.PerformanceAssessmentofReal-TimePrecisePointPositioningUsing
BDSPPP-B2bServiceSignal.Adv.Sp.Res.2021,68,3242–3254.[CrossRef]
18. Wang,L.;Li,Z.;Ge,M.;Neitzel,F.;Wang,X.;Yuan,H.InvestigationofthePerformanceofReal-TimeBDS-OnlyPrecisePoint
PositioningUsingtheIGSReal-TimeService.GPSSolut.2019,23,66.[CrossRef]
19. Zhang,L.;Yang,H.;Gao,Y.;Yao,Y.;Xu,C.EvaluationandAnalysisofReal-TimePreciseOrbitsandClocksProductsfrom
DifferentIGSAnalysisCenters.Adv.Sp.Res.2018,61,2942–2954.[CrossRef]
20. Gao,Z.;Zhang,H.;Ge,M.;Niu,X.;Shen,W.;Wickert,J.;Schuh,H.TightlyCoupledIntegrationofIonosphere-Constrained
PrecisePointPositioningandInertialNavigationSystems.Sensors2015,15,5783–5802.[CrossRef]
21. Gao,Z.;Ge,M.;Shen,W.;Zhang,H.;Niu,X.IonosphericandReceiverDCB-ConstrainedMulti-GNSSSingle-FrequencyPPP
IntegratedwithMEMSInertialMeasurements.J.Geod.2017,91,1351–1366.[CrossRef]
22. Shin, E.-H.EstimationTechniquesforLow-CostInertialNavigation. Ph.D.Thesis, TheUniversityofCalgary, Calgary, AB,
Canada,May2005.
23. Cox,D.B.J.IntegrationofGPSwithInertialNavigationSystems.Navigation1978,25,236–245.[CrossRef]
24. Gu,S.;Dai,C.;Fang,W.;Zheng,F.;Wang,Y.;Zhang,Q.;Lou,Y.;Niu,X.Multi-GNSSPPP/INSTightlyCoupledIntegrationwith
AtmosphericAugmentationandItsApplicationinUrbanVehicleNavigation.J.Geod.2021,95,64.[CrossRef]
25. Le,A.Q.;Lorga,J.CombiningInertialNavigationSystemWithGPSPrecisePointPositioning:FlightTestResults.InProceedings
oftheIONGNSS2006,FortWorth,TX,USA,26–29September2006;pp.3035–3042.
26. Martell,H.TightlyCoupledProcessingofPrecisePointPosition(PPP)andINSData. InProceedingsoftheIONGNSS2009,
Savannah,GA,USA,22–25September2009;pp.1898–1905.
27. Du,S.IntegrationofPrecisePointPositioningandLowCostMEMSIMU.Master’sThesis,TheUniversityofCalgary,Calgary,
AB,Canada,November2010.
28. AbdRabbou,M.;El-Rabbany,A.TightlyCoupledIntegrationofGPSPrecisePointPositioningandMEMS-BasedInertialSystems.
GPSSolut.2015,19,601–609.[CrossRef]
29. BeiDouNavigationSatelliteSystemSignalinSpaceInterfaceControlDocument:PrecisePointPositioningServiceSignalPPP-B2b
(Version1.0).2020.Availableonline:http://en.beidou.gov.cn/SYSTEMS/ICD/202008/P020200803538771492778.pdf(accessed
on20October2021).
30. Gao,Z.;Zhang,H.;Ge,M.;Niu,X.;Shen,W.;Wickert,J.;Schuh,H.TightlyCoupledIntegrationofMulti-GNSSPPPandMEMS
InertialMeasurementUnitData.GPSSolut.2017,21,377–391.[CrossRef]

<!-- PAGE: 20 -->

RemoteSens.2023,15,199 20of20
31. Sun, W.; Yang, Y. BDS PPP/INS Tight Coupling Method Based on Non-Holonomic Constraint and Zero Velocity Update.
IEEEAccess2020,8,128866–128876.[CrossRef]
32. Gao,Z.;Ge,M.;Li,Y.;Chen,Q.;Zhang,Q.;Niu,X.;Zhang,H.;Shen,W.;Schuh,H.Odometer,Low-CostInertialSensors,and
Four-GNSSDatatoEnhancePPPandAttitudeDetermination.GPSSolut.2018,22,57.[CrossRef]
33. Witchayangkoon,B.ElementsofGPSPrecisePointPositioning. Ph.D.Thesis,SpatialInformationScienceandEngineering,
UniversityofMaine,Orono,ME,USA,2000.
34. Pintor,P.;González,E.;Senado,A.;Bohlig,P.;Sperl,A.;Henkel,P.;Simón,J.;Hernández,C.;deBlas,J.;Vázquez,J.GalileoHigh
AccuracyService(HAS)AlgorithmandReceiverDevelopmentandTesting.InProceedingsofthe35thInternationalTechnical
MeetingoftheSatelliteDivisionofTheInstituteofNavigation(IONGNSS+2022),Denver,CO,USA,19–23September2022;
pp.836–851.
35. Cai,C.;Gao,Y.ModelingandAssessmentofCombinedGPS/GLONASSPrecisePointPositioning.GPSSolut.2013,17,223–236.
[CrossRef]
36. Chen,J.;Pei,X.;Zhang,Y.;Wu,B.GPS/GLONASSSystemBiasEstimationandApplicationinGPS/GLONASSCombined
Positioning.Lect.NotesElectr.Eng.2013,244,323–333.
37. Choy,S.;Zhang,S.;Lahaye,F.;Héroux,P.AComparisonbetweenGPS-OnlyandCombinedGPS+GLONASSPrecisePoint
Positioning.J.Spat.Sci.2013,58,169–190.[CrossRef]
38. Zhou,F.;Dong,D.;Li,P.;Li,X.;Schuh,H.InfluenceofStochasticModelingforInter-SystemBiasesonMulti-GNSSUndifferenced
andUncombinedPrecisePointPositioning.GPSSolut.2019,23,59.[CrossRef]
39. Jiang,N.;Xu,Y.;Xu,T.;Xu,G.;Sun,Z.;Schuh,H.GPS/BDSShort-TermISBModellingandPrediction. GPSSolut. 2017,21,
163–175.[CrossRef]
40. Niu,X.;Goodall,C.;Nassar,S.;El-Sheimy,N.AnefficientmethodforevaluatingtheperformanceofMEMSIMUs.InProceedings
ofthePositionlocationandNavigationSymposium,2006IEEE/ION,SanDiego,CA,USA,25–27April2016;pp.766–771.
41. Sukkarieh, S. Low Cost, High Integrity, Aided Inertial Navigation Systems for Autonomous Land Vehicles. Ph.D. Thesis,
UniversityofSydney,Sydney,Australia,January2000.
42. Mohamed,A.;Schwarz,K.AdaptiveKalmanFilteringforINS/GPS.J.Geod.1999,73,193–203.[CrossRef]
43. Lu,C.;Li,X.;Nilsson,T.;Ning,T.;Heinkelmann,R.;Ge,M.;Glaser,S.;Schuh,H.Real-TimeRetrievalofPrecipitableWaterVapor
fromGPSandBeiDouObservations.J.Geod.2015,89,843–856.[CrossRef]
44. An,X.;Meng,X.;Jiang,W.Multi-ConstellationGNSSPrecisePointPositioningwithMulti-FrequencyRawObservationsand
Dual-FrequencyObservationsofIonospheric-FreeLinearCombination.Satell.Navig.2020,1,7.[CrossRef]
45. Li,X.;Ge,M.;Dai,X.;Ren,X.;Fritsche,M.;Wickert,J.;Schuh,H.AccuracyandReliabilityofMulti-GNSSReal-TimePrecise
Positioning:GPS,GLONASS,BeiDou,andGalileo.J.Geod.2015,89,607–635.[CrossRef]
46. Huang,L.;Lu,Z.;Li,B.;Xin,G.;An,W.;Lv,H.;Wang,N.;Zhou,X.ThePerformanceAnalysisofMulti-SystemIntegratedPrecise
PointPositioning(PPP).Lect.NotesElectr.Eng.2016,390,317–326.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.