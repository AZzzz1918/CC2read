<!-- PAGE: 1 -->

4994 IEEESENSORSJOURNAL,VOL.23,NO.5,1MARCH2023
Multi-Frequency BDS-3 Real-Time Positioning
Performance Assessment Using New PPP-B2b
Augmentation Service
Haitao Zhou , Wenju Fu, Lei Wang , Tao Li, Yuan Wu , Ruizhi Chen , and Juanjuan Li
Abstract—Anewprecisepointpositioning(PPP)-B2baug-
mentationservicebroadcastbytheBeiDouNavigationSatel-
liteSystem(BDS-3)geosynchronousEarthorbit(GEO)satel-
lite can provide real-time and high-precision orbit and clock
offset corrections for global navigation satellite system
(GNSS) users in China and its surrounding areas. It has
greatsignificanceandresearchvalueforreal-timeandhigh-
precision positioning applications. First, orbit, clock offset,
and differential code bias (DCB) of PPP-B2b products are
evaluated. Second, the influence of PPP-B2b service on
the enhanced positioning of single-frequency (SF), dual-
frequency (DF), and Multi-Frequency (MF) real-time PPP
using 30 days of BDS-3 observations is verified. The result
shows that the standard deviation (STD) of clock offset and
the root mean square (rms) of orbit in the 3-D direction for
mediumEarthorbit(MEO)satellitesare0.118nsand0.286m,
respectively, which is 75.9% and 18.3% higher than that of
broadcast ephemeris. The statistical results show that the
median positioning accuracy of static SF PPP, DF PPP, and
MFPPPisbetterthan0.20/0.09/0.08m,andtheconvergence
timeisbetterthan51/10/8min.Themedianpositioningaccu-
racyofkinematicSFPPP,DFPPP,andMFPPPisbetterthan
0.40/0.12/0.12 m, and the convergence time is better than 145/16/12 min. Using the PPP-B2b products, the positioning
accuracy of DF PPP and MF PPP is comparable and close to that of DF PPP using the precise products, while the
convergencetimeofMFPPPisimprovedby24.8%and27.7%overDFPPPinstaticandkinematicsolutions,respectively.
Index Terms—BeiDou Navigation Satellite System (BDS-3), multi-frequency (MF), PPP-B2b service, precise point
positioning(PPP),realtime.
I. INTRODUCTION BDS-3constellationwascompleted,indicatingthatBDS-3can
THE BeiDou Navigation Satellite System (BDS-3) is one provide navigation, positioning, and timing (PNT) services to
of the four major navigation and positioning systems in global users [2]. The BDS-3 includes 24 medium Earth orbit
the world, which is independently designed, developed, and (MEO) satellites, three inclined geosynchronous satellite orbit
operated by China. On June 23, 2020, the deployment of (IGSO)satellitesandthreegeosynchronousEarthorbit(GEO)
satellites[3],[4].BDS-3GEOsatellite-basedregionalfeatured
Manuscript received 13 December 2022; accepted 6 January 2023.
services consist of the radio determination satellite service
Dateofpublication23January2023;dateofcurrentversion28Febru-
ary 2023. This work was supported in part by the Program of the (RDSS), the BDS satellite-based augmented service (BDS-
National Natural Science Foundation of China under Grant 41904038 BAS), the regional short message communication (RSMC)
and Grant 42074036, and in part by the China Postdoctoral Science
services,andthesatellite-basedprecisepointpositioning(PPP)
Foundation under Grant 2019M662713. The associate editor coordi-
nating the review of this article and approving it for publication was service via B2b signal (PPP-B2b) [2], [5], [6].
Dr.HassenFourati.(Correspondingauthor:WenjuFu.) ThePPPtechnologyusesasingleglobalnavigationsatellite
HaitaoZhou,WenjuFu,LeiWang,TaoLi,YuanWu,andRuizhiChen
system (GNSS) receiver to achieve high-precision positioning
are with the State Key Laboratory of Information Engineering in Sur-
veying,MappingandRemoteSensing(LIESMARS),WuhanUniversity, by receiving pseudorange and phase observations and using
Wuhan430072,China(e-mail:wenjufu@whu.edu.cn). high-precision satellite orbit and clock offset products. It has
Juanjuan Li is with the 54th Research Institute of China Electronics
important applications in low-orbit satellite orbit determina-
TechnologyGroupCorporation,Shijiazhuang050081,China.
DigitalObjectIdentifier10.1109/JSEN.2023.3235901 tion [7], [8], water vapor inversion [9], seismic monitoring,
1558-1748©2023IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:00:00 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 2 -->

