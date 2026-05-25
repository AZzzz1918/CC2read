<!-- PAGE: 1 -->

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/359227326
Principle and performance of BDSBAS and PPP-B2b of BDS-3
Article  in  Satellite Navigation · December 2022
DOI: 10.1186/s43020-022-00066-2
CITATIONS
52
READS
478
6 authors, including:
Yuanxi Yang
State Key Laboratory of Geo-Information Engineering, Xi’an 710054, China
241 PUBLICATIONS   7,216 CITATIONS   
SEE PROFILE
Yangyin Xu
10 PUBLICATIONS   352 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Yuanxi Yang on 17 March 2022.
The user has requested enhancement of the downloaded file.

> [2 Figure(s)]

<!-- PAGE: 2 -->

Yang et al. Satellite Navigation             (2022) 3:5  
https://doi.org/10.1186/s43020-022-00066-2
ORIGINAL ARTICLE
Principle and performance of BDSBAS 
and PPP‑B2b of BDS‑3
Yuanxi Yang1,2*  , Qun Ding3, Weiguang Gao4, Jinlong Li5, Yangyin Xu1,2 and Bijiao Sun1,2 
Abstract 
Within the framework of differential augmentation, this paper introduces the basic technical framework and per-
formance of the BeiDou Global Navigation Satellite System (BDS-3) Satellite-Based Augmentation System (BDSBAS), 
including orbit products, satellite clock offset products, ionosphere and its integrity performance. The basic principle 
of BDS-3 Precise Point Positioning (PPP-B2b) is expounded, the similarities and differences between the PPP service 
provided by BDS-3 and International Global Navigation Satellite System (GNSS) Service (IGS) are discussed, and the 
limitations of PPP-B2b are analyzed. Since both the BDSBAS and PPP-B2b utilize a ground monitoring station network 
to determine the satellite orbits and clock offset corrections, and broadcast differential corrections through the three 
Geostationary Orbit (GEO) satellites of BDS-3, the feasibility of the co-construction of BDSBAS and PPP-B2b is analyzed, 
strategies for the infrastructure sharing and correction broadcasting are presented, and the influences of BDSBAS 
correction broadcasting strategy adjustment are evaluated. In addition, it assesses the possibility of broadcasting 
differential corrections through the Inclined Geosynchronous Orbit (IGSO) satellites of BDS-3, and the feasibility of 
augmenting satellite navigation with Low Earth Orbit (LEO) satellites.
Keywords:  Satellite-based augmentation, Precise point positioning, Precise orbit, Precise clock offset, Ionospheric 
model
© The Author(s) 2022. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which 
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the 
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line 
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory 
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this 
licence, visit http://​creat​iveco​mmons.​org/​licen​ses/​by/4.​0/.
Introduction
The BeiDou Global Navigation Satellite System (BDS-
3) provides four types of positioning services, i.e. Radio 
Determination Satellite Service (RDSS, an active posi-
tioning based on radio measurement), Standard Point 
Positioning (SPP), positioning based on BDS-3 Satellite-
Based Augmentation System (BDSBAS) and Precise 
Point Positioning (PPP) through B2b signals of Geosta-
tionary Orbit (GEO) satellites (PPP-B2b) (Yang et  al., 
2018, 2019, 2020, 2021). The SPP of BDS-3 applies the 
same principle as other Global Navigation Satellite Sys-
tems (GNSSs), and its positioning accuracy is slightly bet-
ter than that of Global Positioning System (GPS) because 
the Signal-in-Space Range Errors (SISRE) of BDS-3 is 
smaller (Montenbruck et al., 2020). BDSBAS applies the 
same principle and standards as other Satellite-Based 
Augmentation Systems (SBAS), and is embedded into 
BeiDou Navigation Satellite System (BDS) as a compo-
nent. The principle of BDS PPP is consistent with that 
of the International GNSS Service (IGS), but the service 
coverage area and service mode are different. PPP is also 
embedded into the BDS, and become one of the featured 
services.
Differential positioning is a key to GNSS position-
ing augmentation. Ground reference stations with high-
accuracy known coordinates can be used to calculate 
various correction information, such as the satellite orbit 
errors, satellite clock offsets and atmospheric propaga-
tion errors, and then the calculated corrections are usu-
ally transmitted to user terminals. GNSS augmentation 
can be divided into the pseudo range and carrier phase 
differential augmentation. The former possesses good 
real-time characteristic, but relatively lower accuracy; 
Open Access
Satellite Navigation
https://satellite-navigation.springeropen.com/
*Correspondence:  yuanxi_yang@163.com
1 State Key Laboratory of Geo-Information Engineering, Xi’an 710054, 
China
Full list of author information is available at the end of the article

> [1 Figure(s)]

<!-- PAGE: 3 -->

