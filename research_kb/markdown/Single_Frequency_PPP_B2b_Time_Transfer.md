<!-- PAGE: 1 -->

Research on Single-Frequency
PPP-B2b Time Transfer
Zaimin He, Lan Li, Runzhi Zhang, Juan Hou, Gongwei Xiao, Wei Guang,
Jihai Zhang, and Xiangyi He
Time transfer based on global navigation satellite sys- common-view (CV), all-in-view (AV), and GNSS carrier
tem (GNSS) using precise point positioning (PPP) phase. Compared with CV and AV based on low-precision
is a critical technique in universal time coordinated pseudorange observations, GNSS carrier phase time transfer
(UTC) calculation. PPP relies on precise satellite orbit and has higher time transfer accuracy. It is realized by means of
satellite clock offset products obtained through network solu- PPP [1] which uses a single GNSS receiver to obtain precise
tions. Since August 2020, the Beidou global navigation satellite absolute coordinates. The GeoForschungZentrum (GFZ)
system (BDS-3) has provided GNSS users with the PPP prod- analysis center product GBM, whose accuracy can reach
uct using PPP-B2b signal through three geostationary earth 3 cm, can be obtained with a two-day delay. The STD value
orbit (GEO) satellites instead of a network in the Asia-Pacific of post-process PPP time transfer using the GBM product can
area. Network interruption will cause PPP reconvergence and reach 0.3 ns [2]. Since 2013, the IGS has provided users with
terminate the time transfer, which hinders the application of the precise satellite orbit and satellite clock offset products
PPP time transfer. The real-time PPP-B2b product broadcast by required by PPP for free via the networked transport of Ra-
GEO satellites can be considered to solve the problem of inter- dio Technical Commission for Maritime Services (RTCM) via
ruption caused by network fluctuation in the field of real-time internet protocol (NTRIP). Ge et al. analyzed real-time PPP
PPP. To promote the application of real-time PPP time com- time transfer [3]. Their results showed that real-time PPP
parison in UTC calculation and develop PPP-B2b application time transfer could achieve a 0.5 ns level. However, the real-
in time transfer, single-frequency (SF) PPP-B2b time trans- time PPP via the NTRIP protocol can be performed only in
fer is investigated. Meanwhile, the treatment of ionospheric smooth network environments. And network interruption
delay of SF PPP-B2b is crucial, and a GRAPHIC SF PPP-B2b causes instability in PPP time transfer relying on IGS prod-
model is proposed and validated in order to keep PPP-B2b net- ucts. Since August 2020, precise products called the PPP-B2b
work-independent. Data from two international atomic time product have been available through three GEO satellites in-
(TAI) time-keeping laboratories and two international GNSS stead of NTRIP protocol [4]. Presently, the research on the
service (IGS) stations were used to analyze the accuracy in PPP-B2b product focuses on product quality, positioning,
SF time comparison applications using the PPP-B2b product and DF time transfer [5],[6]. The DF time comparison using
from common clock difference (CCD) and long-baseline time the PPP-B2b product can reach an accuracy of sub-nano-
links. Results show that the SF PPP-B2b CCD sequences can be second. The price of the SF receiver has attracted more and
concentrated within 0.2 ns. The long-baseline time difference more researchers to study SF PPP time transfer. However, the
between SF time transfer using PPP-B2b product and dual-fre- PPP-B2b time transfer only verifies the feasibility of dual-
quency (DF) time transfer using the final product fluctuated frequency receiver, while the accuracy of time transfer of
within 2 ns. In addition, the standard deviation (STD) values single-frequency receiver is still blank. The advantages of SF
of PPP-B2b time comparison are mainly distributed at 0.5 ns. PPP-B2b time transfer receiver in cost and stability are begin-
Meanwhile, only BDS and BDS + GPS can achieve similar SF ning to be realized. The treatment of PPP ionospheric delay
PPP-B2b time transfer accuracy. is very tricky. For dual-frequency, the effect of ionospheric
delay can be eliminated by the frequency combination, while
Background single-frequency cannot directly eliminate the effect of ion-
The high-precision time scale can be generated and main- ospheric delay. Also, further PPP solution of the PPP-B2b
tained by the time-frequency system, and the high-precision product is independent of a network, so that the external in-
time transfer is an indispensable part of the time-frequency put of ionosphere is isolated. An analysis of performance of
system. Presently, GNSS time transfer mainly includes SF PPP-B2b time transfer is required.
42 IEEE Instrumentation & Measurement Magazine September 2023
1094-6969/23/$25.00©2023IEEE
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:15:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 2 -->

