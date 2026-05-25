<!-- PAGE: 1 -->

Journal of Geodesy (2022) 96:60
https://doi.org/10.1007/s00190-022-01642-9
ORIGINAL ARTICLE
Orbit determination, clock estimation and performance evaluation
of BDS-3 PPP-B2b service
Chengpan Tang1 · Xiaogong Hu1,3 · Jinping Chen2 · Li Liu2 · Shanshi Zhou1 · Rui Guo2 · Xiaojie Li1,2 · Feng He5 ·
Jinhuo Liu1,4 · Jianhua Yang1,4
Received: 29 November 2020 / Accepted: 14 July 2022 / Published online: 29 August 2022
© Springer-Verlag GmbH Germany, part of Springer Nature 2022
Abstract
This paper focuses on PPP-B2b, one of the featured services for BDS-3, which provides users around China with centimetre-
level static positioning accuracy and decimetre-level kinematic positioning accuracy by broadcasting precise corrections for
GPS/BDS-3 satellites. The GEO PPP-B2b signal broadcasted information types, including the PRN mask, orbit corrections,
differential code bias corrections and clock corrections, are introduced, as well as a brief description of their usage. A new orbit
determination strategy using regional L-band code/phase measurements and inter-satellite link measurements in combination
and a real-time clock estimation strategy based on the Kalman ﬁlter for PPP-B2b precise correction generation are introduced
in this contribution. Then, the accuracy of the orbit and clock corrections is assessed. The orbit user ranging error (URE)
is 0.05 m for the BDS-3 MEO and GPS satellites. The orbit URE for BDS-3 IGSO satellites is worse, i.e., 0.15 m. The
clock correction accuracy is 0.2 ns for BDS-3 and GPS satellites. Finally, the PPP-B2b performance is validated by both
the static PPP process and simulated kinematic PPP process. BDS-3/GPS dual-system PPP offers faster convergence and
better accuracy. The positioning accuracy achievable using PPP-B2b real-time products is at the same level as that using
post-processed products. The RMS for BDS-3/GPS dual-system static positioning errors is less than 1.0 cm in east and north
and about 3.0 cm in the up. The simulated kinematic positioning accuracy is better than 2.5 cm in the north, 3.5 cm in the
east and 8.5 cm in the up directions after convergence.
Highlights
– A new determination strategy using regional L-band code/phase measurements and inter-satellite link measurements in
combination and a real-time clock estimation strategy based on the Kalman ﬁlter for PPP-B2b precise correction generation
are introduced.
– User ranging error (URE) is 0.05 m for the BDS-3 MEO and GPS satellites.
– The clock correction accuracy is 0.2 ns for BDS-3 and GPS satellites.
– The positioning accuracy achievable using PPP-B2b real-time products is at the same level as that using post-processed
products.
Keywords BeiDou navigation satellite system · Satellite orbits · Real-time clock estimation · Precise point positioning ·
Global positioning system
B Xiaogong Hu
hxg@shao.ac.cn
1
Shanghai Astronomical Observatory, Chinese Academy of
Sciences, Shanghai 200030, China
2
Beijing Satellite Navigation Center, Beijing 100094, China
3
Shanghai Key Laboratory for Space Positioning and
Navigation, Shanghai 200030, China
4
University of Chinese Academy of Sciences, Beijing 100049,
China
5
National Defense University, No. 3 Hongsankoujia Road,
Beijing 100091, China
123

> [1 Figure(s)]

<!-- PAGE: 2 -->

60
Page 2 of 17
C. Tanget al.
1 Introduction
The BeiDou Navigation Satellite System (BDS), indepen-
dently developed and operated by China, is regarded as
a temporal-spatial infrastructure of national signiﬁcance,
providing all-time, all-weather and high-accuracy position-
ing, navigation and timing services to global users (CSNO
2019a). The BDS is listed as one of the four satellite navi-
gation providers, along with the GPS of the US, GLONASS
of Russia, and Galileo of Europe. The development of the
BDS has followed a three-step strategy. The establishment
of BDS-1, also named the experimental BeiDou navigation
system, was ﬁnished in 2003, marking the end of the ﬁrst
step of BDS construction. Different from mainstream sys-
tems such as GPS and GLONASS, BDS-1 consists of only
GEO satellites and provides a bidirectional interactive radio
determination satellite service (RDSS). The second step of
BDS construction, BDS-2, was ﬁnished by the end of 2012.
BDS-2 consists of GEO, IGSO and MEO satellites and pro-
vides positioning, navigation and timing (PNT) services to
users around the Asia–Paciﬁc area (Zhou et al. 2012 and
Zhou et al. 2013).
The third step is to construct BDS-3, expanding the cover-
age from the Asia–Paciﬁc region to the globe (CSNO 2019a).
The development of BDS-3 started in 2009. On November
5, 2017, the ﬁrst two BDS-3 satellites were deployed, mark-
ing the ﬁrst step of BDS-3 construction. By December 27,
2018, 18 MEO satellites and 1 GEO satellite had been put
into the sky. The completion of the BDS-3 basic system and
the opening up of global PNT services were announced by
the China Satellite Navigation Ofﬁce on that day.
On June 23, 2020, the last BDS-3 GEO satellite was suc-
cessfully launched, indicating that the deployment of the
BDS-3 constellation was ﬁnished. The BDS-3 constellation
includes 24 MEO satellites, 3 IGSO satellites and 3 GEO
satellites. On July 31, 2020, the Chinese government ofﬁ-
cially announced the commissioning of BDS-3. Compared
to BDS-2, the broadcast orbit and clock accuracy of BDS-3
satelliteswereconsiderablyimproved(Tangetal.2016;Chen
et al. 2020). As reported by Chen et al. (2020), the signal-in-
space accuracy of BDS-3 is better than 0.5 m, the positioning
accuracy is better than 10 m, and the timing accuracy is
better than 20 ns. BDS-3 provides three kinds of services
to users world-wide and four kinds of services to users
around China. The world-wide services include global PNT
services, global short message communication (GSMC) ser-
vice and international search and rescue (SAR) service. The
regional services include satellite-based augmentation sys-
tem (SBAS), ground-based augmentation system (GBAS),
precise point positioning (PPP) and regional short message
communication (RSMC) services (CSNO 2019a).
PPP enables a single receiver to achieve centimetre-level
to decimetre-level positioning accuracy in either static mode
or kinematic mode and is regarded as a popular and widely
used technology in high-precision positioning applications
of GNSS. Due to its high accuracy, PPP is widely used in
crustal deformation monitoring, near real-time GPS meteo-
rology, orbit determination of low Earth orbiting satellites
for gravity recovery missions and the precise positioning of
mobile objects (Calais et al. 2006; Rocken et al. 2005; Zhu
et al. 2004 and Zhang and Andersen 2006). Precise orbit and
clock products with centimetre-level accuracy are the pre-
requisites of PPP services (Zumberge et al. 1997 and Kouba
and Héroux 2001).
PPP is one of the featured services of BDS-3 for support-
ing high-precision positioning applications (Liu et al. 2020).
The PPP-B2b signal, transmitted by BDS-3 GEO satellites,
broadcasts precise orbit corrections, clock corrections and
Differential Code Biases (DCB) of BDS-3 IGSO/MEO satel-
lites and GPS satellites to dual-frequency users around China
and its surrounding areas (CSNO 2019b). Currently, the
supported GNSS constellations include BDS-3 IGSO/MEO
satellites and GPS satellites. The precise corrections enable
GPS/BDS dual-frequency PPP. In this contribution, the gen-
eration strategy of precise corrections for PPP-B2b service
is brieﬂy introduced as well as accuracy evaluation.
The paper is organized as follows. The PPP-B2b broad-
cast messages and information types are brieﬂy introduced in
Sect. 2. The orbit determination and clock estimation strategy
with accuracy assessment are given in Sect. 3. The position-
ing accuracy for a PPP-B2b broadcast message is evaluated
in Sect. 4. Finally, the conclusions and discussion are given
in Sect. 5.
2 PPP-B2b broadcast message
and information type
The Interface Control Document (ICD) of PPP-B2b was
released by the China Satellite Navigation Ofﬁce at the end
of 2019. According to the ICD, the PPP-B2b signal broad-
casts the I-component and the Q-component. Currently, the
ﬁrst three GEO satellites of BDS-3 broadcast only the I-
component. The broadcast PPP-B2b messages are contained
in the I-component. The Q-component will be discussed in
the future (CSNO 2019b). The PPP-B2b ICD deﬁnes seven
information types transmitted in the PPP-B2b I-component.
Currently, the PPP-B2b signal broadcasts four of the seven
information types. Same as the four information types, the
other three information types are also used to broadcast the
orbit corrections, clock corrections and integrity informa-
tion with less communication bandwidth. By using the four
information types, the GPS or BDS-3 users are able to get a
PPP solution. The current regularly broadcasted information
types are given in Table 1.
123

