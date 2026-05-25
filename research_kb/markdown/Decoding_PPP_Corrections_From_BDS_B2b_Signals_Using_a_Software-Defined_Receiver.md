<!-- PAGE: 1 -->

IEEESENSORSJOURNAL,VOL.21,NO.6,MARCH15,2021 7871
Decoding PPP Corrections From BDS B2b
Signals Using a Software-Defined Receiver:
An Initial Performance Evaluation
XiangchenLu ,StudentMember,IEEE, Liang Chen ,SeniorMember,IEEE,
Nan Shen ,StudentMember,IEEE, LeiWang ,Member,IEEE,
ZhenhangJiao,StudentMember,IEEE, and RuizhiChen ,SeniorMember,IEEE
Abstract—With the rapid development of China’s BeiDou
NavigationSatelliteSystem(BDS),theapplicationofreal-time
precisepointpositioning(RTPPP)basedonBDShasbecome
an active research area in the field of Global Navigation
Satellite Systems (GNSS). BDS has provided the service of
broadcasting RTPPP information. It indicates that BDS has
become the second satellite system that provides RTPPP
services,followingGalileoamongtheGNSS,butworkbased
onthisdirectionhasyettobeexplored.Therefore,thispaper
evaluatestheperformanceofprecisepointpositioning(PPP)
service using a software-defined receiver (SDR). An exper-
iment was carried out to verify the feasibility of the SDR.
The PPP-B2b signal was processed to obtain PPP service
information, including orbit corrections, clock corrections, and differential code bias corrections. The time-varying
attributes of these corrections of BDS and GPS are evaluated,and the integrity and stability of the PPP service were
analyzed.TheresultsshowthePPP-B2bsignalcanstablyprovidePPPservicesforsatellitesintheAsia-Pacificregion,
includingcentimetertodecimeter-levelorbitcorrectionsandmeter-levelclockcorrectionsforBDSsatellites.Atthesame
time,PPPservicesprovidedecimetertometer-levelorbitcorrectionandmeter-levelclockcorrectionforGPSsatellites.
Finally, detection tip for bitstream availability in SDR is proposed. Some content which is not defined in the official
document,suchasthePPP-B2bframearrangement,variouscorrectionupdatecyclesandtheprogressofPPPservice
arediscussed.
IndexTerms—Real-timeprecisepointpositioning(RTPPP),BeiDouNavigationSatelliteSystem(BDS),signalprocess-
ing,software-definedreceiver(SDR).
I. INTRODUCTION with positioning, timing, wide-area differential and short
THE development of Chinese BeiDou navigation satellite message communication services. Since 2003, the third
system (BDS) can be divided into three steps. The BeiDou navigation experiment satellite was launched, further
first step was to construct the BeiDou Satellite Navigation enhancing the performance of the BeiDou Navigation
Demonstration System (BDS-1) [1]. Using an active Satellite Demonstration System [2]. The second step was
positioning scheme, the system provided users in China the construction of the BeiDou Satellite Navigation Regional
System(BDS-2).Inadditiontoatechnicalschemecompatible
with that of BDS-1, BDS-2 further included a passive
Manuscript received November 17, 2020; accepted
positioning scheme, and provided users in the Asia-Pacific
November 25, 2020. Date of publication December 2, 2020; date
of current version February 17, 2021. This work was supported in region with positioning, velocity measurement, timing, and
part by the National Key Research and Development Program under short message communication services [1]. By the end
Grant 2018YFB0505400, and in part by the Natural Science Fund
of 2012, a total of 14 satellites, including five Geostationary
of Hubei Province under Grant 2018CFA007. The associate editor
coordinating the review of this article and approving it for publication Earth Orbit (GEO) satellites, five Inclined GeoSynchronous
wasDr.YouLi.(Correspondingauthor:LiangChen.) Orbit (IGSO) satellites, and four Medium Earth Orbit
The authors are with the State Key Laboratory of Information
(MEO) satellites, had been launched to complete the space
EngineeringinSurveying,MappingandRemoteSensing,WuhanUni-
versity, Wuhan 430072, China (e-mail: 2018286190164@whu.edu.cn; constellation deployment [3]. The third step was to construct
l.chen@whu.edu.cn; nanshen@whu.edu.cn; lei.wang@whu.edu.cn; the BeiDou Satellite Navigation System (BDS-3) [1]. A total
2016286190128@whu.edu.cn;ruizhi.chen@whu.edu.cn).
of 19 satellites have been launched to complete a preliminary
DigitalObjectIdentifier10.1109/JSEN.2020.3041486
1558-1748©2020IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 2 -->

