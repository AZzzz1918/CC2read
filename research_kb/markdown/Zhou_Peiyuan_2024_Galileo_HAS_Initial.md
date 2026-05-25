<!-- PAGE: 1 -->

GPS Solutions (2024) 28:2
https://doi.org/10.1007/s10291-023-01540-3
ORIGINAL ARTICLE
Initial performance assessment of Galileo High Accuracy Service
with software‑defined receiver
Peiyuan Zhou1 · Guorui Xiao1 · Lan Du1
Received: 7 May 2023 / Accepted: 26 August 2023
© The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2023
Abstract
The European Galileo High Accuracy Service (HAS) was officially declared as initial service status on January 24, 2023,
which can provide freely and openly accessible real-time precise satellite orbit, clock and code bias products to global users
through the Galileo E6B signals. We conducted initial performance assessment of the HAS GPS and Galileo satellite orbit
and clock products collected with a commercial off-the-shelf software-defined receiver platform located in Zhengzhou,
China, from March 11 to 20, 2023. The results show that the average availability of HAS GPS and Galileo satellite orbit
and clock products is 86.9% and 91.7%, respectively. The average accuracies of HAS GPS satellite orbit products are 0.037,
0.106 and 0.057 m for the radial, along-track and cross-track directions, while those for HAS Galileo are 0.032, 0.094 and
0.065 m, respectively. Meanwhile, the average precision of HAS satellite clock products for GPS and Galileo are 0.24 and
0.18 ns, respectively. After that, Precise Point Positioning experiments are conducted with GPS and Galileo observations
from all the International GNSS Service Multi-GNSS Experiment stations (over 380 stations). It indicates that the average
static positioning accuracies with HAS GPS products are 2.80, 1.53 and 2.18 cm in the east, north and up directions, while
those for HAS Galileo products are 1.40, 1.79 and 2.31 cm, respectively. On the other hand, the average kinematic position-
ing accuracies with HAS GPS products are 7.94, 5.55 and 13.39 cm in the east, north and up directions, while those for
HAS Galileo products are 8.08, 5.28 and 12.43 cm, respectively. It is therefore concluded that the HAS products can support
decimeter-level positioning accuracy in both static and kinematic modes, which will support various emerging real-time
precise positioning applications on a global scale.
Keywords Global Navigation Satellite System (GNSS) · Galileo High Accuracy Service (HAS) · Precise Point Positioning
(PPP) · Software-defined receiver (SDR)
Introduction
decimeter-level precise positioning solutions globally with
a single GNSS receiver (Malys and Jensen 1990; Zumberge
Thanks to the availability of real-time state-space represen- et al. 1997). In addition to those third-party GNSS augmen-
tation (SSR) corrections, including real-time precise satellite tation services, some newly developed GNSS systems are
orbits, clocks and code biases provided by various GNSS also able to disseminate real-time augmentation services via
augmentation services such as the Internet-based Real-Time navigation satellite signals, such as the Centimeter-Level
Service (RTS) of the International GNSS Service (IGS) Augmentation Service (CLAS) of the Quasi-Zenith Satel-
(Caissy et al. 2011; Johnston et al. 2017), as well as those lite System (QZSS) via the L6 signal (Cabinet Office 2020;
from commercial augmentation service operators such as Zhang et al. 2022) as well as the PPP-B2b augmentation
Trimble (Chen et al. 2011), real-time Precise Point Position- service of the Beidou Navigation Satellite System (BDS) via
ing (PPP) is drawing increasing interests among the GNSS Geostationary Orbit (GEO) satellites’ B2b signals (CSNO
community as an innovative and useful technology to derive 2020; Nie et al. 2021). The augmentation services provided
by the GNSS system operators are independent of Internet
* connection and are freely and openly accessible to the users,
Guorui Xiao
xgr@whu.edu.cn which will further promote the development of cost-effective
real-time PPP solutions for various emerging applications
1 Information Engineering University, Zhengzhou 450001, such as autonomous driving and precision farming.
China
Vol.:(0112 33456789)
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 2 -->

