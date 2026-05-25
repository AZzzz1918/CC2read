<!-- PAGE: 1 -->

Remote Sens. 2022, 14, 5835. https://doi.org/10.3390/rs14225835 
www.mdpi.com/journal/remotesensing 
Article 
Evaluation of BDS-3 B1C/B2b Single/Dual-Frequency PPP  
Using PPP-B2b and RTS SSR Products in Both Static and  
Dynamic Applications 
Ruohua Lan, Cheng Yang *, Yanli Zheng, Qiaozhuang Xu, Jie Lv and Zhouzheng Gao 
School of Land Science and Technology, China University of Geosciences Beijing, Beijing 100083, China 
* Correspondence: c.yang@connect.polyu.hk; Tel.: +86-157-1284-7511 
Abstract: The BeiDou Global Navigation Satellite System (BDS-3) can provide PPP-B2b satellite-
based Precise Point Positioning (PPP) real-time service to the Asia–Pacific region via PPP-B2b signal 
transmitted from the three Geostationary Earth Orbit (GEO) satellites. This paper provides a com-
prehensive evaluation of the accuracies of the satellite’s precise real-time orbit and clock products, 
including BDS-3 PPP-B2b precise products and the precise real-time products provided by four IGS 
centers (CAS, DLR, GFZ, and WHU). In addition, the influences of these real-time precise satellite 
products on the PPP positioning accuracy with single-frequency and dual-frequencies are also stud-
ied. Furthermore, the accuracies of broadcast ephemeris and IGS ultra-rapid products are studied, 
as well as their impact on PPP accuracies. Results illustrate that the orbits accuracies of PPP-B2b 
orbits are 9.42 cm, 21.26 cm, and 28.65 cm in the radial, along-track, and cross-track components, 
which are slightly lower than those of real-time orbits provided by the four IGS centers. However, 
the accuracy of PPP-B2b clock biases is 0.18 ns, which is higher than those provided by IGS Real-
Time Service (RTS). In the static positioning test, the 3D positioning accuracy of B1I+B3I dual-fre-
quencies PPP and B1C single-frequency PPP are centimeter-level while using PPP-B2b service, 
which is slightly lower in horizontal components compared to those obtained based on IGS RTS 
products. The results of the dynamic vehicle test indicate that the positioning accuracies of B1I+B2b 
dual-frequency PPP are about 50 cm and 120 cm in horizontal and vertical components, which are 
close to those of B2b single-frequency PPP using PPP-B2b service. Generally, the PPP-B2b orbit and 
clock accuracies on real-time PPP present similar performance to that based on IGS RTS. 
Keywords: PPP-B2b service; BDS-3 new signals; RT-PPP; single-/dual-frequency RT-PPP 
 
1. Introduction 
The 3rd generation of the BeiDou Global Navigation Satellite System (BDS-3) offi-
cially provides services of Positioning, Navigation, and Timing (PNT) to global users as 
of 31 July 2020. The BDS-3 constellation consists of 30 satellites, including 24 Medium 
Earth Orbit (MEO) satellites, 3 Geostationary Earth Orbit (GEO) satellites, and 3 Inclined 
Geosynchronous Satellite Orbit (IGSO) satellites [1–3]. In addition to the standard PNT 
services provided by GPS, Galileo, and GLONASS, BDS-3 is the first system that provides 
short message communication services and Precise Point Positioning (PPP) real-time ser-
vice. Real-Time Kinematic (RTK) and PPP are the most widely applied high-accuracy po-
sitioning techniques. The RTK positioning accuracy, however, declines along with the in-
creasing baseline, and the conventional Real-time PPP (RT-PPP) based on the real-time 
orbit/clock products of the International GNSS Service (IGS) is limited by the internet con-
nection. The RT-PPP service provided by BDS-3 uses the B2b (1207.14 MHz) signal to 
broadcast the orbit and clock corrections directly. 
Citation: Lan, R.; Yang, C.; Zheng, 
Y.; Xu, Q.; Lv, J.; Gao, Z. Evaluation 
of BDS-3 B1C/B2b  
Single/Dual-Frequency PPP Using 
PPP-B2b and RTS SSR Products in 
Both Static and Dynamic  
Applications.  
Remote Sens. 2022, 14, 5835. 
https://doi.org/10.3390/rs14225835 
Academic Editors: Giuseppe Casula, 
Zhetao Zhang and Wenkun Yu 
Received: 18 October 2022 
Accepted: 14 November 2022 
Published: 17 November 2022 
Publisher’s Note: MDPI stays neu-
tral with regard to jurisdictional 
claims in published maps and institu-
tional affiliations. 
 
Copyright: © 2022 by the authors. Li-
censee MDPI, Basel, Switzerland. 
This article is an open access article 
distributed under the terms and con-
ditions of the Creative Commons At-
tribution (CC BY) license (https://cre-
ativecommons.org/licenses/by/4.0/).

> [3 Figure(s)]

<!-- PAGE: 2 -->

Remote Sens. 2022, 14, 5835 
2 of 25 
 
 
The PPP positioning accuracy is highly related to the satellite orbits and clocks accu-
racies, which are mainly obtained from the IGS [4–7]. However, IGS final products are 
generated with a two-week delay, and the IGS fast orbit and clock products are seventeen 
hours delayed. To fulfill the RT-PPP applications, IGS started providing ultra-rapid prod-
ucts on 3 November 2000, with centimeter to decimeter-level accuracy [8–12]. The IGS 
ultra-rapid files involve 24 h of properly arranged orbit and clock ephemerides. The first 
24 h of each IGS ultra-rapid orbit and clock information is estimated from the latest obser-
vations from the IGS hourly tracking network. The second 24 h of data are the predicted 
orbits and clocks, which are extrapolated from the formerly observed orbits. To satisfy the 
growing demand for real-time high-precision applications (such as precision agriculture, 
earthquake warning, and tsunami warning) [13], IGS established a real-time working 
group to provide GPS/GLONASS orbit and clock corrections based on RTCM for the RT-
PPP service [14,15]. Currently, IGS analysis centers (ACs), such as GFZ (Deutsches 
GeoForschungs Zentrum), WHU (Wuhan University), and CAS (Chinese Academic of Sci-
ence), provide real-time orbits and clock products. The types of precise products and re-
lated constellations provided by different IGS centers are presented in Table 1. 
Table 1. The IGS SSR message information and the corresponding interval. 
IGS Center 
Orbit 
Clock 
Code Bias 
Phase Bias 
VTEC 
GNSS 
BKG 
60 s 
5 s 
60 s 
60 s 
- 
G/R/E 
CAS 
5 s 
5 s 
10 s 
- 
60 s 
G/R/E/C 
CNES 
5 s 
5 s 
5 s 
5 s 
60 s 
G/R/E/C 
DLR 
30 s 
5 s 
30 s 
30 s 
- 
G/R/E/C/J 1 
GFZ 
5 s 
5 s 
5 s 
- 
- 
G/R/E/C 
WHU 
5 s 
5 s 
- 
- 
- 
G/R/E/C 
1 G, R, E, C, and J denote GNSS, GOLANSS, Galileo, BDS, and Quasi-Zenith Satellite System (QZSS), 
respectively. 
Scholars have evaluated the accuracies of different IGS ACs’ real-time products and 
their impact on the RT-PPP. Elsobeiey and Al-Harbi [16] analyzed the RT-PPP accuracies 
based on the global IGS stations using the IGS ultra-rapid products and real-time service 
(RTS). The results show that using the RT-PPP based on the IGS RTS can provide 50% 
position improvements compared to ultra-rapid products in terms of the Root Mean 
Square Error (RMSE). Li et al. [17] implemented a network RT-PPP model based on 
RTKLIB software and further evaluated the mode using both static and kinematic GPS 
experiments observations. According to the static positioning results, the horizontal and 
the vertical components achieved centimeter-level accuracy, while the kinematic RT-PPP 
achieved decimeter-level in those components. The quality of GPS/GLONASS/BDS-2/Gal-
ileo quad-system SSR products from eight different IGS analysis centers was evaluated by 
Wang et al. [18]. The study indicated that the RMSE between GPS real-time orbit and final 
precise orbit was centimeter level for all ACs, in which the Standard Deviation (STD) of 
the GPS clock was within 0.3 ns. The GLONASS orbit RMSE was also centimeter level, 
and the clock STD was twice large as that of GPS. The BDS and Galileo orbit accuracies 
from CNES were about 14.54 cm and 4.42 cm, respectively, and the clock accuracies of 
those two constellations were 0.32 ns and 0.18 ns, respectively. The study further studied 
the real-time product accuracy influences on the kinematic PPP with both simulation and 
field tests. The positioning results from the studied IGS ACs were centimeter level in hor-
izontal and vertical components, respectively. The kinematic RT-PPP field test indicates 
that the positioning accuracies estimated by CNES’ real-time products were better than 
those based on CAS precise products. Ouyang et al. [19] studied the performance of BDS-
2 real-time products from four IGS centers, WHU, CNES, DLR, and GFZ. The availabilities 
of all these real-time products were more than 85%, and the real-time orbit accuracies of 
the GEO and IGSO/MEO satellites were meter level and decimeter level, respectively.

