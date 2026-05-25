<!-- PAGE: 1 -->

Citation: Pintor, P.; Lopez-Martinez,
M.; Gonzalez, E.; Safar, J.; Boyle, R.
Testing Galileo High-Accuracy Service
(HAS) in Marine Operations. J. Mar.
Sci. Eng. 2023, 11, 2375. https://
doi.org/10.3390/jmse11122375
Academic Editors: Syed Agha
Hassnain Mohsan and Inam Ullah
Received: 31 October 2023
Revised: 24 November 2023
Accepted: 14 December 2023
Published: 16 December 2023
Copyright: © 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
Journal of
Marine Science 
and Engineering
Article
Testing Galileo High-Accuracy Service (HAS) in
Marine Operations
Pedro Pintor 1, Manuel Lopez-Martinez 2,*, Emilio Gonzalez 1, Jan Safar 3
and Ronan Boyle 4
1
Spaceopal GmbH, 80335 Munich, Germany; pedro.pintor.ext@spaceopal.com (P.P.);
emilio.gonzalez.ext@spaceopal.com (E.G.)
2
European Union Agency for the Space Programme, 170 00 Prague, Czech Republic
3
Research & Development Directorate of the General Lighthouse Authorities of the UK and Ireland (GRAD),
Harwich CO12 3JW, UK; jan.safar@gla-rad.org
4
Commissioners of Irish Lights, Dun Laoghaire, A96 H500 Dublin, Ireland; ronan.boyle@irishlights.ie
*
Correspondence: manuel.lopezmartinez@euspa.europa.eu
Abstract: Global Navigation Satellite System (GNSS) technology supports all phases of maritime
navigation and serves as an integral component of the Automatic Identification System (AIS) and,
by extension, Vessel Traffic Service (VTS) systems. However, the accuracy of standalone GNSS is
often insufficient for specific operations. To address this limitation, various regional and local-area
solutions have been developed, such as Differential GNSS (DGNSS), Satellite Based Augmentation
Service (SBAS) and Real Time Kinematic (RTK) techniques. A notable development in this field is the
recent introduction of the Galileo High-Accuracy Service (HAS), which saw its initial service declared
operational by the European Commission (EC) on 24 January 2023. Galileo HAS provides high-
accuracy Precise Point Positioning (PPP) corrections (orbits, clocks and signal biases) for Galileo and
GPS, enhancing real-time positioning performance at no additional cost to users. This article presents
the results of the first Galileo HAS testing campaign conducted at sea using a buoy-laying vessel
temporarily equipped with a Galileo HAS User Terminal. The results presented in this Article include
accuracy and position availability performance achieved using the Galileo HAS User Terminal. The
article also highlights challenges posed by high-power radio-frequency interference, which likely
originated from the Long-Range Identification and Tracking (LRIT) system antenna on board the
vessel. Furthermore, the article provides additional assessments for different phases of navigation,
demonstrating better performance in slow-motion scenarios, particularly relevant to mooring and
pilotage applications. In these scenarios, values for horizontal accuracy reached 0.22 m 95% and
0.13 m 68% after removing interference periods. These results are in line with the expectations
outlined in the Galileo HAS Service Definition Document (SDD).
Keywords: Galileo; GPS; High-Accuracy Service; HAS; marine operations; horizontal accuracy;
vertical accuracy; position availability; RF interference
1. Introduction
1.1. Galileo High Accuracy Service (HAS)
The Galileo HAS Initial Service was declared operational by the European Commission
(EC) on 24 January 2023. Galileo HAS is under the responsibility of the European Union
Agency for the Space Program (EUSPA), serving as the Galileo Service Provider, and is
operated by Spaceopal GmbH. Galileo HAS provides free-of-charge, high-accuracy Precise
Point Positioning (PPP) corrections (orbits, clocks and signal biases) for Galileo and GPS,
enhancing real-time user positioning performance [1,2]. These corrections are transmitted
via the Galileo E6 signal [3] from a subgroup of Galileo space vehicles and through the
internet [4].
The augmentation corrections delivered by Galileo HAS bring users the opportunity
to lessen errors derived from the orbit and clock information delivered by the Galileo Open
J. Mar. Sci. Eng. 2023, 11, 2375. https://doi.org/10.3390/jmse11122375
https://www.mdpi.com/journal/jmse

> [5 Figure(s)]

<!-- PAGE: 2 -->