7872 IEEESENSORSJOURNAL,VOL.21,NO.6,MARCH15,2021
system for globalservice [4]. There are plans to complete the TABLEI
deployment of BDS-3 comprehensively with the launching STRUCTUREOFB2BSIGNAL
of30satellites by2020[3].OnJune29,2020,inorbittesting
andnetworkaccessevaluationofthe55thsatelliteofBDSwas
completed, which marks the formal establishment of BDS-3.
BDS-3 by inheriting the technical schemes of both active and
passive services, can provide global users with positioning,
navigation and timing, global short message communication,
andinternationalsearchandrescueservices.Atthesametime,
BDS-3addsregionalservicesforusersinChinaandsurround-
ing areas, including satellite-based augmentation, ground
augmentation and precise point positioning (PPP) services,
The main contributions of this paper are listed below:
etc [4], [5].
1) A complete SDR solution on decoding PPP service
Since the concept of Precise Point Positioning (PPP) was
information is proposed, and all the steps of SDR,
first proposed,it has been a hot research direction in the field
includingmodulesofacquisition,tracking,bitstreamand
of GNSS. However, the precise products that the PPP relies
PPP information extraction, are described in detail;
on often have a time delay. In order to meet the demand
2) A frame arrangementof completePPP service informa-
for real-time precise point positioning (RTPPP), the Interna-
tion is provided, through which the update interval of
tional GNSS Service (IGS) since 2013officially has provided
various PPP corrections can be obtained;
real-time precision products (RTS), which are estimated by
3) The clock and orbit corrections for BDS and GPS are
the analysis centers (ACs) [6]–[8]. The RTS are transmitted
compared and evaluated, and the integrity and stability
around the world using the network transmission of the Mar-
of the PPP service are analyzed.
itime Radio Technical Committee (RTCM) under the Internet
The paper is organized as follows: information about the
Protocol (Ntrip) [9]. In addition, several ACs, for exam-
PPP-B2b signal, including signal characteristics, encoding
ple, the German Aerospace Center (DLR), German Research
modulation, and navigation message structure, is introduced
Centre for Geosciences (GFZ), Federal Agency for Cartog-
in Section II. The design scheme and decodingprocessof the
raphy and Geodesy (BKG), and Centre National d’Etudes
SDR based on the B2b signal are presented in Section III.
Spatiales (CNES) also provide such corrections, which can
The experiments and results are presented next, followed
be accessed and processed via BKG NTRIP client (BNC) or
by a discussion of the optimization scheme in the decoding
real-time kinematic library (RTKLIB) software on the user
process and the characteristics of the PPP service, and the
side. With the rapiddevelopmentof BDS, BDS-based RTPPP
conclusions.
has been receiving more attention. Since the CNES became
the first organization to provide RTS for BDS satellites in
II. THE STRUCTURE OF PPP-B2B SIGNALS
November 2015, organizations such as GFZ and DLR have
AND PPP MESSAGE
also begun to release RTS for BDS satellites [10]–[13].
A.SignalStructure
In addition to the RTS provided by IGS, Galileo has been
The format of the PPP-B2b signal is given in the official
providing High Accuracy Services (HAS) for professional
BDS documents. As one of the BDS3 signals, the B2b signal
users at a positioning accuracy of 20 cm. HAS corrections
is broadcastby all BDS-3 satellites (MEO/IGSO/ GEO) with
will be disseminated through the Galileo E6-B signal on the
a center frequency of 1207.14 MHz and bandwidth of 20.46
1278.75MHz frequencybyMEO satellite. ThereceivedHAS
MHz. Table I shows the B2b signal structure and broadcast
corrections can be decoded with a success rate of 90% in an
content based on different satellite types [21].
occludedenvironment[14]–[17]. Japanese QZSS-L6D signals
As shown in Table I, the center frequency of 1207.14MHz
provide a Centimeter Level Augmentation Service (CLAS)
signal can be divided into B2b and PPP-B2b signals for
for Japanese mainland regions, covering GPS, QZSS, and
BDS-3.Bothsignalsonlybroadcastthein-phasecomponentI,
Galileo systems[18]. InAugust2020,BDS releasedthe PPP-
andtheirmodulationandsymbolratesarethesame.ButMEO
B2b document to provide RTPPP service. The joining of this
and IGSO satellites of the BDS-3 broadcasts the navigation
service announced that ordinary users of BDS can obtain
message for position service. The PPP service is provided
RTPPP service by receiving PPP-B2b signals only, without
by the first three GEO satellites on the BDS-3 system. The
RTCM or BNC.
influence of BPSK on the Gold code, PPP service data and
At present, the receiver for PPP-B2b signal processing
carrier of the PPP-B2b signal is shown in Fig. 1.
is not widely used, and the progress and performance of
As shown in Fig. 1, the PPP-B2b signal s (t) is gen-
PPP service provided by the PPP-B2b signal has not been B2b_I
erated by modulating the PPP service data D (t) and
evaluated.Tofillthisgap,wecarriedoutapreliminarystudyto B2b_I
the ranging code C (t). The mathematical expression of
exploreandanalyzethePPPservicebroadcastinthePPP-B2b B2b_I
s (t) is as follows [21]:
signal. The implementation of this work depends on the high B2b_I
flexibility and easy operation of a software-defined receiver 1
s (t)= √ D (t)·C (t) (1)
(SDR) [19], [20]. B2b_I 2 B2b_I B2b_I
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 3 -->

LUetal.:DECODINGPPPCORRECTIONSFROMBDSB2BSIGNALSUSINGASOFTWARE-DEFINEDRECEIVER 7873
Fig.1. InfluenceofBPSKmodulationonGoldcode,PPPservicedata,andB2bcarrier.
where t denoted that the signal is continuous in time.
D (t) is as follows [21]:
B2b_I
(cid:2)∞ (cid:3) (cid:4)
D (t)= d [k]p t −kT (2)
B2b_I B2b_I TB2b_I B2b_I
k=−∞
where k is the chip number of the corresponding data code;
d is the PPP service data code; T is the chip width
B2b_I B2b_I
of the correspondingdata code; p (t) is a rectangle pulse
TB2b_I
with width of T .
B2b_I
The mathematical expression of range code C (t) is as
B2b_I
follows [21]: Fig. 2. Frame structure and channel coding of PPP-B2b navigation
information.
(cid:2)∞ NB(cid:2)2b_I −1
C (t)= c [k]p TABLEII
B2b_I B2b_I Tc_B2b_I
DEFINEDMESSAGETYPES
n=−∞ k=0 (cid:3) (cid:3) (cid:4) (cid:4)
× t − N n+k T (3)
B2b_I c_B2b_I
where n is the number of the broadcasted ranging code;
N is the ranging code length with a value of 10230;
B2b_I
T = 1/R is the PPP-B2b chip period of the
c_B2b_I c_B2b_I
ranging code, and R = 10.23Mbps is the PPP-B2b_I
c_B2b_I
chipping rate; and p (t) is a rectangle pulse with a
Tc_B2b_I
duration of T [21]. Among them, 10 ranging codes are
c_B2b_I
defined for PPP-B2b. Each ranging code c [k] is obtained
B2b_I
by expandingthe Gold code that is generated by the modulo-
2 addition of the shifted output of the two 13-stage linear
feedback shift registers [21]. The introduction of this part is
tounderstandthesignalstructure.Thenextpartisthemessage
structure of PPP information,which is essential for extracting
PPP information. 24 bits of CRC. The specific contents of message data may
depend on the different type of Mestype, which is listed in
Table II. Currently,seven categories(Mestype 1-7) have been
B.PPPMessage
put into use and the remaining messages (Mestype 8-62) are
Each PPP message has a length of 486 bits, wherein the
reserved. The Null message (Mestype 63) are filled in the
highest6bitsindicatethemessagetype,thelowest24bitsare
blank time [21].
cycleredundancycheck(CRC),andtheremaining456bitsare
message data, as shown in Fig. 2.
As represented in Fig. 2, each PPP message has a length III. BDS SOFTWARE-DEFINED RECEIVER
of 486 bits and is encoded into 972 symbols through 64-ary SDR has a flexible open-architecture, which can be easily
Low Density Parity Check (64-ary LDPC). These symbols used to configure parameters to explore new system sig-
are concatenated together with 16 symbols of the preamble, nals[22].Inthissection,SDRisusedtodemodulatethePPP-
6 symbols for the PRN and 6 symbols for the reserved B2b signal. Fig. 3 shows the block diagram of the receiver,
flags to form one PPP-B2b navigation frame with the total which includes the acquisition module, tracking module, bit-
length of 1000 symbols. Each PPP message includes 6 bits streamdemodulationmoduleandB2b-PPPinformationextrac-
of message type (Mestype), 456 bits of message data and tion module. The whole method is described as follows.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 4 -->

