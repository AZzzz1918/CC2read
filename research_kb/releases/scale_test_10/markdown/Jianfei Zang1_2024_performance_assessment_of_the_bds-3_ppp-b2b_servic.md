<!-- PAGE: 1 -->

Vol.:(0123456789)
1 3
GPS Solutions           (2024) 28:26  
https://doi.org/10.1007/s10291-023-01570-x
ORIGINAL ARTICLE
Performance assessment of the BDS‑3 PPP‑B2b service for real‑time 
earthquake source description: a case study for the 2021 Mw 7.4 
Maduo earthquake
Jianfei Zang1 · Shijie Fan1 · Caijun Xu2 · Zhicai Li3 · Rongxin Fang4 · Yidong Lou4
Received: 13 August 2023 / Accepted: 24 October 2023 
© The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2023
Abstract
Retrieving the coseismic displacement in real time is essential when the high-rate Global Navigation Satellite System (GNSS) 
is used for the real-time earthquake source description. In 2020, the third generation of the BeiDou Global Navigation Satel-
lite System (BDS-3) initiated a real-time precise point positioning service through the B2b signal (PPP-B2b), which provides 
a new possibility for real-time earthquake source description. In this study, the performance of the PPP-B2b on the real-time 
retrieval of coseismic displacement was first validated with GNSS observations collected during the 2021 Mw 7.4 Maduo 
earthquake. Then, the warning magnitude, focal mechanism and fault slip distribution were inverted with the derived PPP-
B2b displacement in a simulated real-time model. Our results indicate that the accuracies of the coseismic displacements in 
the north, east and up components are 0.8 cm, 0.5 cm, and 1.4 cm for the single GPS PPP-B2b, 0.5 cm, 0.6 cm, and 0.9 cm 
for the single BDS-3 PPP-B2b and 0.4 cm, 0.3 cm, and 0.4 cm for the combined GPS/BDS-3 PPP-B2b, respectively, when 
compared with the coseismic displacements of the post-processing precise point positioning (PPP). Moreover, the warning 
magnitude, focal mechanism and fault slip distribution inverted with the PPP-B2b displacements are all in good agreement 
with those inverted with the PPP displacements. This study highlights the great possibility of the PPP-B2b to be used for 
earthquake early warning and rapid emergency responses.
Keywords  BDS-3 · PPP-B2b · Coseismic displacement · Earthquake source inversion
Introduction
A high-rate global navigation satellite system (GNSS) is rec-
ognized as an effective complementary means to traditional 
seismic instruments in real-time earthquake monitoring and 
providing early warnings, as high-rate GNSSs can directly 
measure the ground displacement without saturation in the 
near field. Many studies have demonstrated the great perfor-
mance of high-rate GNSSs on warning magnitude calcula-
tions (Crowell et al. 2013; Melgar et al. 2015; Zang et al. 
2020), focal mechanism inversions (Melgar et al. 2012), fault 
slip distribution inversions (Allen and Alon 2011; Minson 
et al. 2014; Zang et al. 2022) and fault dynamic rupture pro-
cess inversions (Miyazaki et al. 2004; Goldberg et al. 2020; 
Wen et al. 2021). It has been confirmed that both relative 
positioning and precise point positioning (PPP) can be used 
to retrieve high-accuracy coseismic displacements (Larson 
et al. 2003; Xu et al. 2013; Geng et al. 2017; Li et al. 2019). 
Compared with relative positioning, PPP can be utilized to 
measure ground motions from a single station alone without 
relying on reference stations and therefore is more suitable 
for earthquake monitoring. The accuracies of the PPP dis-
placements within a short period are at the 2–4 mm and sub-
centimetre levels in the horizontal and upper components, 
respectively, when the final precise orbit and clock products 
are used (Xu et al. 2013). However, when determining the 
final precise orbit and clock products, it has a long-time 
 *	 Shijie Fan 
	
fshijie@upc.edu.cn
1	
College of Oceanography and Space Informatics, China 
University of Petroleum (East China), Qingdao 266580, 
China
2	
School of Geodesy and Geomatics, Wuhan University, 
Wuhan 430079, China
3	
School of Geoscience and Surveying Engineering, 
China University of Mining and Technology-Beijing, 
Beijing 100083, China
4	
GNSS Research Center, Wuhan University, Wuhan 430079, 
China
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [2 Figure(s)]

<!-- PAGE: 2 -->

GPS Solutions           (2024) 28:26 
1 3
   26  
Page 2 of 13
delay and is thus unsuitable for real-time earthquake moni-
toring and providing early warnings. Since 2013, the inter-
national GNSS service (IGS) has provided real-time service 
(RTS) and has broadcasted precise orbit and clock correc-
tions to users through the internet in real time (Hadas and 
Bosy 2015), making it possible to perform real-time GNSS-
based earthquake monitoring and provide early warnings.
On July 31, 2020, the third generation of the BeiDou 
Global Navigation Satellite System (BDS-3) began pro-
viding global service. In addition to normal positioning, 
navigation and timing services, BDS-3 features a satellite-
based real-time precise point positioning service (Yang et al. 
2021), where precise satellite orbit and clock corrections are 
broadcast to users through the B2b signal of BDS-3 geosta-
tionary earth orbit (GEO) satellites. Compared with RTS 
products, the PPP-B2b does not suffer from the influence 
of internet interruption, and users can obtain real-time PPP 
(RT-PPP) easily by decoding the received B2b corrections. 
The performance of the PPP-B2b in real-time positioning 
has been validated by a series of tests, and the results show 
that the positioning accuracies of the static PPP-B2b and 
the simulated dynamic PPP-B2b can reach centimetre and 
decimetre levels (Nie et al. 2021; Ren et al. 2021; Tao et al. 
2021; Xu et al. 2021, 2023; Zhang et al. 2022; Tang et al. 
2022; Yang et al. 2022; Sun et al. 2023). In addition to the 
simulated dynamic tests, Zhang et al. (2022) performed two 
vehicle-based kinematic PPP-B2b tests and determined that 
the average position errors of the combined global position-
ing system (GPS) and the BDS-3 are 18.6 cm and 37.1 cm 
in the horizontal and vertical components, respectively. 
Geng et al. (2022) validated the performance of the PPP-
B2b in an open ocean environment and obtained results that 
indicate that the positioning accuracies of the combined 
GPS + BDS-3 in the north, east and up components are 
0.047 m, 0.036 m and 0.172 m, respectively. In addition 
to positioning, Ge et al. (2023) investigated the method of 
real-time time transfer with PPP-B2b corrections. Yang et al. 
(2023) evaluated the performance of the PPP-B2b in real-
time precipitable water vapour retrieval. In particular, Fang 
et al. (2022) validated the feasibility of real-time coseismic 
displacement retrieval with PPP-B2b by a shake table test 
and 2021 Mw 7.4 Maduo earthquake data. Their results indi-
cate that the accuracies of the coseismic displacements of 
the PPP-B2b are 2–3 cm within a short period of time when 
taking the post-processed PPP displacements as a reference.
Although the performance of the PPP-B2b in real-time 
positioning has been validated by a series of studies, most 
researchers have focused on the evaluation of the PPP-B2b 
for a long time. In earthquake monitoring and providing 
early warnings, the short-term performance of the PPP-
B2b matters because the energy release of an earthquake 
usually lasts for seconds or minutes. However, few studies, 
in which the performance of the PPP-B2b was assessed 
for short time periods and the PPP-B2b displacement was 
applied for real-time earthquake source inversions, were 
conducted. In the study of Fang et al. (2022), only one 
station recorded the BDS-3 observations during the 2021 
Mw 7.4 Maduo earthquake. In this study, we collected 
data from 13 GNSS stations that recorded both the GPS 
and BDS-3 observations during the 2021 Mw 7.4 Maduo 
earthquake. The performances of the single GPS PPP-B2b, 
single BDS-3 PPP-B2b and combined GPS/BDS-3 PPP-
B2b for real-time coseismic displacement retrieval are all 
evaluated. In addition, we performed a warning magni-
tude calculation, focal mechanism inversion and fault slip 
distribution inversion with the derived PPP-B2b displace-
ments to validate the possibility of real-time earthquake 
source inversion with the PPP-B2b displacements. The rest 
of this paper is organized as follows: First, we introduced 
the RT-PPP method with PPP-B2b corrections and the 
real-time earthquake source inversion method with PPP-
B2b displacements. Then, the accuracies of the derived 
coseismic displacements and the inverted earthquake 
source parameters of the Maduo earthquake are analysed. 
Finally, we provided the conclusions of this study.
Methodology
In this section, the recovery procedure of the precise satel-
lite orbit and clock offsets with the PPP-B2b corrections 
are first introduced. Then, the PPP-B2b positioning model 
and the earthquake source inversion methods are presented 
in detail.
Recovery of the precise satellite orbit and clock 
offsets with PPP‑B2b corrections
At present, the PPP-B2b service mainly provides differential 
code bias (DCB) and satellite orbit and clock corrections 
to users. Although the B2b signal was designed to transmit 
GPS, BDS, GLONASS and Galileo corrections, only GPS 
and BDS-3 corrections are currently available. For GPS, 
PPP-B2b corrections are added to the satellite orbit and 
clock offsets that are calculated with the GPS LNAV broad-
cast ephemeris. For BDS-3, the BDS-3 CNAV1 broadcast 
ephemeris is adopted to calculate the initial satellite orbit 
and clock offsets. Then, the initial values are corrected with 
the PPP-B2b products. However, the satellite orbit offsets 
derived from the broadcast ephemeris are of the Earth-Cen-
tre-Earth-Fixed (ECEF) frame, and thus, the PPP-B2b orbit 
corrections, including the radial, along-track, and cross-
track components, must be converted into corrections of 
the ECEF, which can be achieved as follows (CSNO 2020):
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 3 -->