J. Mar. Sci. Eng. 2023, 11, 2375
2 of 13
Service (OS) [5] navigation data and the GPS Standard Positioning Service [6] navigation
messages. The Galileo HAS corrections, completed with Galileo HAS signals biases, enable
the computation of a high-accuracy Position Velocity and Time (PVT) solution in real-time.
By introducing HAS, Galileo pioneers a worldwide, free, high-accuracy positioning
service aimed at applications that require higher performance than that offered by the
Galileo Open Service and GPS Standard Positioning Service (i.e., c.a. 2 m 95% Horizontal
Position Error) [7,8].
1.2. Galileo HAS Roadmap
The Galileo HAS rollout follows a structured roadmap consisting of three phases.
Goals and features of each Galileo HAS phase are the following [2]:
•
Phase 0 (HAS testing and experimentation). In this phase, tests were executed to
confirm the capacity of Galileo space vehicles to broadcast via the E6B channel and
to perform preliminary user testing. The HAS Signal-in-Space (SiS) tests began in
Q1 2021.
•
Phase 1 (HA Initial Service) declared in January 2023. Provision of an initial Galileo
High Accuracy Service resulting from the implementation of a high-accuracy data
generation system processing Galileo and GPS measurements from the Galileo system
infrastructure exclusively. The initial service delivers Service Level 1 augmentation
data but without reaching the performance targets planned for the incoming full
service. Corrections are provided for both Galileo and GPS.
•
Phase 2 (HA Full Service). Full rollout of the Galileo High-Accuracy Service, both
Service Level 1 and 2, reaching its target performance. Phase 2 will include global
coverage, improved accuracy, ionospheric corrections in Europe, authentication and
error characterization. Corrections are provided for both Galileo and GPS.
As of October 2023, the Galileo HAS is in Phase 1 (HA Initial Service).
1.3. Galileo HAS Characterization
The HAS comprises two service levels for global and regional coverage [2]:
•
Service Level 1 (SL1): with global coverage; providing high-accuracy corrections to
Galileo and GPS satellite orbits and clocks, and phase and code biases for Galileo
E1/E5b/E5a/E5AltBOC/E6 and GPS L1/L5/L2C signals.
•
Service Level 2 (SL2): with European coverage; broadcasting atmospheric (at least iono-
spheric) corrections and all SL1 corrections and, eventually, additional signal biases.
Table 1 summarizes the HAS full service features and target performance for Service
Level 1 and 2 at user level.
Table 1. Main HAS full service features and target performances for Service Level 1 and 2 at user
level [2].
High Accuracy Service
Service Level 1
Service Level 2
Coverage
Global
European Coverage Area (ECA)
Type of corrections
Precise Point Positioning (PPP)–orbit, clock,
biases (code and phase)
PPP–orbit, clock, biases (code and phase) incl.
atmospheric corrections
Format of corrections
Open format similar to Compact-SSR (CSSR)
Open format similar to Compact-SSR (CSSR)
Dissemination of corrections
Galileo E6B using 448 bits per satellite per
second/terrestrial (internet)
Galileo E6B using 448 bits per satellite per
second/terrestrial (internet)
Supported constellations
Galileo, GPS
Galileo, GPS
Supported frequencies
E1/E5a/E5b/E6/E5AltBOC
L1/L5/L2C
E1/E5a/E5b/E6/E5AltBOC
L1/L5/L2C

<!-- PAGE: 3 -->

J. Mar. Sci. Eng. 2023, 11, 2375
3 of 13
Table 1. Cont.
High Accuracy Service
Service Level 1
Service Level 2
Horizontal accuracy 95%
<20 cm
<20 cm
Vertical accuracy 95%
<40 cm
<40 cm
Convergence time
<300 s
<100 s
Availability
99%
99%
User helpdesk
24 h/7
24 h/7
Table 2 describes the typical HAS positioning accuracy for users of multi-constellation
GPS and Galileo.
Table 2. Galileo HAS positioning accuracy typical performance from Galileo HAS SDD [1].
Figure of Merit
Typical
Performance
Conditions and Constrains
HAS
horizontal positioning
accuracy
≤15 cm
for Galileo + GPS
68th percentile.
In any 24 h period.
For combination of signals: E1/E5a + L1/L2C, E1/E5b + L1/L2C,
E1/E5a/E6-B + L1/L2C
Evaluated with the performance characterization user algorithm
described in Galileo HAS SDD [1].
At least eight satellites in view above an elevation of 5 degrees for
Galileo + GPS users in open sky conditions
Static user conditions.
Using clock, orbit and code biases
At the Average over all User Locations of the service area (specified
in Galileo HAS SDD [1] Section 3.1).
Usage assumptions as per Galileo HAS SDD [1] Section 2.4.
HAS
vertical
positioning
accuracy
≤20 cm
for Galileo + GPS
The Galileo HAS user algorithm in Table 2 is the algorithm implemented in the Galileo
HAS User Terminal.
Galileo HAS users must realize Galileo HAS Initial Service currently provides a
reduced performance level [1] for a global coverage excluding areas within a rectangle
defined by Latitudes [60◦S–60◦N] and Longitudes [90◦E–180◦E] and a rectangle defined
by Latitudes [60◦S–60◦N] and Longitudes [125◦W–180◦W] as defined in the Minimum
Performance Levels (MPLs) [1]. The MPLs for orbit accuracy [1] are ≤20 cm (95%) for
Galileo and ≤33 cm (95%) for GPS over the instantaneous constellation average (RMS).
The clock accuracy [1] are ≤12 cm (95%) for Galileo and ≤15 cm (95%) for GPS over the
instantaneous constellation average (RMS). The code bias accuracy is ≤50 cm (95%) for
Galileo and GPS over the instantaneous constellation average (RMS). For past and latest
quarterly reports on Galileo HAS at the system level, please refer to the official performance
report documentation [9] for the evaluation of clock/orbit/biases vs. reference products.
1.4. Galileo in Marine Navigation
In 2016, Galileo joined other Global Navigation Satellite Systems (GNSS) as part of the
International Maritime Organization’s World-Wide Radio Navigation System (WWRNS).
The IMO’s Maritime Safety Committee (MSC), during its 96th session (11–20 May 2016),
officially recognized the Galileo OS and Galileo Search and Rescue (SAR) Service as part of
the WWRNS.
While GNSS technology supports all phases of navigation and is an integral component
of Automatic identification systems (AIS) and, consequently, Vessel Traffic Service (VTS)
systems, standalone GNSS accuracy is often insufficient for specific operations. Multiple
technologies have been developed to achieve regional and local accuracy improvements,

