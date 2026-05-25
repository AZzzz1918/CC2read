<!-- PAGE: 1 -->

RESEARCH
GPS Solutions          (2025) 29:162 
https://doi.org/10.1007/s10291-025-01925-6
(Nie et al. 2018; Elsobeiey and Al-Harbi 2016). However, 
the implementation of RTS relies on a stable network com­
munication environment, which restricts the application of 
real-time PPP technology in areas with insufficient network 
coverage, such as deserts and oceans. In recent years, the 
BDS-3 PPP-B2b of China and the Galileo High Accuracy 
Service (HAS) of the European Union (EU) have been 
transmitting real-time precise correction products via satel­
lite-based broadcasting. PPP-B2b and HAS can realize the 
real-time precise positioning independent of network com­
munication, which presents a new solution for wide-area 
real-time high-precision positioning.
Many scholars have evaluated the quality of precise cor­
rections and the positioning performance of BDS-3 PPP-
B2b service since its launch in 2020. The results indicated 
that the accuracy of satellite orbits and clock offsets was at 
the centimeter level and within 0.2 ns, respectively, and the 
satellite clock offsets presented a systematic bias. Moreover, 
the availability of PPP-B2b precise corrections was more 
Introduction
Precise point positioning (PPP) technology enables users 
to achieve high-precision positioning with a single receiver 
through the joint use of code and carrier phase observations 
as well as precise satellite orbit and clock products. With 
the ongoing advancement of PPP technology and the rapidly 
increasing demand for real-time precise positioning, real-
time PPP has become a research hotspot. The international 
Global Navigation Satellite System (GNSS) service (IGS) 
has been delivering real-time precise correction products via 
Internet, providing users with real-time service (RTS) that 
can achieve decimeter-to-centimeter positioning accuracy 
	
 Lin Pan
linpan@csu.edu.cn
1	
School of Geosciences and Info-Physics, Central South 
University, Changsha 410083, China
Abstract
The BDS-3 PPP-B2b of China can offer BDS-3/GPS real-time precise point positioning (PPP) service in the Asia-Pacific 
region, while the Galileo High Accuracy Service (HAS) of the European Union can offer Galileo/GPS real-time PPP 
service worldwide. Their service areas have a geographical overlap in the Asia-Pacific region and there is potential for 
their interoperability in terms of supported satellite systems. In this study, a tightly integrated real-time PPP model by 
incorporating observations from complementary constellations of PPP-B2b and HAS (rather than combining their PPP 
results) based on respective stand-alone service for the Asia-Pacific region is constructed. For comparison, we employ the 
strategy with BDS-3/GPS from PPP-B2b (B2b C/G), the strategy with Galileo/GPS from HAS (HAS E/G), the strategy 
with BDS-3/GPS from PPP-B2b and Galileo from HAS (B2b C/G + HAS E), and the strategy with Galileo/GPS from 
HAS and BDS-3 from PPP-B2b (HAS E/G + B2b C). The datasets from 18 stations over a week are employed. The B2b 
C/G + HAS E strategy has the best performance, followed by B2b C/G and HAS E/G + B2b C strategies, while the per­
formance of HAS E/G strategy is the worst. The B2b C/G + HAS E strategy can provide a convergence time (processed 
every two hours) of 9.4 min with a threshold of 20/40 cm in horizontal/vertical directions, and a positioning accuracy 
(processed every 24  h) of 4.2/3.2/9.1  cm in east/north/up directions. Therefore, benefiting from the increased satellite 
number and improved satellite geometry, the integration of PPP-B2b and HAS can significantly improve the real-time 
PPP performance compared with respective stand-alone service.
Keywords  BDS-3 PPP-B2b · Galileo HAS · Real-time precise point positioning · Tight integration · Satellite 
communication
Received: 9 October 2024 / Accepted: 28 June 2025
© The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2025
BDS-3 PPP-B2b and Galileo HAS tightly integrated real-time PPP
Lin Pan1 · Chen Yang1
1 3

> [2 Figure(s)]

<!-- PAGE: 2 -->