<!-- PAGE: 3 -->

Orbit determination, clock estimation and performance …
Page 3 of 17
60
Table 1 Regularly broadcasted PPP-B2b information types
Type No.
Type name
Update interval (s)
Nominal
validity (s)
Type 1
PRN mask
48
–
Type 2
Orbit correction
and user
range
accuracy
index
48
96
Type 3
Differential
code bias
48
86,400
Type 4
Clock
correction
6
12
The PPP-B2b broadcasted information types include
several slow variables and a fast variable. The slow vari-
ables include the satellite mask, orbit correction and user
range accuracy index, and differential code bias, which are
broadcasted every 48 s. The fast variable is clock correction,
which is broadcasted every 6 s. Note that " Nominal validity"
in Table 1 gives the time interval of validity of the message.
For message outside this interval the data quality cannot be
ensured.
With the information types mentioned in Table 1 and
the navigation messages broadcasted by BDS-3 IGSO/MEO
satellites and GPS satellites, precise orbits and clock offsets
can be recovered.
1) PRN mask
The PRN mask is to deﬁne which satellites are used for
PPP services so that each message type can share a com-
mon set of satellites deﬁned in advance, thereby saving
the message bits. The PRN mask deﬁnes whether the pre-
cise corrections of a speciﬁc satellite are broadcasted.
If the precise corrections of a speciﬁc satellite will be
broadcasted, the corresponding bit in the mask will be
assigned “1”. Satellite orbit correction, clock correction
and differential code bias are used matching the PRN
mask.PRNmaskistheindextablewhichisusedtoassign
corrections to the satellites. Satellite masks are usually
kept ﬁxed; otherwise, a new satellite joins the PPP ser-
vice or a retired satellite is taken away. The IODP (Issue
Of Data, PRN mask) deﬁnes the versions of the satellite
mask. IODP is usually kept ﬁxed unless the bits in PRN
mask are changed. IODP also exists in the orbit correc-
tions (Type 2) and differential code biases (Type 3). PRN
mask, orbit corrections and differential code biases with
different IODP values should not be used together.
2) Orbit correction parameters and user range accuracy
index
Orbit corrections are expressed in terms of radial, along-
track and cross-track corrections through Type 2 (Orbit
Correction Parameters and User Range Accuracy Index).
Note that the orbit corrections of BDS satellites refer to
the CNAV-1 message broadcasted by B1C (CSNO 2017)
and that the orbit corrections of GPS satellites refer to the
L-NAV of GPS L1 and L2 (GPS Directorate 2019). Using
the orbit corrections and the broadcasted navigation mes-
sage, users can obtain the satellite orbits relative to the
satellite phase centre. Therefore, no satellite phase centre
offsets corrections should be applied by the users. The
term IODN (Issue Of Data, Navigation) is used to match
Type 2 and the broadcasted navigation message. IODN
of Type 2 is expected to be equal to IODC (Issue Of Data,
Clock) in a CNAV-1 message or in an L-NAV message.
The orbit correction parameters and user range accuracy
index are used only if IODPs in the type and those in the
PRN mask are equal.
3) Differential Code Bias
The differential code bias deﬁnes the transmitting delay
difference of the signal components involved with
respect to the satellite clock parameters. Currently,
the B1C, B2a, B2b, B1I and B3I differential code
bias parameters are broadcasted. The differential code
bias corrections enable multiple ionosphere-free linear
combinations to be available to users. The differential
code bias should be used in matching the PRN mask by
the IODP.
4) Clock correction parameters
Clock correction parameters also refer to CNAV-1 mes-
sages broadcasted by B1C and L-NAV of GPS L1 and L2.
The clock correction parameters should be used matching the
orbit corrections with the same IOD Cor. A clock correction
is invalid if it equals -26.2128 m. If a clock correction equals
-26.2128 m, users should not use this satellite for PPP.
Estimation of clock corrections is aligned with BDT.
However, the PPP-B2b ICD deﬁnes that the absolute value
of clock corrections should be no larger than 26.2128 m,
which is not large enough to contain the difference between
GPST and BDT. Furthermore, no accurate GPST/BDT dif-
ference parameters are broadcasted by PPP-B2b. Therefore,
for BDS/GPS dual-system users, two different receiver clock
offsets should be set and estimated epoch by epoch. If the
dual-system users estimate one receiver clock offset epoch
by epoch and one constant inter-system bias parameter, the
positioning accuracy may get worse.
3 Orbit and clock correction generation
and accuracy assessment
This section concentrates on the orbit and clock correction
accuracy of PPP-B2b broadcast message. A brief description
of the satellite orbit and clock correction generation process
123

<!-- PAGE: 4 -->

60
Page 4 of 17
C. Tanget al.
Fig. 1 Main ﬂow chart of satellite orbit and clock correction generation
is presented, followed by the accuracy assessment of the orbit
and clock corrections of GPS and BDS-3 satellites.
3.1 Satellite orbit and clock correction generation
Precise satellite orbit and clock correction generation for
PPP-B2b is conducted using the orbit and clock deter-
mination software developed by Shanghai Astronomical
Observatory, Chinese Academy of Science and Beijing Satel-
lite Navigation Centre. The software is operated at the control
segment. Satellite orbit and clock correction determination
is divided into four different processes, as shown in Fig. 1.
Thesatelliteorbitdeterminationprocessisconductedperi-
odically in batch mode and estimates precise BDS and GPS
orbit solutions using code/phase measurements from ground
monitoring receivers and inter-satellite link measurements in
combination. Orbit corrections are generated by differencing
precise orbit solutions with broadcast orbits in the orbit cor-
rection generation process.
In consideration of the irregular behaviour and random
variations of the on-board atomic clock, the real-time clock
estimation process takes code and phase measurements as
input and estimates satellite clock offsets using code and
phase measurements in real-time with a Kalman ﬁlter. To
reduce the computation burden and time loss, the satellite
orbits are no longer estimated but ﬁxed to solutions gen-
erated by the satellite orbit determination process. Finally,
clock corrections are generated by differencing precise clock
offset solutions with broadcast clock parameters in the clock
correction generation process.
3.1.1 Satellite orbit determination strategy
The satellite orbit determination process follows the sta-
tistical orbit determination form using the least-squares
estimation (Weiss et al. 2017). Precise orbits are usually
generated by the orbit determination process using code
and phase measurements from monitoring stations within
a global tracking network. A new orbit determination
strategy of BDS-3 satellites is implemented for the PPP
service, in which the BDS-3 orbits are estimated using
inter-satellite link (ISL) measurements and observations
from 7 stations in mainland China in combination instead
of the globally-distributed monitoring stations. By doing
so, maintenance cost of the globally-distributed stations is
saved. As indicated from Yang et al. (2019a), inter-satellite
link measurements of BDS-3 follow a time division multiple
access (TDMA) structure. According to Tang et al. (2018),
a pair of satellite A and B in view receives pseudorange
measurements from each other at different times. The
observation equations are,
ρAB(t1) 
 ⃗RB(t1) −⃗RA(t1 −t1)
 + c ∗clkB(t1)