2 Page 2 of 14 GPS Solutions (2024) 28:2
On January 24, 2023, the Galileo High Accuracy Service (Montenbruck et al. 2017). Finally, conclusions and future
(HAS) was declared operational as initial service, which dis- works are summarized.
seminates real-time precise satellite orbit, clock and code bias
products via the Galileo E6B signals (European Union 2022,
Methodologies
2023). As the latest GNSS system to provide real-time PPP
augmentation service via navigation satellite signals, Galileo
HAS is aimed to support decimeter-level real-time PPP solu- In this section, we first present the collection of Galileo HAS
tions globally, although the rectangle area of latitudes − 60° corrections with a low-cost COTS software-defined receiver
to 60° and longitudes of − 125° to − 90° is currently excluded (SDR). After that, the method to recover Galileo HAS orbit
from the normal service area (European Union 2023). Before and clock products is briefly presented. Finally, the method to
the official initial service declaration (ISD), initial performance assess the quality of Galileo HAS orbit and clock products is
assessments of the experimental Galileo HAS have been con- described.
ducted with support from the Galileo control segment. Fer-
Collection of Galileo HAS corrections
nandez-Hernandez et al. (2022) analyzed the initial phase of
Galileo HAS and showed that it could provide broad cover-
age with high correction accuracy and positioning accuracy. The Galileo E6B signal with a carrier frequency of
Hauschild et al. (2022) assessed the quality of the satellite orbit 1278.75 MHz is used for the transmission of HAS correc-
and clock corrections from the early HAS test signals from tions. The Galileo e E6B (t) baseband signal component can be
September 2021 and applied them to the real-time precise sat- written as (Fernandez-Prades et al. 2011; Gioia et al. 2022):
ellite orbit determination of Sentinel-6A. Naciri et al. (2023) +∞
assessed the HAS test signals broadcasted during the summer e (t)= D [m] ⊕C [m] ⋅p t−mT
E6B ∑ HAS [ 5115 ] E6B [ 5115 ] ( c,E6B )
of 2022 and conducted a quality assessment of the experimen- m=−∞
(1)
tal Galileo HAS using data, concluding that the signal-in-space
ranging error (SISRE) of 11.8 and 10.6 cm for GPS and Gali- where D is the HAS correction data, which are modulated
leo, respectively, which can support decimeter-level real-time with the H ra A n S ging code C E6B with chip period T c,E6B = 5.1 1 15 μs
PPP at the user. Fernandez-Hernandez et al. (2023) further .
introduced the infrastructure and initial performance of the In order to collect the HAS correction data transmitted by
Galileo HAS. Angrisano et al. (2023) also show that HAS the Galileo E6B signals, we developed a flexible and low-cost
could contribute to the performance improvement of single software-defined receiver (SDR) platform, where the COTS
point positioning at the user. It is noted, however, most of the Universal Software Radio Peripheral (USRP) B210 device is
current work on HAS performance assessment is conducted used as the frontend and the open-source GNSS-SDR (ver-
with experimental services and customized receivers, while sion 0.0.17, Fernandez-Prades et al. 2011) is used for Gali-
HAS performance after the ISD is still to be assessed with leo E6B signal acquisition, tracking and telemetry decoding
commercial off-the-shelf (COTS) devices which are available (Fig. 1). The GNSS-SDR is running in real time in a desktop
to the general public. computer with Intel 12900 k processor and 64 GB random
We aim to evaluate the initial performance of Galileo access memory (RAM). The decoded HAS correction data,
HAS after ISD from the user’s perspective. Considering that including the satellite orbit, clock and code bias corrections,
no COTS GNSS receivers can receive and decode the HAS are output to files for the recovery of HAS GPS and Galileo
corrections disseminated by the Galileo E6B signals, we first satellite orbit and clock products, which will be introduced in
developed a low-cost COTS software-defined receiver (SDR) the next section.
to receive and decode Galileo HAS corrections in Zhengzhou,
Recovery of Galileo HAS orbit and clock products
China. The received HAS corrections are then compared with
IGS post-processed products for quality assessment. The fol-
lowing introduces the data collection and processing strategies The HAS satellite orbit corrections δRs are given in the Satel-
via the developed low-cost COTS SDR. Then, the method- lite Coordinate System (SCS) composed of the radial, along-
ologies for quality assessment of the HAS products are intro- track and cross-track components and centered in the satellite’s
duced. Thereafter, 10-day-long Galileo HAS products, from ionospheric-free antenna phase center (APC), which can be
March 11 to 20, 2023, are collected and assessed with respect transformed to the earth-fixed–earth-centered (ECEF) frame
to precise products from German Research Center for Geo- by (European Union 2022, 2023):
sciences (GFZ). After that, the PPP performance is extensively 𝛿Xs =RECEF𝛿Rs
assessed with GPS and Galileo observations from all the IGS RAC (2)
Multi-GNSS Experiment (MGEX) stations (over 380 stations)
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 3 -->

GPS Solutions (2024) 28:2 Page 3 of 14 2
Fig. 1 HAS correction data col- GNSS Antenna
lection with a software-defined
HAS Orbit
receiver (SDR)
Correc(cid:31)ons
HAS Clock
Bias-Tee USRP B210
Correc(cid:31)ons
GNSS-SDR
HAS Code Bias
where RE R C A E C F is the transformation matrix and can be Geosciences (GFZ) as the references for quality assessment
obtained as: (Männel et al. 2020). Since the recovered HAS and GFZ sat-
ellite orbit products refer to the antenna phase center (APC)
RE R C A E C F = [ x x ̇ ̇ s s × x x s s × × x x ̇ ̇ s s x x ̇ ̇ s s x xs s × × x x ̇ ̇ s s ] (3) and center of mass (CoM), respectively, the phase center
offsets (PCO) should be applied to convert the HAS satellite
| | | | | | | |
where the satellite position xs and velocity ẋs are computed orbit products from the APC to the CoM. Then, the HAS
using the broadcast navigation message as per its corre- satellite orbit errors can be obtained as (Zhou et al. 2019;
sponding GNSS Interface Control Document (ICD). Nie et al. 2022):
The obtained satellite orbit corrections in the ECEF frame Δxs = xs +A×d −xs
(δXs) are then added to the broadcast satellite position xs , and ( HAS PCO ) GFZ (7)
xs
the recovered precise satellite orbit HAS in the Galileo Ter- where xs GFZ are the satellite positions from the GFZ satellite
restrial Reference Frame (GTRF) frame can be derived as: orbit products. A is the satellite attitude matrix and d are
PCO
xs =xs+𝛿Xs the PCO corrections obtained from IGS antenna file (Schmid
HAS (4)
2017). The obtained satellite orbit errors can be further con-
RECEF
Similarly, the HAS clock corrections δCs should be added verted to the SCS frame by using the transpose of RAC.
to the ionospheric-free satellite clock dts computed from the Meanwhile, the recovered HAS clock products are com-
broadcast navigation message. The recovered HAS satellite pared with GFZ precise clocks for quality assessment. The
clock dt H s AS can be derived as (European Union 2022, 2023): HAS satellite clocks refer to the ionospheric-free combina-
tion of GPS C1C/C2P and Galileo C1C/C7Q, respectively,
𝛿Cs
dt H s AS =dts+Δt r s+ c (5) while the GFZ precise clocks refer to the ionospheric-free
combination of C1W/C2W and C1C/C5Q (Männel et al.
where c is the speed of light, and the relativistic correction 2020). Currently, the observable-specific biases (OSB)
Δt r s can be computed as follows: for GPS C1C/C2P/C2L and Galileo C1C/C5Q/C7Q/C6C
are disseminated in HAS (European Union 2022, 2023).
2xs×ẋs
Δts =− Therefore, we use the P1C1.DCB products from the Center
r c2 (6)
for Orbit Determination in Europe (CODE) to transform
It is noted that the recovered precise satellite clock
dt
H
s
AS is
the HAS GPS satellite clock to C1P/C2P, while the code
biases between different codes in the same frequency, i.e.,
referred to as Galileo System Time (GST) for Galileo satel-
C1P and C1W as well as C2P and C2W, are neglected (Vil-
lites, while a possible common offset should be considered
liger et al. 2019). On the other hand, the HAS OSBs are
in the HAS GPS clock corrections.
applied to transform the HAS Galileo satellite clocks to the
ionospheric-free combination of C1C/C5Q. After that, the
Quality assessment of Galileo HAS satellite orbit
double-difference method is adopted to remove the biases
and clock products.
between the HAS and GFZ clock products, which can be
described as (Zhou et al. 2019; Nie et al. 2022):
The HAS satellite orbit and clock products are obtained
with the decoded satellite orbit and clock corrections from N dts,i −dts,i
the GNSS-SDR and the broadcast navigation messages. 𝛿dt H s,i AS,GFZ =dt H s,i AS −dt G s,i FZ − ∑i=1� HA N S GFZ� (8)
Currently, there are no operational multi-GNSS combined
precise satellite orbit and clock products available (Chen where N is the number of satellites, and 𝛿dt H s,i AS,GFZ is the
et al. 2023), and we use the post-processed precise satellite obtained double difference for satellite i and can be used as
orbit and clock products from German Research Center for the quality indicator for HAS satellite clock products.
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 4 -->

