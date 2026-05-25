<!-- PAGE: 1 -->

GPS Solutions (2025) 29:162
https://doi.org/10.1007/s10291-025-01925-6
RESEARCH
BDS-3 PPP-B2b and Galileo HAS tightly integrated real-time PPP
Lin Pan1 · Chen Yang1
Received: 9 October 2024 / Accepted: 28 June 2025
© The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2025
Abstract
The BDS-3 PPP-B2b of China can offer BDS-3/GPS real-time precise point positioning (PPP) service in the Asia-Pacific
region, while the Galileo High Accuracy Service (HAS) of the European Union can offer Galileo/GPS real-time PPP
service worldwide. Their service areas have a geographical overlap in the Asia-Pacific region and there is potential for
their interoperability in terms of supported satellite systems. In this study, a tightly integrated real-time PPP model by
incorporating observations from complementary constellations of PPP-B2b and HAS (rather than combining their PPP
results) based on respective stand-alone service for the Asia-Pacific region is constructed. For comparison, we employ the
strategy with BDS-3/GPS from PPP-B2b (B2b C/G), the strategy with Galileo/GPS from HAS (HAS E/G), the strategy
with BDS-3/GPS from PPP-B2b and Galileo from HAS (B2b C/G + HAS E), and the strategy with Galileo/GPS from
HAS and BDS-3 from PPP-B2b (HAS E/G + B2b C). The datasets from 18 stations over a week are employed. The B2b
C/G + HAS E strategy has the best performance, followed by B2b C/G and HAS E/G + B2b C strategies, while the per-
formance of HAS E/G strategy is the worst. The B2b C/G + HAS E strategy can provide a convergence time (processed
every two hours) of 9.4 min with a threshold of 20/40 cm in horizontal/vertical directions, and a positioning accuracy
(processed every 24 h) of 4.2/3.2/9.1 cm in east/north/up directions. Therefore, benefiting from the increased satellite
number and improved satellite geometry, the integration of PPP-B2b and HAS can significantly improve the real-time
PPP performance compared with respective stand-alone service.
Keywords BDS-3 PPP-B2b · Galileo HAS · Real-time precise point positioning · Tight integration · Satellite
communication
Introduction (Nie et al. 2018; Elsobeiey and Al-Harbi 2016). However,
the implementation of RTS relies on a stable network com-
Precise point positioning (PPP) technology enables users munication environment, which restricts the application of
to achieve high-precision positioning with a single receiver real-time PPP technology in areas with insufficient network
through the joint use of code and carrier phase observations coverage, such as deserts and oceans. In recent years, the
as well as precise satellite orbit and clock products. With BDS-3 PPP-B2b of China and the Galileo High Accuracy
the ongoing advancement of PPP technology and the rapidly Service (HAS) of the European Union (EU) have been
increasing demand for real-time precise positioning, real- transmitting real-time precise correction products via satel-
time PPP has become a research hotspot. The international lite-based broadcasting. PPP-B2b and HAS can realize the
Global Navigation Satellite System (GNSS) service (IGS) real-time precise positioning independent of network com-
has been delivering real-time precise correction products via munication, which presents a new solution for wide-area
Internet, providing users with real-time service (RTS) that real-time high-precision positioning.
can achieve decimeter-to-centimeter positioning accuracy Many scholars have evaluated the quality of precise cor-
rections and the positioning performance of BDS-3 PPP-
B2b service since its launch in 2020. The results indicated
that the accuracy of satellite orbits and clock offsets was at
Lin Pan
the centimeter level and within 0.2 ns, respectively, and the
linpan@csu.edu.cn
satellite clock offsets presented a systematic bias. Moreover,
1 School of Geosciences and Info-Physics, Central South the availability of PPP-B2b precise corrections was more
University, Changsha 410083, China
1 3

<!-- PAGE: 2 -->

