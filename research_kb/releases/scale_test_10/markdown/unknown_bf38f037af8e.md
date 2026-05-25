<!-- PAGE: 1 -->

February 2024	
IEEE Instrumentation & Measurement Magazine	
57
1094-6969/24/$25.00©2024IEEE
Research on Quad-Frequency  
PPP-B2b Time Transfer
Runzhi Zhang, Lan Li, Xueqing Li, Hongjiao Ma, Gongwei Xiao, and Jihai Zhang
C
arrier phase time transfer which is a crucial technique 
in universal time coordinated (UTC) calculation 
is implemented through precise point positioning 
(PPP). Since August 2020, the Beidou global navigation sat-
ellite system (BDS-3) has provided users with the precise 
satellite product which is an essential external input in the 
PPP implementation, named the PPP-B2b product, through 
three geostationary earth orbit (GEO) satellites instead of a 
network in the Asia-Pacific area. The PPP-B2b product can be 
considered to solve the instability problem caused by network 
interruption in traditional PPP time transfer. Currently, the 
fact that the PPP-B2b time transfer using dual-frequency (DF) 
ionosphere-free combination can achieve sub-­nanosecond 
­accuracy has been proven. Considering the BDS-3 can pro-
vide users with a wide range of frequency signals for PPP; 
meanwhile, the multi-frequency PPP will improve the ac-
curacy of time transfer and accelerate the convergence. This 
improvement can be attributed to an increase in the number 
of observation equations due to the utilization of multiple fre-
quencies. To promote the application of real-time PPP-B2b 
time comparison in UTC calculation, a quad-frequency (QF) 
PPP-B2b time transfer model is proposed and investigated. 
Compared to DF PPP-B2b time transfer, the accuracy of the QF 
time transfer model was verified from long-baseline time links 
and zero-baseline common clock difference (CCD). Results 
showed that the QF PPP-B2b time transfer had smoother CCD 
results and fluctuated within 0.1 ns, compared to the DF PPP-
B2b model. Taking the PPP time comparison using the GBM 
product as a reference, the results for all long-baseline links 
show that the residuals of the QF PPP-B2b time comparison 
truly fluctuate within 1 ns.
Background
Global navigation satellite system (GNSS) can provide real-
time positioning, navigation and time services for users 
worldwide. Currently, GNSS time transfer mainly includes 
common-view (CV), all-in-view (AV), and GNSS carrier phase 
time transfer. CV time transfer requires both users to observe 
the same satellites, imposing limitations on the distance of the 
time transfer link. AV, on the other hand, addresses the dis-
tance limitation of CV. However, AV relies on low-precision 
pseudorange observations, resulting in reduced accuracy in 
time transfer. GNSS carrier phase time transfer through PPP 
[1] has the highest accuracy among the three methods without 
distance limitation. Real-time PPP requires external provi-
sion of real-time precise satellite orbit and satellite clock offset. 
The GNSS analysis center provides precise satellite files for 
researchers to study and verify PPP algorithms. The stan-
dard deviation (STD) value of post-process carrier phase time 
transfer using the GBM product which is provided by The 
GeoForschungZentrum (GFZ) analysis center with a two-day 
delay can reach 0.3 ns [2]. Moreover, since 2013, the inter-
national GNSS service (IGS) has provided real-time precise 
satellite products via a network, contributing to the progress 
and development of PPP. PPP time transfer using the real-time 
product can achieve 0.5 ns accuracy [3]. However, the acqui-
sition of precise product over a network not only introduces 
limitations to real-time PPP, but also makes the time trans-
fer unstable because of network interruptions. To mitigate 
the impact of network interruptions on PPP time transfer, the 
BDS-3 has provided precise satellite products called the PPP-
B2b product through three GEO satellites [4]. Compared with 
another service broadcast by GEO satellites, satellite-based 
augmentation system (SBAS), the PPP-B2b product have 
higher accuracy and shorter update intervals [5]. Currently, the 
fact that DF PPP-B2b time transfer can reach sub-­nanosecond 
accuracy has been proven [6],[7]. A highly reliable, network-
independent time transfer will be feasible, which has led to 
an increasing number of researchers to study the PPP-B2b 
time transfer in terms of precision and stability. Given that the 
BDS-3 can provide users with a wide range of frequency sig-
nals for PPP and the increased observation information will 
accelerate PPP convergence and improve the accuracy of time 
transfer, QF PPP-B2b time transfer was studied.
In this study, a new QF PPP-B2b time transfer model 
was investigated. To take full advantage of the BDS-3 fre-
quency signals to comprehensively assess the accuracy of QF 
PPP-B2b time transfer model, the BDS-3 newly broadcasted 
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore.  Restrictions apply.

