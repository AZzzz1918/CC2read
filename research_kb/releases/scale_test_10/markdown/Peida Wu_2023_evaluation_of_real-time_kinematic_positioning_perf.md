<!-- PAGE: 1 -->

Vol.:(0123456789)
1 3
GPS Solutions (2023) 27:192 
https://doi.org/10.1007/s10291-023-01532-3
ORIGINAL ARTICLE
Evaluation of real‑time kinematic positioning performance 
of the BDS‑3 PPP service on B2b signal
Peida Wu1 · Yidong Lou1 · Weixing Zhang1 · Jan Dousa2 · Huizhong He4,5 · Junbing Chai3 · Yongzhong Ouyang4,5 · 
Zhenyi Zhang1 · Xu Zou1
Received: 6 March 2023 / Accepted: 10 August 2023 / Published online: 25 August 2023 
© The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2023
Abstract
The BeiDou global navigation satellite system (GNSS) of China (BDS-3) had full operation capacity on July 31, 2020, and 
started providing free precise point positioning (PPP) service on B2b signals. Although GNSS community has conducted 
many evaluations on the PPP-B2b products and its user performance, comprehensive evaluations of real-time PPP solutions 
using the BDS-3 PPP service at kinematic and highly kinematic platforms are still absent. We present a general evaluation 
of a real-time PPP performance exploiting the PPP-B2b corrections in various user situations represented with static sta-
tions, a car, an offshore vessel and an aircraft. We found that errors of the PPP-B2b corrections are less stable and higher 
approximately by a factor of two for GPS compared to BDS-3 medium earth orbit (MEO) satellites. An average convergence 
time of 28.5 and 12.9 min can be achieved with a standalone BDS-3 and BDS-3 + GPS solution for a low-speed object, such 
as a permanent station, a car, and a ship, in real time when using the PPP-B2b corrections. For a high-kinematic airborne 
platform, the convergence time is much longer, reaching 48.9 min. The 95% positioning errors after convergence are less than 
20 and 35 cm in horizontal and vertical directions for all the experiments. We conclude that the PPP-B2b service offered by 
the BDS-3 is prospective for real-time kinematic positioning applications.
Keywords  BDS-3 B2b · Real-time PPP · Positioning accuracy · Convergence time
Introduction
Precise point positioning (PPP) can achieve a decimeter-/
centimeter-level positioning when using a single receiver. 
Hence, it has been widely used in scientific research and 
engineering applications, provided precise satellite orbit and 
clock products are available (Malys and Jensen 1990; Zum-
berge et al. 1997; Kouba and Héroux 2001). For real-time 
PPP users, the orbit and clock products can be obtained via 
the Internet (Internet-based PPP) or via a satellite link (Sat-
ellite-based PPP) (Xu et al. 2021). For the former, the pre-
cise products are generally sent to users using the Networked 
Transport of Radio Technical Commission for Maritime Ser-
vices (RTCM) via Internet Protocol (NTRIP). An example is 
the Real-Time Service (RTS) launched by the International 
GNSS Service (IGS) in 2013 (Elsobeiey and Al-Harbi 2016; 
Hadas and Bosy 2015), whose quality has been continuously 
improving since that time. Currently, the accuracy of orbit 
products of GPS, GLONASS, Galileo, BDS3-MEO reaches 
a centimeter level, and the accuracy of clock corrections of 
GPS and Galileo is better than 0.2 ns while those of BDS 
and GLONASS is slightly worse (Li et al. 2022; Lou et al. 
2022). Some typical products of the satellite-based real-time 
PPP service are provided by services such as the RTX of 
Trimble (Leandro et al. 2011), OmniStar (Booth and Snow 
2009) and StarFire of NavCom (Dai et al. 2016); however, 
these commercial products are paid.
To meet the demands of a future potential market and 
for the convenience of professional users, some GNSS 
 *	 Yidong Lou 
	
ydlou@whu.edu.cn
1	
GNSS Research Center, Wuhan University, Wuhan 430079, 
China
2	
Research Institute of Geodesy, Topography and Cartography, 
Zdiby 25066, Czech Republic
3	
BGP Inc China National Petroleum Corporation, 
Zhuozhou 072751, China
4	
Key Laboratory of Marine Environmental Survey 
Technology and Application, MNR, Beijing 100000, China
5	
South China Sea Marine Survey Center, MNR, 
Beijing 100000, China
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [1 Figure(s)]

<!-- PAGE: 2 -->

GPS Solutions (2023) 27:192
1 3
192 
Page 2 of 14
systems, including Galileo, Quasi-Zenith Satellite System 
(QZSS) and BeiDou system (BDS-3, hereafter referred 
BDS), have embedded the PPP service in the navigation 
system designs. On January 24, 2023, the Galileo authority 
started the delivery of an initial service of its free global 
High Accuracy Service (HAS) on the E6-B signal, target-
ing a 95% accuracy of 20 and 40 cm for real-time PPP 
horizontal and vertical positioning, respectively (Euro-
pean GNSS Service Center 2023). The new multi-GNSS 
advanced orbit and clock augmentation—precise point 
positioning (MADOCA-PPP) of QZSS launched a trial 
service on September 30, 2022, and planned to provide an 
operational service as of 2024 (Cabinet Office 2022). In 
July 2021, the BDS-3 announced the service supporting 
a kinematic decimeter-level and a static centimeter-level 
real-time PPP when using its GEO B2b signal (PPP-B2b) 
in China and surrounding areas.
Numerous studies have evaluated the performance of 
PPP-B2b products and user positioning. Tao et al. (2021) 
found that the differential code bias (DCB) of PPP-B2b 
shows a comparable performance with the DCB product 
provided by the University of the Chinese Academy of Sci-
ences (CAS). Xu et al. (2021) evaluated the accuracy and 
availability of the PPP-B2b corrections for BDS. The results 
showed that the availability of PPP-B2b corrections in China 
was better than 80%, and the root mean square (RMS) errors 
of orbits were 6.8, 33.4 and 36.6 cm in radial, along-track 
and cross-track directions for the MEO satellites, whereas 
twice higher for the inclined geostationary orbit (IGSO) sat-
ellites, and the accuracy of clock offsets was about 0.2 ns. 
Zhang et al. (2022) compared the accuracy of the PPP-B2b 
corrections for BDS and GPS using 150 days in 2021. The 
results revealed that the RMS and standard deviation (STD) 
of the signal-in-space ranging error (SISRE) of GPS were 
almost double compared to BDS.
The performance of a static real-time PPP can achieve 
centimeter-level accuracy after a convergence (Liu et al. 
2022; Ren et al. 2021). Xu et al. (2021) found that an 
accuracy of 11 cm horizontally and 17 cm vertically after 
convergence could be achieved for a kinematic PPP of a 
permanent station using B1C/B2a ionosphere-free (IF) 
combination and also discovered the B1C/B2a combination 
showed better accuracy than B1I/B3I. Zhang et al. (2022) 
demonstrated that a kinematic PPP of a car trajectory with 
PPP-B2b corrections achieved a position error of about 
23.5 (18.6) and 48.8 (37.1) cm in the horizontal and ver-
tical direction, respectively, with an average convergence 
time of 10.4 (14.2) min for a standalone BDS (BDS + GPS 
solution). Geng et al. (2022) found that a real-time PPP with 
the PPP-B2b service on a coastal area was characterized 
by a 3D error RMS of 21.3 cm for BDS and 18.2 cm for 
GPS + BDS. Some promising results were also achieved 
in seismic monitoring (Fang et al. 2022), loosely coupled 
GNSS/INS integrated navigation (Xu et al. 2022) and time 
transfer (Ge et al. 2023).
However, most of these contributions are focused on the 
accuracy of the PPP-B2b product or PPP performance in 
a single situation, for example, a permanent station, vehi-
cle experiment, or ship experiment, while knowledge of the 
performance in airborne applications is still limited. We 
comprehensively review the PPP-B2b performance in dif-
ferent applications, including static station, car, vessel and 
aircraft. We first introduce the BDS‑3 PPP‑B2b correction 
parameters and the real‑time PPP model, highlighting some 
details not mentioned in previous works. The positioning 
performance of a real‑time kinematic PPP in different situ-
ations is sequentially evaluated, discussed, and compared 
with the existing literature. A summary is finally provided.
Methodology
This section first introduces the user algorithms of apply-
ing PPP-B2b corrections, including the precise ephemeris 
recovery procedure and the datum of PPP-B2b orbit and 
clock products. Then, the real-time PPP model using PPP-
B2b corrections is presented, with special emphasis on the 
BDS satellite phase center error model.
PPP‑B2b correction parameters
Satellite orbit corrections, clock offset corrections, and DCB 
are essential products broadcasted by B2b signals. Cur-
rently, the orbit and clock corrections for GPS and BDS are 
accompanied with the DCB for BDS only (CSNO 2020a) 
to correct code biases between inter-frequency and intra-
frequency pseudoranges (Hakansson et al. 2017). Since BDS 
broadcasts multi-frequency signals, including the legacy B1I 
and B3I signals and the new B1C, B2a and B2b signals, 
the PPP-B2b DCB corrections contain multiple types, such 
as B1I-B3I, B1C-B3I, B2a-B3I and B2I-B3I. Hence, users 
are able to exploit multi-frequency real-time BDS PPP sup-
ported with these DCB corrections (Jin and Su 2020).
The precise satellite position 퐗orbit can be obtained from 
the following expression:
where 퐗broadcast denotes a satellite position calculated 
from the broadcast ephemeris. Specifically, the broadcast 
ephemeris to be used for BDS and GPS is the civil naviga-
tion (CNAV1) message of the B1C signal and the legacy 
(1)
⎧
⎪
⎪
⎨
⎪
⎪⎩
퐗orbit = 퐗broadcast −𝛿퐗
𝛿퐗=  퐞R 퐞A 퐞C
 ⋅𝛿퐎