ZHOUetal.:MFBDS-3REAL-TIMEPOSITIONINGPERFORMANCEASSESSMENT 4995
ionospheric monitoring [10], [11], and other fields. Since PPP correspondinguserrangeaccuracyindex(URI).Type3broad-
was put forward in 1997, it has gone through the develop- casts differential code bias (DCB). Type 4 broadcasts IOD
ment process from ambiguity float solution to fixed solu- Corr and clock offset corrections. The update time is 6 s for
tion [12], [13], [14] and from postprocessing to real-time pro- Type4and48sfortherestofthetypes.ThePPP-B2bcorrec-
cessing [15]. The research of PPP mainly focuses on the PPP tions can be combined with the broadcast ephemeris (BRDC)
positioningmodel,datapreprocessing,errormodelrefinement, to recover the real-time orbit and clock offset with high
ambiguity fixing, and fast initialization [16]. The emergence accuracy.Thissectionbrieflyintroducestheevaluationmethod
oftheMulti-Frequency(MF)GNSStechnology[17],[18]can of PPP-B2b corrections and three MF BDS-3 PPP models.
providemoreredundantobservationsforPPPsolutionandcan
also construct more optimal combinations [19] to meet the A. PPP-B2bCorrections
purpose of cycle slip detection [20] or ambiguity resolution, The orbit and clock offset of PPP-B2b corrections must
and finally improve the positioning accuracy and speed up be matched to be used. If IOD Corr in Type 2 matches that
convergence. in Type 4, the IODN in Type 2 must also match the issue
With the rapid development of GNSS technology, real-time of data, clock (IODC) in the broadcast ephemeris. Then, the
PPP [21], [22] has become a research hotspot in the GNSS PPP-B2bcorrectionscancorrecttheorbitinradial,along,and
community, which has significant application prospects in the cross (RAC) directions and the clock offset of the broadcast
field of unmanned driving, smart agriculture, and earthquake ephemeris. The reference points of orbit and clock offset
warning. However, the main constraint to real-time PPP is of broadcast ephemeris and PPP-B2b products are the B3I
the availability of the GNSS orbit and clock offset products frequency center of BDS-3 satellites. For final precise multi-
with high accuracy in real time [23], [24], [25]. In 2013, IGS GNSS products from Geo Forschungs Zentrum (GFZ) prod-
organizations began to broadcast real-time precise orbit and ucts,theorbitreferencepointofBDS-3satellitesisthesatellite
clockoffsetdatastreamstoglobalusersvianetworkaccording center-of-mass (CoM), while the clock offset reference point
to the standard of Radio Technical Commission for Maritime is the B3I frequency center. When evaluating the accuracy of
Service(RTCM).CentreNationalD’EtudesSpatiales(CNES) orbitandclockoffsetofPPP-B2bproducts,thecorresponding
andotherorganizationsalsobroadcastreal-timecorrectionsof conversion should be carried out for comparison [6], [28].
the multi-GNSS systems to global users [26]. The positioning The evaluation of clock offset accuracy is relatively com-
accuracy of static centimeter level and kinematic decimeter plicated. Clock offset provided by different analysis centers
level can be achieved. However, PPP may be reinitialized cannot be compared directly due to the differences in the
when the network is interrupted. In addition, the PPP-B2b underlying GNSS-specific system time scales [34]. There is a
service broadcast by BDS-3 GEO satellite via the B2b signal systematicbiasafterthesingle-difference(SD)valueisformed
has also started to broadcast the BDS-3/GPS precise orbit between the PPP-B2b products and the GFZ products. In this
and clock offset corrections to China and its surrounding case, the systematic bias of the satellite can be eliminated
areas since 2020 [27]. At present, some studies have been by subtracting the SD value of the reference satellite with a
conducted to enhance dual-frequency (DF) PPP based on longerobservationarcorcorrectinganaverageensembleclock
PPP-B2bcorrections[28],[29],[30],[31]andapplyittotime- difference computed at each epoch from the SD values of
frequencytransmissionandearthquakewarning[32],[33],but satellites in a constellation [6]. This article adopts the second
the positioning performance of single-frequency (SF) and MF waytoeliminatethesystematicbias,andthedouble-difference
PPP has not been studied. (DD) values can be written as follows:
The main contribution of this article is to comprehensively
DDclks(i) = clks (i)−clks (i)
assess the quality of PPP-B2b products and to analyze the B2b GFZ
ns
enhanced positioning effect of PPP-B2b products on SF, DF, − 1 X(cid:0) clkn (i)−clkn (i)(cid:1) (1)
andMFPPPfromtheperspectiveofpositioningaccuracyand ns B2b GFZ
n=1
convergence time, which can provide more options for PPP
where B2b and GFZ represent the PPP-B2b products and the
users. This article is organized as follows. First, this article
finalGFZproducts,respectively;s representsthesatellitePRN
introduces the assessment methods of PPP-B2b products and
of BDS-3. clk stands for satellite clock offset; i indicates
briefly gives the SF, DF, and MF PPP models. Then, the
the current epoch. ns indicates the total number of available
accuracyofPPP-B2bproductsisevaluated,andthepositioning
satellites in the current epoch.
performanceofPPP-B2bservice-enhancedBDS-3SF,DF,and
The signal-in space range error (SISRE) is usually used to
MF PPP is evaluated. Finally, some conclusions and findings
comprehensively reflect the impact of orbit and clock offset
are summarized.
on final positioning. The SISRE is calculated as follows [34]:
II. MF PPP MODEL WITH PPP-B2B CORRECTIONS
SISRE
cor
C
re
u
c
r
t
r
i
e
o
n
n
t
s
ly,
th
B
r
D
ou
S
g
-
h
3 b
G
r
E
oa
O
dca
sa
st
t
s
ell
o
it
n
e
l
s
y
(
f
C
ou
5
r
9,
ty
C
pe
6
s
0,
of
an
P
d
PP
C
-B
61
2
)
b
.
  q (0.98· R)2+(cid:0) A2+C2 (cid:1)/54,
= (2)
Type 1 broadcasts the pseudo-random noise (PRN) mask of  q (0.99· R)2+(cid:0) A2+C2 (cid:1)/126,BDS−3(IGSO)
BDS-3satellites,andthePRNmaskofthesatelliteswithPPP-
B2bcorrectionsis1;otherwise,itis0.Type2broadcastsissue where R, A,andC denotetherootmeansquare(rms)oforbit
of data, navigation (IODN), IOD Corr, orbit corrections, and errors in RAC directions, respectively.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:00:00 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 3 -->

4996 IEEESENSORSJOURNAL,VOL.23,NO.5,1MARCH2023
B. PPPModelWithDifferentFrequencies satellites clock offset for broadcast ephemeris and final GFZ
The PPP model uses the pseudorange and phase observa- products, respectively. DCB B1I-B3I is the DCB obtained from
tion to construct the observation equations. The observation PPP-B2b products.
equations can be expressed as follows: 2) DF PPP Model: The DF PPP model adopts an
 ionosphere-free (IF) combination, and the DF observation
P r s =ρ r s+dt r −dts +Mw r s ·ZWD r +I r s +ε r s ,P equations can be expressed as follows:
 (cid:16) (cid:17)
L r s =ρ r s+dt r −dts +Mw r s ·ZWD r −I r s +λ i sN i s +ε r s ,
(
L
3)
 OMC
(cid:16)
P r s ,IFjk
(cid:17)
=x r s +dt r +Mw r s ·ZWD r +ε r s ,P,IFjk
where s and r represent the satellite PRN and the receiver,
 OMC L r s ,IFjk =x r s +dt r