<!-- PAGE: 3 -->

Remote Sens. 2022, 14, 5835 
3 of 25 
 
 
Among all of these products, CNES provided the highest accuracy on 3D orbit and clock 
products. In static PPP mode, the convergence time on average was less than 1.5 h with 
11.0 cm positioning accuracy, while in the kinematic mode, the convergence time was 2.11 
h~9.84 h with 30.7 cm~68.0 cm positioning accuracy. Ge et al. [20] evaluated the accuracy 
availability of the BDS-3 real-time products from CENS using continuous data of 41 days. 
The results showed that satellite orbit accuracies were about 6 cm in radial and cross-track 
components but more than 10 cm in the along-track component, and the accuracy of the 
clock was 0.46 ns. The BDS-3 real-time product availability from CENS is over 80%. The 
PPP positioning errors in static were within 3 cm at East (E), North (N), and Up (U) com-
ponents, which was comparable to that of GPS RT-PPP. 
Different from the internet-based RT-PPP service provided by the IGS, BDS-3 broad-
casts the correction of satellite orbit and clock for both BDS-3 and GPS via the PPP-B2b 
signal. Simultaneously, the BDS-3 Differential Code Bias (DCB) is broadcast to facilitate 
dual-frequency PPP positioning applications [3]. Table 2 lists the broadcast PPP-B2b cor-
rection messages [21–23]. 
Table 2. The PPP-B2b message information. 
Information  
Message Type 
Sample Rate (s) 
Nominal Validity (s) 
Satellite mask 
1 
48 
- 
Orbit correction and 
User range accuracy 
2 
48 
96 
Differential code bias 
3 
48 
86,400 
Clock correction 
4 
6 
12 
The performance evaluations of PPP-B2b products have gained interest from re-
searchers recently. Yang et al. [3] presented the positioning accuracy evaluation of dual-
frequency B1C/B2a PPP with Ionosphere-Free (IF) combination based on the PPP-B2b data 
from 1 August to 30 November 2020. The results indicated that about 30 cm and 50 cm 
positioning accuracies in the horizontal and vertical components could be achieved with 
a 30 min convergence time. Lu et al. [21] analyzed the accuracy, integrity, and stability of 
the orbit clock and DCB corrections of both BDS and GPS provided by the BDS-3 PPP-B2b 
signal, which proved that the PPP-B2b signal could provide stable and accurate PPP ser-
vices in China and surrounding areas. Nie et al. [22] compared the orbits and clocks accu-
racies between PPP-B2b corrections and GFZ final products with three days of observa-
tion. The BDS-3 satellite orbit accuracies in radial, along-track, and cross-track compo-
nents are about ten centimeters, and the BDS-3 clock accuracy was centimeter-level. The 
static PPP with PPP-B2b correction messages achieved centimeter-level accuracy in the E, 
N, and U components, and the kinematic PPP of those also achieved centimeter-level ac-
curacy. Tao et al. [23] illustrated that the real-time BDS-3 PPP-B2b correction messages 
presented better availability and integrity than CNES on BDS satellites. The positioning 
accuracy of PPP-B2b products-based BDS-3 kinematic PPP can achieve centimeter-level. 
Xu et al. [24] provided an extensive evaluation of the RT-PPP performance of the PPP-B2b 
products in terms of matching characteristics, product accuracies, and availability. The 
results showed that the RMSE of the MEO satellite orbit in radial, along-track, and cross-
track components were 6.8 cm, 33.4 cm, and 36.6 cm, respectively, and the accuracy of the 
clock was 0.2 ns. The availability of BDS-3 PPP-B2b products is over 80%. The PPP test 
results presented that the accuracies of BDS-3 dual-frequency kinematic RT-PPP after con-
vergence were 11 cm and 17 cm in horizontal and vertical components. In addition, the 
positioning accuracy of the B1C/B2a IF combination PPP was better than that of the 
B1I/B3I IF PPP. Ren et al. [25] evaluated the accuracy of PPP-B2b products and the corre-
sponding RT-PPP, and the results showed that the real-time orbit accuracy is about 7.25, 
24.79, and 25.87 cm in radial, along-track, and cross-track components for BDS-3 satellites, 
and 7.29, 30.98, and 21.93 cm for those of GPS satellites. The STD of the clock offset errors

<!-- PAGE: 4 -->

Remote Sens. 2022, 14, 5835 
4 of 25 
 
 
for BDS-3 and GPS are within 0.2 ns and 0.15 ns, respectively. The positioning accuracy of 
real-time BDS+GPS integrated static PPP was about 1.07 cm, 2.69 cm, and 2.25 cm in the 
N, E, and U directions, and the kinematic PPP of those were about 3.6 cm, 5.9 cm, and 9.4 
cm in the N, E, and U directions. 
Earlier studies evaluated the PPP-B2b performance using the dual-frequency PPP 
with static and simulated kinematic mode. However, the PPP-B2b RT-PPP based on the 
practical kinematic data has hardly been studied, especially using the BDS-3 new signals 
(B1C and B2b). Therefore, this contribution will present a comprehensive performance 
evaluation on the real-time orbit and clock products provided by broadcast ephemeris, 
BDS-3 PPP-B2b, CAS, DLR, GFZ, and WHU, as well as the ultra-rapid products from 
WHU. The performance of the kinematic dual-and single-frequency RT-PPP is analyzed 
with B1C+B2b observation data collected in Beijing, China. The paper is arranged as fol-
lows. The recovery method of real-time orbit and clock offset and the mathematical mod-
els of dual-/single-frequency PPP are described in the next section. Then, the accuracy of 
the orbit and clock offset provided by broadcast ephemeris, PPP-B2b, CAS, DLR, GFZ, 
and WHU are evaluated separately. The positioning accuracy with dual-/single-frequency 
real-time dynamic PPP is afterward assessed, and the conclusions about the accuracy of 
real-time satellite orbit and clock products and their impacts on dual-/single-frequency 
PPP are drawn. 
2. Methodologies 
The recovery methods of PPP-B2b real-time orbit and clock, the evaluation principle, 
and the models of real-time dual-frequency and single-frequency PPP are presented in 
this section. 
2.1. PPP-B2b Orbit Recovery 
BDS-3 PPP-B2b orbit and clock products are corrections with respect to the broadcast 
ephemeris. The orbit correction coordinate is related to the satellite-fixed coordinate sys-
tem in radial, along-track, and cross-track directions. The satellite positions used for PPP, 
however, are located in the ECEF frame. Thus, the orbit corrections should be transformed 
into the ECEF system to correct the satellite positions from the broadcast ephemeris [26]. 
The corrected real-time precise satellite position can be expressed as, 
brdc
r
brdc
a
brdc
c
t
t
t
X
X
Y
Y
Z
Z













=
−




















R
 
(1)
With 




=







r
r
r
r
r
r
R
r
r
r
r
r
r
 
(2)
where 
r
, 
a
 and 
c
 represent the position corrections in the radial, along-track, 
and cross-track directions, respectively; 

T
X
Y
Z
 and 

T
brdc
brdc
brdc
X
Y
Z
rep-
resent the corrected satellite coordinates in the EFEC system and the satellite coordinates 
calculated from the broadcast ephemeris, respectively; R  is the transformation matrix 
from the satellite-fixed coordinate system to the ECEF system [26,27]; r  and r  represent 
the satellite position and velocity calculated from the broadcast ephemeris, respectively.  
It should be indicated that the orbit products provided by IGS ACs in this article are 
with respect to the Center of Mass (CoM) of satellites. In contrast, the orbits of PPP-B2b 
products are with respect to the satellite Antenna Phase Center (APC); the BDS is based 
on the APC of B3I frequency, while GPS is based on the APC of IF combination [26].

> [3 Figure(s)]

<!-- PAGE: 5 -->

Remote Sens. 2022, 14, 5835 
5 of 25 
 
 
Therefore, the antenna phase center correction should be considered. The relationship be-
tween APC and CoM can be described by, 
APC
CoM
PCO
T
APC
CoM
PCO
APC
CoM
PCO
X
X
N
Y
Y
E
Z
Z
U