Page 2 of 9
Yang et al. Satellite Navigation             (2022) 3:5 
the latter can achieve higher accuracy, but relatively poor 
timeliness for it takes a longer time for the results to 
converge.
The GNSS augmentation system can be divided into 
Ground-Based Augmentation System (GBAS) and SBAS 
according to the broadcasting mode of augmented infor-
mation. GBAS generally broadcasts various differential 
corrections to users through terrestrial radio or inter-
net, such as the Real-Time Kinematic (RTK) positioning 
and Local Area Augmentation System (LAAS). SBAS 
broadcast differential corrections through GEO satellites, 
which generally provide critical support for civil aviation 
safety. Typical SBASs include United States’ “Wide Area 
Augmentation System” (WAAS), the European Union’s 
“European Geostationary Navigation Overlay System” 
(EGNOS), Russia’s “System for Differential Corrections 
and Monitoring” (SDCM), Japan’s “Multi-Functional 
Transport Satellite (MTSAT) Satellite-based Augmenta-
tion System” (MSAS) and India’s “GPS Aided GEO Aug-
mentation Navigation” (GAGAN) (Shao et al., 2020).
According to the coverage of the ground monitor-
ing (tracking) station network and the augmentation 
service, GNSS augmentation can be divided into wide 
area augmentation system and local augmentation sys-
tem. The former is generally used for national-scale or 
regional-scale GNSS augmentation, while the latter for 
the high-dynamic vehicle precision approach or preci-
sion landing guidance in specific application scenarios, 
such as airports. RTK positioning still belongs to local 
augmentation even though it can provide ultra-long dis-
tance RTK service (Li et al., 2017a, b). PPP based on the 
IGS center products is generally regarded as wide area 
augmentation.
This paper focuses on the satellite-based augmentation 
and PPP technology and analyzes their basic principles 
and possible development trends.
The reliability of SBAS is a key issue for life safety. 
SBAS generally adopts navigation satellite signals (obser-
vations) received by continuous ground tracking stations 
and sends them to a ground processing center, where 
various corrections are calculated, such as satellite orbit 
corrections, clock offset corrections and ionospheric 
corrections. Then these corrections are broadcast to 
users via the GEO satellites. Considering the life safety, 
it is necessary to create redundancy and backup for the 
ground processing center, uplink station, and satellites 
that broadcast the corrections. In addition, integrity 
information is broadcast by SBAS as well.
The PPP is a generalized differential positioning 
method in the authors’ viewpoint. PPP has been widely 
used in many fields since Zumberge et  al. (1997) pro-
posed the method. It generally includes a global refer-
ence station network to collect the observed GNSS data 
and the related service centers to calculate the satellite’s 
precise orbits, precise clock offset, and ionospheric grid 
corrections which are usually broadcast to users through 
the internet. Some scholars regard PPP as a non-differ-
ential positioning technology. It seems that PPP can real-
ize decimeter-, centimeter- and even millimeter-level 
positioning accuracy by only utilizing the precise satel-
lite orbit, clock offset products, and corresponding pre-
cise observation models, and no need for the differential 
calculation from nearby reference stations. However, 
the corrections used in PPP rover-end including satellite 
orbit errors and clock offsets are indeed solved from a 
global reference network. It is in principle also a differen-
tial positioning but with respect to a network, instead of 
a single or few reference stations (Glaner & Weber2021; 
Héroux & Kouba, 1995). The influences of these common 
errors (satellite orbit error and clock offset error) are 
weakened by the differential positioning model. In addi-
tion, PPP employs the carrier phase for positioning, and 
therefore many researches focus on the fixing of carrier-
phase ambiguity parameters (Gao & Shen, 2002; Ge et al., 
2008).
PPP-B2b service of China’s BDS is a satellite-based ser-
vice. The observations from the densified ground tracking 
network are collected and sent to the ground operation 
control center, where the precise satellite orbits and clock 
offsets of BDS and GPS constellations are calculated, and 
then uplinked to the three GEO satellites. Then the GEO 
satellites broadcast them through B2b signals to the users 
in China and surrounding areas (Yang et al., 2020, 2021).
The satellite-based augmentation services of BDS and 
PPP-B2b are similar, but have their own characteristics. 
We describe the principles and performance of BDSBAS 
and PPP-B2b in the following two sections, respectively. 
Then the possible future developments for BDSBAS and 
satellite-based PPP are discussed.
BDSBAS
The construction of China’s SBAS, known as BDSBAS, is 
completed. The corresponding single frequency and dual 
frequency positioning performances were described and 
analyzed (Chen et al., 2020; Yang et al., 2021); the dual 
frequency integrity parameter performance of BDSBAS 
(Shao et al., 2020) and the ephemeris correction perfor-
mance of BDSBAS in China (Jin et al., 2021) were also 
analyzed. Since the ionospheric correction is an impor-
tant influencing factor, some scholars analyzed the ion-
ospheric anomaly detection method of BDSBAS (Bao 
et al., 2019).
BDSBAS is a service component of BDS and they 
are  constructed simultaneously. BDSBAS is composed 
of ground monitoring stations, a data processing center, 
the  differential correction product uplink antenna, and

<!-- PAGE: 4 -->

Page 3 of 9
Yang et al. Satellite Navigation             (2022) 3:5 
	