+
+
λs
Mw r s
N
·
s
ZWD
+
r
εs
(8)
respectively; P and L denotethecodeandphaseobservations, i,IFjk i,IFjk r,L,IFjk
respectively; ρ is the geometric range between the satellite where j and k represent the B1I and B3I signal frequencies;
and receiver antennas; dt and dts denote the receiver and Ps and Ls representtheIFcombinationofpseudorange
r r,IFjk r,IFjk
satellite clock offsets, respectively; I is slant ionospheric and phase; λs and Ns represent the wavelength and
delay; Mw r s and ZWD r are the mapping function of zenith ambiguity of I i F ,IF c jk ombinatio i, n IF f jk or special satellite; ε r s ,P,IFjk and
tropospheric wet delay and corresponding zenith troposphere εs are the measurement noises of pseudorange and phase
wet delay, respectively; λ i and N i s are the wavelength of IF r,L c ,I o F m jk binations. Other parameters are the same as above.
differentfrequenciesandtheambiguityofthespecificsatellite B1I and B3I observations of BDS-3 satellites are adopted to
incycles,respectively;ε r s ,P andε r s ,L arethenoiseofcodeand constructtheDFPPPmodelinthisstudy.TheDCBshouldbe
phase observations. Unless otherwise stated, the units used in considered for B1I/B3I IF combination [36], and the formula
this article are in meters. is as follows [28]:
1) Single-FrequencyPPPModel: The ionosphere effect is a
key issue for SF PPP. In contrast to the conventional SF PPP ds −ds = f j 2 (cid:16) ds −ds (cid:17) − f k 2 (cid:0) ds −ds (cid:1)
to eliminate the ionosphere by employing code-minus-phase IFij B3I f2− f2 j B3I f2− f2 k B3I
j k j k
combination,weestimatetheionospheredelayasparameterin f2 f2
this study [1]. Ignoring second-order ionospheric delay [35], = j DCBs − k DCBs (9)
f2− f2 j f2− f2 k
the observation equation of the SF PPP model is shown as j k j k
follows:
where f is the frequency; d represents the satellite code
 OMC (cid:0) P
r
s(cid:1)= x
r
s +dt
r
+Mw
r
s ·ZWD
r
+I
r
s +ε
r
s
,P
hardwaredelay;DCBcanbeobtainedfromPPP-B2bproducts.
3) MF PPP Model: Based on the B1I/B3I observations,
OMC (cid:0) Ls(cid:1)= xs +dt +Mws ·ZWD −Is +λsNs+εs BDS-3 also broadcasts B1C/B2a signals at the same time,
r r r r r r i i r,L
(4) which provides more observations for MF PPP. To verify
the enhancement effect of PPP-B2b products on MF PPP,
where OMC represents the observed value minus the calcu- B1C/B2a IF combination is added based on the B1I/B3I IF
lated value. Pseudorange or phase observations subtract the combination. The pseudorange and phase observation equa-
errors calculated by the error models. The relevant error mod- tions of MF PPP are as follows:
elsincludetroposphericdrydelay,phasewindup,phasecenter  (cid:16) (cid:17)
d
r
i
o
a
o
e
n e
f
c
n
f
d d
s
e
o
u
e
i
s
v
s c
t
p
o t
e
(
i
h
P
r
n
e
o
C
g
p
r
n
i
o
O
c
t .
s
h
)
i
e x
t
d
c
i
r s
e
o
r
o
e
l
n
r
a
i l
r
,
s a
y
e
r
,
t
c
e
e
t
t
h
a
d
c
i
n
e
o
e
e
i
d
n
v
r c
,
r
e
o
a
o
r
r
e
o
m
r
c
l
s r
a
b
, d
lo
t
i
i t
i
g
n
c
h
v
k
u
a e
is
t
i
o
t
e p
t
i
y
f
a
c
.
f
p r
s
c
a a
W
e
o
m r
t
r
a
,
h
r
e m
t
e
e
t
r
e
c
n
o
e r
t
t
p
i
s e
o
t
o
h
r o
n
.
s
e
f
p
,
r
T
h
t
S
e
i
h
e
d
F e
r
a
a
i
r
r
P
l
c
e
e
P
c
f
w
o
o P
n
r
e
r
r
e i
t
e
v
n ,
d
c
i
c
s
e
a
t
l
i
i
u
l
f
o
b
a
t d e
n
l
y
e
e r
,
,

O
O
M
M
C
C
(cid:16) L
P r
r s
s ,
,
I
I
F
F
j
j
k
k (cid:17) =
=
x
x
r
r
s
s
+
+
d
d
t
t
r
r
+
+
+
λ
i
s
M
M
,IF
w
w
jk
r
r
s
s
N
·
·
i
s
,
Z
Z
IF
W
W
jk
D
D
+
r
r
ε
+
r
s
,L
ε
,
r s
I
,
F
P
j
,
k
IFjk
s
fo
a
l
t
I
e
l
n
o
ll
w
a
it
d
s
e
:
d
s,
iti
t
o
h
n
X
e
,B
=
p
1
a
I
r
(cid:2)
a
o
x
m
b
3×
e
se
t
1
e
r
r
v
d
s
a
t r
ti
o
o
Z
f
n
W
s
S
a
F
D
re
P
I
u
n
P
s
×
P
e
1
d
N
c
fo
a
n
n
r
×
t
1
h
b
(cid:3)
e
e
.
S
e
F
x
P
pr
P
e
P
ss
m
ed
od
(5
a
e
s
)
l
 O
O
M
M
C
C
(cid:0)
(cid:0) L
P r
r s
s ,
,
I
I
F
F
a
a
c
c
(cid:1)
(cid:1)
=
=
x
x
r
r
s
s+
+
d
d
t r
t r
+
+
+
+
ε
λ
M r
s
s
I
,
F
P w ,
B
IF r s
N
+
a · c
s
Z
M
W
w
D
+
r s
r
·
ε
Z
s
WD r (10)
in this study, and the frequency reference of orbit and clock
i,IFac i,IFac r,L,IFac
where a and c represent the B2a/B1C signal frequency; IFB
offset needs to be converted to B1I signal. The orbit can be
is the interfrequency bias of receiver, and the random walk
corrected by PCO, and the clock offset can be corrected by
DCB. The clock offset correction formula is as follows: modelisusedtoestimatethisparameter.Otherparametersare
the same as above. The B1C/B2a IF ambiguity should also be
T ¯ b B ro 1 a I dcast_C = T ˆ broadcast_C +DCB B1I-B3I (6) added to parameter estimation. The parameters for MF PPP
1 are as follows:
T ¯B1I = T − DCB (7)
precise_C precise_C β−1 B1I-B3I
X
=(cid:2)
x 3×1 dt r IFB ZWD N jk,n×1 N ac,n×1
(cid:3).
(11)
where β = f B 2 1I /f B 2 3I ; T ¯ b B ro 1 a I dcast_C and T ¯ p B re 1 c I ise_C are the clock Similarly,DCBshouldalsobeconsideredfortheB1C/B2aIF
ˆ
offset considering DCB; T and T are BDS-3 combination, and the correction method should refer to (9).
broadcast_C precise_C
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:00:00 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 4 -->