2 Page 4 of 14 GPS Solutions (2024) 28:2
Galileo HAS product quality assessment cross-track components, respectively, while the valid val-
ues of the HAS clock corrections range from − 10.2375 to
To assess the performance of the Galileo HAS products, we 10.2350 m (European Union 2022). After excluding invalid
collected HAS correction data of 10 days from March 11 to HAS orbit and clock corrections, the daily availability of
20 (DOY 70–79), 2023, in Zhengzhou, China. The sampling HAS orbit and clock corrections are calculated and plot-
frequency of the USRP B210 is set to 4 million samples per ted in Fig. 2. It is found that the daily availabilities of HAS
second (MSPS), and the HAS correction data are collected orbit and clock corrections for most of the GPS satellites are
and processed by GNSS-SDR in real time. Although located greater than 70%. The HAS corrections of GPS G22 are not
outside of the current HAS service area, we can still obtain available during the whole test period, while those of GPS
HAS data successfully in Zhengzhou, China, from 3 to 5 G28 are not available at the beginning of the period. On
Galileo satellites thanks to the redundancies brought by the the other hand, the daily availability of HAS corrections for
Reed–Solomon encoding (Fernandez-Hernandez et al. 2020; most of the Galileo satellites is greater than 80%, which is
Hirokawa et al. 2021). In the following, the quality of the better than those of GPS satellites. The HAS corrections of
HAS products will be assessed from aspects of availability Galileo E14 and E18 in highly eccentric orbits (not usable
and accuracy. satellites) are not available during the whole test period, and
the daily availabilities of HAS corrections for two Galileo
Availability of Galileo HAS orbit and clock products satellites, i.e., E13 and E30, are below 50% during some
days of the test period.
During the test period, the HAS orbit and clock correc- The availability is further assessed by recovering the sat-
tions are updated every 50 s and 10 s, and the correspond- ellite orbit and clock products at sampling intervals of 10 s
ing number of daily updates should be 1728 and 8640, from DOY 70–79, 2023, and the availability statistics are
respectively. The valid values of HAS orbit corrections plotted in Fig. 3. It is shown that the mean value of the avail-
range from − 10.2375 to 10.2375 m, − 16.376 to 16.376 m ability of the recovered HAS GPS satellite orbit and clock
and − 16.376 to 16.376 m, for the radial, along-track and products during the whole test period is 86.9% (excluding
Fig. 2 Daily availability of HAS
satellite orbit and clock correc-
tions from DOY 70––79, 2023.
The left column is for GPS
satellites, and the right column
is for Galileo satellites. Each
color represents different GPS
and Galileo satellites
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 5 -->

GPS Solutions (2024) 28:2 Page 5 of 14 2
Fig. 3 Availability of the
recovered HAS satellite orbit
and clock products from DOY
70–79, 2023
GPS G22), while that of the recovered HAS Galileo satel- along-track direction, which should be further investigated
lite orbit and clock products is 91.7% (excluding Galileo in future work. Meanwhile, the HAS orbit errors for most
E14 and E18 in highly eccentric orbits). The availability of of the Galileo satellites are within 0.5 m, except for the
HAS Galileo satellite orbit and clock products is higher than Galileo E01 in the along-track direction. Nevertheless, the
those of GPS satellites, which also reveals that the developed HAS Galileo orbit errors in the radial directions are within
COTS SDR can receive and decode the HAS correction data. 0.2 m.
The HAS satellite orbit root-mean-square errors (RMS)
Quality assessment of Galileo HAS orbit and clock
for each satellite in the radial, along-track and cross-track
products
directions for DOY 70, 2023, are shown in Fig. 6. It is
shown that the orbit accuracy in the radial direction is the
In this section, the quality of the recovered HAS satel- best while the orbit accuracy in the along-track direction is
lite orbit and clock products is assessed with respect to the poorest among the three directions. The average RMSs
the GFZ precise satellite orbits with sampling intervals of all the available GPS satellites for DOY 70, 2023, are
of 300 s and precise satellite clocks with sampling inter- 0.033, 0.091 and 0.050 m for the radial, along-track and
vals of 30 s. The obtained HAS satellite orbit errors for cross-track directions, respectively, while those for all the
DOY 70, 2023, are used as examples and are shown in available Galileo satellites are 0.032, 0.082 and 0.059 m,
Figs. 4 and 5 for GPS and Galileo, respectively. It is seen respectively.
clearly that the HAS satellite orbit errors are centered The HAS satellite orbit accuracy statistics during the
toward zero. The HAS GPS orbit errors are within 0.5 m, whole test period are listed in Table 1, and those of the
and orbit errors in the radial directions are within 0.2 m. broadcast satellite orbit products are also provided in
There are outliers in the GPS satellite orbit errors of the Table 2 for comparison. It shows that the daily RMSs
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 6 -->

