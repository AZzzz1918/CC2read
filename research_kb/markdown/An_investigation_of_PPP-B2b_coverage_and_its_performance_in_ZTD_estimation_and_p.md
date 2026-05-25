<!-- PAGE: 1 -->

Survey Review
ISSN: 0039-6265 (Print) 1752-2706 (Online) Journal homepage: www.tandfonline.com/journals/ysre20
An investigation of PPP-B2b coverage and its
performance in ZTD estimation and positioning in
different regions
Xiaoming Wang, Kai Zhou, Jinglei Zhang, Haobo Li, Hong Liang, Manhong Tu,
Yufei Chen, Cong Qiu & Li Li
To cite this article: Xiaoming Wang, Kai Zhou, Jinglei Zhang, Haobo Li, Hong Liang, Manhong
Tu, Yufei Chen, Cong Qiu & Li Li (2025) An investigation of PPP-B2b coverage and its
performance in ZTD estimation and positioning in different regions, Survey Review, 57:402,
258-272, DOI: 10.1080/00396265.2024.2401665
To link to this article: https://doi.org/10.1080/00396265.2024.2401665
© 2024 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group
Published online: 10 Sep 2024.
Submit your article to this journal
Article views: 1620
View related articles
View Crossmark data
Citing articles: 7 View citing articles
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=ysre20

<!-- PAGE: 2 -->