ZHOUetal.:MFBDS-3REAL-TIMEPOSITIONINGPERFORMANCEASSESSMENT 4997
Fig.1. MeanSTDofclockoffsetforBDS-3withBRDCandPPP-B2b
products.
TABLEI
BDS-3MEOSATELLITESOFDIFFERENTMANUFACTURERS Fig.2. Meanrmsoforbiterrorsin(a)radial,(b)alongtrack,(c)cross
track,and(d)SISREforBDS-3withBRDCandPPP-B2bproducts.
TABLEII
MEANRMSOFORBITANDSTDOFCLOCKOFFSETFORBDS-3
III. ACCURACY ASSESSMENT OF PPP-B2B
CORRECTIONS
This section mainly evaluates the accuracy of PPP-B2b
products, including orbit, clock offset, and DCBs. The dataset
decoded by Septentrio R5 receiver was obtained from June
1 to 30, 2022. In addition, the orbit and clock offset results of
broadcast ephemeris are taken as a reference for comparison.
B. AccuracyofOrbit
A. AccuracyofClockOffset The orbit accuracy of PPP-B2b products in RAC directions
To evaluate the accuracy of PPP-B2b clock offset, the can be evaluated when the phase center of satellites for
differences of GNSS-specific system time scales were elim- PPP-B2b products and final GFZ products is converted to
inated by the DD method [6], [34], and the mean standard B1I/B3I IF combination phase center of the satellite. The rms
deviation (STD) of clock offset for each BDS-3 satellites of orbit errors obtained for each satellite using 30 days of
with 30 days of data is shown in Fig. 1. As shown in the data is shown in Fig. 2. The orbit accuracy of the broadcast
figure,exceptfortheC40satellite,theclockoffsetSTDofthe ephemeris is also given for comparison. The rms in the radial
broadcast ephemeris for the other BDS-3 satellites fluctuates direction is the smallest in RAC directions and is better than
within 0.4–0.6 ns. Except for the IGSO satellites (C38, C39, 0.2 m. The rms in along-track and cross-track directions is
and C40), the clock offset STD of PPP-B2b products for better than 0.4 m. In general, due to the application of inter-
all MEO satellites is less than 0.2 ns. Compared with MEO satellite link (ISL) measurements to broadcast ephemeris, the
satellites, the clock offset STD of BDS-3 IGSO satellites is orbitaccuracyofbroadcastephemerisforBDS-3satelliteshas
generallypoor.Theclockoffsetofallsatellitesfluctuatesmore been greatly improved [38]. Even with PPP-B2b corrections,
smoothly with PPP-B2b corrections, which also facilitates the accuracy improvement is not obvious. At the same time,
short-term clock offset forecast in the event of the PPP-B2b it can be seen that the orbit accuracy of C26–C30 satellites in
service outage. the radial direction is very good, which may be due to more
It should be noted that the BDS-3 MEO satellites are available ISL measurements of these satellites [6] during the
manufacturedbytheChinaAerospaceScienceandTechnology generation of broadcast ephemeris.
Corporation (CASC) and the Shanghai Engineering Center The statistical results of the orbit errors of all BDS-3
for Microsatellites (SECM) [37], and the details are shown satellites are shown in Fig. 2 and Table II. The orbit accuracy
in Table I. After the statistics, it was found that the clock ofthePPP-B2bproductsiscomparabletothatofthebroadcast
offsetSTDofthetwotypesofMEOsatelliteswas0.1167and ephemeris, and the improvement is not significant over the
0.12 ns, respectively, with a difference of 0.003 ns, indicating clock offset. The rms of the PPP-B2b products of MEO and
that the clock offset accuracy of the MEO satellites made by IGSO satellites in the 3-D direction is 0.286 and 0.447 m,
CASC and SECM is approximately equivalent. respectively, which are 18.3% and 12.9% higher than that of
The statistical results of all BDS-3 satellites are shown in the broadcast ephemeris. The SISRE of PPP-B2b products of
Table II. The mean STD of MEO and IGSO satellites clock MEO and IGSO satellites is 0.087 and 0.21 m, respectively,
offset is 0.118 and 0.237 ns, respectively, which is 75.9% and which are 6% and 2% higher than that of the broadcast
61.8% higher than that of broadcast ephemeris. The accuracy ephemeris. PPP-B2b products cannot be greatly improved in
ofbroadcastephemerisclockoffsethasbeengreatlyimproved the radial direction due to ISL measurements, but there is a
with PPP-B2b corrections. largeroomforimprovementinthealong-trackandcross-track
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:00:00 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 5 -->