퐞R = 퐫
퐫, 퐞C = 퐫× ̇퐫
퐫× ̇퐫, 퐞A = 퐞C × 퐞R
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 3 -->

GPS Solutions (2023) 27:192	
1 3
Page 3 of 14 
192
navigation (LNAV) message of the L1C/A signal, respec-
tively (CSNO 2020a). 훿퐗 is then a satellite position correc-
tion in the Cartesian coordinate system, 훿퐎 is a PPP-B2b 
orbit correction vector, 퐞R , 퐞A and 퐞C are direction unit vector 
for radial, along-track, and cross-track correction compo-
nents, and 퐫 and ̇퐫 are the satellite position and velocity vec-
tor calculated from the broadcast ephemeris.
The precise satellite clock tclock can be obtained by
where tbroadcast denotes a satellite clock estimated from broad-
cast ephemeris, C0 is a clock correction, and c is the velocity 
of light in vacuum.
It should be noted, corrected with the PPP-B2b products, 
satellite precise orbits and clocks correspond to the antenna 
reference point (ARP), and it is consistent with the datum 
of frequency of broadcast ephemeris, which is B3I for BDS 
and IF combination of C1W and C2W for GPS.
The expression for applying the DCB is defined as
where lsig and ̃lsig are pseudorange with and without correct-
ing DCB value ( DCBsig ). As mentioned before, DCB cor-
rections are not yet provided for GPS. If GPS pseudoranges 
are not in accordance with the datum of GPS broadcast 
ephemeris, these require applying of either the inter-signal 
corrections (ISC) from the new GPS CNAV message (Feess 
et al. 2013; Steigenberger et al. 2015) or the DCB from any 
IGS analysis center. In our work, the ISC from GPS CNAV 
message are used.
Real‑time PPP model using PPP‑B2b corrections
The dual-frequency IF combinations of GNSS pseudorange 
and phase observations can be expressed as follows,
where Ps
r,IF and Ls
r,IF denote pseudorange and phase IF obser-
vations, respectively, 휌s
r represents a satellite-to-receiver geo-
metric distance with subscripts r for a receiver and s for a 
satellite, dtr,IF and dts
IF are receiver and satellite clock offsets, 
dr,IF and ds
IF are the receiver and satellite hardware delays of 
the pseudorange IF combination, br,IF and bs
IF are hardware 
delays of the phase IF combination, Trs
r is the tropospheric 
delay, 휆IF refers to the wavelength of L1 or B1, Ns
r,IF is the 
IF ambiguity, 휀s
r,IF,L and 휀s
r,IF,P is the observation noise for 
Ps
r,IF and Ls
r,IF , respectively. Any other errors, such as phase 
wind-up, relativistic effects, and tide displacement, have 
been corrected with precise models.
(2)
tclock = tbroadcast −C0
c
(3)
̃lsig = lsig −DCBsig
(4)
{
Ps
r,IF = 휌s
r + (dtr,IF −dts
IF
) + (dr,IF −ds
IF
) + Trs
r + 휀s
r,IF,P
Ls
r,IF = 휌s
r + (dtr,IF −dts
IF
) + (br,IF −bs
IF
) + Trs
r + 휆IFNs
r,IF + 휀s
r,IF,L
The datum of BDS broadcast clock offset aligns with the 
B3I signal; thus, the satellite clock offset calculated from (2) 
still contains pseudorange hardware delay of the B3I signal. 
The DCB correction is required to implement a full consist-
ency of the broadcast ephemeris datum for BDS3 satellites. 
Considering dts
IF + ds
IF = dts
B3I + (ds
IF −ds
B3I
) , and assuming 
we use the B1I/B3I IF combination, we can obtain
where fB1I and fB3I are the frequency of the B1I and the B3I 
signal, respectively, and the DCBB1I−B3I is from the PPP-B2b 
product. The observation equations can be then expressed as
where dtr,IF = dtr,IF + dr,IF and N
s
r,IF = 휆IFNs
r,IF + br,IF −dr,IF −bs
IF + ds
B3I 
are user-estimated receiver IF pseudorange delay and IF 
phase ambiguity, respectively, and dts
B3I is the recovered 
BDS satellite clock offset. Additionally, the inter-system 
biases (ISB) should be estimated if multi-GNSS observa-
tions are used (Zuo et al. 2021).
It is necessary to note that the phase center offsets (PCO) 
and phase center variations (PCV) for BDS satellites should 
be corrected by using the model released by the BDS author-
ity when PPP is implemented based on PPP-B2b products 
(https://​www.​beidou.​gov.​cn/).
SISRE evaluation
The accuracy assessment of the PPP-B2b corrections is con-
ducted before evaluating the PPP performance in various 
situations. We use the SISRE as an accurate indicator of 
the PPP-B2b corrections. It is a statistical uncertainty due 
to errors in satellite orbit and clock product and a key per-
formance indicator for the comparison of different GNSS 
(Montenbruck et al. 2015). The SISRE can be calculated 
as follows
where R, A, and C denote orbit errors in radial, along and 
cross directions in meter, and Clk represents a satellite clock 
error in meter.
(5)
ds
IF −ds
B3I = f 2
B1I ⋅DCBB1I−B3I
f 2
B1I −f 2
B3I
(6)
⎧
⎪
⎨
⎪⎩
Ps
r,IF = 휌s
r +

dtr,IF −dts
B3I

−f 2
B1I ⋅DCBB1I−B3I
f 2
B1I −f 2
B3I
+ Trs
r + 휀s
r,IF,P
Ls
r,IF = 휌s
r +

dtr,IF −dts
B3I

+ Trs
r + N
s
r,IF + 휀s
r,IF,L
(7)
SISRE =
⎧
⎪
⎪
⎨
⎪
⎪⎩

(0 ⋅98 ⋅R −Clk)2 + 1
49
A2 + C2 GPS

(0 ⋅99 ⋅R −Clk)2 +
1
126
A2 + C2 BDS(GEO∕IGSO)

(0 ⋅98 ⋅R −Clk)2 + 1
54
A2 + C2 BDS(MEO)
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 4 -->

GPS Solutions (2023) 27:192
1 3
192 
Page 4 of 14
We used the post-processing multi-GNSS products 
(GBM) provided by GeoForschungsZentrum Potsdam 
(GFZ) (Deng et al. 2017) as a reference for evaluating the 
BDS PPP-B2b orbit and clock corrections during the test 
period. The GBM products are in the IGb14 framework, 
while BDS employs the CGCS2000 framework. The differ-
ences between the two frameworks are negligible compared 
to the centimeter-level accuracy of the PPP-B2b products, 
so ignored. And PCO was corrected with the model released 
by IGS for keeping consistency with the GBM products. 
The SISRE RMS and STD were calculated for all satellites, 
first on a daily basis and second as averages over the entire 
test period.
Figure 1 shows the SISRE RMS and STD of the PPP-
B2b product from April to October 2022, i.e., covering the 
period of all the test cases in our work. The gaps in Fig. 1 
are due to receiver failures; hence, data are not available 
for the statistics. After removing a small number of outliers 
(6% for GPS) clearly observed in Fig. 1, the SISRE RMS is 
0.48 m, 0.76 m and 0.82 m for BDS MEO, IGSO and GPS 
satellites, respectively, and the corresponding SISRE STD 
is 0.29 m, 0.44 m and 0.52 m. Some outliers close to 3 m 
can be observed for GPS SISRE RMS, attributed mainly 
to the low accuracy (up to 6 ns) of PPP-B2b satellite clock 
offsets during these days. On the other hand, no outliers 
are observed for the BDS SISRE. Overall, the errors of the 
PPP-B2b corrections are approximately by a factor of two 
larger for GPS compared to BDS and less stable too. The 
results agree with conclusions from previous works (Tao 
et al. 2021; Zhang et al. 2022). The smaller errors in the 
regional network are attributed to inter-satellite links avail-
able within the BDS system (Yang et al. 2020). In PPP pro-
cessing, we thus use a weighting strategy for BDS and GPS 
in accordance with the SISRE results.
Positioning performance of real‑time kinematic PPP
We used a variety of platforms, including permanent sta-
tions, car, offshore vessel, and flying aircraft, to evaluate 
real-time PPP-B2b performance at a user side. BDS and 
GPS observations from daily files were processed in a sim-
ulated real-time mode along with the PPP-B2b corrections 
recorded by a receiver. The data processing strategy is sum-
marized in Table 1.
Permanent station experiment and results
We used 30-s observations collected at four stations (BJF1, 
KUN1, LHA1 and SHA1) from the international GNSS 
monitoring and assessment system (iGMAS) and one sta-
tion (JFNG) from the IGS multi-GNSS experiment (MGEX) 
from April 18 to 24, 2022. The reference positions were 
extracted from the final solutions on April 21, 2022, pro-
vided in the software independent exchange format (SINEX) 
released by iGMAS and IGS, respectively. We defined the 
PPP convergence time as an interval before reaching the 
position error smaller than 0.2 and 0.4 m for the horizontal 
and vertical components, respectively, for 10 continuous 
Fig. 1   SISRE RMS and STD of 
PPP-B2b corrections for GPS, 
BDS MEO and BDS IGSO 
satellites from April to October 
2022
0
1
2
3
RMS (m)
BDS-MEO = 0.48m
BDS-IGSO = 0.76m
GPS = 0.82m
BDS-MEO
BDS-IGSO
GPS
100
150
200
250
300
350
Day of year in 2022
0
1
2
3
STD (m)
BDS-MEO = 0.29m
BDS-IGSO = 0.44m
GPS = 0.52m
Content courtesy of Springer Nature, terms of use apply. Rights reserved.


|Col1|Col2|Col3|BDS-MEO =<br>BDS-IGSO|0.48m<br>= 0.76m|
|---|---|---|---|---|
||||GPS = 0.82|m|




|Col1|Col2|Col3|BDS-MEO =<br>BDS-IGSO|0.29m<br>= 0.44m|
|---|---|---|---|---|
||||GPS = 0.52|m|



<!-- PAGE: 5 -->

GPS Solutions (2023) 27:192	
1 3
Page 5 of 14 
192
minutes at least. An accuracy indicator was the 95% small-
est ranked epoch-wise position error excluding the period 
needed for the convergence.
Figure 2 shows kinematic position errors of real-time PPP 
using the PPP-B2b corrections for BJF1 and JFNG stations 
on April 21, 2022. Similar results are obtained for other 
days too; however, the presented day facilitates a comparison 
with the results of car experiments. The results reveal that a 
kinematic PPP converges quickly to the decimeter level for 
both BDS and BDS + GPS. All positioning errors remain 
within 40 cm in both N (north), E (east) and U (up) compo-
nents after the convergence, and the stability of BDS + GPS 
results outperforms BDS-only. The average horizontal and 
vertical position accuracy in Fig. 2 is 10.6 cm and 14.2 cm 
for BDS compared to 8.3 cm and 12.2 cm for BDS + GPS 
combined solutions.
In Fig. 2, we notice a small jump in the results shortly 
before 9:00. Since it occurs at all stations at the same time, 
we attribute it to the PPP-B2b corrections. Hence, we ana-
lyze in detail the PPP-B2b orbit and clock offsets on that day 
(April 21, 2022) in Fig. 3. The error time series of the radial 
orbit component and the clock offset are normal, but disper-
sions of along-track and cross-track orbit errors are high and 
suddenly reduced at about 9:00, while SISRE also exhibits a 
small jump. This change occurs for all visible BDS satellites; 
hence, we consider it caused a small jump in the position 
time series. We are unable to explain this issue further and 
we can only attribute it to a problem on the provider side.
To further analyze the convergence performance of the 
real-time PPP based on PPP-B2b corrections, the daily 
observations are divided into 43 segments with a length of 
3 h and a moving step of 30 min, resulting in 1505 segments 
in total for the test period. The average convergence time 
of these samples is 28.5 and 12.9 min for BDS-only and 
BDS + GPS, respectively. The 95% errors for BDS solution 
after convergence are 19.7 and 21.7 cm in the horizontal and 
vertical components, respectively, while 13.4 cm and 16.2 
cm for BDS + GPS. It can be found that the dual-constella-
tion solution converges faster with smaller errors than stan-
dalone BDS. Due to a different accuracy indicator, there are 
some differences in our results compared to Xu et al. (2021) 
who reported the average RMS 11.0 and 16.8 cm for BDS-
only horizontal and vertical positioning errors, respectively. 
But the accuracy is close to each other.
Car experiment and results
The car experiment was conducted near the BJF1 station 
(Beijing, China) on April 21, 2022, the same day as the 
results in Fig. 2, with a duration of 90 min and a sampling 
rate of 1 s. The observations were collected by a SOUTH 
RT300 GNSS receiver with a Harxon HX-CSX049A 
antenna. The speed of the car was within 10 km/h. The 
positioning accuracy and convergence time were analyzed 
similarly to the static experiment. The real-time kinematics 
(RTK) solution was used as a reference trajectory.
Table 1   Processing strategy for real-time PPP
Item
Correction model or estimation strategy
Observations
Ionosphere-free linear combination of L1/L2 for GPS and B1I/B3I for BDS
Elevation cutoff
7°
Observations weighting strategy
Elevation-dependent: 1 for elevation (E) > 30°, otherwise 2*sin(E) A-priori sigma: 3 mm and 0.5 m for 
phase and code observation Weight ratio is 1:2 for GPS and BDS satellites, and 1:2 for IGSO and MEO of 
BDS satellites
Satellite orbit and clock offsets
B1C CNAV1 broadcast ephemeris for BDS and LNAV broadcast ephemeris for GPS + PPP-B2b corrections
Satellite DCB
PPP-B2b DCB corrections for BDS; CAS DCB products (Wang et al. 2016) for GPS if needed
Satellite PCO/PCV
igs14.atx (Schmid et al. 2016) for GPS; antenna file provided by the BDS authority for BDS
Phase windup
Model corrected
Relativistic effect
Model corrected
Tide model
Solid tide; Polar tide; Ocean tide (Petit and Luzum 2010))
Ionosphere
Eliminated by IF combination
Troposphere
Zenith hydrostatic delay (ZHD) is corrected by GPT3 (Landskron and Bohm 2018) and Saastamoinen 
model (Saastamoinen 1972); mapping function is GPT3; Zenith wet delay (ZWD) is estimated as a ran-
dom walk with the process noise of 5mm∕√h
Receiver PCO/PCV
igs14.atx for GPS; use GPS values for BDS if corresponding values are not provided
Receiver clock
Estimated as white noise
ISB
Estimated as a random walk with the process noise of 5mm∕√
h
Receiver position
Epoch-wise parameter without constrains between epochs
Ambiguity
Float
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 6 -->

GPS Solutions (2023) 27:192
1 3
192 
Page 6 of 14
The car trajectory and the location of the RTK base sta-
tion are shown in Fig. 4 (left panel). The length of the RTK 
baseline is less than 6000 m, and the RTK fix rate is 99.9% 
and the unfixed RTK results are removed. The number of 
satellites in the car test period is shown in Fig. 4, with the 
average number of visible BDS and GPS satellites of 7.1 
and 5.8, respectively.
Figure 5 shows time series of kinematic positioning errors 
in car experiment. The accuracy of a standalone BDS PPP is 
11.2 and 17.4 cm in the horizontal and vertical components, 
respectively, with a convergence time of about 5.1 min. For 
BDS + GPS PPP, it is 10.6 and 16.6 cm and the convergence 
time is approximately 4.3 min. The accuracy and the conver-
gence time of the dual-constellation outperform a standalone 
one (BDS). Car and station positioning experiments yielded 
similar performances, both coming from the same day.
Offshore vessel experiment and results
The offshore real-time PPP experiment with the BDS 
PPP-B2b corrections was conducted in the surrounding 
sea areas of Dongying City, Shandong Province, China. 
The experiment period lasted from 4:20:00 to 8:00:00 
(GPS time) on October 22, 2022, with the speed of the 
ship within 20 km/h. The antenna was mounted on the 
top of the cockpit of a fishing boat, as shown in Fig. 6, 
and the BDS and GPS observations were collected with a 
sampling rate of 1 s by Sino K803 GNSS module with a 
VLG GNSS-R44QH antenna.
The RTK solution is taken as a reference again; the ship 
trajectory and the RTK base station are shown in Fig. 7 
(left panel). The distances of the RTK baseline are less 
than 3500 m, the RTK fix rate is 99.9%, and the unfixed 
RTK results are removed. The number of satellites in the 
offshore experiment period is shown in Fig. 7, with the 
average number of visible BDS and GPS satellites of 7.8 
and 4.2, respectively.
The positioning errors from real-time PPP with the 
BDS PPP-B2b corrections are shown in Fig. 8. The accu-
racy for BDS PPP is 12.7 and 25.1 cm in the horizontal 
and vertical components, respectively, with a conver-
gence time of about 29.0 min. For BDS + GPS PPP, it is 
10.8 and 21.0 cm, and the convergence time is approxi-
mately 6.1 min. The positioning accuracy as well as the 
convergence time is improved with the inclusion of GPS 
satellites. Conspicuous fluctuations remain before the 
convergence in time series of the positioning error of 
the standalone BDS solution; however, this fluctuation 
is eliminated after including GPS satellites, indicating 
that dual-constellation can accelerate the convergence. A 
-1.2
-0.8
-0.4
0
0.4
0.8
1.2
Positioning errors (m)
BJF1 BDS
Hor.=11.6cm,Ver.=15.2cm
Convergence time=4.5min
N
E
U
BJF1 BDS + GPS
Hor.=9.4cm,Ver.=14.8cm
Convergence time=4.5min
N
E
U
0
4
8
12
16
20
24
GPS time (h)
-1.2
-0.8
-0.4
0
0.4
0.8
1.2
Positioning errors (m)
JFNG BDS
Hor.=9.5cm,Ver.=13.2cm
Convergence time=10.5min
N
E
U
0
4
8
12
16
20
24
GPS time (h)
JFNG BDS + GPS
Hor.=7.1cm,Ver.=9.5cm
Convergence time=10.0min
N
E
U
Fig. 2   BDS (left) and BDS + GPS (right) positioning errors of real-time kinematic PPP using PPP-B2b corrections for BJF1 (top) and JFNG 
(bottom) station on April 21, 2022
Content courtesy of Springer Nature, terms of use apply. Rights reserved.


|H|or.|=11.6|cm,Ver.|=15.|2cm|Col7|
|---|---|---|---|---|---|---|
|H|or|=116|cmVer|=15|2cm||
|C|on|.<br>verge|,.<br>nce time|=4.|5min||
||||||||
||||||||
||||||||
||||||||
||||||||
||||JF1 B|S|||
||||||||




|H|or.=9.4c|m,Ve|r.|=1|4.8|c|m|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|H|or=94c|mVe|r|=1|48|c|m||||N|
|C|..<br>onvergen|,<br>ce t|.<br> im|e|.<br> =4.|5m|in||||E|
||||||||||||U|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||JF1|B|D|S +|G|PS|||||
|||||||||||||




|H|or.|=9.5c|m,Ver.=|13.2|cm|Col7|
|---|---|---|---|---|---|---|
|H|or|=95c|mVer=|132|cm||
|C|on|.<br>verge|,.<br>nce time|.<br> =10|.5min||
||||||||
||||||||
||||||||
||||||||
||||||||
||||FNG B|DS|||
||||||||




|H|or.=7.1c|m,Ve|r.|=9|.5c|m|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|H|or=71c|mVe|r|=9|5c|m|||||N|
|C|..<br>onvergen|,<br>ce t|.<br> im|e|.<br> =10|.0|min||||E|
||||||||||||U|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
||J|FN||BD|S||PS|||||
|||||||||||||



<!-- PAGE: 7 -->

GPS Solutions (2023) 27:192	
1 3
Page 7 of 14 
192
similar improvement in the vertical direction can also be 
observed in Geng et al. (2022).
Unmanned aircraft experiment and results
In addition to the experiments described above, we also 
carried out an aircraft experiment on July 24, 2022, with a 
duration of about 4 h and a sampling rate of 0.1 s (HI-TAR-
GET K20 receiver and AT-35101 antenna). The reference 
trajectory was processed using the RTK method (CHCHAV 
P5 receiver and HX-CSX627A antenna), the GBM post-
processing products (Deng et al. 2017), and the Inertial 
Explorer (IE) software by the Novatel company (https://​
novat​el.​com). The RTK reference was not fixed solutions. 
However, the software provided three-dimensional (3D) 
STD as coordinate accuracy indicators. The percentage of 
RTK references whose 3D STD was better than 4 cm was 
about 92%, between 4 and 6 cm, about 7.7%, and above 
6 cm, about 0.3%. In order to match the RTK reference, the 
raw observations were re-sampled to 1 s.
Figure 9 displays a brief trajectory of the aircraft in the 
experiment. We can see that the aircraft ascends fast at the 
beginning (GPST 4.0—4.4 h), then horizontally flies to 
the southeast direction (4.4—5.5 h) and descends (5.5—
5.8 h), finally keeps a quasi-rectangle trajectory of ten strips 
(5.8—7.8 h). The aircraft's velocity is about 230 km/h in the 
experiment period. The baseline length of RTK gradually 
decreases from 400 to 20 km over time.
According to the characteristics of aircraft trajectory, 
we optimize the process noise of zenith tropospheric delay 
Fig. 3   Error time series of the PPP-B2b real-time orbits, clock offsets and SISRE for the BDS satellites on April 21, 2022 (the subplot in the 
SISRE panel represents the SISRE time series for satellite C25 between 8:30—9:00)
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [1 Figure(s)]

<!-- PAGE: 8 -->

GPS Solutions (2023) 27:192
1 3
192 
Page 8 of 14
(ZTD) to adapt the fast attitude change. First, we extract the 
time and coordinates of the beginning and end point of the 
ascending and descending phases. Second, the ZTD at the 
corresponding position and moment is calculated by NWMs-
based Site module of GMET Online Service (http://​gmet.​
users.​sgg.​whu.​edu.​cn/). Then, it is possible to calculate the 
process noise of ZTD in these two stages using the expres-
sion in Hadas et al. (2017). Eventually, the process noise of 
ZTD is set to 15 cm/√h when the aircraft is climbing and 
descending and maintained at 5 mm/√h when the aircraft 
is leveling.
Figure 10 shows the positioning errors and the height 
of the aircraft. The accuracy of the BDS and BDS + GPS 
PPP is 18.1 (32.8) cm and 17.1 (31.3) cm in the horizontal 
(vertical) direction, respectively, and the convergence time is 
approximately 48.9 and 43.1 min. In Fig. 10, we can clearly 
see how the altitude of the aircraft changes over time. The 
aircraft ascends fast to the altitude of 2000 m and after about 
an hour, descends to an altitude of about 500 m and, finally, 
maintains this altitude until the end of the experiment.
In Fig. 10, visible undulation is present in both BDS and 
BDS + GPS combined solutions during the flight in strips, 
and the positioning error varies sharply during the period 
when the aircraft is maneuvering between adjoining strips. 
Fig. 4   Car trajectory and loca-
tion of RTK base station (left) 
and number of visible satellites 
(right)
116.03
116.08
Longitude (°)
39.48
39.54
Latitude (°)
Car trajectory
RTK base
2
2.5
3
GPS time (h)
0
2
4
6
8
10
12
Number of satellites
GPS
BDS
-1.2
-0.6
0
0.6
1.2
Positioning errors (m)
BDS
Hor.=11.2cm,Ver.=17.4cm
Convergence time=5.1min
N
E
U
2
 
 
 
 
3
GPS time (h)
-1.2
-0.6
0
0.6
1.2
BDS + GPS
Hor.=10.6cm,Ver.=16.6cm
Convergence time=4.2min
N
E
U
Fig. 5   BDS-only (top) and BDS + GPS (bottom) real-time kinematic 
PPP positioning errors for car experiment
Fig. 6   Receiver antenna and 
environment for offshore real-
time positioning experiment
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [1 Figure(s)]


|r.=11.2cm,Ver.=|17.4cm|Col3|
|---|---|---|
|..,.<br>|.<br>||
|nvergence time=|5.1min||
||||
||||
||||
|||N|
|||E|
|BDS|||
|||U|




|r.=10.6cm,Ver.=|16.6cm|Col3|
|---|---|---|
|..,.<br>|.<br>||
|nvergence time=|4.2min||
||||
||||
||||
||||
||||
||||
|BDS +|GPS||
||||



<!-- PAGE: 9 -->

GPS Solutions (2023) 27:192	
1 3
Page 9 of 14 
192
A similar coordinate error pattern in airborne platforms is 
also discovered by Shi et al. (2017), Grayson et al. (2018), 
Shi et al. (2020) and Ocalan et al. (2022). Therefore, we con-
sider it as a normal error in the GNSS-driven positioning of 
the airborne platform, and it is logically independent on the 
PPP-B2b corrections. In PPP-supported aerial triangulation, 
Shi et al. (2017) utilized three translation and three drift 
parameters to compensate this strip-dependent coordinate 
error, and a satisfactory improvement is obtained. How-
ever, in post-processing mode, this compensation method is 
mainly purposed to eliminate the effect of systematic errors 
induced by GNSS positioning on the perspective center of 
the aerial camera in aerial triangulation. Therefore, we do 
not intend to compensate for this strip-dependent undulation 
in our simulated real-time PPP result.
The number of satellites of BDS and BDS + GPS and 
corresponding position dilution of precision (PDOP) are 
shown in Fig. 11. During the approximate 4-h period, the 
average PDOP and number of satellites of single BDS are 
9.3 and 7.9, respectively. Dual-constellation then provides 
an average PDOP of 3.8 and number of satellites of 12.3. 
The convergence time for the aircraft is significantly longer 
than that of the other experiments. In Fig. 11, we notice two 
spikes in PDOP series at about 4.1 h and 4.4 h induced by 
the change in the number of satellites. Both two fast changes 
appear during the convergence and the PDOP changes fre-
quently before the second spike (at about 4.4 h). These two 
reasons can explain the relatively longer convergence time 
for the aircraft experiment.
Discussions
To compare the results in different platforms, we summarize 
the accuracy and the convergence time of all the positioning 
experiments in Table 2. The positioning accuracy is gener-
ally consistent with the official declaration of the positioning 
error at a decimeter level for the kinematic mode when using 
the BDS PPP service (CNSO 2020b).
Fig. 7   Ship trajectory and loca-
tion of RTK base station (left) 
and number of visible satellites 
(right)
118.96
119.02
Longitude (°)
38.02
38.03
Latitude (°)
ship trajectory
RTK base
5
6
7
GPS time (h)
0
2
4
6
8
10
12
Number of satellites
GPS
BDS
-1.2
-0.6
0
0.6
1.2
Positioning errors (m)
BDS-3
Hor.=12.7cm,Ver.=25.1cm
Convergence time=29.0min
N
E
U
5
 
6
 
7
GPS time (h)
-1.2
-0.6
0
0.6
1.2
BDS-3 + GPS
Hor.=10.8cm,Ver.=21.0cm
Convergence time=6.1min
N
E
U
Fig. 8   BDS-only (top) and BDS + GPS (bottom) real-time kinematic 
PPP positioning errors for offshore experiment
Content courtesy of Springer Nature, terms of use apply. Rights reserved.


|Hor.=12.7cm,Ver.=25.1cm<br>1.2 N<br>Convergence time=29.0min E<br>0.6 U<br>0<br>(m)<br>-0.6<br>errors<br>BDS-3<br>-1.2<br>Positioning<br>Hor.=10.8cm,Ver.=21.0cm<br>1.2 N<br>Convergence time=6.1min<br>E<br>0.6<br>U<br>0<br>-0.6<br>BDS-3 + GPS<br>-1.2<br>5 6 7<br>GPS time (h)|Col2|Hor.=|12.7c|m,Ver.|=25.1c|m|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>Positioning errors (m)<br>BDS-3<br>Hor.=12.7cm,Ver.=25.1cm<br>Convergence time=29.0min<br>N<br>E<br>U<br>5<br>6<br>7<br>GPS time (h)<br>-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>BDS-3 + GPS<br>Hor.=10.8cm,Ver.=21.0cm<br>Convergence time=6.1min<br>N<br>E<br>U||Hor=|127c|mVer|=251c|m|||||
|-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>Positioning errors (m)<br>BDS-3<br>Hor.=12.7cm,Ver.=25.1cm<br>Convergence time=29.0min<br>N<br>E<br>U<br>5<br>6<br>7<br>GPS time (h)<br>-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>BDS-3 + GPS<br>Hor.=10.8cm,Ver.=21.0cm<br>Convergence time=6.1min<br>N<br>E<br>U||.<br>|.<br>|,.<br>|.<br>||||||
|-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>Positioning errors (m)<br>BDS-3<br>Hor.=12.7cm,Ver.=25.1cm<br>Convergence time=29.0min<br>N<br>E<br>U<br>5<br>6<br>7<br>GPS time (h)<br>-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>BDS-3 + GPS<br>Hor.=10.8cm,Ver.=21.0cm<br>Convergence time=6.1min<br>N<br>E<br>U||Conv|ergen|e tim|=29.0|min|||||
|-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>Positioning errors (m)<br>BDS-3<br>Hor.=12.7cm,Ver.=25.1cm<br>Convergence time=29.0min<br>N<br>E<br>U<br>5<br>6<br>7<br>GPS time (h)<br>-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>BDS-3 + GPS<br>Hor.=10.8cm,Ver.=21.0cm<br>Convergence time=6.1min<br>N<br>E<br>U|||||||||||
|-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>Positioning errors (m)<br>BDS-3<br>Hor.=12.7cm,Ver.=25.1cm<br>Convergence time=29.0min<br>N<br>E<br>U<br>5<br>6<br>7<br>GPS time (h)<br>-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>BDS-3 + GPS<br>Hor.=10.8cm,Ver.=21.0cm<br>Convergence time=6.1min<br>N<br>E<br>U|||||||||||
|-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>Positioning errors (m)<br>BDS-3<br>Hor.=12.7cm,Ver.=25.1cm<br>Convergence time=29.0min<br>N<br>E<br>U<br>5<br>6<br>7<br>GPS time (h)<br>-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>BDS-3 + GPS<br>Hor.=10.8cm,Ver.=21.0cm<br>Convergence time=6.1min<br>N<br>E<br>U|||||||||||
|-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>Positioning errors (m)<br>BDS-3<br>Hor.=12.7cm,Ver.=25.1cm<br>Convergence time=29.0min<br>N<br>E<br>U<br>5<br>6<br>7<br>GPS time (h)<br>-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>BDS-3 + GPS<br>Hor.=10.8cm,Ver.=21.0cm<br>Convergence time=6.1min<br>N<br>E<br>U|||||||||||
|-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>Positioning errors (m)<br>BDS-3<br>Hor.=12.7cm,Ver.=25.1cm<br>Convergence time=29.0min<br>N<br>E<br>U<br>5<br>6<br>7<br>GPS time (h)<br>-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>BDS-3 + GPS<br>Hor.=10.8cm,Ver.=21.0cm<br>Convergence time=6.1min<br>N<br>E<br>U|||||||||||
|-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>Positioning errors (m)<br>BDS-3<br>Hor.=12.7cm,Ver.=25.1cm<br>Convergence time=29.0min<br>N<br>E<br>U<br>5<br>6<br>7<br>GPS time (h)<br>-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>BDS-3 + GPS<br>Hor.=10.8cm,Ver.=21.0cm<br>Convergence time=6.1min<br>N<br>E<br>U|||BD|S-3|||||||
|-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>Positioning errors (m)<br>BDS-3<br>Hor.=12.7cm,Ver.=25.1cm<br>Convergence time=29.0min<br>N<br>E<br>U<br>5<br>6<br>7<br>GPS time (h)<br>-1.2<br>-0.6<br>0<br>0.6<br>1.2<br>BDS-3 + GPS<br>Hor.=10.8cm,Ver.=21.0cm<br>Convergence time=6.1min<br>N<br>E<br>U|||||||||||




|Col1|Hor.=|10.8c|m,Ver.|=21.0c|m|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||Hor=|108c|mVer|=210c|m|||||
||.<br>|.<br>|,.<br>|.<br>|||N<br>|||
||Conv|ergen|e tim|=6.1m|in||E|||
||||||||U|||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||BD|S-3 +|GPS||||||
|||||||||||



<!-- PAGE: 10 -->

GPS Solutions (2023) 27:192
1 3
192 
Page 10 of 14
Fig. 9   Aircraft trajectory in three-dimensional diagram (left), and in latitude and longitude (right)
Fig. 10   BDS-only (top), the 
BDS + GPS (middle) kinematic 
PPP positioning errors for the 
aircraft experiment. The height 
of the aircraft is shown at the 
bottom. The gray backgrounds 
are adopted to identify ten strips
-1.2
-0.6
0
0.6
1.2
Positioning errors (m)
BDS
Hor.=18.1cm,Ver.=32.8cm
Convergence time=48.9min
N
E
U
-1.2
-0.6
0
0.6
1.2
BDS + GPS
Hor.=17.1cm,Ver.=31.3cm
Convergence time=43.0min
4
4.5
5
5.5
6
6.5
7
7.5
GPS time (h)
0
1000
2000
Height (m)
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [1 Figure(s)]

<!-- PAGE: 11 -->

GPS Solutions (2023) 27:192	
1 3
Page 11 of 14 
192
The permanent station, car and offshore vessel, which 
all can be classified as static or low kinematic platforms, 
achieves a similar performance in terms of positioning accu-
racy. The positioning errors after convergence at the 95% 
confidence level are generally superior to 20 cm in horizon-
tal directions and 26 cm in vertical directions. However, the 
high kinematic airborne PPP experiment results in slightly 
worse positioning accuracy and significantly longer con-
vergence time, but still with an error of less than 20 and 
35 cm in the horizontal and vertical directions, respectively. 
A relatively poor accuracy of the aircraft is attributed to the 
strip-dependent pattern error. Due to the limited duration of 
observations in the vehicle experiment, the convergence time 
in Table 2 is indicative requiring a careful interpretation.
Regarding the comparison between BDS-only and 
BDS + GPS PPP, the latter generally outperforms the former. 
After including additional constellation, the convergence is 
shortened considerably (by more than 70%), as shown in the 
offshore vessel experiment. While as it concern position-
ing error, due to our choice of a 95% error as the accuracy 
indicator, the improvements in horizontal and vertical are 
in the range of 4.6% (vertical component in car and aircraft 
experiment) and 32.0% (horizontal component in permanent 
station experiment).
Conclusions
The BDS PPP service provides a promising opportunity for 
exploiting real-time PPP for GNSS users in China and sur-
rounding areas. This featured service will also have great 
potential in environments without a stable Internet network.
We present a comprehensive evaluation of the kinematic 
PPP performance of the PPP-B2b service in different situ-
ations. The statistical results of seven days of observations 
at five permanent stations indicate that the average conver-
gence time is 28.5 min for standalone BDS, and 12.9 min 
for BDS + GPS. In terms of accuracy, represented by the 
95% positioning errors after the convergence, the BDS solu-
tion using the B1I/B3I IF combination achieves 19.7 cm in 
the horizontal directions and 21.7 cm in the vertical. For 
BDS + GPS combined solutions, the accuracy is 13.4 and 
16.2 cm in horizontal and vertical directions, respectively.
Similarly, the PPP car experiment exhibits an accuracy of 
11.2 (10.6) and 17.4 (16.6) cm in the horizontal and vertical 
direction, respectively, with a convergence of 5.1 (4.3) min 
for BDS (BDS + GPS) solution. The accuracy of the offshore 
positioning is 12.7 (10.8) and 25.1 (21.0) cm in horizontal 
and vertical components after a convergence of 29.0 (6.1) 
min. The aircraft-based PPP experiment, however, results in 
a positioning accuracy of 18.1 cm in horizontal and 32.8 cm 
in vertical components after a convergence time of 48.9 min 
for BDS-only. When combining BDS and GPS, the average 
positioning accuracy becomes 17.1 and 31.3 cm in horizon-
tal and vertical directions, respectively, i.e., without signifi-
cant improvements compared to the BDS accuracy, while 
the convergence time decreases to 43.1 min. Thus, airborne 
positioning results become slightly worse compared to low 
kinematic vehicle experiments.
The achieved positioning accuracies from different exper-
iments are consistent with the official declaration of the posi-
tioning errors for the BDS-B2b service, i.e., to support a 
decimeter level. In future, the PPP services of other GNSS 
0
10
20
PDOP
BDS  9.3
BDS + GPS  3.8
4
4.5
5
5.5
6
6.5
7
7.5
GPS time (h)
0
10
20
Number of satellites
BDS  7.9
BDS + GPS  12.3
Fig. 11   PDOP (top) and number of satellites (bottom) in aircraft 
experiment. The gray backgrounds are adopted to mark ten strips
Table 2   95% positioning 
error (after convergence), 
convergence time for the real-
time kinematic experiment, and 
improvements of BDS + GPS 
results compared to BDS.
BDS / BDS + GPS
Improvement rate (dual-constellation)
Horizontal[cm] Vertical[cm] Conver-
gence Time 
[min]
Horizontal[%] Vertical[%] Conver-
gence Time 
[%]
Permanent station 19.7 / 13.4
21.7 / 16.2
28.5 / 12.9
32.0
25.6
54.7
Car
11.2 /10.6
17.4 / 16.6
5.1 / 4.2
5.4
4.6
17.6
Offshore vessel
12.7 / 10.8
25.1 / 21.0
29.0 / 6.1
15.0
16.3
79.0
Aircraft
18.1 / 17.1
32.8 / 31.3
48.9 / 43.0
5.5
4.6
12.1
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 12 -->

GPS Solutions (2023) 27:192
1 3
192 
Page 12 of 14
systems, such as Galileo and QZSS, will be available too, 
which will further improve the positioning performance of 
the satellite-based real-time PPP and promote the applica-
tion of real-time PPP in more fields.
Acknowledgements  This work is supported by the National 
Key Research and Development Program of China (Grant 
2021YFC3000501), the National Natural Science Foundation of China 
(Grant 42174027), the Fundamental Research Funds for the Central 
Universities (Grant 2042022kf1198), and the Young Elite Scientist 
Sponsorship Program by CAST(YESS20200110).
Author contributions  Conceptualization: Peida Wu, Yidong Lou, 
Weixing Zhang; Formal analysis and investigation: Peida Wu; Writ-
ing - original draft preparation: Peida Wu; Writing - review and edit-
ing: Yidong Lou, Weixing Zhang, Jan Dousa; Funding acquisition: 
Yidong Lou, Weixing Zhang; Resources: Yidong Lou, Weixing Zhang, 
Huizhong He, Junbing Chai, Yongzhong Ouyang, Zhenyi Zhang, Xu 
Zou; Supervision: Yidong Lou, Weixing Zhang.
Data availability  The GNSS data of MGEX station were obtained from 
https://​cddis.​nasa.​gov/​archi​ve/​gnss/​data/​daily/, and the GBM products 
were accessed from https://​datas​ervic​es.​gfz-​potsd​am.​de. The GNSS 
results that support the findings are available at https://​github.​com/​
YoYog​urt/​B2b_​evalu​ation_​paper. The GNSS dataset of the car and 
offshore ship is available upon request.
Declarations 
Competing interests  The authors declare no competing interests.
References
Booth JS, Snow RN (2009) An evaluation of OmniStar XP and PPP 
as a replacement for DGPS in airborne applications. Proceedings 
of ION GNSS 2009, Institute of Navigation, Savannah, Georgia, 
USA, September 22–25, 1188–1194.
Cabinet Office, Government of Japan, 2022. Trial service of 
MADOCA-PPP has now started [EB/OL]. https://​qzss.​go.​jp/​en/​
overv​iew/​notic​es/​madoca_​220930.​html
CSNO (2020a). BeiDou Navigation Satellite System Signal in Space 
Interface Control Document Precise Point Positioning Service 
Signal PPP-B2b (Version 1.0). China Satellite Navigation Office. 
http://​www.​beidou.​gov.​cn/​xt/​gfxz/​2020a​08/​P0202​0a080​33620​
62482​940.​pdf
CSNO (2020b). BeiDou Navigation Satellite System Open Service 
Performance Standard (Version 3.0). China Satellite Navigation 
Office. http://​www.​beidou.​gov.​cn/​xt/​gfxz/​202105/​P0202​10526​
21623​11362​38.​pdf
Dai L, Chen Y, Lie A, Zeitzew M, Zhang Y (2016) StarFire SF3: 
worldwide centimeter-accurate real time GNSS positioning. Pro-
ceedings of ION GNSS 2016, Institute of Navigation, Portland, 
Oregon, USA, September 12–16, 3295–3320.
Deng Z, Nischan T, Bradke M (2017) Multi-GNSS Rapid Orbit-, 
Clock- and EOP-Product Series. GFZ Data Services. https://​doi.​
org/​10.​5880/​GFZ.1.​1.​2017.​002
Elsobeiey M, Al-Harbi S (2016) Performance of real-time precise 
point positioning using IGS real-time service. GPS Solutions 
20(3):565–571. https://​doi.​org/​10.​1007/​s10291-​015-​0467-z
European GNSS Service Centre (2023). Galileo high accuracy ser-
vice service definition document (HAS SDD) (Issue 1.0) https://​
www.​gsc-​europa.​eu/​sites/​defau​lt/​files/​sites/​all/​files/​Galil​eo-​
HAS-​SDD_​v1.0.​pdf
Fang R, Lv H, Hu Z, Wang G, Zheng J, Zhou R, Xiao K, Li M, Liu J 
(2022) GPS/BDS precise point positioning with B2b products 
for high-rate seismogeodesy: application to the 2021 M-w 7.4 
Maduo earthquake. Geophys J Int 231(3):2079–2090. https://​
doi.​org/​10.​1093/​gji/​ggac3​11
Feess W, Cox J, Howard E, Kovach K (2013) GPS Inter-Signal Cor-
rections (ISCs) Study. Proceedings of ION GNSS 2013, Nash-
ville, Tennessee, USA, September 16–20, 951–958.
Ge Y, Cao X, Lyu D, He Z, Ye F, Xiao G, Shen F (2023) An inves-
tigation of PPP time transfer via BDS-3 PPP-B2b service. GPS 
Solut 27(2):61. https://​doi.​org/​10.​1007/​s10291-​023-​01402-y
Geng T, Li Z, Xie X, Liu W, Li Y, Zhao Q (2022) Real-time ocean 
precise point positioning with BDS-3 service signal PPP-B2b. 
Measurement 203:111911. https://​doi.​org/​10.​1016/j.​measu​
rement.​2022.​111911
Grayson B, Penna NT, Mills JP, Grant DS (2018) GPS precise point 
positioning for UAV photogrammetry. Photogrammetric Record 
33(164):427–447. https://​doi.​org/​10.​1111/​phor.​12259
Hadas T, Bosy J (2015) IGS RTS precise orbits and clocks verifica-
tion and quality degradation over time. GPS Solut 19(1):93–
105. https://​doi.​org/​10.​1007/​s10291-​014-​0369-5
Hadas T, Teferle FN, Kazmierski K, Hordyniec P, Bosy J (2017) 
Optimum stochastic modeling for GNSS tropospheric delay 
estimation in real-time. GPS Solut 21(3):1069–1081. https://​
doi.​org/​10.​1007/​s10291-​016-​0595-0
Hakansson M, Jensen ABO, Horemuz M, Hedling G (2017) 
Review of code and phase biases in multi-GNSS position-
ing. GPS Solusitons 21(3):849–860. https://​doi.​org/​10.​1007/​
s10291-​016-​0572-7
Jin S, Su K (2020) PPP models and performances from single- to quad-
frequency BDS observations. Satellite Navigation. https://​doi.​org/​
10.​1186/​s43020-​020-​00014-y
Kouba J, Héroux P (2001) Precise point positioning using IGS Orbit 
and clock products. GPS Solut 5(2):12–28. https://​doi.​org/​10.​
1007/​PL000​12883
Landskron D, Bohm J (2018) VMF3/GPT3: refined discrete and empir-
ical troposphere mapping functions. J Geodesy 92(4):349–360. 
https://​doi.​org/​10.​1007/​s00190-​017-​1066-2
Leandro R, et al. 2011 RTX Positioning: The Next Generation of cm-
accurate Real-time GNSS Positioning. Proceedings of ION GNSS 
2011, Portland, Oregon, USA, September 20–23, 1460–1475.
Li B, Ge H, Bu Y, Zheng Y, Yuan L (2022) Comprehensive assessment 
of real-time precise products from IGS analysis centers. Satellite 
Navigation. https://​doi.​org/​10.​1186/​s43020-​022-​00074-2
Liu Y, Yang C, Zhang M (2022) Comprehensive analyses of PPP-B2b 
performance in china and surrounding areas. Remote Sens. https://​
doi.​org/​10.​3390/​rs140​30643
Lou Y, Dai X, Gong X, Li C, Qing Y, Liu Y, Peng Y, Gu S (2022) 
A review of real-time multi-GNSS precise orbit determination 
based on the filter method. Satell Navig. https://​doi.​org/​10.​1186/​
s43020-​022-​00075-1
Malys S, Jensen PA (1990) Geodetic point positioning with GPS car-
rier beat phase data from the CASA UNO experiment. Geophys 
Res Lett 17(5):651–654. https://​doi.​org/​10.​1029/​gl017​i005p​00651
Montenbruck O, Steigenberger P, Hauschild A (2015) Broadcast ver-
sus precise ephemerides: a multi-GNSS perspective. GPS Solut 
19(2):321–333. https://​doi.​org/​10.​1007/​s10291-​014-​0390-8
Ocalan T, Turk T, Tunalioglu N, Gurturk M (2022) Investigation of 
accuracy of PPP and PPP-AR methods for direct georeferencing 
in UAV photogrammetry. Earth Sci Inf 15(4):2231–2238. https://​
doi.​org/​10.​1007/​s12145-​022-​00868-7
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 13 -->

GPS Solutions (2023) 27:192	
1 3
Page 13 of 14 
192
Petit G, Luzum B, 2010. IERS Conventions (2010). Frankfurt am Main: 
Verlag des Bundesamts für Kartographie und Geodäsie, 2010. 179 
pp, ISBN 3–89888–989–6
Ren Z, Gong H, Peng J, Tang C, Huang X, Sun G (2021) Performance 
assessment of real-time precise point positioning using BDS PPP-
B2b service signal. Adv Space Res 68(8):3242–3254. https://​doi.​
org/​10.​1016/j.​asr.​2021.​06.​006
Saastamoinen J (1972) Atmospheric correction for the troposphere and 
stratosphere in radio ranging satellites. The Use of Artificial Satel-
lites for Geodesy. https://​doi.​org/​10.​1029/​GM015​p0247
Schmid R, Dach R, Collilieux X, Jäggi A, Schmitz M, Dilssner F 
(2016) Absolute IGS antenna phase center model igs08.atx: status 
and potential improvements. J Geodesy 90(4):343–364. https://​
doi.​org/​10.​1007/​s00190-​015-​0876-3
Shi J, Yuan X, Cai Y, Wang G (2017) GPS real-time precise point 
positioning for aerial triangulation. GPS Solut 21(2):405–414. 
https://​doi.​org/​10.​1007/​s10291-​016-​0532-2
Shi J, Huang Y, Ouyang C, Lu X, Xu C (2020) BeiDou/GPS rela-
tive kinematic positioning in challenging environments includ-
ing poor satellite visibility and high receiver velocity. Surv Rev 
52(371):172–182. https://​doi.​org/​10.​1080/​00396​265.​2018.​15372​
27
Steigenberger P, Montenbruck O, Hessels U (2015) Performance 
evaluation of the early CNAV navigation message. Navigation-J 
Institute of Navigation 62(3):219–228. https://​doi.​org/​10.​1002/​
navi.​111
Tao J, Liu J, Hu Z, Zhao Q, Chen G, Ju B (2021) Initial Assessment 
of the BDS-3 PPP-B2b RTS compared with the CNES RTS. GPS 
Solut. https://​doi.​org/​10.​1007/​s10291-​021-​01168-1
Wang N, Yuan Y, Li Z, Montenbruck O, Tan B (2016) Determination 
of differential code biases with multi-GNSS observations. J Geod-
esy 90(3):209–228. https://​doi.​org/​10.​1007/​s00190-​015-​0867-4
Xu X, Nie Z, Wang Z, Wang B, Du Q (2022) Performance assessment 
of BDS-3 PPP-B2b/INS loosely coupled integration. Remote Sens 
14(13):2957. https://​doi.​org/​10.​3390/​rs141​32957
Xu Y, Yang Y, Li J (2021) Performance evaluation of BDS-3 PPP-B2b 
precise point positioning service. GPS Solut. https://​doi.​org/​10.​
1007/​s10291-​021-​01175-2
Yang Y, Mao Y, Sun B (2020) Basic performance and future devel-
opments of BeiDou global navigation satellite system. Satellite 
Navigation. https://​doi.​org/​10.​1186/​s43020-​019-​0006-0
Zhang W, Lou Y, Song W, Sun W, Zou X, Gong X (2022) Initial assess-
ment of BDS-3 precise point positioning service on GEO B2b 
signal. Adv Space Res 69(1):690–700. https://​doi.​org/​10.​1016/j.​
asr.​2021.​09.​006
Zumberge J, Heflin M, Jefferson D, Watkins M, Webb F (1997) Precise 
point positioning for the efficient and robust analysis of GPS data 
from large networks. J Geophys Res-Solid Earth 102(B3):5005–
5017. https://​doi.​org/​10.​1029/​96JB0​3860
Zuo X, Jiang X, Li P, Wang J, Ge M, Schuh H (2021) A square 
root information filter for multi-GNSS real-time precise clock 
estimation. Satellite Navigation. https://​doi.​org/​10.​1186/​
s43020-​021-​00060-0
Publisher's Note  Springer Nature remains neutral with regard to 
jurisdictional claims in published maps and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds 
exclusive rights to this article under a publishing agreement with the 
author(s) or other rightsholder(s); author self-archiving of the accepted 
manuscript version of this article is solely governed by the terms of 
such publishing agreement and applicable law.
Peida Wu   received his Master’s 
degree from Central South Uni-
versity in 2018 and is now a doc-
toral candidate at GNSS 
Research Center, Wuhan Univer-
sity. His current research mainly 
focuses on GNSS data process-
ing and tropospheric model 
refinement in complex 
environments.
Yidong Lou   received his Ph.D. 
in Geodesy and Surveying Engi-
neering from Wuhan University 
in 2008 and is currently a profes-
sor at GNSS Research Center, 
Wuhan University. His current 
research interests are in real-time 
precise GNSS orbit determina-
tion and real-time GNSS PPP.
Weixing Zhang   received his 
Ph.D. in Geodesy and Surveying 
Engineering from Wuhan Uni-
versity in 2016 and is currently 
an associate professor at GNSS 
Research Center, Wuhan Univer-
sity. His research interests 
include GNSS data processing 
and GNSS meteorology.
Jan Dousa   received his M.Sc. 
and Ph.D. in geodesy from the 
Czech Technical University in 
Prague in 1995 and 1999, 
respectively. Since 1996, he has 
worked at Geodetic Observatory 
Pecny for developing high accu-
racy GNSS applications, includ-
ing the determination of precise 
orbits, modeling and monitoring 
troposphere, the realization of 
the reference frame and others. 
He is a founder and developer of 
the G-Nut software library and 
end-user applications.
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [4 Figure(s)]

<!-- PAGE: 14 -->

GPS Solutions (2023) 27:192
1 3
192 
Page 14 of 14
Huizhong He   is currently a sen-
ior engineer. He has been long 
engaged in research and applica-
tion of marine surveying and 
m a r i n e  
g e o p h y s i c a l 
engineering.
Junbing Chai   received his Mas-
ter’s degree from the China Uni-
versity of Petroleum in 2016. He 
is currently a senior engineer 
primarily engaged in the 
research, development, and 
application of precision position-
ing software for GNSS.
Yongzhong Ouyang   received his 
Ph.D. degree from Wuhan Uni-
versity in 2013. He has 
researched and applied marine 
gravity field determination theo-
retical methods.
Zhenyi Zhang   received the Mas-
ter’s degree in geodesy and sur-
vey engineering from Wuhan 
University, Wuhan, China, in 
2023, and would join ETH 
Zurich as a Ph.D. student in 
October 2023. His research 
interests include GNSS data pro-
cessing algorithms and applica-
tions, GNSS meteorology, 
numerical weather modeling, 
and machine learning.
Xu Zou   received his B.S. degree 
from Jianghan University in 
2016 and is currently working in 
GNSS data processing at the 
GNSS Research Center, Wuhan 
University.
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

> [5 Figure(s)]

<!-- PAGE: 15 -->

1.
2.
3.
4.
5.
6.
Terms and Conditions
 
Springer Nature journal content, brought to you courtesy of Springer Nature Customer Service Center GmbH (“Springer Nature”).
 
Springer Nature supports a reasonable amount of sharing of  research papers by authors, subscribers and authorised users (“Users”), for small-
scale personal, non-commercial use provided that all copyright, trade and service marks and other proprietary notices are maintained. By
accessing, sharing, receiving or otherwise using the Springer Nature journal content you agree to these terms of use (“Terms”). For these
purposes, Springer Nature considers academic use (by researchers and students) to be non-commercial.
 
These Terms are supplementary and will apply in addition to any applicable website terms and conditions, a relevant site licence or a personal
subscription. These Terms will prevail over any conflict or ambiguity with regards to the relevant terms, a site licence or a personal subscription
(to the extent of the conflict or ambiguity only). For Creative Commons-licensed articles, the terms of the Creative Commons license used will
apply.
 
We collect and use personal data to provide access to the Springer Nature journal content. We may also use these personal data internally within
ResearchGate and Springer Nature and as agreed share it, in an anonymised way, for purposes of tracking, analysis and reporting. We will not
otherwise disclose your personal data outside the ResearchGate or the Springer Nature group of companies unless we have your permission as
detailed in the Privacy Policy.
 
While Users may use the Springer Nature journal content for small scale, personal non-commercial use, it is important to note that Users may
not:
  
use such content for the purpose of providing other users with access on a regular or large scale basis or as a means to circumvent access
control;
use such content where to do so would be considered a criminal or statutory offence in any jurisdiction, or gives rise to civil liability, or is
otherwise unlawful;
falsely or misleadingly imply or suggest endorsement, approval , sponsorship, or association unless explicitly agreed to by Springer Nature in
writing;
use bots or other automated methods to access the content or redirect messages
override any security feature or exclusionary protocol; or
share the content in order to create substitute for Springer Nature products or services or a systematic database of Springer Nature journal
content.
 
In line with the restriction against commercial use, Springer Nature does not permit the creation of a product or service that creates revenue,
royalties, rent or income from our content or its inclusion as part of a paid for service or for other commercial gain. Springer Nature journal
content cannot be used for inter-library loans and librarians may not upload Springer Nature journal content on a large scale into their, or any
other, institutional repository.
 
These terms of use are reviewed regularly and may be amended at any time. Springer Nature is not obligated to publish any information or
content on this website and may remove it or features or functionality at our sole discretion, at any time with or without notice. Springer Nature
may revoke this licence to you at any time and remove access to any copies of the Springer Nature journal content which have been saved.
 
To the fullest extent permitted by law, Springer Nature makes no warranties, representations or guarantees to Users, either express or implied
with respect to the Springer nature journal content and all parties disclaim and waive any implied warranties or warranties imposed by law,
including merchantability or fitness for any particular purpose.
 
Please note that these rights do not automatically extend to content, data or other material published by Springer Nature that may be licensed
from third parties.
 
If you would like to use or distribute our Springer Nature journal content to a wider audience or on a regular basis or in any other manner not
expressly permitted by these Terms, please contact Springer Nature at
  
onlineservice@springernature.com