7874 IEEESENSORSJOURNAL,VOL.21,NO.6,MARCH15,2021
Fig.3. BlockdiagramoftheSDRofthePPP-B2bsignal.
A.AcquisitionandTrackingModule
After the raw data is successfully collected by SDR,
the acquisition is carried out. The purpose of acquisition
in this work is to determine visible satellites of GEO and
calculatethecoarsevaluesofcarrierfrequencyandcodephase
of the PPP-B2b signals [23]. To this end, the collected raw
data are correlated with the local generated ranging code.
In principle, there are two methods on the correlation, i.e.
serial search acquisition in the time domain and the parallel
search acquisition in the frequency domain. By considering
the computing complexity, in this work, the parallel space
searchacquisitioninthefrequencydomainisapplied,inwhich
Fouriertransformisutilized to performa transformationfrom
the time domain into the frequency domain and the Doppler
frequency shift and code phase are searched in the frequency Fig.4. 64-aryLDPC(81,162)encodeprocess.
domain in parallel [20], [22], [23].
ItisworthmentioningthatPPP-B2bsignalsaretransmitted binary,i.e.,inthevalueof0001010001101111,whichisdue
by the BDS-3 GEO satellites, which are about 35786 km to the 180 ◦ phase shift in the code tracking loop. Naturally,
◦ ◦
away from the earth’s surface, and located at 80 E, 110.5 E, these two patterns can occur anywhere in the received data.
◦
and 140 E respectively [21]. Thus, the Doppler frequency So an additional check to authenticate the preamble must be
shift caused by GEO satellite movement is kept in a small carried out. Based on the design of every frame in the PPP-
range, and the maximum Doppler frequency shift can be B2b signal, the repeatedcheckon the occurrenceof preamble
about 1.46 Hz every 1 Km/h even if the receiver is in the in the bitstream from the tracking results is 1s (1000ms).
movingstate [24]. Therefore,the search range of the Doppler 2)LDPCEncodingandDecoding:When the beginning of
frequency shift in the acquisition module of PPP-B2b is set each frame is correctly detected with the assistance of the
within ± 1000 Hz, which accelerates the whole acquisition preamble information, the last 972 symbols of each frame is
time. the message sequence of PPP-B2b. After decoded by LDPC
The coarse value of the frequency Doppler shift and code (162,81),thePPPserviceinformationwithalengthof486bits
phaseisthenbytheacquisitionmoduleisputintothetracking can be extracted. The LDPC (162,81)encoding and decoding
module. The classic delay locked loop and phase locked loop processes are introduced as follows.
isfurtherusedtopreciselytrackthephaseofcarrierfrequency EachframeofthePPP-B2bnavigationmessagebeforeerror
and the ranging code. After the convergence of the tracking correctionencodinghasa lengthof 486bits andthe encoding
loops,thephaseerrorsandcodeerrorsarekeptwithinasmall schemeadopts64-aryLDPC(162,81).Each(cid:3)cod(cid:4)ewordsymbol
range [20], [22], [25]. The data demodulation is then carried is composed of 6 bits and defined in GF 26 domain with
out. a primitive polynomial of p(x) = 1 + x + x6. A vector
representation (MSB first) is used to describe the mapping
B.BitstreamDemodulationModule relationshipbetweennon-binarysymbolsandbinarybits[19].
In order to decode PPP service information correctly, three Thus486bitswillbeconvertedinto81codewords.Thecheck
steps are carried out, i.e., preamble searching 64-ary LDPC matrixis aspar(cid:3)se m(cid:4)atrixH 81,162 of81rowsand162columns
decoding and CRC. The methods are presented as follows: defined in GF 26 domain with a primitive polynomial of
1)PreambleSearching:The purposeof preamblesearching p(x) = 1 + x + x6. It can be generated by the index
is to find the start of the PPP-B2b message. In PPP-B2b, matrix H 81,162,index and element matrix H 81,162,element . The
preamble is the synchronization head designed as a fixed subsequent encoding steps are shown in Fig. 4.
16bitsuniquewordwiththevalueof0xEB90inhexadecimal As shown in Fig. 4, the generator matrix G can be calcu-
(i.e.,1110101110010000inbinary).Thepreamble.Itshould lated by the sparse matrix H 81,162 . By using generator matrix
be noted that, the preamble may occur in an inverse code in G,theinputsequencemwithalengthof81canbeencodedto
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 5 -->