−c ∗clkA(t1) + c ∗τ Send
A
+ c ∗τ Rcv
B
+ ρ AB
cor
ρB A(t2) 
 ⃗RA(t2) −⃗RB(t2 −t2)

+ c ∗clkA(t2) −c ∗clkB(t2) + c ∗τ Send
B
+ c ∗τ Rcv
A
+ ρ B A
cor
(1)
where ⃗RA and ⃗RB arethevectorsrepresentingCartesiancoor-
dinates of satellite A and satellite B, clkA and clkB are the
clock offsets,t1 and t2 are the signal travel times.τ Send
A
and τ Rcv
A
are the sending hardware delay and receiving hard-
ware delay for satellite A respectively, τ Send
B
and τ Rcv
B
are
the sending hardware delay and receiving hardware delay
for satellite B respectively. ρ AB
cor and ρ B A
cor are the easily-
modelled errors, such as phase centre offset corrections,
gravitational time delay and relativistic effect due to orbital
eccentricity.
123

> [1 Figure(s)]

<!-- PAGE: 5 -->

Orbit determination, clock estimation and performance …
Page 5 of 17
60
Using predicted satellite orbit and clock parameters, the
geometrical distances can be derived with accuracy loss of
less than 1 cm:
(2)
ρAB(t0) + ρB A(t0)
2

 ⃗RB(t0) −⃗RA(t0)
 + c ∗X A
Delay
+ c ∗X B
Delay + ρ AB
cor + ρ B A
cor
2
where, X A
Delay  τ Send
A
+τ Rcv
A
2
, X B
Delay  τ Send
B
+τ Rcv
B
2
, t0 is the
target time which is usually chosen as t1 or t2.
The derived geometrical distances between the two satel-
lites are regarded as inputs in the orbit determination together
with observations from the regional network. The ISL mea-
surements have advantages for orbit determination because
of the geometrical distances that are free of clock offsets
and wider coverage. Furthermore, while the ground stations
track the satellites nearly parallel with the radial direction,
the ISL measurements are more sensitive to along-track and
cross-track directions. By geometrical distances and regional
observations in combination, the orbit solutions are accurate
and comparable to those from 30 globally-distributed moni-
toring receivers (Yang et al. 2019b).
However, the precise orbit determination strategy of GPS
satellites is different from that of BDS-3 satellites. GPS orbit
determination and BDS-3 orbit determination are conducted
separately in two processe. For GPS satellites, un-differenced
L1/L2 ionosphere-free code and phase combinations from 30
globally-distributed stations are used in orbit determination.
The satellite orbit determination process is conducted
every 1 h with a 3-day arc with sampling interval of 60 s. Then
one-hour predicted orbit is generated using the estimated
dynamical variables. The orbit corrections are generated
using the predicted orbit.
The detailed orbit determination strategy is summarized
in Table 2. In the orbit determination process, ﬂoat ambi-
guities are used. The ECOM solar radiation model is used
without prior model and ﬁve acceleration parameters are
estimated including constant accelerations in D, B and Y
directions, cosine and sine accelerations in the B direction
during a 3-day arc (Springer et al. 1999). During eclipses,
the eclipsing factor is modelled in the solar radiation model
and the attitude angles are modelled following Kouba (2009)
and Montenbruck et al. (2015) for GPS satellites and laws
provided by the manufacturers for BDS-3 satellites (CSNO
2019c).
From Eq. (2), the unknown hardware delays are present
in the geometrical distances derived from ISL dual one-way
measurements. Therefore, one hardware delay parameter
per satellite is set and estimated. The estimated parameters
include 6 initial satellite elements and 5 solar pressure model
parameters per satellite, one station-speciﬁc ZTD parameter
every 2 h, ﬂoat ambiguities, satellite-speciﬁc ISL hardware
delays and epoch-wise clock offsets. The receiver and satel-
lite clock offsets are treated as epoch-wise white noise in
orbit determination. For BDS-3 orbit determination with 3-
day arc and 60 s sampling, 34 clock offsets per epoch are
estimated including 27 BDS-3 satellites and 7 receivers. The
total number of clock offsets reaches more than 70,000. If
other global variables are estimated together with the epoch-
wise clock offsets, the computation burden will become too
big. Therefore, the clock offsets elimination method by Zhou
et al. (2011) and Tang et al. (2016) is applied.
3.1.2 Real-time satellite clock estimation strategy
The satellite clock estimation process is conducted in real-
time with a Kalman ﬁlter using un-differenced ionosphere-
free code and phase combinations from the regional network
within mainland China by ﬁxing predicted orbits from the
satellite orbit determination process. The clock offsets of
satellites and receivers are modelled as white noises and are
estimated epoch-wise. To avoid rank deﬁciency, the offset
of one speciﬁc clock should be regarded as the clock datum
and kept ﬁxed on known values. In the proposed strategy,
clock offsets of the receiver located at the master station and
aligned to BDT are kept as the clock datum to estimate off-
sets of the satellites and other ground receivers. By doing so,
the estimated precise satellite clock offsets refer to BDT. Due
to the possible irregular behaviour of the clocks, the clock
offsets of satellites and receivers are estimated as white noise
and the process noise is 1 ms/
√
1s.
The tropospheric delay is corrected with the Saastamoinen
model and GMF (Boehm et al. 2006; Saastamoinen 1972).
The residual tropospheric delay is modelled and estimated as
a random-walk process. The process noise is 1 cm/
√
1hour.
The ﬂoat ambiguities are also estimated. A detailed real-time
satellite clock estimation strategy is summarized in Table 3.
3.2 Accuracy of orbit and clock corrections
of PPP-B2b broadcast message
The accuracy of the PPP-B2b broadcast message is eval-
uated by comparing the orbit and clock corrections with
the MGEX (multi-GNSS) precise products generated by
the GeoForschungsZentrum Potsdam (GFZ) analysis centre
(Montenbruck et al. 2013, 2017; Steigenberger and Mon-
tenbruck 2020).
3.2.1 Accuracy of orbit solutions
Evaluation is done using PPP-B2b broadcast messages from
August 1, 2020, to August 7, 2020. The 3D orbit accuracy of
the MGEX GFZ products is 5 cm for GPS by orbit compar-
isons (Steigenberger and Montenbruck 2020 and Kazmierski
123

<!-- PAGE: 6 -->

60
Page 6 of 17
C. Tanget al.
Table 2 Strategy of the orbit determination process
Orbit determination process strategy
Observations
For BDS-3 satellites, un-differenced B1I/B3I ionosphere-free code and phase combinations from a regional
network containing 12 stations within mainland China and the geometrical distances between two satellites
derived from ISL measurements are used in combination
For GPS satellites, un-differenced L1/L2 ionosphere-free code and phase combinations from 30
globally-distributed stations
Elevation angle cut-off
7°
Arc length
3 days
Sampling
60 s
Satellite PCO
Values from manufacturers for BDS-3, igs14.atx for GPS (Rebischung et al. 2016)
Receiver antenna PCO
Values from manufacturers. The receiver antennas used are made by Chinese manufacturers, whose PCO values
are not provided by igs14.atx
Satellite PCV
Not applied for BDS-3, igs14.atx for GPS (Rebischung et al. 2016)
Receiver antenna PCV
Not corrected. The receiver antennas used are made by Chinese manufacturers, whose PCV values are provided
by neither igs14.atx nor manufacturers
Station coordinates
The station coordinates are ﬁxed in the BDCS frame with is aligned to ITRF2014, which are kept as known
values in orbit determination
Troposphere delay
Saastamoinen model (Saastamoinen 1972) for wet and dry hydrostatic delay with the GMF (Boehm et al.2006)
without the gradient model
Ionosphere delay
The ﬁrst-order ionosphere delay is eliminated by the dual-frequency combinations
Orbit models
Two-body motion and non-spherical Earth; the attracting forces of the sun and the moon; tidal potential and
solar radiation pressure
Solar radiation model
Constant accelerations in the D direction, B direction and Y direction; cosine and sine accelerations in the B
direction (Springer et al.1999). D is the direction Satellite-Sun. Y points along the satellite’s solar panels axes,
and B completes the orthogonal system
Estimated parameters
The initial satellite positions and velocities, 5 solar pressure model parameters, satellite and receiver clock
offsets, one zenith tropospheric delay parameter (ZTD) per hour and carrier phase ambiguities,
satellite-speciﬁc ISL hardware delays
Estimation
Least-squares estimation
et al. 2018). Currently, the accuracy of BDS-3 orbits has not
yet been estimated. The 3D accuracy is 18 cm for BDS-
2 MEO satellites and 36 cm for BDS-2 IGSO satellites
(Steigenberger and Montenbruck 2020 and Kazmierski et al.
2018).
Note that the PPP-B2b orbits and MGEX GFZ orbits refer
to different points. The PPP-B2b BDS-3 orbits are relative to
the satellite B3 phase centre, the PPP-B2b GPS orbits are rel-
ative to the L1/L2 ionosphere-free combination phase centre
of the satellite, and the MGEX GFZ orbits are relative to the
satellite centre-of-mass. The satellite phase centre offsets are
corrected in the comparisons. The orbit differences are used
as follows:
−→
e  −→
B −Tr ∗−→
P −−→
R
(3)
In the above equation, −→
e refers to the orbit difference,
−→
B means the broadcasted orbits of the navigation message,
−→
P refers to the satellite phase centre offsets in the satellite-
ﬁxed system, Tr means the transformation matrix from the
satellite-ﬁxed system to the Earth-ﬁxed system, which can be
calculated by the attitude models reported by Kouba (2009)
and Montenbruck et al. (2015) for GPS satellites and pro-
vided by the manufacturers for BDS-3 satellites (CSNO
2019c). −→
R refers to the precise orbits of the MGEX GFZ.
The phase centre offset values from the IGS-ANTEX ﬁle are
used for the GPS and BDS-3 orbit comparisons.
The root mean square (RMS) values of the orbit differ-
ences are given in Fig. 2 for the BDS and in Fig. 3 for the
GPS. The mean RMS values by satellite type are summarized
in Table 4. The user ranging error (URE) is also calculated
and given in the ﬁgures and table. The URE is calculated as
follows (Zhou et al. 2011):
For IGSO, U RE 