<!-- PAGE: 4 -->

J. Mar. Sci. Eng. 2023, 11, 2375
4 of 13
such as Differential GNSS (DGNSS), Satellite Based Augmentation Service (SBAS) and Real
Time Kinematic (RTK).
When it comes to studies conducted in the past on the accuracy for marine applications
achieved in real time by GNSS standalone and with the addition of augmentations, review
of the literature indicates that GNSS standalone accuracy is in the order of a few meters [10]
and performance is slightly improved to submeter accuracy with the use of DGNSS [11] or
SBAS [12], and to centimeter accuracy using commercial services or postprocessing [13].
To meet the global demand for high-accuracy positioning, the European Commission
(EC) proposed the implementation of the Galileo HAS, making Galileo the first GNSS
constellation offering a worldwide high-accuracy augmentation service.
This article presents the first-ever Galileo HAS testing campaign conducted at sea,
made possible through a collaboration between the European Union Agency for the Space
Program (EUSPA), Spaceopal GmbH, Commissioners of Irish Lights (CIL) and the GLA1
R&D Directorate (GRAD). The results of this campaign hold significant promise for enhanc-
ing maritime operations.
2. Materials and Methods
2.1. Vessel and Test Equipment
The vessel used for this campaign was the Irish Lights Vessel (ILV) Granuaile (IMO
9192947), as shown in Figure 1. The ILV Granuaile is a buoy-laying vessel, constructed in
the year 2000 and currently registered under the flag of Ireland. Her carrying capacity is
1132 t DWT, with a reported draught of 5 m. Her length overall (LOA) is 79.63 m and her
width is 16.08 m. The vessel is owned by the Commissioners of Irish Lights, which is the
statutory body vested with the superintendence and management of all lighthouses, buoys
and beacons throughout Ireland and Northern Ireland. The powers and obligations of the
Commissioners of Irish Lights are set out in legislation in both the UK and Ireland [14].
 
Figure 1. ILV Granuaile.

> [2 Figure(s)]

<!-- PAGE: 5 -->