LUetal.:DECODINGPPPCORRECTIONSFROMBDSB2BSIGNALSUSINGASOFTWARE-DEFINEDRECEIVER 7875
obtain the codeword sequence with a length of 162. Finally, Algorithm 1 Decoding Algorithm: The Extended Min-Sum
each codeword can be reconstructed back to 6 bits and the Decoding Algorithm
result will be converted into the navigation symbol sequence Input: 972 symbols PPP data sequence, the parity-check
with a total length of 972 bits [21]. matrix H
The codeword sequence encoded by LDPC (162,81) are Output: 486 bits PPP data sequence
denoted as: Initialize: set the maximum number of iterations as itr ,
max
c =(c 0 ,c 1 ,...,c n−1 ), 0≤n<162 (4) itr = 0.
1: do
After the modulated codeword sequence is transmitted
2: calculatereliabilityvectorL by972symbolsPPP data
j
through the signal channel, the receiver can get the corre-
sequence
sponding sequence y as follow:
3: repeateach variable node VN then
j
y=(y 0 ,y 1 ,...,y n−1 ) (5) 4: calculate the decision symbols cˆ j and the reliability
vector V2C
where y j = (y j,0 ,y j,1 ,...,y j,r−1 ) is the received 5: untilmeeting the variable node updating rules
inf(cid:3)ormation corresponding to(cid:4) the jth codeword 6: calculate the check sum s=cˆHT
c j c j ∈ GF(2r),r =6,0≤j<n . The parity-check matrix 7: end do
H of the 64-ary LDPC (162,81) code can be used to check 8: if s=0 then
the correctness of the received sequence y. the specific 9: return the decision symbols cˆ as output
j
meth(cid:3)od is described(cid:4)as follows: A hard decision codeword 10: end if
cˆ = cˆ 0 ,cˆ 1 ,...,cˆ n−1 is obtained by making a hard decision 11: itr = itr+1
on the received sequence y bit by bit. The check sum is 12: repeat
calculated as s = cˆHT. If s = 0, cˆ is outputs as the correct 13: if itr =itr then
max
decoding result, otherwise cˆ is erroneous [21]. 14: declare decoding failed
The parity-checkmatrix H denotesthe connectionrelation- 15: end if
shipbetweenthechecknode(CN)andthevariablenode(VN),
16: repeateach check node CN then
i
i.e., the reliability informationcan be transmitted between the 17: calculate the reliability vector C2V
connected CN and VN. The implementation of the reliabil- 18: untilmeeting the check node updating rule
ity transmitting decoding algorithm can correct the received 19: repeateach variable node VN then
j
sequence y to estimated the transmitted codeword cˆ. BeiDou 20: calculate the decision symbols cˆ and the reliability
j
officialdocumentsprovidetwoiterativereliabilitytransmitting vector V2C
decoding algorithms: (1) Extended Min-Sum Method; (2) 21: until meeting the variable node updating rules
Fixed Path Decoding Method. In this module, the Extended 22: calculate the check sum s=cˆHT
Min-Sum Method is used to estimate the transmission code- 23: itr = itr+1
word cˆ. The extended minimum sum decoding algorithm is 24: until s=0 return the decision symbols cˆ as output
j
described as follows [21]:
The updating rule of variable nodes and check nodes, and By dividing decoded sequences with the generator
the specific calculation method involved in the above algo- polynomial g(x), the residue should be all “0”. However,
rithmscanrefertothePPP-B2bsignalofficialdocument[21]. due to the channel effect on signal transmission, there might
3)CRC: After the 64-ary LDPC (162,81) decoding, be errors in the decoded sequence. Therefore, the results of
the CRC will be processed. The CRC check is performed by CRC can be used to determine whether the decode sequence
bit for the 6 bits message type and the 456bits message data. is correct or not.
Thelowest24bitsareCRC code,asshowninthe upperlayer
of Fig. 2.
C.PPPInformationExtractionModule
The implementationof CRC is CRC-24Q and its generator
After LDPC decoding and CRC, the PPP service informa-
polynomial is [26]:
tion can be extracted. The PPP service information mainly
(cid:2)24
includesinformationcontentsuchassatelliteorbitcorrections,
g(x)= g xi (6)
i differentialcodebias,andsatelliteclockcorrections.Asstated
i=0 in Section II-B, different information content is indicated by
where, different message types. Before the PPP service information
(cid:5)
canbeeffectivelyappliedtothereceiver,differentinformation
1, i =0,1,3,4,5,6,7,10,11,14,17,18,23,24
g = content has to be matched first based on the information of a
i 0, else
group of Issue of Data (IOD). For details of the IODs, please
Furthermore, g(x) can be expressed as follows [26]: refer to BeiDou official documents [21].
g(x)=(1+x)p(x) (7)
IV. EXPERIMENT AND RESULTS
where, p(x)=x23+x17+x13+x12+x11+x9+x8+x7+ To verify the feasibility of the PPP-B2b SDR designed in
x5+x3+1. Section III, and to explore the characteristics of the PPP-B2b
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 6 -->

7876 IEEESENSORSJOURNAL,VOL.21,NO.6,MARCH15,2021
TABLEIII
THEPARAMETERSOFCONFIGURATIONDURINGTHEDATACOLLECTION
TABLEIV
THECODEPHASEANDDOPPLERFREQUENCYSHIFTOFTHEACQUIREDSATELLITE
Fig.5. Thetestingscenarioandtestbenchoftheexperiment.(a)TheGNSSantennaandcollectionworkbenchwerearrangedontheroofofthe
buildingofWuhanUniversity.(b)Thedetailofthecollectionworkbench.Theworkbenchismainlycomposedoftwoparts:Labsat3widebandand
laptop.ThelaptopisusedtoconfiguretheparametersofLabsat3wideband.
signal,thefieldtestswerecarriedoutontheroofofabuilding of PPP-B2b, which is from the GEO, is much smaller than
on the campus of Wuhan University on September 8, 2020. thatfromthe BeiDouB1C andGPSL1 C/A, whichare either
from MEO or IGSO.
A.FieldExperiment Fig. 6 shows the tracking results of PPP-B2b signals from
PRN59.From Fig. 6(a), it is observed that, the signal power
The testing scenario and test bench are shown in Fig. 5.
is mainly concentratedin the I phase, while the Q phase only
AsshowninFig. 5(a),anopenenvironmentisselectedforthe
contains the noise, which is consistent with the theoretical
signal collection to avoid the multipath impact. In Fig. 5(b),
design [20]. Fig. 6(b) shows the bitstream from I phase and
the raw data is recorded by LabSat 3 wideband, which is a
the data transmission rate of the bitstream is 1000 sps.
radio frequency (RF) signal recording and playback system.
In LabSat 3 wideband, the supported frequency varies from
1.2 GHz to 1.6 GHz, the sampling rate from 10 MHz to C.BitstreamDemodulationResults
58 MHz and the quantization precision ranges from 1, 2 to
Fig. 7 shows the correlation results of the preamble
3-bitinIandQdigitalsignal.Inthisfieldtest, theparameters
search.Wecanfindthatthereare4synchronousheadswiththe
of receiver are configured in Table III.
correlationpeakvalueof16,andbycalculation,theirintervals
areall1000ms,whichsuggeststhesuccessfuldetectionofthe
B.ResultsofAcquisitionandTracking start of the frame.
Inthetest,thesatelliteswithPRNsof19,21,22,34,35,39, Fig. 8 shows the results of the LDPC decoding and CRC
40, and 44 were acquired using the B1C signal, the satellites from 100 frame sequence, in which, the number of the frame
with PRNs of 59, 60, and 61 are acquired by B2b signal and sequence vs. the iteration times of the LDPC decoding is
the satellites with PRNs of 2, 5, 6, 12, 13, 15, and 29 by the plotted.
L1 C/A signal. The code phase and Doppler frequency shift As shown in Fig. 8, in the 100 frames of data, most of the
of the acquired satellites of BDS3 and GPS are presented in framespassedtheCRC aftertheLDPCdecodingwith1itera-
Table IV. As is clear, in general, the Doppler frequency shift tion. In only three cases, the number of iterations reaches the
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 7 -->