GPS Solutions           (2024) 28:26 	
1 3
Page 3 of 13 
   26 
where 훿X represents the PPP-B2b orbit correction vector 
in the ECEF; 훿퐎radial , 훿퐎along and 훿퐎cross are the PPP-B2b 
orbit corrections in the radial, along-track and cross-track 
directions; and 퐫 and ̇퐫 indicate the satellite position and 
velocity vectors calculated with the broadcast ephemeris in 
the ECEF. With the correction vector of 훿X , the precise sat-
ellite orbit offset can be recovered by:
where 퐗orbit denotes the precise satellite orbit offset and 
퐗broadcast represents the satellite orbit offset calculated with 
the broadcast ephemeris.
The precise satellite clock offset can be calculated as 
follows:
where tclock represents the precise satellite clock offset; 
tbroadcast indicates the satellite clock offset derived from the 
broadcast ephemeris; C0 is the satellite clock correction 
decoded from the B2b signal; and c is the speed of the light 
in the vacuum.
PPP‑B2b positioning model
The PPP-B2b positioning model is consistent with the PPP 
model. Here, traditional dual-frequency ionospheric-free (IF) 
combinations are used to remove the influence of the first-
order ionospheric delay. The code and phase observation equa-
tions of the PPP-B2b positioning model can be expressed as 
follows (Leick et al. 2015):
where Ps
r,IF and Ls
r,IF denote the code and phase IF combina-
tions of the L1/L2 for GPS and B1/B3 for BDS-3, respec-
tively; 휌s
r represents the geometric distance from the satellite 
(1)
훿X =  퐞radial 퐞along 퐞cross
 ⋅
⎡
⎢
⎢⎣
훿퐎radial
훿퐎along
훿퐎cross
⎤
⎥
⎥⎦
(2)
퐞radial = 퐫
|퐫|
(3)
퐞cross = 퐫× ̇퐫
|퐫× ̇퐫|
(4)
퐞along = 퐞cross × 퐞radial
(5)
퐗orbit = 퐗broadcast −훿X
(6)
tclock = tbroadcast −C0
c
(7)
Ps
r,IF = 휌s
r + tr −ts + dr,IF −ds
IF + ms
rT + es
r,PIF
(8)
Ls
r,IF = 휌s
r + tr −ts + br,IF −bs
IF + 휆IFNs
r,IF + ms
rT + 휀s
r,LIF
to the receiver; tr and ts are the clock offsets of the receiver 
and satellite, respectively; dr,IF and ds
IF represent the code 
biases of the receiver and satellite, respectively; br,IF and bs
IF 
are the phase biases of the receiver and satellite, respec-
tively; ms
r indicates the mapping function of the tropospheric 
delay; T is the zenith tropospheric delay; 휆IF and Ns
r,IF are the 
wavelength and ambiguity of the IF combination, respec-
tively; and es
r,PIF and 휀s
r,LIF represent the noises in the code and 
phase observations, respectively. Other errors, such as the 
phase centre deviation, phase wind-up, relativistic effect, 
solid earth tide, ocean tide and pole tide, can be corrected 
with the existing models.
Notably, the PPP-B2b clock corrections refer to the L1/
L2 IF combination for GPS and the B3 signal for BDS-3 
(Tang et al. 2022). It is necessary to convert the BDS-3 
clock correction from the B3 signal to the B1/B3 IF com-
bination, which can be achieved as follows (Fang et al. 
2022):
where ts
B1B3 and ts
B3 denote the recovered precise satellite 
clock offsets referring to the B1/B3 IF combination and the 
B3 signal, respectively; fB1 and fB3 are the frequencies of 
the B1 and B3 signals, respectively; and DCBs
B1B3 represents 
the DCB correction between the B1 and B3 signals decoded 
from the B2b signal.
As dr,IF in Eq. (7) can be absorbed by the receiver clock 
offset and br,IF and bs
IF in Eq. (8) can be absorbed by the 
phase ambiguity, the observation Eqs. (7) and (8) can be 
rewritten as
where ̃Ps
r,IF and ̃Ls
r,IF are the observations minus the com-
puted code and phase, respectively; 퐮s
r denotes the unit direc-
tion vector from the satellite to the receiver; 퐱 is the vector 
of the receiver position increment; and dZWD represents the 
zenith wet delay. The unknown parameters, including the 
receiver position, clock offset, phase ambiguity and zenith 
wet delay, can be estimated with a Kalman filter.
Real‑time earthquake source inversion 
with PPP‑B2b displacements
Studies have confirmed that the earthquake magnitude 
inverted with the GNSS peak ground displacement (PGD) 
does not undergo magnitude saturation. The empirical 
(9)
ts
B1B3 = ts
B3 −
f 2
B1
f 2
B1 −f 2
B3
DCBs
B1B3
(10)
̃Ps
r,IF = −퐮s
r ⋅퐱+ ̃tr + ms
r,ZWD ⋅dZWD + es
r,PIF
(11)
̃Ls
r,IF = −퐮s
r ⋅퐱+ ̃tr + 𝜆IF ̃Ns
r,IF + ms
r,ZWD ⋅dZWD + 𝜀s
r,LIF
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 4 -->

