<!-- PAGE: 1 -->

GPS Solutions (2025) 29:35
https://doi.org/10.1007/s10291-024-01789-2
ORIGINAL ARTICLE
Combining Galileo HAS and Beidou PPP‑B2b with Helmert coordinate
transformation method
Haopeng Wei1 · Guorui Xiao1,2 · Peiyuan Zhou1 · Peigong Li1 · Zhengyang Xiao1 · Baoxiang Zhang3
Received: 4 June 2024 / Accepted: 20 November 2024
© The Author(s) 2024
Abstract
The European Galileo High Accuracy Service (HAS) started to provide freely and openly accessible real-time precise
satellite orbit, clock and code bias products to global users on January 24, 2023. Combined with the already running Bei-
Dou PPP-B2b service, the launch of a variety of satellite-based PPP services provided more choices to users. However,
different satellite-based PPP services provide services for different GNSS systems, which hamper users to make full use of
multi-GNSS systems. Therefore, the combination of different satellite-based products can further improve the availability
of corrections, usage of multi-GNSS observation data and positioning performance. This paper proposes to combine HAS
and PPP-B2b products by the Helmert coordinate transformation method. To validate the algorithm, HAS and PPP-B2b
products of day of year (DOY) 308–317 in 2023 were collected in Zhengzhou, China. First, they are evaluated in terms of
correction availability, orbit and clock quality. Then the HAS and PPP-B2b products are combined by the Helmert coordinate
transformation method. Two combination strategies are proposed. The first strategy is integrating BDS satellites of PPP-B2b
products into HAS products (denoted as C_H), while the second strategy is integrating Galileo satellites of HAS products
into PPP-B2b products (denoted as C_B). Finally, the combined strategies are evaluated with static and kinematic data. Based
on the static data of 18 Multi-GNSS Experiment (MGEX) stations in China and its surrounding areas, the results show that,
when separately using HAS and PPP-B2b products for PPP, the average accuracy in horizontal and vertical directions are
(2.4, 2.7 cm) and (2.4, 2.0 cm), respectively. The average accuracy of C_H strategy is 2.1 and 1.7 cm, which was improved
by 31.3% compared with separately using the products. Similarly, the average accuracy of C_B strategy is 2.1 and 1.9 cm,
corresponding to improvements of 29.6%. When comparing the two combined strategies, it is noted that the C_B strategy
converges faster. Based on the data from vehicle platform, the results show that the horizontal and vertical accuracy of the
C_B strategy is 8.6 and 15.7 cm respectively. The accuracy improvement of C_B is better than that of C_H strategy, and the
average accuracy is 68.4% better than that of separately using the products. The above results show that the two combined
strategies can improve positioning accuracy. In addition, the improvements in accuracy and convergence speed of C_B strat-
egy are more significant. Users are advised to use C_B strategy for the combination of HAS and PPP-B2b products, which
will greatly expand the application of HAS and PPP-B2b services.
Keywords Galileo high accuracy service (HAS) · PPP-B2b · Real-time PPP · Helmert coordinate transformation method
*
Guorui Xiao
xgr@whu.edu.cn
1 Information Engineering University, Zhengzhou 450052,
China
2 Chinese Academy of Surveying and Mapping,
Beijing 100036, China
3 China University of Geosciences, Beijing 100083, China
Vol.:(0123456789)

<!-- PAGE: 2 -->

35 Page 2 of 14 GPS Solutions (2025) 29:35
Introduction receiver platform to obtain decimeter-level PPP accuracy.
Martini et al. (2024) compared the HAS products with
Precise point positioning (PPP) is a technology that can Galileo I/NAV and GPS LNAV broadcast navigation mes-
achieve centimeter-level positioning accuracy with only one sages and showed that the accuracy of orbit and clock had
receiver (Malys and Jensen 1990; Zumberge et al. 1997). improved. Vehicle Kinematic experiments are carried out
Due to the delay of precise orbit and clock product broad- under the tree crown and other obstacles, and the results
casted by the International GNSS Service (IGS), most of the show that the horizontal positioning accuracy is 26.7 cm.
traditional PPP is post-processing, which cannot meet the As can be seen from the above research, the launch of the
needs of new industries such as autopilot, robot navigation, two satellite-based PPP services provided more choices to
precision-agriculture, precision-marine positioning, and so users. However, different satellite-based PPP services pro-
on. Therefore, real-time PPP has become a research hotspot vide services for different GNSS systems, which hamper
in recent years. users to make full use of multi-GNSS systems. Therefore,
On July 31, 2020, the full constellation of the BDS-3 the combination of different satellite-based products can fur-
system was completed and started to provide global services ther improve the availability of corrections, usage of multi-
(CSNO 2021, 2020). The PPP-B2b service broadcasts the GNSS observation data and positioning performance.
orbit and clock correction of GPS/Beidou to China and its For real-time orbit and clock product combinations, Chen
surrounding areas (75°E–135°E, 10°N–55°N) through the (2019) combined the real-time products of different IGS
B2b signals of three Geosynchronous Earth Orbit (GEO) analysis centers, and the results show that the PPP accu-
satellites, enabling users to realize real-time PPP services racy of the combined products is better than that of a single
at the kinematic decimeter-level and static centimeter-level product. Chen (2021) employed both the single-day model
accuracy (Li et al. 2020; Lu et al. 2020). On January 24, and the single-epoch model to solve the seven transforma-
2023, the Galileo HAS was declared operational as initial tion parameters. Results show that the orbit accuracy of the
service, which disseminates real-time precise satellite orbit, single-epoch model is 9.3% better than that of the single-
clock and code bias products of GPS/Galileo via the Galileo day model. Zhou et al. (2022) combined the post-processing
E6B signals and the internet, aiming to support decimeter- products from different IGS analysis centers, and results
level real-time PPP services globally (European Union 2022; show that the average accuracy of multi-GNSS kinematic
European Union 2023). PPP is 1.4, 1.2, and 2.9 cm in East, North, and Up directions,
The services have attracted wide attention. Xu et al. respectively. Inspired by the above research, the combination
(2021) show that the availability of PPP-B2b correction in of Galileo HAS and BDS PPP-B2b products is proposed to
China is better than 80%, the accuracy of real-time orbit of provide enhanced the satellite-based PPP services.
the inclined geostationary orbit satellites (IGSO) is about The first part of this contribution briefly introduces the
two times poorer than that of the medium earth orbit (MEO) combination and evaluation methods of orbit and clock
satellites. Sun et al. (2023) assessed the results of PPP-B2b products. Then, the product quality of HAS and PPP-B2b
service with one year data and showed that the standard is evaluated with respect to availability, orbit and clock
deviation (STD) of Signal-In-Space Ranging Error (SISRE) accuracy. Afterward, two strategies to combine HAS and
for BDS-3 MEO, GPS and BDS-3 IGSO satellites are 5.9, PPP-B2b products are proposed. Finally, the positioning
9.2 and 17.4 cm, respectively. Wu et al. (2023) carried out performance of the combined product is comprehensively
different kinematic experiments and found that the position- analyzed through static and kinematic PPP experiments, and
ing accuracy can reach decimeter-level. As for the Galileo conclusions are summarized.
HAS, Fernandez-Hernandez et al. (2023) introduced the
infrastructure and initial performance of the Galileo HAS.
Methodologies
Hauschild et al. (2022) assessed the quality of the satellite
orbit and clock corrections from the early HAS test signals
in September 2021 and demonstrated its benefit for (near) This section first introduces the evaluation methods of orbit
real-time orbit determination of remote sensing satellites and clock. Then, the combination method of HAS and PPP-
in low earth orbit. Naciri et al. (2023) used experimental B2b based on the Helmert coordinate transformation method
Galileo HAS to evaluate the quality. Results showed that the is proposed.
SISRE were 11.8 and 10.6 cm for GPS and Galileo satel-
Satellite‑based PPP orbit and clock quality
lites, respectively, which can support decimeter-level real-
assessment method
time PPP. After the announcement of Galileo HAS initial
service, Zhou et al. (2024) used the HAS products received
by the developed commercial off-the-shelf Software-defined The satellite-based PPP orbit products, HAS and PPP-B2b,
are compared with Wuhan University (WHU) precise orbit

