<!-- PAGE: 1 -->

Received2April2026,accepted23April2026,dateofpublication4May2026,dateofcurrentversion7May2026.
DigitalObjectIdentifier10.1109/ACCESS.2026.3689972
GKit-SSRDecoder: An Open-Source C/C++-Based
PPP-B2b and HAS Decoding and Formatted
Product Generation Software
ZHIYUANWU1,PANLI 1,JIAHUANHU 2,JINGKAIYUAN 1,MINGBAOWEI1,YANGSUN1,
BAOSHU1,BOBINCUI 1,ANDGUANWENHUANG 1,(StudentMember,IEEE)
1CollegeofGeologyEngineeringandGeomatics,Chang’anUniversity,Xi’an710054,China
2DepartmentofLandSurveyingandGeo-Informatics,TheHongKongPolytechnicUniversity,HongKong,China
Correspondingauthor:PanLi(lipan@chd.edu.cn)
ThisworkwassupportedinpartbytheNationalKeyResearchandDevelopmentProgramofChinaunderGrant2023YFC3008300and
Grant2023YFC3008304;inpartbytheNationalNaturalScienceFoundationofChinaunderGrant42374026;inpartbytheResearch
FundsfortheInterdisciplinaryProjects,Chang’anUniversity(CHU),underGrant300104240914;andinpartbytheFundamental
ResearchFundsfortheCentralUniversities,CHU,underGrant300102263401.
ABSTRACT WiththerapiddevelopmentofReal-TimePrecisePointPositioning(RT-PPP),theBeiDou-3
PPP-B2bandGalileoHighAccuracyService(HAS)havebecomepivotalforprovidingfree,global,satellite-
basedprecisecorrectionservices.However,mostexistingopen-sourcedecodingtoolsaredevelopedbasedon
thePythonlanguage,whichlimitstheirintegrationintoembeddedsystemsandreal-timeC/C++positioning
frameworks. In addition, these raw data streams lack standardized input formats and product generation,
anddonottakeintoaccountuser-sidesatelliteantennacalibration,whichhindersofflineanalysisandcross-
platformverification.Tobridgethesegaps,thisstudydevelopsandpresentstheGKit-SSRDecoder,anopen-
source,high-performanceC/C++-basedsoftwaredesignedfortheend-to-endprocessingofPPP-B2band
HASmessages.Thesoftwarefeaturesamodulararchitecturethatsupportsmulti-receiverrawdatastream
parsing, State Space Representation (SSR) message decoding, and the automated generation of RINEX-
compliant precise orbit, clock, and code bias products. Comprehensive evaluations were conducted using
datafromdiverseGNSSreceiversandcomparedagainstpost-processedproducts.Theresultsdemonstrated
thattheSignal-In-SpaceRangeErrors(SISRE)forthePPP-B2bserviceis0.093mand0.086mforGPSand
BDS-3,respectively,whiletheHASserviceachieves0.057mforGPSand0.048mforGalileo.Positioning
tests showed that the generated products enable RT-PPP to reach centimeter-to-decimeter-level accuracy
in static and kinematic modes. Specifically, in real-time kinematic scenarios, the positioning performance
of the PPP-B2b and HAS services achieves RMS values of 0.13/0.11/0.12 m and 0.18/0.12/0.23 m in the
East/North/Up directions, respectively. This software serves as a useful and portable tool for the GNSS
community, facilitating the industrial application and scientific research of satellite-based augmentation
services.
INDEX TERMS Real-time precise point positioning, PPP-B2b, high accuracy Service, open-source
software.
I. INTRODUCTION latencyofpreciseorbitandclockproducts[2],[3].Tosatisfy
PrecisePointPositioning(PPP)technologyhasbeenwidely the demand for real-time PPP (RT-PPP) applications, many
appliedinPositioning,Navigation,andTiming(PNT)appli- analysiscentersorindustrialserviceprovidersprovidereal-
cationsowingtoitscharacteristicsofall-weatheradaptability timeorbitandclockcorrectionsaccordingtotheRadioTech-
and global high-accuracy services [1]. Initially, PPP was nicalCommissionforMaritimeServices(RTCM)protocols
generallyperformedinpost-processingmodebecauseofthe [4], [5]. These corrections are broadcasted to global users
via the Internet based on Networked Transport of RTCM
The associate editor coordinating the review of this manuscript and viaInternetProtocol(NTRIP)withverylowlatency[6],[7],
[8],[9].
approvingitforpublicationwasXinSun .
2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
67918 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME14,2026

<!-- PAGE: 2 -->