R2 + (0.09 ∗A)2 + (0.09 ∗C)2
(4)
For MEO, U RE 

(0.99 ∗R)2 + (0.14 ∗A)2 + (0.14 ∗C)2
(5)
where R, A and C refer to the orbit error in the radial, along-
track and cross-track directions, respectively.
123

<!-- PAGE: 7 -->

Orbit determination, clock estimation and performance …
Page 7 of 17
60
Table 3 Strategy of the real-time satellite clock estimation process
Real-time satellite clock estimation strategy
Observations
Un-differenced ionosphere-free code and phase combination from a regional network containing 12 stations within
Mainland China
Frequency band
L1/L2 ionosphere-free code and phase combinations for GPS; B1I/B3I ionosphere-free code and phase
combinations for BDS-3
Sampling
6 s
Elevation angle cut-off
7°
Satellite orbits
Phase centre orbits are obtained by adding phase centre offsets to centre-of-mass predicted orbits; phase centre orbits
are ﬁxed
Observation weight
Code: phase  1:10,000
Receiver antenna PCO
Values from manufacturers. The receiver antennas used are made by Chinese manufacturers, whose PCO values are
not provided by igs14.atx
Satellite PCV
Not applied for BDS-3; igs14.atx for GPS (Rebischung et al. 2016)
Receiver antenna PCV
Not corrected. The receiver antennas used are made by Chinese manufacturers, whose PCV values are provided by
neither igs14.atx nor manufacturers
Station displacement
Solid Earth tide, pole tide, ocean tide loading corrected (Petit and Luzum 2010)
Relativity
Corrected (Kouba 2004)
Troposphere delay
Saastamoinen model (Saastamoinen 1972) for wet and dry hydrostatic delay with the GMF (Boehm et al. 2006)
without the gradient model; residual tropospheric delay as a random-walk process. The process noise of the
residual tropospheric delay is 1 cm/
√
1hour
Ionosphere delay
The ﬁrst-order ionosphere delay is eliminated by the dual-frequency combinations
Receiver clock
Estimated as white noise, the initial value is given as 0 and prior covariance is given as 9*1012m2. Clock offsets of
the receiver located at the master station and aligned to BDT are kept as the clock datum to estimate offsets of the
satellites and other ground receivers
Satellite clock
Estimated as white noise, the initial value is given as 0 and prior covariance is given as 9*1012m2
Phase ambiguities
Estimated as constant parameters
Inter-System Biases
Estimated as random-walk variables
Estimation
Kalman ﬁlter
The orbit differences of BDS-3 IGSO satellites (C38, C39
and C40 in Fig. 2) are larger than those of BDS-3 MEO
satellites and GPS satellites. The mean radial orbit error is
approximately 0.155 m, the 3D orbit error is approximately
0.328 m, and the URE is approximately 0.157 m for the BDS-
3 IGSO satellites. The orbit differences of the BDS-3 MEO
satellites are at the same level as those of the GPS satellites.
The radial orbit differences are approximately 0.05 m, the
3D orbit differences are approximately 0.20 m, and the orbit
URE is better than 0.06 m.
From Fig. 2, it can be clearly seen that the radial errors
of C19-C22 and C41-C46 seem to be larger than those
of other MEO satellites. The available ISL measurements
may account for the phenomenon. The available ISL mea-
surements for the four satellites are fewer than other MEO
satellites by 15% during that period.
The ISL measurements are insensitive to the orbital ori-
entation parameters including inclination angle and right
ascension of ascending intersection. In the ISL enhanced
BDS-3 orbit determination, the reduction of orbit error in
the cross-track is smaller than in the radial and along-track
directions, resulting in larger orbit errors in the cross-track
direction.
3.2.2 Accuracy of clock solutions
The MGEX GFZ precise clock is taken as the reference for
evaluating the accuracy of the PPP-B2b clock solutions. The
PPP-B2b broadcast message with the same period as that of
the orbit evaluation is used for the clock accuracy evaluation.
Both the broadcasted PPP-B2b GPS clock corrections and
MGEX GFZ precise GPS clock offsets refer to the L1P/L2P
ionosphere-free combinations. However, the GFZ precise
BDS-3 clock offsets refer to the B1I/B3I ionosphere-free
combinations, while the broadcasted PPP-B2b BDS clock
corrections refer to B3I. Therefore, the MGEX DCB param-
eters provided by the Chinese Academy of Sciences (CAS)
areusedtocorrectthePPP-B2bBDSclockcorrectionsbefore
comparison (Wang et al. 2016).
Following Yao et al. (2017), the accuracy assessment of
the clock solutions follows a two-step process. Firstly, the
PPP-B2b satellite clock offsets are differenced with the GFZ
123

<!-- PAGE: 8 -->

60
Page 8 of 17
C. Tanget al.
Fig. 2 BDS satellite orbit
accuracy of PPP-B2b
0
0.05
0.1
0.15
0.2
0.25
C19
C20
C21
C22
C23
C24
C25
C26
C27
C28
C29
C30
C32
C33
C34
C35
C36
C37
C38
C39
C40
C41
C42
C43
C44
C45
C46
unit:m
Satellite PRN
BDS Satellite Orbit Accuracy of PPP-B2b
Radial
Along-track
Cross-track
URE
Fig. 3 GPS satellite orbit
accuracy of PPP-B2b
0
0.05
0.1
0.15
0.2
0.25
G01 G03 G05 G07 G09 G11 G13 G16 G18 G20 G24 G26 G28 G30 G32
unit:m
Satellite PRN
GPS Satellite Orbit Accuracy of PPP-B2b
Radial
Along-track
Cross-track
URE
123

> [1 Figure(s)]

<!-- PAGE: 9 -->

