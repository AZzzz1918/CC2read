<!-- PAGE: 1 -->



Citation: Liu, Y.; Yang, C.; Zhang, M.
Comprehensive Analyses of PPP-B2b
Performance in China and
Surrounding Areas. Remote Sens.
2022, 14, 643. https://doi.org/
10.3390/rs14030643
Academic Editors: Yunbin Yuan and
Baocheng Zhang
Received: 8 December 2021
Accepted: 26 January 2022
Published: 28 January 2022
Publisher’s Note: MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional afﬁl-
iations.
Copyright:
© 2022 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
remote sensing 
Article
Comprehensive Analyses of PPP-B2b Performance in China and
Surrounding Areas
Yan Liu, Cheng Yang *
and Mengni Zhang
School of Land Science and Geomatics, China University of Geosciences, Beijing 100083, China;
2012190026@cugb.edu.cn (Y.L.); 2112210060@email.cugb.edu.cn (M.Z.)
* Correspondence: c.yang@connect.polyu.hk
Abstract: BeiDou Global Navigation Satellite System (BDS-3) provides a regional Precise Point Posi-
tioning (PPP) service, called PPP-B2b, for users in China and surrounding areas through B2b signal
transmitted from its three geostationary earth orbit (GEO) satellites. The information broadcasted by
the B2b signal include satellite orbit corrections, satellite clock offset corrections, and differential code
bias (DCB) corrections of BDS-3 satellites. In this study, the accuracies of PPP-B2b corrections along
with real-time PPP performance are comprehensively evaluated referenced to precise orbit and clock
products from GFZ and the precise DCB products from CAS. The result indicates that the accuracy
of the BDS-3 broadcast orbit is similar to that of the PPP-B2b real-time orbit. The PPP-B2b clock
offset correction improved the satellite clock offset precision of the BDS-3 broadcast ephemeris. The
Signal-in-Space Range Error (SISRE) of broadcast ephemeris and PPP-B2b are calculated, which are
0.536 and 1.24 m, respectively. The large SISRE value of PPP-B2b is caused by the satellite-speciﬁed
systematic bias to IGS ﬁnal products. The positioning performance evaluation of real-time PPP with
B2b service is carried out and compared with the real-time product provided by Wuhan University
(WHU) based on the eight IGS MGEX stations in China and surrounding countries. The positioning
accuracy of static positioning mode with PPP-B2b service achieved centimeter-level accuracy in the
selected station, and that of kinematic positioning mode achieved decimeter-level accuracy. The
availability rate of PPP-B2b corrections in the surrounding area of China, however, degrades from
88.76% to 60.91% in the selected stations. The accuracy of the PPP solution using PPP-B2b correction
is better than that of using WHU real-time product within China. The positioning performance of
stations located at the boundary of the PPP-B2b service area, however, is affected by the number of
PPP-B2b available satellites. The positioning accuracy in kinematic positioning mode is worse than
that of using WHU real-time precise product.
Keywords: BDS-3; PPP-B2b; real-time PPP; matching strategy; accuracy assessment
1. Introduction
BeiDou Navigation Satellite System (BDS), like other Global Navigation Satellite Sys-
tems (GNSSs), aims to provide positioning, navigation, and timing (PNT) services for
global users [1]. The initial BDS demonstration navigation system (BDS-1) was established
in 2003, and it consisted of three geostationary orbit (GEO) satellites. The system provided
positioning, timing, and short message communication services with transparency retrans-
mission mode. The BDS regional navigation satellite system (BDS-2) started its service
on 27 December 2012. The constellation consisted of ﬁve GEO satellites, ﬁve inclined
geosynchronous orbit (IGSO) satellites, and four medium Earth orbit (MEO) satellites.
BDS-2 broadcasted three frequency signals, 1561.098 MHz (B1I), 1207.140 MHz (B2I), and
1268.520 MHz (B3I), covering the Asia-Paciﬁc region. The BDS-2 continued the services
of BDS-1, and further provided kinematic positioning in three dimensions. The global
constellation of BDS-3 completed on 23 June and provided global service on 31 July 2020.
The constellation consists of 24 MEO satellites, 3 GEO satellites, and 3 IGSO satellites. The
Remote Sens. 2022, 14, 643. https://doi.org/10.3390/rs14030643
https://www.mdpi.com/journal/remotesensing

> [5 Figure(s)]

<!-- PAGE: 2 -->

Remote Sens. 2022, 14, 643
2 of 28
system not only broadcasts the B1I and B3I signals, but also broadcasts 1575.420 MHz
(B1C), 1207.140 MHz (B2b), and 1176.45 MHz (B2a) by MEO satellites for global positioning
users [2]. In addition to providing global PNT services, regional and global short message
communications (SMC) services, the international search and rescue (SAR) services, and
regional precise point positioning (PPP) services are also provided. The service coverage
area of PPP-B2b is between 80◦E and 155◦E longitude, 5◦S and 55◦N latitude [3]. The
correction parameters contain precise orbit correction parameters, clock offset correction
parameters, and differential code bias (DCB).
PPP is able to achieve decimeter or centimeter-level positioning accuracy using a stan-
dalone GNSS receiver with precise satellites orbit and clock products [4–9]. Currently, the
real-time services (RTS) of International GNSS services (IGS) provides the precise satellite
orbit and clock products to global users through the internet. The internet connection,
however, affects the integrity of the correction data, which further affects the performance
of PPP. In addition to IGS RTS, commercial companies, such as StarFire of NavCom and
RTX of Trimble, also provide RTS for PPP by broadcasting the correction parameters via
satellites communication links [10–13]. The cost requirement of satellite-based RTS limited
the application to ordinary users. Furthermore, the Galileo satellite system can also provide
decimeter horizontal positioning accuracy by shortening the ephemeris updating rate,
resulting in smaller SISRE [14]. The BDS-3, however, provides a regional PPP service in a
different way (called PPP-B2b) using the accurate ephemeris broadcast by B2b signals of
GEO satellites, which allows users to perform PPP for free and without the internet.
The performances of the PPP-B2b service have been evaluated with the stations within
China territory. A software-deﬁned receiver is used to evaluate the performance of the
BDS-3 real-time PPP service. It is stated that the PPP-B2b signal can provide a stable PPP
service for users in the Asia-Paciﬁc region with decimeter to centimeter-level orbit cor-
rections and meter-level clock corrections [15]. Referenced to precise ephemeris products
from Deutsches GeoForschungsZentrum (GFZ), Germany and RTS of Centre National
d’Etudes Spatiales (CNES), France, some performance evaluation studies on the PPP-B2b
proved that the PPP-B2b can achieve decimeter or centimeter-level accuracy for static and
kinematic positioning [16–18]. A comprehensive evaluation for PPP-B2b performance, in
terms of message matching strategy, service availability, and correction accuracy, has been
conducted [10]. The study further analyzes the decimeter and centimeter-level positioning
accuracy of PPP-B2b with different ionosphere-free (IF) combinations. Usually, most perfor-
mance evaluations of the PPP-B2b have been focused on the selected IGS or international
GNSS Monitoring and Assessment System (iGMAS) stations within China territory. The
real-time performance of the BDS-3 PPP-B2b service around China, however, needs to be
further evaluated. In this paper, the BDS-3 real-time PPP-B2b performance, in terms of
availability and accuracy, is assessed by the stations located in China and the surround-
ing countries, such as Korea, Japan, and Mongolia. The performance of PPP-B2b is also
compared with solutions acquired from the real-time product of Wuhan university (WHU).
The paper is organized as follows: in Section 2, the PPP-B2b correction parameters and
the corresponding matching strategy are brieﬂy described. The performance assessment
methods for PPP-B2b correction parameters are described in detail. In addition, the IF
model of real-time PPP is also introduced to evaluate the positioning performance of the
real-time PPP service of BDS-3. In Section 3, the accuracy of the PPP-B2b satellite orbit
correction, and clock offset correction are evaluated and compared to the real-time product
from WHU. The SISRE and orbit only SISRE of broadcast ephemeris, PPP-B2b correction
product are then calculated and compared to that of real-time product from WHU, and
the DCB corrections are evaluated as well. The positioning performance assessment
and comparison to WHU real-time products are performed. Finally, some conclusions
are summarized.

<!-- PAGE: 3 -->