Z.Wuetal.:GKit-SSRDecoder:Open-SourceC/C++-BasedPPP-B2bandHASDecoding
However,theseinternet-dependentground-basedservices several open-source decoding tools have emerged as sum-
are inaccessible in remote areas like deserts or oceans. To marized in Table 1, they face critical technical bottlenecks.
addressthis,satellite-basedservicessuchastheBDS-3PPP- For instance, HASlib is restricted to specific input formats,
B2b and the Galileo High Accuracy Service (HAS) service whileGHASPyieldsoutputsthatdeviatefromstandardPPP
have emerged, broadcasting precise corrections directly via requirements [22], [23]. More importantly, the predominant
satellitesignals[10],[11],[12].Whiletheseservicessuccess- relianceonPythoninframeworkslikeNavDecodeandCSS-
fullyenableinternet-freeRT-PPP,theybroadcastcorrections Rlib [24], [25] creates a significant gap. While Python is
in proprietary binary formats due to bandwidth constraints, highly efficient for post-processing analysis, it introduces
creating significant interoperability barriers for users. To substantial latency and integration challenges when embed-
overcome these decoding barriers and facilitate scientific dedintolow-power,mainstreamC/C++positioningframe-
applications, the specific aim of this research is to provide works.AlthoughHASPPPoffersaC/C++alternativeforthe
an efficient, open-source C/C++ software, namely GKit- HASservice[26],itcurrentlylackscomprehensivehandling
SSRDecoder,fordecodingandformattingPPP-B2bandHAS ofsatelliteantennaphasecenter(APC)correctionsaswellas
messagesfromdiversereceivermanufacturers,ensuringsci- theabsenceofephemerisoutput.
entificallyassessedserviceaccuracyandseamlessintegration
intoreal-timeprecisepositioningapplications.
TABLE1. Thestatusofcurrentopen-sourcesoftwarepackages.
The rest of this paper is organized as follows: Section II
reviewsrelatedworksregardingsatellite-basedservicesand
existingdecodingtools.SectionIIIintroducestheframework
andworkflowoftheGKit-SSRDecodersoftware.SectionIV
evaluatesthequalityofthedecodedB2b/HASproductsand
assessesthereal-timePPPperformance.Finally,conclusions
aredrawninSectionV.
II. RELATEDWORK
A. SATELLITE-BASEDSERVICESADVANCEMENT
Withtheoperationalizationofsatellite-basedcorrectionser-
Therefore, a significant research gap remains: existing
vices,extensiveresearchhasevaluatedtheirperformance.the
toolsareoftenimplementedinPython,which,whilesuitable
PPP-B2bservicedirectlybroadcastspreciseorbit,clock,and
for post-processing, poses challenges for low-latency, real-
Differential Code Biases (DCB) corrections via B2b signal
timeintegrationintoindustrialC/C++positioningengines.
ofthreeGeostationaryEarthOrbit(GEO)satellites,enabling
Furthermore,thelackofaunifiedinterfaceformulti-vendor
real-time PPP for users within China and its surrounding
hardware protocols necessitates a redundant development
regions[10].TheGalileoHASserviceoftheEuropeanUnion
process. The GNSS community urgently requires a unified,
provides orbit, clock, code, and phase bias in Observable-
full-featured, C/C++ based end-to-end stream decoding
specific Signal Biases (OSB) format worldwide for free
software that natively supports both PPP-B2b and HAS
through its E6 signal [11]. Besides, the QZSS Centime-
multi-vendorprotocols,whichistheprimarymotivationfor
ter Level Augmentation Service (CLAS) provides compre-
developingGKit-SSRDecoder.
hensive State-Space Representation (SSR) corrections over
Japan, enabling rapid carrier-phase ambiguity resolution III. METHODOLOGY
within minutes [13]. Several studies have comprehensively TheGKit-SSRDecodersupportsthedecodingofrawbinary
analyzed and compared the feasibility of those services B2b/HAS data from various manufacturers and outputting
from various perspectives [14], [15], [16], and successfully preciseephemerisandDCB/OSBproductsinReceiverInde-
applied them to scientific research [17], [18]. Moreover, pendentExchangeFormat(RINEX),andthereferencecenter
specificattentionhasbeenpaidtothestrategiesforestimating of the orbit products could be customized by users. The
PPP-B2b phase bias products, developing novel receiver methodology of GKit-SSRDecoder is built upon a modular
clock models, and combining different services [19], [20], streamingarchitecture.Itinvolvesfourcriticallayers:(1)data
[21]. These evaluations demonstrate that those services can input and reading; (2) SSR message decoding; (3) satellite
achievedecimeter-tocentimeter-levelpositioningaccuracy, precise ephemeris calculating; (4) result and product out-
satisfying the stringent requirements for real-time precise putting. The detailed flowchart of the GKit-SSRDecoder is
positioning. presentedinFig.1.
B. CURRENTLIMITIONANDMOTIVATION A. DATAINPUTANDREADING
DespitetheprovenaccuracyofPPP-B2bandHASservices, ThedatasetsrequiredbyGKit-SSRDecoderaredividedinto
the broadcasting of corrections in proprietary binary for- mandatory and optional components, the mandatory data
mats introduces significant interoperability barriers due to include the raw binary files of B2b/HAS, satellite antenna
heterogeneous frame headers across manufacturers. While correction (.atx) files, and broadcast ephemeris files in
VOLUME14,2026 67919

<!-- PAGE: 3 -->

Z.Wuetal.:GKit-SSRDecoder:Open-SourceC/C++-BasedPPP-B2bandHASDecoding
corrections cannot be applied standalone without broadcast
ephemeris. Initially, the approximate satellite position vec-
tor (r), satellite velocity vector (v), and clock offset (t) are
calculatedusingthebroadcastephemeris,withGPS,Galileo,
andBDS-3employingLNAV,INAV,andCNAV1navigation
messages,respectively.Itisworthmentioningthatthecalcu-
lationofsatellitepreciseorbitandclockinformationforB2b
andHASdiffers.Specifically,theformulasareasfollows:

 b r B2b =r −[ | r r| |r r × × v v | ×
=
|
t
r r |
−
|r r
(cid:49)
× × v v
t
|
B
]
2b
·δO B2b , b t B2b
c (1)
 b r HAS =r +[ | r r × × v v| ×
=
|r r
t
|
+
|r r |
(cid:49)
|
t
r r
H
× ×
A
v v
S
| ]·δO HAS , b t HAS
c
whereδOrepresentsthedecodedthree-dimensionalorbitcor-
rectionscomposedbytheradial,tangential,andnormalcom-
ponents,and(cid:49)treferstoclockoffsetcorrectionofB2b/HAS;
FIGURE1. ArchitectureoftheGKit-SSRDecodersoftware.
crepresents the speed of light;
b
r andb t are the satellite pre-
cise orbit coordinates and clock offsets referred to satellite
APC. Moreover, the reference APC varies across different
RINEX 4.0 format. It is optional to input DCB files from
systems. For GPS and Galileo systems, the satellite APC
theChineseAcademyofSciences(CAS)orCenterforOrbit
isassociatedwiththedual-frequencyionosphere-freesignal
DeterminationinEurope(CODE)forassessingtheaccuracy
combinationsofL1/L2andE1/E5b,respectively.Incontrast,
of code biases broadcast by PPP-B2b and HAS services. It
theAPCcorrespondingtoBDS-3satellitesreferstotheB3I
should be noted that the antenna file must be consistent in
signal. Therefore, to facilitate the applicability of the un-
date with the B2b/HAS data, and the HAS service always
differencedandun-combinedmodel,aswellasincorporating
uses version 14. Otherwise, the accuracy of the recovered
otherfrequenciesinreal-timePPP,itisnecessarytotransform
satellite orbit products at the phase center will be affected
r intosatellitecoordinatesr referencedtothecenterofmass
b s
bytheinconsistencybetweenthem[27].Moreover,broadcast
(CoM):
ephemerisfilesfromthreeconsecutivedaysareneededwhen
processing data over an entire day due to the IOD version r
s
C =rcC −pco
B3I
d
p
e
la
la
ce
y
d
in
in
th
th
e
e
B
s
2
am
b/
e
H
fi
A
l
S
ed
se
ir
r
e
v
c
ic
to
e
r
.
y
N
.
otethatallfilesneedtobe r
s
G =rbG−(α
L1/L2
·pco
L1
+β
L1/L2
·pco
L2
)
r
s
E =rbE −(α
E1/E5b
·pco
E1
+β
E1/E5b
·pco
E5b
)
B. SSRMESSAGEDECODING e = e y ×e z ,e = b r ×( b r −r SUN ) ,e =−b r
TheGKit-SSRDecodersupportsrawbinarydataofB2b/HAS x (cid:12) (cid:12)e y ×e z (cid:12) (cid:12) y | b r ×( b r −r SUN )| z | b r|
corrections collected by different types of receivers, which pco =(e e e )·((cid:49)x (cid:49)y (cid:49)z)T (2)
j x y z j
is conducive to the development of real-time software. By
recognizingthecustomdataframeheadersofvariousmanu- where r is the sun coordinates in Earth-center-Earth-
SUN
facturers,itextractstherawB2b/HASbinarydatafordecod- fixed(ECEF)frame,αandβaredual-frequencyionosphere-
ing. The extracted raw B2b data can be decoded based on freecombinationfactor;((cid:49)x (cid:49)y (cid:49)z) representsthePhase
j
their message types. In contrast, the extracted raw HAS CenterOffset(PCO)correctionsoffrequencyj.Similarly,the
C/NAVdataneedstobefurtherencodedwithaHigh-Parity transformation of orbit product referenced to the combined
Vertical Reed-Solomon (HPVRS) scheme before decoding double-frequencyistheinverseprocessdescribedabove.
the corrections according to their message types [28], [29].
Currently,thesoftwaresupportsrawHASdatacollectedfrom D. RESULTSANDPRODUCTOUTPUTTING
Septentrio,NovAtel,ChineseSINOandUnicorereceivers,as Subsequent to the aforementioned procedures, the soft-
wellasrawB2bdatacollectedfromSeptentrioandUnicore wareproducespreciseephemerisproductsinRINEXformat
receivers. Users can easily extend the capability to process encompassingbothSP3andCLKfiles,atatimeintervalpre-
datafromothermanufacturers. set by the command parameters. Concurrently, the software
outputs daily DCB and OSB files of all satellites, contain-
C. SATELLITEPRECISEEPHEMERISCALCULATING ing a single value for each. The format of DCB/OSB files
The decoded B2b/HAS information in the previous step is adherestotheSINEXbiasformat,andthespecificfrequency
thecorrectionswithrespecttothebroadcastephemerisrather channelsincludedarelistedinTable2.TheGPSC2Wsignal,
than the raw satellite orbit and clock information, i.e., the whichisnotbroadcastedintheHASservice,canbeconverted
67920 VOLUME14,2026