<!-- PAGE: 2 -->

signals (B1C and B2a) were used alongside the existing B1I 
and B3I signals. To ensure the reliability of the results, taking 
the GBM product as a reference, the accuracy of QF PPP-B2b 
time transfer was verified from long-baseline time links and 
zero-baseline CCD. The QF PPP-B2b time transfer calcula-
tion involved several stations, including two international 
atomic time (TAI) keeping laboratories, namely the Telecom-
munication Laboratories (TL) and the National Time Service 
Center (NTSC), as well as an external atomic clock IGS sta-
tion (USUD).
Method
Real-time precise satellite position and satellite clock offset 
can be obtained using ephemeris and the PPP-B2b product [4]. 
Moreover, the PPP-B2b product also provides PPP user with 
differential code bias product to correct uncalibrated code de-
lay (UCD) in pseudorange observation equation.
PPP Model
PPP is an absolute positioning technology that achieves 
high-precision positioning through models, empirical for-
mulas, and parameter estimation methods to process errors, 
employing a single receiver to receive GNSS satellite signals 
to obtain the raw carrier phase and pseudorange observa-
tions. The basic PPP observation equations can be written as 
(1) and (2):
	
P
c dt
dt
T
I
c d
d
r j
s
r
s
r
s
r j
s
r j
s
j
s
r j
s
,
,
,
,
=
+
−
(
)+
+
+
−
(
) +
ρ
ε
	
(1)
  L
c dt
dt
T
I
N
b
b
r j
s
r
s
r
s
r j
s
j
s
r j
s
r j
s
j
s
r j
s
,
,
,
,
,
=
+
−
(
)+
−
+
+
−
(
)+
ρ
λ
ξ
	 (2)
in which L and P denote raw carrier phase and pseudorange 
observations obtained directly through the receiver, respec-
tively. j is frequency numbering of observation. ρ refers to the 
geometric distance from receiver r to satellite s. c is a constant 
of 299792458 m/s. I denote ionospheric delay and T refers 
to tropospheric delay. dtr and dts denote receiver clock off-
set and satellite clock offset, respectively. d and b refer to UCD 
and uncalibrated phase delay (UPD), respectively. N refers to 
the integer ambiguity. ε and ξ denote the noise in observation 
measurement. Table 1 lists the main errors and error process-
ing strategies of PPP.
Quad-Frequency PPP-B2b Model
For convenience, (3) is defined, and f denotes frequency value 
involved in the calculation. α and β are DF ionospheric-free 
(IF) combination coefficient:
	
α
β
ij
i
i
j
ij
j
i
j
f
f
f
f
f
f
=
−
= −
−
2
2
2
2
2
2
,
	
(3)
Considering that the navigation signals provided by the 
BDS-3 include B1I, B3I, B1C, and B2a which are numbered as 
2, 6, 1, and 5, a quad-frequency PPP-B2b time transfer model is 
developed. Meanwhile, a B3I hardware delay is introduced by 
the BDS-3 PPP-B2b clock product, which can be written as (4) 
and corrected using the PPP-B2b differential code bias prod-
uct. After correcting the B3I hardware delay, the QF PPP-B2b 
model can be expressed as (5) and (6):
	
