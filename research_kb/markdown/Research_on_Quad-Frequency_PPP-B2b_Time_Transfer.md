<!-- PAGE: 1 -->

Research on Quad-Frequency
PPP-B2b Time Transfer
Runzhi Zhang, Lan Li, Xueqing Li, Hongjiao Ma, Gongwei Xiao, and Jihai Zhang
Carrier phase time transfer which is a crucial technique time transfer link. AV, on the other hand, addresses the dis-
in universal time coordinated (UTC) calculation tance limitation of CV. However, AV relies on low-precision
is implemented through precise point positioning pseudorange observations, resulting in reduced accuracy in
(PPP). Since August 2020, the Beidou global navigation sat- time transfer. GNSS carrier phase time transfer through PPP
ellite system (BDS-3) has provided users with the precise [1] has the highest accuracy among the three methods without
satellite product which is an essential external input in the distance limitation. Real-time PPP requires external provi-
PPP implementation, named the PPP-B2b product, through sion of real-time precise satellite orbit and satellite clock offset.
three geostationary earth orbit (GEO) satellites instead of a The GNSS analysis center provides precise satellite files for
network in the Asia-Pacific area. The PPP-B2b product can be researchers to study and verify PPP algorithms. The stan-
considered to solve the instability problem caused by network dard deviation (STD) value of post-process carrier phase time
interruption in traditional PPP time transfer. Currently, the transfer using the GBM product which is provided by The
fact that the PPP-B2b time transfer using dual-frequency (DF) GeoForschungZentrum (GFZ) analysis center with a two-day
ionosphere-free combination can achieve sub- nanosecond delay can reach 0.3 ns [2]. Moreover, since 2013, the inter-
accuracy has been proven. Considering the BDS-3 can pro- national GNSS service (IGS) has provided real-time precise
vide users with a wide range of frequency signals for PPP; satellite products via a network, contributing to the progress
meanwhile, the multi-frequency PPP will improve the ac- and development of PPP. PPP time transfer using the real-time
curacy of time transfer and accelerate the convergence. This product can achieve 0.5 ns accuracy [3]. However, the acqui-
improvement can be attributed to an increase in the number sition of precise product over a network not only introduces
of observation equations due to the utilization of multiple fre- limitations to real-time PPP, but also makes the time trans-
quencies. To promote the application of real-time PPP-B2b fer unstable because of network interruptions. To mitigate
time comparison in UTC calculation, a quad-frequency (QF) the impact of network interruptions on PPP time transfer, the
PPP-B2b time transfer model is proposed and investigated. BDS-3 has provided precise satellite products called the PPP-
Compared to DF PPP-B2b time transfer, the accuracy of the QF B2b product through three GEO satellites [4]. Compared with
time transfer model was verified from long-baseline time links another service broadcast by GEO satellites, satellite-based
and zero-baseline common clock difference (CCD). Results augmentation system (SBAS), the PPP-B2b product have
showed that the QF PPP-B2b time transfer had smoother CCD higher accuracy and shorter update intervals [5]. Currently, the
results and fluctuated within 0.1 ns, compared to the DF PPP- fact that DF PPP-B2b time transfer can reach sub- nanosecond
B2b model. Taking the PPP time comparison using the GBM accuracy has been proven [6],[7]. A highly reliable, network-
product as a reference, the results for all long-baseline links independent time transfer will be feasible, which has led to
show that the residuals of the QF PPP-B2b time comparison an increasing number of researchers to study the PPP-B2b
truly fluctuate within 1 ns. time transfer in terms of precision and stability. Given that the
BDS-3 can provide users with a wide range of frequency sig-
Background nals for PPP and the increased observation information will
Global navigation satellite system (GNSS) can provide real- accelerate PPP convergence and improve the accuracy of time
time positioning, navigation and time services for users transfer, QF PPP-B2b time transfer was studied.
worldwide. Currently, GNSS time transfer mainly includes In this study, a new QF PPP-B2b time transfer model
common-view (CV), all-in-view (AV), and GNSS carrier phase was investigated. To take full advantage of the BDS-3 fre-
time transfer. CV time transfer requires both users to observe quency signals to comprehensively assess the accuracy of QF
the same satellites, imposing limitations on the distance of the PPP-B2b time transfer model, the BDS-3 newly broadcasted
February 2024 IEEE Instrumentation & Measurement Magazine 57
1094-6969/24/$25.00©2024IEEE
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 2 -->