J. Mar. Sci. Eng. 2023, 11, 2375
5 of 13
The ILV Granuaile was already equipped with experimental GLA equipment, includ-
ing a Galileo E6 capable GNSS antenna, a TNC cable from the antenna to the equipment
room, a GNSS amplifier to compensate for cable losses, a cellular router for internet con-
nectivity over LTE/5G and an Ethernet switch to connect devices to the cellular router.
Spaceopal installed additional equipment, including a Galileo HAS User Terminal and a
laptop used for configuring, downloading data from the User Terminal and uploading data
to the Spaceopal FTP server. Some minor equipment, such as a power strip and cables,
were also added.
The User Terminal is the first Galileo HAS receiver developed for this new service [15].
It hosts a real-time Galileo HAS user algorithm, capable of operating in dual- and triple-
frequency Galileo-only and Galileo and GPS modes, with corrections obtained from either
the E6-B signal or the internet. In 2021, Spaceopal and partners developed the first HAS
receiver in only 12 months for EUSPA to support HAS initial service deployment.
The Galileo HAS User Terminal is a portable, configurable and autonomous device
designed to calculate a single- (Galileo) or multi-constellation (Galileo + GPS) Galileo HAS
and OS position, velocity and time (PVT) solution. The User Terminal can be configured
to retrieve Galileo HAS corrections either from the Galileo SiS over E6-B or Internet Data
Distribution (IDD) over NTRIP in RTCM3 format. The terminal operates with various
frequency combinations that can be configured by the user. It is a robust device with an
IP64 rating and offers multiple communication and logging capabilities. The requirements
for the High Accuracy User Terminal targeted a wide range of applications, configurations,
dynamics and environmental constraints.
The Galileo HAS User Algorithm [15] is a real-time PPP algorithm that processes
the corrections delivered by Galileo HAS Initial Service (orbit/clock corrections and only
code biases) and calculates position and velocity referred to the GTRF (Galileo Terrestrial
Reference Frame), time-stamped with respect to the GST (Galileo System Time). It uses
Galileo L-Band observables and, in the case of a multi-constellation configuration, GPS
L-Band observables as well. The Galileo HAS User Algorithm estimation technique is an
Extended Kalman filter (EKF) with state predictions and state updates to improve conver-
gence and accuracy as it finds an optimum trade-off between measurement model and
state space model by minimizing the variance of the updated states. The User Algorithm
processing follows an uncombined, satellite-to-satellite single-differenced (SD) processing.
The algorithm has preprocessing steps including outlier detection and elimination of single
satellite failure for each GNSS constellation with RAIM/DIA and of detection and elim-
ination of complete GNSS constellation outages. Preprocessing also addresses cycle slip
detection and correction by using time-differenced Melbourne–Wübbena combination and
ionosphere-free phase combination. With this set of techniques, the proposed UA provides
robustness to different fault behaviors on the site of satellites, the level of the correction
service, and of the receiver and its environment.
Previous work on the Galileo HAS user performance from other developments and
using different algorithms can be found in [16–19].
2.2. Operations
Figure 2 presents the position of ILV Granuaile at 0.00 h UTC every day throughout
the campaign, which ran from 19 July to 16 August 2023 (days 1–29), and the route followed
by the vessel during this period.
The User Terminal was activated on 19 July 2023 in Dun Laoghaire and turned off
in Killibegs on 17 August. Spaceopal monitored the User Terminal operations daily and
uploaded data to the FTP server. Initially, the User Terminal was configured to operate at
1 Hz sampling rate and elevation mask of 5 degrees in Galileo E1/E5a + GPS L1/L2C mode.
On 3 August, the operating mode was changed to Galileo E1/E5a/E6-B + GPS L1/L2C,
and the User Terminal was restarted at 15.00 UTC on that day.

<!-- PAGE: 6 -->

J. Mar. Sci. Eng. 2023, 11, 2375
6 of 13
 
Figure 2. ILV Granuaile position at 0.00 h UTC every day and the route followed.
2.3. Reference Trajectory
The vessel’s reference trajectory was calculated using NovAtel GrafNav post-processing
software (version 8.90) [20]. GrafNav was configured in kinematic differential mode, and
data was processed in both forward and backward directions. The software was supplied
with raw GNSS observables from the Galileo HAS User Terminal and selected reference
stations within the HxGN SmartNet network. Typical baseline lengths were suboptimal,
averaging around 40 km but occasionally extending up to 65 km. The GrafNav processing
was performed by GRAD.
2.4. Performance Metrics
The Galileo HAS position calculated by the Galileo HAS User Terminal was compared
to the reference trajectory position for each epoch calculated using GrafNav. The differences
in the horizontal and vertical position in the local tangent plane are the horizontal and
vertical position error for each epoch, respectively. Table 3 identifies and defines the
performance metrics [1] relevant to the campaign.

> [1 Figure(s)]

<!-- PAGE: 7 -->

J. Mar. Sci. Eng. 2023, 11, 2375
7 of 13
Table 3. Performance metrics.
Performance Metrics
Definition
Position error
Defined as the instantaneous difference between the reference horizontal
(respectively vertical) position and the horizontal (respectively vertical) position
estimated by the user receiver at any time after convergence has been achieved.
Horizontal/vertical position accuracy
Defined as statistical characterization of the position horizontal error (respectively
vertical) over a reference period of time.
Position availability
Defined as percentage of time, over a specified reference period, during both
horizontal and vertical position error remain below predefined thresholds.
3. Results
The accuracy results for the tests in this article are a comparison between the real-time
position (XYZ coordinates) delivered by the Galileo User Terminal (stored in files) with
the postprocessing coordinates from the reference trajectory. The difference between the
reference and real time positions projected to the horizontal tangent plane of the reference
position is the horizontal error and the difference projected to the vertical plane is the
vertical error. A characterization of the 68% and 95% percentile is performed for both
horizontal and vertical errors to obtain the horizontal and vertical accuracy.
3.1. Performance Results
Table 4 presents the results of the position accuracy assessment. The performance
targets were initially defined based on the information in the Galileo HAS info note [2],
specifying a requirement of 0.20 m (95%) for horizontal accuracy and 0.40 m (95%) for
vertical accuracy. Additionally, a second performance level was defined, with requirements
of 0.15 m (68%) for horizontal accuracy and 0.20 m (68%) for vertical accuracy, as described
in the Galileo HAS SDD [1].
Table 4. Position accuracy in meters using Galileo HAS.
Date
Granuaile Location
at 0.00 UTC
Horizontal 68% (m)
Vertical 68% (m)
Horizontal 95% (m)
Vertical 95% (m)
20 July 2023
Dun Laoghaire
0.13
0.14
0.2
0.28
21 July 2023
Dun Laoghaire
0.16
0.13
0.30
0.32
22 July 2023
Kilmore Quay
0.12
0.19
0.26
0.44
23 July 2023
Bere Island
0.09
0.12
0.19
0.26
24 July 2023
Bere Island
0.17
0.2
0.38
0.41
25 July 2023
Ballingskelig Bay
0.18
0.28
0.31
0.60
26 July 2023
Mouth of Shannon
estuary
0.14
0.19
0.22
0.40
27 July 2023
Aran Islands
0.13
0.16
0.29
0.38
28 July 2023
Aran Islands
0.15
0.26
0.30
0.49
29 July 2023
Aran Islands
0.15
0.23
0.25
0.50
30 July 2023
Aran Islands
0.12
0.20
0.21
0.33
31 July 2023
Clew Bay
0.16
0.20
0.38
0.65
1 August 2023
Clew Bay
0.15
0.21
0.26
0.46
2 August 2023
Clew Bay
0.18
0.15
0.58
0.43
4 August 2023
Mouth of Shannon
Estuary
0.14
0.28
0.27
0.5
5 August 2023
Foynes
0.12
0.20
0.21
0.29