In this study, a new single-frequency PPP-B2b time transfer delays is called GRAPHIC [7]. Meanwhile, combining with
was investigated. Two TAI timekeeping laboratories, includ- broadcast ionospheric products such as the Beidou global
ing the National Time Service Center of the Chinese Academy broadcast ionospheric delay correction model (BDGIM) [8] to
of Sciences (NTSC) and the Telecommunication Laboratories replace IGS ionospheric products [9], constraining the iono-
(TL), external atomic clock IGS station (USUD) and an IGS sta- spheric delay in the pseudorange observation equation with
tion (CUSV) with an internal clock were selected to validate the broadcast ionosphere model, a new SF PPP-B2b time trans-
the accuracy of the PPP-B2b product in SF comparison appli- fer model was investigated. The ionosphere-free SF PPP-B2b
cations from zero-baseline CCD and long-baseline time links. model can be written as follows:
Method 

p r s _iono,j =µr s ⋅x+c⋅dtɶr+I r s ,j+T r s +εr s _iono,j
C
sa
u
te
rr
ll
e
i
n
te
t l
c
y
l
,
o
t
c
h
k
e
o
P
f
P
fs
P
e
-
t
B
c
2
o
b
r r
p
e
r
c
o
t
d
io
u
n
c t
o
p
f
r
n
o
a
v
v
i
i
d
g
e
a
s
t i
s
o
a
n
te
e
ll
p
it
h
e
e
o
m
r
e
b
r
i
i
t
s
a
f
n
o
d
r 

 l I s F,j =
p
r
s ,j+l
rr
s
,j =µr s ⋅x+c⋅dtɶr+T r s +λNɶ r s ,j+ξI s F,j
 2 (4)
BDS-3 and GPS users, respectively. 

Ions =I r s ,j+ζion

Precise Satellite Orbit
The rough satellite position which is calculated through the In (4), p r s iono j refers to pseudorange observation corrected us-
_ , s
broadcast ephemeris is corrected using the PPP-B2b product ing the differential code bias PPP-B2b product; µr denotes the
and (1) to obtain the precise satellite position: receiver-to-satellite unit vector; c is the speed of light in vac-
uum,
x
denotes the vector of receiver position increments;
dtɶr
X orbit X brdc δO R refers to the receiver clock offset in seconds; I r s j refers to the
  Y orbit   =   Y brdc   −[ e raadial� e along� e cross]⋅   δO A   (1) ionospheric delay in meters; T r s is the troposph , eric delay in
s
 Z orbit   Z brdc   δO C  m p r s e j t a er n s d ; ε l r s r _ j i r o e n f o e , r j r t e o f t e h rs e t r o a w th o e b p s s e e r u va d t o io ra n n s g m e i o n b u s s e t r h v e a t c i o o m n p n u oi t s e e d ;
In (1),  X orbit(cid:31) Y orbit(cid:31) Z orbit T represents the precise satellite posi- va , lues of t , he carrier phase and pseudorange; λNɶ r s ,j represents
p ti o on si t v i e o c n t o c r a ; l  c X u b la rd t c e (cid:31) Y d b r f d r c o (cid:31) Z m b r t d h c e  T e i p n h d e ic m at e e r s is t ; h [ e e r r a e d a ia l l -t i e m alo e n s g a t e e cr ll o i s t s e ] o th b e s e a r m va b t i i g o u n i t n y o i i n se m ; I e o t n e s r s d ; e ξ n I s o F , t j e s re i p o r n e o s s e p n h ts e r io ic n d o e sp la h y e r c i a c l - c f u re la e t e S d F
corresponds to the unit vectors which can be calculated as (2) from broadcast ephemeris; and ζion denotes broadcast ephem-
in radial, along-track, and cross-track directions, respectively; eris ionospheric measurement noise. Thus, the SF PPP-B2b
T
and δO Rδ(cid:31) O Aδ(cid:31) O C represents the orbit correction vector time transfer estimated parameter vector X is:
from the PPP-B2b product:
  e radial= r r X=  x dtɶr T r s I r s ,j λNɶ r s ,j   . (5)

 r×ν
 e cross= (2) Process and Strategies