signals (B1C and B2a) were used alongside the existing B1I of 299792458 m/s. I denote ionospheric delay and T refers
and B3I signals. To ensure the reliability of the results, taking to tropospheric delay. dt r and dts denote receiver clock off-
the GBM product as a reference, the accuracy of QF PPP-B2b set and satellite clock offset, respectively. d and b refer to UCD
time transfer was verified from long-baseline time links and and uncalibrated phase delay (UPD), respectively. N refers to
zero-baseline CCD. The QF PPP-B2b time transfer calcula- the integer ambiguity. ε and ξ denote the noise in observation
tion involved several stations, including two international measurement. Table 1 lists the main errors and error process-
atomic time (TAI) keeping laboratories, namely the Telecom- ing strategies of PPP.
munication Laboratories (TL) and the National Time Service
Center (NTSC), as well as an external atomic clock IGS sta- Quad-Frequency PPP-B2b Model
tion (USUD). For convenience, (3) is defined, and f denotes frequency value
involved in the calculation. α and β are DF ionospheric-free
Method (IF) combination coefficient:
Real-time precise satellite position and satellite clock offset f i 2 f j 2
can be obtained using ephemeris and the PPP-B2b product [4]. αij = ,βij =− (3)
Moreover, the PPP-B2b product also provides PPP user with
f
i
2 −f
j
2 f
i
2 −f
j
2
differential code bias product to correct uncalibrated code de- Considering that the navigation signals provided by the
lay (UCD) in pseudorange observation equation. BDS-3 include B1I, B3I, B1C, and B2a which are numbered as
2, 6, 1, and 5, a quad-frequency PPP-B2b time transfer model is
PPP Model developed. Meanwhile, a B3I hardware delay is introduced by
PPP is an absolute positioning technology that achieves the BDS-3 PPP-B2b clock product, which can be written as (4)
high-precision positioning through models, empirical for- and corrected using the PPP-B2b differential code bias prod-
mulas, and parameter estimation methods to process errors, uct. After correcting the B3I hardware delay, the QF PPP-B2b
employing a single receiver to receive GNSS satellite signals model can be expressed as (5) and (6):
to obtain the raw carrier phase and pseudorange observa-
tions. The basic PPP observation equations can be written as c⋅dt B s 2b =c⋅dts +c⋅d 6 s (4)
(1) and (2):
(cid:22) Ps (cid:31)(cid:27)(cid:30)c(cid:29)dt (cid:30)Ts(cid:28)c(cid:29)dts (cid:30)(cid:26)s
Ls r,j = P r ρ s ,j + = c ρ (d + t r c − (d d t t r s − ) + dt T s r s ) + − T I r s r s ,j + + I λ r s , j s j ( + N c r s ( , d j r s + ,j b − r s , d j s j − ) b + s j ε ) r s + ,j ξ r s ,j ( ( 1 2 ) ) (cid:21) (cid:20) (cid:20) (cid:20) (cid:20) (cid:20) Ls r, P IF r s 2 , 6 IF r 1 (cid:31) 5 ,I (cid:27) F (cid:31) 26 (cid:30) (cid:27) c (cid:30) (cid:29)d c t (cid:29) r d ,I t F rr 2 , 6 IF r (cid:30) 26 ,I T F (cid:30) r 2 ss 6 (cid:25) (cid:28) is c b (cid:29) (cid:30) r dt T B s r s 2b (cid:28) (cid:30) c (cid:29) B (cid:24) d 2 N t b B s r s 2 , b IF (cid:30) r 2 , 6 (cid:26) IF (cid:30) r 2 s 6 , (cid:23) IF r s 1 , 5 IF 26 (5)
in which L and P denote raw carrier phase and pseudorange (cid:19) (cid:20)Ls r,IF 15 (cid:31)(cid:27)(cid:30)c(cid:29)dt r,IF 26 (cid:30)T r s(cid:28)c(cid:29)ddt B s 2b (cid:30)(cid:24)N r s ,IF 15 (cid:30)(cid:23) r s ,IF 26
observations obtained directly through the receiver, respec-
tively. j is frequency numbering of observation. ρ refers to the    c⋅dt r,IF 26 =c⋅dt r+α26 d r s ,2+β26 d r s ,6 (6)
geometric distance from receiver r to satellite s. c is a constant  θisb=α15 d r s ,1+β15 d r s ,5−α226 d r s ,2−β26 d r s ,6
ρ=ρ0+µr s ⋅∆x (7)
Er T r a o b rs le 1 – Errors and Processing St S ra tr t a e t g eg ie ie s s of PPP and I n ca ( r 5 r ) i , e P r r s , p IF h ij a a s n e d o L b s r s , e IF r ij v r a e t f i e o r n t s o a th t f e r c e o q m ue b n in ci e e d s i I F a n p d se j u a d ft o e r r a c n o g r e -
Satellite orbit PPP-B2b orbit products recting UCD using the PPP-B2b product, respectively. λN
Satellite clock PPP-B2b clock products denotes the floating ambiguity. ρ can be linearized. ρ0 refers
UCD PPP-B2b products to the geometric distance using the last estimated receiver co-
ordinates. µr s denotes the unit vector between receiver r to
Model [8],[9] and parameter
Tropospheric delay satellite s. Δx refers to the receiver coordinates vector incre-
estimation ments. Therefore, after correcting satellite clock offset dt B s 2b
Model [10] or parameter
Ionospheric delay through the PPP-B2b product, the QF PPP-B2b time transfer
estimation estimated parameter vector X is:
Phase wind-up Model [11]
Relativistic effect Model [12] X=  ∆x dt r,IF 26 T r s θisb λN r s ,IF 26 λN r s ,IF 15   . (8)
Satellite and receiver
“atx” file provided by IGS
antenna phase center
PPP-B2b Time Transfer
Receiver coordinates Parameter estimation
The principle of time transfer using the PPP-B2b product
Receiver clock Parameter estimation
is shown as Fig. 1. Fig. 2 illustrates a simplified PPP pro-
Phase ambiguity Parameter estimation
cessing workflow. Meanwhile, Table 2 lists QF PPP-B2b
58 IEEE Instrumentation & Measurement Magazine February 2024
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 3 -->