LUetal.:DECODINGPPPCORRECTIONSFROMBDSB2BSIGNALSUSINGASOFTWARE-DEFINEDRECEIVER 7877
Fig.6. TrackingresultsofPRN59(PPP-B2b).(a)ThepowerdistributionofIandQphaseoftrackingresults.(b)ThebitstreamfromIphase.The
transmissionrateofthebitstreamis1000sps.
D.ArrangementofFrameType
The length of each frame message is 486 bits, of which
the first 6 bits are the message type of the frame. However,
the BeiDou official documentdoes not mention the repetition
period of each frame and the frame arrangement of a set of
PPP service messages, so we output the highest 6-bit frame
message type, and the results are shown in Fig. 9.
Fig. 9 shows the frame arrange of the epoch moment from
17998 to 18046. After message type 1 has been broadcast,
message type 4 and message type 3 are broadcast alternately,
and informationtype 4 is broadcastcontinuously.When mes-
sage type 3 has been broadcast for one round, message type
2 is added. When the message type 2 has been broadcast for
one round, the message type 63 is broadcast in the remaining
Fig. 7. Correlation between 4000ms message sequence and 16-bit time. By summarizing the results of many times, we have
preamble(thepeakvalueindicatesthestartpositionoftheframe). defined a set of PPP-B2b frame format as follows:
1) Taking the time of message type 1 as the starting posi-
tion of a complete PPP service information, the broad-
cast period is 48 s;
2) Theremaining47sbroadcastmessagetypesare2,3,4,
63 (and the defined message types 5, 6 and 7 have not
yet appeared in the measured data);
3) The duration of the remaining 47 s broadcast message
type can be regarded as 3 s as an output unit, there are
15 times, and the 16th time is 2 s;
4) Message type 4 is regarded as one output type, and
another output type is composed of message types 2,
3and63.Thetwooutputtypesarealternatelybroadcast
in one output unit;
5) Messagetype4iscontinuouslybroadcast,andtheepoch
is constantly updated;
Fig. 8. The results of 64-ary LDPC(162,81) decoding and CRC
of100framedata. 6) Message types 2 and 3 are only broadcast once in a set
of PPP information, and the corresponding output unit
maximum number of iterations, two of which fail to pass the broadcastmessage type 63at the remainingtime fills in
CRCduetotheerroneousdecodeddata.Thecorrectlydecoded theblankposition,andthemessagetype63isbroadcast
framedatasequencesarethenprocessedtoextractPPPservice in the last 2 s.
information.However,itisunfortunatethat,thecurrentversion In addition, when extracting PPP information, we found that
of the PPP-B2b space interface document has not described the update time and corresponding epoch of corrections of
the design of a complete set of PPP information frame struc- PPP-B2b signals are different. Their first epoch moment is
tures. In this work, we summarize the frame layout format the same as the epoch moment of message type 1, and the
from measurement data in the field tests in the following update rate of the epoch moment of corresponding message
sections. type 4 is also 6 s. Message types 2 and 3 use the same epoch
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 8 -->

7878 IEEESENSORSJOURNAL,VOL.21,NO.6,MARCH15,2021
Fig.9. Framearrangementstructure.
Fig.10. ThePRNanddurationofBDS3satelliteswithvalidcorrections.
momentbutare7sslowerthantheepochmomentofmessage effectivecorrectionsare analyzed.Fig. 12 shows the effective
type 1, and their update rate is 48 s. The decoding results of orbit corrections of BDS-B1C satellites, with a time range of
PPP service information will be shown in the next. about 65 mins.
As shown in Fig. 12, we found that the orbit corrections
E.DecodingResultsofPPPServiceInformation of BDS satellites are in the range of centimeter to decimeter.
To obtain the PPP service information, the digital signal From the epoch moment of view, when the BDS3-B1C
data were processedaccordingto the proposedmethodin this navigation message is updated, that is, epoch moment
experiment. It was found that the satellites mask provided equal to 18000, the PPP-B2b service information will be
by the message type 1 in the PPP-B2b service information updated immediately. At that moment, most of the satellite
includes all satellites of BDS3 and GPS, that is, the satellites orbit corrections (radial, along and cross) have different
of BDS3 and GPS corresponding masks are all set to “1”. degrees of step-change rather than continuity. In a complete
However, due to the corrections of some satellites are larger epoch moment range, that is, the epoch moment is from
than the effectivevalue set by the document,their corrections 18000to21549,thechangesoforbitcorrectionsarerelatively
are unavailable. The duration of PPP service information continuous. From the satellite type, there is no significant
providing effective correction for BeiDou satellites (BDS3) difference between the corrections of MEO and IGSO. But
is shown in Fig. 10. The PPP service information is provided we found that the standard deviation of the radial direction
by the GEO satellites (PRN-59 and PRN-60). of MEO satellites are far less than that of the along and cross
FromFig. 10wefoundthatthePRNofsatelliteswitheffec- direction, and the standard deviation of IGSO satellites are
tivecorrectionsareconsistentwiththePRNofsatellitesinthe similar, but the differences are not as significant as that of
Asia-Pacific region at the moment, that is, they are similar to MEO satellites. Fig. 13 shows the effective orbit corrections
the PRN of satellites in the results of the acquisition module. of GPS satellites, with a time range of about 65 mins.
Fig. 11 shows the duration of the PPP service information From the comparison of Fig. 13 and Fig. 12, it can be
served for the satellites of GPS. found that the change of orbit correctionsof GPS satellites is
As shown in Fig. 11, the PPP service provided for GPS different from that of BDS, and the changes are smooth and
is similar to the PPP service provided for BDS. In addition, continuouswithoutstepchangeswhenthenavigationmessage
the PPP service information provided by PRN-59 satellite is is updated. The orbit corrections of GPS satellites are much
the same as that provided by PRN-60 satellite. Next, these greaterthantheBDScorrection.TheorbitcorrectionsofGPS
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 9 -->

