<!-- PAGE: 1 -->

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/341982748
Precise Point Positioning Performance Evaluation of QZSS Centimeter Level
Augmentation Service
Chapter · June 2020
DOI: 10.1007/978-981-15-3715-8_8
CITATIONS
2
READS
679
4 authors, including:
Maosen Hao
Chang'an University
2 PUBLICATIONS   2 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Maosen Hao on 16 September 2020.
The user has requested enhancement of the downloaded file.

> [1 Figure(s)]

<!-- PAGE: 2 -->

Precise Point Positioning Performance
Evaluation of QZSS Centimeter Level
Augmentation Service
Maosen Hao1, Wenhai Jiao2, Xiaolin Jia3, and Qingrui Tao1
Abstract.
The
Japanese
Quasi-Zenith
Satellite
System(QZSS)
provides
Centimeter-Level Augmentation Service(CLAS) through L6 signal. The L6
augmentation messages includes satellite orbit correction, clock correction, phase
bias,
code
bias,
troposphere
correction,
ionosphere
correction
and
other
augmentation messages. These augmentation messages are used for a PPP-RTK
service. Using PPP-RTK service, users in Japan can get high-precision real-time
positioning results. Based on the measured data of AIRA, STK2, TSK2 and
USUD of four MGEX stations in Japan, this paper analyzes the PPP augmentation
performance of L6 augmentation signal by post static PPP, and compares it with
the calculation results of QZSS final orbit and clock products. The results show
that there is still a certain gap between the accuracy of orbit and clock augmented
by L6 signal and the final products of QZSS. The static PPP based on L6 signal
can realize centimeter-decimeter level positioning, and the positioning accuracy is
lower than that of the final products of QZSS. Analysis reason: as CLAS are used
to augment PPP-RTK services, PPP augmented service is out of scope of its pre-
service. Therefore, the published orbit and clock correction are not a real-time
precise orbit and clock correction,which leads to a gap between the corrected orbit
and clock and the final products.Similarly, due to different application services,
there are differences in positioning results.
Keywords: Centimeter-Level Augmentation Service·PPP·L6 signal·Signal-
in-Space Accuracy·SSR
1 Maosen Hao
Chang’an University, Xi’an 710054, Shanxi, China
2 Wenhai Jiao
Beijing Institute of Tracking and Telecommunications Technology, Beijing,
China
3 Xiaolin Jia()
Xi’an Research Institute of Surveying and Mapping, Shaanxi, China
Email: 13891907401@139.com
1 Qingrui Tao
Chang’an University, Xi’an 710054, Shanxi, China

<!-- PAGE: 3 -->

2
1 Introduction
Quasi-Zenith Satellite System (QZSS) is a new generation of regional satellite
navigation system jointly established by the Japanese government and enterprises.
On November 1, 2018, the Japanese government announced the official operation
of the QZSS system. The QZSS system consists of four satellites, three are
Inclined Geo-Synchronous Orbit (IGSO) satellites, and one is a Geo-Synchronous
Orbit (GEO) satellite. There are two types of augmentation services officially
provided by QZSS:
Sub-meter Level Augmentation Service
(SLAS) and
Centimeter-Level Augmentation Service (CLAS), the augmented services are
realized by broadcasting L1-SAIF augmented information and L6 augmented
information respectively [1]. The CLAS is mainly applied in Japan to achieve
high-precision positioning services. The L6 signal is divided into L61 and L62
signals. The L61 signal is transformed from the LEX signal of the former QZSS-1
star (MICHIBIK-I), and the L62 is mainly used for the QZS 2-4 star. At present,
L62 information is divided into two types: L6D and L6E. L6D is mainly used for
the CLAS service, and L6E is mainly used for CLAS-E (Centimeter-Level
Augmentation Message for Experiments) service. It is released by Japan JAXA
(Aerospace Exploration Agency) Multi-GNSS Advanced Demonstration tool for
Orbit and Clock Analysis (MADOCA) products based on L6E signals. The L6
signal herein refers to the L6D signal for CLAS service.
QZSS mainly releases augmented information in the form of RTCM-SSR,
including correction information of satellite orbit and clock error, phase bias, code
bias, ionosphere, etc. Users can receive augmented information and broadcast
ephemeris in real-time, extract and correct augmented information. Corrected to
the broadcast orbit to generate a more accurate real-time satellite orbit and clock
offset to achieve high-precision PPP. During the development of the QZSS
system, many experts and scholars studied the QZSS system from different
aspects. Wang Guohui analyzed that the orbit error of the MICHIBIK-I satellite is
better than 11cm, the clock error is better than 16.8cm [2]; Suelynn Choy et al.
[3] proved that the performance of PPP based on LEX can reach decimeter level in
Japan and Australia; Lou Yidong and others proved the feasibility of using the
LEX signal to achieve sub-meter PPP positioning in the eastern coastal areas of
China [4]; Zhang Wenfeng and Jiang Yongsheng found that kinematic and static
PPP solutions based on LEX can achieve decimeter and centimeter accuracy,
respectively [5-6]; Bu Weijin found a combination of BDS and QZSS positioning
can improve the positioning accuracy, reliability, and stability of BDS single
systems in the Asia-Pacific region [7]; Robert Odolinski et al. [8] found that at
higher cut-off altitude angles,the four-system (BDS, Galileo, GPS, QZSS) RTK
model
allows
for
improved
integer
ambiguity
resolution
and
positioning
performance over the single-, dual- or triple systems; Hiromune Namie, etc. found
that the Network RKT post-positioning accuracy based on LEX signals can reach
RMS and STD within 1cm [9]; Zhang Shaocheng et al. [10] proved that real-time