2 Page 6 of 14 GPS Solutions (2024) 28:2
Fig. 4 HAS GPS satellite orbit errors at DOY 70, 2023. Each color Fig. 5 HAS Galileo satellite orbit errors at DOY 70, 2023. Each color
represents different GPS satellites represents different Galileo satellites
of HAS satellite orbit products are stable during the test The quality of the HAS satellite clock products is also
period, and the average RMSs for HAS GPS satellite orbit assessed using GFZ precise clock products as the reference.
products during the whole test period are 0.037, 0.106 and As examples, the double-difference HAS satellite clock
0.057 m, for the radial, along-track and cross-track direc- errors for DOY 70, 2023, are computed according to (8)
tions, respectively, while average RMSs for HAS Gali- and shown in Fig. 7. As can be seen, the HAS GPS satellite
leo satellite orbit products are 0.032, 0.094 and 0.065 m, clock differences vary from − 3 to 3 ns, while those for the
respectively. The accuracy of the radial direction is the HAS Galileo satellites vary from − 2 to 2 ns. Moreover, it
best among the three directions, and the accuracy of the is seen clearly that the HAS GPS satellite clock differences
along-track direction is the poorest. Since the accuracy are more scattered than those of the HAS Galileo satellites.
of the radial direction for both GPS and Galileo are well There are biases that exist in the HAS GPS satellite clock
below 5 cm, it is therefore concluded that the HAS satellite differences, which, however, will be absorbed by the receiver
orbit products can support decimeter-level PPP applica- clock and phase ambiguities and, therefore, will not affect
tions. On the other hand, the average RMSs for broadcast real-time PPP performance. The standard deviation (STD) of
GPS satellite orbit products are 0.345, 0.968 and 0.426 m the HAS satellite clock differences with respect to the GFZ
for the radial, along-track and cross-track directions, precise clock products is further computed as the indicator
respectively. The quality of the Galileo broadcast satellite of clock precision and plotted in Fig. 8. The daily average
orbit products is better than those of GPS, with average of STDs for the HAS GPS and Galileo satellite are 0.22 and
RMSs of 0.115, 0.266 and 0.156 m, respectively, for the 0.15 ns, respectively, which implies that the precision of
radial, along-track and cross-track directions. It is shown the HAS Galileo satellite clock products is generally bet-
that applying HAS corrections to broadcast satellite orbit ter than those of the HAS GPS satellite clock products. It
products significantly improves satellite orbit quality. is further confirmed by the daily precision statistics during
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 7 -->

GPS Solutions (2024) 28:2 Page 7 of 14 2
Fig. 6 RMS of HAS satellite
orbit products at DOY 70, 2023
Table 1 Daily RMS of HAS
DOY GPS Galileo
satellite orbit products during
DOY 70–79, 2023 (unit m) Radial Along-track Cross-track Radial Along-track Cross-track
70 0.033 0.091 0.050 0.032 0.082 0.059
71 0.029 0.086 0.056 0.037 0.088 0.065
72 0.032 0.080 0.050 0.029 0.084 0.052
73 0.031 0.087 0.056 0.032 0.092 0.064
74 0.031 0.090 0.070 0.033 0.095 0.074
75 0.034 0.087 0.059 0.028 0.095 0.072
76 0.047 0.123 0.066 0.031 0.109 0.076
77 0.047 0.157 0.056 0.029 0.089 0.061
78 0.043 0.151 0.053 0.041 0.113 0.066
79 0.039 0.108 0.051 0.032 0.096 0.064
Average 0.037 0.106 0.057 0.032 0.094 0.065
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 8 -->

2 Page 8 of 14 GPS Solutions (2024) 28:2
Table 2 Daily RMS of
DOY GPS Galileo
broadcast satellite orbit products
during DOY 70–79, 2023 (unit Radial Along-track Cross-track Radial Along-track Cross-track
m)
70 0.312 1.010 0.417 0.112 0.241 0.145
71 0.311 0.992 0.421 0.116 0.245 0.140
72 0.316 0.850 0.459 0.124 0.260 0.162
73 0.295 0.866 0.433 0.112 0.262 0.149
74 0.340 0.956 0.458 0.111 0.267 0.152
75 0.343 0.902 0.433 0.115 0.248 0.141
76 0.448 1.117 0.410 0.120 0.277 0.169
77 0.372 1.066 0.379 0.111 0.260 0.159
78 0.395 1.001 0.426 0.118 0.301 0.169
79 0.317 0.918 0.426 0.112 0.301 0.171
Average 0.345 0.968 0.426 0.115 0.266 0.156
the whole test period, as given in Table 3, which shows that for GNSS positioning software. Note that it is different from
the average HAS GPS and Galileo satellite clock precisions the 5 degrees defined in the Galileo official service definition
are 0.24 and 0.18 ns, respectively. Meanwhile, the average document (European Union 2023). It can be seen that the
broadcast GPS and Galileo satellite clock precision are 0.69 number of observable GPS satellites is significantly larger
and 0.45 ns, respectively. The results indicate that the HAS than that of Galileo. Although the number of observable
satellite clock corrections can correct errors in the broadcast Galileo satellites in most regions is larger than 4, it is found
satellite clocks and support high-precision real-time PPP.
PPP performance assessment
This section assesses the PPP performance of HAS products
with all the GPS and Galileo observation data collected by
the IGS Multi-GNSS Experiment (MGEX) network from
March 11 to 20 (DOY 70–79), 2023. First, the data and pro-
cessing strategies are presented. After that, the static and
kinematic PPP performance are assessed from aspects of
convergence performance and positioning accuracy.
Data and processing strategies
The IGS established the Multi-GNSS Experiment (MGEX)
in order to prepare operational services for new and upcom-
ing GNSS, such as the European Galileo, Chinese BeiDou,
and regional systems, such as Japanese QZSS and Indian
NAVIC system (Montenbruck et al. 2017). The MGEX
stations, equipped with multiple brands of professional
receivers, provide almost full and continuous tracking of
GPS/Galileo signals. Therefore, all the data collected by
the MGEX network from March 11 to 20 (DOY 70–79),
2023, are processed. Figure 9 shows the global distribution
of the number of observable GPS and Galileo satellites with
a cutoff elevation of 10 degrees. The cutoff angle is chosen
to avoid the large noise of satellite observations with low
elevation for PPP processing, a common processing strategy
Fig. 7 HAS satellite clock differences with respect to the GFZ precise
clock products for each satellite at DOY 70, 2023. Each color repre-
sents different GPS and Galileo satellites
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 9 -->