GPS Solutions           (2024) 28:26 
1 3
   26  
Page 4 of 13
relationship between the PGD and the earthquake mag-
nitude can be expressed as follows (Crowell et al. 2013; 
Zang et al. 2020):
where MW denotes the earthquake magnitude; R represents 
the epicentre distance; A , B and C are the regression coef-
ficients with values of − 4.434, 1.047 and − 0.138, respec-
tively, provided by Melgar et al. (2015); and Nt , Et and Ut 
indicate the real-time series of the PPP-B2b displacements 
in the north, east and up components, respectively.
For the focal mechanism inversion, we applied the 
fastCMT method (Melgar et al. 2012), where the centroid 
moment tensor (CMT) is inverted with the real-time static 
coseismic offsets derived from the GNSS displacements. 
In this study, we extracted the real-time static coseismic 
offsets by averaging the real-time PPP-B2b displacements 
with a 30-s sliding window. The real-time static coseismic 
offset d and the CMT m are related through (Melgar et al. 
2012)
where dk
i (t) refers to the i th component of the static coseis-
mic offsets at Station k ; t represents the time epoch; mj 
denotes the j th component of the CMT; Gk
i,j is the Green’s 
function that relates the j th component of the moment tensor 
to the i th component of the static coseismic offsets, which 
can be determined by the EDGRN program (Wang et al. 
2003); and n is the number of GNSS stations.
After the inversion of the CMT at each epoch, the fault 
slip distribution inversion will follow shortly with the 
extracted real-time static coseismic offsets on the fault plane 
derived based on the inverted CMT results. The fault length 
and width are set to three times and one time the output 
values of the scaling laws developed by Wells and Copper-
smith (1994). The entire fault plane is discretized into 8-km 
along-strike by 6-km down-dip independent small patches, 
and the slips of all patches are linearly inverted with the non-
negative least-squares method. The inverse problem can be 
written as follows:
where d denotes the extracted real-time static coseismic 
offsets at epoch t; u represents slips on each patch; and G is 
the matrix of the Green’s function determined by the Okada 
mode (1985) that relates the unit slip in each patch to the 
permanent ground coseismic offset. To solve the ill-posed 
problem in the inversion, Laplacian spatial regularization is 
(12)
log10 (PGD) = A + B ⋅MW + C ⋅MW ⋅log10 (R)
(13)
PGD = max
√
N2
t + E2
t + U2
t
(14)
dk
i (t) = Gk
i,jmj(t);(i = x, y, z;j = 1, 2, 3, 4, 5;k = 1, 2, 3 … , n)
(15)
d(t) = G(t) ⋅u(t)
used, and the optimal regularization parameter is determined 
by the L-curve method (Zang et al. 2022).
Experiment and results analysis
The 2021 Mw 7.4 Maduo earthquake occurred in the east-
ern portion of the Tibetan Plateau at 18:04 UTC on May 
21 and was in the centre of the Baya Har block, one of the 
most active blocks in China. This earthquake caused obvi-
ous surface rupture and the west part of the surface rupture 
zone occurred along the pre-existing Kunlun Pass-Jiangcuo 
fault (Wang et al. 2021; Pan et al. 2021; Chen et al. 2022; 
Ren et al. 2022). In this study, we utilized the data from 
13 GNSS stations (Fig. 1) with epicenter distance less than 
200 km to evaluate the performance of the PPP-B2b in real-
time earthquake source inversion. These stations can record 
both GPS and BDS-3 observations and are of the Crustal 
Movement Observation Network of China (CMONOC), the 
Continuously Operating Reference Stations of Qinghai Prov-
ince in China (CORS) and the China Mobile Communica-
tions Group Co., Ltd. The PPP-B2b corrections are collected 
by an FRII-Plus receiver manufactured by Femtomes Tech 
(Beijing) Inc. We first processed the collected GNSS obser-
vations with the PPP-B2b positioning model in a simulated 
real-time model. For comparison, the GNSS observations 
are also processed with the traditional PPP method, where 
the final precise orbit and clock products provided by the 
International GNSS Service (IGS) Data Centre of Wuhan 
University are used. Then, we inverted the warning magni-
tude, focal mechanism, and fault slip distribution with the 
derived PPP-B2b displacements. To analyse the inverted 
results, the abovementioned earthquake source parameters 
are also inverted with the PPP displacements.
Accuracy assessment of the PPP‑B2b displacements 
over a relatively long time
To evaluate the performance of the PPP-B2b, we processed 
the collected GNSS observations with the single BDS-3 
PPP-B2b positioning model (PPP-B2bC) and the combined 
GPS/BDS-3 PPP-B2b positioning model (PPP-B2bGC). For 
comparison, we also processed the GPS/BDS-3 observations 
with the traditional PPP method. Four-hour displacements 
from 14:00 to 18:00 before the earthquake at Station QHAG 
are presented in Fig. 2. The displacements of the PPP are 
the most stable during this period. Compared with the dis-
placements of the PPP-B2bC, the displacements of the PPP-
B2bGC agree well with those of the PPP. Table 1 shows the 
statistical standard deviation (STD) values of the displace-
ments of all stations. It can be found that the STD values of 
the PPP-B2bGC for the north, east and up components are 
2.0 cm, 2.8 cm and 4.9 cm, respectively, which are larger 
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 5 -->

GPS Solutions           (2024) 28:26 	
1 3
Page 5 of 13 
   26 