4998 IEEESENSORSJOURNAL,VOL.23,NO.5,1MARCH2023
TABLEIII
RECEIVERINFORMATIONOFTHEMGEXSTATIONS
TABLEIV
Fig. 3. Mean DCB difference of PPP-B2b products versus CAS
products(top)andPPP-B2bproductsversusTGD(bottom).
PPPSTRATEGY
directions. In addition, the reason why the SISRE of IGSO
satellites is inferior to that of the MEO satellites may be due
to the fact that this kind of regional satellites cannot be well
tracked globally [2], and also due to the fact that there are
fewer available ISL measurements for IGSO satellites [6].
Meanwhile, we also conducted a statistical analysis of the
orbital accuracy of the BDS-3 MEO satellites manufactured
by CASC and SECM. The orbit rms in the 3-D direction of
the two types of the MEO satellites is 0.2838 and 0.3132 m,
and the SISRE is 0.0926 and 0.0772 m, respectively. Both the
orbitrmsdifferenceandtheSISREdifferenceareabout2cm,
indicating that the orbit accuracies of BDS-3 MEO satellites
manufactured by CASC and SECM are approximately com-
parable.
C. AccuracyofDCBs
DCBatdifferentsignalfrequenciesofBDS-3satellitesrep-
resentsthesatelliteDCBbetweenthecorrespondingsignalfre-
quencyandtheB3Isignalfrequency.Atpresent,thePPP-B2b
productsonlyprovidetheDCBsofBDS-3satellites,including
DCB (B1I), DCB (B1Cp), and DCB (B2ap). To evaluate the
DCBs accuracy of the PPP-B2b products, compare them with
the multi-GNSS experiment (MGEX) DCB products provided
Fig.4. DistributionofMGEXstations.
by the Chinese Academy of Sciences (CAS) [39] and the
time group delay (TGD) provided by broadcast ephemeris,
respectively. The average DCB difference of the 30 days of
positioning experiments were conducted using the BDS-3
each BDS-3 satellite is shown in Fig. 3. As can be seen
observations from six MGEX stations in and around China.
from the figure, the DCB difference between the PPP-B2b
The dataset is from June 1 to 30, 2022. The distribution
productsandtheCASproductsisrelativelylarge,andtheDCB
and details of these MGEX stations are shown in Fig. 4
difference of B1I/B1Cp of all satellites fluctuates between
and Table III. The experiment is divided into four schemes,
0 and 2 ns. The DCB difference of B2ap is better than 1 ns,
namely,SFPPP,DFPPP,MFPPP,andreferenceexperiments,
which was slightly better than that of B1I/B1Cp. The DCB
and each scheme is tested by both static and simulated
accuracyofthePPP-B2bproductsandtheTGDiscomparable,
kinematic solutions. The reference experiments are the DF IF
and the difference of B1I/B1Cp/B2ap for all BDS-3 satellites
PPP using final GFZ products. The detailed PPP strategy is
isbetterthan0.1ns.ThismaybethereasonthatbothPPP-B2b
shown in Table IV.
products and TGD are provided by the China Analysis Center
Considering the difference of the geometry of satellites
based on a small number of ground-based tracked stations,
and the number of available satellites in different observation
while CAS products are provided by solutions using global
periods, the PPP solutions were restarted every 4 h, and six
tracked stations.
positioning results can be obtained per day for each station.
Then, each station can get 180 PPP results in 30 days. The
IV. POSITIONING PERFORMANCE WITH PPP-B2B
reference coordinates of MGEX stations are the IGS weekly
CORRECTIONS
solution.Thepositioningerrorsofthese180segmentsforeach
A. DatasetandPPPStrategy station were fused according to each epoch, and the median,
To verify the enhanced effect of PPP-B2b corrections on 68.26% (1σ) value, and 95.44% (2σ) value of statistical
real-time positioning with SF, DF, and MF PPP models, results were given to evaluate the positioning accuracy and
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:00:00 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 6 -->

ZHOUetal.:MFBDS-3REAL-TIMEPOSITIONINGPERFORMANCEASSESSMENT 4999
TABLEV
MEANOFSTATISTICALRESULTSOFPOSITIONINGERRORSWITH
FOURPPPMODELS
Fig.5. MedianpositioningerrortimeserieswithfourPPPmodelsin
staticsolutionsforPTGGstation.
TABLEVI
MEANOFSTATISTICALRESULTSOFCONVERGENCETIMEWITHFOUR
PPPMODELS
Fig.6. MedianpositioningerrorsofsixstationswithfourPPPmodels
instaticsolution.
convergence time. The convergence time was defined as the
horizontal accuracy and vertical accuracy of 20 and 40 cm,
respectively, and lasted for more than 5 min [6].
B. StaticTest
In this study, we use the positioning results from PTGG
station as an example, and the median positioning error time
Fig.7. MedianconvergencetimeofsixstationswithfourPPPmodels
series in the ENU directions for static model are shown in instaticsolution.
Fig. 5. We interrupt the PPP filter every 4 h and compute
the median position error time series using 30 days’ data
to explore the convergence characteristics of different PPP improvement effect of DF PPP and MF PPP with PPP-B2b
models. The black line, red line, yellow line, and gray line productsonthe E and N directionsisthemostobvious,which
representthemedianpositioningerrorsoftheSFPPP,DFPPP, is basically consistent with the reference results. Compared
MF PPP, and reference solutions, respectively. The figure with DF PPP, the accuracy of MF PPP is improved by 6.1%,
shows that the SF PPP converges slowly, and it takes about 9.5%,and7.3%intheENUdirections,respectively.Ascanbe
30 min to converge to 0.2 m in the ENU directions. The seen from Fig. 7, the convergence time of SF PPP is longer,
accuracy of DF PPP and MF PPP is comparable, and it takes greater than 40 min, and far more than the 10 min of DF PPP
about 10 min to converge to 0.2 m in the ENU directions, but and MF PPP. The convergence time of MF PPP is even better
the convergence speed of MF PPP in the initial stage is better than that of reference results at some stations. Compared with
thanthatofDFPPP.Comparedwiththereferenceresults,there DF PPP, the convergence time of MF PPP is improved by
isstillroomforimprovementinthepositioningaccuracyafter 24.8%. It shows that although more frequencies are used, the
convergence. positioning accuracy is not significantly improved after con-
The median of positioning errors and convergence time of vergence, but in the initial state, MF PPP can converge faster.
thesixstationsisshowninFigs. 6and7.TheSFPPPposition- We compared the performance of the four different PPP
ing results are relatively poor, except for the N direction, the models in static solution with the following three measures:
accuraciesofthe E andU directionsareallgreaterthan0.1m. median, 1σvalue, and 2σ value of positioning errors and
TheDFPPPandMFPPPresultsofallstationsarebetterthan convergence time. Tables V and VI show the mean values of
0.1mintheENUdirectionsexcepttheGAMGstation.Among these performance measures computed from the six stations.
them, the positioning accuracy in the E and N directions is With the increase in the statistical range, the positioning
better, which are 4 and 2 cm, respectively. It shows that the accuracydeteriorates,andtheconvergencetimealsoincreases
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:00:00 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 7 -->