the  correction broadcasting satellite system. It follows 
the International Civil Aviation Organization (ICAO) 
standards and is consistent with the principles of other 
international SBAS systems. BDSBAS employs the three 
GEO satellites of BDS-3 located at 80° E (PRN 144), 
110.5° E (PRN 143) and 140° E (PRN 130), respectively, 
to broadcast corrections (Liu et al., 2021); the uplink sys-
tem of BDS is used to inject the differential corrections 
of BDS and other GNSSs, calculated by the ground data 
processing center, into GEO satellites. Specifically, the 
BDSBAS-B1C signal protocol only supports GPS and 
GLObal NAvigation Satellite System (GLONASS), while 
BDSBAS-B2a signal supports BDS, GPS, Galileo Naviga-
tion Satellite System (Galileo) and GLONASS.
The time scale and reference coordinate system of 
BDSBAS are consistent with other existing SBAS sys-
tems, such as WAAS and EGNOS. The time system of 
BDSBAS is consistent with the BDS Time (BDT) tBDT. 
The single frequency Service Network Time (SNT) tSNT 
of BDSBAS can be expressed as tSNT = tBDT + 14, and the 
synchronization with GPS Time (GPST) tGPST is main-
tained within 50 ns (CSNO., 2020). The coordinate sys-
tem adopts World Geodetic System 1984 (WGS84) as 
required by ICAO. However, it must be noted that Chi-
na’s BDS adopts BeiDou Coordinate System (BDCS), 
which is aligned with China Geodetic Coordinate System 
2000 (CGCS2000) (Yang, 2009). CGCS2000 is consistent 
with WGS-84 at centimeter level and the slight difference 
will not affect the flight safety for civil aviation users.
BDSBAS provides two augmented signals, namely 
BDSBAS-B1C (central frequency: 1575.42  MHz) and 
BDSBAS-B2a (central frequency: 1176.45  MHz). BDS-
BAS-B1C adopts the Binary Phase Shift Keying (BPSK(1)) 
modulation mode with a symbol rate of 250 bit/s, which 
broadcasts GPS augmentation corrections (compat-
ible with GLONASS in the future) mainly for civil avia-
tion single frequency users of GPS L1C/A; BDSBAS-B2a 
adopts the Quadrature Phase Shift Keying (QPSK(10)) 
modulation mode with a symbol rate of 250 bit/s, which 
broadcasts BDS-3/GPS augmentation corrections (com-
patible with Galileo and GLONASS in the future), mainly 
for civil aviation dual frequency users of BDS-3 B1C/B2a 
and GPS L1C/L1A/L5.
The data processing center is responsible for collecting 
the tracking data from each ground reference station and 
calculating the corrections of state space domain (satel-
lite orbit corrections, satellite clock offset corrections 
and ionospheric error corrections) in BDSBAS. Then 
the master control station determines the effectiveness 
of the satellite signal through various integrity checks, 
and the modulated ranging signals with differential cor-
rections and integrity information are broadcast to users 
through the three GEO satellites of BDS-3. The level of 
the received BDSBAS-B1C signal at the antenna port is 
within the range of − 161 dBW to − 153 dBW, if a user 
can observe any GEO satellite of BDS with an elevation 
angle greater than or equal to 5 degrees.
In addition to broadcasting the differential corrections 
and integrity information of BDSBAS, the GEO satellites 
of BDS-3 also provide normal ranging and time transmis-
sion services through B1I and B3I signals.
The ground monitoring system of BDSBAS is tempo-
rarily composed of 27 stations (several other stations 
are to be built), which are basically evenly distributed 
throughout the territory of China.
The ionospheric model of BDSBAS adopts the iono-
spheric parameters determined by the ground moni-
toring stations, and the 5° × 5° Grid Ionospheric 
Vertical Delay (GIVD) is obtained using the Inverse 
Distance Weighting (IDW) method. The user needs to 
calculate the ionospheric correction of the location by 
interpolating the values at its surrounding grid points 
(Bao et  al., 2019; Ma et  al., 2021). However, there are 
only about 80% grid points in China whose ionospheric 
delay parameters can be reliably calculated, which greatly 
reduce the availability and continuity of the ionospheric 
corrections in China’s border areas due to the lack of 
ionospheric monitoring information in China’s sur-
rounding areas. Therefore, more monitoring stations in 
the surrounding areas are required for determining the 
ionospheric delay of BDSBAS. Like other SBASs in the 
United States and Japan, BDSBAS also uses Kriging fit-
ting method to calculate the GIVD of grid points, with 
the aim of improving the continuity of GIVD parameters. 
The availability of BDSBAS GIVD can reach 99.88%, and 
the ionospheric integrity risk is about 0.12%.
The positioning accuracy of BDSBAS is evaluated 
for the different stations in the territory of China. Only 
the positioning accuracy of stations in Beijing, Sanya, 
Lhasa, Qiemo, Shanghai, Xi’an and Kunming are listed in 
Table 1. The data of single-frequency and dual-frequency 
BDSBAS from December 4 to 10, 2021, namely the Day 
of Year (DOY) 338–344 are used to evaluate the position-
ing accuracy in the horizontal and vertical components at 
95% confidence level, with the sampling rate of 1 Hz.
In Table  1, HPE and VPE denote the horizontal and 
vertical positioning errors respectively. It can be seen 
from Table  1 that the BDSBAS single-frequency posi-
tioning accuracies for 7 stations are all better than 2.0 
and 3.0 m in the horizontal and vertical components at 
the  95% confidence level, with an average of 1.48 and 
2.78 m, respectively.
It can be seen from Table 2 that the averaged position-
ing accuracies of BDSBAS dual-frequency for 7 stations

<!-- PAGE: 5 -->