c dt
c dt
c d
B b
s
s
s
⋅
= ⋅
+ ⋅
2
6	
(4)
	
	
 
P
c dt
T
c dt
P
c dt
r IF
s
r IF
r
s
B b
s
r IF
s
r IF
s
,
,
,
,
26
26
26
15
2

 

 


 



r IF
isb
r
s
B b
s
r IF
s
r IF
s
r IF
r
T
c dt
L
c dt
T
,
,
,
,
26
15
26
26
2


 


 




s
B b
s
r IF
s
r IF
s
r IF
s
r IF
r
s
c dt
N
L
c dt
T
c
 



 

 
2
26
26
15
26



,
,
,
,
dt
N
B b
s
r IF
s
r IF
s
2
15
26













,
,
	 (5)
	
c dt
c dt
d
d
d
d
r IF
r
r
s
r
s
isb
r
s
r
s
⋅
= ⋅
+
+
=
+
−
,
,
,
,
,
26
26
2
26
6
15
1
15
5
α
β
θ
α
β
α26
2
26
6
d
d
r
s
r
s
,
,
−



β
	
(6)
	
ρ
ρ
µ
=
+
⋅
0
r
s
x
∆	
(7)
In (5), Pr IF
s
ij
,
 and Lr IF
s
ij
,
 refer to the combined IF pseudorange 
and carrier phase observations at frequencies i and j after cor-
recting UCD using the PPP-B2b product, respectively. λ N 
denotes the floating ambiguity. ρ can be linearized. ρ0 refers 
to the geometric distance using the last estimated receiver co-
ordinates. µr
s denotes the unit vector between receiver r to 
satellite s. Δx refers to the receiver coordinates vector incre-
ments. Therefore, after correcting satellite clock offset dtB b
s
2
through the PPP-B2b product, the QF PPP-B2b time transfer 
estimated parameter vector X is:
	
X
x
dt
T
N
N
r IF
r
s
isb
r IF
s
r IF
s
= 



∆
,
,
,
.
26
26
15
θ
λ
λ
	
(8)
PPP-B2b Time Transfer
The principle of time transfer using the PPP-B2b product 
is shown as Fig. 1. Fig. 2 illustrates a simplified PPP pro-
cessing workflow. Meanwhile, Table 2 lists QF PPP-B2b 
Table 1 – Errors and Processing Strategies of PPP
Errors
Strategies
Satellite orbit
PPP-B2b orbit products
Satellite clock
PPP-B2b clock products
UCD
PPP-B2b products
Tropospheric delay
Model [8],[9] and parameter 
estimation
Ionospheric delay
Model [10] or parameter 
estimation
Phase wind-up
Model [11]
Relativistic effect
Model [12]
Satellite and receiver 
antenna phase center
“atx” file provided by IGS
Receiver coordinates
Parameter estimation
Receiver clock
Parameter estimation
Phase ambiguity
Parameter estimation
58	
IEEE Instrumentation & Measurement Magazine	
February 2024
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore.  Restrictions apply.

> [1 Figure(s)]


|Table 1 – Errors and Processing Strategies of PPP|Col2|
|---|---|
|||
|**Errors**|**Strategies**|
|Satellite orbit|PPP-B2b orbitproducts|
|Satellite clock|PPP-B2b clockproducts|
|UCD|PPP-B2bproducts|
|Tropospheric delay|Model [8],[9] and parameter<br>estimation|
|Ionospheric delay|Model [10] or parameter<br>estimation|
|Phase wind-up|Model [11]|
|Relativistic effect|Model [12]|
|Satellite and receiver<br>antennaphase center|“atx” file provided by IGS|
|Receiver coordinates|Parameter estimation|
|Receiver clock|Parameter estimation|
|Phase ambiguity|Parameter estimation|



<!-- PAGE: 3 -->