<!-- PAGE: 4 -->

Z.Wuetal.:GKit-SSRDecoder:Open-SourceC/C++-BasedPPP-B2bandHASDecoding
andoutputbythesoftwareusingDCBproductspublishedby
CODE.
The software is configured using command parameters
intheformat:‘‘<YOURDATAPATH><SSRType><Time
Interval><TimeofStart><TimeofEnd>’’.Here,<YOUR
DATAPATH> is the directory for input data files. <SSR
Type>canbesetto‘‘B2b’’or‘‘HAS’’toidentifyrawSSR
datafiles.<TimeInterval>setstheoutputinterval(inmin-
utes) for SP3 and CLK files. <Time of Start> and <Time
ofEnd>definethedataprocessingdurationintheformatof
YYYY-MM-DD-HH-MM-SS.Moreover,thecombinationof
frequenciesappendedtothecommandcanspecifytherefer-
encecenteroftheorbitproduct,theconfigurablefrequencies
areshowninTable2.
TABLE2. ThefrequencychannelsofoutputtedB2b/HASDCB/OSB
products.
IV. ASSESSMENTOFTHEDECODEDB2bANDHAS
FIGURE2. PPP-B2borbitandclockerrorsfromDOY90-100in2025.
PRODUCTS
To demonstrate the correctness of the GKit-SSRDecoder,
in[31]tocalculatetheroot-mean-square(RMS)ofweighted
the decoded B2b and HAS products were comprehensively
averagedorbiterrorsandSISREconsideringthecorrelations
assessed. The raw B2b and HAS binary data used in the
betweenorbitandclockerrors.Fig.3showstheRMSvalues
experiment were sourced from Septentrio and China SINO
ofPPP-B2borbiterrors,clockerrors,andSISREfordifferent
receiversduringdayofyear(DOY)90-100in2025.Thefinal
satellites over a period of 11 days, and the corresponding
GNSS precise orbit and clock products provided by Wuhan
averaged statistics for BDS-3 and GPS constellations are
University(WUM)wereemployedasreferencestoevaluate
summarized in Table 3. The RMS of orbit and clock errors
the accuracy of the PPP-B2b and HAS orbit and clock cor-
for BDS-3 satellites are 0.075 m and 0.051 m, with the
rections. The performance of B2b/HAS real-time orbit and
IGSOsatellites(C38,C39,C40)showingsignificantlylarger
clock correction messages decoded by GKit-SSRDecoder
orbitalRMSvalues.Incomparison,theGPSsatellitesexhibit
was evaluated through the ‘‘SP3 Comparison’’ module in
a smaller orbit RMS of 0.054 m, but a larger clock RMS
BNCsoftware[30].
of 0.080 m compared with BDS-3. Overall, in terms of the
SISRE,BDS-3achievesasuperiorperformanceof0.086m,
A. EVALUATIONOFTHEACCURACYOFDECODEDB2B
outperformingthevaluesof0.093mforGPS.
PRODUCTS
Fig. 2 depicts the orbit (along-track, cross-track, and radial
components)andclockoffsetdifferencesofGPSandBDS- TABLE3. TheaverageRMSofGPS/BDS-3PPP-B2borbit,clock,andSISRE
errors(unit:m).
3 satellites between PPP-B2b and WUM. Most of the orbit
and clock errors of GPS satellites are within 0.5 m, and the
along-track component has the largest orbital errors while
the radial component exhibits significantly smaller errors.
Moreover,theGPSsatelliteclockerrorsaregenerallywithin TheDCBcorrectionsdecodedbyGKit-SSRDecodersoft-
0.25m.IntermsofBDS-3satellites,significantinstabilities ware are compared with the products from CAS. Notably,
areobservedinalong-trackandcross-trackcomponents,and the PPP-B2b service broadcasts DCB corrections for each
theorbiterrorsofthethreecomponentsarelargercompared frequencywithrespecttotheB3Isignal.Therefore,theOSB
tothoseofGPSsatellites.Incontrast,BDS-3satelliteclock values from the CAS products must be converted into dif-
errors are smaller, indicating higher stability than the orbit ferential values with respect to the B3I reference frequency
components. beforecomparison.Additionally,duetothedifferencesinthe
Whilemostexistingstudiesanalyze3Dorbiterrorsandthe referenceframes,thedifferencesforallsatellitesneedtobe
signal-in-spacerangingerror(SISRE)solelyfromastatistical adjustedbyremovingthemeanoffset.Fig.4summarizesthe
perspective, this study employs the methodology proposed mean difference and standard deviation (STD) of PPP-B2b
VOLUME14,2026 67921