<!-- PAGE: 8 -->

J. Mar. Sci. Eng. 2023, 11, 2375
8 of 13
Table 4. Cont.
Date
Granuaile Location
at 0.00 UTC
Horizontal 68% (m)
Vertical 68% (m)
Horizontal 95% (m)
Vertical 95% (m)
6 August 2023
Mouth of Shannon
Estuary
0.19
0.18
0.31
0.43
7 August 2023
Aran Islands
0.13
0.14
0.18
0.39
8 August 2023
Aran Islands
0.16
0.16
0.28
0.38
9 August 2023
Inishkea Islands
0.13
0.16
0.22
0.38
10 August 2023
Broadhaven bay
0.13
0.18
0.26
0.43
11 August 2023
Sligo
0.16
0.20
0.39
0.5
12 August 2023
Sligo
0.18
0.18
0.29
0.45
13 August 2023
Sligo
0.18
0.22
0.52
0.51
14 August 2023
Killibegs
0.12
0.09
0.22
0.22
15 August 2023
Killibegs
0.13
0.11
0.24
0.21
16 August 2023
Killibegs
0.08
0.09
0.18
0.19
All days
0.14
0.17
0.29
0.42
The User Terminal was initially configured to operate in Galileo E1/E5a + GPS L1/L2C
mode, starting from 19 July. On 3 August, the operating mode was changed to Galileo
E1/E5a/E6-B + GPS L1/L2C. These two days have been excluded from the assessment to
mitigate the impact of the convergence process. However, it is important to note that the
results presented in this section include periods of suspected external RF interference, as
described further below.
Table 5 presents the position availability results from the campaign. Two sets of
thresholds were selected in line with the accuracy targets introduced previously. The
results have not been modified to remove any possible external Radio Frequency (RF)
interference effects.
Table 5. Position availability using Galileo HAS.
Date
Granuaile Location at 0.00 UTC
Position Availability %
H 0.2 m V 0.4 m
Position Availability %
H 0.15 m V 0.20 m
20 July 2023
Dun Laoghaire
94
64
21 July 2023
Dun Laoghaire
76
54
22 July 2023
Kilmore Quay
86
58
23 July 2023
Bere Island
96
85
24 July 2023
Bere Island
71
51
25 July 2023
Ballingskelig Bay
62
36
26 July 2023
Mouth of Shannon estuary
89
53
27 July 2023
Aran Islands
81
62
28 July 2023
Aran Islands
75
41
29 July 2023
Aran Islands
83
45
30 July 2023
Aran Islands
92
61
31 July 2023
Clew Bay
77
52
1 August 2023
Clew Bay
78
50
2 August 2023
Clew Bay
67
49
4 August 2023
Mouth of Shannon Estuary
76
39

<!-- PAGE: 9 -->