=
+



















A
 
(3)
where 

T
APC
APC
APC
X
Y
Z
 and 

T
CoM
CoM
CoM
X
Y
Z
 represent the APC and 
CoM satellite position in the EFEC system; 

T
PCO
PCO
PCO
N
E
U
 represent the PCO 
correction of the satellite from the latest “igs14.atx” file released by IGS; A  is the satellite 
attitude matrix.  
2.2. PPP-B2b Clock Recovery 
The clock corrections broadcast by PPP-B2b can be recovered to form the precise 
clock by [26], 
0 /
s
s
brdc
t
t
C
c
=
−
 
(4)
where 
st , 
s
brdc
t
, 
0
C , and c  represent satellite precise clock, satellite clock calculated 
from the broadcast ephemeris, PPP-B2b clock corrections, and the speed of light in a vac-
uum, respectively.  
It should be indicated that the BDS-3 precision clock provided by PPP-B2b is based 
on the B3I frequency, and all RTS clocks are based on the IF combination [26]. Therefore, 
all of these clocks for a GNSS system should be projected to one frequency. According to 
[26], the following method can be adopted to realize such projection, 
s
s
s
j
j
t
t
b
=
−
 
(5)
where 
s
jt  is the satellite precise clock of signal j ; 
s
jb  represents the DCB between sig-
nal j  and B3I. 
2.3. Orbit and Clock Evaluation Methods 
Several methods can be utilized to evaluate the accuracy of precise orbit and clock. 
For example, the overlapping orbit comparison, satellite laser ranging inspection, and 
comparison with a reference product. The first two usually are used to evaluate the final 
products of IGS precise products. Thus, the third method is adopted in this paper by using 
the final products provided by WHU as references. The orbit differences can be expressed 
as, 
RT
WHU
RT
WHU
RT
WHU
t
t
t
X
X
X
Y
Y
Y
Z
Z
Z














=
−



















 
(6)
where t  is the epoch number; 

T
X
Y
Z



, 

T
RT
RT
RT
X
Y
Z
, and 


T
WHU
WHU
WHU
X
Y
Z
 are the orbit differences, real-time orbit, and final orbit vector. 
The clock products from different ACs contain a benchmark inconsistency error. In 
this paper, to eliminate the system inconsistency, the GPS and BDS-3 constellations use 
G01 and C19 as reference satellites for the single difference from other satellites [28]. The 
STD of the clock difference between real-time and the reference clock after a single

<!-- PAGE: 6 -->

Remote Sens. 2022, 14, 5835 
6 of 25 
 
 
difference is estimated. The degree of clock consistency greatly influenced the solution 
accuracy of PPP [29]. The PPP-B2b products are estimated using the real-time observa-
tions collected by the regional tracking stations in China. Thus, the satellites rise or fall 
more frequently compared with using global observations. Furthermore, it is challenging 
to select a stable reference BDS satellite to generate the inter-satellite differences. To assess 
the accuracy of PPP-B2b clock products, we re-edited the inter-satellite difference clock 
using the method proposed by [23]. The expression of this method can be written as, 
1
1
(
)
(
)
M
s
s
s
i
i
RT
WHU
RT
WHU
i
t
t
t
t
t
M
=

=
−
−
−

 
(7)
where 
st

 is the double-difference clock value; 
s
RT
t
 is PPP-B2b real-time clock; 
s
WHU
t
 
is the final precise clock of WHU; M  is the number of available satellites.  
Due to the observation discontinuity of the BDS satellites, the clock values estimated 
in Equation (7) are segmented, which affects the clock STD value. Therefore, the disconti-
nuity is compensated by,  
,
1
s
s
t
t
t t
t
t
D
−

= 
−
 
(8)
With 
,
1
,
1
0
0
,
1
,
1
0
1
1
,
0.1 ns
1
0,
0.1 ns
M
M
i
i
t t
t t
i
i
t t
M
i
t t
i
t
t
M
M
D
t
M
−
−
=
=
−
−
=






= 







 
(9)
where 
,
1
t t
D
−

 is the compensation term to compensate the discontinuity in the double-
difference clock; 
,
1
i
t tt
−

 is the inter-epoch difference clock based on double difference 
clock. 
2.4. Mathematical Model of Real-Time Single-/Dual-Frequency PPP 
The measurements used for RT-PPP are pseudo-range ( P ) and carrier-phase ( L ), 
which can be expressed as [29,30], 
,
,
,
(
)
(
)
s
s
s
s
s
j
r
r
r j
r
r j
j
P j
P
c t
t
I
T
c b
b


=
+
−
+
+
+
−
+
 
(10)
,
,
,
(
)
(
)
s
s
s
s
s
j
r
r
r j
r
j
j
r j
j
L j
L
c t
t
I
T
N
B
B



=
+
−
−
+
−
+
−
+
 
(11)
where 
s
r
 indicates the geometric distance from the satellite s  to the receiver r ; 
rt  and 
st  are the receiver clock and the satellite clock offset, respectively; 
,
s
r j
I
 and 
s
r
T
 are the 
ionospheric delay and tropospheric delay, respectively; 
,r j
b
 and 
s
jb  are the DCB of the 
pseudo-range on receiver and satellite, respectively; 
j and 
j
N  are wavelength and 
ambiguity of carrier-phase; 
,r j
B
 and 
s
j
B  denote the Un-calibrated Phase Delay (UPD) 
on the satellite and receiver, respectively; 
,
P j

 and 
,
L j

 are observing noise of pseudo-
range and carrier-phase, respectively.  
2.4.1. Dual-Frequency PPP 
The dual-frequency ionosphere-free combination pseudo-range and carrier-phase 
are used to form the observations of dual-frequency PPP [31],

<!-- PAGE: 7 -->

Remote Sens. 2022, 14, 5835 
7 of 25 
 
 
2
2
,
2
2
2
2
(
)
j
s
s
s
i
IF
i
j
r
r
r
P IF
i
j
i
j
f
f
P
P
P
c t
t
T
f
f
f
f


=
−
=
+
−
+
+
−
−
 
(12)
2
2
,
2
2
2
2
(
)
j
s
s
s
i
IF
i
j
r
r
IF
IF
r
P IF
i
j
i
j
f
f
L
L
L
c t
t
N
T
f
f
f
f



=
−
=
+
−
−
+
+
−
−
 
(13)
where 
if  is the frequency number; the other symbols have the same means as above. 
In addition, if the observed frequencies in Equations (12) and (13) are different from 
that of precise real-time products, a DCB correction should be applied [32]. In this study, 
both B1I+B3I and B1I+B2b IF combinations are employed for static and kinematic PPP 
solutions, and the following equations should be employed,  
2
1
1 , 3
1
2
2
1
3
2
2
2
1
1 ,
2
1
2
2
2
2
2
1
2
1
2
(
)
s
s
s
B I
B I B I
B I
B I
B I
s
s
s
s
B b
B I
B I B b
B I
B b
B I
B b
B I
B b
f
t
t
b
f
f
f
f
t
t
b
b
f
f
f
f

=
−

−


=
−
−

−
−

 
(14)
where 
1 ,
3
s
B I B I
t
 and 
1 ,
2
s
B I B b
t
 represent satellite precise clocks using the B1I+B3I and 
B1I+B2b IF combinations; 
1
B I
f
, 
2
B b
f
 and 
3
B I
f
 represent the frequencies correspond-
ing to the B1I, B2b, and B3I observations, respectively. 
In this case, the corresponding parameters that should be estimated are position vec-
tor, receiver clock offset, residual of troposphere delay, and IF ambiguity, which can be 
written as, 


T
r
r
r
r
wet
IF
x
y
z
c
t
d




=

x
N
 
(15)
where 
rx

, 
ry

 and 
rz

 indicate the corrected value of the receiver coordinates in 
three directions; 
rt

 and 
wet
d
 indicate the receiver clock offset and the zenith wet trop-
ospheric delay; 
IF
N
 denotes the IF ambiguity vector. 
2.4.2. Single-Frequency Model 
For single-frequency PPP, Equations (10) and (11) form the observation equations. 
Here, the B1C and B2b measurements will be used in this paper. Thus, the satellite DCB 
corrections should be considered,  
1
1
2
2
s
s
s
B C
B C
s
s
s
B b
B b
t
t
b
t
t
b

=
−

=
−

 
(16)
Compared with the IF model, the ionospheric delay of each satellite and the receiver 
DCB cannot be eliminated. Therefore, they are estimated as parameters [33–35]. The cor-
responding state vector can be expressed as, 
T
r
r
r
r
wet
j
r
r
x
y
z
ct
d
b





= 

x
N
I
 