<!-- PAGE: 3 -->

GPS Solutions (2025) 29:35 Page 3 of 14 35
products for quality assessment, it is worth noting that the unit of
ns,Cs
is the satellite clock from the WHU precise
WHU
centers of HAS and PPP-B2b orbit products refer to the clock products in the unit of ns, Δ∇C S s YS,WUH represents the
antenna phase center (APC), while the WHU precise orbit DD values in the unit of ns. In addition, for HAS and PPP-
products refer to the center of mass (CoM). Therefore, B2b products, only part of the satellites can be received in
the HAS and PPP-B2b reference points need to be trans- each epoch, which leads to the difference of the average of
formed to CoM using the phase center offsets (PCO) before SD values of each epoch, and finally leads to the discontinui-
evaluation. ties of DD series and affects the STD statistics. Because of
ΔXs =(Xs +A×dSYS )−Xs the low availability of PPP-B2b products, the discontinuities
SYS SYS PCO WHU (1) of DD series have a significant influence on the estimation
of PPP-B2b clock. The discontinuities of DD series must be
𝛿e 𝛿e 𝛿e T = ⇀e ⇀e ⇀e ΔXs taken care of for the accurate evaluation of clock products. If
[ R A C] [ R C A] SYS (2)
a discontinuity is detected, it is rectified using the following
formula (Tao et al. 2021):
⇀r ⇀r ×⇀v
⇀e R = ⇀r s ⇀e C = ⇀r s ×⇀v s ⇀e A =⇀e C ×⇀e A (3) Δ∇C S s YS,WHU =Δ∇C S s YS,WHU − M 1 ∑ M ( Δ∇C S s, Y t S,WHU −Δ∇C S s, Y t− S, 1 WHU)
| s| | s s| i=1
| | | | (5)
| | | |
where | X | S s YS are | the sate | llite S positions from the HAS and where t represents the number of epochs. When the absolute
f P r P o P m - B th 2 e b W or H b U it p p r r e o c d i u se c t o s r ,X bi W s t H p U ro a d r u e c t t s h . e d S s Y a S te a l r l e it e th S e P po C s O it i c o o n r s - value of M 1 ∑ M i=1� Δ∇C S s, Y t S,WHU −Δ∇C S s, Y t− S, 1 WHU� is larger
PCO
rections and S represents different satellites. A= [ e X e Y e Z] than ± 0.1 ns, the DD values are corrected.
is the satellite attitude matrix, where e X,e Y , e Z are the unit
Satellite‑based PPP orbit and clock combination
vectors of X, Y, Z axes of the satellite-body frames in Earth-
⇀ ⇀ algorithm
r v
Centered Earth-Fixed (ECEF) coordinate system. and
s s
are the satellite position and velocity vectors in ECEF. The
HAS and PPP-B2b orbit products use different coordinate
PCOs of GPS satellites and Galileo satellites for HAS prod-
reference frames, in which HAS uses the Galileo Terrestrial
ucts and GPS satellites for PPP-B2b are obtained from the
Reference Frame (GTRF) and PPP-B2b uses the BeiDou
IGS antenna files, while the BDS satellites for PPP-B2b use
Coordinate System (BDCS) (CSNO 2020; European Union
the PCO published by the China Satellite Navigation Office
2022) (European Union 2022; CSNO 2020).. The BDS satel-
(Tang et al. 2022).
lites orbit of PPP-B2b products are transformed to the GTRF
Meanwhile, the HAS and PPP-B2b clock products are
using the Helmert coordinate transformation method, lever-
also compared with WHU precise clock products for qual-
aging the common GPS satellites of HAS and PPP-B2b.In
ity assessment. By comparing the HAS and PPP-B2b clock
addition, the seven parameters are estimated for each epoch.
products with the WHU precise clock products, single-
The first step of the implementation is to find out the com-
difference (SD) processing across two satellites is firstly
mon GPS satellites for HAS and PPP-B2b products of the
performed within one product by selecting the reference
satellite
Ci
and
Ci
to eliminate timescale difference,
same epoch.
SYS WHU Second, the error equation is listed using the common
and then differencing of the SD series of the two products
GPS satellites, as shown in Eq. (6).
is performed to obtain the double difference (DD) series.
However, how to choose the reference is inconvenient in M
automatic data processing, especially for regional satellite R_x
⎡ ⎤
clock product evaluation, because the reference satellite will V xg x HAS 0 z HAS −z HAS 1 0 0 ⎢R_y⎥
e c e a h l n n l a d c it n e e i g s t s s e a o a t f f e v r t l e e h l q r i e t a u e g t e w e ( n Y o t M 1 l a y p o ∑ r d o e u M i d t = e u a 1 c t l � o . t s C 2 o a S i 0 b Y r 1 s e S 7 e u − r ) s v : e C a d b W i i t H l o i U t c y � a . f l A c o u r ll m l a t t h s e e a C c v S i o i Y r m S tu − m al o C n r W i e s f H e a U r t- - , ⎡ ⎢ ⎢ ⎢ ⎣ V V y zg g⎤ ⎥ ⎥ ⎥ ⎦ = ⎡ ⎢ ⎢ ⎢ ⎣ y z H H A A S S − y z H H A A S S −x 0 HAS x H 0 AS 0 0 0 1 1 0 ⎤ ⎥ ⎥ ⎥ ⎦ ⋅⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢ T T T R _ _ _ _ x y z z ⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥ (6)
⎢ ⎥
1 M x HAS x B2b ⎢ ⎣ ⎥ ⎦
Δ∇Cs = Cs −Cs − Ci −Ci + y − y
SYS,WHU ( SYS WHU) M ∑( SYS WHU) ⎡ HAS ⎤ ⎡ B2b ⎤
i=1 ⎢z HAS⎥ ⎢z B2b⎥
(4) ⎢ ⎥ ⎢ ⎥
⎢ ⎥ ⎢ ⎥
where M is the number of common satellites,Cs is the sat- ⎣ ⎦ ⎣ ⎦
SYS
ellite clock from the HAS and PPP-B2b clock products in the