Orbit determination, clock estimation and performance …
Page 9 of 17
60
Table 4 RMS of orbit and clock
differences by satellite type
Satellite type
Orbit (m)
STD of clock difference (ns)
R
T
N
3D
URE
BDS-3 IGSO
0.155
0.188
0.220
0.328
0.157
0.241
BDS-3 MEO
0.042
0.133
0.155
0.210
0.051
0.172
GPS block IIR
0.050
0.153
0.120
0.202
0.057
0.156
GPS block IIR-M
0.046
0.148
0.115
0.193
0.053
0.162
GPS block IIF
0.047
0.164
0.119
0.209
0.055
0.177
GPS block IIIA
0.043
0.120
0.125
0.181
0.049
0.153
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
C19 C21 C23 C25 C27 C29 C32 C34 C36 C38 C40 C42 C44 C46
ns
Satellite PRN
STD of BDS Clock Diﬀerence
Fig. 4 STD of BDS-3 Satellite Clock Differences
precise clock offsets, Secondly, the mean clock differences
for all available satellites are subtracted from the above clock
differences toremovedifferences of timereference. For satel-
lite i, the clock differences can be written as:
clki(t)  clk B2b
i
−clkGF Z
i
−
ns

n1
clk B2b
n
−clkGF Z
n
ns
(6)
clk B2b
i
and clkGF Z
i
are the PPP-B2b satellite clock offsets
and GFZ precise clocks for satellite i respectively, ns is the
number of available satellites.
Standard Deviations (STDs) of the BDS-3 clock differ-
ences and GPS clock differences are given in Figs. 4 and 5,
respectively.Thestatisticsoftheclockdifferencesbysatellite
type are also given in Table 4. As shown in Table 4 and Fig. 5,
the STDs of most GPS satellite clock differences are less than
0.3 ns. The STD of clock differences is not satellite-type
dependent for GPS. The average STD of clock differences is
approximately 0.2 ns. The STD of the clock differences of
most BDS-3 satellites are at the same level as those of GPS
and smaller than 0.3 ns.
3.2.3 Accuracy of DCB parameters
DCB parameters of BDS-3 satellites are provided by the
PPP-B2b messages, including DCB(B1I), DCB(B1Cp) and
DCB(B2ap). Both the BDS-3 broadcast clock parameters
and the PPP-B2b precise clock offsets refer to the B3I
signal. DCBs mentioned above refer to differential code
biases between the corresponding signal and the B3I signal.
Speciﬁcally, DCB(B1I) refers to the differential code bias
between B1I and B3I. DCB(B1Cp) refers to the differen-
tial code bias between B1Cp and B3I. DCB(B2ap) refers
to the differential code bias between B2ap and B3I. The
Fig. 5 STD of GPS Satellite
Clock Differences
0
0.05
0.1
0.15
0.2
0.25
G02
G11
G13
G16
G19
G20
G22
G28
G05
G07
G12
G15
G17
G29
G31
G01
G03
G06
G08
G09
G10
G24
G25
G26
G27
G30
G32
G04
G18
IIR
IIR-M
IIF
IIIA
ns
Satellite PRN
STD of GPS Clock Diﬀerence
123


|0.35<br>0.3<br>0.25<br>0.2<br>ns|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns||||||||||
|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns||||||||||||||||||||||||||
|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns|0.2<br>0.25<br>0.3<br>0.35<br>ns||||||||||||||||||||||||||
|0<br>0.05<br>0.1<br>0.15|0<br>0.05<br>0.1<br>0.15|||||||||||||||||||||||||||
|0<br>0.05<br>0.1<br>0.15|0<br>0.05<br>0.1<br>0.15|||||||||||||||||||||||||||
|0<br>0.05<br>0.1<br>0.15||||||||||||||||||||||||||||
|0<br>0.05<br>0.1<br>0.15||||||||||||||||||||||||||||




|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|Col39|Col40|Col41|Col42|Col43|Col44|Col45|Col46|Col47|Col48|Col49|Col50|Col51|Col52|Col53|Col54|Col55|Col56|Col57|Col58|Col59|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G02<br>G11<br>G13<br>G16<br>G19<br>G20<br>G22<br>G28<br>IIR|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G05<br>G07<br>G12<br>G15<br>G17<br>G29<br>G31<br>IIR-M|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G01<br>G03<br>G06<br>G08<br>G09<br>G10<br>G24<br>G25<br>G26<br>G27<br>G30<br>G32<br>IIF|G04<br>G18<br>IIIA|G04<br>G18<br>IIIA|G04<br>G18<br>IIIA|G04<br>G18<br>IIIA|G04<br>G18<br>IIIA|



<!-- PAGE: 10 -->

60
Page 10 of 17
C. Tanget al.
Fig. 6 Comparisons of the
PPP-B2b DCB parameters with
MGEX DCB products
-2.5
-2
-1.5
-1
-0.5
0
0.5
1
1.5
2
C19
C20
C21
C22
C23
C24
C25
C26
C27
C28
C29
C30
C32
C33
C34
C35
C36
C37
C38
C39
C40
C41
C42
C43
C44
C45
C46
ns
Satellite PRN
DCB Diﬀerence
DCB_B1I(B2b-MGEX)
DCB_B1Cp(B2b-MGEX)
DCB_B2ap(B2b-MGEX)
terms DCB(B1I), DCB(B1Cp) and DCB(B2ap) are com-
pared with MGEX DCB products provided by CAS (Wang
et al. 2016). DCB(B1I) parameters of all the BDS-3 satel-
lites, DCB(B1Cp) parameters of C19 to C37 and DCB(B2ap)
parameters of C19 to C37 are provided by CAS. The com-
parison is given in Fig. 6. It can be concluded that the
DCB(B1I) errors are smaller than 2.0 ns and DCB(B1Cp)
and DCB(B2ap) parameters are smaller than 1.0 ns. RMS of
DCB(B1I) errors, DCB(B1Cp) errors and DCB(B2ap) errors
are about 0.66 ns, 0.38 ns and 0.56 ns respectively.
The GPS DCBs are not provided by the PPP-B2b signals
and users are suggested to conduct L1/L2 dual-frequency
GPS PPP.
4 Precise point positioning validation
Performance of the PPP-B2b service is assessed by conduct-
ing PPP using measurements from six International GNSS
MonitoringandAssessmentService(iGMAS,Jiao2014)sta-
tions in mainland China (bjf1, chu1, kun1, sha1, wuh1 and
xia1) as mentioned in Fig. 7 during the period from August 1,
2020, to August 7, 2020. Both the static positioning process
and simulated kinematic positioning process are conducted
for validation. Three processing modes concerning the sys-
tems used are also applied, including BDS-3 only, GPS only
and the GPS/BDS-3 dual system. PPP with GFZ MGEX
products is also conducted for comparison purposes.
PPP-B2b corrections used in the validation experiments
are decoded by a monitoring receiver provided by College
of Electronic Science and Engineering, National University
of Defence Technology, located in Shanghai. The receiver
decodes the PPP-B2b messages from the three GEO satel-
lites. The receiver outputs precise corrections only if PPP-
B2b messages from two of the three GEO satellites pass the
consistency check. The PPP strategy is summarized as fol-
lows.
4.1 Static PPP validation
In this section static precise point positioning is conducted
using PPP-B2b precise corrections. Static PPP accuracy is
assessed in terms of convergence time, positioning repeata-
bility and differences with IGS position solutions. Static
precise point positioning results with GFZ MGEX products
are also conducted for comparison purpose.
4.1.1 Convergence
The PPP-B2b message decoded by the receivers was miss-
ing during 23:00-01:00 every day due to a data transmission
software problem. Therefore, the PPP is reinitialized at 1:00
every day and ends at 23:00. The convergence time of static
123