<!-- PAGE: 5 -->

Z.Wuetal.:GKit-SSRDecoder:Open-SourceC/C++-BasedPPP-B2bandHASDecoding
TABLE4. TheaveragedifferenceandstandarddeviationofPPP-B2bcode
biases(unit:ns).
PPP-B2bdata[24],[25].ThedecodedBDS-3orbitandclock
products were compared against post-processed products,
and the results are illustrated in Fig. 5 and 6. It is evident
thattheclockproductsdecodedbybothmethodsexhibitno
significant difference. However, the three-dimensional orbit
errordecodedbythissoftwareisclosertozero,especiallyin
theradialdirection.ThestatisticalresultsinTable5indicate
that not considering the satellite-end APC correction will
resultinadeviationofmorethan1mintheradialdirection.
FIGURE3. RMSvaluesofPPP-B2borbit,clock,andSISREerrors.
codebiasesoveraperiodof11days,withthecorresponding
statistical value calculated in Table 4. The accuracy of the
BDS-3B2bsignalisthehighestamongallsignals,withmean
valuesof0.241nsand0.260nsforC7ZandC7Dchannels,
respectively.Moreover,theaccuracyoftheBDS-3B2asignal
is0.311nsand0.313nsforC5XandC5P,respectively,which
isalmostcomparablewiththeB2bsignal.Besides,theB1C
signalofBDS-3,withanaccuracyof0.424nsand0.419ns FIGURE5. PPP-B2borbitandclockerrorsonDOY91forGKit-SSRDecoder.
forC1XandC1D,presentsbetterperformancecomparedto
the B3I signal whose accuracy is 0.516 ns. In addition, the
standarddeviationofB1CcodebiasesisclosetothatofB2b
bothfallingwithintherangeof0.13nsto0.14ns.Meanwhile,
the B2a code biases show good stability over 11 days with
STDof0.090nsand0.074ns.
FIGURE6. PPP-B2borbitandclockerrorsonDOY91forCSSRlib.
TABLE5. TheaverageRMSofBDS-3PPP-B2borbiterrorsfordifferent
software(unit:m).
FIGURE4. MeandifferenceandstandarddeviationofPPP-B2bcode
B. EVALUATIONOFTHEACCURACYOFDECODEDHAS
biasesrelativetoCASproducts.
PRODUCTS
To verify the superiority of the proposed method over Similarly,the11-daythree-componentorbiterrorsandclock
existing approaches, the proposed GKit-SSRDecoder and offseterrorsofGPSandGalileosatellitesbetweenHASand
publishedCSSRlibwereemployedtodecodethesamesetof WUM are presented in Fig. 7. The orbit errors of GPS and
67922 VOLUME14,2026

<!-- PAGE: 6 -->

Z.Wuetal.:GKit-SSRDecoder:Open-SourceC/C++-BasedPPP-B2bandHASDecoding
GalileosatellitesinHASservicearegenerallywithin0.25m,
except that the differences for satellite G25 occasionally
exhibit relatively large fluctuations. The accuracy of orbit
radialcomponentevenreachesthecentimeterlevel,indicat-
ing an outstanding orbit accuracy of HAS GPS corrections.
Besides, the clock offset errors of both GPS and Galileo
satellites are mostly below 0.15 m, showing no significant
fluctuations.However,afewjumpsandspikesinclockerrors
areobservedparticularlyforGPSsatellites,whileHASclock
corrections for Galileo satellites exhibit significantly better
stabilitythanGPSsatellites.
FIGURE8. RMSvaluesofHASorbit,clock,andSISREerrors.
TABLE7. TheaveragedifferenceandstandarddeviationofHAScode
biases(unit:ns).
TABLE8. ProcessingstrategiesforHAS/B2bpositioningtest.
FIGURE7. HASorbitandclockerrorsfromDOY90toDOY100in2025.
After excluding epochs with significant jumps, the RMS
valuesofHASorbiterrors,clockerrors,andSISREfordiffer-
entsatellitesover11daysareconcludedinFig.8.Withinthe
sameconstellation,theRMSoforbitandclockoffseterrors
fordifferentsatellitesarerelativelyconsistent.TheGPSorbit
and clock offset accuracies are within 0.08 m except for
satelliteG25,andtheaccuracyofGalileosatellitesiswithin
0.06m.Thecorrespondingaveragevaluesaresummarizedin
TABLE9. The68thand90thpercentilesofconvergencetimeand
Table6,andtheRMSofGPSorbitandclockoffseterrorsare
positioningerrorsforPPP-B2binstaticsolutionwithallprocessed
0.044mand0.038m,whilethoseofGalileoare0.045mand stations.
0.023m,respectively.Overall,theSISREofGPSandGalileo
inHASserviceare0.057mand0.048m,respectively.
TABLE6. TheaverageRMSofGPS/GalileoHASorbit,clock,andSISRE
errors(unit:m).
The CAS products do not provide OSB correction for
the GPS C2P channel, therefore, CODE DCB correction
files in which P1P2 and P1C1 DCBs are provided are used
VOLUME14,2026 67923

<!-- PAGE: 7 -->