LUetal.:DECODINGPPPCORRECTIONSFROMBDSB2BSIGNALSUSINGASOFTWARE-DEFINEDRECEIVER 7879
Fig.11. ThePRNanddurationofGPSsatelliteswithvalidcorrections.
Fig.12. Changesinorbitcorrections(radial,along,cross)ofBDS3BIC. Fig.13. Changesinorbitcorrections(radial,along,cross)ofGPSL1.
Thereareseven BDS3 satelliteswithorbitcorrections,and theepoch There are five GPS satellites with orbit corrections, and the epoch is
isfrom17710to 21549.Top:crossorbitcorrection, middle:alongorbit from 17710 to 21549. Top: cross orbit correction, middle: along orbit
correction,bottom:radialorbitcorrection. correction,bottom:radialorbitcorrection.
Fig. 15 shows the clock correction of GPS satellites over
satellitesareintherangeofdecimetertometer,whichismuch the entire epoch. The clock corrections are in the range
larger than that of BDS satellites. of decimeter to meter level. For the changes in the clock
InFig. 14,theclockcorrectionsandtheirstandarddeviation correction of satellites, three obvious situations are different
ofeachBDSsatellite overacompleteepochrangeareshown. from those of BDS satellites in Fig. 15. It can be seen that
FromFig. 14,wecanknowthattheclockcorrectionofalmost whenthenavigationmessagechanges,thereisnostep-change
allBDSsatellites iswithinthe meterrange.Forthechangeof in clock correction. The changes in the clock corrections of
clock corrections, when the BDS3-B1C navigation message the satellites are consistent during the entire period, which is
is updated, the clock correction of most satellites also has reflected from their standard deviation. In addition, we found
a step change to varying degrees. But in a complete epoch, that the corrections of PRN-5 are all “0” in some periods.
the clock correction changes of each satellite are very small The reason for this situation may be that the clock correction
reflected from their standard deviation, and their changes are istoocloseto“0”,resultinginaninsufficientnumberofbitsto
inconsistent. express it. The differential code bias provided by PPP-B2b is
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 10 -->

7880 IEEESENSORSJOURNAL,VOL.21,NO.6,MARCH15,2021
Fig.14. ChangesinclockcorrectionsofBDS3satellites.TherearesevenBDS3 satelliteswithclockoffsetcorrections,andthe epochisfrom
17710to21549.ThePRNofsatelliteinFig.14.correspondtothoseintheFig.12.
Fig.15. ChangesinclockcorrectionsofGPSsatellites.TherearefiveGPSsatelliteswithclockoffsetcorrections,andtheepochisfrom17710to
21549.ThePRNofsatelliteinFig.15.correspondtothoseintheFig.13.
the pseudo-range code biases between the ranging signal and than 99%. Only PRN-29 and 40 of BDS3 have slightly worse
the clock offset reference signal adopted by the correspond- completeness of clock correction and orbit correction than
ing system. Users need to correct the differential code bias other satellites. The main reason for this situation is that the
accordingly when they are using the signals other than the PPP service information of the two satellites is discontinuous
reference signal, otherwise, the convergence time of precise in time, and the orbit correction exceeds the effective range.
point positioning may be affected [21]. Refer to the PPP-B2b We treat it as a service exception. The PPP services of
signal interface document to check the specific content of the two satellites stopped broadcasting when the epoch time
the signal component corresponding to the differential code was 18525 and 21357, respectively. Therefore, we believe
bias and the signal-receiving mode of that component [21]. that when PPP-B2b stops serving a satellite, its PPP service
Among them, PPP-B2b service only provides the differential information will be unstable. Users who using RTPPP may
code bias of BDS3-B1C, the corresponding model including need to prepare to stop the positioning results of the satellite
0,1,2,4,5,7,8,12. During this epoch, the signal and tracking as soon as possible to prevent the impact on the RTPPP
mode and corresponding corrections have no change. results. In addition, the clock correctionsof all satellites have
anomalies of different durations. There are two abnormal
F.IntegrityofPPPServiceInformation situations.Inmostsituations,thecorrectioninformationisnot
Finally, we found that the remaining satellites, which have updated, that is, the epoch of the frame is still the epoch of
not matched the complete PPP service, often have some the previous frame.
cases of unavailable correctionsor data duplication, as shown Thecontentofthenextframeisbroadcastasusual,andthe
in Fig. 11 and Fig. 12. The situation that the epoch time interval between the two epochs is 12 s. Another situation is
broadcasted by the GEO satellite has not been updated due thattheclockcorrectionexceedstheeffectiverange.However,
to its own clock problem. We classified the above-mentioned clock correction has the characteristics of fast update speed
problems as abnormal problems of the GEO satellite PPP and small changes. The user can choose to continue using
service. We analyzed the PPP service performance of two the clock correction of the previous frame until a new clock
satellites GEO (PRN-59) during the collection period. The correction is extracted.
detailed results are shown in Table V. In general, the PPP information service provided by the
From the results in Table V, we find that the completeness PPP-B2b signal is very stable. At the same time, it has
of the orbitcorrectionofalmostall satellites can reach100%, established PPP services for BDS3 and GPS, with the char-
and the completeness of the clock correction can reach more acteristics of the short broadcast cycle and fast update rate.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 11 -->