r×ν
SF PPP using the PPP-B2b product is performed as shown


e
along
=e cross×e
radial in Fig. 1. Table 1 lists SF PPP-B2b processing strategies. The

PPP processing process is divided into data preparation, data
In (2), r and ν are the satellite position and velocity vectors of preprocessing, error correction, Kalman filtering and esti-
ephemeris. mation. Navigation ephemeris and the PPP-B2b product are
used to recover precise satellite orbit and clock offset, and
Precise Satellite Clock raw observations are also required for PPP calculation. Data
The precise satellite clock offset is obtained by correcting the preprocessing consists of gross error, clock slip detection rep-
satellite clock offset of ephemeris through the PPP-B2b prod- aration and cycle slip detection to provide pure raw data for
uct and (3): subsequent high-precision algorithms. Errors are processed
by models, empirical formulas and parameters estimated. The
C
dt p s rec =dt b s rdc− 0 (3) parameters estimated after Kalman filtering are verified by re-
c
sidual and the receiver clock offset can be obtained.
In (3), dt p s rec indicates the precise clock offset; dt b s rdc indicates
the satellite clock offset calculated from ephemeris; C indi- PPP Time Transfer
0
cates the clock correction provided by the PPP-B2b product in The receiver clock offset can be considered as time difference
meters; and c indicates the speed of light. between the receiver local time t loc and the GNSS reference
time t ref. The GNSS reference time of the two stations through
GRAPHIC SF PPP-B2b Model time transfer is eliminated by the difference, which is written
The biggest challenge for SF PPP is the treatment of iono- as (6):
spheric delay. Averaging SF pseudorange observations and
carrier phase observations to remove first-order ionospheric ∆t=dtɶr,1 −dtɶr,2 =(t loc,1 −t ref)−(t loc,2 −t ref)=t loc,1 −t loc,2 (6)
September 2023 IEEE Instrumentation & Measurement Magazine 43
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:15:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 3 -->

observations from two
GNSS receivers, named
BDS-3/GPS carrier phase and
PPP-B2b data stream Navigation ephemeris NTTS and NT07, with com-
pseudorange observations
mon antenna and external
clock. The observations
Precise satellites participating zero-baseline
orbit and clock CCD were used for 11 d
from day of year (DoY) 86
Gross error detection to 96 in 2022. The PPP-B2b
Data preprocessing Cycle slip detection
clock slip detection product binary files were
saved by the SINO K803 kit,
which was equipped with
PPP model and
error correction PPP-B2b raw binary receiv-
ing module. Moreover, three
time comparison long-base-
Kalman filtering
and estimation line links are formed. Fig. 2
shows their geographic lo-
cation. Table 2 lists detailed
Residual information of receivers.
PPP time comparison using
the GBM product is per-
greater than or equal formed as a reference.
Threshold
PPP-B2b CCD
less Fig. 3 and Fig. 4 illustrate
the receiver clock offset
Receiver clock
offset using GBM and PPP-B2b
products, respectively. The
receiver clock offset for time
Fig. 1. Procedure for data processing.
comparison using PPP is
incorporated into the prod-
Results and Discussion
uct reference time. Compared with GBM time comparison, the
The CCD [12],[13] experiment which is often selected to an- PPP-B2b product reference time contained in the receiver clock
alyze the noise level of time transfer is implemented with offset is continuous. As shown in Fig. 4, the receiver clock offset
acquired by only GPS time transfer using the PPP-B2b prod-
uct is intermittent. The GPS PPP-B2b product does not seem
Table 1 – SF PPP-B2b processing strategies
to maintain the satellite clock reference. Compared to the IGS
Item Strategies product obtained from the global observation network, the
System BDS, GPS
Estimator Kalman filter
Cutoff elevation 10° 60°N
Raw observations GPS: L1C/A; BDS: B3I
Sample interval 30 s 48°N
Satellite hardware delay PPP-B2b differential code bias
correction product NTSC
36°N USUD
Dry delay: corrected with
Saastamoinen model [10] 24°N TLM2
Tropospheric delay Wet delay: estimated as a
random walk noise CUSV
12°N
Mapping function: GMF [11]
Receiver antenna phase
Corrected by the “igs*.atx” file 0°
center 72°E 90°E 108°E
Longitude
Receiver clock offset Estimated as white noise
Phase ambiguity Estimated as float
44 IEEE Instrumentation & Measurement Magazine September 2023
edutitaL
126°E 144°E
Fig. 2. The geographic distribution of time comparison links stations.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:15:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 4 -->