(17)
where 
rb  and 
rI  are the receiver DCB and the ionospheric delay vector. 
Due to the correlations between the ionosphere and receiver DCB, we introduce the 
following pseudo-observations to improve the estimation accuracy of single-frequency 
PPP [33].

<!-- PAGE: 8 -->

Remote Sens. 2022, 14, 5835 
8 of 25 
 
 
,
,
,
2
2
,
40.28
/
,
(0,
)
s
s
s
r j
r j
Ir j
s
r j
j
I
I
I
STEC
f



=
+
 
(18)
where STEC  denotes the vertical electronic content obtained from the GIM model; 
,
2
s
r j
I

 is the variance of the priori ionospheric model errors (
,
s
r j
I

). 
2.4.3. Parameter Modeling and Estimation 
According to the observation functions and state parameters mentioned above, the 
sequential least square algorithm is adopted. The corresponding expressions can be de-
scribed by,  
k
k
k
k
=
−
V
A X
L  
(19)
where 
k
V , 
k
A , 
k
X , and
k
L denote the observation residual vector, the design coeffi-
cient matrix, the state vector, and the observation vector at time k , respectively. 
Target function is, 
,
,
1
,
min
T
T
k
k
k
X k
X k
X k
−
+
=
V PV
V
P
V
 
(20)
where 
,
X k
V
 denotes the difference between the current state vector 
k
X  and its pre-
dicted vector 
k
X ; 
,
1
X k−
P
 denotes the weight matrix of the predicted state vector. The 
equation can be calculated by, 
1
,
1
,
1
(
) (
)
T
T
k
k
k
k
X k
k
k
k
X k
k
−
−
−
=
+
+
X
A P A
P
A P L
P
X
 
(21)
1
1
,
,
1
(
)
T
X k
k
k
k
X k
−
−
−
=
+
P
A P A
P
 
(22)
The corresponding posterior covariance matrix of the state vector 
1
,
1
,
1
,
,
1
,
(
) / (
)
T
T
X k
X k
k
k
k
X k
X k
X k
n
m
−
−
−
−
=
+
−
D
P
V PV
V
P
V
 
(23)
where n  and m  represent the number of satellites obtained at k  and 
1
k − epochs, 
respectively. 
3. Experiments and Discussions 
In this section, we collected four-day data to compare the accuracies of PPP-B2b orbit 
and clock to those of IGS RTS products. The positioning accuracies of PPP-B2b on dual-
frequencies and single-frequency PPP are further studied with static and dynamic tests.  
3.1. Static Data Collection 
The real-time orbit and clock SSR products of PPP-B2b, CAS, DLR, GFZ, and WHU, 
the ultra-rapid products from WHU, and the broadcast ephemeris during the Days of Year 
(DOY) 354–357 in 2021 were collected. The distribution of the stations is illustrated in Fig-
ure 1. The IGS real-time SSR corrections were collected from the internet via the open-
source software BNC Ver2.12.17 [36]. The static data from four MGEX stations (URUM, 
ULAB, WHU2, and JFNG) during DOYs of 354–357 of 2021 were collected.

> [1 Figure(s)]

<!-- PAGE: 9 -->

Remote Sens. 2022, 14, 5835 
9 of 25 
 
 
 
Figure 1. The location of 4 selected MGEX stations. 
In the data analysis phase, (1) all of these orbit and clock products were projected to 
the same coordinate system and time system; (2) static test data were processed daily with 
dual-frequency IF PPP (B1I+B3I and L1+L2) and single-frequency PPP (B1C and L1); (3) 
the corresponding GPS data were also processed as a comparison; (4) the reference coor-
dinates obtained from the MGEX weekly SINEX file. The details of the static data pro-
cessing strategies are listed in Table 3. It is worth noting that the B1C observation is BDS-
3 new signal, which is not used for orbit determination and clock calculation. Thus, the 
corresponding DCB correction should be applied to the observations.  
Table 3. PPP processing strategies of static test. 
Item 
Processing Strategies 
GNSS 
BDS-3 and GPS 
Signal selection of IF PPP 
BDS-3: B1I+B3I 
GPS: L1+L2 
Signal selection of SF PPP 
BDS-3: B1C  
GPS: L1 
Interval 
30 s 
Cutoff angle 
10° 
Weight method 
Elevation angle dependent 
Troposphere 
Estimate the wet component 
Ionospheric 
IF PPP: IF combination 
SF PPP: Estimated 
PCO/PCV 
IGS14.atx 
Ambiguity 
Estimated 
Adjustment 
Sequential least square 
Satellite DCB 
Corrected by DCB products 
Receiver DCB 
IF PPP: IF combination 
SF PPP: Estimated 
The available satellites and PDOP are the two critical indexes for positioning accu-
racy analysis; therefore, the number of visible satellites and the PDOP values for both 
BDS-3 and GPS are presented in Figure 2. The number of available BDS-3 satellites on 
average are 8.4, 8.1, 7.8, and 8.1, with the corresponding PDOP of 2.1, 2.2, 2.9, and 2.3 for 
JFNG, ULAB, URUM, and WUH2 stations. For GPS, the average number of available sat-
ellites are 6.8, 7.1, 6.8, and 6.6, with the corresponding PDOP of 2.5, 2.6, 2.9, and 2.7 for 
JFNG, ULAB, URUM, and WUH2 stations.

> [1 Figure(s)]

<!-- PAGE: 10 -->

Remote Sens. 2022, 14, 5835 
10 of 25 
 
 
 
Figure 2. Number of visible satellites and PDOP values of the four MEGX stations. 
3.2. Assessments of BDS-3 Real-Time Orbits and Clock Products 
To evaluate the accuracies of PPP-B2b BDS-3 real-time orbits and clocks from CAS, 
DLR, GFZ, and WHU, as well as the broadcast ephemeris objectively, this study uses the 
final precision product from WHU as the reference. The B2b corrected GPS orbit and clock 
are also studied as a comparison. The time series of the orbit errors in radial, along-track, 
and cross-track directions, as well as the clock errors, are depicted in Figure 3. The corre-
sponding statistics in terms of RMSE and STD are shown in Figures 4 and 5. In Figure 3, 
the orbit errors of different real-time products of BDS are within 20 cm, 60 cm, and 60 cm 
in radial, along-track, and cross-track directions. The BDS B2b corrected and broadcast 
orbit error in radial and along-track directions are similar to those of other real-time prod-
ucts; in the cross-track direction, however, the fluctuations of B2b-corrected and BDS 
broadcast orbit errors are more significant than those of other real-time products. The B2b 
corrected GPS orbit error is similar to that of the B2b corrected BDS orbit. As plotted in 
Figure 4, the statistic orbit accuracies of the IGSO satellites, C38~C40, are much lower than 
those of MEO satellites, especially while using the SSR corrections from GFZ. Generally, 
the orbit RMSE values of the real-time products from CAS, DLR, GFZ, WHU, and 
WHU_U (ultra-precise products) are within 10 cm in the radial, along-track, and cross-
track components for MEO satellites. The RMSE of BRDC, PPP-B2b for BDS-3, are about 
20 cm in the radial component and 50 cm in the along-track and cross-track components; 
the B2b corrected orbit for GPS has a similar performance as those for BDS in three direc-
tions. According to earlier studies, the higher accuracy in the radial direction is related to 
the high-quality satellite hydrogen and rubidium clocks [37]. In Figure 3, it is noted that 
systematic biases existed among different real-time clock products, especially the B2b cor-
rected BDS and GPS clocks. This systematic clock bias is caused by pseudorange observa-
tion and can be absorbed by ambiguities [24,38]. In Figure 5, The clock STD of the real-
time products from CAS, DLR, GFZ, WHU, and WHU_U are within 0.4 ns for BDS MEO 
satellites. In contrast, the STD of PPP-B2b is within 0.2 ns, and the STD of BRDC is within 
1.0 ns. The STD of the B2b corrected GPS clock is 0.3 ns.

> [1 Figure(s)]

<!-- PAGE: 11 -->

Remote Sens. 2022, 14, 5835 
11 of 25 
 
 
 
Figure 3. Time series of the orbit radial and clock errors of C32 and G20.

> [1 Figure(s)]

<!-- PAGE: 12 -->

Remote Sens. 2022, 14, 5835 
12 of 25 
 
 
 
Figure 4. RMS of real-time orbit errors. 
 
Figure 5. STD of real-time orbit clock errors.

> [2 Figure(s)]

<!-- PAGE: 13 -->