An investigation of PPP-B2b coverage and its
performance in ZTD estimation and positioning
in different regions
Xiaoming Wang ∗a,b, Kai Zhoua, Jinglei Zhanga, Haobo Lic, Hong Liangd,
Manhong Tud, Yufei Chena,b, Cong Qiua,b and Li Lie
This study comprehensively evaluates the Beidou navigation satellite system’s PPP-B2b service
for real-time positioning and zenith total delay (ZTD) estimation. Despite its operational status,
PPP-b2b’s effective coverage is underexplored. We define this coverage by analysing satellite
visibility and geometry and evaluating ZTD and positioning accuracy at 48 stations. Results
show PPP-B2b achieves ZTD Errors of 10–20 mm in China and 15–30 mm in Europe, with
kinematic experiments in China and Japan showing consistent accuracy within 20 mm. This
study highlights PPP-b2b’s potential for enhancing atmospheric monitoring and precise
positioning in its effective regions.
Keywords:BDS-3, PPP-B2b service, GNSS, PDOP, Zenith total delay, Positioning, PPP
Introduction correction information in real-time for various appli-
cations with PPP (Hadas And Bosy, 2015, Kazmierski
Global navigation satellite systems (GNSS), which are
et al., 2020). Previous studies have shown that the accu-
designed mainly for positioning, navigation, and timing
racy of real-time tropospheric estimates using the static
services (Leick et al., 2015), have been used to remotely
PPP method with real-time satellite orbit and clock pro-
sense the Earth’s atmosphere since the 1990s. The precise
ducts can reach 1–2 mm for PWV (Li et al., 2015) and
point positioning (PPP) technique is widely used in esti- approximately 5–18 mm for ZTD (Hadas et al., 2020).
mating the zenith total delay (ZTD), which can be con- In addition to estimating tropospheric information with
verted to precipitable water vapor (PWV) using surface fixed GNSS stations using the static PPP method, various
temperature and pressure measurements at the GNSS
studies have indicated that tropospheric information can
site. However, the accuracy of ZTD derived using the
be monitored using GNSS observations on moving plat-
PPP technique is highly dependent on the quality of the
forms such as ships (Wang et al., 2019), Buoys (Chadwell
satellite orbit and clock data, as these errors are intro-
And Bock, 2001), trains (Aichinger-Rosenberger et al.,
duced into the PPP processing and are neither eliminated
2021), cars (Gratton et al., 2021), and aeroplanes
nor accounted for (Zhou et al., 2020) with the PPP ser-
(Skone et al., 2006), using the kinematic PPP method.
vice via the B2b signal (PPP-B2b) of the Beidou Satellite
However, these studies have highlighted that the major
System (BDS) and the high-accuracy service (HAS) of
issue for real-time GNSS PWV retrieval on moving plat-
Galileo becoming operational in recent years, high-accu-
forms is the limitation of Internet communication. There-
racy orbit and clock corrections are now available
fore, sensing ZTD/PWV with either static or kinematic
through these basic navigation constellations. Before
PPP using the IGS RTS service is constrained by the
the availability of PPP-B2b service provided by BDS
need for a stable Internet connection to receive clock
and the HAS from Galileo, we usually needed to use
and orbit corrections.
the real-time service (RTS) initiated by the International
Both BDS and Galileo, through their basic navigation
GNSS Service (IGS) to access GNSS orbit and clock
constellations, provide accurate satellite orbit and clock
information in real-time, enabling high-accuracy posi-
aAerospace Information Research Institute, Chinese Academy of tioning and ZTD estimation using the PPP Algorithm
Sciences, Beijing, People’s Republic of China without the need for Internet access. The Galileo aims to
bUniversity of Chinese Academy of Sciences, Beijing, People’s Republic of provide global high-accuracy positioning with errors of
China
cRoyal Melbourne Institute of Technology (RMIT) University, Melbourne, less than 20 cm (95%) and 40 m (95%) in the horizontal
Australia and vertical domains, respectively, transmitted through
dMeteorological Observation Center of China Meteorological Adminis-
an open format in the E6-B signal (Fernandez-Hernandez
tration, Beijing, People’s Republic of China
eResearch Center of Beidou Navigation and Remote Sensing, Suzhou Uni- et al., 2022, Zhou et al., 2024), the HAS was officially
versity of Science and Technology, Suzhou, People’s Republic of China declared to have reached initial service status on January
∗Corresponding author. Email: wxmgeo@gmail.com Aerospace Information 24, 2023, and previous studies have shown that HAS pro-
Research Institute, Chinese Academy of Sciences, No.9 Dengzhuang ducts can achieve decimeter-level positioning accuracy in
South Road, Haidian District, Beijing 100094, People’s Republic of China
© 2024 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group
This is an Open Access article distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivatives License (http://creativecommons.org/
licenses/by-nc-nd/4.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited, and is not
altered, transformed, or built upon in any way. The terms on which this article has been published allow the posting of the Accepted Manuscript in a repository by the
author(s) or with their consent.
Received 2 March 2024; accepted 25 August 2024
258 DOI 10.1080/00396265.2024.2401665 Survey Review 2025 VOL 57 NO 402

<!-- PAGE: 3 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
both static and kinematic modes (Zhou et al., 2024) with commission for maritime services under the Internet pro-
the release of the interface control document for PPP ser- tocol (Ntrip) and can be accessed via the Internet by any
vice signal PPP-B2b in 2020 (CSNO, 2020), BDS-3 began user who would like to investigate the PPP-B2b perform-
providing PPP services for china and its surrounding areas ance in any region.
via three geostationary Earth orbit (GEO) satellites (Yang
et al., 2021). Several recent studies have investigated the
PPP-B2b service availability
performance of PPP-B2b services. Ren et al. (2021) Indi-
cated that centimetre-level accuracy can be achieved for Availability is the percentage of time the PPP-B2b service
both static and kinematic position modes with the PPP- is usable within a specified coverage area. In this study,
B2b service at the need for Internet access The high posi- the availability of the PPP-B2b service is defined as
tioning performance of PPP-B2b has been confirmed in epochs with position DOP (PDOP) ≤ 6, which is com-
several recent studies using GNSS stations located in monly used as a basic service availability threshold with
China (Nie et al., 2021, Tao et al., 2021, Wang et al., respect to the GPS (Ward, 1997) and BDS-3 performance
2021, Zhang et al., 2022). Furthermore, applications of standards (CSNO, 2018). Therefore, for a region to uti-
PPP-B2b have been extensively studied in various lize PPP-B2b service, two criteria must be met: (1) at
domains, including water vapor monitoring (Yang et al., least one of the three BDS-3 GEO satellites is visible to
2023), time transfer (Ge et al., 2023), and earthquake receive the PPP-B2b correction information; (2) at least
monitoring (Zang et al., 2024). four visible GNSS satellites have the correction infor-
However, because PPP-B2b correction information is mation from the PPP-B2b signal, and the corresponding
derived only from the BDS-3 tracking stations deployed PDOP does not exceed six. The availability of four satel-
in China, its effective service is limited to China and its lites with PDOP values smaller than six is a basic cri-
surrounding areas (Yang et al., 2022). Therefore, the per- terion for standard point positioning, which does not
formance of PPP-B2b may vary depending on the num- ensure that a high-accuracy positioning result can be
ber of available satellites and the satellite geometry. achieved with PPP. However, we can still provide a
Most studies have focused on the performance of PPP- preliminary definition of PPP-B2b service coverage
B2b in China, and little attention has been paid to its using these criteria, and a more comprehensive investi-
effective service coverage and performance in different gation will be conducted using observations from widely
regions, especially outside China to address these short- distributed GNSS stations. In this study, the cut-off
comings, we comprehensively investigated the visibility elevation of the GNSS and BDS-3 GEO satellites was
and dilution of precision (DOP) of satellites in terms of set to 7°.
PPP-B2b signals in different regions to identify their We used the saved PPP-B2b orbit information from July
effective service coverage. The performance of BDS 21, 2022, to investigate the number of visible satellites and
PPP-B2b in positioning and ZTD estimation was evalu- corresponding DOP values with a spatial resolution of
ated at 48 widely distributed stations using both static 1° × 1° and assumed that the altitudes were zero. This
and kinematic PPP modes. allowed us to investigate the minimum, maximum, and
average numbers of visible satellites and the DOP values
at each grid point, providing us with insights into the avail-
Real-time PPP-B2b decoding and ability of PPP-B2b services in different regions.
transfer via the internet
Number of satellites
Because most GNSS receivers cannot be used to decode
Figure 2shows the number of satellites the PPP-B2b service
PPP-B2b signals, we designed a PPP-B2b-Nrtip-Cater
on July 21, 2022 as observed at the BJ01 site in Beijing,
system to investigate the performance of real-time posi-
China. On average, nine BDS-3 satellites and seven GPS
tioning and ZTD retrieval in different regions. As illus-
satellites are available at each epoch of the PPP-B2b service.
trated in Figure 1, the PPP-B2b correction information
For most epochs, the number of BDS-3 satellites was
was first received and decoded by a custom-developed
receiver located in Beijing, China. These corrections
were then sent to our Ntripcaster Server, which is broad-
cast using the network transmission of the radio technical
2 Number of satellites for BDS-3 (blue line), GPS (green
line), and a combination of BDS-3 and GPS (yellow line)
from 00:00 to 24:00 UTC on July 21, 2022, observed at
1 Workflow of the PPP-B2b-NRTIP-Cater system. station BJ01 located in Beijing, China.
Survey Review 2025 VOL 57 NO 402 259

<!-- PAGE: 4 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
3 Distribution of the minimum (top), maximum (middle), and average (bottom) number of satellites for BDS-3 (left), GPS
(middle), and a combination of BDS-3 and GPS (right) in different regions. The number of satellites is represented by different
colours, as indicated by the colour bar, with values smaller than 4 marked in white and values larger than 10 marked in red.
greater than that of GPS satellites. Given the combination indicate that BDS-3 has slightly better coverage than that
of BDS-3 and GPS satellites, the total number of satellites of GPS because the number of BDS-3 satellites broadcast
ranged from 13 to 20, with a mean value of 16. in PPP-B2b was greater than that of GPS satellites. The
Figure 3 shows the minimum, maximum, and average use of a combination of BDS-3 and GPS satellites ensures
number of GNSS satellites in different regions. The results that at least four satellites are visible in most Asia-Pacific
4 Distribution of the percentage of epochs with no fewer than four (top) or five (bottom) visible satellites for BDS-3 (left), GPS
(middle), and the combination of BDS-3 and GPS (right). The percentages are represented by different colours, as indicated
by the colour bar.
260 Survey Review 2025 VOL 57 NO 402

<!-- PAGE: 5 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
5 Distribution of the average value (top) and variation (bottom) of HDOP (left), VDOP (middle), and PDOP (right). The DOP
values are represented by different colours, with values larger than 20 marked in red, as indicated by the colour bar.
countries, Russia, Eastern Europe, and Northeast Africa. Satellite DOP
The PPP-B2b service provides the most visible satellites
In addition to the number of satellites, the DOP, which rep-
for East China, with relatively even coverage across
resents the quality of the geometry of the satellite constel-
Asia. The average number of satellites (BDS-3 + GPS)
lation, is another important indicator of GNSS accuracy.
steadily decreased from approximately 15 in East China
Figure 5shows the spatial distributions of the average hori-
to four in the regions south of Australia and Northeast
zontal DOP (HDOP), vertical DOP (VDOP), and PDOP
Africa. Figure 4 shows the percentage of epochs with
values and their temporal variations (the maximum value
more than four or five visible GNSS satellites. With a com-
minus the minimum value). In line with the spatial distri-
bination of BDS-3 and GPS satellites, at almost every
bution of visible GNSS satellites, the average DOP was
epoch, there are at least four satellites across most Asia-
the smallest (<2) in East China and increased to more
Pacific countries, Eastern Europe, Northeast Africa, the
than 10 in regions far from China, such as South Australia
Indian Ocean, and the Pacific Ocean.
and Africa. The temporal variation in DOP values in
China was less than approximately 5, whereas, for South
Australia, the variation was greater than 20.
According to the BDS open service performance stan-
dard (CSNO, 2018), the global PDOP availability should
meet the requirement of PDOP ≤ 6 for 95% of the time.
Therefore, to identify the PPP-B2b service availability
based on this criterion, we calculated the percentage of
the time that the PDOP ≤ 6, and the results are shown
in Figure 6. The yellow, blue, and red lines in Figure 6
depict the regions with a PDOP ≤ 6 for 95%, 85%, and
60% of the time, respectively. Hereafter, we define the
effective PPP-B2b service region as the area with a
PDOP ≤ 6, 95% of the time. Figure 6 shows that, com-
pared to the Northern Hemisphere, only a limited region
in the Southern Hemisphere was covered by PPP-B2b.
This only provides us with a preliminary definition of
PPP-B2b service coverage because its performance in
positioning and related applications varies with location
due to the differences in the number and geometry of
usable satellites. To further illustrate the distribution of
6 Distribution of the percentage of time that PDOP ≤ 6. The usable satellites in the PPP-B2b service for different
green, yellow, blue, and red dashed lines represent the regions, a sky view plot of all visible satellites on July
locations with PDOP ≤ 6 for 99%, 95%, 85%, and 60% of 21, 2022, from 00 to 24 h UTC at 12 locations is shown
the time, respectively. in Figure 7. The distribution of usable satellites with
Survey Review 2025 VOL 57 NO 402 261

<!-- PAGE: 6 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
7 Sky view plot of viewable satellites on July 21, 2022, from 00 to 24 h UTC at 12 locations. Different colours represent differ-
ent GNSS satellites.
Table 1 ZTD estimation strategy with PPP-B2b
Observables IFLC of pseudorange and carrier phase
Frequencies GPS L1/L2 and BDS-3 B1I/B3I (B1C/B2a)
Elevation cut-off 7°
angle
ZTD estimation A priori value for the hydrostatic delay, calculated using the Saastamoinen model, and the wet delay was
estimated as a random walk process noise of 5 mm/√h
Coordinate Static mode: coordinates are estimated as constant parameters Kinematic mode: coordinates are estimated as
white noise parameters
Mapping function Global mapping function
Gradient North and east components of the tropospheric gradient parameters were estimated
parameters
Receiver clock Receiver clock estimated as white noise parameter for GPS and BDS-3 separately
Solution type Static/kinematic PPP with float ambiguities
Corrections models Phase wind-up, relativistic delays, the effects of the solid Earth pole tide and the ocean pole tide are modelled
according to the IERS Conventions 2010
262 Survey Review 2025 VOL 57 NO 402

<!-- PAGE: 7 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
Further details regarding the 48 GNSS stations are pro-
vided in the Appendix. With the PPP-B2b information
transferred by the system through the Internet, as illus-
trated in Section 2, and the real-time observation streams
at these stations, the ZTD and position were calculated
using the PPP technique with 30 s sampling in real-
time. The performance of the ZTD and positioning accu-
racy were then evaluated by comparing them with the
post-processed results with Geodetic Benchmark
(GBM) final products provided by the Helmholtz Centre
Potsdam and German Research Centre for Geosciences.
The key processing strategies are listed in Table 1.
Solution integrity
The accuracy and integrity of the solutions are two
important indicators of the PPP-B2b service, which indi-
cate whether this technique can continuously provide
users with a reliable positioning service. An insufficient
8 Integrity of the PPP-B2b solution at 48 sites. The yellow number of visible satellites or poor satellite geometry at
line represents the locations with PDOP ≤6 for 95% of certain epochs may lead to a failure in PPP parameter
the time. The PPP-B2b solution integrity is defined as estimation with PPP-B2b corrections, thus affecting the
the ratio between the number of PPP-B2b solutions and continuity of the PPP-B2b solutions. To investigate the
the number of GBM solutions. integrity of the PPP-B2b solution, we compared the num-
ber of PPP solutions obtained with the PPP-B2b and
GBM products. The PPP-B2b solution integrity was
respect to azimuth and elevation varies with location. For
defined as the ratio of the number of PPP solutions
example, although the average PDOP values at (60° N,
obtained with the PPP-B2b and GBM products. The
120° E) and (30° N, 120° E) are both less than two, the
integrity of the PPP-B2b solution was defined as the
satellite tracks can cover almost all azimuths and
ratio of the number of PPP solutions obtained using
elevations at (30° N and 120° E), whereas at (60° N,
the PPP-B2b products to the number obtained using
120° E), the visible satellites are mostly in the southern
the GBM products. As revealed in Figure 8, for the
direction, which may bias the ZTD estimation results if
sites located within the PPP-B2b service region (PDOP ≤
there is a strong atmospheric horizontal gradient.
6 for 95% of the time), the integrity of the solution is
close to 100%. For sites located outside the PPP-B2b ser-
ZTD retrieval and positioning vice region, the solution integrity decreased from above
90% to approximately 75% at GRAZ (Austria) and
performance of PPP-B2b
approximately 50% in South Australia. For sites in the
As depicted in the previous section, the DOP, number of Antarctic, the integrity values were all less than 10%,
satellites, and sky view of the viewable satellites have an indicating that PPP-B2b was barely useful in this region.
obvious dependence on location. Therefore, to investi- Solution integrity is mainly related to the number and
gate how this affects ZTD retrieval and positioning accu- geometry of usable satellites. Typically, it is not possible
racy in different regions, we selected 48 stations for our to obtain a reliable solution using PPP when the number
real-time positioning and ZTD retrieval experiments. of satellites is very small or the PDOP value is very large.
9 Mean number of visible satellites (cut-off elevation ≥ 7°) for the GBM and PPP-B2b products between DOY 202 and 208 at 48
sites. The different colours represent the number of mean satellites as indicated by the colour bar, with values larger than 20
marked in red.
Survey Review 2025 VOL 57 NO 402 263

<!-- PAGE: 8 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
10 Mean (left) and STD value (right) of PDOP for GBM and PPP-B2b products between DOY 202 and 208 at 48 sites. The colour
bar shows the mean or STD of PDOP values with corresponding colours, where values larger than 10 are marked in red
As shown in Figure 9, when the GBM products were used, using the GBM products. Figure 11 shows the RMS
the number of usable satellites was greater than 15 at 43 of and bias of the ZTD derived using PPP-B2b. For the
the 48 stations. The lowest number of usable satellites was sites located in China, the RMSs of the ZTD are mostly
observed at the FTNA and MSSA stations (approxi- within 10–20 mm, with biases varying from −15 to
mately 12), which could only observe a few of the BDS-3 15 mm. The lowest RMS was observed at site JNYZ,
satellites (PRN number <30) owing to the limitations of with an RMS value of 10.57 mm and a bias of
their receivers. For the PPP-B2b products, the number of −3.95 mm. For the sites located in Europe, the RMSs
usable satellites was greater than 10 at only 13 stations of the ZTD are mostly within 15–30 mm, with biases
and showed a strong dependence on location. Several varying from −20 to 20 mm. The RMSs of the ZTD for
sites with receivers cannot track new BDS-3 satellites sites located in the Northern Hemisphere were lower
(usually PRN > 30), which significantly reduces the num- than those for sites located in the Southern Hemisphere,
ber of usable GNSS satellites. The statistical results show which had RMS values larger than 30 mm at most sites.
that the STDs of the number of usable satellites are less Figure 12shows the comparison between ZTDs derived
than two across all stations, indicating that the number using PPP-B2b and GBM orbit/clock products at
of usable satellites is stable for both GBM and PPP-B2b. TAKJ station in China (36.2° N, 117.1° E) and MTIS
Figure 10shows the spatial characteristics of the PDOP station in Australia (20.7° S, 139.5° E). For the TAKJ
values, which indicate a property similar to the number of station, located in the central region of the PPP-B2b ser-
available satellites distributed. According to the results vice, the ZTDs derived from PPP-B2b and GBM show a
shown in Figure 10, the average PDOP value for satellites very good agreement, with differences mainly within
with GBM products was mostly within 1–2 with a standard ±20 mm. In contrast, for the MTIS station located out-
deviation of less than 1. For satellites with PPP-B2b pro- side of the PPP-B2b service region, a significant discre-
ducts, only the stations located in East China had STD pancy is observed between the two ZTD solutions,
values comparable to those of the GBM products. indicating noticeably degraded accuracy of the PPP-
B2b solution in the Southern Hemisphere.
Figure 13 shows the static position accuracy in the
Real-time ZTD and coordinates derived with
north, east and up directions. The position accuracy for
PPP-B2b using static PPP mode
sites located in the Northern Hemisphere was much bet-
Using the PPP-B2b corrections and real-time obser- ter than those in the Southern Hemisphere. For the nine
vations, the ZTD and coordinates were calculated in stations located in China, the mean RMS errors of the
real-time. The results derived with PPP-B2b were evalu- coordinates in the north, east, and up components were
ated by comparing them with the post-processed results 1.1, 1.5, and 2.3 cm, respectively. The biases were mostly
264 Survey Review 2025 VOL 57 NO 402

<!-- PAGE: 9 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
Asia, the mean RMSs of the position errors in the
north, east, and up components were 2.1, 5.0, and
7.7 cm, respectively. In terms of bias, an obvious negative
bias can be observed at most sites in all three com-
ponents, especially in the up component. The 3D RMS
errors range from 4.6 cm to 18.3 cm, with a mean value
of 9.8 cm. For sites located in the Southern Hemisphere,
the RMS errors are larger than those in the Northern
Hemisphere and show a strong dependence on location.
For the 9 stations located on the continent of Australia,
the mean RMSs of the position errors in the north,
east, and up components are 8.9, 12.6, and 12.4 cm,
respectively, which are much larger than those of sites
located in China. Figure 14 shows the comparison
between the coordinates estimated using PPP-B2b and
GBM at TAKJ and MTIS stations, indicating a slightly
better performance at TAKJ station, located within the
PPP-B2b service region, than at MTIS station, which is
close to the edge of the PPP-B2b service region. The vari-
ation in the accuracy of the ZTD estimates and coordi-
nates, which shows much better performance in China
compared to Australia or Europe, aligns well with the
variation in the number of visible satellites and DOP
values across different regions. This agreement is reason-
able since the PPP solution is strongly dependent on the
number and geometry of the GNSS satellites.
11 RMS (top) and bias (bottom) of the real-time ZTD derived Real-time ZTD and coordinates derived with
with PPP-B2b products using static PPP mode between PPP-B2b using the kinematic PPP mode
DOY 202 and 208 at 48 sites. The ZTD estimated with
To investigate the performance of the kinematic ZTD
GBM products was used as the reference. The colour
estimation with PPP-B2b, an experiment was conducted
bar shows the RMS or bias of PPP-B2b ZTD with corre-
at 44 global stations between DOY 250 and 256. As
sponding colours, where values larger than 40 mm are
shown in Figure 15, the RMS values of the kinematic
marked in deep red.
ZTD values estimated at the eight stations in China
and one station in Japan were all within 20 mm, with a
mean value of 14.9 mm. The biases are all between −20
within −4 cm to 4 cm. The 3D RMS errors range from and 20 mm. For station ADH1, located in the United
1.2 cm to 8.5 cm, with a mean value of 3.3 cm. For the Arab Emirates, the RMS value was 24.4 mm, with a
11 stations located in Europe and western and central bias value of −18.3 mm. At the other stations, the
12 Comparison of ZTDs estimated using static PPP mode with PPP-B2b and GBM at stations TAKJ (left) and MTIS (right). The
X-axis represents time in DOY, and the Y-axis represents ZTD values or their differences. The top panels show ZTD values
for PPP-B2b (red line) and GBM (blue line) solutions, while the bottom panels show their differences
Survey Review 2025 VOL 57 NO 402 265

<!-- PAGE: 10 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
13 RMS (left) and bias (right) of the real-time coordinates derived with PPP-B2b products using static PPP mode between DOY
202 and 208 at 48 sites. The coordinates estimated with GBM products were used as the reference. The colour bar shows
the RMS or bias of the PPP-B2b coordinates with corresponding colours, where values larger than 20 cm for the RMS or
10 cm for the bias are marked in deep red and values smaller than −10 cm for the bias are marked in deep blue.
14 Coordinate differences between PPP-B2b and GBM solutions using static PPP mode at stations TAKJ (left) and MTIS
(right) in north, east, and up directions.
266 Survey Review 2025 VOL 57 NO 402

<!-- PAGE: 11 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
the kinematic PPP mode using PPP-B2b information.
As shown in Figure 16, the comparison of the time series
of ZTDs derived using PPP-B2b and GBM in kinematic
mode reveals a strong agreement at the TAKJ station in
China, located in the central region of the PPP-B2b ser-
vice. In contrast, a significant discrepancy is observed
at the MTIS station in Australia, located near the edge
of the PPP-B2b service region.
As shown in Figure 17, the spatial properties of the
coordinate errors agree well with those of the ZTD
error. For the seven stations located in China, the mean
RMS errors of coordinates in the north, east and up
directions are 2.8, 5.3, and 9.0 cm, respectively, with
biases ranging from −4.3 cm to 7.8 cm. The mean 3D
RMS error was 10.9 cm across the seven stations. The
3D RMS errors at stations POHN (Micronesia), MSSA
(Japan), and ADH1 (Emirates) are 16.8, 20.7, and
27.0 cm, respectively. At other stations, the 3D RMS
errors exceeded 50 cm. The time series shown in Figure
18 demonstrates that the coordinate estimation error at
the MTIS station is significantly greater than at the
TAKJ station. This increased error at MTIS is primarily
caused by a lack of visible satellites or poor satellite geo-
metry during certain epochs.
Convergence performance
15 RMS (top) and bias (bottom) of the real-time ZTD derived
To investigate the convergence performance of the PPP-
with PPP-B2b products using kinematic PPP mode
B2b service in different regions, real-time static and kin-
between DOY 250 and 256 at 44 sites. The ZTD estimated
ematic PPP experiments were conducted on DOY 011
with GBM products was used as the reference. The colour
and 015 in 2023 at 45 stations. The static and simulated
bar shows the RMS or bias of PPP-B2b ZTD with corre-
kinematic PPP processes started at 04:00 UTC on DOY
sponding colours, where values larger than 100 mm for
011 and restarted every 6 h till 08:00 UTC on DOY 015
RMS or 90 mm for bias are marked in deep red, and values
to obtain 17 convergence periods at each station to
smaller than −90 mm for bias are marked in deep blue.
study the convergence behaviour in detail. In this study,
the PPP convergence time was defined as the time when
the position errors were first reached and maintained
RMS values were greater than 30 mm. This finding indi- within 20 (10) and 40 (20) cm in the horizontal (H) and
cates that it is only possible to retrieve a high-accuracy vertical (V) components, respectively, for at least 10 con-
ZTD in China and surrounding areas (e.g. Japan) for secutive min. The success rate of convergence and the
16 Comparison between ZTDs estimated using kinematic PPP mode with PPP-B2b and GBM at stations TAKJ (left) and MTIS
(right). The X-axis represents time in DOY, and the Y-axis represents ZTD values or their differences. The top panels show
ZTD values for PPP-B2b (red line) and GBM (blue line) solutions, while the bottom panels show their differences.
Survey Review 2025 VOL 57 NO 402 267

<!-- PAGE: 12 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
17 RMS (left) and bias (right) of the real-time coordinates derived with PPP-B2b products using kinematic PPP mode between
DOY 250 and 256 at 44 sites. The coordinates estimated with GBM products were used as the reference. The colour bar
shows the RMS or bias of PPP-B2b coordinates with corresponding colours, where values larger than 50 mm for RMS
or 45 mm for bias are marked in deep red, and values smaller than −45 mm for bias are marked in deep blue.
18 Coordinate differences between PPP-B2b and GBM solutions using kinematic PPP mode at stations TAKJ (left) and MTIS
(right) in north, east, and up directions.
268 Survey Review 2025 VOL 57 NO 402

<!-- PAGE: 13 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
average convergence time for the 17 convergence periods PPP experimental results. The average convergence time
are provided in Figures 19and 20for the static and kin- of kinematic PPP was longer than that of static PPP.
ematic modes, respectively. As shown in Figure 19, the Considering eight stations located in China as an
success rate and average time of convergence of static example, the average convergence time varies from
PPP with PPP-B2b corrections show an obvious depen- 16.2 min (TAKJ) to 100.4 min (KSKT) with the conver-
dence on location. The best convergence performance gence criterion of H < 20 cm and V < 40 cm and varies
for the PPP-B2b service was observed in China and its from 35.9 min (TAKJ) to 169.4 min (KSKT) with the
surrounding areas. For example, for eight stations located convergence criterion of H < 10 cm and V < 20 cm. For
in China, the success rate of convergence was 100% for station KSKT, which is located in the westernmost city
two convergence criteria (H < 20 cm, V < 40 cm, H < of China, only 13 of 17 experiments successfully con-
10 cm, and V < 20 cm). The average convergence time verged with the H < 10 cm and V < 20 cm criteria. For
for the convergence criterion of H < 20 cm and V < most stations located south of 30° S, the success rate of
40 cm varies from 11.8 min (TAKJ) to 35.9 min convergence was below 10% with the criteria of H <
(KSKT), whereas for the convergence criterion of H < 20 cm and V < 40 cm.
10 cm and V < 20 cm, the convergence time varies from
23.8 min (TAKJ) to 62.6 min (YNTW). For stations far
Conclusion
from China, the convergence rate becomes low, which
leads to low positioning accuracy, as shown in the pre- The investigation revealed that the average number of vis-
vious subsections. The convergence time for the same ible satellites varies significantly with location, decreasing
station exhibited a large variation with epochs. Consider- steadily from approximately 15 in East China to 4 in the
ing the TAKJ station as an example, the shortest conver- regions south of Australia and Northeast Africa. This led
gence time was only 7.0 min at UTC 04:00 on DOY 013, to an increase in the average PDOP from less than 2 in
and the longest convergence time was 55.4 min at UTC East China to more than 10 in regions far from China,
10:00 on DOY 012. such as South Australia and Africa. An insufficient num-
For the simulated kinematic PPP experiments, as ber of satellites or poor satellite geometry led to the fail-
shown in Figure 20, the convergence performance exhib- ure of the PPP solution at approximately 50% and 90% of
ited a spatial characteristic similar to that of the static the epochs in South Australia and Antarctica,
19 Success rates of convergence and average convergence times at 45 stations with static PPP. Left panels: the success rate
of convergence (left top) and average convergence time (left bottom) with the convergence criterion of a horizontal (H)
error smaller than 20 cm and a vertical (V) error smaller than 40 cm. Right panels: the success rate of convergence
(right top) and average convergence time (right bottom) with the convergence criterion of a horizontal error smaller
than 10 cm and a vertical error smaller than 20 cm. The colour bar shows the success rate of convergence or the conver-
gence time.
Survey Review 2025 VOL 57 NO 402 269

<!-- PAGE: 14 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
20 Success rate of convergence and average convergence time at 45 stations with kinematic PPP. Left panels: the success
rate of convergence (left top) and average convergence time (left bottom) with the convergence criterion of horizontal (H)
error smaller than 20 cm and vertical (V) error smaller than 40 cm. Right panels: the success rate of convergence (right top)
and average convergence time (right bottom) with the convergence criterion of horizontal error smaller than 10 cm and
vertical error smaller than 20 cm. The colour bar shows the success rate of convergence or convergence time.
respectively. The accuracy of the positioning and ZTD coverage for real-time positioning and ZTD estimation
results agreed well with the spatial variation in the in PPP mode. In this study, the performance of PPP-B2b
PDOP values of the satellites. For the static PPP exper- was evaluated over a one-week period, which is insufficient
iments, the best results were observed at stations located for assessing its long-term stability. A comprehensive
in China, with ZTD RMS errors mostly within 10– evaluation requires at least one year of study. To facilitate
20 mm and 3D coordinate RMS errors of 3.3 cm. The long-term analysis of the PPP-B2b service, we have set up
kinematic results revealed that the RMS errors of the kin- a receiver to receive both PPP-B2b and HAS services, and
ematic ZTDs estimated at the stations located in China the received orbit and clock corrections are saved in the
were all within 20 mm, with a mean value of 14.9 mm. SP3 format for future studies.
For the other stations, the RMS values mostly exceeded
30 mm. In terms of the kinematic positioning results,
the mean 3D RMS of the coordinates was 10.9 cm across Acknowledgements
the seven stations located in China, which is notably bet-
The authors would like to thank the GFZ for providing
ter than the performance in other regions. The investi-
high-accuracy orbit and clock products and the IGS for
gation of convergence performance shows that the
providing GNSS observations. This work was funded
success rate of convergence and the average convergence
by the Aerospace Information Research Institute.
time are highly dependent on the location and time.
As a regional service, the PPP-B2b service performs well
in China and surrounding areas (e.g. Japan) in terms of
Funding
positioning and ZTD estimation but deteriorates signifi-
cantly in regions far from China (e.g. Australia). Although This research was supported by National Natural Science Foundation of
the Galileo HAS Initial Service was designed as a global China (42474015).
service, areas including Eastern Asia, Southeast Asia,
Australia, and New Zealand were currently excluded
Disclosure statement
from its coverage. Therefore, a combination of PPP-B2b
and HAS services has the potential to provide global No potential conflict of interest was reported by the author(s).
270 Survey Review 2025 VOL 57 NO 402

<!-- PAGE: 15 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
Data availability statement interests include GNSS precise positioning and GNSS
meteorology.
The datasets generated and/or analyzed during the current
Cong Qiu received the PhD degree from University of
study are available from the corresponding author upon
Chinese Academy of Sciences in 2023, with specialization
reasonable request.
in global navigation satellite system. His research inter-
ests include GNSS precise positioning and GNSS
Notes on contributors meteorology.
Xiaoming Wang received the PhD degree from RMIT Uni- Li Li received the PhD degree from Central South Uni-
versity, Melbourne, VIC, Australia, in 2017, with special- versity, Changsha, Hunan, China, in 2011, with specializ-
ization in GNSS meteorology. He is currently an ation in Global Navigation Satellite System meteorology.
associate professor with the Aerospace Information He is currently an associate professor at the School of
Research Institute, Chinese Academy of Sciences, Beijing, Geographical Sciences and Geomatics Engineering, Suz-
China. His research interests include GNSS precise posi- hou University of Science and Technology, Suzhou,
tioning, GNSS data processing, and GNSS meteorology. China. His research interests include GNSS meteorology
and GNSS precise positioning.
Kai Zhou received the MS degree from Beihang Univer-
sity, Beijing, P.R. China in 2014. He is now an engineer
in Aerospace Information Research Institute, Chinese ORCID
Academy of Sciences. His current research interests
include precision positioning and embedded software Xiaoming Wang http://orcid.org/0000-0003-1720-6630
development.
Jinglei Zhang received the MS degree from China Uni- References
versity of Geosciences (Beijing), in 2021, with specializ-
Aichinger-Rosenberger, M., Weber, R., and Hanna, N. 2021. Kinematic
ation in global navigation satellite system. He is
ZTD estimation from train-borne single-frequency GNSS: vali-
currently an Assistant engineer with the Aerospace Infor-
dation and assimilation. Remote sensing, 13, 3793.
mation Research Institute, Chinese Academy of Sciences, Chadwell, C. D., and Bock, Y. 2001. Direct estimation of absolute preci-
Beijing, China. His research interests include GNSS pre- pitable water in oceanic regions by GPS tracking of a coastal buoy.
cise positioning and GNSS meteorology. Geophysical research letters, 28, 3701–3704.
CSNO. 2018. Beidou navigation satellite system open service perform-
Haobo Li received his first PhD degree in Geodesy and Sur- ance standard (version 2.0). Beijing: China Satellite Navigation
veying Engineering from the China University of Mining Office.
CSNO. 2020. Beidou navigation satellite system signal in space interface
and Technology (joint supervision with the Chinese Acad-
control document: precise point positioning service signal PPP-
emy of Sciences). Then, he completed his second PhD
B2b (version 1.0). Beijing: China Satellite Navigation Office.
degree in Geospatial Sciences from RMIT University. Fernandez-Hernandez, I., et al., 2022. Galileo high accuracy service:
After his postdoc appointment at Tsinghua University, initial definition and performance. GPS solution, 26, 65 (1–18).
He is currently working as a Postdoctoral Research Assist- Ge, Y., et al., 2023. An investigation of PPP time transfer via BDS-3
PPP-B2b service. GPS solutions, 27, 61.
ant at RMIT University. His research interests include geo-
Gratton, P., Banville, S., Lachapelle, G., and O’keefe, K. 2021.
desy, GNSS atmospheric sounding, GNSS meteorology/ Kinematic zenith tropospheric delay estimation with GNSS PPP
climatology, high-accuracy positioning and navigation, in mountainous areas. Sensors (Basel), 21, 5709.
atmospheric science, and disaster risk reduction. Hadas, T., and Bosy, J. 2015. IGS RTS precise orbits and clocks verifica-
tion and quality degradation over time. GPS solution, 19, 93–105.
Hong Liang received the BS degree in climatology from Hadas, T., Hobiger, T., and Hordyniec, P. 2020. Considering different
Nanjing Institute of Meteorology in 2002; the M.S. recent advancements in GNSS on real-time zenith troposphere
degree in meteorology from Chinese Academy of Meteor- estimates. GPS solution, 24, 99.
Kazmierski, K., Zajdel, R., and Sośnica, K. 2020. Evolution of orbit and
ological Science in 2005; and the PhD degree in meteor-
clock quality for real-time multi-GNSS solutions. GPS solution,
ology from the University of Chinese Academy of 24, 111.
Sciences in 2012. From 2017-2018, he was a visiting scho- Leick, A., Rapoport, L., and Tatarnikov, D. 2015. GPS satellite survey-
lar at the Scripps Institution of Oceanography, University ing. Hoboken, New Jersey: John Wiley & Sons.
Li, X., et al., 2015. Multi-GNSS meteorology: real-time retrieving of
of California San Diego, USA. He is currently a
atmospheric water vapor from BeiDou, galileo, GLONASS, and
researcher with the Meteorological Observation Center,
GPS observations. IEEE transactions on geoscience and remote sen-
China Meteorological Administration, China. His sing, 53, 6385–6393.
research interest is GNSS atmospheric remote sensing. Nie, Z., et al., 2021. Initial assessment of BDS PPP-B2b service: pre-
cision of orbit and clock corrections, and PPP performance.
Manhong Tu is a senior engineer at the Meteorological Remote sensors, 13, 2050.
Observation Center of the China Meteorological Adminis- Ren, Z., et al., 2021. Performance assessment of real-time precise point
tration. Her work primarily focuses on the innovative positioning using BDS PPP-B2b service signal. Advances in space
research, 68, 3242–3254.
application of BeiDou technology in meteorological obser-
Skone, S., Gao, Y., Al-Fanek, O., Tao, W., Zhang, Y., Héroux, P., and
vations, equipment development, the establishment of
Collins, P. Atmospheric moisture estimation using GPS on a mov-
business standards, and system development. She serves ing platform. Proceedings of the 19th international technical meet-
as the deputy chief of the GNSS/MET observation and ing of the satellite division of the institute of navigation (ION
application innovation team, chief engineer of key projects GNSS 2006), 2006 Fort Worth, TX. ION, 1891–1901.
Tao, J., et al., 2021. Initial assessment of the BDS-3 PPP-B2b RTS com-
at the China Meteorological Administration, and technical
pared with the CNES RTS. GPS solution, 25, 131.
lead of several important experimental teams. Wang, J., et al., 2019. Retrieving precipitable water vapor from shipborne
multi-GNSS observations. Geophysical research letters, 46, 5000–
Yufei Chen received the MS degree from University of
5008.
Chinese Academy of Sciences in 2023, with specialization
Wang, E., et al., 2021. Performance evaluation of precise point positioning
in global navigation satellite system. His research for BeiDou-3 B1c/B2a signals in the global range. Sensors, 21, 5780.
Survey Review 2025 VOL 57 NO 402 271

<!-- PAGE: 16 -->

Wang et al. An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions
Ward, N. 1997. Understanding GPS—principles and applications (Elliott Zang, J., et al., 2024. Performance assessment of the BDS-3 PPP-B2b ser-
D. Kaplan, Editor). £ 75. ISBN: 0-89006-793-7. Artech House vice for real-time earthquake source description: a case study for
Publishers, Boston & London. 1996. Journal of navigation, 50, the 2021 Mw 7.4 Maduo earthquake. GPS solution, 28, 26.
151–152. Zhang, W., et al., 2022. Initial assessment of BDS-3 precise point positioning
Yang, Y., et al., 2021. Featured services and performance of BDS-3. service on GEO B2b signal. Advances in space research, 69, 690–700.
Science bulletin, 66, 2135–2143. Zhou, F., et al., 2020. Assessment of the positioning performance and
Yang, Y., et al., 2022. Principle and performance of BDSBAS and PPP- tropospheric delay retrieval with precise point positioning using
B2b of BDS-3. Satellite navigation, 3, 5. products from different analysis centers. GPS solution, 24, 12.
Yang, H., et al., 2023. Assessment of precipitable water vapor retrieved Zhou, P., Xiao, G., and Du, L. 2024. Initial performance assessment of
from precise point positioning with PPP-B2b service. Earth science galileo high accuracy service with software-defined receiver. GPS
informatics, 16, 315–328. solution, 28, 2.
Appendix
Table A1shows the detailed information on the GNSS stations used in this study.
Table A1. GNSS station information.
No. Site Lat (°) Lon (°) City Country Tectonic Plate
1 MAC1 −54.5 158.9 Macquarie Island Australia Australian/Pacific
2 HOB2 −42.8 147.4 Hobart Australia Pacific
3 ESPA −33.9 121.9 Esperance Australia Australian
4 PARK −33.0 148.3 Parkes Australia Australian
5 CEDU −31.9 133.8 Ceduna Australia Australian
6 MCHL −26.4 148.1 Mitchell Australia Australian
7 ALIC −23.7 133.9 Alice Springs Australia Australian
8 MTDN −22.1 131.5 Mt Doreen Station Australia Australian
9 MTIS −20.7 139.5 Mount Isa Australia Australian
10 DARW −12.8 131.1 Darwin Australia Australian
11 COCO −12.2 96.8 Cocos Island Australia Australian
12 XMIS −10.5 105.7 Christmas Island Australia Australian
13 DAV1 −68.6 78.0 Davis Australian Antarctic Territory Antarctic
14 MAW1 −67.6 62.9 Mawson Australian Antarctic Territory Antarctic
15 CAS1 −66.3 110.5 Casey Australian Antarctic Territory Antarctic
16 LAUT −17.6 177.5 Lautoka Fiji Pacific
17 REUN −21.2 55.6 Le Tampon France African
18 FTNA −14.3 −178.1 Maopo’opo French Polynesia Pacific
19 THTG −17.6 −149.6 Papeete French Polynesia Pacific
20 KRGG −49.4 70.3 Port aux Francais French Southern Territories Antarctic
21 MAYG −12.8 45.3 Dzaoudzi Mayotte African
22 OWMG −26.2 −178.2 Owenga New Zealand Pacific
23 TUVA −8.5 179.2 Funafuti Tuvalu Pacific
24 GRAZ 47.1 15.5 Graz Austria Eurasian
25 HKSC 22.3 114.1 Hong Kong China Eurasian
26 JFNG 30.5 114.5 Wuhan China Eurasian
27 YNTW 25.0 102.8 KunMing China Eurasian
28 NCEC 28.7 115.8 NanChang China Eurasian
29 SKD1 31.3 120.6 SuZhou China Eurasian
30 TAKJ 36.2 117.1 Taian China Eurasian
31 KSKT 39.5 75.9 Kashgar China Eurasian
32 JNYZ 41.0 113.2 Ulanqab China Eurasian
33 NICO 35.1 33.4 Nicosia Cyprus African
34 POHN 7.0 158.2 Pohnpei Micronesia Pacific
35 BJ01 40.1 116.3 Matera Italy Eurasian
36 MSSA 36.1 138.4 Misasa Japan Eurasian
37 KIRI 1.4 172.9 Betio Kiribati Pacific
38 ORID 41.1 20.8 Ohrid North Macedonia Eurasian
39 BUCU 44.5 26.1 Bucuresti Romania Eurasian
40 KZN2 55.8 49.1 KAZAN Russian Federation Eurasian
41 SIN1 1.3 103.7 Singapore Singapore Eurasian
42 GANP 49.0 20.3 Ganovce-Poprad Slovakia Eurasian
43 KIR8 67.9 21.1 Kiruna Sweden Eurasian
44 ADH1 24.4 54.5 Abu Dhabi United Arab Emirates Arabian
45 HERS 50.9 0.3 Hailsham United Kingdom Eurasian
46 MAO0 20.7 −156.3 Haleakala, Maui United States of America Pacific
47 MET3 60.2 24.4 Kirkkonummi Finland Eurasian
48 SOD3 67.4 26.4 Sodankyla Finland Eurasian
272 Survey Review 2025 VOL 57 NO 402