<!-- PAGE: 4 -->

35 Page 4 of 14 GPS Solutions (2025) 29:35
V x g x HAS 0 z HAS −z HAS 1 0 0 t c r o a m ns p f e o n r s m a a te ti d o n to , t t h h e e c o l r o b c i k t c p o ro o d rd u i c n t a s t t e h r c o h u a g n h g e t s h e n f e o e l d lo t w o in b g e
V = V y g B= y HAS −z HAS 0 x HAS 0 1 0 X equation:
⎡ ⎢ V z g ⎤ ⎥ ⎡z HAS y HAS −x HAS 0 0 0 1⎤
⎢ ⎥ ⎢ ⎥ Ps (t)−Ps (t) ⋅Ps (t)
⎢ M ⎥ ( primitive work ) primitive
⎢ ⎥ ⎣ ⎦ ΔClks (t)= (8)
⎣ ⎦ R_x primitive Rs ⋅c
primitive
⎡
R_y
⎤
x
HAS
x
B2b
=⎢R_z⎥L= y
HAS
− y
B2b where
Ps
primitive is the satellite coordinate vector of PPP-B2b
⎢ ⎢ T_x⎥ ⎥ ⎡z HAS⎤ ⎡z B2b⎤ orbit products before coordinate transformation, Ps work is the
⎢
T_y
⎥
⎢ ⎥ ⎢ ⎥
satellite coordinate vector of PPP-B2b product after coordi-
⎢ ⎥ ⎢ ⎥
⎢T_z⎥ ⎣ ⎦ ⎣ ⎦ nate transformation, Rs is the distance from the satellite
⎢ ⎥ primitive
where V x g , V y g an ⎢ ⎣d V z g a ⎥ ⎦re residuals, x HAS,y HAS and z HAS are u to u m th , e a c n o d o Δ rd C in lk a s te orig r i e n p , r c e s i e s n t t h s e t h v e e l c o lo c c it k y p o r f o d li u g c h t t s i c n o m a p v e a n c- -
the coordinates in the GTRF reference frames, x B2b,y B2b and primitive
t
z
h
B2
e
b
s
a
c
re
a l
t
e
h e
p
c
a
o
ra
o
m
rd
e
in
te
a
r
t
,
e s
R
i
_
n
x
t
,
h e
R
B
_y
D
a
C
n
S
d
r e
R
f
_
e
z
re
a
n
r
c
e
e f
t
r
h
a
e
m
r
e
o
s
t
,
a
M
tio
i
n
s sati
T
o
h
n
e
v a
s
l
e
u
l
e
f-
s
c
i
o
n
n
t
s
h
i
e
s t
u
e
n
n
i
t
t o
c
f
l o
n
c
s
k
.
products
Clks
work
(i)
can be
parameters,
T_x
,
T_y
and
T_z
are the translation parameters
obtained through Eq. (9) based on which the clock products
of PPP-B2b can be consistent with the transformed orbit
(Deakin 1998; Chen and Wang 2009).
According to the principle of least square
VTPV =min
,
products (Kouba and Springer 2001; Springer et al. 1998):
the unknown parameter X can be solved: Clks (i)=Clks (i)−ΔClks (i)
work primitive primitive (9)
X =− BTPB −1 BTPL (7)
( )
The common GPS satellite coordinates from HAS are HAS, PPP‑B2b and combined products
input into x HAS,y HAS and z HAS , while the common GPS satel- quality evaluation
lite coordinates from PPP-B2b are input into x B2b,y B2b and
z B2b . Then the seven transformation parameters are com- This section collects HAS and PPP-B2b products for DOY
puted using the least squares method.
308–317, 2023. The two products are evaluated from the
Finally, with the obtained seven parameters, the coordi-
availability, orbit, and clock products accuracy. Two com-
nates of the BDS satellites in PPP-B2b can be transformed
bined strategies are proposed, and the combined products
to HAS reference frame with Eq. (6). Similarly, the Galileo
are evaluated.
satellites orbits of HAS products can also be transformed to
BDCS reference frame. Availability assessment of HAS and PPP‑B2b
Chen (2019) analyzed the consistency of precise satellite products
orbit and clock products provided by IGS through the cor-
relation of orbit and clock DD series. The orbit and clock
Figure 1 describes the average daily availability of DOY
DD series of GNSS satellites in different analysis center
308–317 for HAS products. It is found that the daily
products showed a strong correlation. After the coordinate
Fig. 1 Availability of the recov-
ered HAS products from DOY
308–317, 2023
20G 30G 40G 50G 60G 70G 80G 90G 01G 11G 21G 31G 41G 51G 61G 71G 81G 91G 02G 12G 32G 42G 52G 62G 72G 82G 92G 03G 13G 23G 20E 30E 40E 50E 70E 80E 90E 01E 11E 21E 31E 51E 91E 12E 42E 52E 62E 72E 03E 13E 33E 43E 63E
100
80
60
40
20
0
Satellite PRN
ytilibaliavA

<!-- PAGE: 5 -->