Remote Sens. 2022, 14, 5835 
13 of 25 
 
 
The average accuracies of real-time orbit and clock products are shown in Table 4. 
DLR did not provide SSR corrections for the three IGSO satellites, C38, C39, and C40, 
during this test; thus, the average accuracies of these three satellites are not considered. 
According to Table 4, the BDS-3 orbit accuracy in the radial component is higher than 
those in the along-track and cross-track components. The RMSE of the BDS-3 PPP-B2b 
orbits in the radial, along-track, and cross-track components are 9.42 cm, 21.26 cm, and 
28.65 cm, respectively. The accuracy of BDS-3 PPP-B2b orbits in terms of RMSE is lower 
than that of IGS centers products due to the distribution and number of the monitoring 
stations. Compared to the broadcast orbit, the IGS real-time products provide about 
30.62~54.95% improvements in the radial component, and the improvement provided by 
BDS PPP-B2b is 2.89%. The STD of PPP-B2b clocks is 0.18 ns, which has the highest accu-
racy among these real-time products of BDS-3. The improvements of the BDS-3 real-time 
clock provided by PPP-B2b is 79.87% compared to broadcast ephemeris. For the GPS cor-
rection, the B2b corrected orbit RMSE in radial, along-track, and cross-track directions are 
13.73 cm, 23.83 cm, and 17.96 cm, respectively, and the clock STD is 0.25 ns. For the user 
side, the positioning accuracy is mainly affected by the orbit in radial and the clock. There-
fore, the PPP-B2b SSR products theoretically can provide precise positioning solutions.  
Table 4. The average accuracies of real-time orbit and clock products. 
Products 
Orbit (cm) 
Clock (ns) 
Radial 
Along-Track 
Cross-Track 
CAS 
6.73 
8.82 
5.79 
0.31 
DLR 
4.37 
11.95 
7.08 
0.27 
GFZ 
5.41 
12.40 
7.63 
0.31 
WHU 
5.38 
8.57 
6.41 
0.22 
WHU_U 
5.39 
7.25 
5.54 
0.35 
BRDC 
9.70 
22.21 
25.74 
0.87 
B2b BDS 
9.42 
21.26 
28.65 
0.18 
B2b GPS 
13.73 
23.83 
17.96 
0.25 
3.3. Accuracy and Convergence of RT-PPP in MGEX Stations 
3.3.1. Dual-Frequency PPP 
The time series of the position differences between the B1I+B3I PPP solutions of the 
four MEGX stations and the SINEX solutions on the E, N, and U components are presented 
in Figure 6. The average RMSE of the static PPP at JFNG, ULAB, URAM, and WUH2 sta-
tions is shown in Figure 7. Accordingly, the positioning accuracy of BDS-3 dual-frequency 
PPP based on the PPP-B2b real-time products is within 4.6 cm in the three directions for 
the four stations. In contrast, the GPS dual-frequency PPP with B2b correction is about 5.3 
cm in three directions. The lower accuracy of GPS PPP with B2b corrections is caused by 
the product accuracy of GPS orbits and clocks, which has been studied in the above sec-
tion. Additionally, the positioning accuracy of PPP-B2b-based positioning in the N com-
ponent is higher than in the E component, which is related to the satellite’s observation 
geometry strength of the carrier phase ambiguity. Most BDS-3 satellites have a north-
south ground track and, thus, provide strong observation geometry strength in N direc-
tions and better positioning accuracy. In addition, the fixing ambiguity may improve the 
positioning accuracy in the E components [39], and similar results can be obtained in 
[22,40]. In general, the positioning accuracy of static RT-PPP with PPP-B2b is slightly 
lower than that of IGS real-time products, but higher than that of WHU ultra-rapid prod-
ucts and broadcast ephemeris.

<!-- PAGE: 14 -->

Remote Sens. 2022, 14, 5835 
14 of 25 
 
 
 
Figure 6. Error series of the four-day IF static PPP solution. 
 
Figure 7. The average accuracy of the four-day IF static PPP solution. 
The statistics accuracy in terms of RMSE of static B1I+B3I PPP using different real-
time products is listed in Table 5. The positioning accuracies of BDS-3 PPP with PPP-B2b 
service are 4.8 cm and 5.4 cm in horizontal and 3D components, respectively. While using 
GPS, the positioning accuracy is slightly lower than that of BDS-3, with 5.4 cm and 5.9 cm 
in horizontal and 3D components, respectively. This demonstrates that the PPP-B2b ser-
vice has the capability of providing centimeter-level positioning accuracy for users in 
China and neighboring countries while using the dual-frequency static PPP mode. How-
ever, the accuracy of PPP using PPP-B2B services is still lower than those solutions based 
on IGS real-time products. Among these solutions, the solution based on the products of 
WHU has the highest accuracy in horizontal components with 1.1 cm. In comparison, the 
solution based on the CAS products has the highest accuracy in 3D with 1.9 cm. The solu-
tions based on DLR real-time products present the worst accuracy with 3.5 cm and 3.9 cm

> [2 Figure(s)]

<!-- PAGE: 15 -->

Remote Sens. 2022, 14, 5835 
15 of 25 
 
 
in horizontal and 3D components, respectively. Additionally, the horizontal and 3D posi-
tioning accuracies using WHU ultra-rapid products are 10.5 cm and 12.1 cm, respectively, 
while those based on broadcast ephemeris are 23.9 cm and 27.7 cm. Generally, the B1I+B3I 
BDS-3 PPP based on PPP-B2b SSR corrections can provide users with centimeter-level 
static positioning solutions, which is close to these based on IGS RTS SSR corrections, es-
pecially in horizontal components.  
Table 5. Average dual-frequency PPP positioning accuracy of the four MGEX stations (unit: cm). 
Direction 
CAS 
DLR 
GFZ 
WHU 
WHU_U BRDC B2b BDS B2b GPS 
E 
1.1 
3.3 
2.1 
0.9 
9.4 
20.4 
4.6 
5.3 
N 
0.7 
0.8 
0.6 
0.5 
4.7 
12.3 
1.2 
1.0 
U 
1.4 
1.8 
1.4 
1.8 
6.0 
13.2 
2.4 
2.2 
2D 
1.3 
3.5 
2.2 
1.1 
10.5 
23.9 
4.8 
5.4 
3D 
1.9 
3.9 
2.7 
2.1 
12.1 
27.7 
5.4 
5.9 
Convergence time is another crucial index for PPP evaluation. In this paper, we de-
fine the convergence criteria of static PPP to be that the position accuracies in horizontal 
and vertical are continuously better than 10 cm and 20 cm for at least 10 min. The conver-
gence times of static PPP for each MGEX station are presented in Figure 8. Since it is dif-
ficult to converge while using WHU ultra-rapid product and broadcast ephemeris, we 
only provide the convergence times of PPP using IGS real-time products and PPP-B2b 
products. As shown in Figure 8, the convergence times of BDS-3 PPP based on PPP-B2b 
products are within 15 min. The PPP-B2b-based GPS PPP presents the slowest conver-
gence time, with an average convergence time of 52 min and the longest time of 109 min. 
The reason for the longer convergence time of JFNG may be caused by the inconsistency 
of the satellites' orbit errors, as shown in Figure 4, in which the fluctuations of B2b cor-
rected orbit is more significant than that of B2b corrected BDS.  
 
Figure 8. Convergence time of static dual-frequency PPP using different real-time orbit and clock 
products. 
3.3.2. Single-Frequency PPP 
In this section, a single-frequency PPP model with ionospheric and receiver DCB con-
straints is used. The time series of position differences between the static single-frequency 
PPP and the reference results in the E, N, and U for each station are shown in Figure 9, 
and the corresponding statistics are presented in Figure 10. The positioning accuracy in 
terms of RMSE of BDS B1C PPP with PPP-B2b SSR products is better than 5.5 cm in the E, 
N, and U for each station. While using GPS L1, the PPP accuracy is better than 5.6 cm in 
three components. The positioning accuracy of single-frequency PPP with PPP-B2b is 
comparable to that of IGS real-time RTS products, which have similar performance to the 
dual-frequency PPP. The positioning accuracy of static single-frequency PPP using WHU 
ultra-rapid product and broadcast ephemeris is much lower than that with PPP-B2b. The

> [1 Figure(s)]

<!-- PAGE: 16 -->

Remote Sens. 2022, 14, 5835 
16 of 25 
 
 
maximum positioning error for broadcast ephemeris-based solution exceeds 39.5 cm in 
the three components.  
 
Figure 9. Time series of position errors of the four-day single-frequency static PPP. 
 