than those of the PPP with the values of the 0.7 cm, 1.3 cm 
and 1.5 cm. For the PPP-B2bC, the STD values in the three 
components are 3.6 cm, 4.5 cm and 10.9 cm. It is clear that 
the fusion of the GPS/BDS-3 PPP-B2b can reduce the STD 
values when compared with the single BDS-3 PPP-B2b. It 
should be noted that we do not present the statistical results 
of the single GPS PPP-B2b here, as the GPS PPP-B2b dis-
placement causes significant errors due to the shortage of the 
PPP-B2b corrections for some GPS satellites.
Accuracy assessment of the PPP‑B2b displacements 
during a relatively short time
In contrast to the long time period allowed for crustal defor-
mation monitoring with GNSSs (Meng et al. 2019), earth-
quake ruptures usually last for seconds or minutes; thus, the 
short-term performance of the PPP-B2b is more important 
when the PPP-B2b is used for real-time earthquake source 
description. Here, we divided the four-hour displacements 
into short periods with a length of 5 min to evaluate the 
short-term performance of the PPP-B2b. The statistical STD 
values of all short-period displacements for the different 
solutions are shown in Table 2. Compared with the STD val-
ues of the four-hour displacements in Table 1, the STD val-
ues of the short-period displacements of all solutions show 
an obvious reduction, particularly for the PPP-B2bGC and 
the PPP-B2bC in the upper component. When comparing 
Fig. 1   Distribution of the 
collected GNSS stations (blue 
triangle). The red star repre-
sents the epicentre of the 2021 
Mw 7.4 Maduo earthquake. 
The black line is the Kunlun 
Pass-Jiangcuo fault. The black 
rectangle in the upper-left inset 
map indicates the location of 
the Tibetan Plateau, where the 
white lines represent secondary 
block boundaries in and around 
the Tibetan Plateau and the blue 
rectangle is the location of the 
study area
Fig. 2   Four-hour displacements derived from the PPP, combined 
GPS/BDS-3 PPP-B2b (PPP-B2bGC) and single BDS-3 PPP-B2b 
(PPP-B2bC) at Station QHAG before the 2021 Mw 7.4 Maduo earth-
quake
Table 1   Statistical standard deviation (STD) values of the four-hour 
displacements for the different solutions at all GNSS stations (unit: 
cm)
Solutions
North
East
Up
PPP
0.7
1.3
1.5
PPP-B2bGC
2.0
2.8
4.9
PPP-B2bC
3.6
4.5
10.9
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [2 Figure(s)]

<!-- PAGE: 6 -->

GPS Solutions           (2024) 28:26 
1 3
   26  
Page 6 of 13
the STD values between the different solutions, we found 
that the STD values of the PPP-B2bGC are much closer 
to those of the PPP in Table 2, and the STD differences 
between them are 0.1 cm, 0.1 cm and 0.3 cm for the north, 
east and up components, respectively. These results are sig-
nificantly better than the STD differences between them as 
shown in Table 1, where the corresponding difference values 
are 1.3 cm, 1.5 cm and 3.4 cm, respectively. When com-
paring the PPP-B2bGC with the PPP-B2bC, it is clear that 
the STD differences between them as shown in Table 2 are 
superior to those in Table 1, and the difference values are 
0.1 cm, 0.2 cm, and 0.3 cm and 1.6 cm, 1.7 cm, and 6.0 cm 
for Tables 1 and 2, respectively. All these statistical results 
indicate that the PPP-B2b has better performance during the 
short term for both the single BDS-3 and the combined GPS/
BDS-3. Compared with the single BDS-3 PPP-B2bC, the 
combined GPS/BDS-3 PPP-B2bGC reduces the displace-
ment noise at frequencies less than approximately 0.01 Hz 
and greater than approximately 0.03 Hz (Fig. S1).
Coseismic displacements derived from the PPP‑B2b 
during the 2021 Mw 7.4 Maduo earthquake
Figure 3 shows the coseismic displacements derived from 
the different PPP-B2b solutions at Station QHAG. Here, we 
also presented the coseismic displacements derived from 
the single GPS PPP-B2b (PPP-B2bG). In the PPP-B2bG 
processing, the GPS observations were first processed with 
the static mode before 18:02. Then, dynamic processing was 
carried out to prevent the reconvergence of the displacement 
caused by the shortage of PPP-B2b corrections. As shown in 
Fig. 3, there are good agreements in the coseismic displace-
ments between the PPP-B2bGC and the PPP for all three 
components. Compared with the PPP-B2bC, the PPP-B2bG 
shows more fluctuations, particularly in the upper compo-
nent, which might be related to the GPS satellite geometry. 
From Fig. S3, we can find that the position dilution of the 
precision (PDOP) of the PPP-B2bG is larger than that of the 
PPP-B2bC and the PPP-B2bGC.
Taking the coseismic displacements from the PPP as a 
reference, we calculated the coseismic displacement errors 
of the other three PPP-B2b solutions by subtracting the 
coseismic displacements of the PPP from those of the other 
three PPP-B2b solutions. The derived error series of the 
different solutions are presented in Fig. 4. Moreover, the 
PPP-B2bGC has the smallest errors in all three components 
when compared with the other two PPP-B2b solutions. The 
errors of the PPP-B2bG and the PPP-B2bC are compara-
ble in the east component while the PPP-B2bG shows the 
relatively larger errors in the north and up components. 
When comparing the errors between the different stations, 
it seems that almost all stations show similar variations for 
the PPP-B2bG and the PPP-B2bC, which might be caused 
by the common mode error related to the satellite geometry. 
Table 3 lists the statistical root mean square errors (RMSEs) 
of the different PPP-B2b solutions, where we can find that 
the PPP-B2bGC achieves the highest accuracies, with RMSE 
values of 0.4 cm, 0.3 cm and 0.4 cm for the north, east and 
up components, respectively. These values are superior to 
the RMSE values of the PPP-B2bG and the PPP-B2bC. The 
RMSE values of the PPP-B2bGC are 50%, 40%, and 71% 
and 20%, 50%, and 56% smaller in the north, east and up 
components than those of the PPP-B2bG and PPP-B2bC, 
respectively.
Magnitude inversion with the PPP‑B2b PGD
For the earthquake early warning and the rapid emergency 
responses, the warning magnitude can be determined with 
the GNSS PGD in real time, which is defined as the maxi-
mum value of the coseismic displacements from the origin 
time of the earthquake to the current epoch. At each station, 
we extracted the PGD at every epoch after the seismic wave 
Table 2   Statistical standard 
deviation (STD) values of 
the short-period (5 min) 
displacements for the different 
solutions at all GNSS stations 
(unit: cm)
Solutions
North
East
Up
PPP
0.4
0.3
0.8
PPP-B2bGC
0.5
0.4
1.1
PPP-B2bC
0.6
0.6
1.4
Fig. 3   Coseismic displacements derived from the PPP, PPP-B2bGC, 
PPP-B2bG and the PPP-B2bC at Station QHAG during the 2021 Mw 
7.4 Maduo earthquake
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [1 Figure(s)]

<!-- PAGE: 7 -->

GPS Solutions           (2024) 28:26 	
1 3
Page 7 of 13 
   26 
arrives at the station with an imaginary velocity of 6 km/s. 
This velocity was used because it approximately corresponds 
to the velocity of the P wave. The derived PGD series at each 
station are presented in Fig. 5, where we can find that the 
PGDs of the PPP, PPP-B2bG, PPP-B2bC and PPP-B2bGC 
are comparable at almost all times. Taking the PPP PGDs 
as a reference, the maximum PDG differences for the PPP-
B2bGC, PPP-B2bG and PPP-B2bC are 0.7 cm, 4.5 cm and 
3.9 cm, respectively. It is clear that the PPP-B2bGC has bet-
ter performance than the PPP-B2bG and the PPP-B2bC.
With the derived PGDs, we calculated the warning 
magnitude at each epoch, which is the average value of 
the magnitudes determined with the PGDs at each station 
with the empirical relationship of (12). Figure 6 presents 
the time series of the derived magnitudes of the different 
Fig. 4   Coseismic displacement 
errors of the PPP-B2bG, PPP-
B2bC and the PPP-B2bGC. 
For clarity, the errors of the 
PPP-B2bC and the PPP-B2bGC 
are offset in the vertical axis, 
and the different stations are 
distinguished by the different 
colours
Table 3   Statistical coseismic 
displacement RMSE values of 
the PPP-B2bG, PPP-B2bC and 
PPP-B2bGC (unit: cm)
Solutions
North
East
Up
PPP-B2bG
0.8
0.5
1.4
PPP-B2bC
0.5
0.6
0.9
PPP-B2bGC
0.4
0.3
0.4
Fig. 5   PGDs extracted in real time from the coseismic displacements 
of the PPP, PPP-B2bG, PPP-B2bC and PPP-B2bGC for all GNSS sta-
tions
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [2 Figure(s)]