|DCB Difference|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||
|||||||||||||||||||||||||
|||||||||||||||||||||||||
|||||||||||||||||||||||||
|C19<br>C20<br>C21<br>|C19<br>C20<br>C21<br>|C19<br>C20<br>C21<br>|C22<br>C23<br>C24<br>|C22<br>C23<br>C24<br>|C22<br>C23<br>C24<br>|C25<br>|C26<br>|C27|C28||C29<br>|C30<br>C32<br>C33<br>|C30<br>C32<br>C33<br>|C30<br>C32<br>C33<br>|C34<br>|C35<br>C36<br>C37<br>|C35<br>C36<br>C37<br>|C35<br>C36<br>C37<br>|C38<br>C39<br>|C40<br>C41<br>C42<br>|C43<br>C44<br>C45<br>C46|C43<br>C44<br>C45<br>C46|C43<br>C44<br>C45<br>C46|
|||||||||||||||||||||||||
|||||||||||||||||||||||||
|||||||||||||||||||||||||
|||||||||||||||||||||||||



<!-- PAGE: 11 -->

Orbit determination, clock estimation and performance …
Page 11 of 17
60
Fig. 7 iGMAS Stations for PPP
validation
Table 5 PPP strategy
PPP strategy
Observations
Undifferenced ionosphere-free code and phase combination from iGMAS stations including bjf1, chu1, kun1,
sha1, wuh1 and xia1
Frequency band
L1/L2 ionosphere-free code and phase combinations for GPS; B1I/B3I ionosphere-free code and phase
combinations for BDS-3
Elevation angle cut-off
7°
Sampling
60 s
Satellite orbits
For PPP-B2b, satellite orbits relative to the phase centre are obtained by adding orbit corrections to the broadcast
orbits; for the GFZ products, centre-of-mass orbits are obtained, with phase centre offsets from igs14.atx added
to the centre-of-mass orbits
Observation weight
Code: phase  1:10,000
Receiver antenna PCO
Values from manufacturers. The receiver antennas used are made by Chinese manufacturers, whose PCO values
are not provided by igs14.atx
Satellite PCV
Not applied for BDS-3; igs14.atx for GPS (Rebischung et al. 2016)
Receiver antenna PCV
Not corrected. The receiver antennas used are made by Chinese manufacturers, whose PCV values are provided
by neither igs14.atx nor manufacturers
Station displacement
Solid Earth tide, pole tide, ocean tide loading corrected (Petit and Luzum 2010)
Relativistic
Corrected (Kouba 2004)
Troposphere delay
Saastamoinen model (Saastamoinen 1972) for wet and dry hydrostatic delay with the GMF (Boehm et al. 2006)
without the gradient model; residual tropospheric delay as a random-walk process
Ionosphere delay
The ﬁrst-order ionosphere delay is eliminated by the dual-frequency combinations
Receiver clock
For BDS-only or GPS-only PPP, one receiver clock offset is set and estimated as white noise; for BDS/GPS
dual-mode PPP, two different receiver clocks are set and estimated as white noise. The initial value is given as 0
and prior covariance is given as 9*1012m2
Receiver position
Estimated as white noise for kinematic PPP and as constant values for static PPP
Satellite clock
Fixed at known values from the PPP-B2b message and GFZ products
Phase ambiguities
Estimated as constant parameters
Estimation
Forward Kalman ﬁlter
123

> [1 Figure(s)]

<!-- PAGE: 12 -->

60
Page 12 of 17
C. Tanget al.
Fig. 8 Convergence time of static PPP
PPP is ﬁrst evaluated. The convergence condition requires
that the horizontal absolute positioning error remains below
20 cm and the vertical remains below 40 cm for at least 5 min
for the corresponding direction.
The average convergence times for the six iGMAS stations
are given in Fig. 8. Compared to the BDS-3-only or GPS-only
PPP, the convergence time of the BDS-3/GPS dual-system
PPP is much shorter due to the larger number of satellites and
better geometry conditions at most times, except for station
chu1, the convergence time of which is a few minutes longer
for the BDS-3/GPS dual-system PPP than for the GPS only
PPP. Taking xia1 as an example, it requires approximately
20 min to converge for BDS-3-only or GPS-only PPP but
converges in less than 10 min for BDS-3/GPS dual-system
PPP. For BDS/GPS dual-system static positioning, 7 min to
12 min are required to obtain a convergent positioning result.
4.1.2 Positioning repeatability
The daily repeatability of the static positioning results with
the PPP-B2b products is calculated for positioning precision
assessment. The daily repeatability with the GFZ products
is also calculated for precision comparison purposes. The
station-speciﬁc repeatability is given in Fig. 9. The aver-
age repeatability is summarized in Table 6. From Fig. 9, the
repeatability of the positioning results with the GFZ products
is slightly better than that with PPP-B2b products in both
GPS-only and BDS/GPS dual-system situations. In BDS-
only situation, the horizontal positioning repeatability with
PPP-B2b is slightly better than that with GFZ products and
the vertical positioning repeatability with PPP-B2b is slightly
largerthanthatwithGFZproducts.TheBDS/GPSstaticposi-
tioning repeatability is smaller than 1.0 cm in the north and
east directions and smaller than 1.5 cm in the up direction.
From Table 6, the north direction has the smallest repeata-
bility, followed by the east direction. The up direction has
the largest repeatability. The average BDS/GPS dual-system
positioning repeatability is smaller than 1.0 cm in all direc-
tions. The BDS/GPS dual-system positioning repeatability is
smaller than that of the BDS-only or GPS-only positioning
results in the east and up directions. The differences in the
BDS/GPS dual-system positioning repeatability are within
0.5 cm between the PPP-B2b solutions and GFZ solutions.
4.1.3 Differences with IGS position solutions
The average BDS/GPS dual-system daily static position-
ing results for the above-mentioned period with the GFZ
products is taken as the ground truth of the iGMAS station
coordinates. Station-speciﬁc RMS of the daily positioning
errors with PPP-B2b products by taking the GFZ solutions
as the ground truth station coordinates as well as the mean
RMS are given in Table 7.
Table 7 reveals that the maximum position differences in
the north and east directions are 1.47 cm and that the average
differences are less than 1.0 cm. However, the position differ-
ences in the up direction are much larger. The average RMS
of difference in the up direction is approximately 3.0 cm, and
the largest differences reach 4.1 cm for wuh1. Larger position
differencesintheupdirectionmaybeattributedtotheslightly
larger errors of PPP-B2b orbit and clock corrections. From
Table 4, orbit errors of PPP-B2b corrections are at decimetre
level in the along-track and cross-track directions, which are
larger than the MGEX post-processed solutions.
4.2 Simulated Kinematic PPP validation
In this section simulated kinematic precise point positioning
is conducted using PPP-B2b precise corrections for iGMAS
stations. Although the iGMAS stations are static, the sta-
tion coordinates are treated as white noise and estimated
epoch-wise to assess performance of PPP-B2b service. The
accuracy is assessed in terms of convergence time and posi-
tioning accuracy after convergence.
4.2.1 Convergence
Simulated kinematic PPP is conducted with the same obser-
vations as static PPP. The convergence condition requires that
the horizontal absolute positioning error remain below 20 cm
and the vertical remain below 40 cm for at least 5 min for
the corresponding direction. The average convergence times
for the iGMAS stations are given in Fig. 10. From Fig. 10,
the convergence time of BDS/GPS dual-system positioning
is much shorter than that of the BDS-only or GPS-only posi-
tioning solutions. To obtain converged positioning results,
20 min to 51 min are required for BDS-only kinematic PPP,
123

<!-- PAGE: 13 -->

Orbit determination, clock estimation and performance …
Page 13 of 17
60
Fig. 9 Daily repeatability of static PPP
Table 6 Average repeatability of static PPP (unit: cm)
Products
N
E
U
BDS-only
GPS-only
BDS/GPS
BDS-only
GPS-only
BDS/GPS
BDS-only
GPS-only
BDS/GPS
PPP-B2b
0.309
0.495
0.351
0.465
0.758
0.447
1.122
1.382
0.792
GFZ
0.379
0.324
0.344
0.518
0.449
0.410
0.814
1.302
0.520
Table 7 RMS of difference between PPP-B2b position solutions and GFZ position solutions (unit: cm)
Station
N
E
U
BDS-only
GPS- only
BDS/GPS
BDS- only
GPS- only
BDS/GPS
BDS- only
GPS- only
BDS/GPS
Bjf1
0.58
0.39
0.52
1.09
0.53
0.77
2.20
1.92
2.22
Chu1
0.85
0.70
0.79
1.41
1.22
1.14
2.19
1.63
1.22
Kun1
0.88
1.12
0.81
0.95
0.95
0.63
3.41
2.68
3.50
Sha1
0.34
0.62
0.29
0.66
1.26
0.47
3.75
3.85
3.81
Wuh1
0.42
0.60
0.40
1.05
1.47
0.85
3.43
4.10
3.81
Xia1
0.68
0.73
0.60
0.99
0.96
0.76
3.20
3.63
3.39
Mean
0.62
0.69
0.57
1.02
1.07
0.77
3.03
2.97
2.99
123