February 2024	
IEEE Instrumentation & Measurement Magazine	
59
time transfer processing strategies. As far as the acquisition 
of precise products is concerned, GEO satellites are used 
in PPP-B2b time transfer instead of a network to broad-
cast real-time data, compared to the traditional PPP time 
transfer. The receiver clock offset obtained by PPP is the de-
viation of the local time tloc compared to the GNSS reference 
time tref. The time links involved in time transfer eliminate 
the GNSS reference time tref through receiver clock offset 
difference to achieve high precision time transfer, which is 
written as:
  ∆t
dt
dt
t
t
t
t
t
t
r A
r B
loc A
ref
loc B
ref
loc A
loc B
=
−
=
−
(
) −
−
(
)=
−
,
,
,
,
,
, 	 (9)
Results and Discussion
The zero-baseline CCD [13],[14] experiment can reflect the 
noise level of time transfer. The receivers involved in the 
zero-baseline time transfer are linked to a shared GNSS an-
tenna, and the baseline length is set to zero. QF PPP-B2b 
model was validated by zero-baseline CCD and long-­
baseline time links. Fig. 3 shows geographic location of two 
long-baseline time links, and Table 3 lists information of re-
ceivers involved in zero-baseline CCD and long-baseline 
time links. NTSC and TL are TAI timekeeping laboratories, 
while IGS station USUD simply uses an external atomic 
clock as the clock source for the GNSS receiver. GNSS re-
ceivers, TLM2, NTTS and NT07, are connected to the 
UTC(k). Taking time comparison using the GBM prod-
uct as a reference, QF and DF PPP-B2b time comparison 
were implemented to verify the improvement of PPP-B2b 
time transfer accuracy by increasing frequency. The ob-
servations participating zero-baseline CCD were used for 
12 d from day of year (DoY) 85 to 96 in 2022, while those 
from DoY 163 to 171 in 2022 were used for long-baseline 
time ­comparison. Observations can be obtained through 
Table 2 – QF PPP-B2b time comparison strategies
Item
Strategies
Navigation system
BDS-3
Raw observations
B1C, B2a, B1I, B3I
Satellite orbit and clock
Ephemeris and the PPP-B2b 
product
Estimator
Kalman filter
Processing interval
300 s
Pseudorange UCD
Corrected: the PPP-B2b 
product
Tropospheric delay
Dry delay: Saastamoinen 
model [8];
Wet delay: estimated as a 
random walk noise;
GMF model [9] is used as the 
mapping function.
Receiver clock
Estimated: white noise
Receiver coordinates
Estimated: constants (static)
Phase ambiguity
Estimated: floating point
GEO Satellite
BDS-3 Satellites
dtr,A
dtr,B
Station B
Station A
Fig. 1. Principle of PPP-B2b time transfer.
Data Preparation
Raw observations
Ephemeris and
PPP-B2b products
Data Preprocessing
Models and 
Empirical Formulas
Parameter 
Estimation
Receiver Clock
Offset
Fig. 2. Simplified PPP processing flow.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore.  Restrictions apply.

> [112 Figure(s)]

<!-- PAGE: 4 -->