Remote Sens. 2022, 14, 643
3 of 28
2. Methodology
In this section, the correction message of PPP-B2b is brieﬂy introduced, and the
matching strategies of the correction parameter are presented. The correction models
of the satellite orbit, satellite clock, and code bias are discussed afterward. Finally, the
performance assessment methods of PPP-B2b are presented, in terms of orbit accuracy,
clock offsets, SISRE, and differential code bias, as well as the PPP IF model.
2.1. PPP-B2b Correction Message and Matching Strategy
The PPP-B2b signals of the GEO satellites of BDS-3 broadcast ﬁve parameters: satellite
mask, satellite orbit and clock offset corrections, DCB, and user range accuracy index
(URAI). These ﬁve parameters and corresponding message types, along with nominal
validities, which indicate the validate durations of information, are listed in Table 1 [19].
The update rate of satellite orbit and clock offset corrections are 48 and 6 s, respectively [19].
Table 1. PPP-B2b message information.
Information Content
Message Type
Nominal Validity(s)
Satellite mask
1
–
Orbit correction
2,6,7
96
DCB
3
86,400
Clock correction
4,6,7
12
URAI
2,5,6,7
96
To ensure the correct matching between the correction information and the broadcast
ephemeris, the Issue of Data (IOD) is employed as a matching indicator. These IODs
include: IOD of state space representation (IOD SSR), IOD of pseudo-random noise mask
(IODP), and IOD of navigation (IODN), as well as the IOD of orbit and clock corrections
(IOD Corr). The matching strategy is illustrated in Figure 1. It should be noted that the
DCB parameter is not included in this matching strategy because it does not change within
a day.
 
Figure 1. Matching strategy.

> [1 Figure(s)]


|Content Message|Type Nominal|
|---|---|
|<br>||



<!-- PAGE: 4 -->

Remote Sens. 2022, 14, 643
4 of 28
As shown in Figure 1, the retrieved IOD SSRs from those messages should remain
consistent with each other, and the received PPP-B2b correction messages should be within
the nominal validity period as listed in Table 1. To acquire the correct satellite clock
correction information, the satellite PRN is decoded if the same IODP is acquired from
message types 1 and 4. The satellite clock correction index and IOD Corr of the certain
satellite could be obtained from message type 4 afterward. The orbit correction information,
including satellite PRN, corresponding IOD Corr, and related IODN, can be acquired
from message type 2. If the IODN matches the IOD of clock (IODC) from the broadcast
ephemeris, and the IOD Corr from orbit correct information matches that from clock
correction information, the precise orbit and clock correction can be used for the real-time
PPP solution.
2.2. PPP-B2b Correction Message Evaluation Methods
The satellite orbit correction message of the PPP-B2b contains the orbit correction
vector δO =

δOr, δOa, δOc
T in radial, along-track, and cross-track components, respec-
tively. The real-time precise orbit thus can be obtained by transforming the correction vector
to the Earth-Center-Earth-Fixed (ECEF) frame as expressed in Equations (1) and (2) [19],
δX =
h
eradial ealong ecross
i
δO
eradial =
rs
|rs|
ecross =
rs×vs
|rs×vs|
ealong = ecross × eradial
(1)
Xpre,B2b = Xbrdc −δX
(2)
where δX is the orbit correction vector in ECEF coordinate system; rs and vs are the satellite
position and velocity vectors calculated from the broadcast ephemeris, respectively; Xbrdc
is the satellite position vector from the broadcast ephemeris in the ECEF frame; Xpre,B2b is
the corrected real-time precise satellite position vector in the ECEF frame.
The clock offset correction is directly related to the satellite clock offset obtained from
the broadcast ephemeris. Hence, the real-time precise satellite clock offset can be retrieved
directly [19],
dts
pre,B2b = dts
brdc −C0
c
(3)
where dts
pre,B2b is the precise satellite clock offset corrected by PPP-B2b correction message;
dts
brdc is the satellite clock offset derived from the broadcast ephemeris; C0 is the PPP-B2b
clock correction value; c is the velocity of light.
DCB is caused by code-based hardware delay difference between different frequencies,
and affects the performance of PPP [20]. The DCB could be corrected by broadcast PPP-B2b
correction messages [19],
ePf req = Pf req −DCBf req
(4)
where ePf req is the corrected pseudorange observation of the certain frequency freq; Pf req is
the observed pseudorange value; DCBf req is the PPP-B2b DCB corrections for correspond-
ing signals of BDS-3 in meters.
To evaluate the performance of satellite orbit, clock offset and DCB recovered from the
PPP-B2b messages, the ﬁnal products from GFZ and the Chinese Academy of Sciences (CAS)
are used as a reference. IGS also initiated the experimental multi-GNSS orbit combination
service [21], however, only precise orbit products are available at the present stage. Thus,
in the study, the precise orbit and clock product from GFZ are employed as reference.
The accuracy of BDS-3 broadcast ephemeris, and PPP-B2b real-time orbit and clock offset,
are further compared to WHU real-time products. The precise orbit product from GFZ
is referred to the center-of-mass (CoM) of the satellite, while the BDS-3 precise orbit

<!-- PAGE: 5 -->

Remote Sens. 2022, 14, 643
5 of 28
information retrieved from the PPP-B2b message referred to the antenna phase center
(APC) of the satellite [22]. Therefore, the phase center offset (PCO) correction between the
GFZ ﬁnal orbit and the PPP-B2b orbit should be employed. The precise orbit error of the
PPP-B2b with respect to GFZ ﬁnal product can be written as [23],
δXpre = Xpre,GFZ −
h
Xpre,B2b + A·δXpco
i
(5)
where δXpre is the precise orbit error vector; Xpre,GFZ is the reference orbit vector obtained
from GFZ; Xpre,B2b is the real-time PPP-B2b precise orbit vector; A is the satellite attitude
matrix; δXpco is the satellite PCO correction vector obtained from the latest “igs14.atx”
ﬁle released by IGS. The orbit error vector in satellite radial, along-track, and cross-track
components then can be expressed as,
δOpre =
 eradial ealong ecross
T·δXpre
(6)
where δOpre is the satellite precise orbit error vector in radial, along-track, and cross-track
components with respect to the ﬁnal product from GFZ; other parameters are deﬁned
as above.
The PPP-B2b satellite clock offset is compared to precise clock offset products from
GFZ. The timescale and frequency references of the GFZ ﬁnal satellite clock offset products,
however, are different from those of the PPP-B2b satellite clock offset. The GPS system
time (GPST) is adopted for the GFZ ﬁnal clock product rather than the BDS time (BDT).
The time offset, 14s, between the different time systems needs to be compensated before
the evaluation. Moreover, the ﬁnal satellite clock offset of GFZ uses the B1I and B3I IF
combination as the reference signal, while the PPP-B2b satellite clock offset is referred to
B3I signal frequency [18,24]. Hence, the corrections of the satellite hardware delays should
be applied, which referred to the broadcasted DCB from PPP-B2b signals [25],
δts
pre,B2b = dts
pre,B2b −
f 2
B1I
f 2
B1I −f 2
B3I
DCBs
B1I
(7)
where δts
pre,B2b is the PPP-B2b satellite clock offset referred to B1I/B3I IF combination after
DCB correction; f 2
B1I and f 2
B3I are the frequencies of B1I and B3I signals, respectively.
The difference in the satellite clock offsets between the PPP-B2b ephemeris and the
GFZ products is
∆δts = δts
pre,B2b −δts
pre,GFZ
(8)
where the ∆δts is the satellite clock offset difference between PPP-B2b ephemeris and
GFZ ﬁnal clock product of the satellite s; the δts
pre,GFZ is the precise satellite clock offset
calculated by GFZ ﬁnal products.
The precise satellite clock offset products from different analysis centers (ACs), how-
ever, have timescale differences. This systematic error is commonly reduced by subtracting
the clock offset of the reference satellite [26]. In our case, it is hard to evaluate the PPP-B2b
satellite clock offset based on a ﬁxed reference satellite with 24 h continuous availability.
Thus, the clock systematic error is reduced by subtracting the average clock offset from
∆δts at each epoch, which forms the single difference between the PPP-B2b clock offset and
the precise clock offset from GFZ,
∇∆δts = ∆δts −1
M
M
∑
i=0
∆δti
(9)
where ∇∆δts is the clock offset difference sequence; M is the available satellite number
from PPP-B2b signal at each epoch. However, the available satellite number M may change
at each epoch. The time sequence of ∇∆δts becomes discontinuous which affects the

<!-- PAGE: 6 -->

Remote Sens. 2022, 14, 643
6 of 28
reliability of clock offset standard deviation (STD). Therefore, the time series ∇∆δts
i needs
to be re-edited properly [17],
^
∇∆δts
t = ∇∆δts
t −∆Dt,t−1
∆Dt,t−1 =









1
M
M
∑
i=0
∆∇∆δti
t,t−1

1
M
M
∑
i=0
∆∇∆δti
t,t−1
 ≥0.1ns
