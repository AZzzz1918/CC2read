<!-- PAGE: 1 -->

Vol.:(0123456789)
1 3
GPS Solutions (2023) 27:61 
https://doi.org/10.1007/s10291-023-01402-y
ORIGINAL ARTICLE
An investigation of PPP time transfer via BDS‑3 PPP‑B2b service
Yulong Ge1 · Xinyun Cao2   · Daqian Lyu3 · Zaimin He4 · Fei Ye5 · Gongwei Xiao4 · Fei Shen2
Received: 27 May 2022 / Accepted: 11 January 2023 / Published online: 26 January 2023 
© The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2023
Abstract
Since 2020, China's Beidou has begun to provide an initial real-time precise point positioning (PPP) service via B2b signals 
for the Asia–Pacific region. It is expected to be used to achieve centimeter-level positioning and also brings opportunities 
for real-time time transfer. We collected 29 days of experimental data and compared it with the Centre National d’Etudes 
Spatiales (CNES) real-time products. The quality of the satellite's orbit and clock was analyzed first. Then, time transfer 
based on BDS-3, GPS, and BDS-3/GPS PPP was investigated. The results showed that the GPS PPP with the PPP-B2b is 
not recommended. The time transfer based on BDS-3 PPP using the PPP-B2a is feasible and achieves a 0.30 ns level. Impor-
tantly, the reliability of time transfer using the PPP-B2b outperforms that of PPP using CNES products due to the problem 
of unstable internet communication. Furthermore, compared to BDS-3-only, the precision of time transfer based on BDS-3/
GPS PPP was not improved significantly.
Keywords  Time transfer · BDS-3/GPS · Real-time PPP · PPP-B2b
Introduction
The BDS-3 in China has been providing all-weather, con-
tinuous PNT services for the world since July 31, 2020 (Lu 
et al. 2020; Yang et al. 2019, 2020). Nowadays, there are 
24 MEO, 3 GEO, and 3 IGSO that make up the BDS-3 
constellation. Compared to BDS-2, in terms of frequency, 
BDS-3 has added three new signals, B1C, B2b, and B2a, in 
addition to continuing to retain the B1I/B3I signals (CSNO 
2019, 2020a). In addition, the quality of the signals outper-
forms that of BDS-2, especially since the signals of BDS-3 
no longer have the problem of satellite-induced code bias 
(Zhang et al. 2017a; b). Furthermore, a hydrogen clock was 
installed on BDS-3, which provides better precision and a 
more stable frequency standard for navigation signals (Wu 
et al. 2018).
A large number of scholars have begun to study the 
BDS-3 in various fields, such as precise orbit determina-
tion (Duan et al. 2019; Li et al. 2018b, c), satellite clock 
offset estimation (Cao et al. 2022; Yang et al. 2021; Zeng 
et al. 2020), tropospheric delay estimation (Ge et al. 2021b), 
precise positioning (Jiao et al. 2020; Li et al. 2020; Shi et al. 
2020, 2021) and time transfer (Ge et al. 2021a; Guang et al. 
2020; Xiao et al. 2021; Zhang et al. 2019). For precise appli-
cations, two representative technologies are Real-time Kin-
ematic (RTK) and PPP (Malys and Jensen 1990; Shi et al. 
2020; Zumberge et al. 1997). IGS has provided RTS for PPP 
since 2013, for the needs of users (Montenbruck et al. 2017). 
Wang et al. (2019) studied the BDS-2 PPP using real-time 
products released from CNES and concluded that its posi-
tioning accuracy reaches to several decimeters due to the 
poor quality of the BDS-2 real-time products. Zhao et al. 
(2020) investigated the real-time GNSS PPP with CNES 
products in kinematic mode and presented the positioning 
accuracy of about 3.2, 2.9, and 6.0 cm at ENU direction, 
respectively.
 *	 Xinyun Cao 
	
xycao@njnu.edu.cn
1	
School of Marine Science and Engineering, Nanjing Normal 
University, Nanjing 210023, China
2	
School of Geography, Nanjing Normal University, 
Nanjing 210023, China
3	
College of Electronic Engineering, National University 
of Defense Technology, Hefei 230037, China
4	
School of Communication and Information Engineering, 
Xi’an University of Posts and Telecommunications, 
Xi’an 710121, China
5	
State Key Laboratory of Geodesy and Earth’s Dynamics, 
Innovation Academy for Precision Measurement Science 
and Technology, CAS, Wuhan 430077, China

> [1 Figure(s)]

<!-- PAGE: 2 -->