Figure 10. Average accuracy of the four-day single-frequency static PPP. 
According to the statistics of average positioning error in Table 6, single-frequency 
RT-PPP based on PPP-B2b SSR products and IGS RTS SSR products (except DLR) can 
satisfy the demand for centimeter-level high-precision real-time positioning accuracy. 
While using PPP-B2b SSR products, the position accuracies in horizontal and 3D of B1C 
PPP are 5.4 cm and 7.7 cm, respectively. While using the IGS RTS products, the B1C PPP 
based on WHU products provides the highest accuracy within 3.5 cm in horizontal, and 
the PPP based on GFZ products provides the highest accuracy in 3D with 7.0 cm among 
evaluated the IGS RTS products. In contrast, the DLR real-time products provide the worst 
static B1C PPP positioning accuracy with 5.5 cm and 14.3 cm in the horizontal and 3D. The

> [2 Figure(s)]

<!-- PAGE: 17 -->

Remote Sens. 2022, 14, 5835 
17 of 25 
 
 
horizontal/3D positioning accuracies using WHU ultra-rapid products and broadcast 
ephemeris were about 7.6/13.1 cm and 18.3/43.5 cm, respectively, much lower than those 
of PPP-B2b PPP. As a comparison, the positioning accuracies of GPS L1 PPP based on PPP 
B2b SSR products are 5.4 cm and 7.8 cm, similar to those of BDS-3 B1C PPP.  
Table 6. The average positioning accuracy at the four stations (unit: cm). 
Direction 
CAS 
DLR 
GFZ 
WHU 
WHU_U BRDC B2b BDS B2b GPS 
E 
3.0 
5.2 
3.7 
2.9 
5.8 
15.5 
4.6 
4.6 
N 
2.0 
1.8 
1.6 
2.0 
4.9 
9.7 
2.8 
2.9 
U 
9.1 
13.2 
5.7 
7.0 
10.7 
39.5 
5.5 
5.6 
2D 
3.6 
5.5 
4.0 
3.5 
7.6 
18.3 
5.4 
5.4 
3D 
9.8 
14.3 
7.0 
7.8 
13.1 
43.5 
7.7 
7.8 
To present the convergence speed of single-frequency B1C PPP, we redefine the con-
vergence criteria of static PPP to be that the position accuracies in horizontal and vertical 
are continuously better than 20 cm and 40 cm for at least 10 min. The convergence times 
of static single-frequency PPP based on different SSR products for each MGEX station are 
shown in Figure 11, in which the average convergence times of BDS-3 B1C PPP and GPS 
L1 PPP using PPP-B2b SSR products are 80 min and 73 min, respectively. For solutions 
based on the four IGS real-time products, the converge times with CAS’s products are the 
shortest among other products, with an average time of 65 min. The DLR products-based 
solutions converge the slowest with an average time of 95 min.  
 
Figure 11. Convergence time of single-frequency PPP using different SSR products. 
3.4. Accuracy of Real-Time Vehicle-Borne PPP 
The dynamic test is carried out on DOY 357 in 2021 from 06:00 to 08:30 on the fifth 
ring road with Inertial Navigation System (INS) (NovAtel SPAN EPSON G370) and No-
vAtel GNSS receiver, which receives the B1I and B2b signal from BDS-3, and L1 and L2 
signal from GPS. To study the PPP-B2b performance in complex environments, especially 
the performance of new signal B2b, we equipped a GNSS jammer to interfere with the 
received GNSS signals. The jammer reduces the number of visible satellites rather than 
affecting the observed distances. In the dynamic test, the vehicle drove about 40 km in the 
north–south direction and 30 km in the east–west direction. The tight integration of 
GPS+BDS RTK and INS provided by Inertial Explorer software were used as reference 
values for the dynamic test, and the corresponding trajectory is presented in Figure 12.

> [1 Figure(s)]

<!-- PAGE: 18 -->

Remote Sens. 2022, 14, 5835 
18 of 25 
 
 
 
Figure 12. The trajectory of vehicle dynamic test. 
The positioning strategies are listed in Table 7. It should be noted that the satellite 
DCB products from both real-time SSR and IGS final products do not contain the satellite 
DCB value of C7D (B2b). Therefore, the DCB value of C7Z from CAS’ was used to weaken 
the influence of satellite DCB on B2b frequency with ignoring the intra-frequency error. 
The number of visible satellites and corresponding PDOP values are presented in Figure 
13. The average number of visible BDS-3 and GPS satellites during the 4-h dynamic test 
in Beijing are 8.9 and 2.0, respectively, and the average corresponding PDOP value of BDS-
3 and GPS are 6.3 and 2.4, respectively. The sharp changes in the number of visible satel-
lites are affected by the equipped GNSS jammer and further affect the PDOP values.  
Table 7. PPP processing strategies of dynamic test. 
Item 
Processing Strategies 
GNSS 
BDS-3 and GPS 
Signal selection of IF PPP 
B1I+B2b 
GPS: L1+L2 
Signal selection of SF PPP 
BDS-3: B2b  
GPS: L1 
Interval 
1 s 
Cutoff angle 
10° 
Weight method 
Elevation angle dependent 
Troposphere 
Estimate the wet component 
Ionospheric 
IF PPP: IF combination 
SF PPP: Estimated 
PCO/PCV 
IGS14.atx 
Ambiguity 
Estimated 
Adjustment 
Sequential least square 
Satellite DCB 
Corrected by DCB products 
Receiver DCB 
IF PPP: IF combination 
SF PPP: Estimated

> [1 Figure(s)]

<!-- PAGE: 19 -->

Remote Sens. 2022, 14, 5835 
19 of 25 
 
 
 
Figure 13. Number of visible satellites and PDOP values during the dynamic test. 
Figure 14 presents the time series of position errors of vehicle-borne dual-frequencies 
(B1i+B2b and L1+L2) PPP, single frequency PPP (L1 and B2b) by comparing with the 
RTK/INS tight integration solutions in E, N, and U components. It is noted that the large 
fluctuations in the three components occur in dual-frequencies and single frequencies 
PPP, especially in the U components. Comparing to the visible satellite number presented 
in Figure 13, the presence of significant error components coincided with epochs of poor 
observations, which results in positioning discontinuity and further leads to PPP re-con-
vergence. We chose dual-frequency PPP during epochs 3587 to 3588, red box in Figure 14, 
to further analyze the effect of GNSS signal blockage. At the period of epochs 3587 and 
3588, the visible satellite is 0, and the BDS cannot provide continuous positioning results. 
At epoch 3589, the number of visible satellites is 8, and the positioning error at E, N, and 
U components are 4 m, −2 m, and −4 m, respectively. The average visible satellite number 
during epochs 3589 and 3900 is 8.9, and the B1I+B2b combination PPP with PPP-B2b con-
verged to 0.5 and 1.0 m positioning accuracy in both horizontal and vertical components. 
The convergence time is 85 s in this period, and the average PDOP value is 2.2. The error 
components of single frequency PPP, L1 and B2b, present similar statuses.

> [1 Figure(s)]

<!-- PAGE: 20 -->

Remote Sens. 2022, 14, 5835 
20 of 25 
 
 
Figure 14. Time series of position errors of the dual-(a)/single (b)-frequency vehicle-borne RT-PPP 
using different SSR products.

> [2 Figure(s)]

<!-- PAGE: 21 -->