LUetal.:DECODINGPPPCORRECTIONSFROMBDSB2BSIGNALSUSINGASOFTWARE-DEFINEDRECEIVER 7881
TABLEV
THEPARAMETERSOFCONFIGURATIONDURINGTHEDATACOLLECTION
It is also possible to use the PPP information of three GEO accordingly, that is, the sum of it and the satellite num-
satellites to check each other without excessively relying on ber (PRN) obtained by the acquisition module should be 63.
one satellite. In addition, we found that when the synchronization head
detectionis correctforthe realsignal data, the decodedresult
V. DISCUSSIONS isstillunusable.Accordingtotheabovesituation,bydetecting
Inthissection,thetipthatcanbeoptimizedinthedecoding the 6-bit satellite number (PRN), whether it matches the
process are discussed. To accelerate decoding progress, this satellite number (PRN) obtained by the acquisition module,
tip can predictthe sequenceswith decodingerror.Inaddition, or matching after flipping. If both conditions do not match,
some rules on broadcasting the PPP service information are itmeansthatthecorrectionsextractedbythissequencecannot
analyzed and summarized through experiments. One part has be used. The problemmay be caused by the trackingmodule.
been explained in Section IV, and the other parts will be Inordertoreducetheoccupationofcomputingresources,this
discussed in this section. sequence can be deleted.
A.OptimizationofTheDecodingProcess B.ProgressofPPP-B2b
As mentioned in Section III, after finding the starting posi- We have summarized some contents that were not clearly
tion corresponding to the synchronization head, their interval definedinthePPP-B2bofficialdocumentbytheBDS,includ-
is used as the other evidence for judging the synchronization ingtheprogressofPPP-B2bservicefortheGNSSsystemand
head. From the perspective of bit information arrangement, some other characteristic (as of September 8, 2020).
the last 6 after the preamble can be converted into satellite 1) ThePPP-B2bsignalhasprovidedreal-timePPPservices
number (PRN), as shown in Fig. 2. It corresponds to the for the two GNSS systems, BDS3 and GPS.
acquired ranging code number. It can be used as a secondary 2) Sincethe messagetype1 providessatellitesmask infor-
check to find the correctness of the synchronization head. mation, the message type 1 appears as a complete set
Therefore, the method of finding the starting position of of PPP service information broadcast time unit, with a
the frame includes a preliminary determination determining total duration of 48 s, that is, the broadcast duration of
that the interval between two consecutive maximum corre- a complete set of PPP service information is 48 s.
lation values is 1s as a preliminary determination. And a 3) The PPP-B2b signal currently only provides PPP ser-
seconddeterminationthatwhetherthe satellite number(PRN) vices to satellites acquired by BDS3-B1C and GPS
extracted by the symbol sequence should be consistent with signals covering the Asia-Pacific region. That is, which
thesatellitenumber(PRN)obtainedbytheacquisitionmodule. satellites (BDS3 and GPS) the user can acquire in the
If the synchronization head is the inverse code, the satellite Asia-Pacific regioncan receive their correspondingPPP
number extracted by the symbol sequence is also inverted service.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 12 -->