Z.Wuetal.:GKit-SSRDecoder:Open-SourceC/C++-BasedPPP-B2bandHASDecoding
FIGURE9. MeandifferenceandstandarddeviationofHAScodebiasesrelativetopost-processedproducts.
FIGURE10. GlobalsatellitedistributionforPPP-B2b(left)andHAS(right)services.
TABLE10. The68thand90thpercentilesofconvergencetimeand
positioningerrorsforHASinstaticsolutionwithallprocessedstations.
TABLE11. Real-timePPPPositioningPerformanceStatisticsinkinematic
vehicletests.
FIGURE11. DistributionofMGEXstationsusedforPPP-B2b(red)andHAS
(blue)servicespositioning.
C2PcorrectionsbroadcastedbyHASareusedasasubstitute
for C2W signal. The code biases of HAS service are in the
OSB format, the HAS DCBs are generated by differencing
OSBs. The mean difference and standard deviation of HAS
DCB over 11 days are illustrated in Fig. 9 and the corre-
FIGURE12. IllustrationandtrajectoriesoftheemployedGNSS/IMU
sponding statistical values are shown in Table 7. The dif-
equipmentsetup.
ferencesofC2L-C1CDCBsforGPSsatellitesare0.119ns,
outperformingtheC2P-C1CandC2W-C1CDCBaccuracies
instead,toevaluatethedecodedbiasproductsoftheGPSC2P whichare∼0.30ns.TheDCBdifferencesofGalileosatellites
channel. Furthermore, the HAS service does not broadcast in HAS service range from 0.094 ns to 0.101 ns, and the
C2W correction. Given that the current research primarily C6C-C1C combination has better performance than others.
employs GPS C1C/C2W dual-frequency observations, the The standard deviation of GPS DCB is lower than that of
67924 VOLUME14,2026

<!-- PAGE: 8 -->

Z.Wuetal.:GKit-SSRDecoder:Open-SourceC/C++-BasedPPP-B2bandHASDecoding
FIGURE13. ProbabilitydistributionofpseudorangeresidualsforHAS/PPP-B2bservicesatGAMGstation.
(bluedots)togetherwith20stationsdistributedintheAsia-
Pacific region (red triangles) from the multi-GNSS experi-
ment (MGEX) were selected to be processed for the static
experiment, as shown in Fig. 11. The data duration is
from DOY 90 to 100 in 2025 with a sampling rate of
30 s. Concurrently, one set of kinematic data with a sam-
pling rate of 1 s was collected in Xi’an, China, on 9th
September, 2025, to assess the performance of kinematic
PPP. As illustrated in Fig. 12, the employed equipment
setup consists of a multi-band GNSS antenna, a standby
antenna,andaMEMSIMU.Thevehicletraveledfor5262s
from UTC 01:30:54 to 02:58:42 in an open test area. The
lever arms between IMU and the GNSS antenna were pre-
ciselycalibratedbeforehand,andthereferencetrajectoryand
FIGURE14. StaticPPPpositioningerrorsattheGAMGstationfor attitude were calculated using a post-processing kinematic
PPP-B2bandHASservice. (PPK)/INS tightly-coupled algorithm using the well-known
commercial software Inertial Explorer (IE). All observa-
tions were processed with the dual-frequency ionosphere-
Galileo, indicating superior stability over several days for
free combination, and a forward Kalman filter was applied
GPSDCB.
to conduct RT-PPP. The precise ephemeris generated by
C. POSITIONINGPERFORMANCEVALIDATIONUSING theGKit-SSRDecodersoftwareisreferencedtothesatellite
DECODEDB2BANDHASPRODUCTS CoM, hence, the IGS14 ANTEX file and IGS 20 ANTEX
Fig. 10 shows the distribution of satellites providing cor- file are applied for HAS and B2b services, respectively.
rections by PPP-B2b and HAS services over one day, the Other detailed strategies are summarized in Table 8. The
PPP-B2bserviceprimarilycoversChinaanditssurrounding positioning experiment was conducted using an enhanced
regions(60◦Eto160◦E,0◦Nto80◦N),withupto20satellites versionofRTKLIB-b34jsoftware[32],whichsupportsdual-
available in China. The HAS service provides satellite cor- frequencyobservationwithdifferentfrequencycombinations
rectionsglobally,however,thenumberofavailablesatellites for multi-GNSS satellites. Additionally, the PPP software
differsacrosslatitudinalregionsduetoorbitalcharacteristics. incorporates the capability of utilizing OSB corrections.
Typically, around 20 satellites are available in high- and The static PPP experiment was reset at 3-hour intervals to
low-latitude areas while mid-latitude regions have about obtainmoreavailablesolutionperiodsforstatisticalanalysis,
15satellites.Theactualusablecountmaybelowerduetofac- i.e., a one-day 24-hour observation file was divided into
tors such as observation environment and satellite elevation eight 3-hour sub-files. The horizontal and vertical conver-
angle. gencetimesaredefinedasthedurationsrequiredtoachieve
To validate the positioning performance with decoded and maintain positioning errors below 20 cm and 40 cm,
HAS and B2b products, 70 globally distributed stations respectively.
VOLUME14,2026 67925

<!-- PAGE: 9 -->

Z.Wuetal.:GKit-SSRDecoder:Open-SourceC/C++-BasedPPP-B2bandHASDecoding
FIGURE15. AveragestaticPPPhorizontalandverticalperformanceatthe90thand68thpercentilesofPPP-B2bservicewithall
processedstations.
FIGURE16. AveragestaticPPPhorizontalandverticalperformanceatthe90thand68thpercentilesofHASservicewithallprocessedstations.
FIGURE17. Real-timekinematicPPPpositioningerrorsoftwoservicesin
avehicleexperiment. FIGURE18. Satellitenumber(top)andPDOP(bottom)fortwoservicesin
kinematicexperiment.
Properpseudorangebiascorrectionisacriticalfactorinflu-
encing PPP convergence performance [33], Fig. 13 exhibits the OSB product decoded by the GKit-SSRDecoder, the
the probability distribution of pseudorange residuals with pseudorange residuals of all frequencycombinations follow
differentfrequencycombinationsforHAS/PPP-B2bservices a zero-mean generalized normal distribution [34], demon-
at GAMG station over one day. With the corrections from strating the correctness of the code bias decoded from the
67926 VOLUME14,2026

<!-- PAGE: 10 -->