GPS Solutions (2023) 27:61
1 3
61 
Page 2 of 17
In addition to positioning, timing is also one of the impor-
tant service capabilities of BeiDou satellites (CSNO 2019). 
Nowadays, the PPP technique is widely applied in the time 
community. Subsequently, Li et al. (2018a) released sub-
nanosecond level time transfer using IGS real-time prod-
ucts. Furthermore, Ge et al. (2021b) analyzed the BDS-3 
real-time PPP time transfer and reached the sub-nanosecond 
level. But real-time PPP using IGS RTS products is difficult 
to guarantee reliability and is susceptible to network out-
ages that cause PPP to re-converge or even become unavail-
able. For this background, BDS-3 can now provide PPP-
B2b service via B2b signals to Asia by three BDS-3 GEO 
satellites (CSNO 2020a, b). PPP with PPP-B2b service in 
precise positioning was analyzed by some researchers (Liu 
et al. 2022; Tao et al. 2021; Xu et al. 2021; Yang et al. 2022). 
Little has been published on time transfer with the PPP-B2b; 
hence, the performance of BDS-3, GPS, and BDS-3/GPS 
PPP time transfer with the PPP-B2b service will be investi-
gated in this contribution.
The method of recovery of precise clock offset and orbit 
will be presented first, followed by PPP time transfer with 
the PPP-B2b. The quality of real-time products will then 
be assessed and analyzed. Next, the experimental dataset 
and the processing strategies are described in detail. Fol-
lowing that is the investigation and validation of PPP time 
transfer with the PPP-B2b correction. Finally, the findings 
are concluded.
Methodology
This part introduces the recovery of precise orbit and clock 
using broadcast ephemeris and PPP-B2b correction. Then, 
the PPP time transfer method is presented and the processing 
of PPP time transfer with the PPP-B2b service is illustrated 
in detail.
Precise orbit and clock offset recovered 
from PPP‑B2b service
Precise orbit can consist of broadcast ephemeris and PPP-
B2b correction (Xu et al. 2021), which is expressed as:
(1)
⎧
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪⎩
퐗= 퐗brd + (퐞r, 퐞a, 퐞c) ⋅Δ퐂
Δ퐂= [𝛿Cr, 𝛿Ca, 𝛿Cc]
er = r
r
ec =
r × ̇r
r × ̇r
ea = ec × er
where 퐗 is the vector of precise orbit in meters; (퐞r, 퐞a, 퐞c) 
indicates the transformation matrix in RAC direction; 퐗brd 
is the orbits calculated from broadcast ephemeris; Δ퐂 is the 
PPP-B2b correction at RAC direction; ̇r and r are the vector 
of satellite velocity and position in the ECEF. Note that the 
PPP-B2b service provides the satellite APC position of the 
B3 signal for BDS-3; hence, for B1I/B3I IF combination or 
another PPP model, the APC satellite position needs to be 
corrected to the corresponding frequency combination (Tao 
et al. 2021). For GPS, the APC of the position of the satellite 
refers to L1/L2 IF combination.
The precise satellite clock is recovered by the broadcast 
ephemeris clock and the corrections from the PPP-B2b ser-
vice as:
where tbrd indicates satellite clock in broadcast ephemeris; 
t illustrates the precise satellite clock offsets; Δt is the cor-
rection in the PPP-B2b service. c is the speed of light. Note 
further that the OSB corrections from the PPP-B2b ser-
vice need to be modified to the corresponding pseudorange 
observations.
PPP Time transfer
DF IF combination is usually employed for PPP (Tu et al. 
2019). The DF IF combination is usually written as:
where ps
r,IFij and ls
r,IFij are the OMC values for IF pseudorange 
and carrier phase observations; Here, s and r indicate the 
satellites and receiver; Δ퐱 illustrates the coordinate incre-
ment;훍s
r is the vector of coefficient for coordinates; i and j 
are the different frequencies. For BDS-3 and GPS satellites, 
B1I/B3I and L1/L2 combinations are selected to realized 
PPP time transfer; dr,i indicates the hardware delay for fre-
quency i at receiver end; fi represents frequency i; dtr is the 
receiver clock offset; dtr,IFij presents the receiver clock offset 
for i and j frequency IF combination ­(IFij) including the 
hardware delay; dr,IFij indicates the hardware delay for i and 
(2)
t = tbrd −Δt
c
(3)
ps
r,IFij = 훍s
r ⋅Δ퐱+ cdtr,IFij + ms
r,w ⋅Zw + 휉s
r,IFij
(4)
ls
r,IFij = 훍s
r ⋅Δ퐱+ cdtr,IFij + ms
r,w ⋅Zw + Ns
r,IFij + 휓s
r,IFij
(5)
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪⎩
cdtr,IFij = cdtr + cdr,IFij
dr,IFij = 훼ijdr,i + 훽ijdr,j
훼ij =
f 2
i
f 2
i −f 2
j
;훽ij = −
f 2
j
f 2
i −f 2
j
;i ≠j

<!-- PAGE: 3 -->