0

1
M
M
∑
i=0
∆∇∆δti
t,t−1
 < 0.1ns
∆∇∆δti
t,t−1 = ∇∆δti
t −∇∆δti
t−1
(10)
where ^
∇∆δts
t is the re-edited time sequence; ∆Dt,t−1 is the systematic error compensation
term which is signiﬁcantly affected by the number of available satellites; ∆∇∆δti
t,t−1 is the
time difference of ∇∆δti
t between epochs t and t −1 for satellite i.
The signal-in-space range error (SISRE) is a key performance indicator for PPP-b2b
orbit and clock errors [25]. Usually, the global average SISRE is employed to evaluate the
performances of different constellations and different precise products [14,27–31]. In this
study, the SISRE of broadcast ephemeris, PPP-B2b corrected orbit, and clock and WHU
real-time product are calculated based on the following equation [31],
SISRE =
q
(RMS(wRδR −δT))2 + w2
A,C(A2 + C2)
(11)
where wR and w2
A,C are constellation-speciﬁc weight factors with values of 0.98 and 1/54
for BDS-3 [17,22]; δR is the radial error components; δT is the satellite clock error with
respect to GFZ ﬁnal clock product; A, C are the RMS of along-track and cross-track error
components, respectively. The orbit-only SISRE for BDS-3 MEO satellites are also calculated
to evaluate the performances of PPP-B2b real-time orbits
SISREorbit =
q
w2
Rδ2
R + w2
A,C(A2 + C2)
(12)
The DCB corrections broadcasted by PPP-B2b can be evaluated by comparing with
precise MGEX DCB products derived by the Chinese Academy of Sciences (CAS). The
CAS DCB products currently provide DCB corrections for BDS-3 satellites from C19 to
C46 with approximately 0.17 ns stability over a month [32]. The relationship between the
PPP-B2b DCB corrections and the CAS DCB corrections can be expressed by the following
expression [33],
DCBB1I,B2b = DCBC2I−C6I,CAS
DCBB1Cp,B2b = DCBC1P−C6I,CAS
DCBB2ap,B2b = DCBC1P−C6I,CAS −DCBC1P−C5P,CAS
(13)
where DCBsig,B2b and DCBsig1−sig2,CAS are the DCB corrections obtained from PPP-B2b
service and CAS ﬁnal products, respectively. The subscripts C2I and C6I denote B1I and
B3I signals, respectively; C1P denotes B1Cp signal; C5P denotes B2ap signal.
2.3. Real-Time IF-PPP Model with PPP-B2b Corrections
The performance of PPP-B2b signal is further evaluated with PPP positioning accuracy.
The multi-frequency pseudorange and carrier phase observations at the ith frequency can
be written as [34],
Pi = ρ + c(dtr −dts) + f 2
1
f 2
i I1 + Mw·Tzwd + Tzhd + Br,i −Bs
i + εPi
Li = ρ + c(dtr −dts) −f 2
1
f 2
i I1 + Mw·Tzwd + Tzhd + λi
 Ni + br,i −bs
i
 + εLi
(14)

<!-- PAGE: 7 -->

Remote Sens. 2022, 14, 643
7 of 28
where Pi and Li are the observations of pseudorange and carrier phase at frequency fi; ρ
is the geometric distance between satellite and receiver; c is the speed of light; dtr and dts
are the satellite and receiver clock offset, respectively; I1 is the ionospheric delay of L1;
Tzwd is the zenith wet tropospheric delay and Mw is the corresponding mapping function;
Tzhd is the zenith hydrostatic tropospheric delay; Br,i and Bs
i are the pseudorange hardware
delays of the receiver and satellite; λi and Ni are the wavelength and the integer ambiguity
of frequency fi; br,i and bs
i are the carrier phase hardware delays of the receiver and
satellite; εPi and εLi are the observation noise and unmodeled errors of the pseudorange
and carrier phase.
The receiver hardware delay can be absorbed in the receiver clock offset. The satellite
clock offset and the satellite hardware delay can be compensated by PPP-B2b clock offset
correction and DCB correction, respectively. The other errors, such as zenith hydrostatic
tropospheric delay, relativistic effect, phase windup effect, Sagnac effect, are corrected
by the corresponding model. Ignoring the observation noise, we write the linearized
observation equation of the dual-frequency IF combination as [35],
PIFij = −e·r + c·δtr + Mw·Tzwd
LIFij = −e·r + c·δtr + Mw·Tzwd + λIFij NIFij
(15)
where PIFij and LIFij are the pseudorange and carrier phase IF combination values at fi and
fj frequencies after error correction; e is the unit vector of receiver-to-satellite direction; r is
the receiver position incremental vector; δtr is the receiver clock offset contains receiver
hardware delay; λIFij and NIFij are the combined wavelength and the combined ambiguity
which absorbs the carrier phase hardware delay and no longer has an integer characteristic.
The error equation is then expressed as:
V = HX −l
(16)
where H is the design matrix; X =

r
c·δtr
Tzwd
NIF

is the estimated parameters;
and l is the measurements vector after the corresponding error has been modeled properly.
3. Experimental Evaluation
In this section, the MEO satellites of BDS-3 are used to evaluate the PPP-B2b perfor-
mance, in terms of satellite orbit and clock, SISRE, as well as DCB accuracy, referenced
to precise products from GFZ. The accuracy of the orbit and the clock offset of the GFZ
precise products achieved centimeter-level accuracy for BDS-3 MEO satellites [36,37]. The
accuracy of PPP-B2b real-time orbit and clock offsets are further compared to the real-time
products from WHU. In addition to the accuracy assessment of the PPP-B2b correction mes-
sage, the performance evaluation of the real-time PPP was also conducted with eight IGS
stations distributed in the service area. The corresponding CNAV1 broadcast ephemerides
of BDS-3 are downloaded from the Test and Assessment Research Center of China Satellite
Navigation Ofﬁce (csno-tarc.cn/datacenter/ephemeris, accessed on 7 December 2021).
3.1. PPP-B2b Orbit Accuracy Assessment
The PPP-B2b orbit correction sequences of the MEO satellites of BDS-3 decoded from
the PPP-B2b message on 9 August 2021 (DoY 221) are shown in Figure 2. The variations
in orbit correction sequence for MEO satellites are within 0.1, 0.3, and 0.3 m in radial,
along-track, and cross-track components, respectively. The centimeter-level corrections
indicate that considerable accuracy could be achieved by the broadcast orbits of BDS-3
MEO satellites, which mainly beneﬁts from the application of inter-satellite links (ISL)
technology [38]. Figure 2 also reveals the hourly discontinuity of the orbit correction series,
which is related to the hourly update of the broadcast ephemeris [39].

<!-- PAGE: 8 -->

Remote Sens. 2022, 14, 643
8 of 28
Figure 2. PPP-B2b orbit corrections of BDS-3 MEO on Doy 221.
The real-time orbit errors in radial, along-track, and cross-track components for the
PPP-B2b referenced to the ﬁnal precise orbit from GFZ are presented in Figure 3a, and
those of broadcast ephemeris are presented in Figure 3b. The WHU real-time orbit errors
referenced to GFZ ﬁnal products are plotted in Figure 3c. The orbit errors for both real-
time PPP-B2b orbit and broadcast orbit exhibit the same level of accuracy. The real-time
orbit error series of PPP-B2b is smoother and more continuous than that of the broadcast
orbit error. The orbit error of WHU real-time product is more continuous and smoother,
and more consistent with the GFZ ﬁnal orbit product. The satellite orbit errors of C41
and C42 of the PPP-B2b real-time orbits show some abnormal errors with 0.6 m in radial
components, compared to the ﬁnal precise orbit from GFZ. The signiﬁcant difference in the
orbits between the PPP-B2b and that of GFZ may relate to the PCO corrections released by
IGS. To further analyze this orbit bias, the orbit errors in radial, along-track, and cross-track
components that apply the PCO corrections provided by China Satellite Navigation Ofﬁce
(CSNO) are presented in Figure 4. The abnormal orbit error of the satellites C41 and C42
no longer exist, but satellite orbit C44 appeared to have a signiﬁcant bias, with about
1 m, on the radial component. Thus, the signiﬁcant biases on satellite orbits are related to
difference in the PCO corrections, which do not participate in real-time PPP solutions with
PPP-B2b signals.

<!-- PAGE: 9 -->

Remote Sens. 2022, 14, 643
9 of 28
Figure 3. Orbit errors of PPP-B2b real-time orbit (a), broadcast orbit (b), and WHU real-time orbit (c).

> [1 Figure(s)]

<!-- PAGE: 10 -->