<!-- PAGE: 8 -->

GPS Solutions           (2024) 28:26 
1 3
   26  
Page 8 of 13
GNSS solutions. Moreover, we determined that there is good 
agreement between the magnitudes of the PPP and the PPP-
B2bGC during the entire duration of the earthquake. For 
the PPP-B2bG and the PPP-B2bC, the derived magnitudes 
are slightly larger than that of the PPP before approximately 
40 s, and these relatively larger differences decrease over 
time. All magnitudes tend to be stable after approximately 
60 s, and the stable magnitudes of the PPP, PPP-B2bG, PPP-
B2bC and PPP-B2bGC are Mw 7.37, Mw 7.38, Mw 7.38 
and Mw 7.38, respectively, which are all close to the final 
magnitude of Mw 7.4.
Centroid moment tensor inversion 
with the real‑time static coseismic offsets derived 
from the coseismic displacements of the PPP‑B2b
Real-time and robust estimation of the centroid moment 
tensor (CMT) is important for assessing the characteristics 
of an earthquake. Here, we inverted the CMT in a simu-
lated real-time mode with the fastCMT method. The real-
time static coseismic offsets are retrieved by averaging the 
coseismic displacements with a 30-s sliding window, and 
the derived real-time static coseismic offsets of the differ-
ent GNSS solutions are presented in Fig. S4-7. Considering 
the relatively high accuracy of the GNSS displacement in 
the horizontal component, the relative weight between the 
horizontal coseismic offsets and the up coseismic offsets is 
set to 3:1. In addition, the stations with epicentre distances 
less than 50 km are extra weighted with a value of two, given 
the better constraint of the near-field stations on the centroid 
depth (Zang et al. 2022). To determine the characteristics of 
the earthquake source, the inverted CMTs are further decom-
posed into a better double couple (DC) component and a 
compensated linear vector dipole component.
The percentage of the DC component and the vari-
ance reduction (VR) that illustrates the misfit between 
the observation and the model prediction are presented 
in Fig. 7, where we can find that the percentages of the 
Fig. 6   Time series of the warning magnitudes determined with differ-
ent GNSS PGDs
Fig. 7   Percentages of the better 
double couple (DC) component 
decomposed from the different 
CMT results and the variance 
reductions (VR) of the different 
CMT solutions
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [2 Figure(s)]

<!-- PAGE: 9 -->

GPS Solutions           (2024) 28:26 	
1 3
Page 9 of 13 
   26 
DC components of all solutions show similar variations 
after approximately 40 s, and all solutions tend to be sta-
ble after approximately 80 s. The average percentages of 
the DC components after 80 s for the PPP, PPP-B2bGC, 
PPP-B2bG, and PPP-B2bC are 92%, 95%, 86% and 88%, 
respectively. These high DC percentages are indicative of 
a good solution for a tectonic earthquake. For the vari-
ance reduction, as shown in Fig. 7, the PPP, PPP-B2bGC 
and PPP-B2bC show good consistency during the whole 
earthquake. For the PPP-B2bG, there are relatively larger 
differences in the VR between it and the other solutions 
before approximately 40 s, and these differences fade away 
gradually after approximately 60 s. The average VRs after 
80 s for the PPP, PPP-B2bGC, PPP-B2bG, and PPP-B2bC 
are 92%, 93%, 91% and 92%, respectively. Both sets of 
results show good fits to the data.
Figure 8 illustrates the focal mechanisms derived from 
the different CMT results. We found that the focal mecha-
nisms derived from the different CMT results are similar 
after approximately 40 s, and it can be basically deter-
mined that this earthquake was a strike-slip event after 
approximately 40 s based on the derived results. Table 4 
compares the nodal planes derived from the focal mecha-
nisms of the different agencies, where the results of the 
PPP-B2bGC, PPP-B2bG and the PPP-B2bC are the aver-
age values of the nodal planes determined after the 80 s. It 
is seen that the two nodal planes of the PPP-B2bGC, PPP-
B2bG and the PPP-B2bC are essentially in good agree-
ments with that of the PPP, and they are all close to the 
result of Zhang and Xu (2021) except the rake in Nodal 
Plane 1 and the dip in Nodal Plane 2.
Fault slip distribution inversion with the real‑time 
static coseismic offsets derived from the coseismic 
displacements of the PPP‑B2b
The fault slip distribution inversions are carried out at each 
epoch when the focal mechanisms are available. We inverted 
the fault slips on both nodal planes, and the plane with the 
largest variance reduction was selected as the fault plane of 
this epoch. In the inversion, the relative weight between the 
horizontal coseismic offsets and the up coseismic offsets 
was also set to 3:1. The fault slip distributions inverted at 
every epoch with the static coseismic offsets of the PPP, 
PPP-B2bGC, PPP-B2bG and PPP-B2bC are presented in 
Move. S1, Move. S2, Move. S3 and Move. S4, respectively. 
Furthermore, we determined that the fault planes deter-
mined with the different GNSS solutions change slightly 
Fig. 8   Focal mechanisms 
derived from the CMT results 
inverted with the different static 
coseismic offsets. For clarity, 
the focal mechanisms are dis-
played with an interval of 10 s
Table 4   Nodal planes derived from the focal mechanisms of the 
global centroid moment tensor project (GCMT), U.S. geological sur-
vey (USGS) and this study
Solutions
Nodal Plane 1 Strike°/
Dip°/Rake°
Nodal Plane 2 
Strike°/Dip°/
Rake°
GCMT
282/83/− 9
13/81/− 173
USGS
99/79/− 38
197/53/− 166
Zhang and Xu (2021)
281/88/1
191/89/178
PPP
278/80/28
183/63/169
PPP-B2bGC
279/80/34
182/56/168
PPP-B2bG
279/82/24
185/66/171
PPP-B2bC
277/83/33
183/58/172
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [1 Figure(s)]

<!-- PAGE: 10 -->

GPS Solutions           (2024) 28:26 
1 3
   26  
Page 10 of 13
Fig. 9   Fault slip distribu-
tions inverted with the static 
coseismic offsets of the PPP, 
PPP-B2bGC, PPP-B2bG, and 
PPP-B2bC at 100 s after the 
earthquake
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [1 Figure(s)]

<!-- PAGE: 11 -->

GPS Solutions           (2024) 28:26 	
1 3
Page 11 of 13 
   26 