Z.Wuetal.:GKit-SSRDecoder:Open-SourceC/C++-BasedPPP-B2bandHASDecoding
GKit-SSRDecoder. For PPP-B2b service, the pseudorange due to the HPVRS decoding approach utilized in the HAS
residuals of BDS-3 B1C/B2a and B1C/B2b are within 2 m service.
and are smaller than the GPS L1/L2 and BDS-3 B1I/B3I.
With decoded HAS products, the pseudorange residuals of V. CONCLUSION
GalileosatellitesaresignificantlysmallerthanthoseofGPS ThisstudyintroducestheGKit-SSRDecoder,anopen-source
satellites, indicating the code bias corrections for Galileo C/C++ software designed to bridge the gap between raw
satellites are more accurate than those of GPS satellites. PPP-B2b/HASstreamsandstandardizedpositioningengines.
The static PPP positioning errors at the GAMG station Itprovidesanend-to-endsolutionfordecodingmulti-vendor
are presented in Fig. 14, following each initialization, both proprietary formats (e.g., Septentrio, NovAtel, SINO, Uni-
services consistently achieve convergence to decimeter and core) and generating RINEX-compliant precise products.
evencentimeter-levelaccuracy.Notably,thePPP-B2bservice Thesoftwaresupportsreal-timestreamingdecodingoforbit,
demonstrates a significantly faster convergence speed and clock, and bias corrections. It features customizable orbit
exhibitssuperiorstabilityinpositioningperformance. referencecenters(i.e.,CoM/APC)andstandardizedoutputto
The time series of average horizontal and vertical static facilitateseamlessintegrationintoexistingC/C++position-
positioning errors at the 90th and 68th percentiles for PPP- ing frameworks. The performance was rigorously evaluated
B2bserviceofallprocessedstationsareshowninFig.15,and using 11 days of Asia-Pacific region station data for PPP-
the corresponding convergence time and positioning errors B2bserviceandglobaldataforHASservice,supplemented
afterconvergenceareprovidedinTable9.Ittakes35.5min bykinematicvehicletests.
and20.0mintoconvergeinhorizontalandverticaldirections, ProductanalysisshowsthattheSISREofBDS-3andGPS
respectively,forthe90thpercentilepositioningerrorsofPPP- reach 0.086 m and 0.093 m for PPP-B2b service, 0.048 m
B2b.Meanwhile,thepositioningaccuracyreaches9.1cmand and0.057mfortheGalileoandGPSinHASservice,respec-
8.4cmafterconvergence.Incomparison,the68thpercentile tively.Besides,theprecisionofcodebiascorrectionisbetter
oftheconvergencetimeis16.5minand7.5mininhorizon- than 0.52 ns for PPP-B2b service and 0.25 ns for HAS
tal and vertical directions, with the positioning precision of service, with exceptional stability observed in BDS-3 and
6.9cmand5.7cm,respectively. Galileo products, which exhibit standard deviations of less
Similarly, Fig. 16 illustrates the time series of average than0.14nsand0.22ns,respectively.
horizontal and vertical static errors at the 90th and 68th StaticPPPtestsindicatethatthePPP-B2bserviceachieves
percentilesforHASservice.Thecorrespondingconvergence fasterconvergence,withthe90thpercentileconvergencetime
time and positioning errors after convergence are summa- of 35.5 min and 16.5 min for the horizontal and vertical
rized in Table 10. It can be noticed that 90% of HAS PPP components, respectively. In comparison, the HAS service
solutions need 62.0 min and 32.0 min to converge in hor- requires 62.0 min and 32.0 min to reach the same level.
izontal and vertical directions, respectively, while those of Regarding positioning accuracy after convergence, the 90th
the 68th percentile are 35.0 min and 12.0 min. After con- percentile for PPP-B2b reaches 9.1 cm horizontally and
vergence, the precision of the 68th percentile positioning 8.4 cm vertically, while the corresponding metrics for HAS
errors achieved centimeter-level with 6.4 cm and 8.1 cm in are11.1cmand13.1cm.Inkinematicvehicletests,PPP-B2b
horizontal and vertical directions, further demonstrating the demonstratessuperiorrobustnessduetotheincreasednumber
corrections decoded by GKit-SSRDecoder are correct and ofvisiblesatellites,yieldingRMSerrorsof0.13m,0.11m,
effective. and0.12mintheEast,North,andUpdirections,respectively.
The kinematic PPP positioning errors for both services TheseresultsconsistentlyoutperformtheHASservice,which
are illustrated in Fig. 15, alongside the overall positioning exhibitscorrespondingerrorsof0.18m,0.12m,and0.23m.
error RMS after 30 min as shown in Table 11. The PPP- Overall, the positioning performance of the Asia-Pacific-
B2b service achieves positioning RMS errors of 0.13 m, oriented PPP-B2b service significantly outperforms the
0.11 m, and 0.12 m in the East, North, and Up directions, globally-oriented HAS service. This superiority can be
respectively. These results are superior to the correspond- attributed to several critical factors: First, the HAS service
ing errors of 0.18 m, 0.12 m, and 0.23 m observed for is currently in its initial operational phase, leading to less
the HAS service. Moreover, the PPP-B2b service not only stable accuracy in its server-side products, as evidenced by
exhibitsfasterconvergencethanHASbutalsodemonstrates our comparative analysis between HAS and post-processed
superior positioning stability post-convergence. As further products. Second, the limited number of HAS monitoring
shown in Fig. 16, the HAS service utilizes fewer satellites stations globally restricts its ability to provide comprehen-
compared to PPP-B2b, leading to correspondingly higher sive tracking compared to the regional network supporting
Position Dilution of Precision (PDOP) values, which likely PPP-B2b. Finally, benefiting from the robust constellation
accounts for its degraded positioning performance. More- architecture of BDS-3, the satellite visibility and geometry
over,Table11comparesthedecodingtimeforbothservices intheAsia-PacificregionaresuperiortothoseoftheGalileo
over the same 86-minute period. The software decodes the system. As demonstrated in our kinematic experiments, the
PPP-B2b messages in just 2.649 s, whereas the HAS mes- increasednumberoftrackedsatellitessignificantlyenhances
sages take nearly half a minute. This efficiency disparity is user-sidepositioningperformanceandreliability.
VOLUME14,2026 67927

<!-- PAGE: 11 -->