Remote Sens. 2022, 14, 643
10 of 28
Figure 4. Orbit errors of PPP-B2b orbit by applying PCO corrections from CSNO.
To further evaluate the accuracy of satellite orbits of PPP-B2b products, the Root
Mean Square Error (RMSE) of PPP-B2b real-time orbits, broadcast orbits, and real-time
orbits from WHU based on a 7-day dataset (6–12 August 2020) are presented in Figure 5.
The RMSE of different satellite orbits also indicates that the radial components of both
PPP-B2b orbit and broadcast orbit have better performance than that of the along-track and
cross-track components. The higher accuracy on the radial component is mainly related
to the high-quality onboard hydrogen and rubidium clocks, which compensate for the
systematic error in the radial component [31]. The corresponding average RMSEs of the
BDS-3 MEO satellites are listed in Table 2. The average RMSE of PPP-B2b orbits is 8.5, 19.3,
14.0 cm in radial, along-track, and cross-track components, respectively. The difference
between the PPP-B2b orbit and the broadcast orbit is only centimeter-level. This slight
accuracy improvement may be related to the better continuity of the PPP-B2b orbit than
that of the broadcast orbit. The WHU real-time orbits exhibit better accuracy than that of
PPP-B2b orbits. The RMSE of WHU real-time orbits on radial, along-track, and cross-track
components are 4.6, 8.1, and 6.1 cm, respectively. The better accuracy of the WHU real-time
orbit is mainly beneﬁted by the global GNSS network, while the PPP-B2b service only relies
on the regional monitoring stations in China.
Table 2. Mean orbit RMSEs (cm) of BDS-3 MEO.
RMSE
Radial
Along-Track
Cross-Track
PPP-B2b
8.5
19.3
14.0
Broadcast
8.8
20.7
15.4
WHU
4.6
8.1
6.1

<!-- PAGE: 11 -->

Remote Sens. 2022, 14, 643
11 of 28
Figure 5. Orbit RMSEs of PPP-B2b orbit (a), broadcast orbit (b), and WHU real-time orbit (c).
3.2. PPP-B2b Clock Offset Accuracy Assessment
The PPP-B2b clock offset correction sequences of BDS-3 MEO satellites on DoY 221 are
shown in Figure 6a. The PPP-B2b clock offset corrections of each satellite are within 3 m
and contain systematic offsets. The details of clock offset correction parameters of satellites
C24, C35, and C44 are presented in Figure 6b. It is easy to ﬁnd that the corrections of these
three satellites ﬂuctuate around constant values of about −1, 2, and 0 m, respectively. The
corrections also exhibit discontinuity in hourly duration, which is also consistent with the
update frequency of the broadcast ephemeris.
The error sequences of broadcast clock offset and the PPP-B2b clock offset referenced to
GFZ precise clock offsets are presented in Figure 7a,b, respectively. As shown in Figure 7b,
the continuity of the broadcast satellite clock offset is signiﬁcantly improved by applying
the PPP-B2b clock offset corrections. However, individual clock offset biases still exist in
the clock offset error sequence. To effectively evaluate the accuracy of the PPP-B2b satellite
clock offsets, the individual clock offset biases need to be corrected by subtracting the
average clock offset, as described in re-edit Equations (9) and (10).
The series of re-edit clock offset differences of the broadcast satellite, and that of
the PPP-B2b corrections, as well as the errors of WHU real-time clock offset are shown
in Figure 8. The re-edit clock offset bias of the PPP-B2b becomes smoother and more
continuous. As shown in Figure 8b, the clock offsets of PPP-B2b, however, clearly exhibit
satellite-speciﬁed systematic errors. For example, the real-time PPP-B2b clock bias of
satellite C35 reaches 5 ns, which results in more than 1.5 m systematic bias. The study
revealed that these satellite-speciﬁed systematic errors are related to the pseudorange
observations [28]. If carrier phase observations are used for positioning, the satellite-
speciﬁed systematic errors can be absorbed by ambiguities [10,28].

<!-- PAGE: 12 -->

Remote Sens. 2022, 14, 643
12 of 28
 
Figure 6. PPP-B2b clock offset corrections of all MEO satellites (a) and that of C24, C35, and C44 in
detail (b).
Figure 7. Satellite clock offset error sequences of broadcast clock offset (a) and PPP-B2b clock offset (b).

> [2 Figure(s)]

<!-- PAGE: 13 -->

Remote Sens. 2022, 14, 643
13 of 28
Figure 8. Satellite clock offset re-edit error sequences of broadcast clock offsets (a) and PPP-B2b clock
offsets (b), WHU real-time clock offset (c).
As the satellite-speciﬁed systematic errors existed in the BDS-3 real-time clock prod-
ucts, the STD values acquired from re-edited error sequences of BDS-3 MEO satellites over
a 7-day period are summarized and presented in Figure 9. The STD of PPP-B2b clock
offsets is within 0.25 ns. The average STD of the PPP-B2b clock offsets is 0.124 ns, which
is signiﬁcantly improved compared to that of the broadcast clock offsets with the STD
of 0.672 ns. The average STD of PPP-B2b clock offsets is also smaller than that of WHU
real-time clock product, which is 0.360 ns.
Figure 9. Satellite clock offset STD.

> [2 Figure(s)]

<!-- PAGE: 14 -->

Remote Sens. 2022, 14, 643
14 of 28
3.3. PPP-B2b SISRE Performance Evaluation
The RMSs of SISRE and orbit only SISRE, as well as the STD of SISRE of broadcast
ephemeris, PPP-B2b and WHU real-time products for BDS-3 MEO satellites during the
7d test period were calculated. The RMS SISRE of each satellite is plotted in Figure 10.
The average RMS SISRE of broadcast ephemeris, PPP-B2b corrected products, and the
real-time products from WHU are 0.536, 1.242, and 0.137 m, respectively. The largest SISRE
of PPP-B2b occurred in satellite C35 with a value of 2.93 m, due to its outlying real-time
clock offset with a value of 5 ns. The orbit only SISRE is plotted in Figure 11. The results
show that the orbit only SISRE of PPP-B2b is similar to that of WHU real-time product. The
abnormal SISRE value of PPP-B2b and the broadcast ephemeris on C41 and C42 are caused
by PCO corrections. Thus, it can be conﬁrmed that the large RMS SISRE value of PPP-B2b
corrected products is mainly caused by the satellite-speciﬁed systematic error on clock
offset. To exclude the systematic error effect on SISRE evaluation, the STD SISRE is also
calculated and presented in Figure 12. The average STD SISRE of PPP-B2b is 0.097 m, which
is similar to that of WHU real-time product. The average SISRE values are summarized in
Table 3.
Figure 10. SISRE RMS of PPP-B2b, broadcast ephemeris, and WHU real-time products.
Figure 11. Orbit only SISRE RMS of PPP-B2b, broadcast ephemeris, and WHU real-time products.
 
Figure 12. SISRE STD of PPP-B2b, broadcast ephemeris, and WHU real-time products.

<!-- PAGE: 15 -->

Remote Sens. 2022, 14, 643
15 of 28
Table 3. Average RMS and STD values of the SISRE for PPP-B2b, broadcast ephemeris, and WHU
real-time products.
PPP-B2b
Broadcast
WHU
SISRE RMS (m)
1.242
0.536
0.137
SISRE STD (m)
0.097
0.261
0.102
3.4. PPP-B2b DCB Accuracy Assessment
The PPP-B2b DCB and TGD from the broadcast ephemeris are converted to the same
reference as the CAS DCB products. The PPP-B2b DCB, broadcast TGD, and CAS DCB of
three signals, B1I, B1Cp, and B2ap, are plotted in Figure 13a,b,c, respectively. Differences
between PPP-B2b DCB and CAS DCB, broadcast TGD and CAS DCB, are also plotted with
blue and red bars in the corresponding ﬁgures. As shown in Figure 13a, the PPP-B2b DCBs
and TGD of the B1I signal are consistent with that of CAS DCB. Some systematic errors
exist between CAS DCB and PPP-B2b DCBs, as well as CAS DCB and the broadcast TGD
of B1Cp and B2ap signals, as shown in Figure 13b,c, respectively. The biases on B1Cp and
B2ap signals are 2 and 10 ns, respectively. In addition, the STD values of the B1I signal,
B1Cp signal, and the B2ap signal are 0.46, 0.54, and 0.47 ns, respectively.
3.5. Real-Time PPP Positioning Accuracy Assessment
The positioning results on DOY 221 of eight IGS MEGX stations in China and sur-
rounding counties were used to assess the positioning accuracy of the PPP-B2b services,
as shown in Figure 14. The red dash indicates the service area of the PPP-B2b signal. The
corresponding observation ﬁles were downloaded from the File Transfer Protocol Server
(FTP) of GFZ. Both static and kinematic mode PPP were processed with B1I/B3I IF com-
binations. The processing strategies are shown in Table 4 in detail. In this section, three
stations, JFNG, MIZU, and SGOC are employed, to demonstrate the performance of the
PPP-B2b service. The JFNG station is located in China, while the MIZU station and the
SGOC station are situated in Japan and Sri Lanka, the boundary of the PPP-B2b service
area, as shown in Figure 14. The Position Dilution of Precision (PDOP) value, positioning
accuracy, and convergence time of the three stations are analyzed in detail.
The visible satellites and available satellites with PPP-B2b corrections on DoY 221 are
presented in Figure 15. During the selected test period, at least nine satellites of BDS-3 are
visible at these three stations. The number of satellites with available PPP-B2b corrections,
however, is less than that of visible satellites. As shown in Figure 15, the number of
minimum available satellites is 4 at the SGOC station during the selected test period.
The PPP-B2b service availability is further analyzed in these three stations. As shown
in Figure 16, the visible satellites and visible periods are marked as red lines, while the
available satellites with PPP-B2b correction and the available duration are marked with
purple lines. It is clearly illustrated that the visible satellites of each station are similar,
but the number of PPP-B2b available satellites of each station is different. In JFNG station,
the number of available satellites is similar to that of visible satellites, and the PPP-B2b
availability rate is 84.3%, while the availability rates of MIZU and SGOC stations are 74.6%
and 57.2%, respectively. The availability rates of the three stations decrease as the stations
are closer to the boundary of the service area.