after approximately 40 s, and the fault slip distributions 
inverted with the different static coseismic offsets are also 
comparable. Taking the fault slips inverted with the different 
static coseismic offsets at 100 s as an example, we found that 
the fault slip distributions of the PPP-B2bGC, PPP-B2bG 
and PPP-B2bC are all in good agreement with that of the 
PPP (Fig. 9). All inverted results show that this earthquake 
ruptures the ground surface. There are mainly two rupture 
areas in the fault, and most ruptures clustered in the east 
segment of the fault with maximum slips of 3.9 m, 4.0 m, 
3.9 m and 3.8 m for the PPP, PPP-B2bGC, PPP-B2bG and 
PPP-B2bC, respectively. The variance reductions of the four 
fault slip models are 90%, 91%, 89% and 89%, respectively, 
with both sets of results showing good fits to the data. The 
final magnitudes derived from the fault slip models of the 
PPP, PPP-B2bGC and PPP-B2bC are Mw 7.42, Mw 7.43 
and Mw 7.42, respectively. For the PPP-B2bG, the derived 
magnitude is Mw 7.46, which is slightly higher than that of 
the other three models. This is because the static coseismic 
offset accuracy of the PPP-B2bG is slightly worse than those 
of the other solutions and leads to more small slips (Fig. 9c) 
in the western boundary of the fault plane that may not exist.
Conclusions
In this study, we evaluated the performance of the PPP-B2b 
for real-time earthquake source description with GNSS 
observations measured during the 2021 Mw 7.4 Maduo 
earthquake. The results indicate that the PPP-B2b performs 
better during the short term. The STD values of the PPP-
B2bGC displacements during the 5 min are 0.5 cm, 0.4 cm 
and 1.1 cm for the north, east and up components, respec-
tively, which are slightly larger than the STD values of the 
PPP displacements. Taking the coseismic displacements 
of the PPP as a reference, the PPP-B2bGC can be used to 
retrieve real-time coseismic displacements with accuracies 
of 0.4 cm, 0.3 cm and 0.4 cm for the three components, 
respectively, which are superior to those of the PPP-B2bC 
and PPP-B2bG. For the PPP-B2bG, although the accu-
racy of the horizontal coseismic displacement is less than 
1.0 cm, it should be noted that the GPS observations were 
processed with the static mode before the earthquake. In the 
realistic dynamic environment, the PPP-B2bG might show 
poor performance due to the influence of the shortage of the 
PPP-B2b corrections, which might be improved with the 
improvement of the generation strategy of the PPP-B2b cor-
rections in the future. For the earthquake source description, 
we determined that the inverted real-time warning magni-
tudes, focal mechanisms and fault slip distributions of the 
PPP-B2bGC, PPP-B2bC and PPP-B2bG are all very close to 
those of PPP. Thus, we conclude that the PPP-B2b has great 
potential to be used for providing earthquake early warning 
and real-time earthquake source descriptions. However, we 
need to note that we only validated the possibility of the 
PPP-B2b being used for large earthquake source descriptions 
in this study. Whether the PPP-B2b has good performance 
on real-time earthquake source descriptions for middle or 
even small earthquakes needs to be validated further. In 
addition, the PPP-B2b corrections for GPS are incomplete 
and are currently unavailable for Galileo and GLONASS. 
With increasing PPP-B2b corrections, the accuracy and reli-
ability of the inverted real-time earthquake source might be 
further improved.
Supplementary Information  The online version contains supplemen-
tary material available at https://​doi.​org/​10.​1007/​s10291-​023-​01570-x.
Acknowledgements  This work is co-supported by the Qingdao Natu-
ral Science Foundation (23-2-1-70-zyyd-jch), the Shandong Provin-
cial Natural Science Foundation (ZR202211210055), the Fundamen-
tal Research Funds for the Central Universities (22CX06034A) and 
the key project of the National Natural Science Foundation of China 
(42130101). The authors acknowledge the Crustal Movement Obser-
vation Network Of China (CMONOC), the Continuously Operating 
Reference Stations of Qinghai Province in China (CORS) and the 
China Mobile Communications Group Co., Ltd. for providing GNSS 
observations.
Author contributions  JZ performed the data processing and wrote the 
manuscript. SF contributed to the experimental design, analysis and 
proof-read the manuscript. CX provided the advice and guidance for 
the results analysis. ZL contributed to the GNSS data collection and 
processing. RF and YL contributed to the recovery of the precise satel-
lite orbit and clock offsets with the PPP-B2b corrections.
Data availability  The final precise orbit and clock products from the 
Wuhan University can be obtained at ftp://​igs.​gnssw​hu.​cn/​pub/. The 
GNSS observations from the CMONOC, the CORS and the China 
Mobile Communications Group Co., Ltd. can be obtained under 
permission.
Declarations 
Conflict of interest  The authors declare no conflicts of interest.
References
Allen R, Alon Z (2011) Application of real-time GPS to earthquake 
early warning. Geophys Res Lett 38(16):L16310. https://​doi.​org/​
10.​1029/​2011G​L0479​47
Chen K, Avouac J, Geng J, Liang C, Zhang Z, Li Z, Zhang S (2022) 
The 2021 Mw 7.4 Madoi earthquake: an archetype bilateral 
slip-pulse rupture arrested at a splay fault. Geophys Res Lett 
49(2):e2021GL095243. https://​doi.​org/​10.​1029/​2021G​L0952​43
Crowell BW, Melgar D, Bock Y, Haase JS, Geng J (2013) Earthquake 
magnitude scaling using seismogeodetic data. Geophys Res Lett 
40(23):6089–6094. https://​doi.​org/​10.​1002/​2013G​L0583​91
CSNO (2020) BeiDou Navigation Satellite System Signal In: Space 
Interface Control Document Precise Point Positioning Service 
Signal PPP-B2b (Version 1.0)
Fang R, Lv H, Hu Z, Wang G, Zheng J, Zhou R, Xiao K, Li M, Liu J 
(2022) GPS/BDS precise point positioning with B2b products for 
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 12 -->

GPS Solutions           (2024) 28:26 
1 3
   26  
