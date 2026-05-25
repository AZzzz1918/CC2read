<!-- PAGE: 1 -->

Academic Editor: Nathan J. Moore
Received: 12 June 2025
Revised: 14 July 2025
Accepted: 17 July 2025
Published: 18 July 2025
Citation: Zhou, L.; Zhang, E.; Liang,
H.; Hu, Z.; Qu, M.; Li, X.; Cao, Y.
Practical Performance Assessment of
Water Vapor Monitoring Using BDS
PPP-B2b Service. Appl. Sci. 2025, 15,
8033. https://doi.org/10.3390/
app15148033
Copyright: © 2025 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license
(https://creativecommons.org/
licenses/by/4.0/).
Communication
Practical Performance Assessment of Water Vapor Monitoring
Using BDS PPP-B2b Service
Linghao Zhou 1,2
, Enhong Zhang 3, Hong Liang 1
, Zuquan Hu 1,4, Meifang Qu 1,5, Xinxin Li 1,6
and Yunchang Cao 1,*
1
Meteorological Observation Centre, China Meteorological Administration, Beijing 100081, China
2
School of Electronic Information Engineering, Beihang University, Beijing 100191, China
3
Guangdong Meteorological Data Centre, Guangzhou 510080, China
4
LaiBin Meteorological Agency of Guangxi Zhuang Autonomous Region, Laibin 546100, China
5
Guangxi Meteorological Observatory, Nanning 530022, China
6
Guangxi Meteorological Technology Equipment Center, Nanning 530022, China
*
Correspondence: caoyc@cma.gov.cn
Abstract
BeiDou navigation satellite system (BDS) precise point positioning (PPP)-B2b has signif-
icant potential for application in meteorological fields, such as standalone water vapor
monitoring in depopulated area without Internet. In this study, the practical ability of water
vapor monitoring using the BDS PPP-B2b service is illustrated through a continuously
operated water vapor monitoring system in Wuhan, China, with a 25-day experiment in
2025. Original observations from the Global Positioning System (GPS) and BDS are col-
lected and processed in the near real-time (NRT) mode using ephemeris from the PPP-B2b
service. Precipitable water vapor PWV monitored with B2b ephemeris are evaluated with
radiosonde and ERA5 reanalysis, respectively. Taking PWV from radiosonde observations
as the reference, RMS of PWV based on B2b ephemeris varies from 3.71 to 4.66 mm for
different satellite combinations. While those values are with a range from 3.95 to 4.55 mm
when compared with ERA5 reanalysis. These values are similar to those processed with
the real-time ephemeris from the China Academy of Science (CAS). In general, this study
demonstrates that the practical accuracy of water vapor monitored based on the BDS PPP-
B2b service can meet the basic demand for operational meteorology for the first time. This
will provide a scientific reference for its wide promotion to meteorological applications in
the near future.
Keywords: BeiDou navigation satellite system (BDS); zenith tropospheric delay (ZTD);
precipitable water vapor (PWV); precise point positioning (PPP)
1. Introduction
Water vapor is as an important meteorological parameter in the atmosphere and plays
a significant role in weather processes [1–3]. The transport, convergence, and variation
characteristics of water vapor are directly related to the intensity and distribution of precip-
itation [4–6]. With the continuous development of meteorological observation techniques,
many methods for water vapor retrieval are established, including radiosonde, microwave
radiometer, spectrometer, and so on. Among them, water vapor derived from the global
navigation satellite system (GNSS) has attracted widespread attention due to its good
accuracy and working ability for all-weather conditions [7–9].
Appl. Sci. 2025, 15, 8033
https://doi.org/10.3390/app15148033

<!-- PAGE: 2 -->

Appl. Sci. 2025, 15, 8033
2 of 15
Theoretically, GNSS signals will be affected by the atmosphere in the troposphere
when transmitting from satellites to receivers, resulting in the zenith tropospheric delay
(ZTD) [10]. ZTD usually consists of the zenith hydrostatic delay (ZHD) caused by dry
atmosphere and the zenith wet delay (ZWD) caused by water vapor. The principle of
GNSS water vapor retrieval is to obtain the wet part and convert it to the precipitable
water vapor (PWV) with the help of related meteorological observations. This technique
has been developed since 1990s and continuously improved [11,12]. The accuracy of
GNSS-PWV has been proved to be about 2 mm for post-processing mode compared with
water vapor from multiple techniques (e.g., [13–15]). At present, water vapor retrieved
from the mainstream navigation systems (including the Global Positioning System (GPS),
Galileo, BeiDou navigation satellite system (BDS), and GLONASS (Global Navigation
Satellite System)) has greatly contributed to both meteorological operations and research
(e.g., [16–20]).
To better meet the requirements of operational meteorology for the timeliness of water
vapor monitoring, real-time (RT) or near real-time (NRT) GNSS water vapor retrieval have
been proposed, which utilizes the real-time products from the Real-Time Service (RTS) of
the International GNSS Services (IGS). The accuracy of PWV from RT/NRT data processing
mode based on the precise point positioning (PPP) technique is slightly worse than that
from post-processing mode. In general, the accuracy of RT/NRT PWV estimated using
different satellite ephemeris is about 3 to 5 mm compared to the reanalysis products among
different regions around the globe [21–23]. This can meet the general requirement of water
vapor accuracy for meteorological applications [24,25].
The real-time products from the IGS RTS are generally provided through the real-time
data streams via the Internet. This not only increases the instability and error of water
vapor monitoring due to the network fluctuations but also raises the requirements of
equipment for data processing. In contrast, the corrections to orbit and clock offset of BDS
PPP-B2b service are broadcasted by three BDS-3 Geostationary Earth Orbit (GEO) satellites
(i.e., C59–C61) and can be received and decoded by receivers [26]. This makes it possible
to real-time GNSS water vapor monitor at a standalone station, which is not dependent
on the Internet, which can better compensate the sparse observation for depopulated
area. Recently, some researchers have conducted water vapor retrieval using the PPP-
B2b products (e.g., [27,28]). Results show that the performance of PWV from the PPP-
B2b service can achieve about 4 mm compared to reanalysis products [29,30], which is
generally consistent with those from traditional IGS RTS products [31]. This manifests
the feasibility of further application of water vapor derived from the PPP-B2b service in
meteorological fields.
However, current studies about water vapor monitoring using the PPP-B2b service
are generally conducted based on simulated real-time PPP mode (i.e., post-processing
using real-time products), while its practical performance remains unclear. In operational
meteorology, water vapor monitoring should be conducted continuously and automatically
with experiment and testing in practical situation. Therefore, current studies based on
simulated real-time processing cannot fully provide robust reference for assessing the
performance of the PPP-B2b service for water vapor monitoring. In this regard, evaluating
the actual performance of water vapor monitoring based on the BDS-PPP B2b service is
of vital importance before its wide promotion. To achieve this purpose, a continuously
operated water vapor monitoring system (here after called monitoring system), which
consist of a GNSS receiver and an Industrial Personal Computer (IPC), was established in
Wuhan, China. This monitoring system was operated same as other meteorological stations
automatically in practical situation. Based on observations of 25 days, PWV data retrieved
in NRT mode were evaluated to veritably illustrate the ability of water vapor monitoring