Table 2 – Detailed information of time links receivers
Station/ID Organization Receiver Clock
SEPT
NTTS NTSC External
POLARX5
SEPT
NT07 NTSC External
POLARX5
SEPT
TLM2 TL External
POLARX5
SEPT External
USUD IGS
POLARX5 H-Maser
JAVAD TRE_3
CUSV IGS Internal
DELTA
–12
–14
–16
–18
–20
–22
086 088 090 092
DoY
PPP-B2b tracking stations are only in the territory of China. As
a result, it is apparent that the time comparison of BDS-3 and
BDS-3 + GPS PPP-B2b is better than that of a single GPS sys-
tem. The content of this study is mainly based on BDS-3 and
BDS-3 + GPS.
The zero-baseline CCD result is displayed in Fig. 5.
The CCD result sequence of SF PPP-B2b fluctuates within concentrated at 0.5 ns. Second, regardless of the three-time
0.2 ns. The STD value of the CCD result residuals was comparison long-baseline links of PPP-B2b, it could be ob-
calculated, and results showed that the addition of GPS served that the addition of GPS system did not improve the
system failed to improve the accuracy of SF PPP-B2b time accuracy of time comparison.
transfer.
Conclusions
Long-baseline PPP-B2b Time Comparison The emergence of the PPP-B2b product promotes the ap-
Taking the DF GBM time comparison as a reference, the dif- plication of real-time PPP in positioning in a networkless
ferences among the long-baseline time comparison results are occasion. Meanwhile, the PPP-B2b product broadcast by
shown in Fig. 6 and Fig. 7. Meanwhile, Table 3 lists the STD three GEO satellites solves the problem of interruption
values of the residuals. Combining Fig. 6, Fig. 7 and Table 3, caused by network fluctuation in the field of real-time PPP
two conclusions have been drawn. First, taking the GBM time time comparison. The treatment of ionospheric delay of SF
comparison as a reference, the PPP-B2b time comparison re- PPP-B2b is crucial, and a GRAPHIC SF PPP-B2b model is pro-
sidual for all three links fluctuated within 2 ns. Furthermore, posed and validated to keep PPP-B2b network-independent.
the receiver clock offset introduces the hardware delay which Considering that the PPP-B2b product serves GPS and BDS
led to a constant deviation in different time links. The STD users in the Asia-Pacific area, two TAI laboratories (NTSC,
values of the time comparison residual of SF PPP-B2b were TL), an external atomic clock station (USUD) and an IGS
September 2023 IEEE Instrumentation & Measurement Magazine 45
)sn(
tesffo
kcolC
15
12
9
6
3
0
086 088 090 092
094 096
Fig. 3. NTTS clock offset using the GBM product for 11 days from DoY 86 to
96 in 2022.
)sn(
tesffo
kcolC
094 096
12
9
6
3
0
–3
086 088 090 092
)sn(
tesffo
kcolC
094 096
–8
–12
–16
–20
–24
–28
–32
086 088 090 092
DoY
)sn(
tesffo
kcolC
094 096
Fig. 4. PPP-B2b NTTS clock offset (GPS + BDS-3, BDS-3, GPS from top to
bottom) for 11 days from DoY 86 to 96 in 2022.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:15:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 5 -->

as a reference to measure
–4.6 the accuracy of the time
–4.8 comparison using the PPP-
–5.0 B2b product. Compared
–5.2 with GBM time compar-
–5.4
ison, the reference time
–5.6
contained in the receiver
–5.8
clock offset using the PPP-
–6.0
B2b product is continuous.
–6.2
086 088 090 092 The receiver clock offset
DoY (300 s interval) through GPS time transfer
using the PPP-B2b product
is intermittent. Only GPS
SF PPP-B2b time compar-
ison is not recommended,
which is similar to DF
PPP-B2b time transfer.
The CCD result sequence
of SF PPP-B2b fluctuates
within 0.2 ns. Taking the
GBM product as a refer-
ence, the STD values of
SF PPP-B2b time compar-
ison using GRAPHIC SF
PPP-B2b model can be
0.5 ns. Meanwhile, the ad-
dition of GPS system does
not significantly improve
the PPP-B2b time transfer
accuracy.
Acknowledgment
The authors acknowledge
TL, IGS and GFZ for provid-
ing observations and precise
satellite orbit and clock
products. This research was
funded by the State Key
Laboratory of Geodesy and
Earth’s Dynamics (Grant
No. SKLGED2022-3-3).
References
[1] J. Zumberge et al, “Precise point positioning for the efficient and
robust analysis of GPS data from large networks,” J. Geophysical
Research-Solid Earth, vol. 102, pp. 5005–5017, Mar. 1997.
[2] J. H. Zhang, S. W. Dong, H. B. Yuan, W. Guang, Y. Zhang et al,
“Study on PPP time comparison based on BeiDou-3 new signal,”
IEEE Instrum. Meas. Mag., vol. 25, pp. 30–40, Aug. 2022.
[3] Y. L. Ge, S. X. Chen, T. Wu, C. M. Fan, W. J. Qin, F. Zhou and X.
H. Yang, “An analysis of BDS-3 real-time PPP: time transfer,
positioning, and tropospheric delay retrieval,” Measurement, vol.
station (CUSV) with an internal clock which were equipped 172, article 108871, Feb. 2021.
with BDS-3 and GPS receivers were selected to validate the [4] “BeiDou Navigation Satellite System Signal in Space Interface
SF PPP-B2b time comparison from NTSC zero-baseline CCD Control Document Precise Point Positioning Service Signal
and long-baseline time links. The GBM product was used PPP-B2b (Version 1.0),” China Satellite Navigation Office, Aug.
46 IEEE Instrumentation & Measurement Magazine September 2023
)sn(
ecnereffid
kcolC
GPS + BDS (STD = 0.0235) BDS (STD = 0.0296) – 0.2 ns
094 096
Fig. 5. PPP-B2b zero-baseline CCD for 11 days from DoY 86 to 96 in 2022.
16
12
8
4
0
–4
–8
–12
–16
166 167 168 169
DoY
)sn(
ecnereffid
kcolC
PPP-B2b SF TLM2 (–10 ns)
PPP-B2b SF USUD
PPP-B2b SF CUSV (–91 ns)
170 171 172
Fig. 6. BDS + GPS PPP-B2b time comparison residual.
16
12
8
4
0
–4
–8
–12
–16
166 167 168 169
DoY
)sn(
ecnereffid
kcolC
PPP-B2b SF TLM2 (–20 ns)
PPP-B2b SF USUD
PPP-B2b SF CUSV (–90 ns)
170 171 172
Fig. 7. BDS PPP-B2b time comparison residual.
Table 3 – STD values of PPP-B2b time comparison
residual (ns)
Time link Model
GPS + BDS BDS
NTSC-TLM2 0.4287 0.3995
NTSC-USUD 0.5028 0.5112
NTSC-CUSV 0.5328 0.5425
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:15:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 6 -->

2022. [Online]. Available: http://www.beidou.gov.cn/xt/ Runzhi Zhang (zhangrunzhi@ntsc.ac.cn) is currently working
gfxz/202008/P020200803362062482940.pdf. toward an M.S. degree in communication and information sys-
[5] J. Tao, J. N. Liu, Z. G. Hu, Q. L. Zhao, G. Chen and B. X. Ju, “Initial tem with National Time Service Center, Chinese Academy of
sssessment of the BDS-3 PPP-B2b RTS compared with the CNES Sciences, Xi'an, China. His main research fields are time trans-
RTS,” GPS Solutions, vol. 25, article 131, Jul. 2021. fer and high precision positioning. He received a B.E. degree in
[6] R. Z. Zhang, Z. M. He, L. M. Ma, G. W. Xiao, W. Guang et al, electronic information engineering from Yanshan University,
“Analysis of BDS-3 PPP-B2b positioning and time transfer Qinhuangdao, China in 2020.
service,” Remote Sensing, vol. 14, no. 12, article 2769, Apr. 2022.
[7] O. Montenbruck, “Kinematic GPS positioning of LEO satellites Juan Hou (hhoujuan@126.com) is an Engineer at Xi’an Univer-
using ionosphere-free single frequency measurements,” Aerospace sity of Posts and Telecommunications, Xi’an, Shaanxi, China.
Science and Technol., vol. 7, pp. 396–405, Jul. 2003. She received the M.S. degree from the University of Chinese
[8] Y. B. Yuan, N. B. Wang, Z. S. Li, X. L. Huo, “The BeiDou global Academy of Sciences in 2012. Her main research fields are in
broadcast ionospheric delay correction model (BDGIM) and its timekeeping techniques and the performance of atomic clocks.
preliminary performance evaluation results,” Navigation, vol. 66,
pp. 55–69, Jan. 2019. Gongwei Xiao (xiaogongwei@xupt.edu.cn) is a Lecturer with
[9] M. Hernandez-Pajares, J. M. Juan, J. Sanz, R. Orus, A. Garcia- the Xi’an University of Posts and Telecommunications, Xi’an,
Rigo et al, “The IGS VTEC maps: a reliable source of ionospheric Shaanxi, China. His current research mainly focuses on multi-
information since 1998,” J. Geodesy, vol. 83, pp. 263–275, Mar. GNSS PPP, real-time precise orbit determination for LEO
2009. satellites and tropospheric delay. He received the M.S. de-
[10] J. Saastamoinen, “Atmospheric correction for the troposphere and gree from the College of Geodesy and Geomatics, Shandong
the stratosphere in radio ranging satellites,” The Use of Artificial University of Science and Technology in 2018 and received
Satellites for Geodesy, vol. 15, pp. 247–251, Jan. 1972. the Ph.D. degree from State Key Laboratory of Geodesy and
[11] J. Boehm, A. Niell, P. Tregoning and H. Schuh, “Global Mapping Earth Dynamics, Innovation Academy for Precision Measure-
Function (GMF): a new empirical mapping function based on ment Science and Technology, Chinese Academy of Sciences
numerical weather model data,” Geophysical Research Letters, vol in 2021.
33, pp. 3–6, Apr. 2006.
[12] W. Guang, J. H. Zhang, H. B. Yuan, W. J. Wu and S. W. Dong, Wei Guang (weiguang@foxmail.com) is a Lecturer at the
“Analysis on the time transfer performance of BDS-3 signals,” School of Communications and Information Engineering and
Metrologia, vol. 57, article 065023 Oct. 2020. School of Artificial Intelligence, Xi’an University of Posts and
[13] W. Guang, S. W. Dong, W. J. Wu, J. H. Zhang, H. B. Yuan et al, Telecommunications, Xi’an, Shaanxi, China. He received the
“Progress of BeiDou time transfer at NTSC,” Metrologia, vol. 55, M.S. and Ph.D. degrees from University of Chinese Academy
pp. 175–187, Feb. 2018. of Sciences in 2012 and 2019, respectively. His main research
field is high performance time transfer.
Zaimin He (hezaimin@xupt.edu.cn) is a Professor at the School
of Communications and Information Engineering and School Jihai Zhang (zhangntsc@126.com) is a Research Associate at
of Artificial Intelligence, Xi’an University of Posts and Tele- the National Time Service Center of Chinese Academy of Sci-
communications, Xi’an, Shaanxi, China. He received the M.S. ences, Xi’an, Shaanxi, China. He received the M.S. degree in
and Ph.D. degrees from the University of Chinese Academy 2014 from the University of Chinese Academy of Sciences.
of Sciences in 2008 and 2012, respectively. His main research Now he is a Ph.D. student at the University of Chinese Acad-
fields are in radio positioning, timing, and communication. emy of Sciences. His main research fields are high precision
time transfer and GNSS time difference monitoring.
Lan Li (lilan@stu.xupt.edu.cn) is a graduate student at the
School of Communications and Information Engineering Xiangyi He (hexiangyiii@163.com) is a graduate student at
and School of Artificial Intelligence, Xi’an University of the School of Communications and Information Engineering
Posts and Telecommunications, Xi'an, Shaanxi, China. Her and School of Artificial Intelligence, Xi’an University of Posts
main research fields are high precision positioning and time and Telecommunications, Xi’an, Shaanxi, China. Her main
transfer. research fields are in GNSS, troposphere.
September 2023 IEEE Instrumentation & Measurement Magazine 47
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 07:15:28 UTC from IEEE Xplore. Restrictions apply.