<!-- PAGE: 4 -->

3
L6E products can provide orbit and clock accuracy of centimeter level, and
kinematic PPP positioning can reach 4.9cm, 4.2cm, 11.7cm in three directions of
ENU, respectively; Po Chunchiu et al. [11] found that L6D-based single-
frequency PPP can improve the convergence time. Within a day, 83% of epoch
positioning accuracy can reach 1m, and 50% of epoch positioning accuracy can
reach 0.3m. This paper mainly introduces the CLAS augmented service based on
QZSS L6D signals, and uses the measured data to evaluate the SIS User Range
Error of the augmented orbit and clock offset. At the same time, the dual-
frequency PPP performance of the augmented service is evaluated.
2 L6 augmentation information content and application
2.1 L6 augmentation information introduction
QZSS system transmits a total of 5 frequencies and 8 signals, including GPS-com
patible PNT service signals: L1C/A, L1C, L2C and L5; L1S signal for the fully fu
nctional sub-meter level augmentation service (SLAS) and disaster and crisis man
agement information dissemination service (DC Report); Provide L5S signal of sat
ellite positioning new technology experiment service (PTV); L6 signal for centime
ter-level augmentation service (CLAS). CLAS augments the service by broadcasti
ng L6D augmentation information on L6 frequency band. The service area of CL
AS is in Japan, which is divided into 19 networks. The service scope and Network
distribution are shown in Fig. 1, different colors represent different Network areas
[11]. The center frequency of the L6 signal is 1278.75 MHz and the frequency ba
ndwidth is 39.0 MHz. The four QZSS satellites (J01, J02, J03, and J07) all provide
centimeter-level augmentation service.L6 signals are stored in SSR format using
RTCM 10403.2 standard. L6 files are published hourly and can be downloaded fro
m the official QZSS website (https://sys.qzss.go.jp/dod/en/archives/agree.html).
Table 1. Correction information in L6 document
Message
Sub
Type ID
Message Name
Nominal
Update
Interval(s)
1
Compact SSR Mask
30
2
Compact SSR GNSS Orbit Correction
30
3
Compact SSR GNSS Clock Correction
5
4
Compact SSR GNSS Satellite Code Bias
30
5
Compact SSR GNSS Satellite Phase Bias
30

<!-- PAGE: 5 -->

4
6
Compact SSR GNSS Satellite Code and Phase Bias
30
7
Compact SSR GNSS URA
30
8
Compact SSR STEC Correction
30
9
Compact SSR Gridded Correction
30
10
Compact SSR Service Information
(N/A)
11
Compact SSR GNSS Combined Correction
5 or 30
Table 1 shows the correction information contained in the L6 file. At present,
correction information of GNSS satellites only includes correction information of
GPS satellites, Galileo satellites and QZSS satellites. GLONASS system and BDS
system are under construction. Type 6 is the correction information of satellite
code bias and phase bias. The user selects the applicable correction information
according to the Network ID of the area in which they are located. The
ionospheric correction information and tropospheric correction information in
types 8 and 9 are limited to use in Japan. The ionospheric grid information and
tropospheric correction information suitable for this region should be matched
with the Network ID in Japan. Type 11 combined correction information contains
orbit correction information and clock correction information.
Fig. 1. CLAS service area and Network distribution
2.2 Real-time precise orbit and clock error recovery
The orbit and clock offset correction information in the L6D augmentation
information is added to the orbit and clock offset calculated by the broadcast

> [1 Figure(s)]

<!-- PAGE: 6 -->

5
ephemeris to obtain the recovered real-time precise orbit and clock offset. The
orbit correction data in Table 1 are the correction information in the orbit
coordinate system, which indicate the satellite position correction data in three
directions: radial, along-track and cross-track. The correction information are
based on the satellite antenna phase center (APC, Antenna Phase Center) ; clock
error correction data is based on the correction information of clock error
parameters in broadcast ephemeris:
0
C ,
1
C ,
2
C , where
1
C and
2
C is zero. The time
reference of each correction information is GPS time system.
CLAS augmentation algorithm stipulates: if the Network ID of type 11
correction information in Table 1 is the same as the Network ID of the user's
location, then the correction information of orbit and clock in type 11 correction
information shall be adopted for correction. Otherwise, the correction information
of orbit and clock in the correction information of type 2 and type 3 are used to
correct .
Real-time precise orbit recovery:
Suppose the orbit correction information at time t is 

c
a
r
R
R
R
,
,
, the satellite
position in the ECEF coordinate system calculated by the broadcast ephemeris at
the moment is


0
0
0
,
,
Z
Y
X
R 
, and the satellite velocity is


z
y
x
V
V
V
V
,
,

, and the
correction information in the ECEF coordinate system is 

Z
Y
X



,
,
. Firstly,
the modified value is transformed from orbital coordinate system to ECEF
coordinate system:


























c
a
r
c
a
r
R
R
R
e
e
e
Z
Y
X
,
,
(2.1)
Where:
)
(
)
(
t
V
t
V
ea 
,
)
(
)
(
)
(
)
(
t
V
t
R
t
V
t
R
ec



,
c
a
r
e
e
e


.
Then the satellite position corrected at time t is:



































Z
Y
X
Z
Y
X
Z
Y
X
0
0
0
(2.2)
Real-time precise clock error recovery:
Suppose the clock difference correction parameter at time t is 

2
1
0
,
,
C
C
C
, and
the correction parameter
1
C and
2
C in QZSS are zero, the satellite clock difference
calculated by broadcast ephemeris at this time is
gt , and the speed of light is c ,
then the corrected satellite clock difference is
st :
c
C
t
t
g
s
0


(2.3)

<!-- PAGE: 7 -->

6
3 Accuracy analysis of real-time orbit and clock error
In order to evaluate the GPS real-time orbit and clock offset data generated by the
L6 augmented information, GPS precise orbits with an epoch interval of 15 min
and precise clock offset with an epoch interval of 5 min provided by QZSS were
selected as references (https://sys.qzss.go.jp/dod/en/archives/pnt.html). Relevant
data of DOY 258-260 days in 2019 were selected for experiments to analyze the
augmented orbit and clock difference accuracy.
Assessment methods:
The space-time datum is unified, and the time system is unified to GPST, and
the coordinate datum is unified to ITRF2008 coordinate system.
Antenna phase center conversion: since the reference point of precise orbit
satellite position is the satellite center of mass, the reference point of broadcast
ephemeris and L6 correction information is the satellite antenna phase center.
Therefore, when comparing the accuracy of the orbit, the IGS14 antenna file was
used to correct the orbit coordinates from the antenna phase center to the satellite
mass by using the dual-frequency ionospheric combination.Then compare the
orbit R, A, and C to get the errors of the augmented orbit and QZSS precise orbit
in the R, A, and C direction, and then calculate the RMS values in each direction.
Clock offset accuracy analysis: In order to eliminate the influence of different
clock offset benchmarks on the accuracy analysis, this paper adopts the quadratic
error method to analyze the corrected satellite clock offset. The specific methods
are as follows: first, make a difference between the satellite clocks with the same
epoch to obtain a difference. Then sum up the difference between the epochs of
the same satellite and calculate the average value.Then subtract the average value
of the satellite from the primary difference of the satellites, make the secondary
difference to obtain the error of the augmented satellite offset. Finally, the RMS
value of the satellite clock offset error is calculated.
Accuracy analysis of SIS User Range Error (SISURE) : after the accuracy
analysis of the orbit and clock offset, the following formula was used to calculate
the SISURE of different satellites, and finally the RMS value of SISURE of each
satellite was calculated.
)
(
)
(
2
2
,
2
C
A
cdt
R
SISURE
C
A
R









(2.4)
In Equation (2.4),
R
and
C
A,

are the contribution factors of radial direction R
and along-track direction A and cross-track direction C, c are the speed of
light, dt are the error of satellite clock, and
C
A
R



,
,
are the errors in the radial
direction, along-track direction and cross-track direction of orbit, respectively.
The final orbit and clock offset of QZSS were selected as a reference. The
results of comparing the satellite clock after L6 augmentation with the QZSS final
clock are shown in Fig. 2 and Fig. 3, and the errors of the orbit, clock and SISURE
are shown in Fig. 4.

<!-- PAGE: 8 -->

7
Fig. 2. GPS 1-16 star clock difference comparison
Fig. 3. GPS 17-32 star clock difference comparison
In the Fig. 2 and Fig. 3, G04, G13 and G18 satellites are missing because the
orbit information of these three satellites is not published in the precise ephemeris

> [2 Figure(s)]

<!-- PAGE: 9 -->

8
of QZSS. The clock difference comparison sequence diagram is discontinuous
because L6 products only release satellite correction information that is observable
and available in Japan. It can be seen from Fig. 4, the clock error RMS is between
0.15m and 0.65m. The orbit error fluctuates greatly, and the radial direction is
generally below 0.65m. The G10 satellite has a large error, which exceeds 1m.
Along-track direction and cross-track direction fluctuate greatly, leading to a
maximum of 2.2m. SISURE as a whole was within 0.9m, while G10 and G21
satellites reached 1.7m and 1.2m, respectively. The G10 and G21 satellites
fluctuated significantly compared to other satellites, and the correction errors were
relatively large. The corrections of other satellites were relatively stable. On
average, the augmented clock offset accuracy is about 0.46m, radial average
accuracy is about 0.26m, along-track accuracy is about 1.05m, cross-track
accuracy is about 0.94m, three-dimensional accuracy is about 1.44m, and SISURE
accuracy is about 0.62m. In general, there is still a certain gap between the
augmented GPS orbit and clock offset and the QZSS final orbit and clock offset.
Analyzing the reasons, the CLAS service of QZSS is oriented to PPP-RTK
service, and the clock offset and orbit correction information published at each
moment are not precise orbit and clock offset correction information. Compared
with the correction information issued by the IGS Real-Time Service (IGS-RTS)
at the same time, there are certain errors in the corrections and even the opposite
corrections ,but this in CLAS service is normal, because the CLAS augmented
service emphasizes the sum of the corrections in the direction of the receiver-to-
satellite line of sight (including orbit correction, clock difference correction,
satellite code and phase bias correction, etc.) is always the best . Therefore, the
accuracy of the orbit and clock offset may not be ideal after correction.
Fig. 4 . GPS 1-32 star R, A, C, CLK, SISURE error

> [1 Figure(s)]

<!-- PAGE: 10 -->

9
4 Precise Point Positioning analysis of L6D products based on
QZSS system
In order to evaluate the PPP augmentation performance of L6D augmentation
information, this paper selected the MGEX (Multi-GNSS Experiment) observation
data of the four stations in Japan: AIRA, STK2, TSK2, and USUD. L6 products
published by QZSS were used to perform a post static PPP processing of DOY
258-260 on the four stations. At the same time, the precise orbit and precise clock
products published by QZSS were used for the same processing of the above data,
and the processing results were taken as reference. Finally, the coordinates in the
SINEX file of IGS on that day were used as the real value to calculate deviation
statistics of PPP results in the directions of E, N and U.
Table 2. PPP treatment plan
Project category
CLAS plan
QZSS plan
Orbit product
Brdc+CLAS correction
QZSS final product
Clock product
Brdc+CLAS correction
QZSS final product
Ionospheric error
Dual-frequency Iono-free
Dual-frequency Iono-free
Tropospheric error
CLAS correction
Saastamoinen model
Code bias
CLAS correction
Code DCB correction
Phase bias
CLAS correction
null
Cut-off height Angle/(°)
15
15
Tidal correction
Model correction
Model correction
Satellite antenna phase center correction
Model correction
Model correction
Receiver antenna phase center correction
Model correction
Model correction
Receiver position
SPP calculation
SPP calculation
Ambiguity
Not fixed
Not fixed
Table 3. Introduction of using station information
station name
Network ID
Receiver type
Receiver antenna type
Received data type
AIRA
3
Trimble NetR9
TRM59800.00
G+E+R+J
STK2
10
Trimble NetR9
TRM59800.00
G+E+R+J
TSK2
7
Trimble NetR9
TRM59800.00
G+E+R+J
USUD
7
SEPT POLARX5
AOAD/M_T
G+E+R+C+J
Table 2 shows the two PPP treatment plans, and Table 3 shows the relevant
information of test stations used in the experiment. The post static PPP processing

<!-- PAGE: 11 -->

10
was performed on the four stations for three days. Fig. 5 shows the deviation of
the positioning results of the two plans of the four stations in the directions of E, N
and U.
Fig. 5. Positioning accuracy of four stations in DOY 260
Table 4 shows the statistical results of PPP positioning accuracy after CLAS
augmentation and PPP positioning accuracy using QZSS final precise ephemeris
and clock products. It can be seen that the positioning error after the augmentation
is smaller in the direction of E, at the level of cm; However, it fluctuates greatly in
the direction of N and in the level of centimeter-decimeter. The horizontal
accuracy of the four stations fluctuates between centimeters and decimeters. In
Fig. 5, it can be clearly found that the convergence rate of positioning using QZSS
final precise ephemeris and clock product is significantly faster than that of CLAS
augmented positioning. As can be seen from Fig. 5, the positioning result after
CLAS augmentation is about 6cm in the direction of E, 11cm in the direction of
N, and 18cm in the direction of U. The positioning results of the final precise
ephemeris and clock products using QZSS are better than the augmented results.
The DOY 258-260 positioning process was performed for three days, and values
with deviations less than 20cm in the direction of E and N and less than 40cm in
the direction of U were selected for statistics. The positioning direction of ENU in
CLAS plan converges to 20cm, 20cm and 40cm at about 420 (30s) of the period,
and the RMS for calculating the deviation values of the three directions are shown
in Table 4. The PPP positioning accuracy after CLAS augmentation can achieve
centimeter-decimeter level positioning, horizontal accuracy is about 13cm, vertical

> [1 Figure(s)]

<!-- PAGE: 12 -->

11
accuracy is about 16cm, and L6 file can be used for augmented positioning
service. However, the results of PPP positioning with QZSS final precise
ephemeris and clock product still have large errors. This is because CLAS is
oriented to the PPP-RTK service, and there is a difference between the algorithms
of PPP and PPP. Therefore, when performing PPP positioning, there may be large
errors in the positioning results. When CLAS is applied to the PPP-RTK service, it
can achieve higher positioning accuracy and achieve centimeter-level positioning
accuracy.
Table 4. RMS statistics of PPP positioning errors for two plans of four stations
Station
CLAS-
E(cm)
CLAS-
N(cm)
CLAS-
U(cm)
CLAS-
H(cm)
QZF-
E(cm)
QZF-
N(cm)
QZF-
U(cm)
QZF-
H(cm)
AIRA
7.85
8.17
16.87
11.33
0.74
1.11
4.99
1.33
TSK2
5.13
12.44
17.94
13.46
0.41
0.90
1.70
0.99
STK2
3.48
8.89
12.22
9.54
0.58
0.82
3.60
1.00
USUD
7.92
14.96
17.57
16.93
0.48
0.42
1.78
0.64
mean
6.09
11.12
16.15
12.68
0.55
0.81
3.02
0.99
5 Conclusion
In this paper, the performance of QZSS L6D augmentation information is
evaluated, and uses the QZSS final orbit and clock products as references to
evaluate the augmentation effect of L6D signals. The results show that the L6D
augmentation information of QZSS can provide the augmentation service. After
the augmentation, the clock offset precision is about 0.46m, the radial average
precision is about 0.26m, the along-track precision is about 1.05m, the cross-track
precision is about 0.94m, the 3D precision is about 1.44m, and the SISURE
precision is about 0.62m. The static PPP positioning horizontal accuracy based on
QZSS L6D augmentation information is about 13cm and the vertical accuracy is
about 16cm, which still has a large error with the final precise ephemeris and
precise clock PPP positioning results of QZSS. Further research is needed on the
PPP-RTK performance of QZSS L6D augmentation information and the PPP
performance of L6E augmentation information.
Acknowledgments Thanks to the precise products and L6 products provided by QZSS officials,
the broadcast ephemeris data provided by IGS, and the station observation data provided by
MGEX. The author thanks International GNSS Monitoring and Assessment System (iGMAS) for
its support.This work is also supported by the National Science Foundation of China (41874041).

<!-- PAGE: 13 -->

12
References
1.
Quasi-Zenith Satellite System Performance Standard (PS-QZSS-001).Available from the
Following Site [OL].https://qzss.go.jp/en/technical/ps-is-qzss/ps_qzss_001_agree.html.
2.
Wang Guohui, Kuang Cuilin. Accuracy evaluation of real-time orbit and clock difference
data of QZSS michibiki satellite [J]. Journal of Surveying and Mapping Science and
technology, 2016,33 (04): 379-382.
3.
Choy, Suelynn & Harima, Ken & Li, Y. & Choudhury, Mazher & Rizos, Chris &
Wakabayashi, Y. & Kogure, Satoshi. (2014). High accuracy real-time precise point
positioning using the Japanese Quasi-Zenith satellite system LEX signal. CEUR
Workshop Proceedings. 1307.
4.
Lou, Yidong & Zheng, Fu & Gong, Xiaopeng & Shengfeng, Gu. (2016). Evaluation of
QZSS
system
augmentation
service performance in
China
region.
41.
298-303.
10.13203/j.whugis20140273.
5.
Zhang Wenfeng. GPS real-time precise single point positioning algorithm for satellite
based augmented signal [J]. Surveying and Mapping Science, 2018,43 (08): 62-67.
6.
Jiang Yongsheng. Analysis of the augmented effect of QZSS on GPS positioning [J].
Beijing surveying and mapping, 2019,33 (08): 969-973.
7.
Bu, Jinwei & Zuo, Xiaoqing & Li, Xiangxin & Chang, Jun & Zhang, Xionghao. (2018).
Evaluation and Analysis on Positioning Performance of BDS/QZSS Satellite Navigation
Systems
in
Asian-Pacific
Region.
Advances
in
Space
Research.
63.
10.1016/j.asr.2018.12.026.
8.
Odolinski, Robert & Teunissen, P. & Odijk, Dennis. (2014). Combined BDS, Galileo,
QZSS and GPS single-frequency RTK. GPS Solutions. 19. 10.1007/s10291-014-0376-6.
9.
Hiromune N , Osamu O , Nobuaki K , et al. Initial performance evaluation of centimeter-
class augmentation system using Quasi-Zenith Satellite System[J]. Electronics and
Communications in Japan, 2018.
10.
Zhang Shaocheng,Du Shikang,Li Wei,Wang Guangxing. Evaluation of the GPS Precise
Orbit and Clock Corrections from MADOCA Real-Time Products.[J]. Sensors (Basel,
Switzerland),2019,19(11).
11.
Po-Chun Chiu, Shuo-Ju Yeh , Shau-Shiun Jan.Performance Analysis of QZSS Centimeter
Level Augmentation Services (CLAS). Stanford PNT
2019, Stanford, California. http://
web.stanford.edu/group/scpnt/pnt/PNT19/presentation_files/S03-Po-Chun-QZSS-Augmen
tation.pdf.
View publication stats