J. Mar. Sci. Eng. 2023, 11, 2375
9 of 13
Table 5. Cont.
Date
Granuaile Location at 0.00 UTC
Position Availability %
H 0.2 m V 0.4 m
Position Availability %
H 0.15 m V 0.20 m
5 August 2023
Foynes
94
72
6 August 2023
Mouth of Shannon Estuary
69
45
7 August 2023
Aran Islands
94
66
8 August 2023
Aran Islands
80
56
9 August 2023
Inishkea Islands
89
63
10 August 2023
Broadhaven bay
84
55
11 August 2023
Sligo
81
47
12 August 2023
Sligo
77
48
13 August 2023
Sligo
66
39
14 August 2023
Killibegs
91
73
15 August 2023
Killibegs
89
68
16 August 2023
Killibegs
97
89
All days
81
55
3.2. Analysis of Results
In order to evaluate the goodness of the accuracy performance in Table 4, results are
compared to the performance targets of 0.15 m (68%) for horizontal accuracy and 0.20 m
(68%) for vertical accuracy described in Table 2. When considering all epochs for all days
together, the 68% horizontal accuracy is 0.14 m and 68% vertical accuracy is 0.17 m 68%.
Both values meet their respective performance targets in Table 2 even if the performance
targets are specified for static users. This indicates positive overall accuracy results and
margin for users in the existing performance targets for Galileo HAS Initial Service. Table 4
also presents results compared to the 0.20 m (95%) for horizontal accuracy and 0.40 m (95%)
for vertical accuracy described in Table 1 for the future Galileo HAS full service Level 1
and Level 2. In this case, results are slightly over the threshold reaching 0.29 m horizontal
95% and 0.42 m vertical 95%. These values are not committed for the current phase (Initial
Service), but for the full service of Galileo HAS to be rolled out in the future.
Even if the overall accuracy results are positive, an analysis of the instantaneous
horizontal and vertical position error was required, because errors presented 6 h periodic
heavy degradations with eventual loss of the position for a few seconds, as in Figure 3.
A first investigation indicated that, every day, at approximately 0.50 UTC, 6.50 UTC,
12.50 UTC and 18.50 UTC, the User Terminal observations were interrupted for a few
seconds for GNSS bands L1 and L2, but not for L5. Having discarded any issues in the
User Terminal and the Galileo HAS corrections through the nominal equipment checks and
correction analysis, the most likely cause was coming from an external source onboard. As
a cargo vessel with a gross tonnage exceeding 300 tons, ILV Granuaile is required to carry
Long Range Identification and Tracking (LRIT) equipment. The LRIT system enables global
vessel identification and tracking, enhancing shipping security and contributing to safety
and marine environment protection.
Shipborne LRIT equipment transmits within the 1600 MHz to 1630 MHz frequency
band, which is close to the GPS/Galileo L1/E1 band (centred at 1575.42 MHz), and it
operates at a power level exceeding 1.5 W. These transmissions occur every six hours.
Every day at approximately 0.50 UTC, 6.50 UTC, 12.50 UTC and 18.50 UTC, the User
Terminal observations were interrupted for a few seconds.

<!-- PAGE: 10 -->

J. Mar. Sci. Eng. 2023, 11, 2375
10 of 13
Figure 3. Real-time User Terminal accuracy vs. time using Galileo HAS corrections for 26 July 2023.
Periodic degradation occurs every 6 h.
The LRIT antenna is mounted 2.5 m below the GNSS antenna used in the campaign.
The recommended separation distance between an LRIT antenna and any GNSS antenna is
30 m. While it is not confirmed that LRIT is responsible for the interference events, there is
a high likelihood that it is the cause. In Figure 3, the reader can observe an example of the
position degradation occurring every 6 h.
The impact of these events on overall performance is significant, happening every 6 h
and resulting in a notable degradation of position accuracy for an undetermined duration.
Performance is affected not only during the event, but also after it has finished, primarily
because the selected positioning technique for Galileo HAS, Precise Point Positioning,
uses a Kalman filter. These events also impacted the calculation of the reference trajectory
using GrafNav.
The test campaign results demonstrate the performance of the Galileo HAS User
Terminal including the adverse effects of the high-power interference likely originating
from the LRIT system antenna onboard the vessel. Table 6 shows the results after removing
1-hour periods at 0.50 h, 6.50 h, 12.50 h and 18.50 h to mitigate the impact of the interference,
classified according to the different phases of navigation. The 1 h removal cannot completely
remove the impact of interference because the selected positioning technique for Galileo
HAS, Precise Point Positioning, uses an Extended Kalman filter (EKF) and effects are carried
over until a device restart.
Table 6. Accuracy and position availability vs. type of navigation removing 1-h periods at interfer-
ence epochs.
68% Accuracy
Horizontal
68% Accuracy
Vertical
95% Accuracy
Horizontal
95% Accuracy
Vertical
Position
Availability %
H 0.15 m V 0.20 m
Position
Availability %
H 0.20 m V 0.40 m
Anchored
0.13
0.14
0.22
0.34
67
90
Coastal
0.12
0.16
0.26
0.38
60
86
Open Sea
0.17
0.15
0.30
0.36
52
75
All
0.13
0.15
0.25
0.36
61
86

> [1 Figure(s)]

<!-- PAGE: 11 -->