<!-- PAGE: 16 -->

Remote Sens. 2022, 14, 643
16 of 28
Figure 13. DCB or TGD corrections and corresponding bias of B1I signal (a), B1Cp signal (b), and
B2ap signal (c).

<!-- PAGE: 17 -->

Remote Sens. 2022, 14, 643
17 of 28
Figure 14. The map of selected stations.
Table 4. Real-time PPP processing strategy.
Item
Strategy/Model
Constellation
BDS-3
Sampling rate
30 s
Mode
Static/Kinematic
IF combination
B1I + B3I
Orbit/Clock offset
CNAV1 + PPP-B2b
DCB
PPP-B2b
Cutoff elevation
7◦
Relativistic effect
Model corrected
Phase windup
Model corrected
Ionosphere
Eliminated by IF combination
Troposphere
Saastamoinen model corrects the zenith dry delay +
Estimate zenith wet delay
Ambiguity
Estimated as a ﬂoat constant
The PDOP is an important factor affecting the PPP positioning accuracy and conver-
gence time [17,40,41]. The Dilution of Precision (DOP) matrix can be expressed as:
G =

HTH
−1
(17)
where H is the design matrix of PPP solutions as expressed in Equation (16). The PDOP is
expressed as:
PDOP =
p
G11 + G22 + G33
(18)
where G11, G22, and G33 are the ﬁrst three diagonal elements of the DOP matrix G. In our
case, the PDOP is calculated according to the PPP-B2b available satellites.
The PDOP values of the JFNG, MIZU, and SGOC stations on DoY 221 are illustrated
in Figure 17. The PDOP values of the JFNG station ﬂuctuate around 2 with a maximum
value of 6. The PDOP values of MIZU and SGOC stations ﬂuctuate more widely compared
with those of the JFNG station. The maximum PDOP value of the MIZU station is 42 at
epoch 7 h:12 m:00 s, while that of the SGOC station is 67 at epoch 10 h:18 m:00 s. To
further analyze the ﬂuctuation in PDOP values of these three stations, the sky images
at 10 h:18 m:00 s are drawn in Figure 18. At that epoch, the SGOC station has 11 visible
satellites, including 5 satellites with PPP-B2b correction information, 4 of which are located
on the north side of the SGOC station. Thus, the poor observation geometry results in the
large value of PDOP.

> [1 Figure(s)]

<!-- PAGE: 18 -->

Remote Sens. 2022, 14, 643
18 of 28
 
Figure 15. Number of visible satellites and number of PPP-B2b available satellites of (a) JFNG,
(b) MIZU, and (c) SGOC.
The average number of visible satellites, the average number of PPP-B2b available
satellites, and the corresponding availability rate, as well as the average PDOP values over
7 days for eight stations are listed in Table 5. The average PPP-B2b correction availability
decreases as distance from the center of the PPP-B2b service area. The maximum PPP-B2b
correction availability rate is 88.76% at the JFNG station, and the minimum availability
rate of that is 60.91% at the SGOC station. The variation in average PDOP values showed
similar trends, ranging from 2.55 to 4.47.
To illustrate the positioning performance of the PPP-B2b service, the PPP with WHU
real-time products (WHU PPP) is also carried out to compare with the PPP-B2b results
(B2b PPP). The positioning errors of B2b PPP and WHU PPP on the east (E), north (N), and
up (U) components for the static positioning mode compared to the reference positions are
presented in Figures 19 and 20, while the positioning errors in the kinematic positioning
mode are presented in Figures 21 and 22, respectively.

<!-- PAGE: 19 -->

Remote Sens. 2022, 14, 643
19 of 28
Figure 16. The visible satellites, the PPP-B2b available satellites, and the corresponding availability
on DoY 221 of JFNG (a), MIZU (b), and SGOC (c).
In Figures 19 and 20, both B2b PPP and WHU PPP of the three stations achieve
centimeter-level positioning accuracies after convergence. For B2b PPP, the positioning
performance of the JFNG station, in terms of converge time and positioning accuracy, is
better than that of the MIZU and the SGOC stations. For WHU PPP, the three stations
present similar error levels, but the SGOC station needs longer convergence time on
U components. The RMSE of E, N, and U components, as well as horizontal (H), and the
three-dimensions (3D) for the eight stations on the static positioning mode based on the
B2b PPP and WHU PPP are calculated and listed in Table 6. For B2b PPP, the RMSE on the
E, N, and U components of all stations are similar, achieving centimeter-level accuracy. The
RMSE of the N component is smaller than that of the E and U components in all stations.
The RMSE of JFNG station on the E, N, and U components is slightly better than those of
other stations due to the station being within the service area. The 3D errors vary between
3.9 and 8.3 cm. The performance of WHU PPP presents a similar trend as B2b PPP in the
analyzed area. The RMSE of 3D error of each station based on the WHU PPP, however, is
larger than that of B2b PPP in all stations. For example, for the JFNG station, the RMSE of
3D error is 3.9 cm for B2b PPP, while that of WHU PPP is 7.2 cm.

> [1 Figure(s)]

<!-- PAGE: 20 -->

Remote Sens. 2022, 14, 643
20 of 28
Figure 17. PDOP values on DoY 221 of three stations, JFNG, MIZU, and SGOC.
Figure 18. Sky images of JFNG (a), MIZU (b), and SGOC (c).

> [2 Figure(s)]


|Col1|Fi|
|---|---|




|Col1|Fi|
|---|---|



<!-- PAGE: 21 -->