Page 4 of 9
Yang et al. Satellite Navigation             (2022) 3:5 
are 1.31 and 2.16 m in the horizontal and vertical compo-
nents (95%), respectively. The results show that the GIVD 
can effectively correct the ionospheric delays in single 
frequency positioning, but there are residual ionospheric 
errors; dual-frequency users can eliminate the influence 
of ionosphere, and the positioning accuracy is signifi-
cantly improved compared with that of single-frequency.
It must be noted that the positioning accuracy of BDS-
BAS in the border areas is slightly lower than that in 
central areas since the ground monitoring stations are 
distributed in the territory of China.
The single-frequency positioning availability of BDS-
BAS is greater than 99.99% in general and reaches 
99.97% in some western regions. Considering the limi-
tation of BDSBAS monitoring station distribution and 
the continuity and availability of ionospheric grid data, 
it is recommended that BDSBAS users employ the Dual 
Frequency Multi Constellation (DFMC) augmentation 
service provided by BDSBAS-B2a signal to implement 
precision positioning and CAT-I precision approach.
PPP‑B2b
PPP-B2b embedded in BDS-3 is a featured service pro-
vided by BDS-3 GEO satellites (Yang et  al., 2021). The 
corresponding service coverage is clearly described in the 
interface document. The signal design and signal format 
of PPP-B2b are also introduced in the relevant papers 
(Liu et al., 2020). Some scholars verified the service per-
formance and the efficiency of orbit corrections and 
clock offset corrections (Xu et al., 2021).
The BDS-3 PPP-B2b employs dozens of high-precision 
continuous tracking stations (with known station coordi-
nates and even precise time) distributed in the territory 
of China to track BDS satellites and obtain pseudo-code 
and carrier phase observations. The BeiDou operation 
control center calculates the precise orbits, clock off-
sets, differential code bias and user range accuracy index 
(URAI) to generate rapid ephemeris parameters, which 
are sent through the uplink station to three GEO sat-
ellites and then broadcast to the users in China and its 
surrounding areas. Users can easily determine their loca-
tions with high accuracy by using dual-frequency BDS 
terminals.
The 
central 
frequency 
of 
PPP-B2b 
signal 
is 
1207.14 MHz and the bandwidth is 20.46 MHz. The PPP-
B2b I-component (PPP-B2b-I) signal adopts BPSK (10) 
modulation mode with RHCP polarization mode. When 
the right-hand circularly polarized antenna has 0 dBi of 
gain (or the linear polarized antenna has 3 dBi of gain), 
the minimum received power level of the PPP-B2b_I on 
ground is -160 dBW (CSNC, 2020).
The frame of PPP-B2b-I navigation message is concat-
enated together with 16 symbols of the preamble, 6 sym-
bols of the PRN, and 6 symbols of the reserved flags to 
form 1000 symbols in total, and the broadcast time of 
each frame is 1 s after 64-ary Low-Density Parity Check 
(LDPC) channel coding. The reserved flags are used to 
identify the status of the PPP service: the "1" in the high-
est bit of the reserved flags means the PPP service of this 
satellite is unavailable; the "0" in the highest bit of the 
reserved flags means the PPP service of this satellite is 
available. According to the navigation message of PPP-
B2b broadcasting strategy, it is better for users to per-
form PPP in a cold start mode to obtain the corrections 
for all satellites.
The precise orbit and clock offset corrections broad-
cast by GEO satellites for PPP users are mainly used to 
accurately correct the satellite orbit and clock offset 
information of the broadcast ephemeris. The differential 
code bias correction mainly provides the service for dual 
frequency or multi frequency users to improve the con-
sistency of the code observations at different frequencies. 
It should be noted that the code bias broadcast by PPP-
B2b is calculated by the operation control system. Some 
scholars found that the code bias parameters of some sat-
ellites are slightly different from the in-orbit calculation 
Table 1  Single-frequency positioning accuracy of BDSBAS
Coordinate component
Beijing
Sanya
Lhasa
Qiemo
Shanghai
Xi’an
Kunming
Average
HPE (95%) (m)
1.54
1.68
1.72
1.34
1.13
1.11
1.88
1.48
VPE (95%) (m)
2.67
2.89
2.65
2.86
2.85
2.64
2.90
2.78
Table 2  Dual-frequency positioning accuracy of BDSBAS
Coordinate 
component
Beijing
Sanya
Lhasa
Qiemo
Shanghai
Xi’an
Kunming
Average
HPE (95%) (m)
1.28
1.67
1.35
1.84
0.84
1.06
1.12
1.31
VPE (95%) (m)
2.13
2.06
2.23
2.99
1.72
1.96
2.00
2.16

<!-- PAGE: 6 -->

Page 5 of 9
Yang et al. Satellite Navigation             (2022) 3:5 
	