J. Mar. Sci. Eng. 2023, 11, 2375
11 of 13
Results in Table 5 present the position availability results from the campaign. The
very same two sets of thresholds were selected in line with the accuracy targets previously
introduced. The availability for the first threshold (0.15 m horizontal/0.20 m vertical) for all
epochs for all days together is 55% with a minimum of 36% and maximum of 89%, and the
second threshold (0.20 m horizontal/0.40 m vertical) is 81% with a minimum of 62% and
maximum of 97%. The availability values are too dissimilar between days. When looking
into the results, the variation between days seemed to be related to the type of navigation
for each specific day. ILV Granuaile spent several days anchored for the full day, whereas
for others it was navigating through coastal waters or open sea. The results indicate
better performance in scenarios involving slow motion, which is of particular relevance for
mooring and pilotage applications. Values for these slow-dynamics applications reach a
horizontal accuracy of 0.22 m 95% and 0.13 m 68%.
It is acknowledged that the variations in estimated performance seen in Table 6 may
in part be related to the vessel’s distance from the HxGN SmartNet station(s).
4. Discussion
This article presented the results of the first Galileo HAS testing campaign conducted
at sea using a buoy-laying vessel temporarily equipped with a Galileo HAS User Terminal.
Whereas GNSS standalone and augmentation have been used in marine navigation for a
long period of time, the operational declaration of Galileo HAS in January 2023 opens new
opportunities for decimeter level applications.
In this test campaign, results were particularly impacted by onboard vessel interfer-
ence, but even under this harsh radio frequency environment, the accuracy reached the
performance targets stated in the Galileo HAS SDD [1].
The overall satisfaction with accuracy and availability results is fostered when it is
considered the negative impact of the high-power interference likely generated by LRIT
equipment onboard the vessel. LRIT broadcasts, occurring daily at 0.50 h, 6.50 h, 12.50 h and
18.50 h, were comparatively strong, with the LRIT antenna located just 2.5 m from the GNSS
antenna making mitigation challenging. One significant feature of the underlying Galileo
HAS positioning algorithm is the need of a continuous flow of GPS and Galileo observations,
otherwise the EKF is restarted. Restarts imply positioning solution convergence periods
during which accuracy is degraded compared to steady-state situations. Even on this
environment, values for horizontal accuracy reached 0.29 m 95% and 0.14 m 68%. The
article also presents better values after removing interference periods when horizontal
accuracy reached 0.22 m 95% and 0.13 m 68%. These results are in line with the expectations
outlined in the Galileo HAS Service Definition Document (SDD). Future work shall ensure
RF interference-free environments.
The article provided additional assessments for different phases of navigation, demon-
strating better performance in slow-motion scenarios, particularly relevant to mooring and
pilotage applications.
The Galileo HAS will evolve in the near future to Phase 1, meeting full performance
targets, and subsequently to Phase 2, introducing additional corrections in Europe. This will
enable enhanced performance. Furthermore, fine-tuning receiver algorithms for maritime
applications, with specific assumptions for the EKF, may bring significant improvement.
Author Contributions: Conceptualization: M.L.-M., P.P. and E.G.; Materials and methods: P.P., J.S.
and R.B.; Results: P.P. and J.S.; Review and editing: M.L.-M., P.P. and E.G. All authors have read and
agreed to the published version of the manuscript.
Funding: The work by Spaceopal was executed in the frame of the Galileo Adoption Plan 2023 as
part of the Galileo Service Operator (GSOp) framework contract funded by European Union Agency
for the Space Program (contract GSA/CD/14/14).
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.

<!-- PAGE: 12 -->