<!-- PAGE: 14 -->

60
Page 14 of 17
C. Tanget al.
Fig. 10 Convergence time of simulated Kinematic PPP
16 min to 63 min are required for GPS-only kinematic PPP,
and less than 12 min are required for GPS/BDS dual-system
kinematic PPP.
4.2.2 Positioning accuracy
Average BDS/GPS dual-system daily static positioning
results for the above-mentioned period with the GFZ prod-
ucts is taken as the ground truth of the iGMAS station
coordinates for simulated kinematic positioning accuracy
assessment. The ﬁrst-hour positioning results after PPP
initialization are ignored to avoid the inﬂuence of the ini-
tialization time on the positioning accuracy evaluation. The
simulated kinematic positioning results of the iGMAS sta-
tion bjf1 are given in Fig. 11. The ﬁgure reveals that the
GPS/BDS dual-system positioning results are much more
stationary and ﬂuctuate less than the GPS-only or BDS-only
positioning results.
The RMS of the station-speciﬁc simulated kinematic
positioning error is given in Fig. 12. As shown, the sim-
ulated kinematic positioning error in the north direction is
the smallest, followed by that in the east direction, and
the up positioning error is the largest. The BDS/GPS dual-
system simulated kinematic positioning accuracy is better
than the GPS-only or BDS-only simulated kinematic posi-
tioning accuracy.
The average RMS values of the simulated kinematic posi-
tioning accuracy are listed in Table 8, which shows that the
RMS of the BDS-only kinematic positioning errors is 3.2 cm
in the north, 5.1 cm in the east and 10.8 cm in the up direc-
tions, while it drops to less than 2.2 cm in the north, less than
3.3 cm in the east and less than 8.5 cm in the up directions for
BDS/GPS dual-system positioning. The results indicate that
the simulated kinematic positioning accuracy obtained using
the PPP-B2b real-time precise corrections is at the same level
Fig. 11 Simulated Kinematic Positioning Results of bjf1 after Conver-
gence (unit: m) (red or ‘C’ stands for the BDS-only results, green or
‘G’ stands for the GPS-only results, and blue or ‘GC’ stands for the
BDS/GPS dual-system results)
as that obtained using the IGS real-time products or QZSS
products (Zhang et al. 2018, Wang et al. 2018 and Zhang
et al. 2019).
From Table 8, the positioning errors with the PPP-B2b
products are from 0.5 cm to 4.0 cm larger than those with the
GFZ products for either single-system PPP or dual-system
PPP. Remember that the PPP-B2b products are generated in
real-time, while the GFZ products are post-processing prod-
ucts (Montenbruck et al. 2013, 2017). Optimal estimations
can be obtained in post-processing. However, real-time pro-
cessing often suffers from quality control and convergence
problems, resulting in larger orbits, clock errors and posi-
tioning errors (Fu et al. 2019).
5 Conclusions and discussion
PPP is one of the featured services of BDS-3, which provides
centimetre-level static positioning accuracy and decimetre-
level kinematic positioning accuracy to users around China.
The PPP performance is assessed by applying static PPP and
kinematic PPP processes to domestic iGMAS stations. Cen-
timetre level static and decimetre level kinematic positioning
accuracy can be expected. PPP-B2b service can be used in
numerous geodetic ﬁelds, such as real-time natural hazards
monitoring, water vapour monitoring and precise orbit deter-
mination of geodetic LEO satellites.
However, note that the positioning results with the PPP-
B2b products are slightly worse than those with the GFZ
123

<!-- PAGE: 15 -->

Orbit determination, clock estimation and performance …
Page 15 of 17
60
Fig. 12 RMS of positioning accuracy of simulated Kinematic PPP after one-hour initialization
Table 8 RMS of positioning accuracy of simulated Kinematic PPP after one-hour initialization (unit: cm)
Products
N
E
U
BDS-only
GPS-only
BDS/GPS
BDS-only
GPS-only
BDS/GPS
BDS-only
GPS-only
BDS/GPS
PPP-B2b
3.157
5.166
2.128
5.118
7.293
3.271
10.778
12.764
8.414
GFZ
3.330
3.341
1.669
5.646
4.499
2.769
11.810
8.672
7.376
post-processed products. The larger orbit error, quality con-
trol problems and convergence problems that the real-time
process faces may account for the larger positioning errors.
The real-time process will be improved for better position-
ing accuracy in the future, such as addition of more stations,
more robust estimation and more accurate phase centre cor-
rections.
Currently, PPP-B2b users require tens of minutes to
obtain a converged positioning result. Therefore, further
work will concentrate on faster convergence approaches,
such as PPP-AR and PPP-RTK. In addition, the PPP integrity
concept, parameterization and monitoring algorithms related
to signal-in-space error monitoring and risk alarms will be
studied to extend the applicability of PPP-B2b service.
Acknowledgements This research is funded by National Key Research
and Development Program of China (2016YFB0501405) and National
Natural Science Foundation of China (Grant No. 41804030, 41874039,
41874043, 41574029 and 41674041).
Author contributions XH and JC provided the initial idea for this study.
CT and XH wrote the article. CT and LL developed the real-time clock
estimation software and conducted the experiments. SZ and RG con-
ducted the inter-satellite link enhanced orbit determination experiments.
123

<!-- PAGE: 16 -->