GPS Solutions (2024) 28:2 Page 9 of 14 2
Fig. 8 STD of HAS satellite
clock differences for each satel-
lite at DOY 70, 2023
Table 3 Daily precision of HAS and broadcast satellite clock prod- In the PPP processing, E1/E5a (C1C/C5Q) are used for
ucts during DOY 70–79, 2023 (unit ns) Galileo, while L1/L2 (C1W/C2W) are used for GPS. These
DOY HAS Broadcast signals were chosen according to high availability and in
accordance with the principle of orbit and clock generation
GPS Galileo GPS Galileo
(Uhlemann et al. 2020). Throughout the processing, MGEX
70 0.22 0.15 0.64 0.42 precise products, including precise satellite orbit, clock and
71 0.23 0.16 0.69 0.42 earth rotation parameters, provided by GFZ are used. The
72 0.24 0.19 0.66 0.49 satellite phase center offsets and variations are corrected
73 0.23 0.17 0.81 0.46 according to the IGS antenna file (Schmid 2017). As for
74 0.24 0.20 0.81 0.43 the receiver antenna phase center offsets and variations,
75 0.25 0.19 0.83 0.44 the correction values for GPS are employed for Galileo in
76 0.27 0.18 0.73 0.48 accordance with the principle of orbit and clock generation
77 0.28 0.16 0.60 0.48 (Prange et al. 2017). All the other errors, including the dry
78 0.25 0.19 0.55 0.48 tropospheric component, phase windup effect and ocean tide
79 0.23 0.16 0.57 0.44 loading, are corrected following the IGS conventions (Kouba
Average 0.24 0.18 0.69 0.45 2009). The dual-frequency ionospheric-free linear combina-
tion model is employed, and the observations are weighted
according to the satellite elevation with cutoff angle set to
that a stand-alone Galileo PPP solution is still not feasible in 10 degrees. The detail of our PPP strategy can be found in
a few regions due to data preprocessing and editing. Xiao et al. (2018).
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 10 -->

2 Page 10 of 14 GPS Solutions (2024) 28:2
Fig. 10 Convergence performance of GPS PPP with GFZ and HAS
products based on 360 stations under 50% confidence levels
accuracy of GPS PPP with GFZ products is 0.32, 0.15 and
0.51 cm for the east, north and up components, respectively,
while that for HAS products is 2.8, 1.53 and 2.18 cm, respec-
tively. The results indicate that the quality of HAS prod-
ucts can support centimeter-level positioning, although it is
slightly worse than GFZ products. As for the convergence,
it takes 3, 6 and 15 min for GPS PPP with GFZ products
to converge to three-dimensional 30, 20 and 10 cm accu-
Fig. 9 Distribution of the number of observable GPS (up) and Gali-
racy, respectively, while that of HAS products is 15, 36 and
leo (bottom) satellites on DOY 70, 2023 with a cutoff elevation of 10
degrees. The pixel size is 0.5 degrees latitude by 0.5 degrees longi- 134 min, respectively.
tude Figure 11 shows the convergence performance of Galileo
PPP with GFZ and HAS products based on 284 stations
under 50% confidence levels on DOY 070, 2023. Due to the
Static PPP processing fewer observable satellites for Galileo, it is found that the
number of successful solutions of Galileo PPP is signifi-
In the static PPP processing, all the MGEX stations (over cantly smaller than that of GPS. Table 5 further presents the
380 stations) are processed in static mode with the products statistics for all 10 days. The average accuracy of Galileo
from GFZ and HAS. Considering that the HAS product pro- PPP with GFZ products is 0.48, 0.25 and 0.71 cm for the
vides corrections for two constellations, Galileo and GPS east, north and up components, respectively, while that for
PPP are separately processed. After the processing, data HAS products is 1.4, 1.79 and 2.31 cm, respectively. When
edits are performed for comparison. First, the integrity of compared with GPS PPP with GFZ products in Table 3, it is
PPP solution should be guaranteed, which indicates that the found that the accuracy of Galileo PPP with GFZ products
epoch number of PPP solution should be larger than 2870 is slightly worse, which is reasonable considering the fewer
for 30 s sample of 24-h data (2880 in theory). Then, the two observable satellites of Galileo. However, the Galileo PPP
solutions using GFZ and HAS products are synchronized, with HAS products are significantly better than that of GPS
which means PPP solutions should exist from both products. PPP with HAS products. This further confirmed that the
Finally, the PPP solutions for all the remaining stations are quality of HAS products for the Galileo constellation is bet-
compared with truth values and east–north–up errors are cal- ter than that of GPS constellation. Although the accuracy of
culated. Note that convergence time and positional accuracy Galileo PPP with HAS products is already very accurate, it
performance is evaluated under different confidence levels is found that the accuracy of the north component is obvi-
for reliability (Lou et al. 2016). ously worse than that of the east component, which is unu-
Figure 10 shows the convergence performance of GPS sual and may be improved by the PPP ambiguity resolution
PPP with GFZ and HAS products based on 360 stations feature in the future. As for the convergence, it takes 4, 7 and
under 50% confidence levels on DOY 070, 2023. Table 4 17 min for Galileo PPP with GFZ products to converge to
further presents the statistics for all 10 days. The average three-dimensional 30, 20 and 10 cm accuracy, respectively,
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 11 -->

GPS Solutions (2024) 28:2 Page 11 of 14 2
Table 4 Daily accuracy of
DOY GFZ HAS
GPS PPP with GFZ and HAS
products during DOY 70–79, East North Up East North Up
2023 (unit cm)
70 0.33 0.12 0.48 3.12 1.70 2.15
71 0.34 0.17 0.63 3.79 1.06 2.71
72 0.40 0.14 0.65 3.02 2.09 2.85
73 0.26 0.12 0.54 2.40 1.46 2.17
74 0.33 0.23 0.56 4.28 1.52 1.97
75 0.42 0.13 0.55 3.19 1.45 1.86
76 0.27 0.13 0.45 2.99 1.79 1.92
77 0.17 0.14 0.41 1.41 1.37 2.49
78 0.45 0.15 0.56 2.13 1.10 1.41
79 0.21 0.14 0.29 1.64 1.75 2.24
Average 0.32 0.15 0.51 2.80 1.53 2.18
Fig. 11 Convergence performance of Galileo PPP with GFZ and Fig. 12 Convergence performance of GPS kinematic PPP with GFZ
HAS products based on 284 stations under 50% confidence levels and HAS products based on 368 stations under 50% confidence levels
Table 5 Daily accuracy of
DOY GFZ HAS
Galileo PPP with GFZ and HAS
products during DOY 70–79, East North Up East North Up
2023 (unit cm)
70 0.35 0.16 0.62 1.05 2.48 1.33
71 0.87 0.41 1.09 1.03 1.68 2.88
72 0.52 0.20 0.70 1.28 2.01 2.50
73 0.28 0.20 0.63 1.38 1.52 2.91
74 0.48 0.39 0.61 2.25 1.78 3.17
75 0.74 0.22 0.74 1.21 1.48 1.72
76 0.39 0.23 0.79 0.77 2.21 1.55
77 0.32 0.26 0.55 1.05 1.28 2.19
78 0.53 0.17 0.77 1.71 1.33 2.42
79 0.34 0.27 0.63 2.27 2.08 2.41
Average 0.48 0.25 0.71 1.40 1.79 2.31
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 12 -->