60	
IEEE Instrumentation & Measurement Magazine	
February 2024
https://cddis.nasa.gov/, and the PPP-B2b product can be 
buffered by a NovAtel OEM729 receiver equipped with a 
PPP-B2b module.
PPP-B2b CCD
The result of zero-baseline CCD between NTTS and NT07 
with a common antenna and external clock using QF and DF 
PPP-B2b model was displayed in Fig. 4. The STD value of 
the CCD result was calculated. The satellite products are the 
same in PPP solution, and only the processing model is dif-
ferent. Ideally the CCD result should be a horizontal line, 
but the presence of noise makes the result sequence fluctu-
ate. The smoothness of the curve reflects the level of PPP-B2b 
model noise. Results show that QF PPP-B2b time transfer has 
smoother CCD results and fluctuates within 0.1 ns, compared 
to the DF PPP-B2b model.
Long-baseline PPP-B2b Time Comparison
Fig. 5 displays the results of the QF NTSC-TLM2 PPP-B2b 
time comparison from DoY 163 to 171 in 2022. The results of 
the time comparison reflect the TAI retention of the NTSC 
and TL laboratories. Certainly, the time comparison link er-
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
72˚E
0˚
12˚N
24˚N
36˚N
48˚N
60˚N
90˚E
108˚E
Longitude
TLM2
USUD
NTSC
Latitude
126˚E
144˚E
Fig. 3. The geographic distribution of time comparison links stations.
Table 3 – Detailed information of time links receivers
Station/
ID
Organization
GNSS 
Receiver
Clock
NTTS
NTSC
SEPT 
POLARX5
EXTERNAL
NT07
NTSC
SEPT 
POLARX5
EXTERNAL
TLM2
TL
SEPT 
POLARX5
EXTERNAL
USUD
IGS
SEPT 
POLARX5
EXTERNAL 
H-MASER
086
–7.2
–7.0
–6.8
–6.6
088
090
DoY (300 s interval)
Clock difference (ns)
092
094
096
QF PPP-B2b (STD = 0.0191)
DF PPP-B2b (STD = 0.0239)
Fig. 4. QF and DF PPP-B2b zero-baseline CCD.
164
–126
–125
–124
–123
–122
166
168
DoY
Clock difference (ns)
170
172
NTSC-TLM2 QF PPP-B2b
Fig. 5. QF PPP-B2b long-baseline time comparison for 9 d from DoY 163 to 171 in 2022.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore.  Restrictions apply.

> [6 Figure(s)]