Remote Sens. 2022, 14, 643
21 of 28
Table 5. Average number of visible satellites, average number of available satellites, average PPP-B2b
correction availability rate, and average PDOP for each station.
Stations
Average Number
of Visible
Satellites
Average Number
of Available
Satellites
Average PPP-B2b
Correction
Availability Rate
Average PDOP
JFNG
11.41
8.29
88.76%
2.55
GAMG
13.92
8.92
83.22%
2.57
MIZU
13.71
8.37
78.97%
3.07
PTGG
13.96
7.83
73.03%
2.88
ULAB
14.14
8.15
81.19%
3.90
URUM
14.76
8.00
75.47%
4.24
LCK4
12.15
7.45
72.89%
3.94
SGOC
14.91
7.06
60.91%
4.47
Figure 19. Positioning error series of static positioning mode PPP (B2b PPP) on DoY 221.
In Figure 21, the positioning errors of B2b PPP at the JFNG on E, N, and U components
are within 0.3 m after convergence for the kinematic positioning mode. The horizontal
components of the positions of the MIZU and the SGOC stations are similar to those
of the JFNG. The U component error of the MIZU and the SGOC stations, however, is
relatively large compared to that of the JFNG station. The maximum error of the U
component is at SGOC station with 1.3 m, which is caused by poor observation geometrics
and a lower number of available satellites with PPP-B2b corrections. The peak value
can be easily observed on the SGOC station at epoch 10 h:18 m:00 s, 12 h:00 m:00 s, and
15 h:30 m:00 s, when the positioning error is larger than 0.9 m. The number of PPP-B2b
available satellites at these epochs are less than 5, and the PDOP value is larger than 10,
as shown in Figures 15 and 17. In Figure 22, the positioning errors of WHU PPP of the
three stations are similar and all of them achieve decimeter-level accuracy. The positioning
performance of the SGOC station with WHU PPP, compared to that of B2b PPP, is not
affected by the number of PPP-B2b available satellites. The convergence time of WHU PPP,
however, is slightly longer than that of B2b PPP.


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|in|0.|3|m|af|er|c|n|ve|rg|en|ce|f|r|th||in|e|a|tic|p|os|itio|
|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|||
|~~e~~n|ts|of|t|e|p|os|ti|n|s|f|th|e|MI|Z||an|d|th|e|G|O|C s|
|~~N~~|G.|T|he|U|c|om|p|on|en|t|er|ror|o|f t|he|M|I|ZU|a|nd|t|he ~~S~~|
|y|lar|<br>ge|c|<br>o|<br>p|ar|ed|t|o t|<br>ha|t|of|<br> th|<br>e|JF|<br>N|G|st|<br>ti|on|<br>.|<br> The|
|<br>|||<br>|||||<br>|<br>||<br>|<br>|<br>|<br>|<br>||<br>|<br>|||<br>|<br>|
|n|i|a|S|G||s|at|io||i|h|1.||,||ic|h i|s c|a|se|d|by|
|~~w~~|~~er ~~|~~n~~||~~b~~|~~r ~~|~~of~~|~~a~~|~~va~~|~~il~~|~~bl~~|~~e ~~|~~a~~|~~el~~|~~it~~|~~s ~~|~~w~~|~~t~~||~~P~~|~~-~~|~~2~~|~~c~~|




|as|ily|o|bs|er|ve|d o|n|th|e|SG|O|C|sta|ti|on|at|e|po|ch|1|0 h|:18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|:|0|s,|w|e||h|p|os|iti|o|in|g|r|o|i|l|r|er|t|a||.9|
|s|at|ell|ite|s|at|th|es|e|po|ch|s|ar|e l|es|t|ha|n|5,|an|d|h|P|
|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|~~n~~|n|Fi|g|re|s|5|an|d|7|I||i|u|e|22|, t|e|p|s|ti|n|ing|
|i|n|a|e|i|i|ar|a|d|al||f t|he||a|hi|v||e|i|e|er|lev|
|<br>|<br>c|<br> o|<br> t|<br>e|<br> S|<br>|<br>|<br> s|<br>a|<br>io|<br>|<br>i|<br>h|<br>|<br>|<br>U|<br> P|<br>|<br> c|<br>|<br>|<br>are|
|||<br>|<br>|<br>|<br>|||<br>|||<br>||<br>|<br>||<br>|<br>||<br>||||




|, i|s s|lig|ht|ly|lo|ng|er|th|an|t|ha|t o|f B|2b|P|P|P.|Col19|Col20|Col21|Col22|Col23|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||



<!-- PAGE: 22 -->

Remote Sens. 2022, 14, 643
22 of 28
 
Figure 20. Positioning error series of static positioning mode PPP (WHU PPP) on DoY 221.
Figure 21. Kinematic mode PPP (B2b PPP) positioning error series of DoY 221.


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||




|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||




|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||




|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||



<!-- PAGE: 23 -->

Remote Sens. 2022, 14, 643
23 of 28
Figure 22. Kinematic mode PPP (WHU PPP) positioning error series of WHU on DoY 221.
Table 6. RMSE (cm) for each station on static positioning mode (B2b PPP vs. WHU PPP).
Stations
Static B2b PPP
Static WHU PPP
E
N
U
H
3D
E
N
U
H
3D
JFNG
3.3
0.5
2.1
3.4
3.9
5.2
3.5
3.6
6.3
7.2
GAMG
4.6
0.8
4.7
4.6
6.6
5.4
4.5
7.5
7.0
10.3
MIZU
3.6
1.2
4.9
3.8
6.2
5.9
4.6
11.8
7.5
14.0
PTGG
4.6
1.2
5.8
4.7
7.5
5.0
2.4
15.3
5.5
16.3
ULAB
5.9
0.7
3.6
5.9
6.9
4.9
4.0
7.9
6.3
10.1
URUM
3.6
2.3
7.1
4.3
8.3
3.0
2.3
7.5
3.8
8.4
LCK4
5.3
2.2
5.1
5.7
7.7
3.3
3.4
14.1
4.7
14.8
SGOC
3.5
2.2
3.3
4.1
5.3
4.9
2.8
10.8
5.6
12.2
mean
4.3
1.4
4.6
4.6
6.5
4.7
3.4
9.8
5.8
11.7
The RMSE of E, N, and U components, horizontal (H), and 3-dimensions (3D) for eight
stations on kinematic positioning mode regarding B2b PPP and WHU PPP are calculated
and listed in Table 7. The RMSE of the E, N, and U components of all stations achieve
decimeter-level accuracy. The RMSE of the N component is smaller than that of the E and
U components in all stations. For B2b PPP, the RMSE of the JFNG station on E, N, and
U components are 7.3, 3.5, and 9.1 cm, respectively, while the errors of the three components
at the SGOC station are 19.2, 9.2, and 21.3 cm, respectively, which are two times larger
than that of JFNG station. Especially, for the RMSE of WHU PPP all eight stations present
similar performance, achieving decimeter-level accuracy. For stations located on the service
boundary, such as SGOC and LCK4, the RMSEs are smaller than those of B2b PPP. The
RMSE values of different positioning strategies are summarized in Figure 23.


|ng m|ode regarding B2b PPP and W|HU P|
|---|---|---|



<!-- PAGE: 24 -->

Remote Sens. 2022, 14, 643
24 of 28
Table 7. RMSE (cm) for each station (B2b PPP vs. WHU PPP).
Stations
Kinematic B2b PPP
Kinematic WHU PPP
E
N
U
H
3D
E
N
U
H
3D
JFNG
7.3
3.5
9.1
8.1
12.2
12.9
7.9
16.5
15.1
22.4
GAMG
6.7
5.0
16.4
8.3
18.4
15.0
9.1
22.5
17.5
28.5
MIZU
6.8
5.9
14.7
9.0
17.2
12.9
10.1
28.3
16.4
32.7
PTGG
9.1
6.3
21.3
11.1
24.0
12.1
7.0
25.4
14.0
29.0
ULAB
7.8
6.0
15.1
9.8
18.0
16.1
9.8
24.8
18.8
31.1
URUM
15.4
5.1
11.6
16.2
19.9
15.5
8.1
28.1
17.5
33.1
LCK4
19.3
7.6
18.9
20.7
28.1
12.4
6.7
21.8
14.1
26.0
SGOC
19.2
9.2
21.3
21.3
30.1
13.6
9.2
15.9
16.4
22.9
Mean
11.5
6.1
16.1
13.1
21.0
13.8
8.5
22.9
16.2
28.2
Figure 23. The RMSE summary of different positioning strategies.
To further evaluate the real-time performance of PPP-B2b services, the PPP with
broadcast ephemeris is also carried out which is listed in Table 8. For the static positioning
mode, the RMSE of horizontal components are similar, with decimeter-level accuracy. For
the kinematic positioning mode, the RMSE of horizontal component is around 1.5 m.
The convergence time of these stations is also used to analyze the positioning perfor-
mance. The convergence time for the static positioning mode is deﬁned as the positioning
error less than 10 cm on the E and N components and less than 30 cm on the U component,
and lasts for at least 10 min. For the kinematic positioning mode, the convergence time
is deﬁned as the error within 30 cm on the E and N components, within 60 cm on the
U component, and lasts for at least 10 min. The daily convergence time over 7 days of
the eight stations is summarized in Table 9 with both B2b PPP and WHU PPP. In static
positioning mode, for B2b PPP, the convergence time varies between 16.33 and 40.58 min
except for the MIZU station. The convergence time of the MIZU station is 99.17 min due to
the signiﬁcant error on the U component at the beginning epochs, which is further caused

<!-- PAGE: 25 -->