2 Page 12 of 14 GPS Solutions (2024) 28:2
while that of HAS products is 16, 25 and 148 min, respec- 2.54 cm for the east, north and up components, respectively,
tively. The overall convergence time is slightly longer than while that for HAS products is 7.94, 5.55 and 13.39 cm,
that of GPS PPP due to the fewer observable satellites of respectively. Although the worse quality of HAS products
Galileo. may result in low accuracy, we also found that the missing
values in HAS products significantly influence kinematic
Kinematic PPP processing
PPP performance. Since the extend Kalman filtering is used
to process the PPP, the missing values in HAS products will
The data from the previous subsection are processed in kin- result in frequent re-initializations of ambiguity parameters
ematic PPP mode to further assess the kinematic PPP per- and degradation of PPP performance. Nevertheless, deci-
formance. The data edit strategy, conversion and statistics meter-level positioning accuracy is achievable from HAS
are the same as in the static PPP analysis. Figures 12 and 13 products.
present the convergence performance of GPS and Galileo Figure 13 and Table 7 show that the average accuracy of
kinematic PPP with GFZ and HAS products, respectively. Galileo kinematic PPP with GFZ products is 2.17, 1.45 and
Tables 6 and 7 gives the statistics for all 10 days. 3.86 cm for the east, north and up components, respectively,
Figure 12 and Table 5 show that the average accuracy while that for HAS products is 8.08, 5.28 and 12.43 cm,
of GPS kinematic PPP with GFZ products is 1.27, 0.9 and respectively. As for the large fluctuation, it is likely intro-
duced by incomplete correction data. Based on the above
results, it can be concluded that GPS and Galileo PPP with
the current HAS products are able to achieve decimeter
accuracy.
Conclusions
On January 24, 2023, the Galileo High Accuracy Service
(HAS) was declared available for initial service, significantly
expanding the current GNSS augmentation service portfolio
in terms of accuracy, delivery methods and geographical
coverage. A low-cost SDR platform with COTS devices is
developed to receive and decode real-time precise satellite
orbit, clock and code bias products disseminated via the
Galileo E6B signals from March 11 to 20 (DOY 70–79),
2023, in Zhengzhou, China. The results show that the aver-
Fig. 13 Convergence performance of Galileo kinematic PPP with age value of the availability of the recovered HAS GPS sat-
GFZ and HAS products based on 289 stations under 50% confidence ellite orbit and clock products during the whole test period
levels
Table 6 Daily accuracy of GPS
DOY GFZ HAS
kinematic PPP with GFZ and
HAS products during DOY East North Up East North Up
70–79, 2023 (unit cm)
70 1.36 0.9 2.54 7.42 5.08 12.78
71 1.31 0.92 2.55 8.44 5.01 12.45
72 1.47 0.95 2.80 10.09 6.15 14.31
73 1.20 0.93 2.62 7.95 6.42 13.27
74 1.21 0.88 2.49 10.30 6.28 15.65
75 1.26 0.95 2.78 6.92 5.24 13.56
76 1.16 0.82 2.31 6.18 5.27 12.65
77 1.15 0.85 2.36 8.10 5.95 14.60
78 1.31 0.95 2.52 7.38 5.39 11.80
79 1.27 0.87 2.48 6.61 4.68 12.79
Average 1.27 0.90 2.54 7.94 5.55 13.39
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 13 -->