5000 IEEESENSORSJOURNAL,VOL.23,NO.5,1MARCH2023
Fig.10. MedianconvergencetimeofsixstationswithfourPPPmodels
inkinematicsolution.
PPP, the positioning accuracy in the ENU directions is close
Fig.8. MedianpositioningerrortimeserieswithfourPPPmodelsin
to the reference results, and both are better than 0.2 m,
kinematicsolutionsforPTGGstation.
especially the N direction is better than 0.04 m. Compared
with DF PPP, MF PPP has an increase of 4.2%, 7.4%, and
8.2% in the ENU directions, respectively. From the median
convergence time in Fig. 10, it can be seen that SF PPP is
more than 90 min, while DF PPP and MF PPP are better than
25 min. Compared with DF PPP, the convergence time of MF
PPP is improved by 27.7%. For JFNG, URUM, and ULAB
stations, the convergence time of MF PPP is better than that
ofreferenceresults,whichindicatesthattheincreasednumber
of observations contributes to fast convergence.
For the statistical results of six stations with four PPP
models in kinematic solution, we also give the median, 1σ
Fig.9. MedianpositioningerrorsofsixstationswithfourPPPmodels value, and 2σ value of positioning errors and convergence
inkinematicsolution.
time, and Tables V and VI show the mean values of these
performance measures. The 1σ statistical results of position
gradually. The 1σ statistical results of DF PPP and MF PPP errors show that the SF PPP is better than 0.4 m in the E
are better than 0.1 m in the E and N directions and 0.2 m in and N directions and 0.6 m in the U direction. DF PPP and
the U direction, respectively. The 2σ statistical results of DF MF PPP are better than 0.08 m in the E and N directions
PPPandMFPPParebetterthan0.5mintheENUdirections. and 0.16 m in theU direction. The 2σ statistical results show
From the perspective of convergence time, the 1σ statistical that the accuracy of SF PPP in the ENU directions is at the
results of DF PPP and MF PPP are better than 15 min, and meterlevel,andtheaccuracyofDFPPPandMFPPPisatthe
the results of MF PPP and reference experiments are more decimeterlevel.Atthesametime,thepositioningaccuracyof
consistent. The mean of matched satellites number for these DFPPPandMFPPPisclosetothatofreferenceresultsinthe
stations is 8.09–8.61. The available satellites decrease rapidly E and N directions,butthereisstillroomforimprovementin
as the stations get farther away from the PPP-B2b service theU direction.Intermsofconvergencetime,themedian,1σ,
area. Fewer satellites lead to poorer PPP performance and and 2σ statistical results show that MF PPP is improved by
longer convergence time. Therefore, to ensure the positioning 27.7%,19.9%,and8.4%comparedwithDFPPP,respectively,
performanceofPPP-B2bservicetoenhancereal-timePPP,the and the results are more consistent with reference results.
service should be applied close to its service area.
V. CONCLUSION
C. KinematicTest The new PPP-B2b-enhanced service broadcast by the
We also use positioning results from PTGG station as an BDS-3 GEO satellite is freely available to GNSS users in
example, and the median positioning error time series in China and its surrounding areas, enabling real-time static
the ENU directions are shown in Fig. 8. The experimental centimeter-level and kinematic decimeter-level positioning
calculation procedure is similar to the static solution. SF PPP accuracy.Theaccuracyoforbit,clockoffset,andDCBsofthe
takes about 2 h to converge to 0.2 m in the ENU directions. PPP-B2b products is first evaluated, and then, the augmenta-
The positioning error time series of DF PPP, MF PPP, and tion effect of PPP-B2b service on positioning accuracy and
reference experiments are very consistent, and the positioning convergence time of real-time BDS-3 SF, DF, and MF PPP is
accuracy after convergence is similar, which is about 15 min analyzed. The PPP-B2b products and the BDS-3 observations
to converge to 0.2 m. ofsixMGEXstationswereusedfromJune1to30,2022.The
In the kinematic model, the median of positioning errors relevant conclusions are as follows.
and convergence time of the six stations are shown in 1) The clock offset STD of MEO and IGSO satellites is
Figs. 9 and 10. The accuracy of SF PPP is relatively poor, 0.118 and 0.237 ns, respectively, which is 75.9% and 61.8%
about 0.2 m in the E and N directions and about 0.4 m higher than that of broadcast ephemeris. The orbit rms of
in the U direction. After convergence of DF PPP and MF MEO and IGSO satellites in the 3-D direction is 0.286 and
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:00:00 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 8 -->