GPS Solutions (2025) 29:35 Page 5 of 14 35
Fig. 2 Availability of the recov-
ered PPP-B2b products from
DOY 308–317, 2023
availability of Galileo satellites (except E05 satellite) is It can be seen that the accuracy of HAS orbit products is
better than 95%. The average daily availability of GPS sat- better than that of PPP-B2b orbit products on the whole.
ellites is better than 80%. The reason for the low average The satellites daily root-mean-square errors (RMS) for
daily availability of some satellites is that the corrections of each satellite in the radial direction for DOY 308–317, 2023,
those satellites are not available in individual periods. For are shown in Fig. 4. The average daily RMSs of radial direc-
example, the corrections of E05 satellite are not available tion errors are relatively stable. The HAS and PPP-B2b sat-
during DOY 312–317. Figure 2 describes the average daily ellite orbit accuracy statistics during the whole test period
availability of DOY 308–317 for PPP-B2b products. It can are listed in Table 1. It shows that the average RMSs for
be seen that the average daily availability of BDS-MEO sat- HAS Galileo satellites orbit products during the whole test
ellites is over 29%, and that of BDS-IGSO satellites is better period are 3.1, 9.5 and 6.2 cm, for the radial, along-track
than 70%. The average daily availability of GPS satellites and cross-track directions, respectively, while that for HAS
(except G15/G18/G23) is better than 25%, with an average Galileo satellites orbit products are 3.4, 9.2 and 5.7 cm,
of 30.1%. As the PPP-B2b service broadcasts the orbit and respectively. The accuracy of the radial direction is the best
clock correction of GPS/Beidou to China and its surround- among the three directions, and the accuracy of the along-
ing areas, while the HAS service broadcasts the orbit and track direction is the poorest. Similarly, the average RMSs
clock correction of GPS/Galileo to global areas, the average for B2b BDS MEO satellites in three directions are 5.9, 13.5
daily availability of PPP-B2b products is lower than that of and 11.6 cm, respectively, and that for B2b BDS IGSO satel-
HAS products. But an average of 10 BDS-3 satellites and 8 lites are 15.2, 21.4 and 21.8 cm, respectively, and that for
GPS satellites in each epoch can be ensured in the range of B2b GPS satellites are 5.9, 24.7 and 17.0 cm, respectively.
PPP-B2b service area, which can meet the needs of high- Only BDS IGSO satellites have radial direction errors of
precision positioning. It can be seen from Figs. 1 and 2 that more than 10 cm. The radial direction errors of the other
the availability of HAS correction is significantly better than satellites are less than 7 cm. Since the radial direction of
that of PPP-B2b. The main reason is that the service area of the satellite orbit directly affect the receiver-satellite dis-
PPP-B2b is limited to China and its surrounding areas, so tance measuring and has the largest influence on position-
it only broadcasts the satellite correction over China and its ing, its error directly affects the PPP accuracy. With radial
surrounding areas. direction errors of less than 7 cm, it can be concluded that
the collected HAS and PPP-B2b orbit products can support
Accuracy assessment of HAS and PPP‑B2b products
decimeter-level PPP applications.
Meanwhile, the quality of the HAS and PPP-B2b clock
The quality of the HAS and PPP-B2b orbit products are products are also assessed using WHU precise clock prod-
assessed using WHU precise orbit products as reference. ucts as the reference. As examples, the HAS and PPP-B2b
The obtained HAS and PPP-B2b satellite orbit errors for DD series for DOY 312, 2023 are shown in Fig. 5. Clear
DOY 312, 2023, are used as examples and shown in Fig. 3. It color stratification between satellites reveals systematic
is seen that the radial, along-track and cross-track directions biases in HAS and PPP-B2b clock products. The system-
±20 ±50
error of HAS orbit products are within ranges of , atic biases will be absorbed by the receiver clock and phase
±30
and cm, respectively. Similarly, the PPP-B2b orbit prod- ambiguities, therefore, will not affect PPP performance. The
±30 ±50 ±50
ucts are within ranges of , and cm, respectively. STD of the HAS and PPP-B2b clock products with respect
to the WHU precise clock products for the whole test period
20G 30G 40G 50G 60G 70G 80G 90G 01G 21G 31G 51G 61G 81G 91G 02G 22G 32G 42G 52G 62G 72G 82G 92G 03G 13G 23G 91C 02C 12C 22C 32C 42C 52C 62C 72C 82C 92C 03C 23C 33C 43C 53C 63C 73C 83C 93C 04C 14C 24C 34C 44C 54C 64C
80
70
60
50
40
30
20
10
0
Satellite PRN
ytilibaliavA

<!-- PAGE: 6 -->