<!-- PAGE: 3 -->

Appl. Sci. 2025, 15, 8033
3 of 15
using the PPP-B2b service. The conclusion of this paper is expected to provide scientific
reference for developing future water vapor observation platforms.
2. Data Description
Data utilized in this study includes three parts, i.e., the GNSS observations, GNSS
satellite ephemeris, and the ERA5 reanalysis.
2.1. GNSS Observations
The original code and phase observations from the GPS and BDS satellites are collected
by the antenna and receiver, which are parts of the monitoring system, as shown in Figure 1.
To be specific, the Leica AR20 multi-GNSS antenna (Leica Geosystems AG, Heerbrugg,
Switzerland) is placed on the roof without being blocked by the surroundings, and the
receiver is the Hexagon FangZhou receiver (Hexagon Geosystems (Qingdao) Co., Ltd.,
Qingdao, China), which can decode signals from both GPS and BDS satellites. The GNSS
observation will be transferred to the IPC, in which the raw data will be stored and
processed through the NRT processing mode for water vapor monitoring.
(a) 
(b) 
Figure 1. The installation environment of the antenna (a) and Hexagon FangZhou receiver (b), which
are part of the water vapor monitoring system.
2.2. GNSS Satellite Ephemeris
Satellite ephemeris in this study include three products. First, orbit and clock offset
corrections provided by the BDS PPP-B2b service are directly captured and decoded by
the Hexagon FangZhou receiver in the State Space Representation (SSR) format. The B2b
ephemeris can be obtained with the combination of SSR and navigation message. Second,
the final multi-GNSS ephemeris from Wuhan University (WUM) are collected and applied
for the post-processing [32], which will serve as the reference for the following evaluation.
In addition, the real-time multi-GNSS ephemeris generated by the China Academy of
Science (CAS) are also collected and applied for processing for comparison [33]. Except for
the B2b ephemeris, satellite products from WUM and CAS can both be obtained from the
IGS (https://igs.org/products/#about, accessed on 12 June 2025).
2.3. ERA5 Reanalysis
The fifth generation ECMWF reanalysis (ERA5) in pressure-level format is employed
in this study. It can provide meteorological variables for 37 specific pressure levels from
the earth’s surface to about 80 km [34]. The specific humidity of ERA5 reanalysis will
be integrated into PWV for water vapor accuracy assessment in this study. The detailed
method for the integration process can be found in [35]. The ERA5 reanalysis can be
downloaded from the Climate Data Store (CDS) via https://cds.climate.copernicus.eu/
datasets/reanalysis-era5-pressure-levels?tab=overview (accessed on 12 June 2025).

> [4 Figure(s)]

<!-- PAGE: 4 -->

Appl. Sci. 2025, 15, 8033
4 of 15
3. Methodology
This section detailly describes the methods used for the evaluation experiments,
including the GNSS data processing and the following performance evaluation process. A
general flow chart of this experiment is presented in Figure 2 as follows.
 
Figure 2. Flowchart of the experiment methodology.
3.1. GNSS Data Processing
To achieve the monitoring of water vapor based on GNSS observations, the PPP tech-
nique is applied for processing the original code and phase observations from GPS and
BDS. There are two processing modes included in this study, i.e., the post-processing mode
and NRT processing mode. The post-processing mode is to conventionally process GNSS
observations with final satellite ephemeris (e.g., WUM) on a daily basis (24 h processing
length). It is widely employed for generating ZTD products (e.g., [36]). The detailed
strategies for post-processing mode are given in Table 1. The priori values for tropospheric
parameters are obtained from the Saastamoinen model [37] and the Global Pressure and
Temperature 3 (GPT3) [38]. The Vienna Mapping Function 3 (VMF3) is adopted for map-
ping the tropospheric delay from the zenith direction to the slant signal paths [38]. All
observations are processed with the interval of 30 s, and the tropospheric parameters are
estimated every 3600 s.

> [1 Figure(s)]

<!-- PAGE: 5 -->

Appl. Sci. 2025, 15, 8033
5 of 15
Table 1. GNSS data processing strategies for the post-processing model and NRT processing mode.
Title 1
Post-Processing Mode
NRT Processing Mode
Data length for processing
24 h
6 h window
Processing interval
30 s
30 s
Satellite ephemeris
WUM
WUM (for verification)
CAS or B2b (for evaluation)
Estimator
Least-squares (LSQ) + backward smoothing
Tropospheric priori model
Saastamoinen + GPT3
Mapping function
VMF3
Stochastic model for ZTD
Estimated as piece-wise constant every 3600 s with random walk process
between pieces (20 mm/sqrt(h))
Horizontal tropospheric
gradients
Estimated as constant
Receiver coordinates
Tightly constrained to double-differenced solutions
Receiver clock offsets
Estimated as white noise
Ambiguity
Estimated as arc-constant
Different from the post-processing mode, the NRT processing mode only adopts 6 h
data for each processing to estimate ZTD for the final epoch. The length of 6 h is selected due
to the consideration for both ZTD and ambiguity convergence [39]. The general schematic
diagram for the NRT processing mode is shown as Figure 3. Apart from the data length,
the key difference between two modes is the satellite ephemeris. The NRT mode applies
two RT ephemeris (i.e., CAS and B2b) for data processing to achieve timeliness for water
vapor monitoring. The processing software is secondary developed on the basis of the
Geodetic SpatioTemporal data Analysis and Research (GSTAR) software (v.1.0) developed
by Beihang University [40]. It is installed on the IPC of the monitoring system and will be
launched every hour for water vapor monitoring.
Figure 3. The general schematic diagram for the NRT processing mode.
3.2. PWV Conversion Based on Estimated ZTD
To achieve the water vapor monitoring based on GNSS technique, the conversion of
PWV from the estimated ZTD will be conducted after GNSS data processing. First, the
ZHD is calculated through the Saastamoinen model and the in-situ pressure observations
from the monitoring system, as follows:
Zh =
2.279 ± 0.0024
1 −0.00266cos(2φ) −0.00028h × P
(1)

> [1 Figure(s)]

<!-- PAGE: 6 -->

Appl. Sci. 2025, 15, 8033
6 of 15
where Zh represents the ZHD, φ and h are the latitude and height of GNSS antenna, and
P is the pressure measurement in hPa unit. Afterwards, the ZWD can be obtained after
removing ZHD from the estimated ZTD. Finally, PWV can be converted with ZWD (Zw)
and the conversion factor as follows:
Wg = Π × Zw =
106
ρwRV( k3
Tm + k′
2)
× Zw
(2)
where Wg represents PWV converted from ZWD (Zw) and the conversion factor (Π). ρw
and RV are the density of liquid water and universal gas constant for wet air. k′
2 and k3
represent coefficients of atmospheric refractivity. Tm is the weighted mean temperature,
which can be calculated through the air temperature measurement and linear coefficient
from Yao et al. (2014) [41].
4. Results and Discussion
To analyze the practical applicability of the BDS PPP-B2b service in water vapor
monitoring, ZTD and PWV retrieved from the monitoring system for a total of 25 days from
day-of-year (DOY) 076 to 100 in 2025 are analyzed in this section. Firstly, the consistency of
NRT processing mode and post-processing mode for ZTD estimation are firstly verified.
Subsequently, to analyze the performance of the PPP-B2b service, ZTD estimated from
two RT ephemeris (i.e., CAS and PPP-B2b) based on NRT processing mode are evaluated
through comparison with post-processed ZTD. Finally, the accuracy of PWV from the
monitoring system is assessed with that from ERA5 reanalysis to prove the feasibility of
PPP-B2b service in water vapor monitoring.
4.1. Verification of Near Real-Time (NRT) Processing Mode Through Comparison with
Post-Processing Mode
This subsection first verifies the effectiveness of the NRT processing mode adopted by
the monitoring system. To achieve the verification requirements, ZTD estimated from the
post-processing mode using WUM final ephemeris products with GPS-only observations
is adopted as the reference. Afterwards, the original GPS and BDS observations for a
total of 25 days from DOY 076 to DOY 100 in 2025 are consistently processed via the
PPP technique on a daily batch. The processing strategy are exhibited in Table 1. Based
on the consistent strategies for parameter and input data (including GNSS observations
and satellite ephemeris), ZTD time series in 1 h temporal resolution can be obtained for
the entire research period. This guarantees that the comparison between ZTD from NRT
and post-processing mode are generally in accordance, despite the satellite utilization
and processing mode. For satellite utilization, three combinations of satellite systems are
selected, i.e., the GPS-only (G), BDS-only (C), and the combination of GPS and BDS (GC).
The time series of ZTD estimated from different satellite combinations during the entire
research period are shown in Figure 4. In all subplots of Figure 4, the black lines represent
the referenced ZTD time series estimated using WUM final ephemeris in post-processing
mode, while ZTD time series in NRT processing mode for G/C/GC combinations are
illustrated in blue, red, and green, respectively. It can be observed from the figures that
no matter which satellite combination is adopted, ZTD estimated by the NRT processing
mode can be well consistent with the results from the post-processing mode. However,
three time series of ZTD estimated from NRT processing mode are all less smooth than that
from post-processing mode, exhibiting some distinguished outliers. This may be attributed
to the fact that the accuracy of RT ephemeris (i.e., CAS and B2b) is generally worse than
the final ephemeris for some epochs, which influences the accuracy of data processing [8].
Afterwards, two accuracy indicators, i.e., the bias and RMS of ZTD error, are utilized for

<!-- PAGE: 7 -->

Appl. Sci. 2025, 15, 8033
7 of 15
quantification. It shows that the bias of ZTD using GPS-only observation is close to 0.01 mm,
and the corresponding RMS is 6.91 mm. The phenomenon that almost no bias exists is
possibly attributed to the fact that the ZTD reference from the post-processing mode was
also estimated using the GPS-only observation, thus guaranteeing the consistency. This also
partly proves the consistency between the NRT processing mode and the post-processing
mode. In contrast, the estimation result of BDS-only manifests a relatively large bias with
the value of −3.39 mm, manifesting an evident bias between the processing results. This
might be because of the poorly calibrated antenna-related error for the BDS satellites.
According to previous research (e.g., [42,43]), the authors have also discovered that the
significant systemic biases exist for ZTD derived from BDS and GPS constellations. They
attributed this to the poorly calibrated PCO/PCV errors for BDS satellites, which in turn
influences the performance of data processing, while for the GPS and BDS combination,
the bias of ZTD is closer to 0 than that of BDS-only result with the value of −2.15 mm. This
should be because the joint processing after introducing GPS observations can improve
the robustness and accuracy of parameter estimation [8]. ZTD RMS from the combined
GPS and BDS is the smallest with the value of 6.88 mm, revealing a tiny improvement
of about 0.03 mm. This accuracy is basically consistent with previous studies [40]. In
general, the NRT processing mode can obtain comparable ZTD estimation to those from
the post-processing mode. Therefore, the NRT mode implanted on the monitoring system
can be used for water vapor monitoring.
Figure 4. Time series of ZTD estimated from NRT processing model using GPS-only ((a), blue), BDS-
only ((b), red), and GPS and BDS ((c), green) satellite combinations during the entire research period.
The black line in each subfigure represents reference ZTD estimated from post-processing mode.

> [1 Figure(s)]

<!-- PAGE: 8 -->

Appl. Sci. 2025, 15, 8033
8 of 15
4.2. Performance Evaluation of NRT ZTD Estimation from PPP-B2b Service Through Comparison
with Post-Processing Mode
Subsequently, the accuracy of ZTD estimated through the NRT processing mode from
the monitoring system is evaluated to analyze the performance of the PPP-B2b service.
For the same observations, the real-time ephemeris provided by CAS through IGS RTS
and that from the PPP-B2b service were, respectively, adopted in the monitoring system
based on the NRT processing mode. Three satellite combinations including G/C/GC are
applied for ZTD estimation. Figure 5 presents the time series of NRT ZTD estimated using
different RT ephemeris (i.e., CAS and B2b) with different satellite combinations during
the research period. Overall, ZTD results estimated from the CAS and B2b product are
relatively consistent with the reference values. However, compared with the reference
obtained by the post-processing mode, ZTD estimated using two RT ephemeris (CAS and
B2b) has more significant fluctuations and some outlier. This feature is more obvious
for B2b results, which might be due to the relatively lower accuracy of B2b ephemeris
compared with CAS products [44].
Figure 5. Time series of ZTD estimated from NRT processing model using GPS-only (blue), BDS-only
(red), and GPS and BDS (green) satellite combinations based on CAS (a,c,e) and B2b ephemeris (b,d,f)
during the entire research period. The black line in each subfigure represents reference ZTD estimated
from post-processing mode.
The corresponding bias and RMS of ZTD error evaluated by ZTD from the post-
processing mode are summarized in Figure 6, including the NRT processing results with
WUM final ephemeris. Statistics results of accuracy indicators show that the bias of ZTD
estimation for the CAS ephemeris with the satellite combination of GPS-only, BDS-only, and

> [2 Figure(s)]

<!-- PAGE: 9 -->

Appl. Sci. 2025, 15, 8033
9 of 15
GPS and BDS combinations are 0.95, 6.98, and 1.71 mm, respectively, and the corresponding
RMS are 14.18, 22.85, and 16.16 mm, respectively, while these values for B2b ephemeris are
1.64, −6.54, 1.35 mm for bias, and 24.32, 23.34, 21.49 mm for RMS. These numerical results
are basically similar to previous studies [31], that is, ZTD accuracy based on PPP-B2b
service is approximately 20 mm. Although the performance of B2b is slightly worse than
that of CAS products, according to the theory of error propagation [45], the corresponding
PWV accuracy can achieve around 4 mm with PPP-B2b service. This can basically meet the
requirements of real-time water vapor monitoring for meteorological applications [24].
Figure 6. The bias (a) and RMS (b) of ZTD estimation from NRT processing mode using different
ephemeris (WUM, CAS, and B2b) with different satellite combinations (G, C, and GC).
4.3. Performance Evaluation of NRT PWV Monitoring from PPP-B2b Service Through
Comparison with ERA5 Reanalysis
Finally, the accuracy of PWV monitored through NRT processing mode from the
monitoring system are evaluated to verify the practical effectiveness of the PPP-B2b service
for water vapor monitoring. PWV is converted using ZTD and in situ meteorological
observations from the monitoring system with the method described in Section 3. Different
from ZTD, the assessment of PWV was conducted using that from the radiosonde observa-
tions from the adjacent meteorological stations (with a horizontal distance of about 15 km)
and ERA5 reanalysis products, which has been proven to be a valid external reference
for evaluating water vapor [35,46]. The radiosonde-derived PWV data for the research
period can be directly retrieved from the GNSS meteorological ensemble tools (GMET) [35].
Figure 7 exhibits the scatter plots of PWV retrieved from radiosonde observations (Radio-
PWV) and monitored from two RT ephemeris (i.e., CAS and B2b) with different satellite
combinations during the research period. It can be observed from Figure 7 that PWV from
all combinations reveals consistency with the radiosonde observations. The correlation
coefficients for all combinations are higher than 0.85. For the accuracy indicators, results
show that the bias of PWV monitored based on the B2b ephemeris using the combination
of G, C, and GC satellite combinations are −0.14, −2.21, and 0.14 mm, respectively, and the
corresponding RMS are 3.71, 4.66, and 3.73 mm, respectively, while those values for the
results from B2b ephemeris are 0.20, 1.82, and 0.42mm for bias, and 2.05, 4.31, and 2.41 mm
for RMS. Compared to the B2b results, PWV monitored with CAS ephemeris generally ex-
hibit better accuracy with about 45%, 8%, and 35% for G, C, and GC satellite combinations.
The obviously better accuracy for the G and GC combinations indicates that the quality
of orbit and clock offset for GPS satellite from B2b services are generally lower than those

> [1 Figure(s)]

<!-- PAGE: 10 -->

Appl. Sci. 2025, 15, 8033
10 of 15
from CAS ephemeris. While the general tiny improvements for the BDS-only combinations
reveals that the qualities for BDS satellites from two RT ephemeris are generally consistent.
Despite that the performance of water vapor monitored with B2b ephemeris being worse,
the accuracy is about 3 to 4 mm compared to radiosonde observations, which can be reliably
applied for meteorological research and operations [46].
Figure 7. Scatter plots of PWV retrieved from radiosonde observations and monitored from NRT pro-
cessing model using GPS-only (blue), BDS-only (red), and GPS and BDS (green) satellite combinations
based on CAS (a,c,e) and B2b ephemeris (b,d,f) during the entire research period.
Figure 8 exhibits the time series of PWV monitored through the NRT processing mode
using two RT ephemeris (i.e., CAS and B2b) with different satellite combinations during
the research period. For clearer illustration, the bias and RMS for PWV monitored with two
RT ephemeris are summarized in Table 2. In general, the variation in PWV in the temporal
scale monitored by CAS and B2b products are generally consistent with the reference values
from the ERA5 reanalysis products. Correlating analysis indicates that the correlations
between PWV monitored from different combinations all exhibit high value greater than
0.95. In addition, PWV time series obtained by the NRT processing mode also has relatively
obvious fluctuations and outliers, which is similar to the results of ZTD above. This is

> [2 Figure(s)]

<!-- PAGE: 11 -->

Appl. Sci. 2025, 15, 8033
11 of 15
potentially due to the fact that the stability and accuracy of the real-time product (CAS and
B2b) are lower compared to the final product (WUM). For accuracy statistical results, it
shows that the bias of PWV monitored based on the CAS ephemeris using the combination
of G, C, and GC satellite combinations are −0.34, −1.32, and −0.29 mm, respectively, and
the corresponding RMS are 2.94, 4.36, and 3.46 mm, respectively, while those values for the
results from B2b ephemeris are −0.23, 0.96, −0.29 mm for bias, and 4.55, 4.40, 3.95 mm for
RMS. These values are generally about 1/6 of the ZTD error, which is consistent with the
theory of error propagation mentioned above. Compared with B2b results, PWV monitored
from CAS ephemeris exhibits better accuracy of about 35%, 1%, and 12% for G, C, and GC
satellite combinations. Similarly to the results compared with radiosonde observations, the
G and GC combinations reveals more obviously better accuracy, which might be due to
the lower quality of orbit and clock offset for the GPS satellite from B2b services, while
the general consistent accuracy for the BDS-only combinations (~1%) manifests the similar
qualities for BDS satellites from two RT ephemeris. Basically, these numerical results are
consistent with previous studies [29,30], that is, the accuracy that can be achieved by about
4 mm using the PPP-B2b service.
Figure 8. Time series of PWV monitored from NRT processing model using GPS-only (blue), BDS-
only (red), and GPS and BDS (green) satellite combinations based on CAS (a,c,e) and B2b ephemeris
(b,d,f) during the entire research period. The black line in each subfigure represents reference PWV
retrieved from the ERA5 reanalysis.

> [2 Figure(s)]

<!-- PAGE: 12 -->

Appl. Sci. 2025, 15, 8033
12 of 15
Table 2. Statistical results of PWV accuracy monitored from NRT processing mode using CAS and
B2b ephemeris with different satellite combinations.
Ephemeris
Satellite Combinations
Bias (mm)
RMS (mm)
GPS-only (G)
−0.34
2.94
CAS
BDS-only (C)
−1.32
4.36
GPS and BDS (GC)
−0.29
3.46
GPS-only (G)
−0.23
4.55
B2b
BDS-only (C)
0.96
4.40
GPS and BDS (GC)
−0.29
3.95
It should be noted that among the CAS results, PWV monitored with GPS-only
observation performs the best, followed by that from the GPS and BDS combination, and
the BDS-only performs the worst. In contrast, for the results of B2b, PWV monitored
with GPS-only performed the worst, followed by that of BDS-only, and the GPS and
BDS combination performed the best. This might be because that the production of the
B2b ephemeris mainly relies on some domestic stations in China and about 30 global
stations [44], which leads to the relatively low accuracy for GPS satellites. Therefore, the
accuracy is relatively lower when using GPS-only observations for PWV monitoring based
on the B2b ephemeris. However, when the BDS satellites were introduced to form dual-
system observations, the estimation of ZTD and the subsequent PWV monitoring were
improved, as is reported in previous research [8,39]. Based on the above analysis, the water
vapor monitoring based on the BDS PPP-B2b service can generally meet the demand for
NRT monitoring, and it is expected to be promoted and contribute to the extreme weather
forecasting in the near future.
5. Conclusions
The PPP-B2b service has significant potential for application in meteorological fields,
such as standalone water vapor monitoring in depopulated areas without Internet. While
most current studies are generally based on the simulated real-time PPP mode, analyzing its
practical performance should be conducted. For this purpose, a continuously operated wa-
ter vapor monitoring system using the PPP-B2b service was established in Wuhan, China.
The effectiveness of the NRT processing mode adopted by the monitoring system
is firstly verified through comparison of ZTD estimated from the post-processing mode.
Subsequently, the accuracy of ZTD estimated through the NRT processing mode using
two RT ephemeris is evaluated. Accuracy results show that the RMS of ZTD error for
the B2b ephemeris are 24.32, 23.34, 21.49 mm, respectively. These values were generally
comparable with those from CAS ephemeris, which can basically meet the requirements
for the following conversion to water vapor.
Finally, the accuracy of PWV monitored through the NRT processing mode are evalu-
ated to verify the practical performance of PPP-B2b service. Taking PWV from radiosonde
observations as the reference, RMS of PWV based on B2b ephemeris are 3.71, 4.66, and
3.73 mm for G, C, and GC combinations, respectively, while those values are 4.55, 4.40,
3.95 mm for G, C, and GC combinations, respectively. These accuracies are generally
comparable with those from CAS ephemeris and can generally meet the demand for NRT
water vapor monitoring. To sum up, water vapor monitoring based on the BDS PPP-B2b
service is feasible to be promoted to operational meteorology.
Future work lies in two directions. First, the assessment in the presented study
generally adopts GPS estimation as the reference, while further analysis with more satellite
systems (e.g., GLONASS and Galileo) can provide a more comprehensive perspective
on the performance of water vapor monitoring using BDS PPP-B2b service. Second, this

<!-- PAGE: 13 -->

Appl. Sci. 2025, 15, 8033
13 of 15
study only contains results of 25 days in a single place, while a further evaluation with a
longer time span and more stations should be conducted. The characteristics of accuracy in
different seasons (including rainy and non-rainy periods) and areas can be explored. This
will provide a more robust reference for its promotion in the near future.
Author Contributions: Conceptualization, Y.C.; methodology, Y.C. and L.Z.; software, L.Z. validation,
L.Z. and Y.C.; formal analysis, L.Z.; investigation, Y.C.; resources, Y.C. and H.L.; data curation, L.Z.,
E.Z., Z.H. and Y.C.; writing—original draft preparation, L.Z.; writing—review and editing, Y.C. and
H.L.; visualization, L.Z., X.L. and M.Q.; supervision, Y.C. and H.L.; project administration, Y.C. and
H.L.; funding acquisition, Y.C. and H.L. All authors have read and agreed to the published version of
the manuscript.
Funding: This research was funded by the National Natural Science Foundation of China (Grant
No. U2442214), the Observational Experiment Project of Meteorological Observation Center of China
Meteorological Administration (Grant No. GCSYJH24-21, GCSYJH24-02), and the Innovation and
development project of China Meteorological Administration (Grant No. CXFZ2024J061).
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: All data that support the findings of this study are included within the
article.
Acknowledgments: The authors are grateful to the ECMWF for providing the ERA5 reanalysis
products.
Conflicts of Interest: The authors declare no conflicts of interest.
Abbreviations
The following abbreviations are used in this manuscript:
BDS
BeiDou navigation satellite system
CAS
China Academy of Science
CDS
Climate Data Store
DOY
Day-of-Year
ECMWF
European Centre for Medium-Range Weather Forecasts
ERA5
The Fifth Generation ECMWF Reanalysis
GEO
Geostationary Earth Orbit
GLONASS
GLObal NAvigation Satellite System
GNSS
Global Navigation Satellite System
GPS
Global Positioning System
IGS
International GNSS Services
IPC
Industrial Personal Computer
NRT
Near Real-time
PPP
Precise Point Positioning
PWV
Precipitable Water Vapor
RT
Real-time
RTS
Real-Time Service
ZHD
Zenith Hydrostatic Delay
ZTD
Zenith Tropospheric Delay
ZWD
Zenith Wet Delay
References
1.
Trenberth, K.E.; Christy, J.R.; Olson, J.G. Global atmospheric mass, surface pressure, and water vapor variations. J. Geophys. Res.
Atmos. 1987, 92, 14815–14826. [CrossRef]

<!-- PAGE: 14 -->

Appl. Sci. 2025, 15, 8033
14 of 15
2.
Sherwood, S.C.; Roca, R.; Weckwerth, T.M.; Andronova, N.G. Tropospheric water vapor, convection, and climate. Rev. Geophys.
2010, 48, Rg2001. [CrossRef]
3.
Zhou, L.H.; Cao, Y.C.; Shi, C.; Liang, H.; Fan, L. Quantifying the Atmospheric Water Balance Closure over Mainland China Using
Ground-Based, Satellite, and Reanalysis Datasets. Atmosphere 2024, 15, 497. [CrossRef]
4.
Neelin, J.D.; Martinez-Villalobos, C.; Stechmann, S.N.; Ahmed, F.; Chen, G.; Norris, J.M.; Kuo, Y.H.; Lenderink, G. Precipitation
Extremes and Water Vapor Relationships in Current Climate and Implications for Climate Change. Curr. Clim. Change Rep. 2022,
8, 17–33. [CrossRef]
5.
Chen, X.L.; Xu, X.D.; Ma, Y.M.; Wang, G.L.; Chen, D.L.; Cao, D.B.; Xu, X.; Zhang, Q.; Li, L.H.; Liu, Y.J.; et al. Investigation of
Precipitation Process in the Water Vapor Channel of the Yarlung Zsangbo Grand Canyon. Bull. Am. Meteorol. Soc. 2024, 105,
e370–e386. [CrossRef]
6.
Liu, Y.; Yan, X.; Yao, Y.B.; Zhang, B.; Zhao, Q.Z.; Wang, X.Q.; E, S.L.; Zhang, L. Revealing the synergistic contribution of PWV and
CAPE to extreme precipitation throughout China. Adv. Space Res. 2025, 75, 2739–2752. [CrossRef]
7.
Emardson, T.R.; Johansson, J.M. Spatial interpolation of the atmospheric water vapor content between sites in a ground-based
GPS network. Geophys. Res. Lett. 1998, 25, 3347–3350. [CrossRef]
8.
Lu, C.X.; Chen, X.H.; Liu, G.; Dick, G.; Wickert, J.; Jiang, X.Y.; Zheng, K.; Schuh, H. Real-Time Tropospheric Delays Retrieved from
Multi-GNSS Observations and IGS Real-Time Product Streams. Remote Sens. 2017, 9, 1317. [CrossRef]
9.
Zhou, L.H.; Fan, L.; Shi, C. Evaluation and Analysis of Remotely Sensed Water Vapor from the NASA VIIRS/SNPP Product in
Mainland China Using GPS Data. Remote Sens. 2023, 15, 1528. [CrossRef]
10.
Ning, T.; Wang, J.; Elgered, G.; Dick, G.; Wickert, J.; Bradke, M.; Sommer, M.; Querel, R.; Smale, D. The uncertainty of the
atmospheric integrated water vapour estimated from GNSS observations. Atmos. Meas. Tech. 2016, 9, 79–92. [CrossRef]
11.
Bevis, M.; Businger, S.; Herring, T.A.; Rocken, C.; Anthes, R.A.; Ware, R.H. GPS meteorology: Remote sensing of atmospheric
water vapor using the global positioning system. J. Geophys. Res. Atmos. 1992, 97, 15787–15801. [CrossRef]
12.
Maciejewska, A. Use of Tropospheric Delay in GNSS-Based Climate Monitoring-A Review. Remote Sens. 2025, 17, 1501. [CrossRef]
13.
Bevis, M.; Businger, S.; Chiswell, S.; Herring, T.A.; Anthes, R.A.; Rocken, C.; Ware, R.H. GPS meteorology: Mapping zenith wet
delays onto precipitable water. J. Appl. Meteorol. Climatol. 1994, 33, 379–386. [CrossRef]
14.
Zhang, W.X.; Lou, Y.D.; Cao, Y.C.; Liang, H.; Shi, C.; Huang, J.F.; Liu, W.X.; Zhang, Y.; Fan, B.B. Corrections of Radiosonde-Based
Precipitable Water Using Ground-Based GPS and Applications on Historical Radiosonde Data Over China. J. Geophys. Res. Atmos.
2019, 124, 3208–3222. [CrossRef]
15.
Zhou, L.H.; Fan, L.; Shi, C.; Liang, H.; Cao, Y.C. Comprehensive analysis of zenith tropospheric delay and precipitable water
vapor retrieved from BDS-3 B1C and B2a signals. Measurement 2025, 242, 116079. [CrossRef]
16.
Wang, M.H.; Wang, J.X.; Bock, Y.; Liang, H.; Dong, D.A.; Fang, P. Dynamic Mapping of the Movement of Landfalling Atmospheric
Rivers Over Southern California With GPS Data. Geophys. Res. Lett. 2019, 46, 3551–3559. [CrossRef]
17.
Zhou, L.H.; Fan, L.; Zhang, W.X.; Shi, C. Long-term correlation analysis between monthly precipitable water vapor and
precipitation using GPS data over China. Adv. Space Res. 2022, 70, 56–69. [CrossRef]
18.
Wu, Z.L.; Lu, C.X.; Liu, Y.; Lin, H.; Zheng, Y.X.; Wei, Q.; Liu, Y.X. Global statistical assessment of Haiyang-2B scanning microwave
radiometer precipitable water vapor. Front. Earth Sci. 2023, 11, 1084285. [CrossRef]
19.
Wang, H.S.; Liu, Y.B.; Liu, Y.W.; Cao, Y.C.; Liang, H.; Hu, H.; Liang, J.S.; Tu, M.H. Assimilation of GNSS PWV with NCAR-RTFDDA
to Improve Prediction of a Landfall Typhoon. Remote Sens. 2022, 14, 178. [CrossRef]
20.
Liu, Y.; Zhang, B.; Yao, Y.B.; Zhao, Q.Z.; Xu, C.Q.; Yan, X.; Zhang, L. Revealing the spatiotemporal patterns of water vapor and its
link to North Atlantic Oscillation over Greenland using GPS and ERA5 data. Sci. Total Environ. 2024, 918, 170596. [CrossRef]
[PubMed]
21.
Li, L.J.; Wu, S.Q.; Zhang, K.F.; Wang, X.M.; Li, W.; Shen, Z.; Zhu, D.T.; He, Q.M.; Wan, M.F. A new zenith hydrostatic delay model
for real-time retrievals of GNSS-PWV. Atmos. Meas. Tech. 2021, 14, 6379–6394. [CrossRef]
22.
Li, H.J.; Li, X.M.; Kang, Q. Handling Method for Outages of IGS Real-Time Service (RTS) in GNSS Real-Time Sensing of
Atmospheric Water Vapor. IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens. 2023, 16, 8310–8318. [CrossRef]
23.
Paz, J.M.A.; Mendoza, L.P.O.; Fernández, L.I. Near-real-time GNSS tropospheric IWV monitoring system for South America. GPS
Solut. 2023, 27, 93.
24.
Wang, H.; He, J.X.; Wei, M.; Zhang, Z.D. Synthesis Analysis of One Severe Convection Precipitation Event in Jiangsu Using
Ground-Based GPS Technology. Atmosphere 2015, 6, 908–927. [CrossRef]
25.
Du, M.B.; Cao, Y.C.; Liang, H.; Hu, H.; Wang, H.S.; Song, S.L.; Jiao, G.Q. Construction of a meteorological application system
based on BDS ground-based augmentation network and water vapor products validation. GPS Solut. 2024, 28, 107. [CrossRef]
26.
Yang, Y.X.; Ding, Q.; Gao, W.G.; Li, J.L.; Xu, Y.Y.; Sun, B.J. Principle and performance of BDSBAS and PPP-B2b of BDS-3. Satell.
Navig. 2022, 3, 5. [CrossRef]
27.
Yang, H.; He, X.F.; Ferreira, V.; Ji, S.Y.; Xu, Y.; Song, S.S. Assessment of precipitable water vapor retrieved from precise point
positioning with PPP-B2b service. Earth Sci. Inf. 2023, 16, 315–328. [CrossRef]

<!-- PAGE: 15 -->

Appl. Sci. 2025, 15, 8033
15 of 15
28.
Cao, Y.C.; Cheng, Z.H.; Liang, J.S.; Zhao, P.P.; Cao, Y.C.; Wang, Y.Z. Performance of Ground-Based Global Navigation Satellite
System Precipitable Water Vapor Retrieval in Beijing with the BeiDou B2b Service. Remote Sens. 2024, 16, 2902. [CrossRef]
29.
Wang, X.M.; Chen, Y.F.; Zhang, J.L.; Qiu, C.; Zhou, K.; Li, H.B.; Huang, Q.Y. Assessment of BDS-3 PPP-B2b Service and Its
Applications for the Determination of Precipitable Water Vapour. Atmosphere 2024, 15, 1048. [CrossRef]
30.
Xu, Y.; Zhao, P.P.; Wang, J. Precipitable water vapor retrieval for rainfall forecasting using BDS-3 PPP-B2b signal in the coastal
region of China. Meas. Sci. Technol. 2024, 35, 116309. [CrossRef]
31.
Zhou, P.Y.; Zhang, Z.K.; Liu, Z.J.; Lyu, D.; Xiao, G.R.; Xiao, K.; Du, L. Real-Time Precise Zenith Tropospheric Delay Estimation with
BDS PPP-B2b, Galileo HAS, and QZSS MADOCA-PPP Services. IEEE Trans. Geosci. Remote Sens. 2024, 62, 5802011. [CrossRef]
32.
Guo, J.; Xu, X.L.; Zhao, Q.L.; Liu, J.N. Precise orbit determination for quad-constellation satellites at Wuhan University: Strategy,
result validation, and comparison. J. Geod. 2016, 90, 143–159. [CrossRef]
33.
Lee, Z.; Wang, L.; Wang, N.; Li, Y.; Liu, A.; Li, M.; Lee, Z. Performance Assessment and Integrity Support Information Estimation
of CAS Real-time Orbits and Clocks Products. Geomat. Inf. Sci. Wuhan Univ. 2024, 1–19. [CrossRef]
34.
Hersbach, H.; Bell, B.; Berrisford, P.; Hirahara, S.; Horányi, A.; Muñoz-Sabater, J.; Nicolas, J.; Peubey, C.; Radu, R.; Schepers, D.;
et al. The ERA5 global reanalysis. Q. J. R. Meteorol. Soc. 2020, 146, 1999–2049. [CrossRef]
35.
Zhang, W.X.; Lou, Y.D.; Zhou, Y.Z.; Liu, M.J.; Zhang, Z.Y.; Ou, S.Y.; Liu, J.N. GNSS meteorological ensemble tools (GMET): A
free-access online service for GNSS meteorological applications. GPS Solut. 2024, 28, 202. [CrossRef]
36.
Byun, S.H.; Bar-Sever, Y.E. A new type of troposphere zenith path delay product of the international GNSS service. J. Geod. 2009,
83, 367–373. [CrossRef]
37.
Saastamoinen, J. Atmospheric correction for the troposphere and stratosphere in radio ranging satellites. Geophys. Monogr. 1972,
15, 247–251.
38.
Landskron, D.; Böhm, J. VMF3/GPT3: Refined discrete and empirical troposphere mapping functions. J. Geod. 2018, 92, 349–360.
[CrossRef] [PubMed]
39.
Lu, C.X.; Feng, G.L.; Zheng, Y.X.; Zhang, K.K.; Tan, H.; Dick, G.; Wickert, J. Real-Time Retrieval of Precipitable Water Vapor from
Galileo Observations by Using the MGEX Network. IEEE Trans. Geosci. Remote Sens. 2020, 58, 4743–4753. [CrossRef]
40.
Shi, C.; Guo, S.W.; Fan, L.; Gu, S.F.; Fang, X.Q.; Zhou, L.H.; Zhang, T.; Li, Z.; Li, M.; Li, W.W.; et al. GSTAR: An innovative
software platform for processing space geodetic data at the observation level. Satell. Navig. 2023, 4, 18. [CrossRef]
41.
Yao, Y.B.; Zhang, B.; Xu, C.Q.; Chen, J.J. Analysis of the global Tm-Ts correlation and establishment of the latitude-related linear
model. Chin. Sci. Bull. 2014, 59, 2340–2347. [CrossRef]
42.
Lu, C.X.; Li, X.X.; Nilsson, T.; Ning, T.; Heinkelmann, R.; Ge, M.R.; Glaser, S.; Schuh, H. Real-time retrieval of precipitable water
vapor from GPS and BeiDou observations. J. Geod. 2015, 89, 843–856. [CrossRef]
43.
Zhou, L.H.; Fan, L.; Guo, S.W.; Shi, C. Assessing the feasibility of atmospheric water vapor monitoring with standalone BDS
receiver. Environ. Monit. Assess. 2025, 197, 66. [CrossRef] [PubMed]
44.
Tang, C.P.; Hu, X.G.; Chen, J.P.; Liu, L.; Zhou, S.S.; Guo, R.; Li, X.J.; He, F.; Liu, J.H.; Yang, J.H. Orbit determination, clock
estimation and performance evaluation of BDS-3 PPP-B2b service. J. Geod. 2022, 96, 60. [CrossRef]
45.
Wang, J.H.; Zhang, L.Y.; Dai, A.; Van Hove, T.; Van Baelen, J. A near-global, 2-hourly data set of atmospheric precipitable water
from ground-based GPS measurements. J. Geophys. Res. Atmos. 2007, 112, D11107. [CrossRef]
46.
Shi, C.; Zhou, L.H.; Fan, L.; Zhang, W.X.; Cao, Y.C.; Wang, C.; Xiao, F.; Lü, G.Q.; Liang, H. Analysis of “21·7” extreme rainstorm
process in Henan Province using BeiDou/GNSS observation. Chin. J. Geophys. 2022, 65, 186–196.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