ZHOUetal.:MFBDS-3REAL-TIMEPOSITIONINGPERFORMANCEASSESSMENT 5001
0.447 m, respectively, which are 18.3% and 12.9% higher [12] X. Li et al., “Multi-constellation GNSS PPP instantaneous ambiguity
than that of the broadcast ephemeris. The DCB difference of resolution with precise atmospheric corrections augmentation,” GPS
Solutions,vol.25,no.3,p.107,2021.
B1I/B1Cp/B2ap between the PPP-B2b products and the CAS
[13] M. Glaner and R. Weber, “PPP with integer ambiguity resolution for
productsiswithin2ns,andtheDCBofthePPP-B2bproducts GPSandGalileousingsatelliteproductsfromdifferentanalysiscenters,”
and the TGD has the same accuracy. GPSSolutions,vol.25,no.3,p.102,Jul.2021.
2) In static solutions, the statistical results show that the [14] L.WangandS.Verhagen,“Anewambiguityacceptancetestthreshold
determinationmethodwithcontrollablefailurerate,”J.Geodesy,vol.89,
median positioning accuracy of SF PPP, DF PPP, and MF
no.4,pp.361–375,Apr.2015.
PPP is better than 0.2, 0.09, and 0.08 m, respectively, and the [15] J.Geng,J.Guo,C.Wang,andQ.Zhang,“Satelliteantennaphasecenter
convergencetimeisbetterthan51,10,and8min,respectively. errors: Magnified threat to multi-frequency PPP ambiguity resolution,”
J.Geodesy,vol.95,no.6,p.72,Jun.2021.
Compared with DF PPP, the positioning accuracy of MF PPP
[16] J. Guo, J. Geng, and C. Wang, “Impact of the third frequency GNSS
is increased by 6.1%, 9.5%, and 7.3% in the ENU directions,
pseudorangeandcarrierphaseobservationsonrapidPPPconvergences,”
and the convergence time is increased by 24.8%. GPSSolutions,vol.25,no.2,p.30,Apr.2021.
3) In kinematic solutions, the statistical results show that [17] X.Lietal.,“GalileoPPPrapidambiguityresolutionwithfive-frequency
observations,”GPSSolutions,vol.24,no.1,p.24,2019.
the median positioning accuracy of SF PPP, DF PPP, and
[18] J.Li,Y.Yang,H.He,andH.Guo,“Ananalyticalstudyonthecarrier-
MF PPP is better than 0.4, 0.12, and 0.12 m, respectively, phase linear combinations for triple-frequency GNSS,” J. Geodesy,
and the convergence time is better than 145, 16, and 12 min, vol.91,pp.151–166,Feb.2017.
respectively.ComparedwithDFPPP,thepositioningaccuracy [19] V.Duong,K.Harima,S.Choy,D.Laurichesse,andC.Rizos,“Anopti-
mal linear combination model to accelerate PPP convergence using
of MFPPPis increasedby 4.2%, 7.4%,and 8.2%in theENU
multi-frequency multi-GNSS measurements,” GPS Solutions, vol. 23,
directions, and the convergence time is increased by 27.7%. no.2,p.49,Apr.2019.
4) In general, the positioning accuracy of DF PPP and MF [20] X.ZhangandP.Li,“Benefitsofthethirdfrequencysignaloncycleslip
correction,”GPSSolutions,vol.20,pp.451–460,Jul.2015.
PPP with the PPP-B2b products is relatively consistent, close
[21] S. Ye et al., “A cycle slip fixing method with GPS + GLONASS
tothatofDFPPPusingthefinalpreciseproducts.Intermsof
observationsinreal-timekinematicPPP,”GPSSolutions,vol.20,no.1,
convergence time, the results of MF PPP are better than that pp.101–110,Jan.2016.
of DF PPP, which is consistent with DF PPP using the final [22] Z. Xiaohong and L. Xingxing, “Instantaneous re-initialization in real-
timekinematicPPPwithcycleslipfixing,”GPSSolutions,vol.16,no.3,
preciseproducts,indicatingthattheincreasedobservationscan
pp.315–327,Jul.2012.
effectively accelerate convergence.
[23] W. Zhang, Y. Lou, W. Song, W. Sun, X. Zou, and X. Gong, “Initial
assessment of BDS-3 precise point positioning service on GEO B2b
ACKNOWLEDGMENT signal,”Adv.SpaceRes.,vol.69,no.1,pp.690–700,Jan.2022.
[24] W. Fu, Y. Yang, Q. Zhang, and G. Huang, “Real-time estimation of
The authors thank the IGS for providing the data and
BDS/GPShigh-ratesatelliteclockoffsetsusingsequentialleastsquares,”
products for this study. Adv.SpaceRes.,vol.62,no.2,pp.477–487,Jul.2018.
[25] W.Fu,G.Huang,Q.Zhang,S.Gu,M.Ge,andH.Schuh,“Multi-GNSS
REFERENCES real-time clock estimation using sequential least square adjustment
with online quality control,” J. Geodesy, vol. 93, no. 7, pp.963–976,
[1] C. Zhao, B. Zhang, and X. Zhang, “SUPREME: An open-source
Jul.2019.
single-frequency uncombined precise point positioning software,” GPS
[26] P. Zhou, H. Yang, G. Xiao, L. Du, and Y. Gao, “Estimation of GPS
Solutions,vol.25,no.3,pp.1–9,Jul.2021.
LNAVbasedonIGSproductsforreal-timePPP,”GPSSolutions,vol.23,
[2] Y.Yangetal.,“FeaturedservicesandperformanceofBDS-3,”Sci.Bull.,
no.1,p.27,Jan.2019.
vol.66,no.20,pp.2135–2143,Oct.2021.
[27] X.Lu,L.Chen,N.Shen,L.Wang,Z.Jiao,andR.Chen,“DecodingPPP
[3] Z.Zhang,B.Li,L.Nie,C.Wei,S.Jia,andS.Jiang,“Initialassessment
corrections from BDS B2b signals using a software-defined receiver:
ofBeiDou-3globalnavigationsatellitesystem:Signalquality,RTKand
An initial performance evaluation,” IEEE Sensors J., vol. 21, no. 6,
PPP,”GPSSolutions,vol.23,no.4,Oct.2019.
pp.7871–7883,Mar.2021.
[4] H. Ge, B. Li, M. Ge, Y. Shen, and H. Schuh, “Improving BeiDou
[28] Y. Xu, Y. Yang, and J. Li, “Performance evaluation of BDS-3 PPP-
preciseorbitdeterminationusingobservationsofonboardMEOsatellite
B2b precise point positioning service,” GPS Solutions, vol. 25, no. 4,
receivers,”J.Geodesy,vol.91,no.12,pp.1447–1460,Dec.2017.
pp.1–14,Oct.2021.
[5] Y. Yang, Q. Ding, W. Gao, J. Li, Y. Xu, and B. Sun, “Principle and
performance of BDSBAS and PPP-B2b of BDS-3,” Satell. Navigat., [29] J.Tao,J.Liu,Z.Hu,Q.Zhao,G.Chen,andB.Ju,“Initialassessment
of the BDS-3 PPP-B2b RTS compared with the CNES RTS,” GPS
vol.3,no.1,p.5,Dec.2022.
Solutions,vol.25,no.4,pp.1–16,Oct.2021.
[6] C.Tangetal.,“Orbitdetermination,clockestimationandperformance
evaluationofBDS-3PPP-B2bservice,”J.Geodesy,vol.96,no.9,p.60, [30] Z.Ren,H.Gong,J.Peng,C.Tang,X.Huang,andG.Sun,“Performance
2022. assessment of real-time precise point positioning using BDS PPP-
[7] M. Li, T. Xu, M. Guan, F. Gao, and N. Jiang, “LEO-constellation- B2b service signal,” Adv. Space Res., vol. 68, no. 8, pp.3242–3254,
augmentedmulti-GNSSreal-timePPPforrapidre-convergenceinharsh Oct.2021.
environments,”GPSSolutions,vol.26,no.1,pp.1–12,Jan.2022. [31] Z.Nie,X.Xu,Z.Wang,andJ.Du,“InitialassessmentofBDSPPP-B2b
[8] A.Allahvirdi-Zadeh,K.Wang,andA.El-Mowafy,“PODofsmallLEO service:Precisionoforbitandclockcorrections,andPPPperformance,”
satellites based on precise real-time MADOCA and SBAS-aided PPP RemoteSens.,vol.13,no.11,p.2050,May2021.
corrections,”GPSSolutions,vol.25,no.2,p.31,Apr.2021. [32] Y.Liu,C.Yang,andM.Zhang,“ComprehensiveanalysesofPPP-B2b
[9] E.TunalıandM.T.Özlüdemir,“GNSSPPPwithdifferenttroposphere performance in China and surrounding areas,” Remote Sens., vol. 14,
modelsduringsevereweatherconditions,”GPSSolutions,vol.23,no.3, no.3,p.643,Jan.2022.
p.82,Jul.2019. [33] H.Yang,S.Ji,D.Weng,Z.Wang,K.He,andW.Chen,“Assessmentof
[10] T. Liu, B. Zhang, Y. Yuan, and X. Zhang, “On the application of thefeasibilityofPPP-B2bserviceforreal-timecoseismicdisplacement
the raw-observation-based PPP to global ionosphere VTEC modeling: retrieval,”RemoteSens.,vol.13,no.24,p.5011,Dec.2021.
An advantage demonstration in the multi-frequency and multi-GNSS [34] O. Montenbruck, P. Steigenberger, and A. Hauschild, “Broadcast ver-
context,”J.Geodesy,vol.94,no.1,p.1,Jan.2020. sus precise ephemerides: A multi-GNSS perspective,” GPS Solutions,
[11] Z. Li, N. Wang, L. Wang, A. Liu, H. Yuan, and K. Zhang, “Regional vol.19,no.2,pp.321–333,2015.
ionospheric TEC modeling based on a two-layer spherical harmonic [35] H. Zhou et al., “Impact of higher-order ionospheric delay on the
approximationforreal-timesingle-frequencyPPP,”J.Geodesy,vol.93, reliabilityofRTKambiguityestimation,”Adv.SpaceRes.,vol.69,no.1,
no.9,pp.1659–1671,Sep.2019. pp.727–736,Jan.2022.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:00:00 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 9 -->