Remote Sens. 2022, 14, 643
25 of 28
by the considerable value of PDOP, as shown in Figure 17. In kinematic positioning mode,
B2b PPP, the convergence time varies between 11.08 and 45.66 min. The convergence time
with B2b PPP is shorter than that of WHU PPP, which is mainly caused by the smaller STD
on PPP-B2b clock offset.
Table 8. RMSE (m) of broadcast PPP.
Stations
Static
Kinematic
E
N
U
H
3D
E
N
U
H
3D
JFNG
0.22
0.61
1.22
0.65
1.38
0.94
1.39
3.08
1.68
3.51
GAMG
0.23
0.57
0.85
0.61
1.05
0.75
1.50
1.99
1.68
2.59
MIZU
0.41
0.67
0.92
0.79
1.21
0.73
1.32
1.93
1.51
2.45
PTGG
0.42
0.51
1.02
0.67
1.22
1.37
1.07
3.39
1.74
3.81
ULAB
0.23
0.62
1.35
0.67
1.50
0.94
1.52
2.96
1.79
3.46
URUM
0.29
0.17
1.25
0.34
1.29
1.23
1.11
2.29
1.66
2.83
LCK4
0.75
0.20
0.76
0.78
1.09
1.39
1.13
2.23
1.79
2.86
SGOC
0.49
0.21
0.50
0.53
0.73
1.28
1.00
2.06
1.62
2.62
Mean
0.38
0.45
0.98
0.63
1.18
1.08
1.26
2.49
1.68
3.01
Table 9. Convergence time (min) for each station.
Stations
B2b PPP
WHU PPP
Static
Kinematic
Static
Kinematic
JFNG
16.33
11.08
22.17
29.87
GAMG
23.83
14.75
27.84
30.36
MIZU
99.17
13.75
39.33
23.68
PTGG
17.91
27.75
46.00
14.83
ULAB
18.91
24.66
28.67
67.00
URUM
21.75
39.41
41.33
109.50
LCK4
29.58
32.75
45.85
99.14
SGOC
40.58
45.66
54.50
54.29
From the results of the experiments, we found that the positioning accuracy of the
selected stations with real-time PPP-B2b service can achieve centimeter-level accuracy in
static positioning mode and decimeter-level accuracy in kinematic positioning mode. The
overall positioning performance of PPP-B2b service within the test area is slightly better
than that of WHU real-time products. The reason may be that the service areas of the
PPP-B2b are consistent with those of its monitoring network, while the WHU real-time
products are calculated based on the global GNSS network which is not consistent with the
test area. The positioning performance of stations located at the boundary of the service
area, however, is worse than that of the WHU real-time product. The PPP with broadcast
ephemeris can achieve decimeter level accuracy in static positioning mode in the selected
stations, which also corresponds to the smaller value of SISRE of broadcast ephemeris,
which is 0.536 m.
4. Conclusions
The PPP-B2b signals transmitted by the GEO satellites of BDS-3 provide a real-time
PPP service in China and the surrounding areas. In this study, we evaluated the perfor-
mance of the PPP-B2b service within China and surrounding countries. The BDS-3 PPP-B2b
performance in terms of satellite orbit and clock, SISRE, and DCB were evaluated related
to those from GFZ ﬁnal precise products and compared to those from the WHU real-time
product. The PPP performance of PPP-B2b service was evaluated with comparison to
PPP with WHU real-time products in both static and kinematic positioning modes. The
following conclusions could be drawn:

<!-- PAGE: 26 -->

Remote Sens. 2022, 14, 643
26 of 28
1.
The accuracy of the BDS-3 broadcast orbit is similar to that of the PPP-B2b real-time
orbit. The RMSE of broadcast orbit is 8.8, 20.7, and 15.4 cm in radial, along-track,
and cross-track components, respectively, while those of PPP-B2b orbits are 8.5, 19.3,
and 14.0 cm, respectively. It should be emphasized that the difference between the
broadcast orbit and PPP-B2b orbit is only centimeter-level due to the support of the
inter-satellite links among the BDS-3 satellites. The PCO corrections from CSNO
and IGS are different, which results in abnormal orbit bias in different satellites with
different PCO corrections.
2.
The satellite clock offset precision of the BDS-3 broadcast ephemeris is signiﬁcantly
improved by PPP-b2b clock corrections and improved the continuity of the broadcast
clock offsets accordingly. The satellite-speciﬁed systematic errors exist in the PPP-B2b
clock offsets, which further affects the SISRE of PPP-B2b. The STD of the real-time
precise PPP-B2b clock offsets is within 0.2 ns, while the average STD of the broadcast
satellite clock offsets is 0.672 ns.
3.
The RMS SISRE of broadcast ephemeris is 0.536 m, and that of PPP-B2b is 1.24 m.
Comparing the orbit only SISRE, we found that the large SISRE values of broadcast
ephemeris and PPP-B2b are mainly caused by the satellite-speciﬁed systematic error
of the clock offset. The STD of PPP-B2b SISRE is only 0.097 m, which is similar to that
of WHU real-time products.
4.
The DCB corrections in the message of PPP-B2b and broadcast TGD are compared
with the CAS ﬁnal DCB products. The STD values of DCB corrections relative to
CAS DCB corrections are 0.46, 0.54, and 0.47 ns for B1I, B1Cp, and B2ap signals,
respectively. The DCB corrections and broadcast TGD on B1Cp and B2ap signals with
respect to those of CAS DCB, however, exhibit constant bias of about 2 and 10 ns.
5.
The average availability rate of PPP-B2b service during the test period at the eight
IGS stations is above 60%. The positioning accuracy of static positioning mode
achieves centimeter-level accuracy with the PPP-B2b service, which is similar with
the PPP solution by using WHU real-time products. For kinematic positioning mode,
decimeter-level accuracy is achieved with the PPP-B2b service. The station JFNG
located in China has the best positioning accuracy among the eight stations, with
7.3, 3.5, and 9.1 cm in the E, N, and U components, respectively, which is better
than those of the PPP solutions with WHU real-time products. The RMSE of the
positioning solution with the PPP-B2b service at the SGOC station, which is located at
the boundary of the service area with considerable PDOP value, is two times larger
than that of the JFNG station. The PPP solution on the SGOC station with WHU
real-time product, however, has better positioning accuracy than that of the PPP-B2b
service, which is not affected by the number of PPP-B2b available satellites. From
our study, the PPP-B2b service has better positioning performance than that of WHU
real-time products within the service coverage area in both static positioning mode
and kinematic positioning mode.
Author Contributions: Conceptualization, C.Y.; Data curation, M.Z.; Funding acquisition, C.Y.;
Investigation, Y.L. and C.Y.; Software, Y.L.; Supervision, C.Y.; Visualization, Y.L. and M.Z.; Writing—
original draft, Y.L.; Writing—review & editing, C.Y. and Y.L. All authors have read and agreed to the
published version of the manuscript.
Funding: This study is supported by the National Science Foundation of China (No. 41804036) and
the National Key Research and Development Program of China (No. 2020YFB0505802).
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The datasets analyzed in this study are managed by the School of Land
Science and Geomatics, China University of Geosciences, Beijing and can be available on request
from the corresponding author.

<!-- PAGE: 27 -->