35 Page 6 of 14 GPS Solutions (2025) 29:35
0.5
0.4
0.3
0.2
0.1
0
-0.1
-0.2
-0.3
-0.4
-0.5
0 3 6 9 12 15 18 21 24
Time (H)
is computed as the indicator of clock accuracy and plot- period, as given in Table 2, which shows that the average
ted in Fig. 6. It can be seen that the STD of HAS Galileo accuracy of HAS GPS and Galileo satellites clock are 0.15
satellites is smaller than 0.20 ns, and the STD of HAS GPS and 0.19 ns, respectively. The average accuracy of B2b BDS
satellites is only partly larger than 0.25 ns (G11/G18/G23). MEO, B2b BDS IGSO and B2b GPS satellites clock are
Only the STD of C25 satellite in B2b BDS MEO satellites is 0.12, 0.22 and 0.17 ns, respectively. The results indicate that
larger than 0.2 ns, while the STD of C40 in IGSO satellites the collected HAS and PPP-B2b clock products can support
is relatively large. Only three B2b GPS satellites have STD decimeter-level PPP applications.
larger than 0.25 ns. The overall accuracy difference between
HAS and PPP-B2b clock products is not significant. It is
further confirmed by the average STD during the whole test
)m(
srorrE
tibrO
laidaR
0.5
0.4
0.3
0.2
0.1
0
-0.1
-0.2
-0.3
-0.4
-0.5
0 3 6 9 12 15 18 21 24
Time (H)
)m(
srorrE
tibrO
laidaR
0.5
0.4
0.3
0.2
0.1
0
-0.1
-0.2
-0.3
-0.4
-0.5
0 3 6 9 12 15 18 21 24
Time (H)
)m(
srorrE
tibrO
kcarT-gnolA
0.5
0.4
0.3
0.2
0.1
0
-0.1
-0.2
-0.3
-0.4
-0.5
0 3 6 9 12 15 18 21 24
Time (H)
)m(
srorrE
tibrO
kcarT-gnolA
0.5
0.4
0.3
0.2
0.1
0
-0.1
-0.2
-0.3
-0.4
-0.5
0 3 6 9 12 15 18 21 24
Time (H)
)m(
srorrE
tibrO
kcarT-ssorC
0.5
0.4
0.3
0.2
0.1
0
-0.1
-0.2
-0.3
-0.4
-0.5
0 3 6 9 12 15 18 21 24
Time (H)
)m(
srorrE
tibrO
kcarT-ssorC
Fig. 3 HAS (left) and PPP-B2b (right) orbit errors at DOY 312, 2023

<!-- PAGE: 7 -->

GPS Solutions (2025) 29:35 Page 7 of 14 35
0.18 the whole test period and listed the results in Table 3. It is
concluded that the orbit and clock accuracy of the combined
0.16
product is on the same level as that of a single product. The
0.14
clock accuracy of C_H-BDS-IGSO and C_B-Galileo satel-
0.12 lites is slightly improved, which is caused by the clock self-
0.1 consistent process. The results indicate that the combined
products can support decimeter-level PPP applications.
0.08
0.06
0.04 Combined products PPP performance
assessment
0.02
8 9 0 1 2 3 4 5 6 7
0 0 1 1 1 1 1 1 1 1
3 3 3 3 3 3 3 3 3 3
DAY In this section, 18 MGEX stations and real-time kinematic
data of vehicle platform within the coverage of PPP-B2b
were utilized to evaluate the performance of HAS, PPP-B2b,
as well as their combined products. The kinematic experi-
mental data were collected using a Sinan T30 (SN-T30)
receiver. Firstly, four positioning strategies are shown in
Table 4. Then, the data and processing strategies are briefly
introduced. Finally, the positioning performance of the four
PPP strategies is evaluated for both static and kinematic
data.
Static PPP processing
In the static processing, 18 MEGX stations distributed
across China and its surrounding areas are selected, as
depicted in Fig. 8. The experiment session is DOY 308–317,
2023, and all stations support GPS, Galileo and BDS-3. The
HAS and PPP‑B2b combination and quality four positioning strategies were individually processed, and
assessment a comparative analysis was conducted. The PPP strategy is
shown in Table 5 (Xiao et al. 2018).
The following two combined strategies are proposed to com- In order to compare the results, we perform a re-conver-
bine the products. gence every three hours during the data processing. Figure 9
Combined HAS(C_H) Strategy: The seven Helmert shows the convergence performance of the four positioning
parameters are first obtained using the common GPS satel- strategies based on 18 stations under 68% confidence levels
lites of the two products, and then the PPP-B2b BDS satel- on DOY 308–317, 2023 (a total of 1296 time periods). It can
lites are integrated into the HAS products after coordinate be seen that the convergence speeds from fast to slow are
transformation and clock self-consistent process. C_B, S_B, C_H and S_H. In order to evaluate the position-
Combined B2b(C_B) Strategy: The seven Helmert ing accuracy of the four strategies, the average RMSs of the
parameters are obtained using the common GPS satellites positioning accuracy in the last three hours of the single-
of the two products, and then the HAS Galileo satellites day solution is calculated, as shown in Table 6. The average
are integrated into the PPP-B2b products after coordinate accuracy of S_H and S_B strategies are 3.4, 2.7 cm and 2.4,
transformation and clock self-consistent process. 2.0 cm for horizontal and vertical directions, respectively.
As an example, the Helmert seven parameters for DOY The average accuracy of C_H strategy is 2.1 and 1.7 cm, cor-
312, 2023, are computed according to (9) and shown in responding to improvements of 38.2% and 37.0% compared
Fig. 7. It can be seen that the magnitudes of scale param- to the S_H strategy, and corresponding to improvements of
eter, rotation parameter, and translation parameter are 12.5% and 37.4% compared to the S_B strategy. Similarly,
− 5 ~ 15 ppb, − 20 ~ 20 ns, and − 50 ~ 30 cm, respectively. the average accuracy of C_B strategy is 2.1 and 1.9 cm, and
The average of the three translation parameters during the improved by 27.5% compared to the two single strategies. It
whole test period were 8, 8, and 9 cm, respectively. In order is concluded that the C_B strategy has the best positioning
to better demonstrate the accuracy of the orbit and clock performance.
of the combined products, we calculated the accuracy over
)m(srorrEtibrOlaidaR
HAS-E
HAS-G
B2b-MEO
B2b-IGSO
B2b-G
Fig. 4 Daily RMS of radial directions of HAS and PPP-B2b orbit
products during DOY 308–317, 2023
Table 1 Average RMS of HAS and PPP-B2b orbit products during
DOY 308–317, 2023 (unit cm)
Satellite category Radial Along-track Cross-track
HAS-Galileo 3.1 9.5 6.2
HAS-GPS 3.4 9.2 5.7
B2b-BDS-MEO 5.9 13.5 11.6
B2b-BDS-IGSO 15.2 21.4 21.8
B2b-GPS 5.9 24.7 17.0

<!-- PAGE: 8 -->

35 Page 8 of 14 GPS Solutions (2025) 29:35
3
2
1
0
-1
-2
-3
0 3 6 9 12 15 18 21 24
Time (H)
Kinematic PPP processing Inertial Explorer (IE) with centimeter-level accuracy. We
have utilized attitude and positional relationships to convert
An experiment was also carried out in Zhengzhou, China, the coordinates obtained from the IE solution to the phase
on November 8, 2023 (DOY 312), to assess the perfor- center of the Sinan T30 receiver.
mance of kinematic PPP. A SN-30 receiver was mounted Figure 10 shows that the observational environments were
on a vehicle to receive GNSS signals, along with a high- very good as there were almost no tall trees or buildings on
precision GNSS/INS navigation system Novatel 100c with either side of the road. Figure 11 shows that the average
fiber optic gyroscope to calculate the reference trajectory. number of satellites involved in the four positioning strate-
Furthermore, industrial cameras were used to record the gies is larger than 10, and the number of satellites of the
observational environment. All the sensors were mounted on two combined strategies is much larger than that of the two
a high-strength steel framework and carefully calibrated in single strategies. The combined strategies will use more
advance to achieve millimeter-level spatial synchronization observations, which will decrease the convergence time and
and microsecond-level time synchronization, as shown in increase the positioning accuracy. The average of Position
Fig. 10 and the position of our sensors is consistent with that Dilution of Precision (PDOP) of the four positioning strate-
of Xiao et al. (2024). The parameters of sensors are shown gies are smaller than 1.60. The PDOP of S_H, S_B, C_H and
in Table 7. The vehicle travels for 5401 s from 279,600 to C_B are 1.50, 1.41, 1.16 and 1.15, respectively.
285,000 in GPST, i.e., from 05:40:00 to 07:10:00 in UTC The horizontal and vertical accuracy for the four position-
time. The sample rate is 1 Hz. Figure 10 also shows the tra- ing strategies is illustrated in Fig. 12. It can be seen that both
jectory of the vehicle calculated by the GNSS/IMU tightly the convergence speed and the accuracy of the two combined
combined system using the commercial software Novatel strategies are generally better than those of the two single
strategies. It is worth noting that the vertical direction error
)sn(
seires
DD
HAS GPS clock
4
2
0
-2
-4
-6
0 3 6 9 12 15 18 21 24
Time (H)
)sn(
seires
DD
PPP-B2b BDS clock
3
2
1
0
-1
-2
-3
0 3 6 9 12 15 18 21 24
Time (H)
)sn(
seires
DD
HAS GPS clock
6
4
2
0
-2
-4
-6
-8
0 3 6 9 12 15 18 21 24
Time (H)
)sn(
seires
DD
PPP-B2b GPS clock
Fig. 5 HAS (left) and PPP-B2b (right) DD series at DOY 312, 2023. The satellite represented by each color is found in Fig. 3

<!-- PAGE: 9 -->

GPS Solutions (2025) 29:35 Page 9 of 14 35
Fig. 6 Average STD of HAS
and PPP-B2b satellite clock
products for each satellite at
DOY 308–317, 2023
20G 30G 40G 50G 60G 70G 80G 90G 01G 11G 21G 31G 41G 51G 61G 71G 81G 91G 02G 12G 32G 42G 52G 62G 72G 82G 92G 03G 13G 23G 20E 30E 40E 50E 70E 80E 90E 01E 11E 21E 31E 51E 91E 12E 42E 52E 62E 72E 03E 13E 33E 43E 63E
0.3
0.25
0.2
0.15
0.1
0.05
0
Satellite PRN
)sn(DTS
20G 30G 40G 50G 60G 70G 80G 90G 01G 21G 31G 51G 61G 81G 91G 02G 22G 32G 42G 52G 62G 72G 82G 92G 03G 13G 23G 91C 02C 12C 22C 32C 42C 52C 62C 72C 82C 92C 03C 23C 33C 43C 53C 63C 73C 83C 93C 04C 14C 24C 34C 44C 54C 64C
0.4
0.3
0.2
0.1
0
SatellitePRN
)sn(DTS
Table 2 Average STD of HAS Satellite category STD
and PPP-B2b clock products
during DOY 308–317, 2023 HAS-Galileo 0.15
(unit ns)
HAS-GPS 0.19
B2b-BDS-MEO 0.12
B2b-BDS-IGSO 0.22
B2b-GPS 0.17
15
10
5
0
-5
)bpp(elacS
20
0
-20
)sn(noitatoR RX RY RZ
0.3
0.1
-0.1
-0.3
-0.5
0 500 1000 1500 2000 2500
EPOCH
)m(noitalsnarT
Table 3 Accuracy of orbit and clock of combined products during
DOY 308–317, 2023
Satellite category Radial [cm] Along- Cross- STD [ns]
track [cm] track
[cm]
C_H-BDS-MEO 5.8 13.5 11.5 0.11
C_H-BDS-IGSO 15.1 21.4 21.8 0.19
C_B-Galileo 3.1 9.5 6.2 0.12
Table 4 Four positioning strategies
Positioning products GNSS
strategies
S_H Single HAS GPS + Galileo
S_B Single B2b GPS + BDS
C_H Combined HAS strategy GPS + Galileo + BDS
C_B Combined B2b strategy GPS + Galileo + BDS
DX DY DZ
Fig. 7 The Helmert seven parameters at DOY 312, 2023

<!-- PAGE: 10 -->

35 Page 10 of 14 GPS Solutions (2025) 29:35
0.5
0.4
0.3
0.2
0.1
0.05
0
30 60 90 120 150 180
Time(min)
Fig. 8 Station geographical distribution
Table 5 PPP solution strategy
addition, Fig. 13 depicts the trajectory of the four position-
Item Strategy
ing strategies and IE Solution. The four positioning strate-
Orbit/clock CNAV1 + PPP-B2b (BDS) gies are generally consistent with the IE trajectory. Among
LNAV + PPP-B2b (GPS) these, the C_B strategy aligns most closely with the IE solu-
I/NAV + HAS (Galileo) tion, which is consistent with the accuracy statistics results.
LNAV + HAS (GPS) Figure 11 shows that the number of satellites involved in the
Observation GPS: L1/L2 IF combination solving of the S_H strategy is less, and the PDOP series of
Galileo: E1/E5b IF combination the S_H strategy fluctuates more often with a large ampli-
BDS: B1I/B3I IF combination tude, which may be the reason for the poor positioning
Elevation cutoff angle 10° accuracy of the S_H strategy. Similarly, the C_H strategy
Observation weight Elevation angle weighting presents poorer positioning accuracy among the two com-
Phase windup Model corrected bined strategies. For this phenomenon, we will discuss it in
Tide Model corrected the next section.
Relativistic effect Model corrected
Tropospheric delay Saastamoinen model + random-walk process
Receiver clock Estimated as white noise for each epoch Discussion
Ambiguity Estimated as a constant within continuous
arcs
Although the C_H and C_B strategies are just linear trans-
Estimation Kalman filter
formations, the GPS satellites, i.e., HAS GPS and PPP-B2b
GPS, are different in the two strategies. Different GPS sat-
ellites in the combined products lead to positioning differ-
becomes larger after 6:30 a.m. We believe that this phe- ences, as the GPS positioning performance is different. We
nomenon may be related to the continuous fluctuation of the have added another two static experiments to verify this.
PDOP series after 6:30 a.m. The two static experiments use 18 MEGX stations shown
To further evaluate the positioning accuracy of the four in Fig. 8 and use only GPS satellites of HAS and PPP-B2b
positioning strategies, we statistically averaged the errors products for positioning, which are defined as HAS_G and
after 15 min in the four positioning strategies, as depicted in B2b_G, respectively. Consistent with the static experiments,
Table 8. Among them, the C_H strategy improves the hori- we perform a re-convergence every three hours. Figure 14
zontal and vertical directions by 63.5%, 70.4%, 49.7% and shows the convergence performance of the HAS_G and
11.83% compared to the strategies S_H strategy and S_B B2b_G based on 18 stations under 50% confidence levels
strategy, respectively, while that of C_B strategy improves for DOY 308–317, 2023. It can be seen that although the
by 80.4%, 79.9%, 73.0%, and 40.1%, respectively. The aver- convergence speed of HAS_G is faster than that of B2b_G
age improvement of C_B strategy is 68.7% with horizontal within the first 30 min, the positioning accuracy of B2b_G
and vertical accuracy at 8.6 and 15.7 cm respectively. In is better than HAS_G. The positioning accuracy of the last
)m(rorrE
D3
S_H
S_B
C_H
C_B
3D--68%
Fig. 9 Convergence performance of the four positioning strategies
based on 18 stations under 68% confidence levels for DOY 308–317,
2023

<!-- PAGE: 11 -->

GPS Solutions (2025) 29:35 Page 11 of 14 35
Table 6 Four strategies static PPP positioning accuracy
Strategy Horizontal Vertical [cm] Compare S_H improvement Compare S_B improvement Average
[cm] improvement
Horizontal [%] Vertical [%] Horizontal [%] Vertical [%]
[%]
S_H 3.4 2.7 \ \ \ \ \
S_B 2.4 2.0 \ \ \ \ \
C_H 2.1 1.7 38.2 37.0 12.5 37.4 31.3
C_B 2.1 1.9 38.2 29.6 12.5 29.6 27.5
Fig. 10 Vehicle platform and
the trajectory for the real experi-
ment
Table 7 Information about the
Equipment Model Specification Information
mounted sensors
GNSS receiver Sinan T30 GPS: L1, L2, L5
BDS-3: B1, B2, B3, B1C, B2a, B2b
Galileo: E1, E5a, E5b
Sampling interval: 1 Hz
Static horizontal accuracy:± 2.5+0.5×10−6×D mm
( )
Static vertical accuracy:± 5+0.5×10−6×D mm
( )
GNSS/INS system Novatel 100c Gyroscope bias:
0.05◦∕hr
Accelerometer bias:
100𝜇g
Camera MER-131 Resolution:
1280H×1027V
epoch of B2b_G is 7.4 cm, while that of HAS_G is only for real-time PPP. Combined with PPP-B2b services, it will
15.7 cm. The static experimental results show that the posi- provide users with more satellites to overcome shortcomings
tioning performance of PPP-B2b is better than that of HAS such as long convergence time and sensitivity to environ-
in China and its surrounding areas. At the same time, it is mental interference. In this paper, two combined strategies
also verified that the reason for the positioning differences are proposed, and their positioning performance is analyzed.
between the two combined products is the different GPS The following conclusions are drawn:
satellite positioning performance of HAS and PPP-B2b
products. 1. The HAS and PPP-B2b products of DOY 307–318, 2023
were collected, and the WHU precise products were
used as a reference for quality assessment. In the whole
Conclusion
test period, the average daily RMSs of radial directions
of HAS and PPP-B2b products are relatively stable. On
On January 24, 2023, the Galileo High Accuracy Service the other hand, the accuracy of clock products can also
(HAS) was declared available for initial service, which can meet the needs of high-precision positioning. The orbit
provide a new option for users to use satellite-based products and clock accuracy of the combined products is not

<!-- PAGE: 12 -->

35 Page 12 of 14 GPS Solutions (2025) 29:35
3
2.5
2
1.5
1
2. Based on the observations of 18 MGEX stations in
significantly different from that of a single product, the China and its surrounding areas in DOY307-318, 2023,
clock accuracy of some satellites is slightly improved, the static PPP performance of four positioning strategies
which is caused by the clock self-consistent process. is evaluated. The average accuracy of C_H strategy is
The results show that the combined product can sup- 2.1 and 1.7 cm for horizontal and vertical directions,
port decimeter-level PPP applications. respectively, which was improved by 31.3% on average
PODP
S_H 1.50 S_B 1.41 C_H 1.16 C_B 1.15
25
20
15
10
5:40 6:10 6:40 7:10
Time(H:min)
setilletas
fo
rebmuN
S_H 11.54 S_B 15.23 C_H 19.16 C_B 19.96
Fig. 11 PDOP (top) and number of satellites (bottom) in kinematic
experiments
5
4
3
2
1
5:40 6 : 1 0 6:40 7:10
Time(H:min)
)m(rorrE
113.474°E 113.478°E 113.482°E
Longitude
S_H
S_B
C_H
C_B
5:40 6:10 6:40 7:10
Time(H:min)
Fig. 12 Real-time kinematic PPP horizontal(left) and vertical(right)
positioning errors of four positioning strategies in vehicle experi-
ments
Table 8 Real-time kinematic experiments with four strategies for positioning accuracy
Strategy Horizontal [cm] Vertical [cm] Compare S_H improvement Compare S_B improvement Average
improvement
Horizontal [%] Vertical [%] Horizontal [%] Vertical [%]
[%]
S_H 43.8 78.1 \ \ \ \ \
S_B 31.8 26.2 \ \ \ \ \
C_H 16.0 23.1 63.5 70.4 49.7 11.83 48.9
C_B 8.6 15.7 80.4 79.9 73.0 40.1 68.4
edutitaL
N°838.43
N°438.43
N°038.43
S_H
S_B
C_H
C_B
IE
34.82852
34.8285
34.82848 113.48115 113.481155 113.48116 113.481165
Fig. 13 IE solution trajectories and real-time kinematic PPP trajecto-
ries for four positioning strategies in vehicle experiments
1
0.8
0.6
0.4
0.2
0
30 60 90 120 150 180
Time(min)
)m(rorrE
D3
HAS_G
B2b_G
3D--50%
Fig. 14 Convergence performance of the HAS_G and B2b_G based
on 18 stations under 50% confidence levels for DOY 308–317, 2023

<!-- PAGE: 13 -->

GPS Solutions (2025) 29:35 Page 13 of 14 35
compared with the two single strategies. Similarly, the material is not included in the article’s Creative Commons licence and
average accuracy of C_B strategy is 2.1 and 1.9 cm, and your intended use is not permitted by statutory regulation or exceeds
the permitted use, you will need to obtain permission directly from
the average improvement is 29.6%. The convergence
the copyright holder. To view a copy of this licence, visit http://crea-
rates from fast to slow are C_B, S_B, C_H, and S_H. tivecommons.org/licenses/by-nc-nd/4.0/.
Considering the positioning accuracy and convergence
speed, C_B is the best strategy for static PPP perfor-
mance. References
3. For the vehicle kinematic experiment, the average PDOP
of the four positioning strategies in the whole test period
Chen J, Wang J (2009) Orbit fitting based on Helmert transforma-
is less than 1.60, and the number of satellites involved in tion. Geo-Spatial Inform Sci 12:95–99. https://d oi.o rg/1 0.1 007/
the solution is more than 10. Among them, the accuracy s11806-0 09-0 236-7
of the two combined strategies is improved compared Chen G (2019) Research on the methods for multi-GNSS products
combination and its application in iGMAS activities. Wuhan
with the two single strategies. The average improvement
University.
of the accuracy of C_B strategy is 68.4%, and the hori- Chen L (2021) Research on the theory and method of BDS/GNSS
zontal and vertical directions accuracy are 8.6 cm and real-time precise satellite orbit and clock products combination.
15.7 cm respectively. Considering the static PPP perfor- Wuhan University.
CSNO (2020) BeiDou Navigation Satellite System Signal in space
mance, the positioning accuracy of C_B is significantly
interface control document Precise Point Positioning Service
improved compared with the two single products, and Signal PPP-B2b (Version 1.0). http://w ww.b eidou.g ov.c n/x t/g fxz/
it is also the better choice between the two combined 202008/P 02020 08033 62062 48294 0.p df
strategies. In addition, the positioning performance of CSNO (2021) BeiDou Navigation Satellite System Open Service Per-
formance Standard (Version 3.0). http://w ww.b eidou.g ov.c n/x t/
PPP-B2b is better than that of HAS in China and its sur-
gfxz/2 02105/P 02021 05262 16231 13623 8.p df
rounding areas, which leads to the difference in position- Deakin RE (1998) 3-D coordinate transformations. Surv Land Inform
ing performance between the two combined products. Syst 58:223–234
European Union (2022) Galileo High Accuracy Service Signal-InSpace
Interface Control Document (HAS SIS ICD) Issue 1.0. https://
Acknowledgements We gratefully acknowledge the European Union www.g sc-e uropa.e u/s ites/d efaul t/fi les/s ites/a ll/fi les/G alile o_H AS_
SIS_I CD_v 1.0.p df
for providing the Galileo HAS and the China Satellite Navigation
European Union (2023) Galileo High Accuracy Service Service Defi-
Office for providing PPP-B2b. We also thank MGEX and WHU for
nition Document (HAS SDD) Issue 1.0. https://w ww.g sc-e uropa.
providing the GNSS data and products.
eu/s ites/d efaul t/fi les/s ites/a ll/fi les/G alile o-H AS-S DD_v 1.0.p df
Author contributions PW, PZ and GX designed the research; GX pro- Fernandez-Hernandez I, Damy S, Simón C-D, Adrián C-M, J. David
C-C, Martini I, Winkel DJÓ, Blas FJd, Simón J, Blonski D, Izqui-
vided the software; PW and GX wrote the main manuscript text; PL,
erdo DI (2023) Galileo authentication and high accuracy: getting
ZX and BZ analyzed the result; All authors reviewed the paper and
to the truth. Inside GNSS.
agreed to the submitted version.
Hauschild A, Montenbruck O, Steigenberger P, Martini I, Fernandez-
Funding This work was sponsored by National Natural Science Foun- Hernandez I (2022) Orbit determination of Sentinel-6A using the
Galileo high accuracy service test signal. GPS Solut 26:1–13.
dation of China (grants nos. 42274045, 41931076 and 41904039),
https://d oi.o rg/1 0.1 007/s 10291-0 22-0 1312-5
Natural Science Foundation of Henan (grants no. 232300421105), and
Kouba J, Springer T (2001) New IGS station and satellite clock com-
China Postdoctoral Science Foundation (Grant no. 2024T170851 and
bination. GPS Solut 4:31–36. https://d oi.o rg/1 0.1 007/p l0001 2863
2023M733285).
Li R, Zheng S, Wang E, Chen J, Feng S, Wang D, Dai L (2020)
Data availability The Galileo HAS data, PPP-B2b data and kine- Advances in BeiDou navigation satellite system (bds) and satel-
lite navigation augmentation technologies. Satell Navig 1:1–23.
matic data are available from the corresponding author on reasonable
https://d oi.o rg/1 0.1 186/s 43020-0 20-0 0010-2
requests, while the GNSS data and products can be downloaded from
Lu J, Guo X, Su C (2020) Global capabilities of BeiDou navigation
IGS.
satellite system. Satell Navig. https://d oi.o rg/1 0.1 186/1 0.1 186/
Declarations S43020-0 20-0 0025-9
Malys S, Jensen PA (1990) Geodetic point positioning with GPS car-
rier beat phase data from the CASA UNO experiment. Geophys
Conflict of interest The authors declare no competing interests.
Res Lett 17:651–654. https://d oi.o rg/1 0.1 029/g l017i 005p0 0651
Martini I, Susi M, Cucchi I, Hernandez LF (2024) Galileo high accu-
Open Access This article is licensed under a Creative Commons
racy service performance and anomaly mitigation capabilities.
Attribution-NonCommercial-NoDerivatives 4.0 International License,
GPS Solut 28:25. https://d oi.o rg/1 0.1 007/s 10291-0 23-0 1555-w
which permits any non-commercial use, sharing, distribution and repro-
Naciri N, Yi D, Bisnath S, de Blas FJ, Capua R (2023) Assessment of
duction in any medium or format, as long as you give appropriate credit
Galileo high accuracy service (HAS) test signals and preliminary
to the original author(s) and the source, provide a link to the Creative
positioning performance. GPS Solut 27:73. https://d oi.o rg/1 0.
Commons licence, and indicate if you modified the licensed material.
1007/s 10291-0 23-0 1410-y
You do not have permission under this licence to share adapted material
Springer T, Zumberge J, Kouba J (1998) The IGS analysis products and
derived from this article or parts of it. The images or other third party
the consistency of the combined solutions.
material in this article are included in the article’s Creative Commons
licence, unless indicated otherwise in a credit line to the material. If

<!-- PAGE: 14 -->

35 Page 14 of 14 GPS Solutions (2025) 29:35
Sun S, Wang M, Liu C, Meng X, Ji R (2023) Long-term performance Publisher's Note Springer Nature remains neutral with regard to
analysis of BDS-3 precise point positioning (PPP-B2b) service. jurisdictional claims in published maps and institutional affiliations.
GPS Solut 27:69. https://d oi.o rg/1 0.1 007/s 10291-0 23-0 1409-5
Tang C, Hu X, Chen J, Liu L, Zhou S, Guo R, Li X, He F, Liu J, Yang
J (2022) Orbit determination, clock estimation and performance
evaluation of BDS-3 PPP-B2b service. J Geodesy 96:60. https://
doi.o rg/1 0.1 007/s 00190-0 22-0 1642-9 Haopeng Wei is currently a Master’s degree candidate at Informa-
Tao J, Liu J, Hu Z, Zhao Q, Chen G, Ju B (2021) Initial Assessment tion Engineering University, China. He has completed his B.Eng. the
of the BDS-3 PPP-B2b RTS compared with the CNES RTS. GPS Department of Surveying and Mapping Engineering at Henan Poly-
Solut 25:1–16. https://d oi.o rg/1 0.1 007/s 10291-0 21-0 1168-1 technic University in 2022. His area of research currently focuses on
Wu P, Lou Y, Zhang W, Dousa J, He H, Chai J, Ouyang Y, Zhang GNSS real-time precise positioning.
Z, Zou X (2023) Evaluation of real-time kinematic positioning
performance of the BDS-3 PPP service on B2b signal. GPS Solut Guorui Xiao is currently an associate professor at Information Engi-
27:192. https://d oi.o rg/1 0.1 007/s 10291-0 23-0 1532-3 neering University, China. He received his B.Sc. degree from the
Xiao G, Sui L, Heck B, Zeng T, Tian Y (2018) Estimating satellite School of Geodesy and Geomatics in Wuhan University in 2011 and
phase fractional cycle biases based on Kalman filter. GPS Solut Ph.D. degree from the Geodetic Institute of Karlsruhe Institute of Tech-
22:82. https://d oi.o rg/1 0.1 007/s 10291-0 18-0 749-3 nology in Germany. His current research focuses on GNSS and multi-
Xiao G, Yang C, Wei H, Xiao Z, Zhou P, Li P, Dai Q, Zhang B, sensor integrated precise positioning and applications.
Yu C (2024) PPP ambiguity resolution based on factor graph
optimization. GPS Solutions 28:178. https://d oi.o rg/1 0.1 007/ Peiyuan Zhou obtained his Ph.D. from the University of Calgary and
s10291-0 24-0 1715-6 is a lecturer at Information Engineering University, China. His current
Xu Y, Yang Y, Li J (2021) Performance evaluation of BDS-3 PPP-B2b research focuses on GNSS precise positioning and remote sensing.
precise point positioning service. GPS Solut 25:142. https://d oi.
org/1 0.1 007/s 10291-0 21-0 1175-2 Peigong Li is currently a Master’s degree candidate at Information
Yao Y, He Y, Yi W, Song W, Cao C, Chen M (2017) Method for evalu- Engineering University, China. He has completed his B.Sc. the College
ating real-time GNSS satellite clock offset products. GPS Solut of Geography and Environmental Science, Henan University.
21:1417–1425. https://d oi.o rg/1 0.1 007/s 10291-0 17-0 619-4
Zhou W, Cai H, Chen G, Jiao W, He Q, Yang Y (2022) Multi-GNSS Zhengyang Xiao is a master student at Information Engineering Uni-
combined orbit and clock solutions at iGMAS. Sensors 22:457. versity. His research focuses on multi-sensor integrated precise posi-
https://d oi.o rg/1 0.3 390/s 22020 457 tioning and applications.
Zhou P, Xiao G, Du L (2024) Initial performance assessment of Gali-
leo high accuracy service with software-defined receiver. GPS Baoxiang Zhang is a postgraduate student of China University of Geo-
Solutions 28:2 sciences Beijing. He graduated from China University of Geosciences
Zumberge J, Heflin M, Jefferson D, Watkins M, Webb FH (1997) Pre- Beijing in 2021 with a major in Surveying and Mapping Engineering.
cise point positioning for the efficient and robust analysis of GPS His current research focuses on LiDAR SLAM based on factor graphs.
data from large networks. J Geophys Res Solid Earth 102:5005–
5017. https://d oi.o rg/1 0.1 029/9 6JB03 860