5002 IEEESENSORSJOURNAL,VOL.23,NO.5,1MARCH2023
[36] F. Guo, X. Zhang, and J. Wang, “Timing group delay and differential Tao Li received the B.Sc. degree in surveying
codebiascorrectionsforBeiDoupositioning,”J.Geodesy,vol.89,no.5, and mapping engineering from the China Uni-
pp.427–445,May2015. versityofMiningandTechnology,Beijing,China,
[37] X. Lin, L. Baojun, L. Yingchun, X. Sujie, and B. Tao, “Satellite in 2018. He is pursuing the Ph.D. degree with
geometry and attitude mode of BDS-3 MEO satellites developed by WuhanUniversity,Wuhan,China.
SECM,”inProc.31stInt.Tech.MeetingSatell.DivisionInst.Navigat., His research interests include atmosphere
2018,pp.1268–1289. delay modeling and low Earth orbit (LEO) nav-
[38] Y.Yangetal.,“BeiDou-3broadcastclockestimationbyintegrationof igationaugmentationtechnology.
observationsofregionaltrackingstationsandinter-satellitelinks,”GPS
Solutions,vol.25,no.2,p.57,Apr.2021.
[39] N.Wang,Y.Yuan,Z.Li,O.Montenbruck,andB.Tan,“Determination
ofdifferentialcodebiaseswithmulti-GNSSobservations,”J.Geodesy,
vol.90,no.3,pp.209–228,2016.
YuanWureceivedtheB.S.degreeincomputer
scienceandtechnologyfromSouthwestUniver-
sity, Chongqing, China, in 2016, and the M.S.
degreeincomputerapplicationtechnologyfrom
Haitao Zhou received the M.S. degree in
theInstituteofAutomation,ChineseAcademyof
geodesy and surveying engineering from
Sciences, China, in 2019. He is currently pur-
InformationEngineeringUniversity,Zhengzhou,
suing the Ph.D. degree in geodesy and survey
China,in2016.HeispursuingthePh.D.degree
engineering with the State Key Laboratory of
in geodesy and surveying engineering with
InformationEngineeringinSurveying,Mapping,
WuhanUniversity,Wuhan,Hubei,China.
andRemoteSensing,WuhanUniversity,China.
His research interests include surveying
Hisresearchinterestsincludeindoorposition-
data processing and global navigation satellite
ing and navigation, information fusion, data-driven navigation, and
system(GNSS)precisepositioning.
location-basedservices.
Wenju Fu received the Ph.D. degree from Ruizhi Chen is a Professor and the Direc-
Chang’anUniversity,Xi’an,China,in2018. tor of the State Key Laboratory of Information
He is currently a Postdoctoral Researcher EngineeringinSurveying,MappingandRemote
with the State Key Laboratory of Informa- Sensing,WuhanUniversity,Wuhan,China,and
tion Engineering in Surveying, Mapping and anAcademicianoftheFinnishAcademyofSci-
Remote Sensing (LIESMARS), Wuhan Uni- enceandLetters,SuomalainenTiedeakatemia-
versity, Wuhan, China. His research inter- Academia Scientiarum Fennica, Finland. He is
ests include global navigation satellite system an international scholar working in the field
(GNSS)precisepointpositioning,precisesatel- of navigation and positioning. He is committed
liteclock,andlowEarthorbit(LEO)applications. to the theoretical research and core technol-
ogy development for seamless indoor/outdoor
positioningusingsmartphones.
Lei Wang received the Ph.D. degree in elec-
tronicalengineerandcomputerscience(EECS)
Juanjuan Li received the master’s degree in
from the Queensland University of Technology,
geodesyandsurveyingengineeringfromWuhan
Brisbane,QLD,Australia,in2015.
University,Wuhan,China,in2009.
HeiscurrentlyanAssociateResearchFellow
She is a Senior Engineer with the 54th
with the State Key Laboratory of Information
ResearchInstituteofChinaElectronicsTechnol-
EngineeringinSurveying,MappingandRemote
ogy Group Corporation (CETC), Shijiazhuang,
Sensing,WuhanUniversity,Wuhan,China. His
China. Her research interests include global
research interests include precise global navi-
navigationsatellitesystem(GNSS)receiversig-
gationsatellitesystem(GNSS)positioning,low
nalprocessingandpositioning.
Earth orbit (LEO) orbit determination and navi-
gationaugmentation,andindoorpositioning.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:00:00 UTC from IEEE Xplore. Restrictions apply.