Page 12 of 13
high-rate seismogeodesy: application to the 2021 Mw 7.4 Maduo 
earthquake. Geophys J Int 231(3):2079–2090. https://​doi.​org/​10.​
1093/​gji/​ggac3​11
Ge Y, Cao X, Lyu D, He Z, Ye F, Xiao G, Shen F (2023) An investiga-
tion of PPP time transfer via BDS-3 PPP-B2b service. GPS Solut 
27:61. https://​doi.​org/​10.​1007/​s10291-​023-​01402-y
Geng J, Jiang P, Liu J (2017) Integrating GPS with GLONASS for 
high-rate seismogeodesy. Geophys Res Lett 44(7):3139–3146. 
https://​doi.​org/​10.​1002/​2017G​L0728​08
Geng T, Li Z, Xie X, Liu W, Li Y, Zhao Q (2022) Real-time ocean 
precise point positioning with BDS-3 service signal PPP-B2b. 
Measurement 203:111911. https://​doi.​org/​10.​1016/j.​measu​rement.​
2022.​111911
Goldberg D, Melgar D, Sahakian V, Thomas A, Xu X, Crowell B, Geng 
J (2020) Complex rupture of an immature fault zone: a simulta-
neous kinematic model of the 2019 Ridgecrest CA earthquakes. 
Geophys Res Lett 47:e2019GL086382. https://​doi.​org/​10.​1029/​
2019G​L0863​82
Hadas T, Bosy J (2015) IGS RTS precise orbits and clocks verifica-
tion and quality degradation over time. GPS Solut 19(1):93–105. 
https://​doi.​org/​10.​1007/​s10291-​014-​0369-5
Larson K, Bodin P, Gomberg J (2003) Using 1 Hz GPS data to meas-
ure deformations caused by the Denali fault earthquake. Science 
300(5624):1421–1424. https://​doi.​org/​10.​1126/​scien​ce.​10845​31
Leick A, Rapoport L, Tatarnikov D (2015) GPS satellite surveying. 
Wiley, Hoboken
Li X, Zheng K, Li X, Liu G, Ge M, Wickert J, Schuh H (2019) Real-
time capturing of seismic waveforms using high-rate BDS, GPS 
and GLONASS observations: the 2017 Mw 6.5 Jiuzhaigou earth-
quake in China. GPS Solut 23(1):17. https://​doi.​org/​10.​1007/​
s10291-​018-​0808-9
Melgar D, Bock Y, Crowell BW (2012) Real-time centroid moment 
tensor determination for large earthquakes from local and regional 
displacement records. Geophys J Int 188(2):703–718. https://​doi.​
org/​10.​1111/j.​1365-​246X.​2011.​05297.x
Melgar D, Crowell BW, Geng J, Allen RM, Bock Y, Riquelme S, Hill 
EM, Protti M, Ganas A (2015) Earthquake magnitude calculation 
without saturation from the scaling of peak ground displacement. 
Geophys Res Lett 42(13):5197–5205. https://​doi.​org/​10.​1002/​
2015G​L0642​78
Meng G, Su X, Wu W, Nikolay S, Takahashi H, Ohzono M, Gerasi-
menko M (2019) Crustal deformation of the Northeastern China 
after the 2011 Tohoku, Japan Mw 9.0 earthquake estimated from 
GPS observations: strain heterogeneity and seismicity. Remote 
Sens 11(24):3029. https://​doi.​org/​10.​3390/​rs112​43029
Minson S, Murray JR, Langbein JO, Gomberg JS (2014) Real-time 
inversions for finite fault slip models and rupture geometry based 
on high-rate GPS data. J Geophys Res Solid Earth 119(4):3201–
3231. https://​doi.​org/​10.​1002/​2013J​B0106​22
Miyazaki S, Larson K, Choi K, Hikima K, Koketsu K, Bodin P, Haase 
J, Emore G, Yamagiwa A (2004) Modeling the rupture process of 
the 2003 September 25 Tokachi-Oki (Hokkaido) earthquake using 
1-Hz GPS data. Geophys Res Lett 31:L21603. https://​doi.​org/​10.​
1029/​2004G​L0214​57
Nie Z, Xu X, Wang Z, Du J (2021) Initial assessment of BDS PPP-B2b ser-
vice: precision of orbit and clock corrections, and PPP performance. 
Remote Sens 13(11):2050. https://​doi.​org/​10.​3390/​rs131​12050
Okada Y (1985) Surface deformation due to shear and tensile faults in 
a half-space. Bull Seismol Soc Am 75(4):1135–1154. https://​doi.​
org/​10.​1785/​BSSA0​75004​1135
Pan J, Bai M, Li C, Liu F, Li H, Liu D, Chevalier ML, Wu K, Wang 
P, Lu H, Chen P, Li C (2021) Coseismic surface rupture and 
seismogenic structure of the 2021–05–22 Maduo (Qinghai) Ms 
7.4 earthquake. Acta Geol Sin 95(6):1655–1670. https://​doi.​org/​
10.​19762/j.​cnki.​dizhi​xuebao.​20211​66
Ren Z, Gong H, Peng J, Tang C, Huang X, Sun G (2021) Perfor-
mance assessment of real-time precise point positioning using 
BDS PPP-B2b service signal. Adv Space Res 68(8):3242–3254. 
https://​doi.​org/​10.​1016/j.​asr.​2021.​06.​006
Ren J, Xu X, Zhang G, Wang Q, Zhang Z, Gai H, Kang W (2022) 
Coseismic surface ruptures, slip distribution, and 3D seismo-
genic fault for the 2021 Mw 7.3 Maduo earthquake, central 
Tibetan Plateau, and its tectonic implications. Tectonophysics 
827:229275. https://​doi.​org/​10.​1016/j.​tecto.​2022.​229275
Sun S, Wang M, Liu C, Meng X, Ji R (2023) Long-term performance 
analysis of BDS-3 precise point positioning (PPP-B2b) service. 
GPS Solut 27:69. https://​doi.​org/​10.​1007/​s10291-​023-​01409-5
Tang C, Hu X, Chen J, Liu L, Zhou S, Guo R, Li X, He F, Liu J, Yang 
J (2022) Orbit determination, clock estimation and performance 
evaluation of BDS-3 PPP-B2b service. J Geod 96:60. https://​
doi.​org/​10.​1007/​s00190-​022-​01642-9
Tao J, Liu J, Hu Z, Zhao Q, Chen G, Ju B (2021) Initial assessment of 
the BDS-3 PPP-B2b RTS compared with the CNES RTS. GPS 
Solut 25(4):131. https://​doi.​org/​10.​1007/​s10291-​021-​01168-1
Wang R, Martin F, Roth F (2003) Computation of deformation 
induced by earthquakes in a multi-layered elastic crust: FOR-
TRAN programs EDGRN/EDCMP. Comput Geosci 29(2):195–
207. https://​doi.​org/​10.​1016/​S0098-​3004(02)​00111-5
Wang W, Fang L, Wu J, Tu H, Chen L, Lai G, Zhang L (2021) 
Aftershock sequence relocation of the 2021 Ms7.4 Maduo 
Earthquake. Qinghai China Sci China Earth Sci 64:1371–1380. 
https://​doi.​org/​10.​1007/​s11430-​021-​9803-3
Wells B, Coppersmith K (1994) New empirical relationships among 
magnitude, rupture length, rupture width, rupture area, and 
surface displacement. Bull Seismol Soc Am 84(4):974–1002
Wen Y, Xiao Z, He P, Zang J, Liu Y, Xu C (2021) Source characteris-
tics of the 2020 Mw 7.4 Oaxaca, Mexico, earthquake estimated 
from GPS, InSAR, and teleseismic waveforms. Seismol Res Lett 
92(3):1900–1912. https://​doi.​org/​10.​1785/​02202​00313
Xu P, Shi C, Fang R, Liu J, Niu X, Zhang Q, Yanagidani T (2013) 
High-rate precise point positioning (PPP) to measure seismic 
wave motions: an experimental comparison of GPS PPP with 
inertial measurement units. J Geod 87(4):361–372. https://​doi.​
org/​10.​1007/​s00190-​012-​0606-z
Xu Y, Yang Y, Li J (2021) Performance evaluation of BDS-3 PPP-
B2b precise point positioning service. GPS Solut 25(4):142. 
https://​doi.​org/​10.​1007/​s10291-​021-​01175-2
Xu X, Nie Z, Wang Z, Zhang Y, Dong L (2023) An improved 
BDS-3 PPP-B2b positioning approach by estimating signal in 
space range errors. GPS Solut 27:110. https://​doi.​org/​10.​1007/​
s10291-​023-​01455-z
Yang Y, Liu L, Li J, Yang Y, Zhang T, Mao Y, Sun B, Ren X 
(2021) Featured services and performance of BDS-3. Sci Bull 
66(20):2135–2143. https://​doi.​org/​10.​1016/j.​scib.​2021.​06.​013
Yang Y, Ding Q, Gao W, Li J, Xu Y, Sun B (2022) Principle and 
performance of BDSBAS and PPP-B2b of BDS-3. Satell Navig 
3:5. https://​doi.​org/​10.​1186/​s43020-​022-​00066-2
Yang H, He X, Ferreira V, Ji S, Xu Y, Song S (2023) Assessment 
of precipitable water vapor retrieved from precise point posi-
tioning with PPP-B2b service. Earth Sci Inform 16:315–328. 
https://​doi.​org/​10.​1007/​s12145-​023-​00939-3
Zang J, Xu C, Li X (2020) Scaling earthquake magnitude in real 
time with high-rate GNSS peak ground displacement from vari-
ometric approach. GPS Solut 24:101. https://​doi.​org/​10.​1007/​
s10291-​020-​01013-x
Zang J, Wen Y, Li Z, Xu C, He K, Zhang P, Wen G, Fan S (2022) 
Rapid source models of the 2021 Mw 7.4 Maduo, China, 
earthquake inferred from high-rate BDS3/2, GPS, Galileo and 
GLONASS observations. J Geod 96:58. https://​doi.​org/​10.​1007/​
s00190-​022-​01641-w
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 13 -->