Remote Sens. 2022, 14, 643
27 of 28
Acknowledgments: The authors greatly appreciate IGMAS, GFZ, CAS, WHU, and CSNO for provid-
ing the necessary products.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Yang, Y.X. Concepts of Comprehensive PNT and Related Key Technologies. Acta Geod. Cartogr. Sin. 2016, 45, 505–510.
2.
Yang, Y.; Mao, Y.; Sun, B. Basic performance and future developments of BeiDou global navigation satellite system. Satell. Navig.
2020, 1, 1. [CrossRef]
3.
Yang, Y.; Liu, L.; Li, J.; Yang, Y.; Zhang, T.; Mao, Y.; Sun, B.; Ren, X. Featured services and performance of BDS-3. Sci. Bull. 2021,
66, 2135–2143. [CrossRef]
4.
Zumberge, J.F.; Heﬂin, M.B.; Jefferson, D.C.; Watkins, M.M.; Webb, F.H. Precise point positioning for the efﬁcient and robust
analysis of GPS data from large networks. J. Geophys. Res.-Solid Earth 1997, 102, 5005–5017. [CrossRef]
5.
Jin, S.; Su, K. PPP models and performances from single- to quad-frequency BDS observations. Satell. Navig. 2020, 1, 16. [CrossRef]
6.
Guo, J.; Geng, J.H.; Wang, C. Impact of the third frequency GNSS pseudorange and carrier phase observations on rapid PPP
convergences. GPS Solut. 2021, 25, 30. [CrossRef]
7.
Geng, J.; Guo, J.; Meng, X.; Gao, K. Speeding up PPP ambiguity resolution using triple-frequency GPS/BeiDou/Galileo/QZSS
data. J. Geod. 2020, 94, 6. [CrossRef]
8.
Li, P.; Jiang, X.; Zhang, X.; Ge, M.; Schuh, H. GPS + Galileo + BeiDou precise point positioning with triple-frequency ambiguity
resolution. GPS Solut. 2020, 24, 78. [CrossRef]
9.
Hong, J.; Tu, R.; Zhang, R.; Fan, L.; Zhang, P.; Han, J. Contribution analysis of QZSS to single-frequency PPP of
GPS/BDS/GLONASS/Galileo. Adv. Space Res. 2020, 65, 1803–1817. [CrossRef]
10.
Xu, Y.; Yang, Y.; Li, J. Performance evaluation of BDS-3 PPP-B2b precise point positioning service. GPS Solut. 2021, 25, 142.
[CrossRef]
11.
Dai, L.; Chen, Y.; Lie, A.; Zeitzew, M.; Zhang, Y. StarFire™SF3: Worldwide Centimeter-Accurate Real Time GNSS Positioning.
In Proceedings of the 29th International Technical Meeting of The Satellite Division of the Institute of Navigation (ION GNSS+
2016), Portland, OR, USA, 12–16 September 2016; pp. 3295–3320.
12.
Leandro, R.; Landau, H.; Nitschke, M.; Glocker, M.; Seeger, S.; Chen, X.; Deking, A.; BenTahar, M.; Zhang, F.; Ferguson,
K.; et al. RTX Positioning: The Next Generation of cm-accurate Real-time GNSS Positioning. In Proceedings of the 24th
International Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS 2011), Portland, OR, USA,
20–23 September 2011; pp. 1460–1475.
13.
Ge, Y.; Chen, S.; Wu, T.; Fan, C.; Qin, W.; Zhou, F.; Yang, X. An analysis of BDS-3 real-time PPP: Time transfer, positioning, and
tropospheric delay retrieval. Measurement 2021, 172, 108871. [CrossRef]
14.
Carlin, L.; Hauschild, A.; Montenbruck, O. Precise point positioning with GPS and Galileo broadcast ephemerides. GPS Solut.
2021, 25, 77. [CrossRef]
15.
Lu, X.; Chen, L.; Shen, N.; Wang, L.; Jiao, Z.; Chen, R. Decoding PPP Corrections From BDS B2b Signals Using a Software-Deﬁned
Receiver: An Initial Performance Evaluation. IEEE Sens. J. 2021, 21, 7871–7883. [CrossRef]
16.
Nie, Z.; Xu, X.; Wang, Z.; Du, J. Initial Assessment of BDS PPP-B2b Service: Precision of Orbit and Clock Corrections, and PPP
Performance. Remote Sens. 2021, 13, 2050. [CrossRef]
17.
Tao, J.; Liu, J.; Hu, Z.; Zhao, Q.; Chen, G.; Ju, B. Initial Assessment of the BDS-3 PPP-B2b RTS compared with the CNES RTS.
GPS Solut. 2021, 25, 131. [CrossRef]
18.
Ren, Z.; Gong, H.; Peng, J.; Tang, C.; Huang, X.; Sun, G. Performance assessment of real-time precise point positioning using BDS
PPP-B2b service signal. Adv. Space Res. 2021, 68, 3242–3254. [CrossRef]
19.
China Satellite Navigation Ofﬁce. BeiDou Navigation Satellite System Signal in Space Interface Control Document: Precise Point
Positioning Service Signal PPP-B2b (Version 1.0). Available online: http://en.beidou.gov.cn/SYSTEMS/ICD/202008/P020200803
538771492778.pdf (accessed on 20 October 2021).
20.
Montenbruck, O.; Teunissen, P. Springer Handbook of Global Navigation Satellite Systems. In Springer Handbooks; Online
Resource XXXI, 1327 Pages 818 Illustrations in Color; Springer International Publishing: Cham, Switzerland, 2017; p. 1.
21.
So´snica, K.; Zajdel, R.; Bury, G.; Bosy, J.; Moore, M.; Masoumi, S. Quality assessment of experimental IGS multi-GNSS combined
orbits. GPS Solut. 2020, 24, 54. [CrossRef]
22.
Montenbruck, O.; Steigenberger, P.; Hauschild, A. Broadcast versus precise ephemerides: A multi-GNSS perspective. GPS Solut.
2014, 19, 321–333. [CrossRef]
23.
Shi, Y.; Hao, J.; Liu, W.; Jiao, B.; Zhang, H.; Song, B. Performance Assessment of BDS Real-Time Precise Point Positioning Based
on SSR Corrections. J. Surv. Eng. 2019, 145, 05019003. [CrossRef]
24.
China Satellite Navigation Ofﬁce. BeiDou Navigation Satellite System Signal in Space Interface Control Document: Open
Service Signal B1C (Version 1.0). Available online: http://www.beidou.gov.cn/xt/gfxz/201712/P020171226741342013031.pdf
(accessed on 30 December 2021).
25.
Montenbruck, O.; Steigenberger, P.; Hauschild, A. Multi-GNSS signal-in-space range error assessment—Methodology and results.
Adv. Space Res. 2018, 61, 3020–3038. [CrossRef]

<!-- PAGE: 28 -->

Remote Sens. 2022, 14, 643
28 of 28
26.
Yao, Y.; He, Y.; Yi, W.; Song, W.; Cao, C.; Chen, M. Method for evaluating real-time GNSS satellite clock offset products. GPS Solut.
2017, 21, 1417–1425. [CrossRef]
27.
Xue, B.; Wang, H.; Yuan, Y. Performance of BeiDou-3 signal-in-space ranging errors: Accuracy and distribution. GPS Solut. 2021,
25, 23. [CrossRef]
28.
Lv, Y.; Geng, T.; Zhao, Q.; Xie, X.; Zhou, R. Initial assessment of BDS-3 preliminary system signal-in-space range error. GPS Solut.
2019, 24, 16. [CrossRef]
29.
Zhang, W.; Lou, Y.; Song, W.; Sun, W.; Zou, X.; Gong, X. Initial assessment of BDS-3 precise point positioning service on GEO B2b
signal. Adv. Space Res. 2022, 69, 690–700. [CrossRef]
30.
Wu, W.; Guo, F.; Zheng, J. Analysis of Galileo signal-in-space range error and positioning performance during 2015–2018. Satell.
Navig. 2020, 1, 6. [CrossRef]
31.
Kazmierski, K.; Zajdel, R.; So´snica, K. Evolution of orbit and clock quality for real-time multi-GNSS solutions. GPS Solut. 2020, 24,
111. [CrossRef]
32.
Wang, N.; Yuan, Y.; Li, Z.; Montenbruck, O.; Tan, B. Determination of differential code biases with multi-GNSS observations.
J. Geod. 2015, 90, 209–228. [CrossRef]
33.
Dai, P.; Xing, J.; Ge, Y.; Yang, X.; Qin, W.; Dong, Y.; Zhang, Z. The Effect of BDS-3 Time Group Delay and Differential Code Bias
Corrections on Positioning. Appl. Sci. 2020, 11, 104. [CrossRef]
34.
Zhang, B.; Zhao, C.; Odolinski, R.; Liu, T. Functional model modiﬁcation of precise point positioning considering the time-varying
code biases of a receiver. Satell. Navig. 2021, 2, 11. [CrossRef]
35.
An, X.; Meng, X.; Jiang, W. Multi-constellation GNSS precise point positioning with multi-frequency raw observations and
dual-frequency observations of ionospheric-free linear combination. Satell. Navig. 2020, 1, 7. [CrossRef]
36.
Wang, W.; Wang, Y.; Yu, C.; Xu, F.; Dou, X. Spaceborne atomic clock performance review of BDS-3 MEO satellites. Measurement
2021, 175, 109075. [CrossRef]
37.
Sakic, P.; Mansur, G.; Mannel, B. A prototype for a Multi-GNSS orbit combination. In Proceedings of the 2020 European
Navigation Conference (ENC), Dresden, Germany, 23–24 November 2020.
38.
Yang, Y.; Xu, Y.; Li, J.; Yang, C. Progress and performance evaluation of BeiDou global navigation satellite system: Data analysis
based on BDS-3 demonstration system. Sci. China-Earth Sci. 2018, 61, 614–624. [CrossRef]
39.
China Satellite Navigation Ofﬁce. BeiDou Navigation Satellite System Open Service Performance Standard (Version 3.0). 2021.
Available online: http://m.beidou.gov.cn/xt/gfxz/202105/P020210526216231136238.pdf (accessed on 11 November 2021).
40.
Biswas, S.K.; Qiao, L.; Dempster, A. Effect of PDOP on performance of Kalman Filters for GNSS-based space vehicle position
estimation. GPS Solut. 2017, 21, 1379–1387. [CrossRef]
41.
Teng, Y.; Wang, J. Some Remarks on PDOP and TDOP for Multi-GNSS Constellations. J. Navig. 2015, 69, 145–155. [CrossRef]