Remote Sens. 2022, 14, 5835 
21 of 25 
 
 
The accuracies in terms of RMSE of vehicle-borne dual-frequency PPP and single-
frequency PPP based on different SSR products are shown in Tables 8 and 9. For the dual-
frequency PPP, the positioning accuracy of the BDS-3 B1I+B2b PPP using PPP-B2b SSR 
products is 35.8 cm, 55.0 cm, and 121.3 cm in the E, N, and U components, respectively. In 
contrast, the B1I+B2b PPP positioning accuracy using CAS products is the highest in hor-
izontal with 58.9 cm, and WHU products are the highest in 3D with 129.7 cm. The solu-
tions based on broadcast ephemeris (67.5 cm and 182.4 cm in horizontal and 3D compo-
nents) have the worst positioning accuracy among the seven products. The GPS L1+L2 
PPP is 57.0 cm, 47.9 cm, and 101.4 cm in the E, N, and U components. The GPS L1+L2 PPP 
solution has the highest 3D accuracy (126.0 cm) and the worst horizontal accuracy (74.5 
cm) compared to the BDS-3 B1I+B2b PPP using the SSR product of both PPP-B2b and IGS 
RTS.  
For the single-frequency PPP, the positioning accuracy of B2b frequency PPP based 
on PPP-B2b products in E, N, and U components are 87.1 cm, 32.9 cm, and 103.5 cm, re-
spectively; those positioning accuracies of GPS L1 PPP are 42.3 cm, 47.8 cm, and 63.9 cm, 
respectively. While using GPS, the positioning accuracy is slightly higher in horizontal 
components (42.3 cm and 47.8 cm) but much worse in the U direction (129.2 cm). For the 
solutions based on IGS RTS real-time products, the positioning accuracy using GFZ real-
time products is the best, with 75.9 cm and 96.8 cm in horizontal and 3D components, 
respectively. The positioning accuracy with WHU real-time products is 175.7 cm and 250.5 
cm in horizontal and 3D components, respectively, which are the worst among other real-
time products. In Figure 14, a noticeable systematic error exists in the N and U compo-
nents, which are caused by the unabsorbed satellite clock errors. Compared to BDS-3 
B1I+B2b PPP, the BDS-3 B2b PPP provides smoother position solutions, especially after 
satellites signal re-tracking, which is caused by the greater noise of the dual-frequency IF 
and high-accuracy of prior ionosphere data used in single-frequency PPP.  
Table 8. Position RMSE of vehicle-borne real-time dual-frequency PPP using different SSR products 
(unit: cm). 
Direction 
CAS 
DLR 
GFZ 
WHU 
WHU_U BRDC B2b BDS B2b GPS 
E 
27.8 
33.0 
35.4 
34.9 
35.5 
49.2 
35.8 
57.0 
N 
61.9 
51.8 
53.9 
62.1 
49.7 
46.1 
55.0 
47.9 
U 
115.7 
139.4 
138.2 
108.4 
125.5 
169.4 
121.3 
101.4 
2D 
58.9 
61.4 
64.5 
71.2 
61.1 
67.5 
65.7 
74.5 
3D 
129.9 
152.3 
152.5 
129.7 
139.5 
182.4 
137.9 
126.0 
Table 9. Position RMSE of vehicle-borne real-time single-frequency PPP using different SSR prod-
ucts (unit: cm). 
Direction 
CAS 
DLR 
GFZ 
WHU 
WHU_U BRDC B2b BDS B2b GPS 
E 
80.0 
88.6 
54.3 
79.4 
73.9 
111.8 
87.1 
42.3 
N 
53.9 
72.0 
53.1 
156.7 
57.3 
72.7 
32.9 
47.8 
U 
88.6 
87.8 
60.0 
178.6 
57.3 
126.3 
103.5 
129.2 
2D 
96.5 
114.2 
75.9 
175.7 
93.5 
133.4 
93.1 
63.9 
3D 
131.0 
144.0 
96.8 
250.5 
109.6 
183.7 
139.2 
144.1 
Figure 15 shows the radial, along-track, and cross-track RMS values of the orbit’s 
errors and clock STD values for each type of real-time product, as well as the positioning 
accuracy of static and dynamic with single/dual-frequency PPP. In static PPP, the IGS real-
time product positioning accuracy is better than that of PPP-B2b, and BRDC positioning 
accuracy is the worst among the seven products. This is consistent with the orbit and clock 
accuracies of each real-time product. In dynamic PPP, affected by the complex positioning 
environment, the positioning accuracy of various products is similar.

<!-- PAGE: 22 -->

Remote Sens. 2022, 14, 5835 
22 of 25 
 
 
 
Figure 15. The average accuracy of positioning and real-time products. 
It also can be found from Figure 15 that the accuracies of the real-time WHU orbits 
and clock products are similar to other ACs, but the positioning of single frequency PPP 
with WHU products is lower than that of other ACs. This is because the WHU BDS real-
time clock products contain systematic errors. The RMSE of different BDS real-time clock 
products with respect to the WHU final clock product is presented in Figure 16. It can be 
clearly found that the RMSE value of WHU BDS real-time products is more significant 
than that of other products. 
  
Figure 16. The RMSE of real-time orbit clock errors.

> [2 Figure(s)]

<!-- PAGE: 23 -->

Remote Sens. 2022, 14, 5835 
23 of 25 
 
 
4. Conclusions 
Real-time orbits and clocks are crucial factors for RT-PPP applications. To evaluate 
the impacts of existing real-time orbit and clock products (BDS-3 PPP-Bb and IGS RTS), 
this study provides comprehensive assessments of the accuracy of these real-time prod-
ucts and their influences on the positioning accuracy and convergence time of RT-PPP in 
both static and dynamic tests. After the descriptions of the evaluation methods for real-
time orbits and clocks as well as the real-time single-/dual-frequency PPP models, BDS-3 
new signals observations of B1C and B2b from the four MEGX stations and a set of the 
vehicle-borne test were used to find the conclusions of the assessment. The main conclu-
sions can be summarized as follows.  
For these real-time SSR products, the orbit accuracy of PPP-B2b SSR products is lower 
than these of IGS real-time products (CAS, DLR, GFZ, and WHU). However, the clock 
accuracy of PPP-B2b is better than these of IGS real-time products. Additionally, the ac-
curacy of the real-time orbit and clock of BDS-3 provided by PPP-B2b is higher than that 
of GPS.  
For real-time dual-frequency PPP, the position RMSEs of the four MEGX stations 
based on PPP-B2b SSR products are slightly lower than those based on the IGS RTS SSR 
products. Meanwhile, the BDS-3 B1I+B3I PPP positioning accuracy using the PPP-B2b ser-
vice is centimeter-level which is better than that of GPS L1+L2 PPP. The dual-frequency 
B1I+B2b PPP positioning accuracy in the vehicle-borne test achieved submeter-level and 
meter-level in horizontal and vertical components in our test environment. 
For the single-frequency RT-PPP based on PPP-B2b SSR products, the BDS-3 B1C PPP 
is lower than that of B1I+B3I PPP, providing about 10–20 cm-level positioning accuracy 
with MEGX data. While using the vehicle-borne B2b frequency data, the accuracy of BDS-
3 PPP is very close to that of B1I+B2b PPP with submeter-level and meter-level in horizon-
tal and vertical components. 
In general, our work shows that both the BDS-3 PPP-B2b service and the IGS RTS can 
satisfy the demand for high-accuracy positioning in real time. However, these real-time 
products provided by IGS RTS are calculated from the global-distributed stations, which 
are more accurate than BDS-3 PPP-B2b, especially for GPS. However, IGS RTS are limited 
by the connection of the internet. Additionally, BDS-3 PPP-B2b introduces inter-satellite 
link technology and broadcasts SSR information by navigation signal, which gives it more 
significant potential in real-time precise positioning applications in the future. 
Author Contributions: Conceptualization, C.Y., Y.Z. and Z.G.; Data curation, Q.X.; Funding acqui-
sition, C.Y. and Z.G.; Investigation, R.L., C.Y. and Z.G.; Software, R.L.; Supervision, C.Y. and Z.G.; 
Visualization, R.L., Q.X. and J.L.; Writing—original draft, R.L.; Writing—review and editing, R.L., 
C.Y., Y.Z. and Z.G. All authors have read and agreed to the published version of the manuscript. 
Funding: This research was partly supported by the National Key Research and Development Pro-
gram of China (Grant No. 2020YFB0505802), the National Natural Science Foundation of China 
(NSFC) (Grants No. 42274022, No. 42274024). 
Data Availability Statement: The datasets analyzed in this study are managed by the School of 
Land Science and Geomatics, China University of Geosciences, Beijing, and can be available on re-
quest from the corresponding author. 
Acknowledgments: Thanks to the original observations provided by MGEX and the multi-system 
SSR products provided by the analysis centers CAS, DLR, GFZ, and WHU.  
Conflicts of Interest: The authors declare no conflict of interest. 
References 
1. 
Yang, Y.; Gao, W.; Guo, S.; Mao, Y.; Yang, Y. Introduction to BeiDou-3 navigation satellite system. Navigation 2019, 66, 7–18. 
2. 
Yang, Y. Resilient PNT concept frame. Acta Geod. Cartogr. Sin. 2018, 47, 893. 
3. 
Yang, Y.; Mao, Y.; Sun, B. Basic performance and future developments of BeiDou global navigation satellite system. Satell. Navig. 
2020, 1, 1.

<!-- PAGE: 24 -->