J. Mar. Sci. Eng. 2023, 11, 2375
12 of 13
Data Availability Statement: Data used for the preparation of this paper is available for free. Please
contact the corresponding author in case you would like to access the raw data.
Acknowledgments: The authors would like to thank Commissioners of Irish Lights for permitting
the installation of equipment on the ILV Granuaile.
Conflicts of Interest: M.L. is an employee of European Union Agency for the Space Program. P.P.,
E.G are employed by Spaceopal GmbH. J.S. and R.B. declare no conflict of interest.
Notes
1
General Lighthouse Authorities of the UK and Ireland.
References
1.
European Union. Galileo High Accuracy Service-Service Definition Document (HAS SDD), Issue 1.0. Available online: https:
//www.gsc-europa.eu/sites/default/files/sites/all/files/Galileo-HAS-SDD_v1.0.pdf (accessed on 1 September 2023).
2.
European Union. Galileo High Accuracy Service–Info Note, Issue 1.0. Available online: https://www.gsc-europa.eu/sites/
default/files/sites/all/files/Galileo_HAS_Info_Note.pdf (accessed on 1 September 2023).
3.
European Union. Galileo High Accuracy Service–Signal-in-Space Interface Control Document (HAS SiS ICD), Issue 1.0. Avail-
able online: https://www.gsc-europa.eu/sites/default/files/sites/all/files/Galileo_HAS_SIS_ICD_v1.0.pdf (accessed on 1
September 2023).
4.
European Union. Galileo High Accuracy Service-Internet Data Distribution Interface Control Document (HAS IDD ICD), Issue 1.0.
Available online: https://www.gsc-europa.eu/galileo/services/galileo-high-accuracy-service-has/internet-data-distribution-
registration-form (accessed on 1 September 2023).
5.
European Union. Galileo Open Service-Service Definition Document (OS SDD), Issue 1.2. Available online: https://www.gsc-
europa.eu/sites/default/files/sites/all/files/Galileo-OS-SDD_v1.3.pdf (accessed on 1 September 2023).
6.
Department of Defence, USA. Global Positioning System Standard Positioning Service Performance Standard (GPS SPS), 5th ed.;
Department of Defence: Washington, DC, USA, 2020.
7.
European Union. European GNSS (Galileo) Services–Open Service–Quarterly Performance Report April June 2023, Issue 1.0.
Available online: https://www.gsc-europa.eu/electronic-library/performance-reports/galileo-open-service-os (accessed on 1
September 2023).
8.
Renfro, B.A.; Stein, M.; Reed, E.B.; Villalba, E. An Analysis of Global Positioning System Standard Positioning Service Performance for
2020; Space and Geophysics Laboratory Applied Research Laboratories; The University of Texas at Austin: Austin, TX, USA, 2020.
Available online: https://www.gps.gov/systems/gps/performance/ (accessed on 1 September 2023).
9.
European Union. European GNSS (Galileo) Services–High Accuracy Service (HAS)–Quarterly Performance Report April June
2023, Issue 1.0. Available online: https://www.gsc-europa.eu/electronic-library/performance-reports/galileo-high-accuracy-
service-has (accessed on 1 September 2023).
10.
Pandele, A.; Croitoru, A.; Hulea, A.; Costel, C.; Radutu, A.; Porretta, M.; Buist, P.J.; Andrescu, D.; Dutu, L.; Dragasanu, C.; et al.
Galileo and GPS Performances in the Maritime Environment. In Proceedings of the 33rd International Technical Meeting of the
Satellite Division of The Institute of Navigation (ION GNSS+ 2020), Online, 22–25 September 2020; pp. 896–919.
11.
Morán, J.; Lacarra, E.; Vázquez, J.; Sánchez, M.A.; Cantos, F.; Horváth, T. EDAS for a DGPS Maritime Service: EGNOS Based VRS
Performance with Pre-Broadcast Integrity Monitoring. In Proceedings of the 29th International Technical Meeting of the Satellite
Division of The Institute of Navigation (ION GNSS+ 2016), Portland, OR, USA, 12–16 September 2016; pp. 3481–3493.
12.
González, R.; Lacarra, E.; López, M.; Heikonen, K. EGNOS Performance Along Finnish Coast. TransNav. Int. J. Mar. Navig. Saf.
Sea Transp. 2021, 15, 551–556. [CrossRef]
13.
Tegedor, J.; Ørpen, O.; Melgard, T.; Łapucha, D.; Visser, H. G4 Multi-constellation Precise Point Positioning Service for High
Accuracy Offshore Navigation. TransNav. Int. J. Mar. Navig. Saf. Sea Transp. 2017, 11, 425–429. [CrossRef]
14.
Commissioners of Irish Lights. Available online: www.irishlights.ie (accessed on 1 September 2023).
15.
González, E.; Pintor, P.; Senado, A.; Dhital, N.; Ostolaza, J.; Hernández, C.; de Blas, J. Galileo High Accuracy Service (HAS)
Algorithm and Receiver Development and Testing. In Proceedings of the 35th International Technical Meeting of the Satellite
Division of The Institute of Navigation (ION GNSS+ 2022), Denver, CO, USA, 19–23 September 2022; pp. 836–851.
16.
Pintor, P.; González, E.; Bohlig, P.; Sperl, A.; Ostolaza, J.; Hernández, C.; Vazquez, J.; de Blas, J.; Lagrasta, S. Testing the Galileo
High Accuracy Service (HAS) User Terminal. In Proceedings of the 2023 European Navigation Conference (ENC 2023), Noordwijk,
The Netherlands, 31 May–2 June 2023.
17.
Fernandez-Hernandez, I.; Chamorro-Moreno, A.; Cancela-Diaz, S.; Calle-Calle, J.D.; Zoccarato, P.; Blonski, D.; Senni, T.;
de Blas, F.J.; Hernández, C.; Simón, J.; et al. Galileo high accuracy service: Initial definition and performance. GPS Solut. 2022,
26, 65. [CrossRef]
18.
Chamorro, A.; Cancela, S.; García, A.J.; Calle, D.; Fernández-Hernández, I.; de Blas, F.J.; Hernández, C. Early Demonstration
of Galileo HAS User Performances. In Proceedings of the 35th International Technical Meeting of the Satellite Division of The
Institute of Navigation (ION GNSS+ 2022), Denver, CO, USA, 19–23 September 2022; pp. 828–835.

<!-- PAGE: 13 -->

J. Mar. Sci. Eng. 2023, 11, 2375
13 of 13
19.
Naciri, N.; Yi, D.; Bisnath, S.; de Blas, F.J.; Capua, R. Assessment of Galileo High Accuracy Service (HAS) test signals and
preliminary positioning performance. GPS Solut. 2023, 27, 73. [CrossRef] [PubMed]
20.
Novatel. A NovAtel Precise Positioning Product. In Waypoint Software 8.90 User Manual; Revision v10; NovAtel Inc.: Calgary, AB,
Canada, 2020.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