results (Guo et al., 2015; Hu et al., 2019; Li et al., 2013, 
2018).
The PPP-B2b user range accuracy index of BDS-3 
mainly provides users with the priori accuracy of range 
observation. High precision users can use the variance 
component estimation or robust estimation method to 
estimate user range accuracy in real time and make more 
rational use of satellite range observation information 
(Yang et al., 2005).
International GNSS Monitoring and Assessment Sys-
tem (iGMAS) stations in Beijing (BJF1), Shanghai (SHA1) 
and Kunming (KUN) and a Multi-GNSS Experiment 
(MGEX) station in Wuhan (WUH2) are selected for the 
experiment. The basic information of the stations is pre-
sented in Table 3.
The data were collected from September 5 to 9, 2021 
(DOY 248–252), five days in total, with a sampling inter-
val of 30 s. The extended Kalman filter is used for param-
eter estimation, and the elevation cut-off angle is set as 
10°. The calculation results are shown in Table 4.
Table  4 lists the Root Mean Squares (RMS) errors of 
PPP-B2b kinematic positioning in the horizontal (H) 
and vertical (V) directions after convergence. The con-
vergence condition is that the horizontal and vertical 
positioning accuracies are better than 0.3 and 0.6  m, 
respectively, and can last for longer than 10 epochs. It 
should be mentioned that the accuracy of 0.3 and 0.6 m 
means that the horizontal and vertical component errors 
in the test calculation are with respect to the known 
coordinates of stations. In practice, however, the standard 
deviation of PPP positioning with a particular value may 
be applied for the convergence condition. It can be seen 
from Table 4 that the BDS-3 real-time PPP based on PPP-
B2b corrections can achieve decimeter-level kinematic 
positioning accuracy. After convergence, the horizontal 
and vertical positioning accuracy is better than 0.15 and 
0.2 m, respectively. The average convergence time of the 
selected stations is about 18 min.
The main differences between the PPP-B2b of BDS and 
the PPP provided by IGS are as follows.
(1)	 PPP-B2b provided by BDS-3 is a service embed-
ded into GEO satellites with no need for Internet 
access, which is very helpful for PPP users in the 
areas without Internet connection or 5G network 
coverage, such as in ocean, desert and plateau. By 
contrast, IGS-PPP provides services to global users 
through the Internet.
(2)	 IGS-PPP generates GNSS precise ephemeris and 
ultra-fast forecast ephemeris using the selected 
continuous tracking stations distributed around 
the world and provides high-precision services to 
global users through the Internet. The PPP-B2b 
tracking stations of BDS-3 are deployed only in the 
territory of China, and thus the effective service of 
PPP-B2b is limited to China and its surrounding 
areas. If more observations can be obtained from 
the stations around the world and used in GNSS 
orbit and satellite clock offset calculation, the ser-
vice accuracy of BDS-3 PPP-B2b will be improved.
Table 3  Basic information of stations
Station
Agency
Receiver
Antenna
WUH2
MGEX
JAVAD TRE_3
JAVRINGANT_G5T NONE
BJF1
iGMAS
CETC-54-GMR-4016
LEIAR25.R4 LEIT
SHA1
iGMAS
Unicore UB4B0
NOV 750.R4
KUN1
iGMAS
Unicore UB4B0
NOV 750.R4
Table 4  Accuracy (root mean squares) and convergence time of BDS PPP-B2b kinematic positioning
Positioning performance
WUH2
BJF1
SHA1
KUN1
H
V
H
V
H
V
H
V
RMS (m)
DOY 248
0.077
0.125
0.080
0.124
0.061
0.075
0.087
0.118
DOY 249
0.077
0.126
0.112
0.161
0.094
0.132
0.096
0.139
DOY 250
0.077
0.136
0.116
0.132
0.093
0.122
0.107
0.111
DOY 251
0.077
0.147
0.118
0.120
0.106
0.151
0.093
0.142
DOY 252
0.056
0.138
0.079
0.114
0.068
0.116
0.090
0.129
Average
0.073
0.134
0.101
0.130
0.085
0.119
0.094
0.128
Convergence time (min)
18.75
18.43
21.79
16.17

<!-- PAGE: 7 -->