|Table 3 – Detailed information of time links receivers|Col2|Col3|Col4|
|---|---|---|---|
|||||
|**Station/**<br>**ID**|**Organization**|**GNSS**<br>**Receiver**|**Clock**|
|NTTS|NTSC|SEPT<br>POLARX5|EXTERNAL|
|NT07|NTSC|SEPT<br>POLARX5|EXTERNAL|
|TLM2|TL|SEPT<br>POLARX5|EXTERNAL|
|USUD|IGS|SEPT<br>POLARX5|EXTERNAL<br>H-MASER|




|Col1|QF PPP-B2b (STD|
|---|---|



<!-- PAGE: 5 -->

February 2024	
IEEE Instrumentation & Measurement Magazine	
61
Conclusions
PPP time transfer accuracy can reach sub-nanosecond without 
limitations on distance. Conversely, PPP execution requires 
the external provision of real-time precise satellite products. 
Since August 2020, BDS-3 has provided precise products called 
the PPP-B2b product through three GEO satellites instead of a 
network, which solves the problem of interruption caused by 
network fluctuation in the field of real-time PPP time compar-
ison. The truth that BDS-3 DF PPP-B2b time transfer can reach 
an accuracy of sub-nanosecond has been proven. Considering 
the BDS-3 can provide users with a wide range of frequency 
signals for PPP and the increasing observation information 
will accelerate the PPP convergence and improve the accuracy 
of time transfer, the QF PPP-B2b time transfer was studied.
A QF PPP-B2b time transfer model was proposed and val-
idated from zero-baseline CCD and long-baseline time links. 
To ensure the accuracy of the results, two TAI keeping labora-
tories (NTSC and TL) and the IGS external atomic clock station 
(USUD) in the Asia-Pacific region were selected. To make full 
use of the BDS-3 frequency signals to verify the accuracy of QF 
PPP-B2b time transfer model, the newly broadcasted B1C and 
B2a signals of BDS-3 were 
used alongside existing B1I 
and B3I signals. The results 
showed that QF PPP-B2b 
time transfer had smoother 
CCD results and fluctuated 
within 0.1 ns, compared 
to the DF PPP-B2b model. 
In the NTSC-TLM2 long-
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
References
	[1]	 J. Zumberge et al., “Precise point positioning for the efficient 
and robust analysis of GPS data from large networks,” J. 
Geophysical Research-solid Earth, vol. 102, pp. 5005–5017, Mar. 
1997. 
	[2]	 J. H. Zhang, S. W. Dong, H. B. Yuan, W. Guang, Y. Zhang et al., 
“Study on PPP time comparison based on BeiDou-3 new signal,” 
IEEE Instrum. Meas. Mag., vol. 25, pp. 30–40, Aug. 2022. 
	[3]	 Y. L. Ge, S. X. Chen, T. Wu, C. M. Fan,  
W. J. Qin, F. Zhou and X. H. Yang, “An analysis of BDS-3 real-time 
PPP: time transfer, positioning, and tropospheric delay retrieval,” 
Measurement, vol. 172, 108871, Feb. 2021. 
	[4]	 “BeiDou navigation satellite system signal in space interface 
control document precise point positioning service signal  
PPP-B2b (version 1.0),” China Satellite Navigation Office,  
Aug. 2022. [Online]. Available: http://www.beidou.gov.cn/xt/
gfxz/202008/P020200803362062482940.pdf.
	[5]	 Y. X. Yang, Q. Ding, W. G. Gao, J. L. Li, Y. Y. Xu, B. J. Sun, 
“Principle and performance of BDSBAS and PPP-B2b of BDS-3,” 
Satellite Navigation, vol. 3, 2022. 
164
–2.0
–1.5
–1.0
–0.5
0.0
0.5
1.0
1.5
2.0
166
168
DoY
Clock difference (ns)
170
172
QF PPP-B2b
DF PPP-B2b
Fig. 6. Difference time sequences of NTSC-TLM2 PPP time comparison results using the GBM product and the PPP-B2b 
product.
164
17
18
19
20
21
22
23
24
25
166
168
DoY
Clock difference (ns)
170
172
QF PPP-B2b
DF PPP-B2b
Fig. 7. Difference time sequences of NTSC-USUD PPP time comparison results using the GBM product and the PPP-B2b 
product.
Table 4 – STD values of PPP-B2b time comparison 
residual
Time link
Model
QF PPP-B2b
DF PPP-B2b
NTSC-TLM2
0.161
0.215
NTSC-USUD
0.201
0.255
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore.  Restrictions apply.

> [4 Figure(s)]


|Table 4 – STD values of PPP-B2b time comparison<br>residual|Col2|Col3|
|---|---|---|
||||
|**Time link**|**Model**|**Model**|
|**Time link**|**QF PPP-B2b**|**DF PPP-B2b**|
|**NTSC-TLM2**|0.161|0.215|
|**NTSC-USUD**|0.201|0.255|



<!-- PAGE: 6 -->

62	
IEEE Instrumentation & Measurement Magazine	
February 2024
	[6]	 R. Z. Zhang, Z. M. He, L. M. Ma, G. W. Xiao, W. Guang et al., 
“Analysis of BDS-3 PPP-B2b positioning and time transfer 
service,” Remote Sensing, vol. 14, no. 12, 2769, Apr. 2022. 
	[7]	 J. Tang, D. Q. Lyu, F. L. Zeng, Y. L. Ge, R. Z. Zhang, 
“Comprehensive analysis of PPP-B2b service and its impact on 
BDS-3/GPS real-time PPP time transfer,” Remote Sensing, vol. 14, 
no. 21, 5366, Nov. 2022. 
	[8]	 J. Saastamoinen, “Atmospheric correction for the  
troposphere and the stratosphere in radio ranging Satellites,”  
The Use of Artificial Satellites for Geodesy, vol. 15, pp. 247–251,  
Jan. 1972.
	[9]	 J. Boehm, A. Niell, P. Tregoning and H. Schuh, “Global mapping 
function (GMF): a new empirical mapping function based on 
numerical weather model data,” Geophysical Research Letters,  
vol. 33, pp. 3–6, Apr. 2006. 
	[10]	M. Deo, A. El-Mowafy, “Triple-frequency GNSS models for PPP 
with float ambiguity estimation: performance comparison using 
GPS,” Survey Review, vol. 50, pp. 249–261, 2018. 
	[11]	J. T. Wu, S. C. Wu, G. A. Hajj, W. I. Bertiger, S. M. Lichten, “Effects 
of antenna orientation on GPS carrier phase,” Manuscripta 
Geodaetica, vol. 18, pp. 91–98, 1993.
	[12]	P. Heroux, J. Kouba, “GPS precise point positioning using IGS 
orbit products,” Physics and Chemistry of the Earth, Part A: Solid 
Earth and Geodesy, vol. 26, pp. 573–578, 2001. 
	[13]	W. Guang, J. H. Zhang, H. B. Yuan, W. J. Wu and S. W. Dong, 
“Analysis on the time transfer performance of BDS-3 signals,” 
Metrologia, vol. 57, 065023, Oct. 2020. 
	[14]	W. Guang, S. W. Dong, W. J. Wu, J. H. Zhang, H. B. Yuan et al., 
“Progress of BeiDou time transfer at NTSC,” Metrologia, vol. 55, 
pp. 175–187, Feb. 2018. 
Runzhi Zhang (zhangrunzhi@ntsc.ac.cn, corresponding au-
thor) is pursuing a Ph.D. degree at Key Laboratory of Precision 
Navigation and Timing Technology, National Time Service 
Center (NTSC), Chinese Academy of Sciences, Xi’an, China. 
His main research fields are time transfer and high precision 
positioning. He received an M.S. degree in communication 
and information systems from the NTSC in 2023.
Lan Li (lilan@stu.xupt.edu.cn) is a graduate student at the 
School of Communications and Information Engineering and 
School of Artificial Intelligence, Xi’an University of Posts and 
Telecommunications, Xi’an, China. Her main research fields 
are high precision positioning and time transfer.
Xueqing Li (lixueqing@ntsc.ac.cn) is currently working 
toward an M.S. degree in communication and information sys-
tem with the National Time Service Center, Chinese Academy 
of Sciences, Xi’an, China. Her research interests include satel-
lite network security and information security. She received 
her B.E. degree in computer science and technology from Qufu 
Normal University, Rizhao, China in 2020.
Hongjiao Ma (mahj@ntsc.ac.cn) received a Ph.D. degree in 
astrometry and celestial mechanics with National Time Ser-
vice Center, Chinese Academy of Sciences, Xi’an, China. His 
main research fields are time transfer and high precision 
positioning.
Gongwei Xiao (xiaogongwei@xupt.edu.cn) is a Lecturer 
with the Xi’an University of Posts and Telecommunications, 
Xi’an, China. His current research focuses on multi-GNSS 
PPP, real-time precise orbit determination for LEO satellites 
and tropospheric delay. To meet the demands of research 
and precise point positioning (PPP) in a multi-GNSS envi-
ronment, he open-sourced a GNSS data processing software 
named MG-APP (https://geodesy.noaa.gov/gps-toolbox/; 
https://github.com/xiaogongwei/MG_APP). He received 
the M.S. degree from the College of Geodesy and Geomatics, 
Shandong University of Science and Technology in 2018 and 
earned a Ph.D. degree from State Key Laboratory of Geod-
esy and Earth Dynamics, Innovation Academy for Precision 
Measurement Science and Technology, Chinese Academy of 
Sciences in 2021.
Jihai Zhang (zhangntsc@126.com) is a Research Associate 
at the National Time Service Center of Chinese Academy 
of Sciences, Xi’an, China and is working towards is Ph.D. 
degree. His main research fields are high precision time 
transfer and GNSS time difference monitoring. He received 
the M.S. degree in 2014 from University of Chinese Academy 
of Sciences.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:37:36 UTC from IEEE Xplore.  Restrictions apply.