GPS Solutions (2024) 28:2 Page 13 of 14 2
Table 7 Daily accuracy of
DOY GFZ HAS
Galileo kinematic PPP with
GFZ and HAS products during East North Up East North Up
DOY 70–79, 2023 (unit cm)
70 1.71 1.29 3.67 7.55 5.39 11.75
71 2.67 1.67 4.40 7.16 5.12 12.09
72 2.46 1.49 4.18 9.14 5.54 13.13
73 1.73 1.34 3.48 7.21 5.57 11.88
74 2.16 1.41 3.81 11.03 6.13 15.37
75 2.62 1.36 4.29 6.76 4.48 12.48
76 1.81 1.44 3.31 9.28 6.00 13.71
77 2.12 1.54 3.60 7.97 5.09 12.81
78 2.39 1.58 3.83 6.94 4.81 9.60
79 2.04 1.39 4.06 7.79 4.67 11.45
Average 2.17 1.45 3.86 8.08 5.28 12.43
is 86.9% (excluding GPS G22), while that of the recovered to support cost-effective real-time decimeter-level PPP on
HAS Galileo satellite orbit and clock products is 91.7% a global scale with a single GNSS receiver. It should be
(excluding Galileo E14 and E18 in highly eccentric orbits). noted, however, the presented initial assessment is based
The recovered HAS products are then compared with on HAS products received by the developed COTS SDR
GFZ precise products for quality assessment. It is found platform located in Zhengzhou, China, which could be fur-
that the average RMSs for HAS GPS satellite orbit products ther validated with datasets from a reference source of HAS
during the whole test period are 0.037, 0.106 and 0.057 m, products.
for the radial, along-track and cross-track directions, respec-
Acknowledgements We gratefully acknowledge the European Union
tively, while average RMSs for HAS Galileo satellite orbit
for providing the Galileo HAS. We also thank IGS and GFZ for pro-
products are 0.032, 0.094 and 0.065 m, respectively. On the
viding the GNSS data and products. This work was supported by the
other hand, the average precision of HAS GPS and Galileo National Natural Science Foundation of China (Grant nos. 42204041,
satellite clock products is 0.24 and 0.18 ns, respectively. The 42274045 and 41904039) and the Natural Science Foundation of
Henan (Grant no. 232300421105).
quality of the HAS products for GPS and Galileo is generally
consistent and stable during the test period, which indicates Author contributions PZ and GX conceived the presented idea,
that high-quality HAS products can be received, decoded performed data collection and results analysis, and wrote the main
and recovered at the user to support real-time PPP. manuscript. LD reviewed and edited the manuscript. All authors were
involved in discussions throughout the development and contributed
The PPP performance of the HAS products is exten-
to the revision of the manuscript.
sively assessed with GPS and Galileo observations from all
stations of the current IGS MEGX network (over 380 sta- Data availability The Galileo HAS data are available from the cor-
tions). The dual-frequency ionospheric-free linear combina- responding author on reasonable requests, while the GNSS data and
products can be downloaded from IGS.
tion model is employed, and the observations are weighted
according to the satellite elevation with cutoff angle set to Declarations
10 degrees. The results indicate that PPP accuracies with
HAS products are worse than those with GFZ final prod- Competing interests The authors declare no competing interests.
ucts. The GPS stand-alone PPP accuracies in static mode is
2.80, 1.53 and 2.18 cm in the east, north and up directions,
while those for Galileo stand-alone PPP are 1.40, 1.79 and
References
2.31 cm, respectively. Moreover, the GPS stand-alone PPP
accuracies in kinematic mode are 7.94, 5.55 and 13.39 cm
Angrisano A, Ascione S, Cappello G, Gioia C, Gaglione S (2023)
in the east, north and up directions, while those for Galileo
Application of “Galileo High Accuracy Service” on single-point
stand-alone PPP are 8.08, 5.28 and 12.43 cm, respectively. positioning. Sensors 23:4223
Overall, it can be concluded that decimeter-level PPP accu- Cabinet Office (2020) Quasi-Zenith Satellite System Interface Specifi-
racy can be obtained utilizing the HAS products received cation Centimeter Level Augmentation Service (IS-QZSS-L6-003)
Caissy M, Weber G, Agrotis L, Wübbena G, Hernandez-Pajares M
from the developed COTS SDR platform. It highlights
(2011) The IGS real-time pilot project—the development of
that Galileo HAS after ISD demonstrates great potential real-time IGS correction products for Precise Point Positioning.
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 14 -->

2 Page 14 of 14 GPS Solutions (2024) 28:2
In: EGU General Assembly, Geophysics Research Abstracts 13, Naciri N, Yi D, Bisnath S, de Blas FJ, Capua R (2023) Assessment of
EGU2011-7472 Galileo High Accuracy Service (HAS) test signals and prelimi-
Chen X et al (2011) Trimble RTX, an innovative new approach for nary positioning performance. GPS Solut 27:73
network RTK. In: Proceedings of the ION GNSS 2011, Insti- Nie Z, Xu X, Wang Z, Du J (2021) Initial assessment of BDS PPP-B2b
tute of Navigation, Portland, Oregon, USA, September 20–23, service: precision of orbit and clock corrections, and PPP perfor-
2214–2219 mance. Remote Sens 13:2050
Chen C, Guo J, Geng T (2023) Zhao Q (2023) Multi-GNSS orbit com- Prange L, Orliac E, Dach R, Arnold D, Beutler G, Schaer S, Jaggi A
bination at Wuhan University: strategy and preliminary products. (2017) CODE’s five-system orbit and clock solution—the chal-
J Geodesy 97:41 lenges of multi-GNSS data analysis. J Geodesy 91:345–360
CSNO (2020) BeiDou Navigation Satellite System Signal in space Schmid R (2017) IGS antenna working group technical report. In: Vil-
interface control document Precise Point Positioning Service liger A, Dach R (eds) IGS technical report 2016. Astronomical
Signal PPP-B2b (Version 1.0) Institute, University of Bern, Bern, pp 139–144
European Union (2022) Galileo High Accuracy Service Signal-In- Villiger A, Schaer S, Dach R, Prange L, Sušnik A, Jäggi A (2019)
Space Interface Control Document (HAS SIS ICD) Issue 1.0 Determination of GNSS pseudo-absolute code biases and their
European Union (2023) Galileo High Accuracy Service Service Defini- long-term combination. J Geodesy 93(9):1487–1500
tion Document (HAS SDD) Issue 1.0 Xiao G, Sui L, Heck B, Zeng T, Tian Y (2018) Estimating satellite
Fernandez-Hernandez I, Senni T, Borio D, Vecchione G (2020) High- phase fractional cycle biases based on Kalman filter. GPS Solut
parity vertical Reed–Solomon codes for long GNSS high-accuracy 22:82
messages. NAVIGATION J Inst Navig 67(2):365–378 Zhang Y, Kubo N, Pullen S (2022) Evaluation of QZSS Centimeter
Fernandez-Hernandez I, Chamorro-Moreno A, Cancela-Diaz S, Calle- Level Augmentation System (CLAS): open-sky to urban environ-
Calle JD, Zoccarato P, Blonski D, Senni T, de Blas FJ, Hernández ments and geodetic to low-cost receivers. In: Proceedings of the
C, Simón J, Mozo A (2022) Galileo high accuracy service: initial ION GNSS+ 2022, Institute of Navigation, Denver, Colorado,
definition and performance. GPS Solutions 26(3):65 USA, September 19–23, pp 2729–2750
Fernandez-Hernandez I, Damy S, Susi M, Martini I, Winkel J, Zhou P, Yang H, Xiao G, Du L, Gao Y (2019) Estimation of GPS
Cancela-Diaz S, Chamorro-Moreno A, Calle-Calle JD, de Blas LNAV based on IGS products for real-time PPP. GPS Solut 23:27
FJ, Simón J, Blonski D, Izquierdo DI (2023) Galileo authentica- Zumberge JF, Heflin MB, Jefferson DC, Watkins MM, Webb FH
tion and high accuracy: getting to the truth. Inside GNSS (1997) Precise Point Positioning for the efficient and robust
Fernandez-Prades C, Arribas J, Closas P (2011) GNSS-SDR: an open analysis of GPS data from large networks. J Geophys Res
source tool for researchers and developers. In: Proceedings of the 102(B3):5005–5017
ION GNSS 2011, Institute of Navigation, Portland, Oregon, USA,
September 20–23, pp 780–794 Publisher's Note Springer Nature remains neutral with regard to
Gioia C, Borio D, Susi M, Fernandez-Hernandez I (2022) The Galileo jurisdictional claims in published maps and institutional affiliations.
High Accuracy Service (HAS): decoding and processing live cor-
rections for code-based positioning. In: Proceedings of the ION Springer Nature or its licensor (e.g. a society or other partner) holds
ITM 2022, Institute of Navigation, Long Beach, California, USA, exclusive rights to this article under a publishing agreement with the
January 25–27, pp 1065–1074 author(s) or other rightsholder(s); author self-archiving of the accepted
Hauschild A, Montenbruck O, Steigenberger P, Martini I, Fernandez- manuscript version of this article is solely governed by the terms of
Hernandez I (2022) Orbit determination of sentinel-6A using the such publishing agreement and applicable law.
Galileo High Accuracy Service test signal. GPS Solut 26(4):120
Hirokawa R, Fernandez-Hernandez I, Reynolds S (2021) PPP/PPP-
RTK open formats: overview, comparison, and proposal for an Peiyuan Zhou obtained his Ph.D. from the University of Calgary and
interoperable message. Navigation 68(4):759–778 is a lecturer at Information Engineering University, China. His current
Johnston G, Riddell A, Hausler G (2017) The International GNSS Ser- research focuses on GNSS precise positioning and remote sensing.
vice. Teunissen PJG, Montenbruck O (eds) Springer Handbook
of Global Navigation Satellite Systems, 1st ed. Springer, Chamm, Guorui Xiao is currently an associate professor at Information Engi-
pp 967–982 neering University, China. He received his B.Sc. degree from the
Kouba J (2009) A guide to using International GNSS Service (IGS) School of Geodesy and Geomatics at Wuhan University in 2011 and
products his Ph.D. degree from the Geodetic Institute of Karlsruhe Institute of
Lou Y, Zheng F, Gu S, Wang C, Guo H, Feng Y (2016) Multi-GNSS Technology in Germany. His current research focuses on multi-GNSS
Precise Point Positioning with raw single-frequency and dual- and multi-sensor integrated precise positioning and applications.
frequency measurement models. GPS Solut 20:849–862
Malys S, Jensen PA (1990) Geodetic point positioning with GPS carrier Lan Du is a Professor at Information Engineering University, China,
beat phase data from the CASA UNO Experiment. Geophys Res where she obtained a Ph.D. in geodesy in 2006. Her research interests
Lett 17(5):651–654 include satellite navigation, space geodesy and astrodynamics.
Männel B, Brandt A, Nischan T, Brack A, Sakic P, Bradke M (2020)
GFZ rapid product series for the IGS. GFZ Data Serv. https://d oi.
org/1 0.5 880/G FZ.1.1 .2 020.0 03
Montenbruck O et al (2017) The Multi-GNSS Experiment (MGEX) of
the International GNSS Service (IGS)—achievements, prospects
and challenges. Adv Space Res 59(7):1671–1697
1 3
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