Page 6 of 9
Yang et al. Satellite Navigation             (2022) 3:5 
(3)	 Both the reference coordinate system and time 
datum of PPP-B2b are different from those of IGS-
PPP. The former adopts BDCS and BDT scale, while 
the latter adopts the WGS 84 and GPST.
(4)	 The service area of BDS-3 PPP-B2b is also sub-
ject to the beam coverage of the three GEO satel-
lites of BDS-3. PPP-B2b cannot provide services 
for the areas where GEO satellite signal is unavail-
able, no matter whether it is within the coverage of 
the ground tracking stations or not, because users 
cannot receive the precise differential corrections 
broadcast by GEO satellites.
(5)	 If the ionosphere-free combination mode is adopted 
to implement BDS-3 multi signal combined PPP 
service, the B1C/B2a combination mode is recom-
mended for dual frequency users, and the B1C/B1I/
B2a combination mode is recommended for triple 
frequency users (Li et al., 2020).
Possible future developments for BDSBAS 
and satellite‑based PPP
Since BDSBAS and PPP-B2b provide similar basic prod-
ucts and follow similar principles, they might be possibly 
constructed and improved as a whole.
(1)	 The ground monitoring networks for BDSBAS and 
PPP-B2b can be co-constructed and shared. The 
function requirements for the two types of moni-
toring stations are similar, and their construction 
and maintenance are costly and laborious. There-
fore, the ground monitoring networks should be co-
constructed to realize resource sharing.
(2)	 BDSBAS and PPP-B2b can share the computing 
resource. Both need to generate precise orbit and 
clock offset corrections with different approaches. 
The former employs the pseudo-range observation 
or phase smoothing pseudo-range measurement to 
obtain orbit correction and clock offset corrections, 
while the latter adopts phase observations. The cor-
responding PPP-B2b products will achieve a slightly 
higher accuracy. In the authors’ viewpoint, BDS-
BAS can directly adopt the products with higher 
accuracy generated by PPP-B2b, sharing its com-
puting resource.
(3)	 BDSBAS and PPP-B2b navigation message broad-
casting modes can be unified on certain condi-
tions. For PPP-B2b, the update intervals of orbit 
correction and clock offset correction are 48 and 
6 s, respectively. For BDSBAS, the update interval 
is 120 s for satellite orbit correction (dx/dy/dz) and 
300 s for the grid ionosphere parameter. The update 
period for the fast correction parameters (mainly 
the combined corrections of orbit and clock offset 
after deducting broadcast ephemeris and long-term 
corrections, together with corresponding fast cor-
rections and the integrity parameters) is 6 s. If the 
update time intervals for the orbit corrections are 
unified to 48 s and for satellite clock offset correc-
tions are set to 6 s, both requirements of PPP-B2b 
and BDSBAS can be met. In this case, the fast cor-
rection parameter tends to be very small for BDS-
BAS compared to its accuracy, which can be set to 
zero and omitted.
It must be noted that the message data rate of BDS-
BAS is different from that of PPP-B2b, i.e., 250 bit/s for 
BDSBAS and 500 bit/s for PPP-B2b. PPP-B2b broadcasts 
more messages with shorter interval, and the rate is to 
be upgraded to 1000 bit/s or 2000 bit/s in the future. In 
order to share messages broadcast by them, the BDSBAS 
must be backward compatible, which means that the 
BDSBAS user terminal may need to be changed appro-
priately to improve the positioning accuracy. If the SBAS 
user does not change the reception mode, the message of 
PPP-B2b and BDSBAS can still be broadcast separately.
It should be noted that SBAS needs to broadcast the 
integrity information, which has not yet been consid-
ered in most PPP services. However, the integrity infor-
mation and early warning of abnormal information can 
also be helpful for regular navigation and positioning 
users because the robustness of data processing can be 
improved by selecting observations with reference to the 
early warning information.
(4)	 In addition to functioning as normal navigation, 
positioning and timing satellites, the three BDS-3 
GEO satellites broadcast the differential correc-
tions of BDSBAS and PPP-B2b and provide short 
message communication service and RDSS. If the 
two types of correction products of BDSBAS and 
PPP-B2b are combined and the resulting prod-
uct is uplinked to GEO satellites as a whole, then 
the pressure on uplink and broadcast channel can 
be reduced and the broadcasting platform and the 
uplink and downlink channel can be shared.
(5)	 Globally, most SBASs use GEO satellites to broad-
cast differential corrections, and users in northern 
hemisphere are subject to the "south wall effect" 
(Yang et al., 2020), which means that the GEO sig-
nals can be easily blocked by the obstacles in its 
south. In order to improve the availability of satel-
lite-based augmentation differential corrections, 
IGSO satellites can also be used to jointly broad-
cast the corrections of BDSBAS and PPP-B2b. The 
expected service coverage after the participation

<!-- PAGE: 8 -->

Page 7 of 9
Yang et al. Satellite Navigation             (2022) 3:5 
	
of the IGSO satellites is shown in Fig. 1. With the 
increase of the Number of visible SATellites (NSAT) 
with a probability of 95%, the service coverage will 
be obviously expanded, and the "south wall effect" 
of BDSBAS and PPP-B2b services for users in the 
Asia-Pacific region will disappear.
(6)	 The development of LEO constellation for augmen-
tation will also improve the service mode and per-
formance of SBAS and satellite-based PPP. On one 
hand, LEO satellites can broadcast satellite-based 
augmentation corrections; on the other hand, LEO 
satellites and BDS-3 satellites can form a hybrid 
constellation to broadcast normal navigation and 
positioning signals, which will significantly improve 
the geometric strength of the integrated constella-
tion, and then improve the orbit precision of BDS-3 
satellites and the measurement accuracy of satel-
lite clock offset. The participation of LEO constel-
lation in providing PPP-B2b service can effectively 
improve the convergence speed of PPP-B2b (Li 
et  al., 2022). Assuming that 120 LEO satellites at 
an altitude of 975  km with an orbital inclination 
of 55°  are evenly distributed on 12 orbital planes 
and participate in PPP service together with PPP-
B2b, the required convergence time corresponding 
to the positioning accuracies of 10 and 100 cm are 
shown in Table 5.
Obviously, with the support of LEO satellites, the 
"south wall effect" can be eliminated and the 1 and 0.1 m 
positioning accuracy can be achieved within 20  s and 
around 1 min, respectively.
(7)	With the wide application of satellite-based augmen-
tation and PPP, most ground-based augmentation 
services will gradually lose their significance.
Conclusions
BDSBAS and PPP-B2b are two types of embedded 
satellite-based augmentation services of BDS-3. They 
are important components and featured services of 
BDS-3. The single frequency positioning performance 
of BDSBAS can meet the CAT I precision approach 
requirements of ICAO, with the horizontal and vertical 
positioning accuracies better than 2.1 and 3.5 m, respec-
tively. The positioning accuracy in China’s surrounding 
areas is slightly lower, due to the fact that the ground 
monitoring stations are only deployed in the territory of 
China and the continuity of the ionospheric monitoring 
is relatively poor. The latest service performance of PPP-
B2b is as follows: the horizontal and vertical positioning 
accuracies are approximately 0.15 and 0.2 m; if the posi-
tioning accuracies are required to be better than 0.3 and 
0.6 m in the horizontal and vertical components, the con-
vergence time is within 20 min in general.
Both BDSBAS and PPP-B2b need a ground monitor-
ing station network, computing center and differential 
correction broadcasting platform. Therefore, we can for-
mulate an integrated plan to coordinate and optimize 
 
 
 
 
5
4
3
2
1
5
4
3
2
1
30
60
90
a
b
75
60
45
30
15
0
−15
−30
−45
−60
−75
−90
90
120
150
180
Longitude (°)
30
60
90
120
150
180
Longitude (°)
NSAT (95%)
NSAT (95%)
Latitude (°)
90
75
60
45
30
15
0
−15
−30
−45
−60
−75
−90
Latitude (°)
Fig. 1  a 3 visible GEO sats with the elevation cut-off angle of 40°. b 3 GEO + 3 IGSO visible satellites
Table 5  Convergence time of PPP-B2b + LEO
Stations
Convergence time of 
10 cm accuracy (s)
Convergence time of 
100 cm accuracy (s)
Beijing
44
7
Wuhan
59
17
Kunming
49
19
Shanghai
68
7