60
Page 16 of 17
C. Tanget al.
XL and Feng He analysed the information type of PPP-B2b message.
Jianhua Yang evaluated orbit and clock accuracy. JL conducted the pre-
cise point positioning experiments.
Declarations
Conﬂict of interest The authors declare that they have no conﬂict of
interest.
Data availability The PPP-B2b broadcast message can be obtained with
a customized receiver following the public PPP-B2b ICD of BDS-3.
Measurements of iGMAS stations for evaluation can be obtained via
application. The GFZ products can be download from the IGS website.
References
Boehm J, Niell A, Tregoning P, Schuh H (2006) Global mapping func-
tion (GMF): a new empirical mapping function based on numerical
weather data. Geophys Res Lett 33:L07304. https://doi.org/10.
1029/2005GL025546
Calais E, Han JY, DeMets C, Nocquet JM (2006) Deformation of
the North American plate interior from a decade of continuous
GPS measurements. J Geophys Res 111:B06402. https://doi.org/
10.1029/2005JB004253
Chen JP, Hu XG, Tang CP, Zhou SS, Yang YF, Pan JY, Ren H, Ma YX,
Tian QN, Wu B, Yu Y (2020) SIS accuracy and service perfor-
mance of the BDS-3 basic system. Sci China Phys Mech Astron
63(6)
CSNO (2017) BeiDou navigation satellite system signal in space
interface control document-B1C (Version 1.0). China Satellite
Navigation Ofﬁce, 2017
CSNO (2019a) China satellite navigation ofﬁce, development of the
BeiDou navigation satellite system 4.0, China Satellite Navigation
Ofﬁce, 2019a
CSNO (2019b) BeiDou navigation satellite system signal in space inter-
face control document-precise point positioning service signal
PPP-B2b, China Satellite Navigation Ofﬁce, 2019b
CSNO (2019c) Deﬁnitions and descriptions of BDS/GNSS satellite
parameters for high precision application, China Satellite Navi-
gation Ofﬁce, 2019c
Fu W, Huang G, Zhang Q et al (2019) Multi-GNSS real-time clock
estimation using sequential least square adjustment with online
qualitycontrol.JGeodesy93(7):963–976.https://doi.org/10.1007/
s00190-018-1218-z
GPS Directorate (2019) Navstar GPS space segment/navigation user
segment interfaces. Interface speciﬁcation IS-GPS-200, revision
K, 5 June 2019, Global Positioning Systems Directorate
Jiao W (2014) International GNSS monitoring and assessment system
(iGMAS) and latest progress. In: Presented at China satellite nav-
igation conference (CSNC) 2014, Nanjing, 20 May 2014
Kazmierski K, So´snica K, Hadas T (2018) Quality assessment of multi-
GNSS orbits and clocks for real-time precise point positioning.
GPS Solutions, 2018, 22(1). https://doi.org/10.1007/s10291-017-
0678-6
Kouba J, Héroux P (2001) Precise point positioning using IGS orbit
and clock products. GPS Solut 2001, 5(2):12–28. https://doi.org/
10.1007/PL00012883
KoubaJ(2004)ImprovedrelativistictransformationsinGPS.GPSSolut
8(3):170–180. https://doi.org/10.1007/s10291-004-0102-x
Kouba J (2009) A simpliﬁed yaw-attitude model for eclipsing GPS
satellites. GPS Solut 13(1):1–12. https://doi.org/10.1007/s10291-
008-0092-1
Liu C, Gao W, Liu T, Wang D, Yao Z, Gao Y, Nie X, Wang W, Li D,
Zhang W, Wang D, Rao Y (2020) Design and implementation of a
BDS precise point positioning service. Navigation 67(4):875–891.
https://doi.org/10.1002/navi.392
Montenbruck O, Steigenberger P, Khachikyan R, Weber G, Langley
R, Mervart L, Hugentobler U, Langley K (2013) IGS-MGEX:
preparing the ground for multi-constellation GNSS science. In: 4th
international colloquium on scientiﬁc and fundamental aspects of
the Galileo system, 4–6 December 2013, Prague, CZ
Montenbruck O, Schmid R, Mercier F, Steigenberger P, Noll C, Fatkulin
R, Kogure S, Ganeshan A (2015) GNSS satellite geometry and
attitude models. Adv Space Res 56(6):1015–1029. https://doi.org/
10.1016/j.asr.2015.06.019
Montenbruck O, Steigenberger P, Prange L, Deng Z, Zhao Q, Perosanz
F, Romero I, Noll C, Sturze A, Weber G, Schmid R, Macleod
K, Schaer S (2017) The multi-GNSS experiment (MGEX) of the
international GNSS service (IGS)—achievements, prospects and
challenges. Adv Space Res 59(2017)7:1671–1697. https://doi.org/
10.1016/j.asr.2017.01.011.
Petit G, Luzum B: IERS Conventions (2010) IERS technical note No.
36, Verlag des Bundesamts für Kartographie und Geodäsie, Frank-
furt 2010
Rebischung P, Schmid R (2016) IGS14/igs14.atx: a new framework for
the IGS products, AGU Fall Meeting, San Francisco, 2016, USA
Rocken C, Johnson J, Van Hove T, Iwabuchi T (2005) Atmo-
spheric water vapor and geoid measurements in the open ocean
with GPS. Geophys Res Lett 32:L12813. https://doi.org/10.1029/
2005GL022573
Saastamoinen J (1972) Contributions to the theory of atmospheric
refraction. B Géodes 105(1):279–298
Springer TA, Beutler G, Rothacher M (1999) A new solar radiation
pressure model for GPS satellites. GPS Solut 1999, 2(3):50–62.
https://doi.org/10.1007/PL00012757
Steigenberger P, Montenbruck O (2020) (2020) Consistency of MGEX
orbit and clock products. Engineering 6:898–903. https://doi.org/
10.1016/j.eng.2019.12.005
Tang CP, Hu XG, Zhou SS et al (2016) Improvement of orbit determina-
tion accuracy for BeiDou navigation satellite system with two-way
satellite time frequency transfer. Adv Space Res 58(7):1390–1400.
https://doi.org/10.1016/j.asr.2016.06.007
Tang C, Hu X, Zhou S, et al (2018) Initial results of centralized
autonomous orbit determination of the new-generation BDS satel-
lites with inter-satellite link measurements. J Geodesy 2018,
92(10):1–15. https://doi.org/10.1007/s00190-018-1113-7
Wang L, Li ZS, Ge MR, Neitzel F, Wang Z, Yuan H (2018) Validation
and assessment of multi-GNSS real-time precise point positioning
in simulated kinematic mode using igs real-time service. Remote
Sens 2018, 10(2):337. https://doi.org/10.3390/rs10020337
Wang N, Yuan Y, Li Z et al (2016) Determination of differential code
biases with multi-GNSS observations. J Geod 90(3):209–228.
https://doi.org/10.1007/s00190-015-0867-4
Weiss JP, Steigenberger P, Springer T (2017) Orbit and clock product
generation. In: Teunissen PJ, Montenbruck O (eds) Springer hand-
book of global navigation satellite systems. Springer handbooks.
Springer, Cham. https://doi.org/10.1007/978-3-319-42928-1_34
Yang Y, Gao W, Guo S, et al (2019a) Introduction to Bei-Dou-3 navi-
gation satellite system. Navigation 66(1):7–18. https://doi.org/10.
1002/navi.291
Yang Y, Yang Y, Hu X et al (2019b) Inter-satellite link enhanced orbit
determination for BeiDou-3. J Navig 2019:1–16. https://doi.org/
10.1017/S0373463319000523
Yao Y, He Y, Yi W, Song W, Cao C, Chen M (2017) Method for eval-
uating real-time GNSS satellite clock ofset products. GPS Solut
21:1417–1425. https://doi.org/10.1007/s10291-017-0619-4
Zhang L, Yang H, Gao Y, et al. (2018). Evaluation and analysis of real-
time precise orbits and clocks products from different IGS analysis
123

<!-- PAGE: 17 -->

Orbit determination, clock estimation and performance …
Page 17 of 17
60
centers. Advances in Space Research, 2018, 61(12): 2942–2954.
https://doi.org/10.1016/j.asr.2018.03.029
Zhang S, Du S, Li W, et al (2019) Evaluation of the GPS precise orbit
and clock corrections from MADOCA real-time products. Sensors
2019, 19(11):2580:1–13. https://doi.org/10.3390/s19112580
Zhang XH, Andersen OB (2006) Surface ice ﬂow velocity and tide
retrieval of the amery ice shelf using precise point positioning. J
Geod 80(4):171–176. https://doi.org/10.1007/s00190-006-0062-8
Zhou SS, Cao YL, Zhou JH et al (2012) Positioning accuracy assess-
ment for the 4GEO/5IGSO/2MEO constellation of COMPASS.
Sci China Phys Mech Astron 55:2290–2299
Zhou SS, Hu XG, Zhou JH et al (2013) Accuracy analyses of
precise orbit determination and timing for COMPASS/Beidou-
2 4GEO/5IGSO/4MEO constellation. Lecture Notes Electr Eng
245:89–102
Zhou SS, Hu XG, Wu B et al (2011) Orbit determination and time
synchronization for a GEO/IGSO satellite navigation constella-
tion with regional tracking network. Sci China Phys Mech Astron
54:1089–1097
Zhu S, Reigber CH, König R (2004) Integrated adjustment of CHAMP
GRACE and GPS data. J Geod 78(1–2):103–108. https://doi.org/
10.1007/s00190-004-0379-0
Zumberge JF, Heﬂin MB, Jefferson DC, Watkins MM, Webb FH (1997)
Precise point positioning for the efﬁcient and robust analysis
of GPS data from large networks. J Geophys Res Solid Earth
1997(102):5005–5017. https://doi.org/10.1029/96JB03860
Springer Nature or its licensor holds exclusive rights to this article
undera publishingagreement withthe author(s)orotherrightsholder(s);
author self-archiving of the accepted manuscript version of this article
is solely governed by the terms of such publishing agreement and appli-
cable law.
123