<!-- PAGE: 15 -->

Terms and Conditions
S pringer Nature journal content, brought to you courtesy of Springer Nature Customer Service Center GmbH (“Springer Nature”).
Springer Nature supports a reasonable amount of sharing of research papers by authors, subscribers and authorised users (“Users”), for small-
scale personal, non-commercial use provided that all copyright, trade and service marks and other proprietary notices are maintained. By
accessing, sharing, receiving or otherwise using the Springer Nature journal content you agree to these terms of use (“Terms”). For these
p urposes, Springer Nature considers academic use (by researchers and students) to be non-commercial.
These Terms are supplementary and will apply in addition to any applicable website terms and conditions, a relevant site licence or a personal
subscription. These Terms will prevail over any conflict or ambiguity with regards to the relevant terms, a site licence or a personal subscription
(to the extent of the conflict or ambiguity only). For Creative Commons-licensed articles, the terms of the Creative Commons license used will
a pply.
We collect and use personal data to provide access to the Springer Nature journal content. We may also use these personal data internally within
ResearchGate and Springer Nature and as agreed share it, in an anonymised way, for purposes of tracking, analysis and reporting. We will not
otherwise disclose your personal data outside the ResearchGate or the Springer Nature group of companies unless we have your permission as
d etailed in the Privacy Policy.
While Users may use the Springer Nature journal content for small scale, personal non-commercial use, it is important to note that Users may
n ot:
1.use such content for the purpose of providing other users with access on a regular or large scale basis or as a means to circumvent access
control;
2.use such content where to do so would be considered a criminal or statutory offence in any jurisdiction, or gives rise to civil liability, or is
otherwise unlawful;
3.falsely or misleadingly imply or suggest endorsement, approval , sponsorship, or association unless explicitly agreed to by Springer Nature in
writing;
4.use bots or other automated methods to access the content or redirect messages
5.override any security feature or exclusionary protocol; or
6.share the content in order to create substitute for Springer Nature products or services or a systematic database of Springer Nature journal
content.
In line with the restriction against commercial use, Springer Nature does not permit the creation of a product or service that creates revenue,
royalties, rent or income from our content or its inclusion as part of a paid for service or for other commercial gain. Springer Nature journal
content cannot be used for inter-library loans and librarians may not upload Springer Nature journal content on a large scale into their, or any
o ther, institutional repository.
These terms of use are reviewed regularly and may be amended at any time. Springer Nature is not obligated to publish any information or
content on this website and may remove it or features or functionality at our sole discretion, at any time with or without notice. Springer Nature
m ay revoke this licence to you at any time and remove access to any copies of the Springer Nature journal content which have been saved.
To the fullest extent permitted by law, Springer Nature makes no warranties, representations or guarantees to Users, either express or implied
with respect to the Springer nature journal content and all parties disclaim and waive any implied warranties or warranties imposed by law,
i ncluding merchantability or fitness for any particular purpose.
Please note that these rights do not automatically extend to content, data or other material published by Springer Nature that may be licensed
f rom third parties.
If you would like to use or distribute our Springer Nature journal content to a wider audience or on a regular basis or in any other manner not
e xpressly permitted by these Terms, please contact Springer Nature at
onlineservice@springernature.com