162 Page 2 of 11 GPS Solutions (2025) 29:162
than 90% in China, and the kinematic positioning accuracy or software such as HASlib, GHASP, and HASPPP to facili-
of real-time PPP could reach centimeter level after conver- tate the decoding and integration of HAS corrections (Borio
gence (Xu et al. 2021; Tao et al. 2021). Tang et al. (2022) et al. 2023; Zhang et al. 2024a; Prol et al. 2024).
provided a detailed description of the generation strategies BDS-3 PPP-B2b can provide real-time PPP service in
for various PPP-B2b correction products, and conducted a the Asia-Pacific region, while Galileo HAS is able to pro-
comprehensive evaluation of the quality of PPP-B2b precise vide real-time PPP service for global users. Thus, the ser-
corrections. In addition, several researchers also focused vice areas of PPP-B2b and HAS overlap in the Asia-Pacific
on these aspects and derived comparable results (Wu et al. region. Moreover, PPP-B2b service supports BDS-3 and
2023; Ouyang et al. 2023). With regard to the systematic bias GPS constellations, while HAS service supports Gali-
in PPP-B2b satellite clock offsets, Sun et al. (2023) derived leo and GPS constellations. Therefore, there is potential
its estimate by taking the post-processed precise ephemeri- for interoperability between PPP-B2b and HAS services
des as a reference, and then the corrected PPP-B2b satellite regarding the supported satellite constellations. This study
clock offsets by the estimate were applied to the real-time constructs a tightly integrated real-time PPP model with the
PPP processing. Alternatively, Xu et al. (2023) introduced joint use of PPP-B2b and HAS precise corrections in the
an additional parameter to compensate for the systematic Asia-Pacific region. For completeness, four real-time PPP
bias in the real-time PPP processing. Both approaches sig- strategies are analyzed and compared, including the stand-
nificantly improved the convergence speed of real-time PPP. alone PPP-B2b strategy, stand-alone HAS strategy, and two
The Galileo HAS Signal-In-Space (SIS) testing activities PPP-B2b and HAS integration strategies. We first introduce
were conducted in the 2020–2022 timeframe. Fernandez- the recovery of precise correction products and uniformity
Hernandez et al. (2022) provided a detailed explanation of of datum. Next, the PPP-B2b and HAS tightly integrated
the message structure for Galileo HAS, including the orga- real-time PPP model is constructed. Then, the results are
nization and transmission mode of correction data, as well presented and discussed. Finally, the main conclusions are
as how HAS uses Galileo monitoring stations and uplinks to summarized.
provide services. HAS delivers precise correction products
through the E6-B signal of Galileo satellites, and provides
high-precision real-time PPP service to global users. The Recovery of precise correction products and
EU Agency for the Space Programme (EUSPA) officially uniformity of datum
announced that Galileo provided the initial HAS service on
January 24, 2023. Since then, a number of scholars have The orbit and clock corrections of PPP-B2b refer to the
conducted research on the availability, the quality of satel- legacy navigation message (LNAV) of GPS and the civil
lite orbit and clock corrections, and the positioning perfor- navigation message on B1C frequency (CNAV1) of BDS-3,
mance of Galileo HAS. Zhang et al. (2024b) evaluated the while HAS provides orbit and clock corrections for LNAV
number of visible satellites and the service rate of HAS on of GPS and integrity navigation message (I/NAV) of Gali-
a global scale, and the results showed that the globally aver- leo. The decoded corrections are matched with the corre-
age number of GPS and Galileo satellites with valid HAS sponding broadcast ephemerides to recover the real-time
corrections was 9.44 and 7.95, respectively, with the aver- precise satellite orbits and clock offsets, that is:
age service rate being 99.9% and 99.6% for GPS-only and
Galileo-only PPP, respectively. Zhou et al. (2024) assessed O˜ B2b =O B2b
−
R rac2xyz δO B2b
(1)
the accuracy of HAS orbit and clock correction products, {O˜
HAS
=O
HAS
−
R
ntw2xyz
(δO
HAS
+δO˙
HAS
∆t)
and analyzed the HAS-based positioning accuracy. The
results indicated that the accuracy of orbit and clock correc- cd˜ts =cdts δC /c
tions of Galileo was slightly higher than that of GPS, and cd˜ts B2b =cdts B2b− +δC B2b /c (2)
{ HAS HAS HAS
both static and kinematic positioning of HAS could reach
centimeter level. Similar results about the accuracy of HAS
correction products and the HAS-based positioning perfor- where the subscripts B2b and HAS represent PPP-B2b and
mance were also derived by some other scholars (Naciri et HAS corrections, respectively, O˜ and cd˜ts are the recovered
al. 2023; Kan et al. 2024). In addition, receivers that sup- precise satellite positions and clock offsets, respectively,
port the E6 signal can directly receive the HAS correction O and cdts are the satellite positions and clock offsets cal-
message broadcast by Galileo satellites, but this is restricted culated by broadcast ephemerides, respectively, R
rac2xyz
by the baud rate of E6-B signal and the particularity of and R represent the transformation matrix from the
ntw2xyz
HAS encoding scheme (Fernandez-Hernandez et al. 2022). radial, along-track and cross-track (RAC) coordinate sys-
Therefore, some scholars developed open-source libraries tem to the Earth-Centered Earth-Fixed (ECEF) coordinate
1 3

<!-- PAGE: 3 -->

GPS Solutions (2025) 29:162 Page 3 of 11 162
system, both of which are calculated by the satellite position frequency, so as to be consistent with the reference of the
and velocity vectors derived from broadcast ephemerides, recovered real-time precise satellite clock offsets. It should
δO represents the corrections of satellite orbits, δO˙ denotes be noted that the sign of the PPP-B2b and HAS correction
the changing rates of orbit corrections, δC represents the formulas is opposite when using the augmentation services
corrections of satellite clock offsets, ∆t is the time interval for OSB corrections (EUSPA 2022). For convenience, the
from the reference time of state-space representation (SSR) single-frequency reference is denoted by m, and the dual-
messages containing orbit corrections to the current time, frequency reference is denoted by m and n. Thus, the spe-
and c is the speed of light in a vacuum. cific components of the recovered real-time precise satellite
Table 1 lists the datums of recovered real-time precise clock offsets can be expressed as:
satellite orbits and clock offsets of PPP-B2b and HAS. The
r th ef e e i r n e s n t c a e n t o a f n e G o N us S S an c te o n d n e a a p n h d a s c e a r c ri e e n r t e p r h ( a A se P C ob ) s o e f r v th at e i o s n a s te i l s - { cd˜ts I c F d˜ ,m ts m n = = c c d d t t s s − − d d s m s IF,mn (4)
lite and the receiver. However, the orbit corrections pro-
vided by PPP-B2b refer to the L1/L2 ionospheric-free (IF) ds IF,mn =a mn,m · ds m +a mn,n · ds n (5)
combined APC for GPS and the B3 APC for BDS-3, respec-
with a =f2/(f2 f2) and a = f2/(f2 f2)
tively, and the corresponding reference of orbit corrections mn,m m m− n mn,n − n m− n
where a and a are the dual-frequency IF combina-
provided by HAS is the L1 APC and E1 APC for GPS and mn,m mn,n
tion coefficients, f is the carrier frequency, ds is the satel-
Galileo, respectively. To ensure the consistency, the datums
lite code hardware delay, cd˜ts denotes the precise satellite
of recovered real-time precise satellite orbits of each satel- m
lite must be converted to the center of mass (CoM) by using clock offset with a single-frequency datum, and cd˜ts IF,mn
the phase center offset (PCO) corrections in the ANTenna denotes the precise satellite clock offset with a dual-fre-
Exchange format (ANTEX) file provided by IGS, that is: quency IF combined datum.
The raw code observations contain the satellite code
O˜ COM =O˜ i,APC Tr PCO i (3) hardware delay on a single frequency, which needs to be
− ·
corrected by OSB to make them consistent with the satellite
where i denotes L1/L2 IF APC, B3 APC, L1 APC, or E1 code hardware delay included in the precise satellite clock
APC, O˜ and O˜ represent the satellite orbits refer- offsets. The BDS-3 code observations can be corrected by
APC COM
ring to the APC and CoM, respectively, Tr is a conversion OSB from PPP-B2b according to the following formula:
matrix from the satellite body-fixed coordinate system to the
ECEF coordinate system, and PCO denotes the PCO cor- P¯ j =P j′+ds j − OSB m,j =P j′+ds m (6)
rections. The reference of observations is transferred to the
CoM by applying PCO and phase center variation (PCV) where j represents the frequency, OSB represents the code
corrections for the consistency of PPP processing. OSB corrections, P represents the code observations cor-
As shown in Table 1, the clock offset datum of GPS rected by OSB, and P ′ represents the code observations
and BDS-3 in PPP-B2b products is L1P/L2P IF combina- without the satellite code hardware delay. It should be noted
tion and B3I, respectively, while that of GPS and Galileo in that the PPP-B2b product does not contain the OSB cor-
HAS products is the IF combination with L1 C/A and L2P, rections of GPS. Since the GPS satellite clock offsets from
and E1 and E5B, respectively. For real-time PPP process- PPP-B2b product take a L1/L2 dual-frequency IF combined
ing with multiple frequencies, the PPP-B2b and HAS also datum, the inconsistency of satellite code hardware delay
provide the code observable-specific signal bias (OSB) cor- between code observations and satellite clock offsets will be
rection products. Hence, we just need to directly apply the absorbed by the ionospheric delay parameter when employ-
OSB corrections to the code observations on the required ing a L1/L2 dual-frequency uncombined observation model.
The Galileo and GPS code observations can be corrected
by OSB from HAS according to the following formula:
Table 1 Datums of recovered real-time precise satellite orbits and
clock offsets of PPP-B2b and HAS
Items Systems Datums P¯ j =P j′+ds j +OSB IF,mn,j =P j′+ds IF,mn (7)
PPP-B2b HAS
Satellite orbits GPS L1 and L2 IF APC L1 APC
BDS-3 B3 APC –
Galileo – E1 APC
Clock offsets GPS L1P and L2P IF L1 C/A and L2P IF
BDS-3 B3I –
Galileo – E1 and E5B IF
1 3

<!-- PAGE: 4 -->

162 Page 4 of 11 GPS Solutions (2025) 29:162
PPP-B2b and HAS tightly integrated real- precise satellite orbits and clock offsets as well as the OSB
time PPP model corrections, the PPP-B2b and HAS tightly integrated real-
time PPP dual-frequency uncombined observation model
Since both PPP-B2b and HAS products support GPS, for can be expressed as:
ease of expression, the GPS constellation taking PPP-B2b
corrections is represented as GPS B2b, and the GPS con- ps r, , 1 sys = + µ α s r , s s , y sy s s· X Z r + + c θ d¯ s t y s r s ys D + s γ ,s 1 s y y s s · I¯ r s,sys
stellation taking HAS corrections is represented as GPS  ps,sys =µs, r sys · X r +cd¯tsys · +γsys I¯s,sys
H
a


s
A
L
f
+
o
S
s
r,
,
l
.
j
γ s
l
+
y
o
j s
T
s y
w
T
h
s = P
s
r
e
s
·
:
,
r
s
s I ρ
c
,
y
, j r s s
r
o
s
s
, , y
d
s s s
+
y y
e
s s =
N
a
+ +
n
ρ
r
s
d
,
T c s r
,
j
s
, d r s s
y
p
t y ,
s
s s
r
h
s y y
+
a
s + s
s
+
e
b −
c
s
r ,
d
y
o
d
j
c
s
t
b
d s r s r , y
+
s
t y j s
e
s s ,
r
b
+ s −
v
s
j
y
,
a
s
s
d c
t
y
i
−
s j d
s
o
,s t
n
+
γ y s
s
, s
j
s s
ε
y y +
c
s
s
r
s
a
,
,
j
s·
e
n
y
I s r
s
, ,
r
b
s j s , y
e
s s y
e
s
x press
(
e
8
d
)

 l
l
r
r
s
s
r
,
,
,
,
,
1
2
s
s
2
y
y
s
s
=
=
+
µ
µ
α
s
r
s r
r
+ +
,
,
r
s
s
s
,
y
y α α
s
s
s
y
r
r s s
s
·
· , ,
·
s s
X
X
·
y y
Z
s s
r
r
r
r
·
·
+
+ Z Z
+
r
r
c
c
θ
d
d
¯
¯ + +
s
t
t
y
s
r
s r
r
N N
s
y
y ¯ ¯
s
s
·
r
r
s s ,
,
−
−
D
, , 1
2
s s y y
s
γ
γ s s
,s
1
2
s
s
2 y
y
y
s
s
s
·
·
·
I
I
¯
¯
r
r
s
s
r
,
,
s
s
y
y
s
s
(9)
where
sys represents GPS B2b, GPS HAS, BDS-3 or Gali- θsys=
0, sys=GPS HASorGalileo
(10)
1, sys=GPS B2borBDS-3
leo, r and s represent the receiver and satellite, respectively, {
j is the frequency, P represents code observations, L repre-
cd¯tsys=cdtsys+asys dsys+asys dsys
sents carrier phase observations, ρ is the geometric distance I¯s,sys= r Is,sys+a r sys 1 ( 2 d ,1 sy·s r,1 dsys) 1 + 2, η 2 s · ys r,2 ds,sys
b re e c t e w iv ee e n r a s n a d te s ll a i t t e e l l a it n e d c r lo ec c e k i v o e ff r s , e c t d s, t r r e s a p n e d c t c i d v t e s l y r , e I p r r e e p s r e e n s t e t n h t e s   N N ¯ ¯ r s s , , , 1 −s s y y s s r as 1 = = y 2, s 2 N N · r s s ( , , , 1 1 s s y y r + s s+ + γ 1 s b b y s s r s , y y 1 ) s s 1 · + + 2 d , s r 2 b b , y 2 s 1 s · s , , s s− y y s s r, d 1 −s p , r − s ( ( e y a a s s 1 s y y 2 + r , s s , 1 2 η −sy γ γ s 1 s s· y y γ s s 1 s·y a a · s s s 1 ·y y 2 i d , s s o 2 s i n ) ) o ,s n ·y d d s s r s , y y 1 s s (11)
t i h o e n o s s l p a h n e t r i i o c n d o e s l p a h y e f r a ic c to d r e l ( a γ y
j
s y o s n = th ( e f
1
fi sy r s s / t f fr
j
s e y q s u )2 e ) n , c f y i , s γ th i e s c t a h r e -  r,2 − as 1 y 2, s 2· r ( ,2 1+γ 2 sy r s ,2 ) · ds r, y 2 2 s − d −s p , r s e ys 12 + ,1 η −sys 2 · γ 2 s·ys 1 · 2 d ,2 s io ,s n ·ys r,1
r a i n e d r d fr s e q d u en en o c te y , t h T e r r e e p c r e e i s v e e n r t a s n t d h e s a s t l e a l n li t t e tr c o o p d o e s p h h a e rd ri w c a d r e e l a d y e , l a d y r , ds p , r s e ys= { d a s m s m , y s n s y , s m , · d s s m y ,s s ys = + B a D s m y S n s - , 3 n· ds n ,sys,sys=others (12)
respectively, N is the phase ambiguity, b and bs denote the
r
receiver and satellite phase hardware delay, respectively, ηsys = 1, sys=GPS B2b (13)
and e and ε represent the measurement noises of code and 0, sys=others
{
carrier phase observations (including unmodeled errors
such as multipath effects), respectively. ds,sys =asys (ds,sys ds,sys) (14)
ion mn,n· m − n
The datums of satellite clock offsets of GPS B2b are fre-
with
asys =(fsys)2/((fsys)2 (fsys)2)
and
quently switched because the PPP-B2b products are derived 12,1 1 1 − 2
asys = (fsys)2/((fsys)2 (fsys)2) where p and l
from the regional network solutions. Therefore, a separate 12,2 − 2 1 − 2
receiver clock offset parameter should be estimated for each denote the observed-minus-computed (OMC) code and
satellite system. Alternatively, the inter-system bias (ISB) phase observables, respectively, µ denotes the unit vector
parameter should be estimated as white noise process to in the line of sight direction from the receiver to the sat-
absorb the influence of switched datums. The former method ellite, X denotes the three-dimensional (3D) coordinates
is adopted in this study. It should be noted that there is an of the receiver, cd¯t r denotes the receiver clock offset esti-
initial systematic bias in the recovered PPP-B2b precise sat- mate that absorbs the receiver code hardware delay in the
ellite clock offsets for each satellite, which can be absorbed form of the dual-frequency IF combination, I¯ denotes the
by the phase ambiguity parameter and does not affect the ionospheric delay estimate that absorbs the code hardware
carrier phase observations. However, the initial systematic delay at the receiver as well as the code hardware delay at
bias will impact the accuracy of code observations. There- the satellite (only for GPS B2b), Z denotes the tropospheric
fore, a compensating parameter is introduced into the code zenith wet delay (ZWD), α denotes the wet mapping func-
observation equation for each satellite to mitigate the effects tion, N¯ denotes the phase ambiguity estimate that absorbs
of the initial systematic bias included in satellite clock off- the code and phase hardware delay at the satellite and
sets for GPS B2b and BDS-3 constellations. Taking the final receiver, and D denotes the compensating parameter for the
satellite clock product as the reference, the errors of PPP- initial systematic bias of PPP-B2b satellite clock offsets. In
B2b satellite clock offsets exhibit relatively stable charac- Eq. (11), ds p , r s e ys denotes the satellite code hardware delay
teristics within each continuous arc. Thus, the compensating absorbed by the phase ambiguity parameter, which is intro-
parameter for the initial systematic bias is estimated as ran- duced when applying the PPP-B2b or HAS precise satel-
dom-walk process. After applying the recovered real-time lite clock offsets, and is consistent with their reference (see
1 3

<!-- PAGE: 5 -->

GPS Solutions (2025) 29:162 Page 5 of 11 162
Eq. (4)). In Eq. (11),
ds,sys
denotes satellite code hardware
ion parameter is estimated as random-walk process, the intro-
delay absorbed by the ionospheric delay parameter and then
duction of a compensating parameter into the code obser-
propagated to the phase ambiguity parameter (only for GPS
vation equation for each satellite of GPS B2b and BDS-3
B2b), which is introduced by the inconsistency of satellite
constellations will not reduce the redundancy of the real-
code hardware delay between code observations and satel-
time PPP model. Actually, the redundancy of the model
lite clock offsets. To remove the rank deficiency caused by
approximates the difference between the number of obser-
the introduction of compensating parameter for the initial
vations and the number of parameters without strong con-
systematic bias for each satellite within a constellation in
straints, such as receiver clock offset parameters.
Eq. (9), a separate pseudo-observation equation of the com-
pensating parameter with a pseudo-observable of zero for a
selected satellite for each of GPS B2b and BDS-3 constella- Results and discussion
tions can be introduced into the observation model.
In view that the pseudo-observable is introduced as The datasets and processing strategies are first introduced.
a datum to eliminate the rank deficiency, a much smaller Next, the availability is analyzed. Finally, the position solu-
magnitude should be assigned to its noise. In this study, tions are provided.
the variance of the pseudo-observable is set to 1 × 10–6 m2.
There is a strong correlation between the receiver clock off- Datasets and processing strategies
set parameter and numerous compensating parameters. By
assigning a numerical value of zero to the compensating In this study, the datasets on day of year (DOY) 180–186 of
parameter of the selected satellite, the receiver clock offset 2024 from 18 Multi-GNSS Experimental (MGEX) stations
estimates actually absorb the initial systematic bias of the located in the Asia-Pacific region are employed to evalu-
selected satellite, while the estimated compensating param- ate the performance of PPP-B2b and HAS tightly integrated
eter for other satellites is essentially the difference of ini- real-time PPP. Due to the absence of observations at cer-
tial systematic bias between these satellites and the selected tain stations on specific days (i.e., JDPR, LCK4 and IITK
satellite. Considering the regional service nature of BDS-3 stations on DOY 185 of 2024 and SGOC station on DOY
PPP-B2b, even when the selected satellite exits the service 180 of 2024), the analysis ultimately involves a total of 122
coverage, the introduced datum will propagate backward to sets of daily observations. The geographical distribution
subsequent epochs because the compensating parameter is of the selected stations is shown in Fig. 1. The stations are
modeled as random-walk process. During satellite ingress chosen according to three principles: (1) coverage within
events, compensating parameters for the newly visible sat- the PPP-B2b service area (75°E–135°E, 10°N–55°N) with
ellites require initialization, whereas compensating param- minor boundary extensions of several degrees, (2) support
eters for all satellites must undergo re-initialization upon for simultaneous tracking of BDS-3, GPS, and Galileo sig-
re-entry of the selected satellite into the service area. nals, and (3) quasi-uniform spatial distribution. As for the
Since the estimator adopts the Kalman filter, there is analysis period, while it is arbitrarily chosen, we adopt a
predicted information for the parameters with a strongly continuous 7-day period after considering the orbital repeat
constrained dynamic model. Thus, as the compensating period and the computational burden.
For comparison, four real-time PPP strategies are ana-
lyzed, including the strategy with BDS-3/GPS from PPP-
B2b (B2b C/G), the strategy with Galileo/GPS from HAS
(HAS E/G), the strategy with BDS-3/GPS from PPP-B2b
and Galileo from HAS (B2b C/G + HAS E), and the strat-
egy with Galileo/GPS from HAS and BDS-3 from PPP-B2b
(HAS E/G + B2b C). The real-time PPP processing is carried
out with the strategies summarized in Table 2.
Availability
The availability analysis presented in this study is concen-
trated on the Asia-Pacific region with specific geographical
ranges from latitude 0° to 60°N and longitude 60°E to 180°.
The service rates, the number of visible satellites, and the
Fig. 1 Geographical distribution of 18 MGEX stations located in the position dilution of precision (PDOP) for four real-time PPP
Asia-Pacific region
1 3

<!-- PAGE: 6 -->

162 Page 6 of 11 GPS Solutions (2025) 29:162
Table 2 Processing strategies for real-time PPP strategies (namely B2b C/G, B2b C/G + HAS E, HAS E/G,
Items Strategies
and HAS E/G + B2b C) are analyzed. To ensure the consis-
Frequencies BDS-3: B1/B3
tency with the positioning strategies, the sampling interval
GPS: L1/L2
is set to 30 s, and the cut-off elevation angle is set to 10°. The
Galileo: E1/E5A
Positioning mode Kinematic research area is divided into 60 × 60 grids with an interval of
Weighting method Elevation-dependent weights 2° in longitude and 1° in latitude, and it is assumed that a
Sampling rate 30 s virtual receiver at an altitude of 25 m is placed in the center
Elevation cut-off angle 10° of each grid (Yang et al. 2011). Subsequently, the relative
PCO/PCV PPP-B2b: IGS20 atx file geometries between each satellite and the virtual receiver
HAS: IGS14 atx file
are analyzed to evaluate the availability of four real-time
Phase wind-up effect Corrected
PPP strategies by combining the known receiver positions
Relativistic effect Corrected
and the calculated satellite positions.
Station displacement Corrected with IERS Convention 2010
When there are at least four visible satellites and the
Satellite orbit/clock/ Broadcast ephemerides with correspond-
code bias ing augmentation products PDOP values are less than 30 at a certain epoch, the posi-
Receiver clock A separate receiver clock offset parameter tion determination at this epoch is considered to be feasible.
is estimated for each satellite system, and In this study, the service rate is defined as the percentage of
modeled as white noise process (104 m2) the number of epochs with feasible position solutions over
Ionospheric delay Estimated as random-walk process (10–4
the total number of epochs. The service rate for each grid is
m2/s)
calculated. The results indicate that all four real-time PPP
Tropospheric delay Dry component: Saastamoinen model
Wet component: mapping slant delays to strategies can achieve a service rate of 100% in the Asia-
zenith delays with global mapping func- Pacific region, which means that even the stand-alone PPP-
tion (GMF) and estimated as random- B2b service and the stand-alone HAS service can provide
walk process (10–8 m2/s)
continuous positioning services for users in the Asia-Pacific
Phase ambiguity Estimated as float constants
region.
Compensating param- Estimated as random-walk process (10–10
eter for initial system- m2/s) over each continuous arc Figure 2 illustrates the geographical distribution of the
atic bias average number of visible satellites over seven days from
DOY 180 to 186 of 2024 for four real-time PPP strategies.
Fig. 2 Geographical distribution of the average number of visible satellites for four real-time PPP strategies
1 3

<!-- PAGE: 7 -->

GPS Solutions (2025) 29:162 Page 7 of 11 162
The number of visible satellites under the B2b C/G strategy Figure 3 displays the geographical distribution of aver-
is relatively larger in the mainland of China and its coastal age PDOP values over the entire analysis period for four
regions, especially within the range of 12°N to 48°N and real-time PPP strategies. The B2b C/G + HAS E strategy
90°E to 130°E, with the corresponding satellite numbers integrating HAS Galileo presents lower PODP values in
ranging from 14.9 to 16.5. In addition, the visible satellite contrast to the B2b C/G strategy that only employs PPP-B2b
numbers present a decreasing trend towards surrounding products. Similarly, the HAS E/G + B2b C strategy that inte-
areas in a circular pattern, with the lowest number in the grates PPP-B2b BDS-3 also exhibits lower PODP values
Pacific region being 9.3. After integrating with HAS Gali- compared with the HAS E/G strategy. The PDOP values of
leo, the number of visible satellites increases significantly, the B2b C/G and B2b C/G + HAS E strategies are relatively
ranging from 16.6 to 22.9, and the distribution character- smaller within the range of 80°E to 140°E, particularly in
istics of satellite numbers are consistent with those of the the mainland of China, with the minimum values of 1.28 and
B2b C/G strategy (i.e., more visible satellites in the central 1.06, respectively. In the areas of 60°E to 80°E and 140°E
regions and less visible satellites in the peripheral regions). to 180°, the PDOP values of B2b C/G and B2b C/G + HAS
The number of visible satellites under the HAS E/G strat- E strategies gradually increase towards both sides, ranging
egy is mainly concentrated in the areas spanning 0° to 12°N from 1.39 to 3.01 and 1.11 to 1.41, respectively. For the
and 50°N to 60°N, with the corresponding satellite num- other two strategies, the distribution of PDOP values is rela-
bers ranging from 13.2 to 16.2. However, in the mainland tively even, ranging from 1.35 to 1.62 for HAS E/G strategy
of China and its coastal regions, the number of visible satel- and from 1.07 to 1.25 for HAS E/G + B2b C strategy. After
lites under the HAS E/G strategy is relatively smaller, with an integration with PPP-B2b BDS-3, the HAS E/G + B2b C
a varying range of 12.9 to 14.8. After integrating with PPP- PDOP values within the latitude range from 12°N to 40°N
B2b BDS-3, the distribution characteristics of the satellite are still slightly higher than those in other regions, espe-
numbers are consistent with those of the HAS E/G strat- cially in the longitude range from 150°E to 180°.
egy, and there are less visible satellites (ranging from 18.7
to 21.2) in the regions spanning 12°N to 50°N (especially Position solutions
in the regions of 160°E to 180°), while the corresponding
numbers increase to 23.3 in other regions. Figures 4 and 5 depict the epoch-wise positioning errors for
four real-time PPP strategies (i.e., B2b C/G, B2b C/G + HAS
Fig. 3 Geographical distribution of average PDOP values for four real-time PPP strategies
1 3

<!-- PAGE: 8 -->

162 Page 8 of 11 GPS Solutions (2025) 29:162
Fig. 6 Distribution of convergence time for four real-time PPP
strategies
E, HAS E/G, and HAS E/G + B2b C) at stations JDPR and
POL2 on DOY 186 of 2024, respectively. As can be seen
from the two figures, the position solutions of all the four
real-time PPP strategies can quickly converge to the target
accuracy of PPP-B2b and HAS services (i.e., 20 cm in hori-
Fig. 4 Epoch-wise positioning errors for four real-time PPP strategies zontal direction and 40 cm in vertical direction). The posi-
at station JDPR on DOY 186 of 2024 tioning accuracy in the east and north directions is usually
better than 10 cm after convergence, while the correspond-
ing accuracy in the up direction is usually better than 20 cm.
It should be noted that the stability of position solutions of
HAS E/G strategy is inferior to that of the other three strate-
gies after the position filter converges.
To evaluate the convergence time of four real-time PPP
strategies, the observations from 18 stations in the Asia-
Pacific region on seven consecutive days are employed. In
PPP processing, the estimator is reset every two hours to
obtain the position solutions, and thus a total of 1464 sets
of 2-hour position solutions are counted. When the horizon-
tal positioning errors are less than 20 cm and the vertical
positioning errors are less than 40 cm within 10 consecu-
tive epochs (i.e., 5 min) (CSNO 2021; EUSPA 2023), the
position solutions are considered to have converged. The
distribution of convergence time is plotted in Fig. 6. The
proportion of real-time PPP solutions with a convergence
time longer than 90 min is represented as a 90-minute sta-
tistic in Fig. 6, and the average convergence time of each
strategy is also provided in each panel. It can be seen that
the B2b C/G + HAS E strategy achieves the shortest con-
vergence time of 9.4 min on average, followed by B2b C/G
and HAS E/G + B2b C strategies with an average conver-
gence time of 12.3 and 12.2 min, respectively. In contrast,
Fig. 5 Epoch-wise positioning errors for four real-time PPP strategies the HAS E/G strategy exhibits the slowest convergence per-
at station POL2 on DOY 186 of 2024 formance with an average convergence time of 21.7 min.
The real-time PPP solutions with a convergence time less
1 3

<!-- PAGE: 9 -->

GPS Solutions (2025) 29:162 Page 9 of 11 162
Fig. 7 Distribution of positioning accuracy for four real-time PPP strategies
than 10/20 min account for 59.6%/87.4%, 72.4%/92.6%, statistics of positioning errors over all available epochs for
35.1%/64.3%, and 58.6%/86.9% for the B2b C/G, B2b each real-time PPP strategy are calculated and shown in
C/G + HAS E, HAS E/G, and HAS E/G + B2b C strate- each panel. The results indicate that the B2b C/G + HAS E
gies, respectively. The average convergence time of B2b strategy can achieve the highest positioning accuracy, fol-
C/G + HAS E strategy is shortened by 2.9 min compared lowed by B2b C/G and HAS E/G + B2b C strategies, while
with the B2b C/G strategy, with an improvement of 24%, the HAS E/G strategy has the lowest positioning accuracy.
which can be reflected in the increase of the proportion of The real-time PPP solutions with a positioning accuracy
position solutions with a convergence time shorter than better than 10/10/20 cm in the east/north/up directions
15 min. Compared with the HAS E/G strategy, the average account for 96.2%/98.4%/95.2%, 97.5%/99.3%/96.7%,
convergence time of HAS E/G + B2b C strategy is short- 80.3%/88.3%/84.1%, and 95.3%/97.7%/93.5% for the B2b
ened by 9.5 min and the improvement rate is 44%, which C/G, B2b C/G + HAS E, HAS E/G, and HAS E/G + B2b C
is reflected not only in the increased proportion of position strategies, respectively. Compared with the B2b C/G strat-
solutions with a convergence time less than 15 min, but also egy, the positioning accuracy of B2b C/G + HAS E strategy
in the significantly reduced proportion of real-time PPP is improved by 9%/6%/7% in the east/north/up directions,
solutions with a convergence time over 90 min. respectively, with the RMS statistics being 4.2/3.2/9.1 cm
To evaluate the kinematic positioning accuracy of four and 4.6/3.4/9.8 cm for the two strategies, respectively.
real-time PPP strategies, the observations from 18 sta- Similarly, compared with the HAS E/G strategy, the HAS
tions in the Asia-Pacific region on seven consecutive days E/G + B2b C strategy improves the positioning accuracy
are processed every 24 h. To avoid the influence of posi- by 36%/35%/24% in the three directions, respectively, and
tion solutions in the converging stage, the results within the the corresponding RMS statistics are 4.8/4.1/10.6 cm and
first two hours of each day are removed. Figure 7 shows the 7.5/6.3/13.9 cm for the two strategies, respectively.
distribution of the absolute value of epoch-wise positioning By comparing the convergence time and positioning
errors for all available epochs. The root mean square (RMS) accuracy among the four real-time PPP strategies, it can
1 3

<!-- PAGE: 10 -->

162 Page 10 of 11 GPS Solutions (2025) 29:162
be found that the positioning performance of the HAS E/G 12.2 min, respectively. By contrast, the HAS E/G strategy
strategy is significantly worse than that of the B2b C/G has the longest convergence time at 21.7 min. Compared
strategy. Even after the introduction of BDS-3 observations with the B2b C/G strategy, the convergence time of the B2b
with PPP-B2b service, the positioning performance of the C/G + HAS E strategy is shortened by 24%, while the con-
HAS E/G + B2b C strategy still remains inferior to that of vergence time of the HAS E/G + B2b C strategy is shortened
the B2b C/G strategy. It is indicated that the positioning per- by 44% over the HAS E/G strategy. As for the positioning
formance of HAS service is worse than that of PPP-B2b accuracy, the comparative results are similar to those of con-
service in the Asia-Pacific region. This is because there are vergence time. The B2b C/G + HAS E strategy performs the
few monitoring stations used to generate the precise cor- best, followed by B2b C/G and HAS E/G + B2b C strategies,
rection products of HAS service in the Asia-Pacific region, while the HAS E/G strategy ranks the lowest in the posi-
and in fact, the HAS service does not commit to guarantee- tioning accuracy. The positioning accuracy of the B2b C/G
ing the positioning performance in the Asia-Pacific region strategy can reach 4.6, 3.4 and 9.8 cm in the east, north and
(EUSPA 2023). Despite this, both the convergence time and up directions, respectively, whereas the positioning accu-
positioning accuracy can be significantly improved by inte- racy of the B2b C/G + HAS E strategy can be improved by
grating the HAS-based Galileo observations into the PPP- 9%, 6% and 7% to 4.2, 3.2 and 9.1 cm over the B2b C/G
B2b service. strategy in the three directions, respectively. The position-
ing accuracy of the HAS E/G strategy can reach 7.5, 6.3 and
13.9 cm in the three directions, respectively, while the posi-
Conclusions tioning accuracy of the HAS E/G + B2b C strategy can be
improved by 36%, 35% and 24% compared with the HAS
Considering that the service areas of BDS-3 PPP-B2b and E/G strategy in the three directions, reaching 4.8, 4.1 and
Galileo HAS overlap in the Asia-Pacific region, and there 10.6 cm, respectively.
is potential for interoperability between the two services In summary, the tightly integrated real-time PPP with
in terms of supported satellite constellations, a tightly inte- PPP-B2b and HAS in the Asia-Pacific region can signifi-
grated real-time PPP model with PPP-B2b and HAS for the cantly shorten the convergence time and improve the posi-
Asia-Pacific region is constructed in this study. Four real- tioning accuracy compared with a stand-alone augmentation
time PPP strategies, including B2b C/G, B2b C/G + HAS E, service, which verifies the effectiveness of the proposed
HAS E/G, and HAS E/G + B2b C, are used for compara- model. However, the precise correction products of HAS
tive analysis in terms of availability, convergence time, and service are generated by few monitoring stations in the
positioning accuracy. Asia-Pacific region, and the HAS service does not commit
Regarding the availability in the Asia-Pacific region, to guaranteeing the positioning performance in the Asia-
among the four real-time PPP strategies, the number of Pacific region. Therefore, the two HAS-based strategies,
visible satellites of B2b C/G + HAS E and HAS E/G + B2b namely using the stand-alone HAS service and integrating
C strategies is at a similar level, ranging from about 16 to the PPP-B2b BDS-3 observations into the HAS service, may
24, and the distribution characteristics of PDOP values are not be as effective as expected in this region. It is expected
closely related to the number of visible satellites, with the that the positioning performance of tightly integrated real-
corresponding statistics being 1.06 to 1.41 and 1.07 to 1.25 time PPP with the two augmentation services will be further
for the two strategies, respectively. The B2b C/G strategy improved as their service levels develop in the future.
has the smallest number of visible satellites in the Pacific
region, with the minimum value being 9.3, and the PDOP Acknowledgements The contribution of data from MGEX is appreci-
ated.
value can reach as high as 3.01. By contrast, in the mainland
of China and its coastal regions, the number of visible satel-
Author contributions All authors contributed to the study and design.
lites is increased to 14.9–16.5, and the corresponding PDOP CY performed material preparation, data collection, and analysis. LP
value is relatively smaller, with a minimum value of 1.28. and CY wrote the first draft of the manuscript, and all authors com-
For the HAS E/G strategy, the number of visible satellites mented on previous versions of the manuscript. All authors read and
approved the final manuscript.
varies within a range of 12.9 to 16.2, and the PDOP values
fluctuate between 1.35 and 1.62. In the Asia-Pacific region,
Funding This research was funded by the National Natural Science
all four real-time PPP strategies can achieve a service rate Foundation of China (Grant No. 42388102), and the Department of
of 100%. Natural Resources of Hunan Province (Grant No. HNGTCH-2023-05).
The convergence time of B2b C/G + HAS E strategy is the
Data availability The datasets at selected MGEX stations can be
shortest at 9.4 min, while the B2b C/G and HAS E/G + B2b
obtained from http://igs.gnsswhu.cn.
C strategies have a similar convergence time of 12.3 and
1 3

<!-- PAGE: 11 -->

GPS Solutions (2025) 29:162 Page 11 of 11 162
Declarations Xu Y, Yang Y, Li J (2021) Performance evaluation of BDS-3 PPP-B2b
precise point positioning service. GPS Solut 25(4):142. h t t p s : / / d o
i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 2 1 - 0 1 1 7 5 - 2
Ethics approval and consent to participate Not applicable.
Xu X, Nie Z, Wang Z et al (2023) An improved BDS-3 PPP-B2b posi-
tioning approach by estimating signal in space range errors. GPS
Competing interests The authors declare no competing interests.
Solut 27(3):110. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 2 3 - 0 1 4 5 5 - z
Yang Y, Li J, Xu J et al (2011) Contribution of the compass satel-
lite navigation system to global PNT users. Chin Sci Bull
References 56(26):2813–2819. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 4 3 4 - 0 1 1 - 4 6 2 7 - 4
Zhang R, Tu R, Lu X (2024a) HASPPP: an open-source Galileo HAS
embeddable RTKLIB decoding package. GPS Solut 28(4):169. h
Borio D, Susi M, Gioia C (2023) GHASP: a Galileo HAS parser. GPS
t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 2 4 - 0 1 7 0 6 - 7
Solut 27(4):197. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 2 3 - 0 1 5 2 9 - y
Zhang R, Tu R, Lu X et al (2024b) Initial and comprehensive analysis
CSNO (2021) BeiDou Navigation Satellite System Open Service Per-
of PPP time transfer based on Galileo high accuracy service. GPS
formance Standard. China Satellite Navigation Office, Beijing,
Solut 28(2):94. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 2 4 - 0 1 6 3 3 - 7
Version 3.0, May 2021. h t t p : / / w w w . b e i d o u . g o v . c n / x t / g f x z / 2 0 2 1 0
Zhou P, Xiao G, Du L (2024) Initial performance assessment of Gali-
5 / P 0 2 0 2 1 0 5 2 6 2 1 6 2 3 1 1 3 6 2 3 8 . p d f
leo high accuracy service with software-defined receiver. GPS
Elsobeiey M, Al-Harbi S (2016) Performance of real-time precise point
Solut 28(1):2. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 2 3 - 0 1 5 4 0 - 3
positioning using IGS real-time service. GPS Solut 20(3):565–
571. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 1 5 - 0 4 6 7 - z
Publisher’s note Springer Nature remains neutral with regard to juris-
EUSPA (2023) Galileo High Accuracy Service: Service Definition
dictional claims in published maps and institutional affiliations.
Document (HAS SDD). European Union Agency for the Space
Programme, Prague, Version 1.0, January 2023. h t t p s : / / w w w . g s
c - e u r o p a . e u / s i t e s / d e f a u l t / fi l e s / s i t e s / a l l / fi l e s / G a l i l e o - H A S - S D D _ v Springer Nature or its licensor (e.g. a society or other partner) holds
1 . 0 . p d f exclusive rights to this article under a publishing agreement with the
EUSPA (2022) Galileo High Accuracy Service: Signal-In-Space Inter- author(s) or other rightsholder(s); author self-archiving of the accepted
face Control Document (HAS SIS ICD). European Union Agency manuscript version of this article is solely governed by the terms of
for the Space Programme, Prague, Version 1.0, May 2022. h t t p s : such publishing agreement and applicable law.
/ / w w w . g s c - e u r o p a . e u / s i t e s / d e f a u l t / fi l e s / s i t e s / a l l / fi l e s / G a l i l e o _ H A
S _ S I S _ I C D _ v 1 . 0 . p d f
Fernandez-Hernandez I, Chamorro-Moreno A, Cancela-Diaz S et al Lin Pan is currently an associate professor at
(2022) Galileo high accuracy service: initial definition and per- Central South University. He received a Ph.D.
formance. GPS Solut 26(3):65. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 degree in Geodesy and Engineering Survey-
2 2 - 0 1 2 4 7 - x ing from Wuhan University in 2018. His cur-
Kan H, Hu Z, Chen G et al (2024) Performance comparison of orbit rent research mainly focuses on GNSS precise
and clock augmentation corrections from PPP-B2b, HAS and positioning and its application.
CLAS. Adv Space Res 74(2):668–681. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j
. a s r . 2 0 2 4 . 0 4 . 0 2 9
Naciri N, Yi D, Bisnath S et al (2023) Assessment of Galileo high
accuracy service (HAS) test signals and preliminary positioning
Chen Yang is currently a master’s candidate
performance. GPS Solut 27(2):73. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9
at Central South University. He received his
1 - 0 2 3 - 0 1 4 1 0 - y
B.Sc. degree in Surveying Engineering from
Nie Z, Gao Y, Wang Z et al (2018) An approach to GPS clock predic-
Nanjing Tech University in 2023. His current
tion for real-time PPP during outages of RTS stream. GPS Solut
research focuses on GNSS precise
22(1):14. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 1 7 - 0 6 8 1 - y
positioning.
Ouyang C, Shi J, Peng W et al (2023) Exploring characteristics of
BDS-3 PPP-B2b augmentation messages by a three-step analysis
procedure. GPS Solut 27(3):119. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9
1 - 0 2 3 - 0 1 4 5 7 - x
Prol FS, Kirkko-Jaakkola M, Horst O et al (2024) Enabling the Galileo
high accuracy service with open-source software: integration of
HASlib and RTKLIB. GPS Solut 28(2):71. h t t p s : / / d o i . o r g / 1 0 . 1 0 0
7 / s 1 0 2 9 1 - 0 2 4 - 0 1 6 1 7 - 7
Sun S, Wang M, Liu C et al (2023) Long-term performance analysis of
BDS-3 precise point positioning (PPP-B2b) service. GPS Solut
27(2):69. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 2 3 - 0 1 4 0 9 - 5
Tang C, Hu X, Chen J et al (2022) Orbit determination, clock Estima-
tion and performance evaluation of BDS-3 PPP-B2b service. J
Geodesy 96(9):60. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 0 0 1 9 0 - 0 2 2 - 0 1 6 4 2 - 9
Tao J, Liu J, Hu Z et al (2021) Initial assessment of the BDS-3 PPP-
B2b RTS compared with the CNES RTS. GPS Solut 25(4):131. h
t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 2 1 - 0 1 1 6 8 - 1
Wu P, Lou Y, Zhang W et al (2023) Evaluation of real-time kinematic
positioning performance of the BDS–3 PPP service on B2b sig-
nal. GPS Solut 27(4):192. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 2 9 1 - 0 2 3 - 0
1 5 3 2 - 3
1 3