> [2 Figure(s)]

<!-- PAGE: 9 -->

Page 8 of 9
Yang et al. Satellite Navigation             (2022) 3:5 
the construction of them and employ the same ground 
monitoring station network and computing center. The 
precise orbit and clock offset of PPP-B2b can be used for 
the orbit correction and satellite clock offset correction 
of BDSBAS, the broadcasting frequency is also based on 
that of PPP-B2b, and the integrity information can be 
provided to both BDSBAS and PPP-B2b users.
If IGSO satellite is also added to BDSBAS and PPP-
B2b augmentation signal broadcast, the "south wall 
effect" will be reduced and the service availability will be 
improved. If LEO satellite augmentation is adopted, not 
only the "south wall effect" can be eliminated, but also the 
positioning accuracy will be significantly improved, and 
the convergence time will be shortened.
Acknowledgements
Not applicable.
Authors’ contributions
YY proposed the idea and drafted the article; QD provided the results of BDS-
BAS; WG provided the results of LEO satellites joint with PPP-B2b; JL calculated 
the coverage contribution of IGSO satellites; YX provided the new calculation 
results of PPP-B2b in the territory of China; BS assisted in text-proofing and 
manuscript revision. All the authors read and approved the final manuscript.
Funding
This work is supported by the National Natural Science Foundation of China 
(No. 41931076), the National Key Research and Development Program of 
China (No. 2020YFB0505802), and the Wenhai Program of Qingdao National 
Laboratory for Marine Science and Technology (QNLM) (No. 2021WHZZB1005).
 Availability of data and materials