time transfer processing strategies. As far as the acquisition
of precise products is concerned, GEO satellites are used Ephemeris and
Data Preparation Raw observations
PPP-B2b products
in PPP-B2b time transfer instead of a network to broad-
cast real-time data, compared to the traditional PPP time
Data Preprocessing
transfer. The receiver clock offset obtained by PPP is the de-
viation of the local time t loc compared to the GNSS reference Models and
time t ref. The time links involved in time transfer eliminate Empirical Formulas
the GNSS reference time t ref through receiver clock offset
Parameter
difference to achieve high precision time transfer, which is Estimation
written as:
Receiver Clock
Offset
∆t=dt r,A−dt r,B= (t loc,A−t ref ) − (t loc,B−t ref ) =t loc,A−t loc,B (9)
Fig. 2. Simplified PPP processing flow.
Results and Discussion
Table 2 – QF PPP-B2b time comparison strategies
The zero-baseline CCD [13],[14] experiment can reflect the
Item Strategies
noise level of time transfer. The receivers involved in the
zero-baseline time transfer are linked to a shared GNSS an- Navigation system BDS-3
tenna, and the baseline length is set to zero. QF PPP-B2b Raw observations B1C, B2a, B1I, B3I
model was validated by zero-baseline CCD and long- Ephemeris and the PPP-B2b
Satellite orbit and clock
baseline time links. Fig. 3 shows geographic location of two product
long-baseline time links, and Table 3 lists information of re- Estimator Kalman filter
ceivers involved in zero-baseline CCD and long-baseline Processing interval 300 s
time links. NTSC and TL are TAI timekeeping laboratories,
Corrected: the PPP-B2b
while IGS station USUD simply uses an external atomic Pseudorange UCD
product
clock as the clock source for the GNSS receiver. GNSS re-
Dry delay: Saastamoinen
ceivers, TLM2, NTTS and NT07, are connected to the
model [8];
UTC(k). Taking time comparison using the GBM prod-
Wet delay: estimated as a
uct as a reference, QF and DF PPP-B2b time comparison Tropospheric delay
random walk noise;
were implemented to verify the improvement of PPP-B2b
GMF model [9] is used as the
time transfer accuracy by increasing frequency. The ob-
mapping function.
servations participating zero-baseline CCD were used for
Receiver clock Estimated: white noise
12 d from day of year (DoY) 85 to 96 in 2022, while those
Receiver coordinates Estimated: constants (static)
from DoY 163 to 171 in 2022 were used for long-baseline
Phase ambiguity Estimated: floating point
time comparison. Observations can be obtained through
GEO Satellite
BDS-3 Satellites
dt
r,A
Station A
Station B
dt
r,B
Fig. 1. Principle of PPP-B2b time transfer.
February 2024 IEEE Instrumentation & Measurement Magazine 59
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 4 -->