7882 IEEESENSORSJOURNAL,VOL.21,NO.6,MARCH15,2021
4) The PPP service informationis broadcastby the BDS3- [9] H. Gebhard and G. Weber, “NTRIP: Networked transport of RTCM
GEO satellites, PRN is 59, 60, and 61 respectively.The via Internet protocol—Internet radio technology for real-time GNSS
purposes,” in Proc. AGU Fall Meeting, Washington, DC, USA,
three satellites jointly broadcast the same PPP service
Dec.2003,pp.1–2.
information. [10] Y. S. Shi, J. M. Hao, W. P. Liu, B. Jiao, H. Zhang, and B. F. Song,
5) When the collection conditions are limited, users can “Performance assessment of BDS real-time precise point positioning
based on SSR corrections,” J. Surv. Eng., vol. 145, no. 4, 2019,
check and splice the PPP service information obtained
Art.no.05019003.
by the three GEO satellites to restore the complete PPP [11] W. Liang, Z. S. Li, M. R. Ge, F. Neitzel, X. M. Wang, and H. Yuan,
service information. “Investigation of the performance of real-time BDS-only precise point
positioning using the IGS real-time service,” GPS Solutions, vol. 23,
6) The currently designed useful message types are 1-7.
no.3,p.66,May2019.
In actual situations, users can only receive message [12] R. Fang, C. Shi, W. Song, G. Wang, and J. Liu, “Determination of
type 1-4. earthquake magnitude using GPS displacement waveforms from real-
time precise point positioning,” Geophys. J. Int., vol. 196, no. 1,
7) Currently, the differential code bias corrections from
pp.461–472,Jan.2014,doi:10.1093/gji/ggt378.
message type 4 only provide services for BDS3 satel- [13] Z. Li, J. Zhang, T. Li, X. He, and M. Wu, “Analysis of static and
lites. dynamicreal-timeprecisepointpositioningandprecisionbasedonSSR
correction,” in Proc. IEEE Int. Conf. Inf. Autom. (ICIA), Aug. 2016,
8) The epochs of various PPP service corrections are
pp.2022–2027,doi:10.1109/ICInfA.2016.7832151.
10-20 s slower than that of B1C navigation message. [14] L. Chen et al., “Robustness, security and privacy in location-based
servicesforfutureIoT:Asurvey,”IEEEAccess,vol.5,pp.8956–8977,
VI. CONCLUSIONS AND FUTURE WORKS 2017.
ThispaperaimsatacquiringPPPservicesinformationfrom [15] E. Göhler, I. Krol, M. Bodenbach, J. Winkel, G. Seco-Granados,
andI.Fernandez-Hernandez, “A galileo E6-B/Creceiver: Signals, pro-
PPP-B2b signal. A PPP-B2b SDR is implemented, which
totype, tests andperformance,” in Proc.29thInt.Tech.Meeting Satell.
includes the acquisition and tracking module, the bitstream DivisionInst.Navigat. (IONGNSS+),Nov.2016,pp.486–496.
decoding module, and the PPP service information extraction [16] D.Borio,T.Senni,andI.Fernandez-Hernandez,“Experimentalanalysis
of a candidate galileo E6-B data dissemination scheme,” in Proc. Int.
module. To verify the feasibility of SDR, field experiments
Tech.Meeting Inst.Navigat., Feb.2020,pp.509–520.
are carried out, in which, the time-varying attributes of the [17] I. Fernandez-Hernandez et al., “Testing GNSS high accuracy and
corrections of BDS and GPS are evaluated, and the integrity authentication–Galileo’s commercial service,” in Proc. Inside GNSS,
Jan./Feb.2015,pp.38–48.
and stability of the PPP information service were analyzed.
[18] T. C. Office and G. O. Japan, Quasi-Zenith Satellite System Interface
The results also showed that the PPP-B2b signal can sta- Specification Centimeter Level Augmentation Service, document (IS-
bly provide PPP services for satellites in the Asia-Pacific QZSS-L6-002)[DB/OL],Dec.2019.
[19] L.Chen,P.Thevenon,G.Seco-Granados,O.Julien,andH.Kuusniemi,
region,includingcentimeter-leveltodecimeter-levelorbitcor-
“Analysis on the TOA tracking with DVB-T signals for positioning,”
rections and meter-level clock corrections for BDS satellites. IEEETrans.Broadcast.,vol.62,no.4,pp.957–961,Dec.2016.
In the meanwhile, PPP services provide decimeter-level to [20] J. B. Y. Tsui, Fundamentals of Global Positioning System Receivers:
ASoftwareApproach,vol.1,1sted.Hoboken, NJ,USA:Wiley,2000.
meter-level orbit correction and meter-level clock correction
[21] BeiDouNavigation Satellite System:Signal inSpace Interface Control
for GPS satellites. Finally, detection tips for bitstream avail- Document Precise Point Positioning Service Signal PPP-B2b Version
ability in SDR are proposed, and some content which is not 1.0,ChinaSatell. Navigat.Office, Beijing, China,Jul.2020.
[22] K. Borre, D. M. Akos, N. Bertelsen, P. Rinder, and S. H. Jensen,
defined in the official document, such as the PPP-B2b frame
A Software-Defined GPS and Galileo Receiver: A Single-Frequency
arrangement scheme, various correction update cycles and Approach,vol.1,1sted.Boston,MA,USA:Springer,2007,pp.99–100.
PPP-B2b’s progress in providing PPP service are discussed. [23] L. Chen, L.-L.Yang, J. Yan, and R. Chen, “Joint wireless positioning
and emitter identification in DVB-T single frequency networks,” IEEE
Relatedtothefutureworks,theimplementationofthedecoded
Trans.Broadcast.,vol.63,no.3,pp.577–582,Sep.2017.
PPP-B2bserviceinformationdirectlyontheSDRreceiverwill [24] F. V. Diggelen and C. Abraham, “Indoor GPS technology,” CTIA
be considered and the positioning accuracy and integrity will Wireless-Agenda, Dallas, TX, USA, Tech. Rep., May 2001, vol. 89,
no.1,pp.1–10.
be further compared in detail.
[25] L. Chen, O. Julien, P. Thevenon, D. Serant, A. G. Pena, and
H.Kuusniemi, “TOA estimation for positioning with DVB-T signals
REFERENCES
in outdoor static tests,” IEEE Trans. Broadcast., vol. 61, no. 4,
[1] TheStateCouncilInformationOfficeofthePeople’sRepublicofChina, pp.624–638,Dec.2015.
China’s BeiDou Navigation Satellite System. Beijing, China: Foreign [26] BeiDouNavigation Satellite System:Signal inSpace Interface Control
Languages Press,2016. DocumentOpenServiceSignalB1CVersion1.0,ChinaSatell.Navigat.
[2] Report on the Development of BeiDou Navigation Satellite System Office,Beijing, China,Dec.2017.
Version2.1,ChinaSatell. Navigat.Office, Beijing, China, Dec.2012.
[3] Development of the BeiDou Navigation Satellite System Version 3.0,
ChinaSatell. Navigat. Office,Beijing, China, Dec.2018.
[4] Development of the BeiDou Navigation Satellite System Version 4.0,
ChinaSatell. Navigat. Office,Beijing, China, Dec.2019.
[5] Press Conference for the Completion of Beidou-3 Global Satellite
Navigation System, China Satell. Navigat. Office, Beijing, China, XiangchenLu(StudentMember,IEEE) iscur-
Aug.2020. rently pursuing the master’s degree with the
[6] M.ElsobeieyandS.Al-Harbi, “Performance ofreal-time precise point StateKeyLaboratoryofInformationEngineering
positioningusingIGSreal-timeservice,”GPSSolutions,vol.20,no.3, in Surveying, Mapping and Remote Sensing,
pp.565–571,Jun.2015. WuhanUniversity.Hismainresearchdirectionis
[7] X. H. Zhang, X. X. Li, and P. Li, “Review of GNSS PPP and its software-definedreceiver.
application,” ActaGeodaetica etCartographicaSinica,vol.46,no.10,
pp.1399–1407,Oct.2017.
[8] X. Li, M. Ge, J. Douša, and J. Wickert, “Real-time precise point
positioning regional augmentation for large GPS reference networks,”
GPSSolutions, vol.18,no.1,pp.61–71,Jan.2013.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 13 -->

LUetal.:DECODINGPPPCORRECTIONSFROMBDSB2BSIGNALSUSINGASOFTWARE-DEFINEDRECEIVER 7883
LiangChen(SeniorMember,IEEE)isaProfes- Zhenhang Jiao (Student Member, IEEE) is
sorwiththeStateKeyLaboratoryofSurveying, currently pursuing the Ph.D. degree with the
Mapping and Remote Sensing Information StateKeyLaboratoryofInformationEngineering
Engineering, Wuhan University. His research in Surveying, Mapping and Remote Sensing,
interests include navigation new signal theory Wuhan University. His research interests focus
andmethod,ubiquitoussmartphonepositioning, onsignals-of-opportunity-basedpositioningand
and indoor and outdoor seamless positioning datafusion.
andnavigation.
NanShen(StudentMember,IEEE)iscurrently
pursuing the Ph.D. degree with the State Key
LaboratoryofInformationEngineeringinSurvey-
ing,MappingandRemoteSensing,WuhanUni-
versity. His research interests focus on precise
GNSS data processing and software-defined
receiver.
LeiWang(Member,IEEE)iscurrentlyanAsso- RuizhiChen(SeniorMember,IEEE)isaProfes-
ciate Research Fellow at the State Key Labo- sorwiththeStateKeyLaboratoryofSurveying,
ratory of Information Engineering in Surveying, MappingandRemoteSensingInformationEngi-
Mapping and Remote Sensing, Wuhan Univer- neering,WuhanUniversity,andalsotheDirector
sity.HisresearchinterestsincludeGNSSprecise of the laboratory. His main research interests
positioning and LEO navigation augmentation include smartphone ubiquitous positioning and
system. satellitenavigationandpositioning.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:40:02 UTC from IEEE Xplore. Restrictions apply.