Remote Sens. 2022, 14, 5835 
24 of 25 
 
 
4. 
Zumberge, J.; Heflin, M.; Jefferson, D.; Watkins, M.; Webb, F. Precise point positioning for the efficient and robust analysis of 
GPS data from large networks. J. Geophys. Res. Solid Earth 1997, 102, 5005–5017. 
5. 
Kouba, J.; Héroux, P. Precise point positioning using IGS orbit and clock products. GPS Solut. 2001, 5, 12–28. 
6. 
Gao, Y.; Shen, X. A New Method for Carrier-Phase-Based Precise Point Positioning. Navigation 2002, 49, 109–116. 
7. 
Abdel-Salam, M.A.-T. Precise Point Positioning using Un-Differenced Code and Carrier Phase Observations; University of Calgary: 
Calgary, 
AB, 
Canada, 
2005; 
Volume 
69. 
Available 
online: 
https://www.collectionscanada.gc.ca/obj/thesescan-
ada/vol2/002/NR37676.PDF?is_thesis=1&oclc_number=302053384 (accessed on 17 October 2022). 
8. 
Dow, J.M.; Neilan, R.E.; Rizos, C. The international GNSS service in a changing landscape of global navigation satellite systems. 
J. Geod. 2009, 83, 191–198. 
9. 
Ogutcu, S. Performance assessment of IGS combined/JPL individual rapid and ultra-rapid products: Consideration of Precise 
Point Positioning technique. Int. J. Eng. Geosci. 2020, 5, 1–14. 
10. 
Chu, C.-W.; Chiang, Y.-T.; Chang, F.-R.; Wang, H.-S. Toward real-time precise point positioning: Differential GPS based on IGS 
ultra rapid product. In Proceedings of the Proceedings of SICE Annual Conference, Taipei, Taiwan, 18–21 August 2010; pp. 355–
358. 
11. 
Chen, J.; Li, H.; Wu, B.; Zhang, Y.; Wang, J.; Hu, C. Performance of real-time precise point positioning. Mar. Geod. 2013, 36, 98–
108. 
12. 
Duan, B.; Hugentobler, U.; Chen, J.; Selmke, I.; Wang, J. Prediction versus real-time orbit determination for GNSS satellites. GPS 
Solut. 2019, 23, 39. 
13. 
Pan, L.; Gao, X.; Hu, J.; Ma, F.; Zhang, Z.; Wu, W. Performance assessment of real-time multi-GNSS integrated PPP with un-
combined and ionospheric-free combined observables. Adv. Space Res. 2021, 67, 234–252. 
14. 
Caissy, M.; Agrotis, L.; Weber, G.; Fisher, S. The IGS real-time service. In Proceedings of the EGU General Assembly Conference 
Abstracts, Vienna, Austria, 7–12 April 2013; pp. EGU2013–11168. 
15. 
Weber, G.; Mervart, L.; Lukes, Z.; Rocken, C.; Dousa, J. Real-time clock and orbit corrections for improved point positioning via 
NTRIP. In Proceedings of the 20th international technical meeting of the satellite division of the institute of navigation (ION 
GNSS 2007), Fort Worth, TX, USA, 25–28 September 2007; pp. 1992–1998. 
16. 
Elsobeiey, M.; Al-Harbi, S. Performance of real-time Precise Point Positioning using IGS real-time service. GPS Solut. 2016, 20, 
565–571. 
17. 
Li, Z.; Zhang, J.; Li, T.; He, X.; Wu, M. Analysis of static and dynamic real-time precise point positioning and precision based 
on SSR correction. In Proceedings of the 2016 IEEE International Conference on Information and Automation (ICIA), Ningbo, 
China, 1–3 August 2016; pp. 2022–2027. 
18. 
Wang, Z.; Li, Z.; Wang, L.; Wang, X.; Yuan, H. Assessment of multiple GNSS real-time SSR products from different analysis 
centers. ISPRS Int. J. Geo-Inf. 2018, 7, 85. 
19. 
Ouyang, C.; Shi, J.; Huang, Y.; Guo, J.; Xu, C. Evaluation of BDS-2 real-time orbit and clock corrections from four IGS analysis 
centers. Measurement 2021, 168, 108441. 
20. 
Ge, Y.; Chen, S.; Wu, T.; Fan, C.; Qin, W.; Zhou, F.; Yang, X. An analysis of BDS-3 real-time PPP: Time transfer, positioning, and 
tropospheric delay retrieval. Measurement 2021, 172, 108871. 
21. 
Lu, X.; Chen, L.; Shen, N.; Wang, L.; Jiao, Z.; Chen, R. Decoding PPP corrections from BDS B2b signals using a software-defined 
receiver: An initial performance evaluation. IEEE Sens. J. 2020, 21, 7871–7883. 
22. 
Nie, Z.; Xu, X.; Wang, Z.; Du, J. Initial assessment of BDS PPP-B2b service: Precision of orbit and clock corrections, and PPP 
performance. Remote Sens. 2021, 13, 2050. 
23. 
Tao, J.; Liu, J.; Hu, Z.; Zhao, Q.; Chen, G.; Ju, B. Initial Assessment of the BDS-3 PPP-B2b RTS compared with the CNES RTS. 
GPS Solut. 2021, 25, 131. 
24. 
Xu, Y.; Yang, Y.; Li, J. Performance evaluation of BDS-3 PPP-B2b precise point positioning service. GPS Solut. 2021, 25, 142. 
25. 
Ren, Z.; Gong, H.; Peng, J.; Tang, C.; Huang, X.; Sun, G. Performance assessment of real-time precise point positioning using 
BDS PPP-B2b service signal. Adv. Space Res. 2021, 68, 3242–3254. 
26. 
BeiDou Navigation Satellite System Signal in Space Interface Control Document: Precise Point Positioning Service Signal PPP-
B2b (Version 1.0). 2020. Available online: http://en.beidou.gov.cn/SYSTEMS/ICD/202008/P020200803538771492778.pdf (ac-
cessed on 20 October 2021). 
27. 
Hadas, T.; Bosy, J. IGS RTS precise orbits and clocks verification and quality degradation over time. GPS Solut. 2015, 19, 93–105. 
28. 
Ge, M.; Chen, J.; Douša, J.; Gendt, G.; Wickert, J. A computationally efficient approach for estimating high-rate satellite clock 
corrections in realtime. GPS Solut. 2012, 16, 9–17. 
29. 
Li, X.; Ge, M.; Dai, X.; Ren, X.; Fritsche, M.; Wickert, J.; Schuh, H. Accuracy and reliability of multi-GNSS real-time precise 
positioning: GPS, GLONASS, BeiDou, and Galileo. J. Geod. 2015, 89, 607–635. 
30. 
Gao, Z.; Zhang, H.; Ge, M.; Niu, X.; Shen, W.; Wickert, J.; Schuh, H. Tightly coupled integration of multi-GNSS PPP and MEMS 
inertial measurement unit data. GPS Solut. 2017, 21, 377–391. 
31. 
An, X.; Meng, X.; Jiang, W. Multi-constellation GNSS precise point positioning with multi-frequency raw observations and dual-
frequency observations of ionospheric-free linear combination. Satell. Navig. 2020, 1, 7. 
32. 
Guo, F.; Zhang, X.; Wang, J. Timing group delay and differential code bias corrections for BeiDou positioning. J. Geod. 2015, 89, 
427–445.

<!-- PAGE: 25 -->

Remote Sens. 2022, 14, 5835 
25 of 25 
 
 
33. 
Gao, Z.; Ge, M.; Shen, W.; Zhang, H.; Niu, X. Ionospheric and receiver DCB-constrained multi-GNSS single-frequency PPP 
integrated with MEMS inertial measurements. J. Geod. 2017, 91, 1351–1366. 
34. 
Jin, S.; Su, K. PPP models and performances from single-to quad-frequency BDS observations. Satell. Navig. 2020, 1, 16. 
35. 
Zhang, B.; Zhao, C.; Odolinski, R.; Liu, T. Functional model modification of precise point positioning considering the time-
varying code biases of a receiver. Satell. Navig. 2021, 2, 11. 
36. 
Weber, G.; Mervart, L.; Stuerze, A.; Rülke, A.; Stöcker, D. BKG Ntrip Client (BNC), Version 2.12; Mitteilungen des Bundesamtes 
für Kartographie und Geodäsie: Frankfurt am Main, Germany, 2016. 
37. 
Kazmierski, K.; Zajdel, R.; Sośnica, K. Evolution of orbit and clock quality for real-time multi-GNSS solutions. GPS Solut. 2020, 
24, 111. 
38. 
Lv, Y.; Geng, T.; Zhao, Q.; Xie, X.; Zhou, R. Initial assessment of BDS-3 preliminary system signal-in-space range error. GPS 
Solut. 2019, 24, 16. 
39. 
Blewitt, G. Carrier phase ambiguity resolution for the Global Positioning System applied to geodetic baselines up to 2000 km. 
J. Geophys. Res. Solid Earth 1989, 94, 10187–10203. 
40. 
Liu, Y.; Yang, C.; Zhang, M. Comprehensive Analyses of PPP-B2b Performance in China and Surrounding Areas. Remote Sens. 
2022, 14, 643. https://doi.org/10.3390/rs14030643.