GPS Solutions          (2025) 29:162 
than 90% in China, and the kinematic positioning accuracy 
of real-time PPP could reach centimeter level after conver­
gence (Xu et al. 2021; Tao et al. 2021). Tang et al. (2022) 
provided a detailed description of the generation strategies 
for various PPP-B2b correction products, and conducted a 
comprehensive evaluation of the quality of PPP-B2b precise 
corrections. In addition, several researchers also focused 
on these aspects and derived comparable results (Wu et al. 
2023; Ouyang et al. 2023). With regard to the systematic bias 
in PPP-B2b satellite clock offsets, Sun et al. (2023) derived 
its estimate by taking the post-processed precise ephemeri­
des as a reference, and then the corrected PPP-B2b satellite 
clock offsets by the estimate were applied to the real-time 
PPP processing. Alternatively, Xu et al. (2023) introduced 
an additional parameter to compensate for the systematic 
bias in the real-time PPP processing. Both approaches sig­
nificantly improved the convergence speed of real-time PPP.
The Galileo HAS Signal-In-Space (SIS) testing activities 
were conducted in the 2020–2022 timeframe. Fernandez-
Hernandez et al. (2022) provided a detailed explanation of 
the message structure for Galileo HAS, including the orga­
nization and transmission mode of correction data, as well 
as how HAS uses Galileo monitoring stations and uplinks to 
provide services. HAS delivers precise correction products 
through the E6-B signal of Galileo satellites, and provides 
high-precision real-time PPP service to global users. The 
EU Agency for the Space Programme (EUSPA) officially 
announced that Galileo provided the initial HAS service on 
January 24, 2023. Since then, a number of scholars have 
conducted research on the availability, the quality of satel­
lite orbit and clock corrections, and the positioning perfor­
mance of Galileo HAS. Zhang et al. (2024b) evaluated the 
number of visible satellites and the service rate of HAS on 
a global scale, and the results showed that the globally aver­
age number of GPS and Galileo satellites with valid HAS 
corrections was 9.44 and 7.95, respectively, with the aver­
age service rate being 99.9% and 99.6% for GPS-only and 
Galileo-only PPP, respectively. Zhou et al. (2024) assessed 
the accuracy of HAS orbit and clock correction products, 
and analyzed the HAS-based positioning accuracy. The 
results indicated that the accuracy of orbit and clock correc­
tions of Galileo was slightly higher than that of GPS, and 
both static and kinematic positioning of HAS could reach 
centimeter level. Similar results about the accuracy of HAS 
correction products and the HAS-based positioning perfor­
mance were also derived by some other scholars (Naciri et 
al. 2023; Kan et al. 2024). In addition, receivers that sup­
port the E6 signal can directly receive the HAS correction 
message broadcast by Galileo satellites, but this is restricted 
by the baud rate of E6-B signal and the particularity of 
HAS encoding scheme (Fernandez-Hernandez et al. 2022). 
Therefore, some scholars developed open-source libraries 
or software such as HASlib, GHASP, and HASPPP to facili­
tate the decoding and integration of HAS corrections (Borio 
et al. 2023; Zhang et al. 2024a; Prol et al. 2024).
BDS-3 PPP-B2b can provide real-time PPP service in 
the Asia-Pacific region, while Galileo HAS is able to pro­
vide real-time PPP service for global users. Thus, the ser­
vice areas of PPP-B2b and HAS overlap in the Asia-Pacific 
region. Moreover, PPP-B2b service supports BDS-3 and 
GPS constellations, while HAS service supports Gali­
leo and GPS constellations. Therefore, there is potential 
for interoperability between PPP-B2b and HAS services 
regarding the supported satellite constellations. This study 
constructs a tightly integrated real-time PPP model with the 
joint use of PPP-B2b and HAS precise corrections in the 
Asia-Pacific region. For completeness, four real-time PPP 
strategies are analyzed and compared, including the stand-
alone PPP-B2b strategy, stand-alone HAS strategy, and two 
PPP-B2b and HAS integration strategies. We first introduce 
the recovery of precise correction products and uniformity 
of datum. Next, the PPP-B2b and HAS tightly integrated 
real-time PPP model is constructed. Then, the results are 
presented and discussed. Finally, the main conclusions are 
summarized.
Recovery of precise correction products and 
uniformity of datum
The orbit and clock corrections of PPP-B2b refer to the 
legacy navigation message (LNAV) of GPS and the civil 
navigation message on B1C frequency (CNAV1) of BDS-3, 
while HAS provides orbit and clock corrections for LNAV 
of GPS and integrity navigation message (I/NAV) of Gali­
leo. The decoded corrections are matched with the corre­
sponding broadcast ephemerides to recover the real-time 
precise satellite orbits and clock offsets, that is:
{ ˜OB2b = OB2b −Rrac2xyzδOB2b
˜OHAS = OHAS −Rntw2xyz(δOHAS + δ ˙OHAS∆t)
(1)
{
c˜dts
B2b = cdts
B2b −δCB2b/c
c˜dts
HAS = cdts
HAS + δCHAS/c
(2)
where the subscripts B2b and HAS represent PPP-B2b and 
HAS corrections, respectively, ˜O and c˜dts are the recovered 
precise satellite positions and clock offsets, respectively, 
O and cdts are the satellite positions and clock offsets cal­
culated by broadcast ephemerides, respectively, Rrac2xyz
and Rntw2xyz represent the transformation matrix from the 
radial, along-track and cross-track (RAC) coordinate sys­
tem to the Earth-Centered Earth-Fixed (ECEF) coordinate 
1 3
  162 
 
Page 2 of 11

<!-- PAGE: 3 -->

GPS Solutions          (2025) 29:162 
system, both of which are calculated by the satellite position 
and velocity vectors derived from broadcast ephemerides, 
δO represents the corrections of satellite orbits, δ ˙O denotes 
the changing rates of orbit corrections, δC represents the 
corrections of satellite clock offsets, ∆t is the time interval 
from the reference time of state-space representation (SSR) 
messages containing orbit corrections to the current time, 
and c is the speed of light in a vacuum.
Table 1 lists the datums of recovered real-time precise 
satellite orbits and clock offsets of PPP-B2b and HAS. The 
reference of GNSS code and carrier phase observations is 
the instantaneous antenna phase center (APC) of the satel­
lite and the receiver. However, the orbit corrections pro­
vided by PPP-B2b refer to the L1/L2 ionospheric-free (IF) 
combined APC for GPS and the B3 APC for BDS-3, respec­
tively, and the corresponding reference of orbit corrections 
provided by HAS is the L1 APC and E1 APC for GPS and 
Galileo, respectively. To ensure the consistency, the datums 
of recovered real-time precise satellite orbits of each satel­
lite must be converted to the center of mass (CoM) by using 
the phase center offset (PCO) corrections in the ANTenna 
Exchange format (ANTEX) file provided by IGS, that is:
˜OCOM = ˜Oi,AP C −Tr · PCOi
(3)
where i denotes L1/L2 IF APC, B3 APC, L1 APC, or E1 
APC, ˜OAP C and ˜OCOM represent the satellite orbits refer­
ring to the APC and CoM, respectively, Tr is a conversion 
matrix from the satellite body-fixed coordinate system to the 
ECEF coordinate system, and PCO denotes the PCO cor­
rections. The reference of observations is transferred to the 
CoM by applying PCO and phase center variation (PCV) 
corrections for the consistency of PPP processing.
As shown in Table  1, the clock offset datum of GPS 
and BDS-3 in PPP-B2b products is L1P/L2P IF combina­
tion and B3I, respectively, while that of GPS and Galileo in 
HAS products is the IF combination with L1 C/A and L2P, 
and E1 and E5B, respectively. For real-time PPP process­
ing with multiple frequencies, the PPP-B2b and HAS also 
provide the code observable-specific signal bias (OSB) cor­
rection products. Hence, we just need to directly apply the 
OSB corrections to the code observations on the required 
frequency, so as to be consistent with the reference of the 
recovered real-time precise satellite clock offsets. It should 
be noted that the sign of the PPP-B2b and HAS correction 
formulas is opposite when using the augmentation services 
for OSB corrections (EUSPA 2022). For convenience, the 
single-frequency reference is denoted by m, and the dual-
frequency reference is denoted by m and n. Thus, the spe­
cific components of the recovered real-time precise satellite 
clock offsets can be expressed as:
{
c˜dts
m = cdts −ds
m
c˜dts
IF,mn = cdts −ds
IF,mn 
(4)
ds
IF,mn = amn,m · ds
m + amn,n · ds
n
(5)
with amn,m = f 2
m/(f 2
m −f 2
n) and amn,n = −f 2
n/(f 2
m −f 2
n) 
where amn,mand amn,n are the dual-frequency IF combina­
tion coefficients, f is the carrier frequency, ds is the satel­
lite code hardware delay, c˜dts
m denotes the precise satellite 
clock offset with a single-frequency datum, and c˜dts
IF,mn 
denotes the precise satellite clock offset with a dual-fre­
quency IF combined datum.
The raw code observations contain the satellite code 
hardware delay on a single frequency, which needs to be 
corrected by OSB to make them consistent with the satellite 
code hardware delay included in the precise satellite clock 
offsets. The BDS-3 code observations can be corrected by 
OSB from PPP-B2b according to the following formula:
¯Pj = P ′
j + ds
j −OSBm,j = P ′
j + ds
m
(6)
where j represents the frequency, OSB represents the code 
OSB corrections, P represents the code observations cor­
rected by OSB, and P ′ represents the code observations 
without the satellite code hardware delay. It should be noted 
that the PPP-B2b product does not contain the OSB cor­
rections of GPS. Since the GPS satellite clock offsets from 
PPP-B2b product take a L1/L2 dual-frequency IF combined 
datum, the inconsistency of satellite code hardware delay 
between code observations and satellite clock offsets will be 
absorbed by the ionospheric delay parameter when employ­
ing a L1/L2 dual-frequency uncombined observation model.
The Galileo and GPS code observations can be corrected 
by OSB from HAS according to the following formula:
¯Pj = P ′
j + ds
j + OSBIF,mn,j = P ′
j + ds
IF,mn
(7)
Table 1  Datums of recovered real-time precise satellite orbits and 
clock offsets of PPP-B2b and HAS
Items
Systems
Datums
PPP-B2b
HAS
Satellite orbits
GPS
L1 and L2 IF APC
L1 APC
BDS-3
B3 APC
–
Galileo
–
E1 APC
Clock offsets
GPS
L1P and L2P IF
L1 C/A and L2P IF
BDS-3
B3I
–
Galileo
–
E1 and E5B IF
1 3
Page 3 of 11 
  162

<!-- PAGE: 4 -->

GPS Solutions          (2025) 29:162 
precise satellite orbits and clock offsets as well as the OSB 
corrections, the PPP-B2b and HAS tightly integrated real-
time PPP dual-frequency uncombined observation model 
can be expressed as:























ps,sys
r,1
= µs,sys
r
· Xr + c¯dtsys
r
+ γsys
1
· ¯Is,sys
r
+αs,sys
r
· Zr + θsys · Ds,sys
ps,sys
r,2
= µs,sys
r
· Xr + c¯dtsys
r
+ γsys
2
· ¯Is,sys
r
+αs,sys
r
· Zr + θsys · Ds,sys
ls,sys
r,1
= µs,sys
r
· Xr + c¯dtsys
r
−γsys
1
· ¯Is,sys
r
+αs,sys
r
· Zr + ¯N s,sys
r,1
ls,sys
r,2
= µs,sys
r
· Xr + c¯dtsys
r
−γsys
2
· ¯Is,sys
r
+αs,sys
r
· Zr + ¯N s,sys
r,2

(9)
θsys=
{0, sys = GPS HAS or Galileo
1, sys = GPS B2b or BDS-3 
(10)















c¯dtsys
r
= cdtsys
r
+asys
12,1 · dsys
r,1 + asys
12,2 · dsys
r,2
¯Is,sys
r
= Is,sys
r
+ asys
12,2 · (dsys
r,1 −dsys
r,2 ) + ηsys · ds,sys
ion
¯N s,sys
r,1
= N s,sys
r,1
+ bsys
r,1 + bs,sys
1
−(asys
12,1 −γsys
1
· asys
12,2) · dsys
r,1
−asys
12,2 · (1 + γsys
1
) · dsys
r,2 −ds,sys
pre
+ ηsys · γsys
1
· ds,sys
ion
¯N s,sys
r,2
= N s,sys
r,2
+ bsys
r,2 + bs,sys
2
−(asys
12,1 −γsys
2
· asys
12,2) · dsys
r,1
−asys
12,2 · (1 + γsys
2
) · dsys
r,2 −ds,sys
pre
+ ηsys · γsys
2
· ds,sys
ion

(11)
ds,sys
pre
=
{
ds,sys
m
,
sys = BDS-3
asys
mn,m · ds,sys
m
+ asys
mn,n · ds,sys
n
, sys = others 
(12)
ηsys =
{
1, sys = GPS B2b
0, sys = others

(13)
ds,sys
ion
= asys
mn,n · (ds,sys
m
−ds,sys
n
)
(14)
with 
asys
12,1 = (f sys
1
)2/((f sys
1
)2 −(f sys
2
)2) 
and 
asys
12,2 = −(f sys
2
)2/((f sys
1
)2 −(f sys
2
)2) where p and l 
denote the observed-minus-computed (OMC) code and 
phase observables, respectively, µ denotes the unit vector 
in the line of sight direction from the receiver to the sat­
ellite, X denotes the three-dimensional (3D) coordinates 
of the receiver, c¯dtr denotes the receiver clock offset esti­
mate that absorbs the receiver code hardware delay in the 
form of the dual-frequency IF combination, ¯I denotes the 
ionospheric delay estimate that absorbs the code hardware 
delay at the receiver as well as the code hardware delay at 
the satellite (only for GPS B2b), Z denotes the tropospheric 
zenith wet delay (ZWD), α denotes the wet mapping func­
tion, ¯N denotes the phase ambiguity estimate that absorbs 
the code and phase hardware delay at the satellite and 
receiver, and D denotes the compensating parameter for the 
initial systematic bias of PPP-B2b satellite clock offsets. In 
Eq. (11), ds,sys
pre  denotes the satellite code hardware delay 
absorbed by the phase ambiguity parameter, which is intro­
duced when applying the PPP-B2b or HAS precise satel­
lite clock offsets, and is consistent with their reference (see 
PPP-B2b and HAS tightly integrated real-
time PPP model
Since both PPP-B2b and HAS products support GPS, for 
ease of expression, the GPS constellation taking PPP-B2b 
corrections is represented as GPS B2b, and the GPS con­
stellation taking HAS corrections is represented as GPS 
HAS. The code and phase observations can be expressed 
as follows:







P s,sys
r,j
= ρs,sys
r
+ cdtsys
r
−cdts,sys
+γsys
j
· Is,sys
r
+ T s,sys
r
+ dsys
r,j + ds,sys
j
+ es,sys
r,j
Ls,sys
r,j
= ρs,sys
r
+ cdtsys
r
−cdts,sys −γsys
j
· Is,sys
r
+T s,sys
r
+ N s,sys
r,j
+ bsys
r,j + bs,sys
j
+ εs,sys
r,j

(8)
where sys represents GPS B2b, GPS HAS, BDS-3 or Gali­
leo, r and s represent the receiver and satellite, respectively, 
j is the frequency, P represents code observations, L repre­
sents carrier phase observations, ρ is the geometric distance 
between satellite and receiver, cdtr and cdts represent the 
receiver and satellite clock offsets, respectively, I represents 
the slant ionospheric delay on the first frequency, γ is the 
ionospheric delay factor (γsys
j
= (f sys
1
/f sys
j
)2), f is the car­
rier frequency, T represents the slant tropospheric delay, dr 
and ds denote the receiver and satellite code hardware delay, 
respectively, N is the phase ambiguity, br and bs denote the 
receiver and satellite phase hardware delay, respectively, 
and e and ε represent the measurement noises of code and 
carrier phase observations (including unmodeled errors 
such as multipath effects), respectively.
The datums of satellite clock offsets of GPS B2b are fre­
quently switched because the PPP-B2b products are derived 
from the regional network solutions. Therefore, a separate 
receiver clock offset parameter should be estimated for each 
satellite system. Alternatively, the inter-system bias (ISB) 
parameter should be estimated as white noise process to 
absorb the influence of switched datums. The former method 
is adopted in this study. It should be noted that there is an 
initial systematic bias in the recovered PPP-B2b precise sat­
ellite clock offsets for each satellite, which can be absorbed 
by the phase ambiguity parameter and does not affect the 
carrier phase observations. However, the initial systematic 
bias will impact the accuracy of code observations. There­
fore, a compensating parameter is introduced into the code 
observation equation for each satellite to mitigate the effects 
of the initial systematic bias included in satellite clock off­
sets for GPS B2b and BDS-3 constellations. Taking the final 
satellite clock product as the reference, the errors of PPP-
B2b satellite clock offsets exhibit relatively stable charac­
teristics within each continuous arc. Thus, the compensating 
parameter for the initial systematic bias is estimated as ran­
dom-walk process. After applying the recovered real-time 
1 3
  162 
 
Page 4 of 11

<!-- PAGE: 5 -->

GPS Solutions          (2025) 29:162 
parameter is estimated as random-walk process, the intro­
duction of a compensating parameter into the code obser­
vation equation for each satellite of GPS B2b and BDS-3 
constellations will not reduce the redundancy of the real-
time PPP model. Actually, the redundancy of the model 
approximates the difference between the number of obser­
vations and the number of parameters without strong con­
straints, such as receiver clock offset parameters.
Results and discussion
The datasets and processing strategies are first introduced. 
Next, the availability is analyzed. Finally, the position solu­
tions are provided.
Datasets and processing strategies
In this study, the datasets on day of year (DOY) 180–186 of 
2024 from 18 Multi-GNSS Experimental (MGEX) stations 
located in the Asia-Pacific region are employed to evalu­
ate the performance of PPP-B2b and HAS tightly integrated 
real-time PPP. Due to the absence of observations at cer­
tain stations on specific days (i.e., JDPR, LCK4 and IITK 
stations on DOY 185 of 2024 and SGOC station on DOY 
180 of 2024), the analysis ultimately involves a total of 122 
sets of daily observations. The geographical distribution 
of the selected stations is shown in Fig. 1. The stations are 
chosen according to three principles: (1) coverage within 
the PPP-B2b service area (75°E–135°E, 10°N–55°N) with 
minor boundary extensions of several degrees, (2) support 
for simultaneous tracking of BDS-3, GPS, and Galileo sig­
nals, and (3) quasi-uniform spatial distribution. As for the 
analysis period, while it is arbitrarily chosen, we adopt a 
continuous 7-day period after considering the orbital repeat 
period and the computational burden.
For comparison, four real-time PPP strategies are ana­
lyzed, including the strategy with BDS-3/GPS from PPP-
B2b (B2b C/G), the strategy with Galileo/GPS from HAS 
(HAS E/G), the strategy with BDS-3/GPS from PPP-B2b 
and Galileo from HAS (B2b C/G + HAS E), and the strat­
egy with Galileo/GPS from HAS and BDS-3 from PPP-B2b 
(HAS E/G + B2b C). The real-time PPP processing is carried 
out with the strategies summarized in Table 2.
Availability
The availability analysis presented in this study is concen­
trated on the Asia-Pacific region with specific geographical 
ranges from latitude 0° to 60°N and longitude 60°E to 180°. 
The service rates, the number of visible satellites, and the 
position dilution of precision (PDOP) for four real-time PPP 
Eq. (4)). In Eq. (11), ds,sys
ion  denotes satellite code hardware 
delay absorbed by the ionospheric delay parameter and then 
propagated to the phase ambiguity parameter (only for GPS 
B2b), which is introduced by the inconsistency of satellite 
code hardware delay between code observations and satel­
lite clock offsets. To remove the rank deficiency caused by 
the introduction of compensating parameter for the initial 
systematic bias for each satellite within a constellation in 
Eq. (9), a separate pseudo-observation equation of the com­
pensating parameter with a pseudo-observable of zero for a 
selected satellite for each of GPS B2b and BDS-3 constella­
tions can be introduced into the observation model.
In view that the pseudo-observable is introduced as 
a datum to eliminate the rank deficiency, a much smaller 
magnitude should be assigned to its noise. In this study, 
the variance of the pseudo-observable is set to 1 × 10–6 m2. 
There is a strong correlation between the receiver clock off­
set parameter and numerous compensating parameters. By 
assigning a numerical value of zero to the compensating 
parameter of the selected satellite, the receiver clock offset 
estimates actually absorb the initial systematic bias of the 
selected satellite, while the estimated compensating param­
eter for other satellites is essentially the difference of ini­
tial systematic bias between these satellites and the selected 
satellite. Considering the regional service nature of BDS-3 
PPP-B2b, even when the selected satellite exits the service 
coverage, the introduced datum will propagate backward to 
subsequent epochs because the compensating parameter is 
modeled as random-walk process. During satellite ingress 
events, compensating parameters for the newly visible sat­
ellites require initialization, whereas compensating param­
eters for all satellites must undergo re-initialization upon 
re-entry of the selected satellite into the service area.
Since the estimator adopts the Kalman filter, there is 
predicted information for the parameters with a strongly 
constrained dynamic model. Thus, as the compensating 
Fig. 1  Geographical distribution of 18 MGEX stations located in the 
Asia-Pacific region
 
1 3
Page 5 of 11 
  162

> [1 Figure(s)]

<!-- PAGE: 6 -->

GPS Solutions          (2025) 29:162 
strategies (namely B2b C/G, B2b C/G + HAS E, HAS E/G, 
and HAS E/G + B2b C) are analyzed. To ensure the consis­
tency with the positioning strategies, the sampling interval 
is set to 30 s, and the cut-off elevation angle is set to 10°. The 
research area is divided into 60 × 60 grids with an interval of 
2° in longitude and 1° in latitude, and it is assumed that a 
virtual receiver at an altitude of 25 m is placed in the center 
of each grid (Yang et al. 2011). Subsequently, the relative 
geometries between each satellite and the virtual receiver 
are analyzed to evaluate the availability of four real-time 
PPP strategies by combining the known receiver positions 
and the calculated satellite positions.
When there are at least four visible satellites and the 
PDOP values are less than 30 at a certain epoch, the posi­
tion determination at this epoch is considered to be feasible. 
In this study, the service rate is defined as the percentage of 
the number of epochs with feasible position solutions over 
the total number of epochs. The service rate for each grid is 
calculated. The results indicate that all four real-time PPP 
strategies can achieve a service rate of 100% in the Asia-
Pacific region, which means that even the stand-alone PPP-
B2b service and the stand-alone HAS service can provide 
continuous positioning services for users in the Asia-Pacific 
region.
Figure 2 illustrates the geographical distribution of the 
average number of visible satellites over seven days from 
DOY 180 to 186 of 2024 for four real-time PPP strategies. 
Table 2  Processing strategies for real-time PPP
Items
Strategies
Frequencies
BDS-3: B1/B3
GPS: L1/L2
Galileo: E1/E5A
Positioning mode
Kinematic
Weighting method
Elevation-dependent weights
Sampling rate
30 s
Elevation cut-off angle
10°
PCO/PCV
PPP-B2b: IGS20 atx file
HAS: IGS14 atx file
Phase wind-up effect
Corrected
Relativistic effect
Corrected
Station displacement
Corrected with IERS Convention 2010
Satellite orbit/clock/
code bias
Broadcast ephemerides with correspond­
ing augmentation products
Receiver clock
A separate receiver clock offset parameter 
is estimated for each satellite system, and 
modeled as white noise process (104 m2)
Ionospheric delay
Estimated as random-walk process (10–4 
m2/s)
Tropospheric delay
Dry component: Saastamoinen model
Wet component: mapping slant delays to 
zenith delays with global mapping func­
tion (GMF) and estimated as random-
walk process (10–8 m2/s)
Phase ambiguity
Estimated as float constants
Compensating param­
eter for initial system­
atic bias
Estimated as random-walk process (10–10 
m2/s) over each continuous arc
Fig. 2  Geographical distribution of the average number of visible satellites for four real-time PPP strategies
 
1 3
  162 
 
Page 6 of 11

> [1 Figure(s)]

<!-- PAGE: 7 -->

GPS Solutions          (2025) 29:162 
Figure 3 displays the geographical distribution of aver­
age PDOP values over the entire analysis period for four 
real-time PPP strategies. The B2b C/G + HAS E strategy 
integrating HAS Galileo presents lower PODP values in 
contrast to the B2b C/G strategy that only employs PPP-B2b 
products. Similarly, the HAS E/G + B2b C strategy that inte­
grates PPP-B2b BDS-3 also exhibits lower PODP values 
compared with the HAS E/G strategy. The PDOP values of 
the B2b C/G and B2b C/G + HAS E strategies are relatively 
smaller within the range of 80°E to 140°E, particularly in 
the mainland of China, with the minimum values of 1.28 and 
1.06, respectively. In the areas of 60°E to 80°E and 140°E 
to 180°, the PDOP values of B2b C/G and B2b C/G + HAS 
E strategies gradually increase towards both sides, ranging 
from 1.39 to 3.01 and 1.11 to 1.41, respectively. For the 
other two strategies, the distribution of PDOP values is rela­
tively even, ranging from 1.35 to 1.62 for HAS E/G strategy 
and from 1.07 to 1.25 for HAS E/G + B2b C strategy. After 
an integration with PPP-B2b BDS-3, the HAS E/G + B2b C 
PDOP values within the latitude range from 12°N to 40°N 
are still slightly higher than those in other regions, espe­
cially in the longitude range from 150°E to 180°.
Position solutions
Figures 4 and 5 depict the epoch-wise positioning errors for 
four real-time PPP strategies (i.e., B2b C/G, B2b C/G + HAS 
The number of visible satellites under the B2b C/G strategy 
is relatively larger in the mainland of China and its coastal 
regions, especially within the range of 12°N to 48°N and 
90°E to 130°E, with the corresponding satellite numbers 
ranging from 14.9 to 16.5. In addition, the visible satellite 
numbers present a decreasing trend towards surrounding 
areas in a circular pattern, with the lowest number in the 
Pacific region being 9.3. After integrating with HAS Gali­
leo, the number of visible satellites increases significantly, 
ranging from 16.6 to 22.9, and the distribution character­
istics of satellite numbers are consistent with those of the 
B2b C/G strategy (i.e., more visible satellites in the central 
regions and less visible satellites in the peripheral regions). 
The number of visible satellites under the HAS E/G strat­
egy is mainly concentrated in the areas spanning 0° to 12°N 
and 50°N to 60°N, with the corresponding satellite num­
bers ranging from 13.2 to 16.2. However, in the mainland 
of China and its coastal regions, the number of visible satel­
lites under the HAS E/G strategy is relatively smaller, with 
a varying range of 12.9 to 14.8. After integrating with PPP-
B2b BDS-3, the distribution characteristics of the satellite 
numbers are consistent with those of the HAS E/G strat­
egy, and there are less visible satellites (ranging from 18.7 
to 21.2) in the regions spanning 12°N to 50°N (especially 
in the regions of 160°E to 180°), while the corresponding 
numbers increase to 23.3 in other regions.
Fig. 3  Geographical distribution of average PDOP values for four real-time PPP strategies
 
1 3
Page 7 of 11 
  162

> [1 Figure(s)]

<!-- PAGE: 8 -->

GPS Solutions          (2025) 29:162 
E, HAS E/G, and HAS E/G + B2b C) at stations JDPR and 
POL2 on DOY 186 of 2024, respectively. As can be seen 
from the two figures, the position solutions of all the four 
real-time PPP strategies can quickly converge to the target 
accuracy of PPP-B2b and HAS services (i.e., 20 cm in hori­
zontal direction and 40 cm in vertical direction). The posi­
tioning accuracy in the east and north directions is usually 
better than 10 cm after convergence, while the correspond­
ing accuracy in the up direction is usually better than 20 cm. 
It should be noted that the stability of position solutions of 
HAS E/G strategy is inferior to that of the other three strate­
gies after the position filter converges.
To evaluate the convergence time of four real-time PPP 
strategies, the observations from 18 stations in the Asia-
Pacific region on seven consecutive days are employed. In 
PPP processing, the estimator is reset every two hours to 
obtain the position solutions, and thus a total of 1464 sets 
of 2-hour position solutions are counted. When the horizon­
tal positioning errors are less than 20 cm and the vertical 
positioning errors are less than 40 cm within 10 consecu­
tive epochs (i.e., 5 min) (CSNO 2021; EUSPA 2023), the 
position solutions are considered to have converged. The 
distribution of convergence time is plotted in Fig. 6. The 
proportion of real-time PPP solutions with a convergence 
time longer than 90 min is represented as a 90-minute sta­
tistic in Fig. 6, and the average convergence time of each 
strategy is also provided in each panel. It can be seen that 
the B2b C/G + HAS E strategy achieves the shortest con­
vergence time of 9.4 min on average, followed by B2b C/G 
and HAS E/G + B2b C strategies with an average conver­
gence time of 12.3 and 12.2 min, respectively. In contrast, 
the HAS E/G strategy exhibits the slowest convergence per­
formance with an average convergence time of 21.7 min. 
The real-time PPP solutions with a convergence time less 
Fig. 6  Distribution of convergence time for four real-time PPP 
strategies
 
Fig. 5  Epoch-wise positioning errors for four real-time PPP strategies 
at station POL2 on DOY 186 of 2024
 
Fig. 4  Epoch-wise positioning errors for four real-time PPP strategies 
at station JDPR on DOY 186 of 2024
 
1 3
  162 
 
Page 8 of 11

> [3 Figure(s)]

<!-- PAGE: 9 -->

GPS Solutions          (2025) 29:162 
statistics of positioning errors over all available epochs for 
each real-time PPP strategy are calculated and shown in 
each panel. The results indicate that the B2b C/G + HAS E 
strategy can achieve the highest positioning accuracy, fol­
lowed by B2b C/G and HAS E/G + B2b C strategies, while 
the HAS E/G strategy has the lowest positioning accuracy. 
The real-time PPP solutions with a positioning accuracy 
better than 10/10/20  cm in the east/north/up directions 
account for 96.2%/98.4%/95.2%, 97.5%/99.3%/96.7%, 
80.3%/88.3%/84.1%, and 95.3%/97.7%/93.5% for the B2b 
C/G, B2b C/G + HAS E, HAS E/G, and HAS E/G + B2b C 
strategies, respectively. Compared with the B2b C/G strat­
egy, the positioning accuracy of B2b C/G + HAS E strategy 
is improved by 9%/6%/7% in the east/north/up directions, 
respectively, with the RMS statistics being 4.2/3.2/9.1 cm 
and 4.6/3.4/9.8  cm for the two strategies, respectively. 
Similarly, compared with the HAS E/G strategy, the HAS 
E/G + B2b C strategy improves the positioning accuracy 
by 36%/35%/24% in the three directions, respectively, and 
the corresponding RMS statistics are 4.8/4.1/10.6 cm and 
7.5/6.3/13.9 cm for the two strategies, respectively.
By comparing the convergence time and positioning 
accuracy among the four real-time PPP strategies, it can 
than 10/20 min account for 59.6%/87.4%, 72.4%/92.6%, 
35.1%/64.3%, and 58.6%/86.9% for the B2b C/G, B2b 
C/G + HAS E, HAS E/G, and HAS E/G + B2b C strate­
gies, respectively. The average convergence time of B2b 
C/G + HAS E strategy is shortened by 2.9  min compared 
with the B2b C/G strategy, with an improvement of 24%, 
which can be reflected in the increase of the proportion of 
position solutions with a convergence time shorter than 
15 min. Compared with the HAS E/G strategy, the average 
convergence time of HAS E/G + B2b C strategy is short­
ened by 9.5 min and the improvement rate is 44%, which 
is reflected not only in the increased proportion of position 
solutions with a convergence time less than 15 min, but also 
in the significantly reduced proportion of real-time PPP 
solutions with a convergence time over 90 min.
To evaluate the kinematic positioning accuracy of four 
real-time PPP strategies, the observations from 18 sta­
tions in the Asia-Pacific region on seven consecutive days 
are processed every 24 h. To avoid the influence of posi­
tion solutions in the converging stage, the results within the 
first two hours of each day are removed. Figure 7 shows the 
distribution of the absolute value of epoch-wise positioning 
errors for all available epochs. The root mean square (RMS) 
Fig. 7  Distribution of positioning accuracy for four real-time PPP strategies
 
1 3
Page 9 of 11 
  162

> [1 Figure(s)]

<!-- PAGE: 10 -->

GPS Solutions          (2025) 29:162 
12.2 min, respectively. By contrast, the HAS E/G strategy 
has the longest convergence time at 21.7 min. Compared 
with the B2b C/G strategy, the convergence time of the B2b 
C/G + HAS E strategy is shortened by 24%, while the con­
vergence time of the HAS E/G + B2b C strategy is shortened 
by 44% over the HAS E/G strategy. As for the positioning 
accuracy, the comparative results are similar to those of con­
vergence time. The B2b C/G + HAS E strategy performs the 
best, followed by B2b C/G and HAS E/G + B2b C strategies, 
while the HAS E/G strategy ranks the lowest in the posi­
tioning accuracy. The positioning accuracy of the B2b C/G 
strategy can reach 4.6, 3.4 and 9.8 cm in the east, north and 
up directions, respectively, whereas the positioning accu­
racy of the B2b C/G + HAS E strategy can be improved by 
9%, 6% and 7% to 4.2, 3.2 and 9.1 cm over the B2b C/G 
strategy in the three directions, respectively. The position­
ing accuracy of the HAS E/G strategy can reach 7.5, 6.3 and 
13.9 cm in the three directions, respectively, while the posi­
tioning accuracy of the HAS E/G + B2b C strategy can be 
improved by 36%, 35% and 24% compared with the HAS 
E/G strategy in the three directions, reaching 4.8, 4.1 and 
10.6 cm, respectively.
In summary, the tightly integrated real-time PPP with 
PPP-B2b and HAS in the Asia-Pacific region can signifi­
cantly shorten the convergence time and improve the posi­
tioning accuracy compared with a stand-alone augmentation 
service, which verifies the effectiveness of the proposed 
model. However, the precise correction products of HAS 
service are generated by few monitoring stations in the 
Asia-Pacific region, and the HAS service does not commit 
to guaranteeing the positioning performance in the Asia-
Pacific region. Therefore, the two HAS-based strategies, 
namely using the stand-alone HAS service and integrating 
the PPP-B2b BDS-3 observations into the HAS service, may 
not be as effective as expected in this region. It is expected 
that the positioning performance of tightly integrated real-
time PPP with the two augmentation services will be further 
improved as their service levels develop in the future.
Acknowledgements  The contribution of data from MGEX is appreci­
ated.
Author contributions  All authors contributed to the study and design. 
CY performed material preparation, data collection, and analysis. LP 
and CY wrote the first draft of the manuscript, and all authors com­
mented on previous versions of the manuscript. All authors read and 
approved the final manuscript.
Funding  This research was funded by the National Natural Science 
Foundation of China (Grant No. 42388102), and the Department of 
Natural Resources of Hunan Province (Grant No. HNGTCH-2023-05).
Data availability  The datasets at selected MGEX stations can be 
obtained from http://igs.gnsswhu.cn.
be found that the positioning performance of the HAS E/G 
strategy is significantly worse than that of the B2b C/G 
strategy. Even after the introduction of BDS-3 observations 
with PPP-B2b service, the positioning performance of the 
HAS E/G + B2b C strategy still remains inferior to that of 
the B2b C/G strategy. It is indicated that the positioning per­
formance of HAS service is worse than that of PPP-B2b 
service in the Asia-Pacific region. This is because there are 
few monitoring stations used to generate the precise cor­
rection products of HAS service in the Asia-Pacific region, 
and in fact, the HAS service does not commit to guarantee­
ing the positioning performance in the Asia-Pacific region 
(EUSPA 2023). Despite this, both the convergence time and 
positioning accuracy can be significantly improved by inte­
grating the HAS-based Galileo observations into the PPP-
B2b service.
Conclusions
Considering that the service areas of BDS-3 PPP-B2b and 
Galileo HAS overlap in the Asia-Pacific region, and there 
is potential for interoperability between the two services 
in terms of supported satellite constellations, a tightly inte­
grated real-time PPP model with PPP-B2b and HAS for the 
Asia-Pacific region is constructed in this study. Four real-
time PPP strategies, including B2b C/G, B2b C/G + HAS E, 
HAS E/G, and HAS E/G + B2b C, are used for compara­
tive analysis in terms of availability, convergence time, and 
positioning accuracy.
Regarding the availability in the Asia-Pacific region, 
among the four real-time PPP strategies, the number of 
visible satellites of B2b C/G + HAS E and HAS E/G + B2b 
C strategies is at a similar level, ranging from about 16 to 
24, and the distribution characteristics of PDOP values are 
closely related to the number of visible satellites, with the 
corresponding statistics being 1.06 to 1.41 and 1.07 to 1.25 
for the two strategies, respectively. The B2b C/G strategy 
has the smallest number of visible satellites in the Pacific 
region, with the minimum value being 9.3, and the PDOP 
value can reach as high as 3.01. By contrast, in the mainland 
of China and its coastal regions, the number of visible satel­
lites is increased to 14.9–16.5, and the corresponding PDOP 
value is relatively smaller, with a minimum value of 1.28. 
For the HAS E/G strategy, the number of visible satellites 
varies within a range of 12.9 to 16.2, and the PDOP values 
fluctuate between 1.35 and 1.62. In the Asia-Pacific region, 
all four real-time PPP strategies can achieve a service rate 
of 100%.
The convergence time of B2b C/G + HAS E strategy is the 
shortest at 9.4 min, while the B2b C/G and HAS E/G + B2b 
C strategies have a similar convergence time of 12.3 and 
1 3
  162 
 
Page 10 of 11

<!-- PAGE: 11 -->

GPS Solutions          (2025) 29:162 
Xu Y, Yang Y, Li J (2021) Performance evaluation of BDS-3 PPP-B2b 
precise point positioning service. GPS Solut 25(4):142. ​h​t​t​p​s​:​/​/​d​o​
i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​2​1​-​0​1​1​7​5​-​2
Xu X, Nie Z, Wang Z et al (2023) An improved BDS-3 PPP-B2b posi­
tioning approach by estimating signal in space range errors. GPS 
Solut 27(3):110. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​2​3​-​0​1​4​5​5​-​z
Yang Y, Li J, Xu J et al (2011) Contribution of the compass satel­
lite navigation system to global PNT users. Chin Sci Bull 
56(26):2813–2819. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​1​4​3​4​-​0​1​1​-​4​6​2​7​-​4
Zhang R, Tu R, Lu X (2024a) HASPPP: an open-source Galileo HAS 
embeddable RTKLIB decoding package. GPS Solut 28(4):169. ​h​
t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​2​4​-​0​1​7​0​6​-​7
Zhang R, Tu R, Lu X et al (2024b) Initial and comprehensive analysis 
of PPP time transfer based on Galileo high accuracy service. GPS 
Solut 28(2):94. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​2​4​-​0​1​6​3​3​-​7
Zhou P, Xiao G, Du L (2024) Initial performance assessment of Gali­
leo high accuracy service with software-defined receiver. GPS 
Solut 28(1):2. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​2​3​-​0​1​5​4​0​-​3
Publisher’s note  Springer Nature remains neutral with regard to juris­
dictional claims in published maps and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds 
exclusive rights to this article under a publishing agreement with the 
author(s) or other rightsholder(s); author self-archiving of the accepted 
manuscript version of this article is solely governed by the terms of 
such publishing agreement and applicable law.
Lin Pan   is currently an associate professor at 
Central South University. He received a Ph.D. 
degree in Geodesy and Engineering Survey­
ing from Wuhan University in 2018. His cur­
rent research mainly focuses on GNSS precise 
positioning and its application.
Chen Yang   is currently a master’s candidate 
at Central South University. He received his 
B.Sc. degree in Surveying Engineering from 
Nanjing Tech University in 2023. His current 
research 
focuses 
on 
GNSS 
precise 
positioning.
Declarations
Ethics approval and consent to participate  Not applicable.
Competing interests  The authors declare no competing interests.
References
Borio D, Susi M, Gioia C (2023) GHASP: a Galileo HAS parser. GPS 
Solut 27(4):197. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​2​3​-​0​1​5​2​9​-​y
CSNO (2021) BeiDou Navigation Satellite System Open Service Per­
formance Standard. China Satellite Navigation Office, Beijing, 
Version 3.0, May 2021. ​h​t​t​p​:​/​/​w​w​w​.​b​e​i​d​o​u​.​g​o​v​.​c​n​/​x​t​/​g​f​x​z​/​2​0​2​1​0​
5​/​P​0​2​0​2​1​0​5​2​6​2​1​6​2​3​1​1​3​6​2​3​8​.​p​d​f
Elsobeiey M, Al-Harbi S (2016) Performance of real-time precise point 
positioning using IGS real-time service. GPS Solut 20(3):565–
571. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​1​5​-​0​4​6​7​-​z
EUSPA (2023) Galileo High Accuracy Service: Service Definition 
Document (HAS SDD). European Union Agency for the Space 
Programme, Prague, Version 1.0, January 2023. ​h​t​t​p​s​:​/​/​w​w​w​.​g​s​
c​-​e​u​r​o​p​a​.​e​u​/​s​i​t​e​s​/​d​e​f​a​u​l​t​/​f​​i​l​e​s​/​s​i​t​e​s​/​a​l​l​/​f​​i​l​e​s​/​G​a​l​i​l​e​o​-​H​A​S​-​S​D​D​_​v​
1​.​0​.​p​d​f
EUSPA (2022) Galileo High Accuracy Service: Signal-In-Space Inter­
face Control Document (HAS SIS ICD). European Union Agency 
for the Space Programme, Prague, Version 1.0, May 2022. ​h​t​t​p​s​:​
/​/​w​w​w​.​g​s​c​-​e​u​r​o​p​a​.​e​u​/​s​i​t​e​s​/​d​e​f​a​u​l​t​/​f​​i​l​e​s​/​s​i​t​e​s​/​a​l​l​/​f​​i​l​e​s​/​G​a​l​i​l​e​o​_​H​A​
S​_​S​I​S​_​I​C​D​_​v​1​.​0​.​p​d​f
Fernandez-Hernandez I, Chamorro-Moreno A, Cancela-Diaz S et al 
(2022) Galileo high accuracy service: initial definition and per­
formance. GPS Solut 26(3):65. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​
2​2​-​0​1​2​4​7​-​x
Kan H, Hu Z, Chen G et al (2024) Performance comparison of orbit 
and clock augmentation corrections from PPP-B2b, HAS and 
CLAS. Adv Space Res 74(2):668–681. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​
.​a​s​r​.​2​0​2​4​.​0​4​.​0​2​9
Naciri N, Yi D, Bisnath S et al (2023) Assessment of Galileo high 
accuracy service (HAS) test signals and preliminary positioning 
performance. GPS Solut 27(2):73. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​
1​-​0​2​3​-​0​1​4​1​0​-​y
Nie Z, Gao Y, Wang Z et al (2018) An approach to GPS clock predic­
tion for real-time PPP during outages of RTS stream. GPS Solut 
22(1):14. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​1​7​-​0​6​8​1​-​y
Ouyang C, Shi J, Peng W et al (2023) Exploring characteristics of 
BDS-3 PPP-B2b augmentation messages by a three-step analysis 
procedure. GPS Solut 27(3):119. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​
1​-​0​2​3​-​0​1​4​5​7​-​x
Prol FS, Kirkko-Jaakkola M, Horst O et al (2024) Enabling the Galileo 
high accuracy service with open-source software: integration of 
HASlib and RTKLIB. GPS Solut 28(2):71. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​
7​/​s​1​0​2​9​1​-​0​2​4​-​0​1​6​1​7​-​7
Sun S, Wang M, Liu C et al (2023) Long-term performance analysis of 
BDS-3 precise point positioning (PPP-B2b) service. GPS Solut 
27(2):69. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​2​3​-​0​1​4​0​9​-​5
Tang C, Hu X, Chen J et al (2022) Orbit determination, clock Estima­
tion and performance evaluation of BDS-3 PPP-B2b service. J 
Geodesy 96(9):60. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​0​0​1​9​0​-​0​2​2​-​0​1​6​4​2​-​9
Tao J, Liu J, Hu Z et al (2021) Initial assessment of the BDS-3 PPP-
B2b RTS compared with the CNES RTS. GPS Solut 25(4):131. ​h​
t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​2​1​-​0​1​1​6​8​-​1
Wu P, Lou Y, Zhang W et al (2023) Evaluation of real-time kinematic 
positioning performance of the BDS–3 PPP service on B2b sig­
nal. GPS Solut 27(4):192. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​9​1​-​0​2​3​-​0​
1​5​3​2​-​3
1 3
Page 11 of 11 
  162

> [2 Figure(s)]