GPS Solutions (2023) 27:61	
1 3
Page 3 of 17 
61
j frequency IF combination; Zw is the tropospheric ZWD; 
ms
r,w demonstrates the wet mapping function; Ns
r,IFij is the 
float IF ambiguity; 휓s
r,IFij and 휉s
r,IFij are the noise. In addition, 
based on elevation-dependent weighting used in our work, 
the precision of orbit and clock calculated from the PPP-B2b 
correction also need to be considered. The weight W can be 
expressed as
where F is the satellite system error factor; Rr indicates 
code/carrier phase error ratio; a휎 and b2
휎 are carrier‐phase 
error factors a and b (m); E illustrates elevation angle; 휎eph 
is the URA from the PPP-B2b service; m is the number of 
satellites.
Unlike final products from MGEX or real-time multi-
GNSS products from IGS RTS, the reference for the BDS-3 
satellite clock is the BDT in the PPP-B2b service, which is 
more stable and continuous. However, the reference of the 
GPS satellite clock is not aligned to the same time reference; 
fortunately, this phenomenon does not affect the perfor-
mance of time transfer (Tao et al. 2021; Yang et al. 2022). 
The receiver clock offset cdtr,IFij , estimated from the PPP 
model using BDS-3, consists of the difference between BDT 
and the local time, and the hardware delay. Generally, the 
hardware delay is calibrated in advance. The difference Du 
between local time and BDT can then be described as
where u indicates the user; Tlocal demonstrates the local time 
of the users.
(6)
{
퐖= diag(휎−2
1 , 휎−2
2 , 휎−2
3 , ⋯, 휎−2
m )
휎2 = FRr(a2
휎+ b2
휎
/sin E2) + 휎2
eph
(7)
Du = Tlocal −BDT
For two different places, the difference ΔT will be 
expressed as
where T1 and T2 are the local time of different users.
For each station, receiving the BDS-3 or GPS pseudor-
ange and phase observation and 3 GEO satellite signals for 
decoding PPP-B2b corrections. Based on BDS-3 CNAV1 
and GPS LNAV broadcast ephemeris and decoded the PPP-
B2b correction, precise orbit and clock offset are then recov-
ered. Note that the OSB correction will be corrected directly 
for pseudorange at each frequency. Next, the time difference 
between BDT and the local time will be estimated directly 
by using the corresponding PPP model. Finally, the time 
transfer solutions can be obtained directly using Eq. (8).
Assessment of precise products recovered 
from the PPP‑B2b
The quality of orbit and clock determines PPP time transfer 
performance directly. 29 days, from DOY 122 to 131, 2022 
and from DOY 144 to 162, 2022, precise products recovered 
from the PPP-B2b are compared and evaluated with WUM 
final products released from Wuhan University, China. The 
RMSs of BDS-3 and GPS orbit errors for the CNES real-
time products and PPP-B2b are presented in Figs. 1 and 
2 and listed in Table 1, respectively, at RAC directly with 
respect to WUM products. Overall, the GPS orbit errors 
at the radial direction for the PPP-B2b are approximately 
(8)
ΔT = D1−D2
= T1 −BDT −(T2 −BDT)
= T1 −T2
Fig. 1   Orbits errors of GPS sat-
ellites for the CNES’s real-time 
products (Bottom) and PPP-B2b 
(Top) in the RAC direction

> [1 Figure(s)]

<!-- PAGE: 4 -->

GPS Solutions (2023) 27:61
1 3
61 
Page 4 of 17
0.1 m, while the orbit errors are relatively large at along 
and cross-directions. The mean RMS values in the RAC 
vector are about (0.10, 0.43, 0.23) m. For CNES real-time 
GPS products, the orbit errors agree with each other at the 
RAC direction; the mean RMS values in the RAC vector are 
approximately (0.02, 0.03, 0.02) m. The precision of GPS 
orbit in PPP-B2b is obviously worse than that of CNES, 
especially in the cross and along components. The reason 
is that a global network is employed by CNES, while only 
a regional network is applied for GPS in the PPP-B2b (Tao 
et al. 2021). For BDS-3 satellites, an interesting finding is 
that the precision of BDS-3 orbit at along component is bet-
ter than that of GPS in the PPP-B2b. That may be because 
BDS-3 is equipped with ISL terminals, which provide addi-
tional observations (Tang et al. 2018). The average RMS 
values for BDS-3 with PPP-B2b are about (0.07, 0.27, 0.23) 
m at RAC direction. For BDS-3 in CNES products, the pre-
cision of BDS-3 orbit is worse than that of GPS with (0.07, 
0.18, 0.12) m at RAC direction, which may be due to the 
poor distribution of BDS-3 tracking station as compared to 
GPS.
To further evaluate the satellite clock offset recovered 
from the PPP-B2b, the double-difference (DD) method 
was employed by using WUM final clock products as the 
reference (Montenbruck et al. 2014), with G01 and C38 
selected as references. The STD values of DD GPS and 
BDS-3 satellite clock recovered from CNES and PPP-B2b 
are displayed in Figs. 3 and 4. For the GPS constellation, the 
STD values of PPP-B2b are about 2 times larger than that of 
CNES. The average STD values of GPS satellite clocks are 
about 0.13 ns and 0.06 ns for PPP-B2b and CNES real-time 
products. More interestingly, the precision of the BDS-3 
satellite's clock from PPP-B2b outperforms that of BDS-3 
satellites from CNES, which may benefit the additional 
ISL observations. The average accuracies of the BDS-3 
clock from PPP-B2b and CNES are 0.12 ns and 0.23 ns, 
respectively.
Experimental setup
To test and investigate the performance of real-time PPP 
time transfer with the PPP-B2b service, detailed information 
on stations from MGEX is introduced in this part. Process-
ing strategies are then illustrated in detail.
Dataset
Since there are not many GNSS stations connected to an 
atomic clock in the Asia–Pacific region for time transfer, 
we only chose 2 GNSS stations, namely USUD and CUSV 
(Fig. 5). USUD is equipped with an H-master clock. Station 
Fig. 2   Orbits errors of BDS-3 
in the CNES real-time products 
(Bottom) and PPP-B2b (Top) in 
the RAC direction
Table 1   Mean RMS values of 
GPS or BDS-3 orbit errors in 
the PPP-B2b and the CNES 
real-time products with respect 
to WUM final products
PPP-B2b (m)
CNES’s real-time products (m)
R
A
C
R
A
C
GPS
0.10
0.43
0.23
0.02
0.03
0.02
BDS-3
0.07
0.27
0.23
0.07
0.18
0.12

> [1 Figure(s)]

<!-- PAGE: 5 -->

GPS Solutions (2023) 27:61	
1 3
Page 5 of 17 
61
CUSV does not link atomic clocks, but its frequency source 
is relatively stable, so we also chose it for experiments. The 
observations cover 29 days from DOY 122 to 131, 2022, 
and from DOY 144 to 162, 2022. Note that data from DOY 
132 to 143, 2022 were an internet interruption. The precise 
products will be recovered with LANV and CNAV1 broad-
cast ephemeris and the PPP-B2b correction. The CNES real-
time products were received and recovered by BNC software 
(Weber et al. 2016). Final products and ultra-rapid products 
released from Wuhan university were downloaded from 
ftp://​igs.​gnssw​hu.​cn/. Note that ultra-rapid products were 
called WUU for ease of expression in this work.
Processing strategy
In our work, the strategies of PPP time transfer are sum-
marized in Table 2. Those known errors, such as relativ-
istic effects, Sagnac effect et al., are modified by the IERS 
standard models (Petit and Luzum 2010). The receiver clock 
offset was regarded as white noise to estimate. BDS-3, GPS, 
and BDS-3/GPS PPP time transfer with the PPP-B2b were 
designed and compared with PPP with CNES, WUU, and 
WUM products. Here, the time transfer solutions from the 
IGS final clock products were set as the time standard. Note 
that considering the convergence of the PPP time transfer, 
the results of the first day were not used for the calculation of 
Fig. 3   The STD values of dou-
ble-difference of GPS satellites 
clock in the CNES’s real-time 
products and PPP-B2b
Fig. 4   The STD of double-
difference of satellites clock for 
the CNES’s real-time products 
and PPP-B2b
Fig. 5   Selected stations for time transfer from MGEX. Both stations 
are located in the Asia Pacific region and the PPP-B2B service can 
cover both regions. CUSV and USUD stations are equipped with 
high-performance crystal and hydrogen clocks, respectively

> [3 Figure(s)]

<!-- PAGE: 6 -->

GPS Solutions (2023) 27:61
1 3
61 
Page 6 of 17
the precision. In addition, for the BDS-3/GPS PPP model, an 
inter-system bias (ISB) parameter will be added. Here, the 
receiver clock offset was set to BDS-3 observations, while 
the receiver clock offset of GPS observations will consist of 
the receiver clock offset of BDS-3 and ISB. Note that a back-
ward filter was not employed in this study. In addition, MEO 
and GEO weighting ratio is 10:1 for BDS-3 PPP processing.
Results and validation
The time transfer based on PPP using the PPP-B2b service 
was investigated and compared with PPP using WUM, 
WUU, and CNES products. The STD values of the differ-
ence between time transfer solutions and the reference were 
employed to reflect the noise level. In addition, the MDEV 
was also utilized to assess real-time PPP in the frequency 
domain. Note that the CNES products in the full text repre-
sent the CNES real-time products. Below B2b indicates the 
real-time products recovered from the PPP-B2b correction. 
Note that B2b indicates the PPP-B2b in this contribution.
Before studying time transfer, we give the number of sat-
ellites involved in PPP with B2b products at two stations 
and display it in Fig. 6. The average numbers of satellites 
involved in PPP are (5.2, 6.9, 11.2) at station USUD and 
(5.3, 7.5, 12.2) at station CUSV for GPS-only, BDS-3-only, 
and BDS-3/GPS. The satellite number of BDS-3 is signifi-
cantly more than GPS. In addition, we can see that there 
are some epochs where the number of used GPS satellites 
is under 3 in the PPP processing, which is similar to BDS-3 
satellites. That can be explained by two facts. The one fact 
is that, unlike final precise products, the PPP-B2b service 
does not provide all GPS or BDS-3 satellite orbit and clock 
corrections at any given moment. The other fact is that some 
Table 2   Summary of PPP 
time transfer as used in this 
contribution
Estimator
Kalman filter
Signals
BDS-3: B1I/B3I
GPS: L1/L2
PCV and PCO
igs14.atx
Receiver clock offset
Estimated with a white noise model ­(104 ­m2)
Precise products
Broadcast ephemeris (CNAV1 or LNAV) + PPP-B2b correction
Broadcast ephemeris + CNES’s real-time correction
WUM final products
Tropospheric delay
ZHD: corrected (Saastamoinen 1972)
ZWD: estimated with a random walk noise model (3 × ­10–8 ­m2/s)
Tidal displacement
Corrected (Petit and Luzum 2010)
Phase ambiguities
Estimate as constant at each arc; When cycle-slip happened, 
estimated as white noise model ­(104 ­m2)
Receiver coordinates
Estimate as constant
Fig. 6   Number of satellites for 
BDS-3, GPS, and BDS-3/GPS 
used in PPP with the PPP-B2b 
service

> [1 Figure(s)]

<!-- PAGE: 7 -->

GPS Solutions (2023) 27:61	
1 3
Page 7 of 17 
61
satellites have been removed due to their large residuals. 
After the filter update, we check the observation residuals for 
each satellite. If the residual of the certain satellite exceeds, 
the weight of this abnormal observation is reduced, and re-
start the filter. If the result is still not qualified, we will fur-
ther eliminate the satellite with too large residuals.
GPS‑only
Now turn to Figs. 7 and 8, which exhibited the receiver clock 
offset for 29 days at CUSV and USUD stations, respec-
tively. From Fig. 7, the receiver clock offset based on the 
four products does not coincide very well, which can be 
further proved in Fig. 8. Especially in Fig. 8, we find that 
the time series of receiver offset using B2b is disorderly and 
discontinuous, which is because the reference of GPS in 
B2b is not the same clock. Further, the reference to GPS in 
CNES and WUU products is also discontinuous. Besides, 
the noise of the time series obtained from PPP using WUU 
products is larger because the sampling interval of the WUU 
products is 5 min. Moreover, the reference of the GPS clock 
in WUM products is continuous for one day and discontinu-
ous between different days. Luckily, the performance of time 
transfer is not affected by the reference of a precise clock 
product (see Eq. 8). In addition, from the figures, there is 
an understandable phenomenon that receiver clock offsets 
Fig. 7   Receiver clock offset for station CUSV estimated from GPS 
PPP using WUM, CNES, WUU, and B2b products
Fig. 8   Receiver clock offset for station USUD estimated from GPS 
PPP using WUM, CNES, WUU, and B2b products
Table 3   Availability percentages for PPP solutions with each precise 
product (%)
DOY
122–131
144–153
153–162
WUM
100
100
100
WUU​
100
100
100
CNES
97.1
95.3
96.5
B2b
99.9
99.4
99.6

> [2 Figure(s)]

<!-- PAGE: 8 -->

GPS Solutions (2023) 27:61
1 3
61 
Page 8 of 17
calculated from PPP using the CNES real-time products 
are prone to interruptions due to the instability of the inter-
net. We can further find the phenomenon in Table 3, which 
exhibits the availability percentages for PPP solutions with 
each precise product, compared with the theoretical number 
of epochs. Obviously, the availability percentages for PPP 
solutions with B2b are better than that of PPP with CNES. 
Since we are using the server to receive CNES corrections, 
the availability percentages of PPP with CNES products 
achieve about 95–97% only when the network is relatively 
good. But it is difficult to ensure such a good network envi-
ronment in the actual application process. This also strongly 
proves that PPP time transfer using B2b is significantly bet-
ter than the current that of PPP based on IGS RTS products 
in terms of reliability. Figure 9 exhibits the clock difference 
of CUSV-USUD estimated from PPP with WUM, WUU, 
CENS, and B2b products. As we mentioned, the differ-
ence in the reference was removed by using (8) for the time 
transfer, and the PPP time transfer using different products 
is generally consistent. Figure 10 displays the clock differ-
ence between GPS PPP time transfer with different products 
and the reference. The performance of GPS PPP with the 
PPP-B2b is significantly worse than GPS PPP with CNES, 
WUU, and WUM products. In addition, the STD and mean 
values of the difference between time transfer solutions and 
the reference are calculated and listed in Table 4. From the 
table, two findings are concluded. First, the mean values 
of time transfer with WUM, WUU, and CNES are close to 
zero, while that of time transfer with B2b is about 0.5 ns, 
an obvious system bias. That may be caused by the nonzero 
mean satellite bias, which has been presented by Tao et al. 
(2021). Second, the mean STD values of the difference for 
three arcs obtained from PPP with WUM, CNES, and WUU 
products are approximately 0.12 ns, 0.23 ns, and 0.50 ns, 
while that of PPP with B2b products is about 0.89 ns. That 
may be because GPS orbit and clock precision are poor, 
Fig. 9   CUSV-USUD clock difference obtained from GPS PPP using 
WUM, CNES, WUU, and B2b products
Fig. 10   CUSV-USUD clock difference between GPS PPP using 
WUM, CNES, and B2b products and the solutions from IGS final 
clock products

> [2 Figure(s)]

<!-- PAGE: 9 -->

GPS Solutions (2023) 27:61	
1 3
Page 9 of 17 
61
and the satellites involved in the time transfer solutions are 
fewer in the selected station. Combining Tables 3 and 4, 
PPP time transfer using WUU performs worse than PPP 
with CNES, but the data integrity of PPP with WUU is bet-
ter than that of CNES. In addition, let us analyze it further 
from the frequency domain. Figure 11 presents the MDEV 
of the solution based on different products. Similarly, the 
frequency stability of PPP with the PPP-B2b correction pre-
sents a worse performance in the four schemes. Hence, the 
precision of PPP time transfer with CNES products is almost 
as accurate as that of PPP with WUM products, while that 
of PPP with the PPP-B2b correction is poor, GPS-only PPP 
with B2b products is not recommended for time transfer.
BDS‑3 only
The receiver clock offset for CUSV and USUD stations 
estimated from BDS-3 PPP by applying WUM, WUU, 
CNES, and B2b products are displayed in Figs. 12 and 
13. Four interesting findings can be presented. First, unlike 
GPS PPP with WUM, the jump between days based on 
Table 4   Mean and STD of the difference between GPS PPP time transfer using different products and the reference (unit: ns). Note that the time 
transfer solutions calculated from GPS PPP using IGS final products were set as the time standard
DOY
B2b
WUM
CNES
WUU​
Mean
STD
Mean
STD
Mean
STD
Mean
STD
122–131
0.55
0.97
0.05
0.13
0.09
0.21
0.08
0.51
144–153
0.53
0.88
0.05
0.15
0.08
0.26
0.09
0.48
153–162
0.58
0.83
0.04
0.10
0.05
0.22
0.06
0.53
Fig. 11   MDEV of GPS time transfer using WUM, CNES, B2b prod-
ucts
Fig. 12   CUSV receiver clock offset from PPP BDS-3 in WUM, 
CNES, WUU, and B2b products

> [2 Figure(s)]

<!-- PAGE: 10 -->

GPS Solutions (2023) 27:61
1 3
61 
Page 10 of 17
BDS-3 PPP with WUM is very large, but it is still very 
continuous and stable throughout the day, which is the 
same as that of GPS PPP. It can be explained by the fact 
that the reference of GPS and BDS-3 clock in WUM is 
not the same. Second, although the relative continuity 
of BDS-3 PPP using CNES is compared to WUM, there 
are still jumps at the part-time and some outliers. Third, 
importantly, the BDS-3 PPP with B2b presents a very 
smooth and continuous time series, it may benefit from the 
fact the reference of B2b products is BDT. It also releases 
a signal that PPP based on B2b products can achieve better 
receiver clock modeling, which also proves from another 
perspective the superiority of time transfer in the real-
time model using BDS-3 in the PPP-B2b. Fourth, the time 
series of PPP using WUU presents a noticeable jump. That 
may be because WUU products are updated every hour, 
so there is a problem of constantly switching between the 
reference of ultra-rapid products.
The time transfer solutions of CUSV-USUD based on 
BDS-3 PPP are illustrated in Fig. 14. From the figure, the 
time series using different products agree well with each 
other, which indicates the viability of time transfer based on 
BDS-3 PPP using B2b products. Figure 15 presents the clock 
difference between BDS-3 PPP time transfer using differ-
ent products and the reference. Further, the mean and STD 
values of the difference between BDS-3 PPP using WUM, 
WUU, CNES, and B2b products and the reference are cal-
culated and introduced in Table 5. The difference in mean 
values between the four schemes is very small, further prov-
ing the feasibility of BDS-3 PPP using B2b numerically. The 
mean STD values of time transfer are 0.30, 0.14, 0.35, and 
0.54 ns for PPP based on BDS-3 with B2b, WUM, CNES, 
and WUU products. Obviously, the performance of PPP 
using WUM is best in four schemes, which can be explained 
because it is, after all, the final product. Another interesting 
finding is that the performance of time transfer using B2b 
Fig. 13   USUD receiver clock offset from PPP BDS-3 in WUM, 
CNES, WUU, and B2b products
Fig. 14   CUSV-USUD time transfer with BDS-3 PPP using different 
products

> [2 Figure(s)]

<!-- PAGE: 11 -->

GPS Solutions (2023) 27:61	
1 3
Page 11 of 17 
61
is slightly better than that of PPP using CNES. That may 
be because more stations that can track BDS-3 satellites in 
China were utilized to estimate the satellite orbit and clock, 
while CNES can use fewer stations in China for satellite 
clock estimation, and we can further explain the precision 
of the satellite clock offset (see Fig. 4). The performance of 
BDS-3 PPP time transfer with WUU products was the worst 
of the four schemes. In addition, we further calculated the 
MDEV of BDS-3 PPP using different products and display 
in Fig. 16. It can be easily found that the frequency stability 
of PPP using WUM outperforms that of PPP using B2b, and 
PPP using WUU performs worse. The mean frequency sta-
bilities are about (1.68E-12, 2.00E-12, 1.67E-12, 2.13E-12) 
at 960 s and about (6.99E-13, 7.39E-13, 6.96E-13, 7.55E-
13) at 15,360 s for BDS-3 PPP using B2b, CNES, WUM, 
and WUU products, which further prove the above finding.
BDS‑3/GPS
The characteristic of GPS, BDS-3, and BDS-3/GPS PPP 
with B2b products is investigated and compared. Fig-
ures 17 and 18 display the receiver clock offset for USUD 
and CUSV stations by using BDS-3, GPS, and BDS-3/
GPS PPP. Here, the receiver clock offsets estimated from 
BDS-3, BDS-3/GPS PPP are basically coincident, while 
that of GPS PPP presents a large fluctuation, due to the 
discontinuity of clock reference for GPS in the PP-B2b 
service. Figure 19 demonstrates the time transfer solu-
tions for CUSV-USUD using GPS, BDS-3, and BDS-3/
GPS PPP. In addition, the clock difference between time 
transfer calculated from GPS, BDSS-3, and BDS-3/GPS 
PPP with the PPP-B2b and the reference. A systematic 
bias is found between GPS PPP and BDS-3 PPP or BDS-3/
GPS PPP is displayed in Fig. 20. That may be due to the 
hardware delay at the receiver end. The STD and mean 
values of the difference between the reference and PPP 
using B2b products are also listed in Table 6. BDS-3 PPP 
time transfer precision using B2b product (0.30 ns) is sig-
nificantly better than GPS PPP (0.89 ns). Compared with 
BDS-3 PPP, the improvement of precision for BDS-3/GPS 
PPP is limited by adding GPS observations with 0.28 ns 
for time transfer. That is because the GPS observation 
equation has a relatively low weight. After all, the preci-
sion of the orbit and clock offset of GPS is lower than that 
of BDS-3. In addition, the MDEV of BDS-3, GPS, and 
BDS-3/GPS PPP using B2b products is drawn in Fig. 21. 
The frequency stability of BDS-3, GPS, and BDS-3/GPS 
PPP is about (2.11E-12, 1.72E-12, 1.67E-12) at 960 s and 
Fig. 15   CUSV-USUD clock difference between time transfer with 
BDS-3 PPP using different products and time transfer from IGS final 
products
Table 5   Mean and STD values 
of the time transfer based on 
BDS-3 PPP using B2b, WUM, 
and CNES products and the 
reference (unit: ns)
DOY
B2b
WUM
CNES
WUU​
Mean
STD
Mean
STD
Mean
STD
Mean
STD
122–131
− 55.45
0.28
− 55.15
0.14
− 55.63
0.31
− 54.98
0.49
144–153
− 55.73
0.30
− 56.86
0.16
− 55.02
0.35
− 55.30
0.55
153–162
− 54.92
0.31
− 54.86
0.12
− 54.82
0.39
− 55.13
0.58

> [1 Figure(s)]

<!-- PAGE: 12 -->

GPS Solutions (2023) 27:61
1 3
61 
Page 12 of 17
about (8.70E-13, 7.02E-13, 6.99E-13) at 15,360 s. The 
conclusion of frequency stability is similar to the precision 
of time transfer.
As we mentioned, the convergence time at the beginning 
of filtering was removed. Here, the mean convergence times 
for PPP with the PPP-B2b, CNES, WUU, and WUM prod-
ucts at different schemes are calculated and listed in Table 7. 
We use the positioning error rather than the receiver clock 
offset time series to calculate the convergence time, which 
is defined as the time when the horizontal and the verti-
cal positioning error fall within 0.1 m and 0.2 m, respec-
tively. We can find that GPS PPP using the PPP-B2b needs 
65.5 min to converge, while the average time for BDS-3 
PPP is about 39.5 min. Compared with BDS-3 only, the 
time of BDS-3/GPS PPP with the PPP-B2b correction can 
shorten by 16.4%. For PPP with the CNES products, the 
convergence times for GPS-only and BDS-3-only PPP are 
27.5 min and 42 min, respectively. The convergence time 
of PPP with WUU products is larger than PPP with CENS 
products, which may be affected by the precision of the sat-
ellite clock and the sample interval. In addition, PPP using 
the WUM products achieved the best results among the 
three products, with 23.5 min and 26.5 min for GPS-only 
and BDS-only PPP.
Summary
To meet the requirement of real-time PPP, the PPP-B2b 
service is provided by BDS-3 for users in China. 29-day 
PPP-B2b corrections were collected and recovered to the 
precise product. Then, the BDS-3 and GPS orbit and clock 
released by CNES and PPP-B2b products were assessed by 
using WHU final products (WUM) as the reference. The 
mean RMS of GPS orbit errors is about (0.10, 0.43, 0.23) 
m and (0.02, 0.03, 0.02) m at RAC direction in PPP-B2b 
and CNES, respectively. The average RMS values of BDS-3 
orbit errors are about (0.07, 0.27, 0.23) m and (0.07, 0.18, 
Fig. 16   MDEV of time transfer BDS-3 PPP using different products
Fig. 17   USUD receiver clock offset from BDS-3, GPS, and BDS-3/
GPS PPP using B2b products

> [2 Figure(s)]

<!-- PAGE: 13 -->

GPS Solutions (2023) 27:61	
1 3
Page 13 of 17 
61
0.12) m at RAC direction in PPP-B2b and CNES, respec-
tively. In terms of the satellite clock, the STD values of GPS 
satellites in PPP-B2b are larger than that of CNES. The pre-
cision of the BDS-3 satellite clock (0.12 ns) in PPP-B2b 
outperforms that of BDS-3 satellites in CNES (0.23 ns), due 
to the additional ISL observations.
The precision of time transfer obtained from GPS PPP 
using the PPP-B2b products (0.89 ns) is less than that 
of PPP using the CENS products (0.23 ns). There is a 
systematic bias between time transfer based on GPS PPP 
using the PPP-B2b and the time transfer solutions from 
the IGS final product. Besides, the reference of the sat-
ellite clock recovered from PPP-B2b is discontinuous. 
Overall, we do not recommend time transfer based on 
GPS PPP with the PPP-B2b service.
The precision of time transfer obtained from BDS-3 
PPP using the PPP-B2b, WUM, CENS, and WUU prod-
ucts are 0.30, 0.14, 0.35, and 0.54 ns, respectively. The 
performance of BDS-3 PPP time transfer using the PPP-
B2b products is slightly better than PPP using CNES due 
to the quality of precise products. Further, the frequency 
stability of time transfer presents similar conclusions. 
Hence, the time transfer calculated from BDS-3 PPP with 
the PPP-B2b is feasible and achieves a good performance. 
More importantly, real-time BDS-3 PPP using the PPP-
B2b products have better reliability because it sometimes 
does not re-converge due to Internet instability.
Compared with time transfer from BDS-3 PPP using 
the PPP-B2b, the precision of BDS-3/GPS PPP time 
transfer was slightly improved. The frequency stability 
of BDS-3, GPS and BDS-3/GPS PPP are about (2.11E-12, 
Fig. 18   CUSV receiver clock offset from BDS-3, GPS, and BDS-3/
GPS PPP using B2b products
Fig. 19   CUSV-USUD time transfer from BDS-3, GPS, and BDS-3/
GPS BDS-3 PPP using B2b products

> [2 Figure(s)]

<!-- PAGE: 14 -->

GPS Solutions (2023) 27:61
1 3
61 
Page 14 of 17
1.72E-12, 1.67E-12) at 960 s and about (8.70E-13, 7.02E-
13, 6.99E-13) at 15,360 s.
Acronyms
APC (Antenna Phase Center), BDS (BeiDou Navigation 
Satellite System), BDS-3 (Beidou Global Navigation Sat-
ellite System), BDT (BeiDou Navigation Satellite System 
Time), CNES (Centre National d’Etudes Spatiales), DF 
(Dual-Frequency), DOY (Day of Year), E (East), GNSS 
(Global Navigation Satellite System), IF (Ionosphere-
Free), IFCB (Inter Frequency Code Bias), IGS (Interna-
tional GNSS Service), ISL (Inter-Satellite Link), MGEX 
(Multi-GNSS Experiment), N (North), OMC (Observed 
Minus Computed), OSB (Observation-Specific Bias), 
PCOs (Phase Center Offsets), PCVs (Phase Center Vari-
ations), PNT (Positioning, Navigation, and Timing), PPP 
(Precise Point Positioning), QF (Quad Frequency), RAC 
Table 6   STD and mean of 
BDS-3, GPS, BDS-3/GPS 
PPP time transfer using B2b 
products and the reference (unit: 
ns)
DOY
GPS
BDS-3
BDS-3/GPS
Mean
STD
Mean
STD
Mean
STD
122–131
0.55
0.97
− 55.45
0.28
− 55.41
0.26
144–153
0.53
0.88
− 55.73
0.30
− 55.62
0.30
153–162
0.58
0.83
− 54.92
0.31
− 55.39
0.29
Fig. 20   CUSV-USUD clock difference between time transfer from 
BDS-3, GPS, and BDS-3/GPS BDS-3 PPP using B2b products and 
time transfer from IGS final clock products. Note that G and C indi-
cate GPS and BDS-3, respectively
Fig. 21   The MDEV of BDS-3, GPS, BDS-3/GPS PPP using B2b 
products
Table 7   The mean convergence time for the two stations with the 
PPP-B2b, CNES, WUU, and WUM products in static PPP (unit: min)
GPS
BDS-3
BDS-3/GPS
B2b
65.5
39.5
33.0
CNES
27.5
42.0
26.0
WUM
23.5
26.5
18.5
WUU​
56.5
60.0
45.5

> [2 Figure(s)]

<!-- PAGE: 15 -->

GPS Solutions (2023) 27:61	
1 3
Page 15 of 17 
61
(Radial, Along and Cross), RMS (Root Mean Square), 
RTS (Real-time Service), SF (Single-Frequency), STD 
(Standard Deviation), TAI (International Atomic Time), 
TF (Triple-Frequency), URA (User range accuracy), 
U (Up), ZTD (Zenith Total Delays), ZWD (Zenith Wet 
Delay).
Acknowledgements  We thank MGEX for providing observations. This 
work was supported by the National Natural Science Foundation of 
China (No. 42104014; 42077003; 41904018). Natural Science Foun-
dation of Jiangsu Province (No. BK20201374; BK20190714), Natural 
Science Foundation of the Higher Education Institutions of Jiangsu 
Province, China (21KJB420005), State Key Laboratory of Geodesy and 
Earth’s Dynamics (SKLGED2022-3-6, SKLGED2022-3-3) and High-
level innovation and entrepreneurship talent plan of Jiangsu Province.
Data availability  The GNSS data of MGEX are provided by the IGS 
and can be downloaded through ftp://​igs.​gnssw​hu.​cn.
References
Cao X, Kuang K, Ge Y, Shen F, Zhang S, Li J (2022) An efficient 
method for undifferenced BDS-2/BDS-3 high-rate clock estima-
tion. GPS Solutions. https://​doi.​org/​10.​1007/​s10291-​022-​01252-0
CSNO (2019) Development of the BeiDou navigation satellite system 
(Version 4.0). http://​www.​beidou.​gov.​cn/​xt/​gfxz/​201912/​P0201​
91227​43056​54554​78.​pdf
CSNO (2020a) BeiDou navigation satellite system signal in space 
interface control document open service signal B2b (Version 1.0)
CSNO (2020b) BeiDou navigation satellite system signal in space 
interface control document precise point positioning service sig-
nal PPP-B2b (Version 1.0).
Duan B, Hugentobler U, Chen J, Selmke I, Wang J (2019) Prediction 
versus real-time orbit determination for GNSS satellites. GPS 
Solut. https://​doi.​org/​10.​1007/​s10291-​019-​0834-2
Ge Y, Cao X, Shen F, Yang X, Wang S (2021a) BDS-3/Galileo time 
and frequency transfer with quad-frequency precise point posi-
tioning. Remote Sens. https://​doi.​org/​10.​3390/​rs131​42704
Ge Y, Chen S, Wu T, Fan C, Qin W, Zhou F, Yang X (2021b) An 
analysis of BDS-3 real-time PPP: Time transfer, positioning, and 
tropospheric delay retrieval. Measurement. https://​doi.​org/​10.​
1016/j.​measu​rement.​2020.​108871
Guang W, Zhang J, Yuan H, Wu W, Dong S (2020) Analysis on the 
time transfer performance of BDS-3 signals. Metrologia. https://​
doi.​org/​10.​1088/​1681-​7575/​abbcc1
Jiao G, Song S, Liu Y, Su K, Cheng N, Wang S (2020) Analysis and 
assessment of BDS-2 and BDS-3 broadcast ephemeris: accuracy, 
the datum of broadcast clocks and its impact on single point posi-
tioning. Remote Sens. https://​doi.​org/​10.​3390/​rs121​32081
Li G, Lin Y, Shi F, Liu J, Yang Y, Shi J (2018a) Using IGS RTS 
products for real-time subnanosecond level time transfer. China 
Satell Navig Conf (CSNC) 497:505–518. https://​doi.​org/​10.​1007/​
978-​981-​13-​0005-9_​40
Li X, Chen X, Ge M, Schuh H (2018b) Improving multi-GNSS ultra-
rapid orbit determination for real-time precise point positioning. 
J Geodesy. https://​doi.​org/​10.​1007/​s00190-​018-​1138-y
Li X, Yuan Y, Zhu Y, Huang J, Wu J, Xiong Y, Zhang X, Li X (2018c) 
Precise orbit determination for BDS3 experimental satellites using 
iGMAS and MGEX tracking networks. J Geodesy. https://​doi.​org/​
10.​1007/​s00190-​018-​1144-0
Li Z, Chen W, Ruan R, Liu X (2020) Evaluation of PPP-RTK based 
on BDS-3/BDS-2/GPS observations: a case study in Europe. GPS 
Solut. https://​doi.​org/​10.​1007/​s10291-​019-​0948-6
Liu Y, Yang C, Zhang M (2022) Comprehensive analyses of PPP-B2b 
performance in china and surrounding areas. Remote Sens. https://​
doi.​org/​10.​3390/​rs140​30643
Lu J, Guo X, Su C (2020) Global capabilities of BeiDou naviga-
tion satellite system. Satell Navig. https://​doi.​org/​10.​1186/​
s43020-​020-​00025-9
Malys S, Jensen PA (1990) Geodetic point positioning with GPS carrier 
beat phase data from the CASA UNO experiment. Geophys Res 
Lett 17(5):651–654
Montenbruck O, Steigenberger P, Hauschild A (2014) Broadcast ver-
sus precise ephemerides: a multi-GNSS perspective. GPS Solut 
19(2):321–333. https://​doi.​org/​10.​1007/​s10291-​014-​0390-8
Montenbruck O, Steigenberger P, Prange L, Deng Z, Zhao Q, Perosanz 
F, Romero I, Noll C, Stürze A, Weber G, Schmid R, MacLeod K, 
Schaer S (2017) The Multi-GNSS experiment (MGEX) of the 
international GNSS service (IGS)–achievements, prospects and 
challenges. Adv Space Res 59(7):1671–1697. https://​doi.​org/​10.​
1016/j.​asr.​2017.​01.​011
Petit G, Luzum BJITN (2010) IERS Conventions (2010). 36
Saastamoinen J (1972) Atmospheric correction for the troposphere 
and stratosphere in radio ranging satellites. Artif Satell Geodesy 
15:247–251. https://​doi.​org/​10.​1029/​GM015​p0247
Shi J, Ouyang C, Huang Y, Peng W (2020) Assessment of BDS-3 
global positioning service: ephemeris, SPP, PPP, RTK, and new 
signal. GPS Solut. https://​doi.​org/​10.​1007/​s10291-​020-​00995-y
Shi C, Wu X, Zheng F, Wang X, Wang J (2021) Modeling of BDS-2/
BDS-3 single-frequency PPP with B1I and B1C signals and posi-
tioning performance analysis. Measurement. https://​doi.​org/​10.​
1016/j.​measu​rement.​2021.​109355
Tang C, Hu X, Zhou S, Liu L, Pan J, Chen L, Guo R, Zhu L, Hu G, Li 
X, He F, Chang Z (2018) Initial results of centralized autonomous 
orbit determination of the new-generation BDS satellites with 
inter-satellite link measurements. J Geodesy 92(10):1155–1169. 
https://​doi.​org/​10.​1007/​s00190-​018-​1113-7
Tao J, Liu J, Hu Z, Zhao Q, Chen G, Ju B (2021) Initial assessment of 
the BDS-3 PPP-B2b RTS compared with the CNES RTS. GPS 
Solut. https://​doi.​org/​10.​1007/​s10291-​021-​01168-1
Tu R, Hong J, Zhang P, Zhang R, Fan L, Liu J, Lu X (2019) Multiple 
GNSS inter-system biases in precise time transfer. Meas Sci Tech-
nol. https://​doi.​org/​10.​1088/​1361-​6501/​ab32b​3o
Wang L, Li Z, Ge M, Neitzel F, Wang X, Yuan H (2019) Investigation 
of the performance of real-time BDS-only precise point position-
ing using the IGS real-time service. GPS Solut. https://​doi.​org/​10.​
1007/​s10291-​019-​0856-9
Weber G, Mervart L, Stürze A, Rülke A, Stcker D (2016) BKG Ntrip 
Client (BNC) Version 2.12: BKG Ntrip Client (BNC) Version 
2.12
Wu Z, Zhou S, Hu X, Liu L, Shuai T, Xie Y, Tang C, Pan J, Zhu L, 
Chang Z (2018) Performance of the BDS3 experimental satel-
lite passive hydrogen maser. GPS Solut. https://​doi.​org/​10.​1007/​
s10291-​018-​0706-1
Xiao X, Shen F, Lu X, Shen P, Ge Y (2021) Performance of BDS-2/3, 
GPS, and galileo time transfer with real-time single-frequency 
precise point positioning. Remote Sens. https://​doi.​org/​10.​3390/​
rs132​14192
Xu Y, Yang Y, Li J (2021) Performance evaluation of BDS-3 PPP-B2b 
precise point positioning service. GPS Solut. https://​doi.​org/​10.​
1007/​s10291-​021-​01175-2
Yang Y, Gao W, Guo S, Mao Y, Yang Y (2019) Introduction to Bei-
Dou-3 navigation satellite system. Navigation 66(1):7–18. https://​
doi.​org/​10.​1002/​navi.​291

<!-- PAGE: 16 -->

GPS Solutions (2023) 27:61
1 3
61 
Page 16 of 17
Yang Y, Mao Y, Sun B (2020) Basic performance and future develop-
ments of BeiDou global navigation satellite system. Satell Navig. 
https://​doi.​org/​10.​1186/​s43020-​019-​0006-0
Yang Y, Yang Y, Hu X, Tang C, Guo R, Zhou Z, Xu J, Pan J, Su M 
(2021) BeiDou-3 broadcast clock estimation by integration of 
observations of regional tracking stations and inter-satellite links. 
GPS Solut. https://​doi.​org/​10.​1007/​s10291-​020-​01067-x
Yang Y, Ding Q, Gao W, Li J, Xu Y, Sun B (2022) Principle and perfor-
mance of BDSBAS and PPP-B2b of BDS-3. Satell Navig. https://​
doi.​org/​10.​1186/​s43020-​022-​00066-2
Zeng T, Sui L, Ruan R, Jia X, Feng L (2020) Uncombined precise orbit 
and clock determination of GPS and BDS-3. Satell Navig. https://​
doi.​org/​10.​1186/​s43020-​020-​00019-7
Zhang X, Li X, Lu C, Wu M, Pan L (2017a) A comprehensive analysis 
of satellite-induced code bias for BDS-3 satellites and signals. 
Adv Space Res. https://​doi.​org/​10.​1016/j.​asr.​2017.​11.​031
Zhang X, Wu M, Liu W, Li X, Yu S, Lu C, Wickert J (2017b) Ini-
tial assessment of the COMPASS/BeiDou-3: new-genera-
tion navigation signals. J Geodesy. https://​doi.​org/​10.​1007/​
s00190-​017-​1020-3
Zhang P, Tu R, Wu W, Liu J, Wang X, Zhang R (2019) Initial accu-
racy and reliability of current BDS-3 precise positioning, veloc-
ity estimation, and time transfer (PVT). Adv Space Res. https://​
doi.​org/​10.​1016/j.​asr.​2019.​11.​006
Zhao X, Ge Y, Ke F, Liu C, Li F (2020) Investigation of real-time 
kinematic multi-GNSS precise point positioning with the CNES 
products. Measurement. https://​doi.​org/​10.​1016/j.​measu​rement.​
2020.​108231
Zumberge JF, Heflin MB, Jefferson DC, Watkins MM, Webb FH 
(1997) Precise point positioning for the efficient and robust 
analysis of GPS data from large networks. J Geophys Res 
B3(102):5005–5017
Publisher's Note  Springer Nature remains neutral with regard to 
jurisdictional claims in published maps and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds 
exclusive rights to this article under a publishing agreement with the 
author(s) or other rightsholder(s); author self-archiving of the accepted 
manuscript version of this article is solely governed by the terms of 
such publishing agreement and applicable law.
Yulong Ge   received his Ph.D. 
degree from the University of 
Chinese Academy of Sciences in 
2020 and is currently a lecturer 
at Nanjing Normal University. 
His current research mainly 
focuses on high-precise position-
ing and time transfer using 
multi-GNSS and multi-fre-
quency PPP. 
Xinyun Cao   received his Ph.D. 
degree from Wuhan University 
in 2018 and is an associate pro-
fessor at Nanjing Normal Uni-
versity, Nanjing, China. His cur-
rent research mainly focuses on 
multi-GNSS high-precise posi-
tioning and its geoscience 
applications. 
Daqian Lyu   received his Ph.D. 
degree from the National Univer-
sity of Defense Technology in 
2020 and is a lecturer at the 
National University of Defense 
Technology. His current research 
mainly focuses on precise point 
p o s i t i o n i n g  
a n d  
t i m e 
synchronization. 
Zaimin He   received his Ph.D. 
from the National Time Service 
Center (NTSC), Chinese Acad-
emy of Sciences (CAS) in 2012 
and is now working as a profes-
sor and master supervisor at 
Xi’an University of Posts & Tel-
ecommunications. His main 
research interests are focused on 
radio positioning, timing, and 
communication. 
Fei Ye   received his Ph.D. from 
the Institute of Geodesy and 
Geophysics, Chinese Academy 
of Sciences, in 2019 and is cur-
rently a postdoctoral fellow at 
the Innovation Academy for Pre-
cision Measurement Science and 
Technology, Chinese Academy 
of Sciences. His research focuses 
on post- and real-time GNSS 
precise orbit determination 
(POD) and Earth rotation param-
eters (ERP) determination.

> [5 Figure(s)]

<!-- PAGE: 17 -->

GPS Solutions (2023) 27:61	
1 3
Page 17 of 17 
61
Gongwei Xiao   received Ph.D. 
from the State Key Laboratory of 
Geodesy and Earth Dynamics, 
Innovation Academy for Preci-
sion Measurement Science and 
Technology, Chinese Academy 
of Sciences (CAS) in 2021 and is 
now working as a lecturer with 
the Xi’an University of Posts and 
Telecommunications. His cur-
rent research mainly focuses on 
multi-GNSS PPP, real-time pre-
cise orbit determination for LEO 
satellites and tropospheric delay. 
To meet the demands of research 
and precise point positioning 
(PPP) in a multi-GNSS environment, he open-sourced a GNSS data 
processing software named MG-APP (https://​geode​sy.​noaa.​gov/​gps-​
toolb​ox/; https://​github.​com/​xiaog​ongwei/​MG_​APP). 
Fei Shen   received his Ph.D 
degree from Wuhan University 
in 2012 and is an professor at 
Nanjing Normal University, 
Nanjing, China. His main 
research interests are interdisci-
plinary GNSS applications for 
Earth Observation.

> [2 Figure(s)]