The datasets used and/or analyzed during the current study are available from 
the corresponding author on reasonable request.
Declarations
Competing interests
The authors declare that they have no competing interests.
Author details
1 State Key Laboratory of Geo-Information Engineering, Xi’an 710054, China. 
2 Xi’an Research Institute of Surveying and Mapping, Xi’an 710054, China. 3 The 
20th Research Institute of China Electronics Technology Group Corporation, 
Xi’an 710054, China. 4 Satellite Navigation Laboratory, Beijing Institute of Track-
ing and Telecommunication Technology, Beijing 100094, China. 5 Beijing Satel-
lite Navigation Center, Beijing 100094, China. 
Received: 4 January 2022   Accepted: 6 February 2022
References
Bao, S., Li, R., Liu, Y., & Shao, B. (2019). Ionospheric anomaly detection to sup-
port the BDSBAS. IEEE Access, 99, 1691–1704. https://​doi.​org/​10.​1109/​
ACCESS.​2019.​29622​33
Chen, J., Wang, A., Zhang, Y., et al. (2020). BDS satellite-based augmentation 
service correction parameters and performance assessment. Remote 
Sensing, 12(5), 766.
CSNO. (2020). BeiDou navigation satellite system signal in space interface control 
document precise point positioning service signal PPP-B2b (Version 1.0). http://​
www.​beidou.​gov.​cn/​xt/​gfxz/​202008/​P0202​00803​36206​24829​40.​pdf
Gao, Y., & Shen, X. (2002). A new method for carrier-phase-based precise point 
positioning. Navigation, 49(2), 109–116.
Ge, M., Gendt, G., Rothacher, M., Shi, C., & Liu, J. (2008). Resolution of GPS 
carrier-phase ambiguities in Precise Point Positioning (PPP) with daily 
observations. Journal of Geodesy, 82(7), 389–399. https://​doi.​org/​10.​1007/​
s00190-​007-​0187-4
Glaner, M., & Weber, R. (2021). PPP with integer ambiguity resolution for GPS 
and Galileo using satellite products from different analysis centers. GPS 
Solutions. https://​doi.​org/​10.​1007/​s10291-​021-​01140-z
Guo, F., Zhang, X., & Wang, J. (2015). Timing group delay and differential 
code bias corrections for BeiDou positioning. Journal of Geodesy, 89(5), 
427–445. https://​doi.​org/​10.​1007/​s00190-​015-​0788-2
Héroux, P., & Kouba, J. (1995). GPS precise point positioning with a difference. 
Paper presented at geomatics’95. Canada, Ottawa, 13–15.
Hu, J., Zhang, X., Li, P., Ma, F., & Pan, L. (2019). Multi-GNSS fractional cycle bias 
products generation for GNSS ambiguity-fixed PPP at Wuhan University. 
GPS Solutions. https://​doi.​org/​10.​1007/​s10291-​019-​0929-9
Jin, B., Chen, S., Li, D., Wang, Y., & Takka, E. (2021). Performance analysis of SBAS 
ephemeris corrections and integrity algorithms in China region. Satellite 
Navigation. https://​doi.​org/​10.​1186/​s43020-​021-​00045-z
Li, B., Li, Z., Zhang, Z., & Tan, Y. (2017). ERTK: Extra-wide-lane RTK of triple-fre-
quency GNSS signals. Jouurnal of Geodesy, 91(9), 1031–1047. https://​doi.​
org/​10.​1007/​s00190-​017-​1006-1
Li, J., Yang, Y., He, H., & Guo, H. (2020). Benefits of BDS-3 B1C/B1I/B2a triple-
frequency signals on precise positioning and ambiguity resolution. GPS 
Solution, 26, 29. https://​doi.​org/​10.​1007/​s10291-​020-​01016-8
Li, M., Xu, T., Guan, M., Gao, F., & Jiang, N. (2022). LEO-constellation-
augmented multi-GNSS real-time PPP for rapid re-convergence 
in harsh environments. GPS Solution. https://​doi.​org/​10.​1007/​
s10291-​021-​01217-​91-​021-​01217-9
Li, P., Zhang, X., & Guo, F. (2017). Ambiguity resolved precise point positioning 
with GPS and BeiDou. Journal of Geodesy, 91(1), 25–40.
Li, X., Ge, M., Zhang, H., & Wickert, J. (2013). A method for improving uncali-
brated phase delay estimation and ambiguity-fixing in real-time precise 
point positioning. Journal of Geodesy, 87(5), 405–416.
Li, X., Li, X., Yuan, Y., Zhang, K., Zhang, X., & Wickert, J. (2018). Multi-GNSS phase 
delay estimation and PPP ambiguity resolution: GPS, BDS, GLONASS. 
Galileo. Journal of Geodesy, 92(6), 579–608.
Liu, C., Gao, W., Liu, T., Wang, D., Yao, Z., Gao, Y., Nie, X., Wang, W., Li, D., Zhang, 
W., Wang, D., & Rao, Y. (2020). Design and implementation of a BDS 
precise point positioning service. Navigation, 67(4), 875–891. https://​doi.​
org/​10.​1002/​navi.​392
Liu, C., Gao, W., Shao, B., Lu, J., Wang, W., Chen, Y., Su, C., Xiong, S., & Ding, Q. 
(2021). Development of BeiDou satellite-based augmentation system. 
Navigation. https://​doi.​org/​10.​1002/​navi.​422
Ma, Y., Tang, C., Hu, X., Chang, Z., Pu, J., Nan, X., Cao, Y., & Wang, N. (2021). 
Optimalization of GIVE algorithm for grid-based single shell ionospheric 
model over Chinese region based on residual statistics. Acta Geodaetica Et 
Cartographica Sinica, 50(3), 304–314.
Montenbruck, O., Steigenberger, P., & Hauschild, A. (2020). Comparing the ’Big 
4’ —A user’s view on GNSS performance. In 2020 IEEE/ION Position, Loca-
tion and Navigation Symposium (PLANS) (pp. 407–418). IEEE. https://​doi.​
org/​10.​1109/​PLANS​46316.​2020.​91102​08
Shao, B., Ding, Q., & Wu, X. (2020). Estimation method of SBAS dual-frequency 
range error integrity parameter. Satellite Navigation. https://​doi.​org/​10.​
1186/​s43020-​020-​00011-1
Xu, Y., Yang, Y., & Li, J. (2021). Performance evaluation of BDS-3 PPP-B2b precise 
point positioning service. GPS Solution., 25(4), 1–14.
Yang, Y. (2009). Chinese geodetic coordinate system 2000. Chinese Science 
Bulletin, 54, 2714–2721.
Yang, Y., Gao, W., Guo, S., Mao, Y., & Yang, Y. (2019). Introduction to BeiDou-3 
navigation satellite system. Navigation, 66(1), 7–18.
Yang, Y., Liu, L., Li, J., Yang, Y., Zhang, T., Mao, Y., Sun, B., & Ren, X. (2021). Featured 
services and performance of BDS-3. Science Bulletin, 66(20), 2135–2143. 
https://​doi.​org/​10.​1016/j.​scib.​2021.​06.​013
Yang, Y., Mao, Y., & Sun, B. (2020). Basic performance and future developments 
of BeiDou global navigation satellite system. Satellite Navigation, 1(1), 1–8. 
https://​doi.​org/​10.​1186/​s43020-​019-​0006-0
Yang, Y., Xu, T., & Song, L. (2005). Robust estimation of variance components 
with application in Global Positioning System network adjustment. 
Journal of Surveying Engineering, 131(4), 107–112.

> [1 Figure(s)]

<!-- PAGE: 10 -->

Page 9 of 9
Yang et al. Satellite Navigation             (2022) 3:5 
	
Yang, Y., Xu, Y., Li, J., & Yang, C. (2018). Progress and performance evaluation of 
BeiDou global navigation satellite system: Data analysis based on BDS-3 
demonstration system. Science China Earth Sciences, 61(5), 614–624.
Zumberge, J. F., Heftin, M. B., Jefferson, D. C., Watkins, M. M., & Webb, F. H. 
(1997). Precise point positioning for the efficient and robust analysis of 
GPS data from large networks. Journal of Geophysical Research, 102(B3), 
5005–5017.
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in pub-
lished maps and institutional affiliations.
View publication stats