Z.Wuetal.:GKit-SSRDecoder:Open-SourceC/C++-BasedPPP-B2bandHASDecoding
Despite its utility, GKit-SSRDecoder has several limita- [15] R.Zhang,R.Tu,J.Zhang,andX.Lu,‘‘Acomparativeinvestigationof
tions.First,thesoftware’scompatibilitywithdiversepropri- broadcastframeworks,serviceavailability,andtimetransferperformance
in PPP-b2b, HAS, and MADOCA-PPP,’’ IEEE Instrum. Meas. Mag.,
etary data formats is currently limited. Second, the current
vol.28,no.8,pp.61–69,Nov.2025.
implementation focuses exclusively on PPP-B2b and HAS [16] H. Namie and N. Kubo, ‘‘Performance evaluation of centimeter-level
servicesanddoesnotyetsupportotherregionalorcommer- augmentationpositioningL6-CLAS/MADOCAatthebeginningofofficial
operationofQZSS,’’IEEJJ.Ind.Appl.,vol.10,no.1,pp.27–35,2021.
cialSSRcorrections.Movingforward,weplantoexpandthe
[17] P.Zhou,Z.Zhang,Z.Liu,D.Lyu,G.Xiao,K.Xiao,andL.Du,‘‘Real-time
rangeofrawmanufacturerdataformatssupportedbythesoft- precisezenithtroposphericdelayestimationwithBDSPPP-b2b,Galileo
wareandincorporateadditionalhigh-precisionservices,such HAS,andQZSSMADOCA-PPPservices,’’IEEETrans.Geosci.Remote
Sens.,vol.62,pp.1–11,2024.
asCLASandMADOCA.Furthermore,weremaincommitted [18] D.Yi,N.Naciri,andS.Bisnath,‘‘SmartphoneGNSSlane-levelnavigation
to monitoring the evolving landscape of GNSS correction with Galileo HAS corrections and an iterative PPP algorithm,’’ IEEE
InternetThingsJ.,vol.12,no.12,pp.21130–21143,Jun.2025.
services, ensuring that the software’s functional capabilities
[19] J.Tao,G.Zhang,G.Chen,Y.Jiang,andQ.Zhao,‘‘Real-timeestimation
are promptly synchronized with the latest protocol updates ofmulti-frequencyphaseobservable-specificbiasfortheBDS3PPP-B2b
andserviceenhancements. service,’’GPSSolutions,vol.29,no.1,p.19,Jan.2025.
[20] Y.Ge,Q.Wang,Y.Wang,D.Lyu,X.Cao,F.Shen,andX.Meng,‘‘Anew
receiverclockmodeltoenhanceBDS-3real-timePPPtimetransferwith
ACKNOWLEDGMENT thePPP-B2bservice,’’Satell.Navigat.,vol.4,no.1,p.8,Dec.2023.
[21] K. Zheng, Z. Ye, J. Zhao, Q. Ma, W. Fu, J. Hu, K. Liu, L. Tang, and
The authors would like to thank Lewen Zhao, a Lecturer of
X.Zhang,‘‘Real-timePPPwiththefusionofGalileoHASandBDS-3
NanjingUniversityofInformationScienceandTechnology, PPP-B2b,’’Measurement,vol.257,Jan.2026,Art.no.118829.
forprovidingtherawPPP-B2b/HASdata. [22] O. Horst, M. Kirkko-Jaakkola, T. Malkamäki, S. Kaasalainen,
I.Fernández-Hernández, A. C. Moreno, and S. C. Díaz, ‘‘HASlib:
Anopen-sourcedecoderfortheGalileohighaccuracyservice,’’inProc.
REFERENCES IONGNSS+,Int.Tech.MeetingSatell.DivisionInst.Navigat.,Denver,
CO,USA,Oct.2022,pp.2625–2633.
[1] Y.Yang,Z.Yao,Y.Mao,T.Xu,andD.Wang,‘‘Resilientsatellite-based [23] D.Borio,M.Susi,andC.Gioia,‘‘GHASP:AGalileoHASparser,’’GPS
PNTsystemdesignandkeytechnologies,’’Sci.ChinaEarthSci.,vol.68, Solutions,vol.27,no.4,p.197,Oct.2023.
no.3,pp.669–682,2025. [24] L.Zhao,‘‘PythontoolboxforBDSPPP-B2bandGalileoHASdecoding
[2] P.Li,X.Jiang,X.Zhang,M.Ge,andH.Schuh,‘‘GPS+Galileo+BeiDou anditsproductsperformancevalidation,’’GPSSolutions,vol.29,no.2,
precisepointpositioningwithtriple-frequencyambiguityresolution,’’GPS p.83,Apr.2025.
Solut.,vol.24,no.3,pp.L07304–543,Jul.2020. [25] R. Hirokawa, A. Hauschild, and T. Everett, ‘‘Python toolkit for open
[3] O. Montenbruck, P. Steigenberger, L. Prange, Z. Deng, Q. Zhao, PPP/PPP-RTKservices,’’inProc.IONGNSS+,Int.Tech.MeetingSatell.
F.Perosanz, I. Romero, C. Noll, A. Stürze, G. Weber, R. Schmid, DivisionInst.Navigat.,Denver,CO,USA,Oct.2023,pp.2514–2526.
K.MacLeod,andS.Schaer,‘‘Themulti-GNSSexperiment(MGEX)of [26] R.Zhang,R.Tu,andX.Lu,‘‘HASPPP:Anopen-sourceGalileoHAS
theinternationalGNSSservice(IGS)–achievements,prospectsandchal- embeddableRTKLIBdecodingpackage,’’GPSSolutions,vol.28,no.4,
lenges,’’Adv.SpaceRes.,vol.59,no.7,pp.1671–1697,Apr.2017. p.169,Oct.2024.
[4] M.ElsobeieyandS.Al-Harbi,‘‘Performanceofreal-timeprecisepoint [27] N.Naciri,D.Yi,S.Bisnath,F.J.deBlas,andR.Capua,‘‘Assessmentof
positioningusingIGSreal-timeservice,’’GPSSolutions,vol.20,no.3, Galileohighaccuracyservice(HAS)testsignalsandpreliminaryposition-
pp.565–571,Jul.2016. ingperformance,’’GPSSolutions,vol.27,no.2,p.73,Apr.2023.
[28] GalileoHighAccuracyServiceSignal-in-SpaceInterfaceControlDocu-
[5] C.O.Yigit,M.Bezcioglu,V.Ilci,I.M.Ozulu,R.M.Alkan,A.A.Dindar,
ment(HASSISICD),EUSPA,Prague,CzechRepublic,2022.
and B. Karadeniz, ‘‘Assessment of real-time PPP with trimble RTX
[29] I.Fernández-Hernández,T.Senni,D.Borio,andG.Vecchione,‘‘High-
correctionserviceforreal-timedynamicdisplacementmonitoringbased
parityverticalReed–SolomoncodesforlongGNSShigh-accuracymes-
on high-rate GNSS observations,’’ Measurement, vol. 201, Sep. 2022,
sages,’’NAVIGATION,vol.67,no.2,pp.365–378,Jun.2020.
Art.no.111704.
[30] G.Weber,L.Mervart,S.Andrea,R.Axel,andD.Stcker,‘‘BKGNtrip
[6] StandardforNetworkedTransportofRTCMViaInternetProtocol(Ntrip) client(BNC)version2.12,’’TechnicalManual,FederalAgencyforCar-
Version2.0WithAmendment2,StandardRTCM10410.1,2021. tographyandGeodesy(BKG),Frankfurt,Germany,Tech.Rep.,2016.
[7] B.Li,H.Ge,Y.Bu,Y.Zheng,andL.Yuan,‘‘Comprehensiveassessment [31] O. Montenbruck, P. Steigenberger, and A. Hauschild, ‘‘Multi-GNSS
ofreal-timepreciseproductsfromIGSanalysiscenters,’’Satell.Navigat., signal-in-space range error assessment–methodology and results,’’ Adv.
vol.3,no.1,p.12,Dec.2022. SpaceRes.,vol.61,no.12,pp.3020–3038,Jun.2018.
[8] V.İlçiandA.U.Peker,‘‘Thekinematicperformanceofreal-timePPP [32] T.Takasu,‘‘RTKLIB:AnopensourceprogrampackageforGNSSposi-
servicesinchallengingenvironment,’’Measurement,vol.189,Feb.2022, tioning, ver. 2.4.2,’’ Tokyo Univ. Marine Sci. Technol., Tokyo, Japan,
Art.no.110434. Tech.Rep.,2013.
[9] Z.-X.LinandS.Jan,‘‘AnalysisofPPP-ARusingreal-timeproductinsub- [33] Z. Wu, Q. Wang, Z. Yu, C. Hu, H. Liu, and S. Han, ‘‘Modeling and
urbanenvironment,’’inProc.Int.Tech.MeetingInst.Navigat.,Jan.2024, performanceassessmentofprecisepointpositioningwithmulti-frequency
pp.840–845. GNSSsignals,’’Measurement,vol.201,Sep.2022,Art.no.111687.
[34] B. Shu, T. Lei, P. Li, L. Wang, G. Huang, S. Zhang, and Q. Zhang,
[10] X. Lu, L. Chen, N. Shen, L. Wang, Z. Jiao, and R. Chen, ‘‘Decoding
‘‘Calibrationofinconsistentreceiver-dependentpseudorangebiasandits
PPPcorrectionsfromBDSB2bsignalsusingasoftware-definedreceiver:
impact on wide-lane ambiguity fixing,’’ GPS Solutions, vol. 29, no. 2,
An initial performance evaluation,’’ IEEE Sensors J., vol. 21, no. 6,
p.64,Apr.2025.
pp.7871–7883,Mar.2021.
[11] GalileoHighAccuracyService(HAS)InfoNote,EUSPA,Prague,Czech
Republic,2020.
[12] T. Hadas, K. Kazmierski, I. Kudłacik, G. Marut, and S. Madraszek, ZHIYUAN WU is currently pursuing the Ph.D.
‘‘Galileohighaccuracyserviceinreal-timePNT,geoscienceandmonitor- degree with Chang’an University. His primary
ingapplications,’’IEEEGeosci.RemoteSens.Lett.,vol.21,pp.1–5,2024. researchfocusesonreal-timePPP.
[13] R.Hirokawa,I.Fernández-Hernández,andS.Reynolds,‘‘PPP/PPP-RTK
openformats:Overview,comparison,andproposalforaninteroperable
message,’’Navigation,vol.68,no.4,pp.759–778,Dec.2021.
[14] H. Zhou, W. Fu, L. Wang, T. Li, Y. Wu, R. Chen, and J. Li, ‘‘Multi-
frequency BDS-3 real-time positioning performance assessment using
new PPP-B2b augmentation service,’’ IEEE Sensors J., vol. 23, no. 5,
pp.4994–5002,Mar.2023.
67928 VOLUME14,2026