GPS Solutions           (2024) 28:26 	
1 3
Page 13 of 13 
   26 
Zhang Z, Xu L (2021) The centroid moment tensor solution of the 
2021 Mw7.5 Maduo, Qinghai, earthquake. Acta Seismol Sin 
43(3):387–391. https://​doi.​org/​10.​11939/​jass.​20210​079
Zhang W, Lou Y, Song W, Sun W, Zou X, Gong X (2022) Initial assess-
ment of BDS-3 precise point positioning service on GEO B2b 
signal. Adv Space Res 69(1):690–700. https://​doi.​org/​10.​1016/j.​
asr.​2021.​09.​006
Publisher's Note  Springer Nature remains neutral with regard to 
jurisdictional claims in published maps and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds 
exclusive rights to this article under a publishing agreement with the 
author(s) or other rightsholder(s); author self-archiving of the accepted 
manuscript version of this article is solely governed by the terms of 
such publishing agreement and applicable law.
Jianfei Zang   received his Ph.D. 
in Geodesy at Wuhan University. 
The focus of his current research 
lies in the real-time GNSS posi-
tioning and seismology.
Shijie Fan   received his Ph.D. in 
Geodesy at Wuhan University 
and is an associate professor at 
the China University of Petro-
leum (East China). His research 
interests are in the GNSS data 
processing and application.
Caijun Xu   received his Ph.D. in 
Geodesy at Wuhan University 
and is currently a professor at 
School of Geodesy and Geomat-
ics, Wuhan University. His 
research interests are in the 
Geodesy and Seismology.
Zhicai Li   received his Ph.D. in 
Geodesy at Wuhan University 
and is currently a professor at 
China University of Mining and 
Technology-Beijing. His 
research interests are in the 
Geodesy and Seismology.
Rongxin Fang   received his Ph.D. 
in Geodesy from Wuhan Univer-
sity in 2010 and is currently a 
professor at GNSS Research 
Center, Wuhan University. His 
current research interests are in 
the GNSS high-precision posi-
tioning and multi-sensor fusion.
Yidong Lou   received his Ph.D. 
in Geodesy and Surveying Engi-
neering from Wuhan University 
in 2008 and is currently a profes-
sor at GNSS Research Center, 
Wuhan University. His current 
research interests are in the real-
time precise GNSS orbit deter-
mination and real-time GNSS 
PPP.
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [6 Figure(s)]

<!-- PAGE: 14 -->

1.
2.
3.
4.
5.
6.
Terms and Conditions
 
Springer Nature journal content, brought to you courtesy of Springer Nature Customer Service Center GmbH (“Springer Nature”).
 
Springer Nature supports a reasonable amount of sharing of  research papers by authors, subscribers and authorised users (“Users”), for small-
scale personal, non-commercial use provided that all copyright, trade and service marks and other proprietary notices are maintained. By
accessing, sharing, receiving or otherwise using the Springer Nature journal content you agree to these terms of use (“Terms”). For these
purposes, Springer Nature considers academic use (by researchers and students) to be non-commercial.
 
These Terms are supplementary and will apply in addition to any applicable website terms and conditions, a relevant site licence or a personal
subscription. These Terms will prevail over any conflict or ambiguity with regards to the relevant terms, a site licence or a personal subscription
(to the extent of the conflict or ambiguity only). For Creative Commons-licensed articles, the terms of the Creative Commons license used will
apply.
 
We collect and use personal data to provide access to the Springer Nature journal content. We may also use these personal data internally within
ResearchGate and Springer Nature and as agreed share it, in an anonymised way, for purposes of tracking, analysis and reporting. We will not
otherwise disclose your personal data outside the ResearchGate or the Springer Nature group of companies unless we have your permission as
detailed in the Privacy Policy.
 
While Users may use the Springer Nature journal content for small scale, personal non-commercial use, it is important to note that Users may
not:
  
use such content for the purpose of providing other users with access on a regular or large scale basis or as a means to circumvent access
control;
use such content where to do so would be considered a criminal or statutory offence in any jurisdiction, or gives rise to civil liability, or is
otherwise unlawful;
falsely or misleadingly imply or suggest endorsement, approval , sponsorship, or association unless explicitly agreed to by Springer Nature in
writing;
use bots or other automated methods to access the content or redirect messages
override any security feature or exclusionary protocol; or
share the content in order to create substitute for Springer Nature products or services or a systematic database of Springer Nature journal
content.
 
In line with the restriction against commercial use, Springer Nature does not permit the creation of a product or service that creates revenue,
royalties, rent or income from our content or its inclusion as part of a paid for service or for other commercial gain. Springer Nature journal
content cannot be used for inter-library loans and librarians may not upload Springer Nature journal content on a large scale into their, or any
other, institutional repository.
 
These terms of use are reviewed regularly and may be amended at any time. Springer Nature is not obligated to publish any information or
content on this website and may remove it or features or functionality at our sole discretion, at any time with or without notice. Springer Nature
may revoke this licence to you at any time and remove access to any copies of the Springer Nature journal content which have been saved.
 
To the fullest extent permitted by law, Springer Nature makes no warranties, representations or guarantees to Users, either express or implied
with respect to the Springer nature journal content and all parties disclaim and waive any implied warranties or warranties imposed by law,
including merchantability or fitness for any particular purpose.
 
Please note that these rights do not automatically extend to content, data or other material published by Springer Nature that may be licensed
from third parties.
 
If you would like to use or distribute our Springer Nature journal content to a wider audience or on a regular basis or in any other manner not
expressly permitted by these Terms, please contact Springer Nature at
  
onlineservice@springernature.com