https://cddis.nasa.gov/, and the PPP-B2b product can be PPP-B2b CCD
buffered by a NovAtel OEM729 receiver equipped with a The result of zero-baseline CCD between NTTS and NT07
PPP-B2b module. with a common antenna and external clock using QF and DF
PPP-B2b model was displayed in Fig. 4. The STD value of
the CCD result was calculated. The satellite products are the
60˚N
same in PPP solution, and only the processing model is dif-
ferent. Ideally the CCD result should be a horizontal line,
but the presence of noise makes the result sequence fluctu-
48˚N
ate. The smoothness of the curve reflects the level of PPP-B2b
model noise. Results show that QF PPP-B2b time transfer has
NTSC
36˚N USUD smoother CCD results and fluctuates within 0.1 ns, compared
to the DF PPP-B2b model.
24˚N TLM2
Long-baseline PPP-B2b Time Comparison
12˚N Fig. 5 displays the results of the QF NTSC-TLM2 PPP-B2b
time comparison from DoY 163 to 171 in 2022. The results of
0˚ the time comparison reflect the TAI retention of the NTSC
72˚E 90˚E 108˚E
Longitude and TL laboratories. Certainly, the time comparison link er-
ror mainly contains the local receiver clock error and PPP
solution error with precise satellite products and models.
Taking the GBM PPP time comparison as a reference, the
time transfer result difference is shown in Fig. 6 and Fig. 7.
Meanwhile, Table 4 lists the STD values of the residuals. The
fluctuation of the curve reflects the time comparison error of
different PPP-B2b models. Whether NTSC-TLM2 or NTSC-
USUD time link, QF has some improvement in accuracy
and the residuals of time comparison really fluctuate within
1 ns. Compared with the DF PPP-B2b time transfer, the STD
value of the long-baseline time comparison using QF PPP-
B2b time transfer model is improved from 0.25 ns to 0.2 ns.
The truth that the QF PPP-B2b model makes the time error of
the stations involved in the time comparison within 1 ns can
be demonstrated.
60 IEEE Instrumentation & Measurement Magazine February 2024
edutitaL
126˚E 144˚E
Fig. 3. The geographic distribution of time comparison links stations.
Table 3 – Detailed information of time links receivers
Station/ GNSS
Organization Clock
ID Receiver
SEPT
NTTS NTSC EXTERNAL
POLARX5
SEPT
NT07 NTSC EXTERNAL
POLARX5
SEPT
TLM2 TL EXTERNAL
POLARX5
SEPT EXTERNAL
USUD IGS
POLARX5 H-MASER
–6.6
–6.8
–7.0
–7.2
086 088 090
DoY (300 s interval)
)sn(
ecnereffid
kcolC
QF PPP-B2b (STD = 0.0191)
DF PPP-B2b (STD = 0.0239)
092 094 096
Fig. 4. QF and DF PPP-B2b zero-baseline CCD.
–122
–123
–124
–125
–126
164 166 168
DoY
)sn(
ecnereffid
kcolC
NTSC-TLM2 QF PPP-B2b
170 172
Fig. 5. QF PPP-B2b long-baseline time comparison for 9 d from DoY 163 to 171 in 2022.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 5 -->

2.0 B2a signals of BDS-3 were
1.5 used alongside existing B1I
1.0 and B3I signals. The results
0.5 showed that QF PPP-B2b
0.0
time transfer had smoother
–0.5
CCD results and fluctuated
–1.0
within 0.1 ns, compared
–1.5
–2.0 to the DF PPP-B2b model.
164 166 168
In the NTSC-TLM2 long-
DoY
baseline time comparison
experiment, the QF PPP-
B2b time comparison
residuals fluctuate within
1 ns. Meanwhile, taking
the GBM PPP time trans-
fer as a reference, whether
NTSC-TLM2 or NTSC-
USUD long-baseline time
link, QF has some improve-
ment in accuracy and the
residuals of time compari-
son really fluctuate within
1 ns. According to the STD
values calculated, QF has
a significant improvement
compared to DF PPP-B2b
time transfer. In conclusion, the truth that the QF PPP-B2b
model makes the time error of the stations involved in time
comparison within 1 ns can be demonstrated.
Acknowledgment
The authors acknowledge TL, IGS and GFZ for providing ob-
servations and precise satellite orbit and clock products. This
research was funded by the State Key Laboratory of Geodesy
and Earth Dynamics (Grant No. SKLGED2022-3-3).
Conclusions
PPP time transfer accuracy can reach sub-nanosecond without References
limitations on distance. Conversely, PPP execution requires [1] J . Zumberge et al., “Precise point positioning for the efficient
the external provision of real-time precise satellite products. and robust analysis of GPS data from large networks,” J.
Since August 2020, BDS-3 has provided precise products called Geophysical Research-solid Earth, vol. 102, pp. 5005–5017, Mar.
the PPP-B2b product through three GEO satellites instead of a 1997.
network, which solves the problem of interruption caused by [2] J . H. Zhang, S. W. Dong, H. B. Yuan, W. Guang, Y. Zhang et al.,
network fluctuation in the field of real-time PPP time compar- “Study on PPP time comparison based on BeiDou-3 new signal,”
ison. The truth that BDS-3 DF PPP-B2b time transfer can reach IEEE Instrum. Meas. Mag., vol. 25, pp. 30–40, Aug. 2022.
an accuracy of sub-nanosecond has been proven. Considering [3] Y . L. Ge, S. X. Chen, T. Wu, C. M. Fan,
the BDS-3 can provide users with a wide range of frequency W. J. Qin, F. Zhou and X. H. Yang, “An analysis of BDS-3 real-time
signals for PPP and the increasing observation information PPP: time transfer, positioning, and tropospheric delay retrieval,”
will accelerate the PPP convergence and improve the accuracy Measurement, vol. 172, 108871, Feb. 2021.
of time transfer, the QF PPP-B2b time transfer was studied. [4] “ BeiDou navigation satellite system signal in space interface
A QF PPP-B2b time transfer model was proposed and val- control document precise point positioning service signal
idated from zero-baseline CCD and long-baseline time links. PPP-B2b (version 1.0),” China Satellite Navigation Office,
To ensure the accuracy of the results, two TAI keeping labora- Aug. 2022. [Online]. Available: http://www.beidou.gov.cn/xt/
tories (NTSC and TL) and the IGS external atomic clock station gfxz/202008/P020200803362062482940.pdf.
(USUD) in the Asia-Pacific region were selected. To make full [5] Y. X. Yang, Q. Ding, W. G. Gao, J. L. Li, Y. Y. Xu, B. J. Sun,
use of the BDS-3 frequency signals to verify the accuracy of QF “Principle and performance of BDSBAS and PPP-B2b of BDS-3,”
PPP-B2b time transfer model, the newly broadcasted B1C and Satellite Navigation, vol. 3, 2022.
February 2024 IEEE Instrumentation & Measurement Magazine 61
)sn(
ecnereffid
kcolC
QF PPP-B2b
DF PPP-B2b
170 172
Fig. 6. Difference time sequences of NTSC-TLM2 PPP time comparison results using the GBM product and the PPP-B2b
product.
25
24
23
22
21
20
19
18
17
164 166 168
DoY
)sn(
ecnereffid
kcolC
QF PPP-B2b
DF PPP-B2b
170 172
Fig. 7. Difference time sequences of NTSC-USUD PPP time comparison results using the GBM product and the PPP-B2b
product.
Table 4 – STD values of PPP-B2b time comparison
residual
Model
Time link
QF PPP-B2b DF PPP-B2b
NTSC-TLM2 0.161 0.215
NTSC-USUD 0.201 0.255
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 6 -->

[6] R. Z. Zhang, Z. M. He, L. M. Ma, G. W. Xiao, W. Guang et al., School of Artificial Intelligence, Xi’an University of Posts and
“Analysis of BDS-3 PPP-B2b positioning and time transfer Telecommunications, Xi’an, China. Her main research fields
service,” Remote Sensing, vol. 14, no. 12, 2769, Apr. 2022. are high precision positioning and time transfer.
[7] J. Tang, D. Q. Lyu, F. L. Zeng, Y. L. Ge, R. Z. Zhang,
“Comprehensive analysis of PPP-B2b service and its impact on Xueqing Li (lixueqing@ntsc.ac.cn) is currently working
BDS-3/GPS real-time PPP time transfer,” Remote Sensing, vol. 14, toward an M.S. degree in communication and information sys-
no. 21, 5366, Nov. 2022. tem with the National Time Service Center, Chinese Academy
[8] J. Saastamoinen, “Atmospheric correction for the of Sciences, Xi’an, China. Her research interests include satel-
troposphere and the stratosphere in radio ranging Satellites,” lite network security and information security. She received
The Use of Artificial Satellites for Geodesy, vol. 15, pp. 247–251, her B.E. degree in computer science and technology from Qufu
Jan. 1972. Normal University, Rizhao, China in 2020.
[9] J. Boehm, A. Niell, P. Tregoning and H. Schuh, “Global mapping
function (GMF): a new empirical mapping function based on Hongjiao Ma (mahj@ntsc.ac.cn) received a Ph.D. degree in
numerical weather model data,” Geophysical Research Letters, astrometry and celestial mechanics with National Time Ser-
vol. 33, pp. 3–6, Apr. 2006. vice Center, Chinese Academy of Sciences, Xi’an, China. His
[10] M. Deo, A. El-Mowafy, “Triple-frequency GNSS models for PPP main research fields are time transfer and high precision
with float ambiguity estimation: performance comparison using positioning.
GPS,” Survey Review, vol. 50, pp. 249–261, 2018.
[11] J. T. Wu, S. C. Wu, G. A. Hajj, W. I. Bertiger, S. M. Lichten, “Effects Gongwei Xiao (xiaogongwei@xupt.edu.cn) is a Lecturer
of antenna orientation on GPS carrier phase,” Manuscripta with the Xi’an University of Posts and Telecommunications,
Geodaetica, vol. 18, pp. 91–98, 1993. Xi’an, China. His current research focuses on multi-GNSS
[12] P. Heroux, J. Kouba, “GPS precise point positioning using IGS PPP, real-time precise orbit determination for LEO satellites
orbit products,” Physics and Chemistry of the Earth, Part A: Solid and tropospheric delay. To meet the demands of research
Earth and Geodesy, vol. 26, pp. 573–578, 2001. and precise point positioning (PPP) in a multi-GNSS envi-
[13] W. Guang, J. H. Zhang, H. B. Yuan, W. J. Wu and S. W. Dong, ronment, he open-sourced a GNSS data processing software
“Analysis on the time transfer performance of BDS-3 signals,” named MG-APP (https://geodesy.noaa.gov/gps-toolbox/;
Metrologia, vol. 57, 065023, Oct. 2020. https://github.com/xiaogongwei/MG_APP). He received
[14] W. Guang, S. W. Dong, W. J. Wu, J. H. Zhang, H. B. Yuan et al., the M.S. degree from the College of Geodesy and Geomatics,
“Progress of BeiDou time transfer at NTSC,” Metrologia, vol. 55, Shandong University of Science and Technology in 2018 and
pp. 175–187, Feb. 2018. earned a Ph.D. degree from State Key Laboratory of Geod-
esy and Earth Dynamics, Innovation Academy for Precision
Runzhi Zhang (zhangrunzhi@ntsc.ac.cn, corresponding au- Measurement Science and Technology, Chinese Academy of
thor) is pursuing a Ph.D. degree at Key Laboratory of Precision Sciences in 2021.
Navigation and Timing Technology, National Time Service
Center (NTSC), Chinese Academy of Sciences, Xi’an, China. Jihai Zhang (zhangntsc@126.com) is a Research Associate
His main research fields are time transfer and high precision at the National Time Service Center of Chinese Academy
positioning. He received an M.S. degree in communication of Sciences, Xi’an, China and is working towards is Ph.D.
and information systems from the NTSC in 2023. degree. His main research fields are high precision time
transfer and GNSS time difference monitoring. He received
Lan Li (lilan@stu.xupt.edu.cn) is a graduate student at the the M.S. degree in 2014 from University of Chinese Academy
School of Communications and Information Engineering and of Sciences.
62 IEEE Instrumentation & Measurement Magazine February 2024
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore. Restrictions apply.