<!-- PAGE: 12 -->

Z.Wuetal.:GKit-SSRDecoder:Open-SourceC/C++-BasedPPP-B2bandHASDecoding
PANLIreceivedthePh.D.degreefromtheSchool YANG SUN is currently pursuing the master’s
of Geodesy and Geomatics, Wuhan University, degree with Chang’an University. His research
China,in2016.HeisaProfessoratChang’anUni- focusesonGNSS/LEORTK.
versity,China.Hiscurrentresearchfocusesmainly
on GNSS precise point positioning and precise
clockestimation.
JIAHUAN HU received the M.Sc. degree from BAO SHU received the Ph.D. degree from
WuhanUniversity,China,in2020,andthePh.D. the GNSS Research Center, Wuhan University,
degree from York University, Canada, in 2024. Wuhan,China,in2019.HeisanAssociatePro-
He is a Postdoctoral Fellow at The Hong Kong fessoratChang’anUniversity,Xi’an,China.His
Polytechnic University. His main research inter- research activities mainly include GNSS high-
ests are GNSS ambiguity resolution, PPP-RTK, precisionpositioningalgorithmsandapplications.
andsmartphoneprecisepositioning.
JINGKAI YUAN is currently pursuing the mas- BOBIN CUI received the Ph.D. degree from
ter’sdegreewithChang’anUniversity.Hismain Technische Universität Berlin, Berlin, Germany,
researchinterestsincludeGNSSsmartphoneposi- in 2023. He is a Lecturer at Chang’an Univer-
tioning. sity,Xi’an,China.Hisresearchactivitiesinclude
precisepointpositioning,real-timesatelliteclock
model,andapplication.
MINGBAO WEI is currently pursuing the mas- GUANWEN HUANG (Student Member, IEEE)
ter’sdegreewithChang’anUniversity.Hisprimary receivedthePh.D.degreeinsurveyingengineer-
research is GNSS precise positioning and iono- ing from Chang’an University, Xi’an, China, in
sphericmonitoring. 2012.HeisaProfessorofChang’anUniversity.
Hisresearchactivitiesincludeprecisepointposi-
tioningtheory,real-timesatelliteclockmodel,and
theirapplication.
VOLUME14,2026 67929