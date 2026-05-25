<!-- PAGE: 1 -->

IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.62,2024 5802011
Real-Time Precise Zenith Tropospheric Delay
Estimation With BDS PPP-B2b, Galileo HAS,
and QZSS MADOCA-PPP Services
Peiyuan Zhou , Zhongkai Zhang, Zejun Liu, Daqian Lyu , Guorui Xiao , Kai Xiao , and Lan Du
Abstract—Real-time precise point positioning (PPP) is an I. INTRODUCTION
innovativeandusefulatmosphereremotesensingtooltoestimate
zenith tropospheric delays (ZTDs) to support various emerging THE estimation of zenith tropospheric delays (ZTDs)
meteorologicalapplicationssuchasweatherandclimateresearch. is significant to support various emerging applications,
However, additional costs on internet accesses or service sub- such as numerical weather forecasting and global climate
scriptionlicensesarerequiredtoobtainreal-timeprecisesatellite
monitoring [1], [2], [3], space geodesy [4], [5], and precise
orbitandclockproductsfromexternalPPPaugmentationservice
positioning [6], [7], [8]. Thanks to the deployment of GNSS
operators. We present the real-time precise estimation of ZTD
with freely and openly accessible GNSS satellite-based PPP real-time precise satellite orbit and clock augmentation cor-
augmentation services, i.e., BeiDou navigation satellite system rection services, real-time precise point positioning (PPP) is
(BDS) PPP-B2b service, Galileo high accuracy service (HAS), emerging as an alternative atmosphere remote sensing tool
and quasi-zenith satellite system(QZSS) Multi-GNSS ADvanced
to retrieve real-time precise ZTD with high spatiotempo-
Orbit and Clock Augmentation-PPP (MADOCA-PPP) service.
ral resolution in all-weather conditions, which is drawing
GNSSobservationsof49daysfrom15stationsintheAsia–Pacific
region are used for performance assessment and comparison. increasing interests from both academia and industrial
It shows that the real-time PPP estimated ZTDs agree well areas [9], [10], [11].
with International GNSS Service (IGS) final ZTDs, with mean However, previous research on ZTD estimation with
standard deviation (STD) values of 20.0, 17.5, and 9.5 mm
real-timePPPhasbeenfocusedmainlyonusingreal-timepre-
for BDS PPP-B2b, Galileo HAS, and QZSS MADOCA-PPP,
cise satellite orbit and clock products from external real-time
respectively.Thederivedreal-timezenithwetdelays(ZWDs)are
further compared with those derived from Integrated Global PPP augmentation correction service operators [12], which
Radiosonde Archive (IGRA) and the European Centre for brings several challenges to be addressed in the routine
Medium-Range Weather Forecasts (ECMWF) Reanalysis v5 application implementation. On the one hand, reliable and
(ERA5)datasets,whichconfirmsthatthereal-timePPPestimated
continuous communication links to the server are required to
ZWDs are accurate with mean STDs of smaller than 30 mm.
obtain real-time corrections from the service operators; other-
It concludes that real-time PPP with GNSS satellite-based real-
timePPPaugmentationcorrectionserviceswillbeaflexibleand wise, the quality of the real-time orbit and clock corrections
cost-effective tool to derive real-time precise ZTDs/ZWDs with would be degraded during communication link outages [13].
high spatiotemporal resolution in all-weather conditions. Hence, the performance of the obtained ZTD products will be
Index Terms—BeiDou navigation satellite system (BDS) pre- deteriorated. For example, internet access should be guaran-
cise point positioning (PPP)-B2b, Galileo high accuracy service teed for ZTD estimation with real-time PPP using corrections
(HAS), Multi-GNSS ADvanced Orbit and Clock Augmentation-
from real-time service (RTS) of International GNSS Service
PPP (MADOCA-PPP), zenith tropospheric delay (ZTD), zenith
(IGS) [13], [14]. On the other hand, users are subjected to
wet delay (ZWD).
expensive subscription fees to access augmentation correction
Manuscriptreceived8May2024;revised14July2024;accepted9August services provided by commercial companies [15], [16]. These
2024.Dateofpublication15August2024;dateofcurrentversion9September
additional costs and complexity are still to be optimized for
2024. This work was supported in part by the National Natural Science
Foundation of China under Grant 42204041 and Grant 42204039; in part the further promotion of ZTD estimation with real-time PPP.
by the State Key Laboratory of Geodesy and Earth’s Dynamics, Innova- Notethatthereal-timePPPbasedZTDestimationcanalsobe
tion Academy for Precision Measurement Science and Technology, Chinese
conducted using Galileo broadcast ephemeris with improved
AcademyofSciences(CAS),Wuhan,ChinaunderGrantSKLGED2023-3-5;
and in part by the Postdoctoral Fellowship Program of China Postdoctoral quality[17],[18],andtheavailabilityandreliability,however,
Science Foundation (CPSF) under Grant GZC20233523. (Corresponding are still limited since only Galileo observations can be used.
author:DaqianLyu.)
Instead of disseminating real-time precise satellite orbit
Peiyuan Zhou is with Information Engineering University, Zhengzhou
450001,China,andalsowiththeNationalUniversityofDefenseTechnology, and clock corrections via internet or dedicated commu-
Hefei230037,China. nication satellite links, several newly developed GNSSs
ZhongkaiZhang,ZejunLiu,GuoruiXiao,KaiXiao,andLanDuarewith
provide freely and openly accessible real-time PPP aug-
InformationEngineeringUniversity,Zhengzhou450001,China.
DaqianLyuiswiththeNationalUniversityofDefenseTechnology,Hefei mentation correction services via navigation satellite signals.
230037,China,andalsowiththeLaboratoryofScienceandTechnologyon Specifically, the Chinese BeiDou navigation satellite system
CommunicationInformationSecurityControl,Jiaxing314033,China(e-mail:
(BDS) starts to provide PPP-B2b service via B2b signals
daqian_lv@nudt.edu.cn).
DigitalObjectIdentifier10.1109/TGRS.2024.3443884 in 2020 to users located in China and surrounding areas
1558-0644©2024IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:35:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 2 -->

5802011 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.62,2024
(10◦N∼55◦N and 75◦W∼135◦W) [19], and the quasi-zenith (ERA5). Finally, the conclusions are summarized in
satellite system (QZSS) Multi-GNSS ADvanced Orbit and Section IV.
Clock Augmentation-PPP (MADOCA-PPP) service starts to
provide trial service in 2022 to users in the Asia–Pacific II. METHODOLOGY
area (60◦S∼60◦N and 70◦E∼200◦E) [20], followed by the
A. Computation of Real-Time Precise Satellite Orbit and
European Galileo to declare initial service of its high accu-
Clock
racy service (HAS) via E6B signals in 2023 to global
users (the rectangle area of 60◦S∼60◦N and 125◦W∼180◦W Real-time precise satellite orbit and clock are fundamental
and the rectangle area of 60◦S∼60◦N and 90◦E∼180◦E are to ZTD estimation with real-time PPP. The computation of
not guaranteed for minimum performance levels) [21]. Note real-time GPS and BDS satellite orbits from PPP-B2b dis-
that PPP-B2b supports BDS/GPS constellations, and HAS seminated satellite orbit corrections δOs B2b can be described
supports Galileo/GPS constellations, while MADOCA-PPP as [27]
supports GPS/Galileo/GLONASS/QZSS constellations. Qual-
δXs = R δOs (1)
ity assessment of the obtained real-time satellite orbit and B2b B2b B2b
clock products from BDS PPP-B2b, Galileo HAS, and QZSS where δXs is the obtained satellite orbit corrections in the
B2b
MADOCA-PPP has been conducted extensively, which indi- Earth-centered, Earth-fixed (ECEF) frame, and R is the
B2b
cates that they can support decimeter- to centimeter-level transformation matrix and can be obtained as
real-time PPP at the user [19], [21], [22], [23]. Since these (cid:20) xs xs ×x˙s xs xs ×x˙s (cid:21)
real-time PPP augmentation correction services are dissem- R B2b = |xs| (cid:12) (cid:12)xs ×x˙s (cid:12) (cid:12) × |xs| (cid:12) (cid:12)xs ×x˙s (cid:12) (cid:12) (2)
inated via navigation satellite signals, no additional costs
on hardware and software are required at the user, which where the satellite position xs and velocity x˙s are computed
bringsgreatopportunitiesforimplementinglow-costreal-time using the broadcast navigation message as per its correspond-
precise ZTD estimation based on real-time precise satel- ing GNSS interface control document (ICD). The computed
lite orbit and clock products from BDS PPP-B2b, Galileo precise satellite orbit xs in the BeiDou coordinate system
B2b
HAS, and QZSS MADOCA-PPP. Although real-time precise (BDCS) can be derived as
ZTD estimation with BDS PPP-B2b [24], [25] and Galileo
xs = xs −δXs . (3)
HAS [26] has been investigated in previous research, further B2b B2b
developments and comprehensive performance assessment of ThePPP-B2bdisseminatedsatelliteclockcorrectionsδCs
real-time ZTD estimation with all the three operational GNSS should be applied to the broadcast satellite clock dts co B m 2b -
satellite-basedreal-timePPPaugmentationservicesarestillto
puted from the broadcast navigation message. The computed
be conducted. PPP-B2b satellite clock dts referenced to the BeiDou navi-
This article presents the methods and assessment of B2b
gation satellite system time (BDT) can be derived as [27]
real-timepreciseZTDestimationwithallofthethreecurrently
δCs
operational GNSS satellite-based real-time PPP augmentation dts =dts − B2b (4)
correction services, including BDS PPP-B2b, Galileo HAS, B2b c
and QZSS MADOCA-PPP. The main contributions of this where c denotes the speed of light.
article are to answer the following research questions. On the other hand, real-time GPS and Galileo satellite
1) How to estimate real-time precise ZTDs with GNSS orbits can be computed with HAS disseminated satellite orbit
satellite-based real-time PPP augmentation correction corrections δOs , which can be written as [28]
HAS
services?
δXs = R δOs (5)
2) Is it possible to estimate highly available and accurate HAS HAS HAS
real-time precise ZTDs? Do they meet the threshold where δXs is the obtained satellite orbit corrections in the
HAS
(15 mm) and target (10 mm) accuracy requirement for ECEF frame and R is the transformation matrix and can
HAS
numerical weather prediction (NWP) assimilation [26]? be obtained as
3) How does the accuracy of the real-time PPP estimated
(cid:20) x˙s xs ×x˙s x˙s xs ×x˙s (cid:21)
The Z r T es D t s of co th m is pa a r r e ti d cl t e o is ex o i r s g ti a n n g iz a e t d m a o s sp fo h l e lo ri w c s p . r T o h d e uc m ts e ? thods R HAS = (cid:12) (cid:12)x˙s (cid:12) (cid:12) × (cid:12) (cid:12)xs ×x˙s (cid:12) (cid:12) (cid:12) (cid:12)x˙s (cid:12) (cid:12) (cid:12) (cid:12)xs ×x˙s (cid:12) (cid:12) . (6)
to estimate real-time ZTD with precise satellite orbit and After that, real-time GPS and Galileo satellite orbit from
clock products from the three GNSS satellite-based real- HAS in the Galileo terrestrial reference frame (GTRF) can be
time PPP augmentation correction services are described in derived as
SectionII.InSectionIII,extensiveexperimentsandvalidation
are conducted to examine the performance of the obtained xs HAS = xs +δXs HAS . (7)
real-time ZTD products using IGS final ZTD products as the
Meanwhile, real-time GPS and Galileo satellite clock refer-
references. Furthermore, the quality of the obtained real-time
enced to the Galileo system time (GST) can be derived from
zenith wet delays (ZWDs) is assessed with respect to ZWDs HAS disseminated satellite clock corrections δCs as [28]
derived with datasets from Integrated Global Radiosonde HAS
Archive (IGRA) as well as the European Centre For dts =dts +
δC
H
s
AS. (8)
Medium-Range Weather Forecasts (ECMWF) Reanalysis v5 HAS c
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:35:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 3 -->

ZHOUetal.:REAL-TIMEPRECISEZENITHTROPOSPHERICDELAYESTIMATION 5802011
Similarly, real-time GPS, GLONASS, and Galileo satellite
orbits can be computed with MADOCA-PPP disseminated
satelliteorbitcorrectionsδOs ,whichcanbewrittenas[20]
MAD
δXs = R δOs (9)
MAD MAD MAD
where δXs is the obtained satellite orbit corrections in the
MAD
ECEF frame and R is the transformation matrix and can
MAD
be obtained as
(cid:20) x˙s xs ×x˙s x˙s xs ×x˙s (cid:21)
R MAD = (cid:12) (cid:12)x˙s (cid:12) (cid:12) × (cid:12) (cid:12)xs ×x˙s (cid:12) (cid:12) (cid:12) (cid:12)x˙s (cid:12) (cid:12) (cid:12) (cid:12)xs ×x˙s (cid:12) (cid:12) . (10)
After that, real-time GPS, GLONASS, and Galileo satellite
orbit from MADOCA-PPP in the International Terrestrial
Reference Frame (ITRF2020) can be derived as
Fig.1. Geographicaldistributionof15GNSSstations.
xs = xs −δXs . (11)
MAD MAD
Meanwhile,real-timeGPS,GLONASS,andGalileosatellite ConsideringthedifferentcharacteristicsofZWDandZHD,
clock referenced to the QZSS time (QZSST) can be derived the ZWD and horizontal gradients G ns and G ew are estimated
from MADOCA-PPP disseminated satellite clock corrections asunknownparameters,whileZHDismodeledwithempirical
δCs as [20] model such as Saastamoinen model [30]. Meanwhile, the
MAD
satellite orbit and clock are obtained from PPP-B2b, HAS,
δCs
dts =dts − MAD. (12) and MADOCA-PPP services, and the receiver coordinates are
MAD c
fixed to reference solutions. The unknown state vectors in
The code biases are also disseminated by PPP-B2b, HAS, real-time PPP are {dt r,G dt r,C Zw G ns G sw N I 1 F ··· N I s F }T
andMADOCA-PPP,whichshouldbeappliedappropriatelyas for PPP-B2b, {dt r,G dt r,E Zw G ns G sw N I 1 F ··· N I s F }T for
per corresponding ICDs [20], [27], [28]. It is also noted that HAS, and {dt r,G dt r,R dt r,E Zw G ns G sw N I 1 F ··· N I s F }T
the computed real-time satellite orbit and clock from PPP- for MADOCA-PPP, where dt r,G , dt r,C , dt r,R , and dt r,E are
B2b, HAS, and MADOCA-PPP refer to different reference the receiver clock for GPS, BDS, GLONASS, and Galileo,
frame and time system. Therefore, real-time PPP are running respectively. It is noted that the ionospheric-free ambiguities
independently without integrating these three services in this are estimated as float constants since no carrier phase bias
study. products are available from these three services.
After estimating the state vector, the real-time ZTD is
B. ZTD Estimation With Real-Time PPP obtained as
The dual-frequency ionospheric-free observation model is ZTD= Zw +Z
h
. (15)
used for ZTD estimation with real-time PPP, which can be
described as [8], [29] III. EXPERIMENTS,RESULTS,ANDDISCUSSION
P I s F =ρs +dt r,sys −dts +Ts +ε P I s F A. Data Collection and Processing Strategies
(cid:56)s IF =ρs +dt r,sys −dts +Ts +N I s F +ε (cid:56)s IF (13) Toassesstheperformanceofreal-timeZTDestimationwith
PPP-B2b, HAS, and MADOCA-PPP services, GNSS obser-
where the superscript “s” refers to the satellite, and Ps and
IF vations of 15 stations from the IGS multi-GNSS experiment
(cid:56)s are the dual-frequency ionospheric-free code and carrier
IF (MGEX) network in the PPP-B2b, HAS, and MADOCA-PPP
phase observations after applying necessary corrections in
overlapped service region [20], [28], [31], from day of year
r u e n s i p ts ec o ti f ve m ly e . te ρ r s s, is w t i h t e h g c e o o r m re e sp tr o ic nd d i i n s g tan n c o e is b e e s tw as ee ε n P I t s F he an s d ate ε l (cid:56) li s I t F e , (DOY) 181 to 229, 2023, are collected. The geographic
distribution of the 15 GNSS stations is shown in Fig. 1. It is
andreceiver.dts isthesatelliteclock,whiledt r,sys istheGNSS noted that the selected stations are located in the nonnominal
system-specific receiver clock. Ns is the ionospheric-free
IF HAS service area [28], which may expect quality degradation
ambiguityinunitsofmeters.Ts istheslanttroposphericdelay,
of the real-time PPP estimated ZTDs/ZWDs [26].
which can be expressed as [1]
Meanwhile, a Septentrio Mosaic X5 receiver (SEPT) is
Ts = M
w
s(e)Zw +M
h
s(e)Z
h
deployed in Zhengzhou, China, to collect PPP-B2b and
HAS corrections, while the MADOCA-PPP corrections are
+Ms(e)cote(G ·cosa+G ·sina) (14)
w ns ew obtained from QZSS official MADOCA-PPP data archive
where e and a are the satellite elevation and azimuth angles, (https://l6msg.go.gnss.go.jp/). It is noted that different GNSS
respectively; Zw and Z
h
are the zenith wet tropospheric delay observationcombinationsareselectedbasedontheavailability
(ZWD)andzenithhydrostatictroposphericdelay(ZHD),with of real-time precise satellite orbit and clock products as listed
elevation-dependent mapping functions Ms(e) and Ms(e), in Table I, while detailed data processing strategies are listed
w h
respectively; and G and G are the horizontal gradients in Table II. In addition, the postprocessed precise satellite
ns ew
in the north–south and east–west directions, respectively. orbit and clock products from Wuhan University, one of
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:35:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 4 -->

5802011 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.62,2024
TABLEI TABLEII
REAL-TIMEPPPOBSERVATIONCONFIGURATIONS REAL-TIMEPPPPROCESSINGSTRATEGIES
the IGS MGEX Analysis Center (WUM), are also used for
ZTDestimationwithquad-constellationPPP(i.e.,GPSL1/L2,
GLONASS G1/G2, Galileo E1/E5a, and BDS B1/B3). Note
that the ZTD estimation is conducted in a simulated real-time
manner based on data availability. Furthermore, to minimize
the impacts of different reference frames (Table I) on ZTD
estimation, the receiver coordinates are fixed to respective
PPP static solutions to ensure self-consistency. As for inter-
comparison with other products, the time system differences
are neglected considering the relatively slow-varying charac-
teristics of ZTDs, while the reference frame differences will
likely contribute to the constant biases. The obtained ZTD
time series are referred to as ZTD-B2B (with BDS PPP-
B2b),ZTD-HAS(withGalileoHAS),ZTD-MAD(withQZSS
MADOCA-PPP),andZTD-WUM(withIGSWUMproducts),
respectively.
The obtained ZTD time series at CUSV station are plotted
inFig.2asanexample.ItisobservedthattheZTDtimeseries
vary similarly among different solutions, with ZTD values
ranging from 2.4 to 2.8 m. The availability of the real-time
PPP estimated ZTD time series is first assessed considering
thenominalobservationsamplingintervalsof30s;hence,the
nominal daily updates of ZTDs should be 2880. Fig. 3 shows
the calculated availability percentage of ZTD-B2B, ZTD-
HAS, ZTD-MAD, and ZTD-WUM. Generally, the available
percentage of all the 15 stations is larger than 99%, with no
significant differences being found among different ZTD time
series at the same station. However, the availability of the
ZTD time series is different among different stations, which
areattributedtothevariedqualityofGNSSobservations.Nev-
ertheless,itindicatesthatthereal-timecorrectionsprovidedby
PPP-B2b/HAS/MADOCA-PPP are capable of deriving highly
available ZTDs comparable to those of using postprocessed
IGS WUM products.
Fig. 2. ZTD time series estimated with PPP-B2b, HAS, MADOCA-PPP,
B. Inter-GNSS ZTD Comparison
andWUMattheCUSVstation.
The internal consistency is first verified by comparing
the real-time ZTD solutions (i.e., ZTD-B2B/ZTD-HAS/ZTD-
MAD) with respect to those derived with the postprocessed quality of the estimated ZTDs should therefore be attributed
IGSWUMproducts(ZTD-WUM).Sincetheprocessingstrate- mainly to the quality of different real-time satellite orbit and
gies are the same among different ZTD solutions, the varied clock products.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:35:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 5 -->

ZHOUetal.:REAL-TIMEPRECISEZENITHTROPOSPHERICDELAYESTIMATION 5802011
Fig. 4. Differences of ZTD-B2B/ZTD-HAS/ZTD-MAD with respect to
ZTD-WUM at CUSV station. Offsets of 0.15 and −0.15 m are applied to
ZTD-B2BandZTD-MADforbettervisibility.
TABLEIII
STATISTICSOFREAL-TIMEZTDSOLUTIONSCOMPAREDTO
ZTD-WUMSOLUTIONS(UNITS:mm)
Fig.3. AvailabilitypercentageoftheestimatedZTDs.
The time series of ZTD differences at CUSV are shown IGSWUMproductsaremoreconcentratedtowardzero,which
in Fig. 4 as an example. It can be seen that the ZTD- are significantly better than those derived with PPP-B2b and
B2B solutions has a relatively significant bias of 3.3 mm HAS. The corresponding STDs are 25.2, 19.8, 12.8, and
with a standard deviation (STD) of 20.6 mm, indicating that 12.2 mm, which indicates that the quality of ZTDs derived
the obtained ZTDs can vary significantly over time. On the with WUM products is the best, followed by those derived
other hand, the ZTD-HAS solution shows a smaller bias of with MADOCA-PPP and HAS products, while the quality
0.5 mm with an STD of 15.3 mm, suggesting that there is of ZTDs derived with PPP-B2b is the poorest, which should
considerable variability. In contrast, the ZTD-MAD solution be attributed to the satellite availability and varied quality of
is highly consistent with the ZTD-WUM solution, with a bias different products.
of nearly zero and a much lower STD of 5.7 mm. The statistics over all the 15 GNSS stations are plotted
Furthermore, the statistics of real-time ZTD solutions com- in Fig. 6, and the mean of the statistics is provided in
pared to the ZTD-WUM solution over all the 15 stations Table IV. On the one hand, when comparing ZTD quality
are provided in Table III. The results show that ZTD-MAD among different GNSS stations using the same satellite orbit
solution is the most consistent with respect to ZTD-WUM and clock products, it is found that the quality of the obtained
solution, with mean root-mean square errors (RMSEs) of ZTDs at GNSS station WUH2 is generally poorer than other
6.8 mm, followed by ZTD-HAS with an RMSE value of stations,whichindicatesthatthequalityofZTDsisaffectedby
16.2mm.TheZTD-B2B,however,showsthemostsignificant thequalityGNSSobservations.Ontheotherhand,whencom-
biasesandvariationsamongthethreereal-timeZTDsolutions, paring ZTD quality among solutions using different satellite
with an RMSE value of 19.2 mm. The large biases of ZTD- orbitandclockproducts,itisshownthatthemeanbiasesover
B2B could be attributed to the PPP-B2b constellation rotation all the selected stations are 5.4, 0.7, 0.3, and 1.1 mm for the
errors as revealed in [22]. Overall, the results highlight the ZTD-B2B,ZTD-HAS,ZTD-MAD,andZTD-WUMsolutions,
impacts of the varied quality of different real-time satellite respectively, while the mean STDs are at the same level of
orbit and clock products on real-time ZTD estimation. 20.0and17.5mmforZTD-B2BandZTD-HAS,and10.1and
Then,thereal-timePPPestimatedZTDsarecomparedwith 9.0 mm for ZTD-MAD and ZTD-WUM, respectively. The
the IGS final ZTD products, and the distribution of ZTD quality of ZTD-WUM, with a mean RMSE of 9.0 mm, is the
differences for station CUSV are shown in Fig. 5. It is shown bestamongallthefoursolutions,followedbyZTD-MADwith
that the ZTD differences obtained using MADOCA-PPP and ameanRMSEof10.1mmandZTD-HASwithameanRMSE
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:35:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 6 -->

5802011 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.62,2024
TABLEIV
STATISTICSOFREAL-TIMEZTDSOLUTIONSCOMPARED
TOIGSFINALPRODUCTS(UNITS:mm)
Fig. 5. Differences of real-time ZTDs estimated with (top left) PPP-B2b,
(top right) HAS, (bottom left) MADOCA-PPP, and (bottom right) WUM at
CUSVusingIGSfinalZTDproductsasthereferences.
of 17.8 mm. The quality of ZTD-B2B, with a mean RMSE of
21.5mm,isthepoorest,whichcouldbeattributedtothelarge
biases and variations. The results indicates that the quality of
ZTDs obtained with real-time MADOCA-PPP corrections is
comparable to those derived with postprocessed IGS WUM
products, while the quality of ZTDs obtained with PPP-B2b
and HAS are significantly worse. It is found that the quality
of ZTD-B2B is comparable to previous research such as [24]
and [25], while the quality of ZTD-HAS is slightly poorer
compared to [26], which might be restricted mainly by HAS
quality degradation in the nonnominal service area. Based on
the above results, we concluded that the ZTD-MAD solution
may be safely used for NWP assimilation, while the quality
of ZTD-B2B and ZTD-HAS (in the Asia–Pacific region) are
still to be improved.
C. ZWD Comparison With IGRA Radiosonde Dataset
To further assess the quality of real-time ZTDs, data from
Fig.6. Mean(circle)andstandarddeviation(bar)ofZTDsestimatedwith
radiosonde stations with horizontal distances of smaller than differentsatelliteorbitandclockproducts.
50 km and height differences of smaller than 200 m are
collected for ZWD calculation according to [5] and [36]. stations based on the availability of radiosonde data. Note
The comparison is then conducted at eight of the GNSS that the radiosonde-derived ZWDs are available twice per
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:35:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 7 -->

ZHOUetal.:REAL-TIMEPRECISEZENITHTROPOSPHERICDELAYESTIMATION 5802011
Fig.7. Timeseriesofreal-timePPPestimatedZWDsatJFNGaswellasZWDsderivedfromnearbyradiosondedata.
day, while the PPP derived ZWDs are computed with much TABLEV
highertemporalresolution,specificallyevery30sinthisstudy. STATISTICSOFREAL-TIMEZWDSOLUTIONS
Therefore, the comparison is only conducted when both PPP
COMPAREDTORADIOSONDE(UNITS:mm)
derived ZWDs and radiosonde-derived ZWDs are available,
andthestatisticsoftheobtaineddifferencesarethencalculated
accordingly.
The time series of the PPP estimated ZWDs at JFNG and
radiosonde-derived ZWDs are plotted in Fig. 7. The results
showthattheZWDsvaryfrom0.1to0.6mduringtheselected
period. The real-time ZWDs and the radiosonde-derived
ZWDs at JFNG are generally consistent over time, and the
meanandSTDare−0.1and30.2mmforZTD-B2Bsolution,
−2.5and35.8mmforZTD-HASsolution,−7.4and24.7mm
for ZTD-MAD solution, and −5.7 and 24.4 mm for ZTD-
WUM solution, respectively. The corresponding correlation
coefficients are 0.913, 0.890, 0.943, and 0.944. The results
indicate that there are large biases and variations over time
between the PPP estimated ZWDs and the radiosonde-derived
ZWDs,whichareexpectedasthespatialcorrelationofZWDs,
are significantlydegraded with horizontaldistance of43.3 km
between JFNG (GNSS) and 57494 (radiosonde).
The statistics of the differences of real-time PPP estimated
ZWDsandtheradiosonde-derivedZWDsareplottedinFig.8,
and the mean of the statistics is provided in Table V. It can
be seen that the consistency are the best at ULAB and
URUM. The results reveal that there are no significant biases
between the estimated ZWDs and the radiosonde-derived
ZWDs.Meanwhile,therearelargevariationsinthedifferences
of the real-time PPP estimated ZWDs and radiosonde-derived Fig. 8. STDs of ZWDs estimated with different satellite orbit and clock
productscomparedtoradiosonde-derivedZWDs.
ZWDs, which could be attributed to many factors, such as
the spatial correlation degradation of ZWDs between the
GNSS and radiosonde stations due to the large horizontal
D. ZWD Comparison With ERA5 Dataset
distances. The quality variation of real-time ZWDs as already
been revealed in Section III-B also contribute significantly Tofurtherverifythequalityofreal-timePPPderivedZWDs,
to the large STDs. Overall, the quality of the real-time PPP the ECMWF ERA5 hourly variables of geopotential, relative
estimated ZWDs using MADOCA-PPP and WUM satellite humidity,andtemperatureateachofthe37pressurelevelsare
orbit and clock products is comparable, with mean RMSEs of collected. Since the ERA5 data are provided with a resolution
20.8 and 20.2 mm, while those for ZTD-B2B and ZTD-HAS of 0.25◦ latitude by 0.25◦ longitude, the obtained ERA5 data
are 25.7 and 26.2 mm, respectively. are interpolated to the GNSS station to compute the hourly
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:35:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 8 -->

5802011 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.62,2024
Fig.9. Real-timePPPestimatedZWDsagainstZWDsderivedfromERA5atJFNG.
ZWDs[37].Similarly,thedifferencesofPPPestimatedZWDs TABLEVI
and ERA5-derived ZWDs are calculated when both datasets STATISTICSOFREAL-TIMEZWDSOLUTIONS
are available, which are then used for the computation of
COMPAREDTOERA5(UNITS:mm)
various statistics, including mean, STD, and RMSE.
The real-time PPP estimated ZWDs at JFNG and the cor-
responding ERA5-derived ZWDs are plotted in Fig. 9. The
results show that the real-time PPP estimated ZWDs and the
ERA5-derived ZWDs at JFNG are highly correlated, with
correlation coefficients of 0.911, 0.895, 0.938, and 0.945 for
ZTD-B2B, ZTD-HAS, ZTD-MAD, and ZTD-WUM, respec-
tively, and the corresponding STDs are 28.4, 32.2, 25.1, and
24.2 mm, respectively. The results further confirms that the
qualityoftheZTD-MADisthebestamongthethreereal-time
PPP derived ZWD solutions, which is comparable to the
qualityofZTD-WUMderivedusingpostprocessedIGSWUM STDsaregenerallysmallerthan30mmatmostofthestations,
products. which indicates high consistency between the real-time PPP
The STDs of the differences of real-time PPP estimated estimated ZWDs and the ERA5-derived ZWDs. Overall, it is
ZWDs and the ERA5-derived ZWDs are plotted in Fig. 10, observedthatthequalityofZTD-MADiscomparabletothose
and the mean of the statistics is provided in Table VI. It can of ZTD-WUM, but it is significantly better than those of
be seen that the consistency is the best at ULAB, with STDs ZTD-B2B and ZTD-HAS, with mean RMSEs of 28.2, 24.6,
of 14.9 mm for ZTD-B2B, 19.7 mm for ZTD-HAS, 14.0 mm 19.8,and19.6mmforZTD-B2B,ZTD-HAS,ZTD-MAD,and
for ZTD-MAD, and 13.8 mm for ZTD-WUM solutions. The ZTD-WUM, respectively.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:35:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 9 -->

ZHOUetal.:REAL-TIMEPRECISEZENITHTROPOSPHERICDELAYESTIMATION 5802011
Fig.10. STDsofreal-timePPPestimatedZWDscomparedtoERA5derivedZWDs.
IV. CONCLUSION The real-time PPP estimated ZWDs are compared with
ZWDs derived from IGRA radiosonde and ECMWF
The freely and openly accessible GNSS satellite-based PPP
ERA5 datasets. It is found that the mean STDs are
augmentationserviceshavebeenconsideredasacost-effective
smaller than 30 mm for all the three real-time ZTD
alternative to obtain real-time precise ZTD estimates at
solutions, which highlights its consistency with com-
reducedcoststosupportvariousemergingatmosphericremote
monlyusedatmosphericproducts.SincePPP-B2b,HAS,
sensing applications. This article presents the methodologies
and MADOCA-PPP are all disseminated by navigation
and comprehensive performance assessment of real-time ZTD
satellite signals, no external communication links or
estimation with all the three operational GNSS satellite-based
service subscription fees are required at the user to
real-timePPPaugmentationservices,andthemainconclusions
obtain real-time precise ZTDs. Considering that dense
can be summarized as follows.
GNSS networks are available globally thanks to the
1) How to Estimate Real-Time Precise ZTDs With GNSS
development of continuously operating reference sta-
Satellite-Based Real-Time PPP Augmentation Correc-
tions (CORSs), the proposed real-time ZTD estimation
tionServices?Real-timepreciseZTDscanbeestimated
procedures are therefore expected to provide real-time
with dual-frequency ionospheric-free PPP observation
preciseZWDs/ZTDswithhighspatiotemporalresolution
model following data processing strategies provided in
in all-weather conditions to support time-critical atmo-
Table II. Furthermore, the scope of this work could
spheric remote sensing applications on a routine basis.
be significantly expanded by incorporating alternative
The GNSS satellite-based PPP augmentation services are
real-time PPP observation models (e.g., uncombined
continuously being evolved in many aspects, such as the
PPP/triple-frequency PPP/quad-frequency PPP models).
improvementofproductquality,theexpansionofservicearea,
2) IsItPossibletoEstimateHighlyAvailableandAccurate
as well as the incorporation of carrier phase bias corrections
Real-Time Precise ZTDs? Do They Meet the Threshold
to support real-time PPP ambiguity resolution [28] and so
(15 mm) and Target (10 mm) Accuracy Requirement for
on. It is expected that the quality of the obtained real-time
NWP Assimilation? On the one hand, highly available
(>99%) real-time precise ZTDs can be obtained for ZWDs/ZTDs with GNSS satellite-based PPP augmentation
services will be improved over time, which will play an
all the three services. On the other hand, when using
increasingly important role in atmospheric remote sensing
IGS final ZTD products as the references, the STDs of
applications.
real-time ZTDs are 20.0, 17.5, and 9.5 mm for PPP-
B2b, HAS, and MADOCA-PPP, respectively. Overall,
the quality of the real-time ZWDs/ZTDs derived with ACKNOWLEDGMENT
MADOCA-PPP is comparable to those derived with The authors would like to thank the International GNSS
postprocessed IGS WUM products and is significantly Service (IGS) for providing the GNSS data and products,
betterthanthosederivedwithPPP-B2bandHAS.There- the National Climatic Data Center (NCDC) for providing the
fore, the real-time ZTDs obtained with MADOCA-PPP Integrated Global Radiosonde Archive (IGRA) dataset, and
may be safely used for NWP assimilation, while that the European Centre for Medium-Range Weather Forecasts
obtainedwithPPP-B2bandHASsuffersfromsignificant (ECMWF) for providing the Reanalysis v5 (ERA5) dataset.
variations and should be further improved. It is noted
that however, Galileo HAS may suffer from quality
REFERENCES
degradationconsideringthattheselecteddatasetsareall
located in the nonnominal service area. [1] M. Bevis, S. Businger, T. A. Herring, C. Rocken, R. A. Anthes, and
R.H.Ware,“GPSmeteorology:Remotesensingofatmosphericwater
3) HowDoestheAccuracyoftheReal-TimePPPEstimated
vapor using the global positioning system,” J. Geophys. Res., Atmos.,
ZTDs Compared to Existing Atmospheric Products? vol.97,no.D14,pp.15787–15801,Oct.1992,doi:10.1029/92jd01517.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:35:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 10 -->

5802011 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.62,2024
[2] Q. Zhao, K. Liu, T. Sun, Y. Yao, and Z. Li, “A novel regional [22] H. Kan, Z. Hu, G. Chen, X. Liu, C. Liu, and Q. Zhao, “Performance
drought monitoring method using GNSS-derived ZTD and precipita- comparison of orbit and clock augmentation corrections from PPP-
tion,”RemoteSens.Environ.,vol.297,Nov.2023,Art.no.113778,doi: b2b, HAS and CLAS,” Adv. Space Res., vol. 74, no. 2, pp.668–681,
10.1016/j.rse.2023.113778. Jul.2024,doi:10.1016/j.asr.2024.04.029.
[3] Z. Wu et al., “Real-time GNSS tropospheric delay estimation with a [23] J. Tang, D. Lyu, F. Zeng, Y. Ge, and R. Zhang, “Comprehensive
novelglobalrandomwalkprocessingnoisemodel(GRM),”J.Geodesy, analysis of PPP-B2b service and its impact on BDS-3/GPS real-time
vol.97,no.12,p.112,Dec.2023,doi:10.1007/s00190-023-01780-8. PPP time transfer,” Remote Sens., vol. 14, no. 21, p.5366, Oct. 2022,
[4] C. He, A. Pollet, D. Coulot, V. Schott-Guilmault, and F. Perosanz, doi:10.3390/rs14215366.
“Towards the tropospheric ties in the GPS, DORIS, and VLBI com- [24] Y.Xu,P.Zhao,J.Wang,andX.Meng,“PerformanceassessofBDS-3
binationanalysisduringCONT14,”J.Geodesy,vol.97,no.12,p.111, PPP-B2b signal service and its application in precipitable water vapor
Dec.2023,doi:10.1007/s00190-023-01803-4. retrieval,” in Proc. China Satell. Navigat. Conf. (CSNC), in Lecture
[5] A. E. Niell et al., “Comparison of measurements of atmospheric Notes in Electrical Engineering, vol. 1092, C. Yang and J. Xie, Eds.,
wet delay by radiosonde, water vapor radiometer, GPS, and VLBI,” Singapore:Springer,2024,pp.118–131,doi:10.1007/978-981-99-6928-
J.Atmos.Ocean.Technol.,vol.18,no.6,pp.830–850,Jun.2001,doi: 9_11.
10.1175/1520-0426(2001)018<0830:COMOAW>2.0.CO;2. [25] H.Yang,X.He,V.Ferreira,S.Ji,Y.Xu,andS.Song,“Assessmentof
precipitable water vapor retrieved from precise point positioning with
[6] Q.Zhaoetal.,“Ahigh-precisionZTDinterpolationmethodconsidering
PPP-B2b service,” Earth Sci. Informat., vol. 16, no. 1, pp.315–328,
large area and height differences,” GPS Solutions, vol. 28, no. 1, p.4,
Mar.2023,doi:10.1007/s12145-023-00939-3.
Jan.2024,doi:10.1007/s10291-023-01547-w.
[26] T. Hadas, K. Kazmierski, I. Kudłacik, G. Marut, and S. Madraszek,
[7] P. Zhou, J. Wang, Z. Nie, and Y. Gao, “Estimation and representation
“Galileohighaccuracyserviceinreal-timePNT,geoscienceandmoni-
of regional atmospheric corrections for augmenting real-time single-
toringapplications,”IEEEGeosci.RemoteSens.Lett.,vol.21,pp.1–5,
frequency PPP,” GPS Solutions, vol. 24, no. 1, p.7, Jan. 2020, doi:
2024,doi:10.1109/LGRS.2024.3354293.
10.1007/s10291-019-0920-5.
[27] BeiDou Navigation Satellite System Signal in Space Interface Control
[8] F.Zhou,X.Cao,Y.Ge,andW.Li,“Assessmentofthepositioningper-
Document Precise Point Positioning Service Signal PPP-B2b (Version
formanceandtroposphericdelayretrievalwithprecisepointpositioning
1.0),CSNO,Beijing,China,2020.
usingproductsfromdifferentanalysiscenters,”GPSSolutions,vol.24,
[28] GalileoHighAccuracyServiceSignal-in-SpaceInterfaceControlDoc-
no.1,p.12,Jan.2020,doi:10.1007/s10291-019-0925-0.
ument(HASSISICD),EU,Brussels,Belgium,2022.
[9] C. Lu et al., “Real-time retrieval of precipitable water vapor from
[29] P.TeunissenandO.Montenbruck,SpringerHandbookofGlobalNavi-
Galileo observations by using the MGEX network,” IEEE Trans.
gationSatelliteSystems.Berlin,Germany:Springer,2017.
Geosci. Remote Sens., vol. 58, no. 7, pp.4743–4753, Jul. 2020, doi:
[30] J.Saastamoinen,“Atmosphericcorrectionforthetroposphereandstrato-
10.1109/TGRS.2020.2966774.
sphere in radio ranging satellites,” Use Artif. Satell. Geodesy, vol. 15,
[10] N. Dymarska et al., “An assessment of the quality of near-real time
pp.247–251,Jan.1972.
GNSS observations as a potential data source for meteorology,” Mete-
[31] Y.Yang,W.Gao,S.Guo,Y.Mao,andY.Yang,“IntroductiontoBeiDou-
orol. Hydrol. Water Manage., vol. 5, no. 1, pp.3–13, Jan. 2017, doi:
3 navigation satellite system,” Navigation, vol. 66, no. 1, pp.7–18,
10.26491/mhwm/65146.
Jan.2019,doi:10.1002/navi.291.
[11] Y.Fan,F.Xia,S.Ye,F.Hu,H.Luo,andZ.Sha,“AnalysisofGNSS-ZTD
[32] R. Schmid, P. Steigenberger, G. Gendt, M. Ge, and M. Rothacher,
retrievalusingdual-frequencyrawobservations,”Measurement,vol.231,
“Generation of a consistent absolute phase-center correction model
May2024,Art.no.114597,doi:10.1016/j.measurement.2024.114597.
for GPS receiver and satellite antennas,” J. Geodesy, vol. 81, no. 12,
[12] T. Hadas and T. Hobiger, “Benefits of using Galileo for real-time
pp.781–798,Nov.2007,doi:10.1007/s00190-007-0148-y.
GNSSmeteorology,”IEEEGeosci.RemoteSens.Lett.,vol.18,no.10,
[33] J. T. Wu, S. C. Wu, G. A. Hajj, W. I. Bertiger, and S. M. Lichten,
pp.1756–1760,Oct.2021,doi:10.1109/LGRS.2020.3007138.
“Effects of antenna orientation on GPS carrier phase,” Presented at
[13] P. Zhou, H. Yang, G. Xiao, L. Du, and Y. Gao, “Estimation the AAS/AIAA Astrodynamics Conf., Durango, CO, USA, Jan. 1992.
of GPS LNAV based on IGS products for real-time PPP,” GPS [Online].Available:https://ntrs.nasa.gov/citations/19920060722
Solutions, vol. 23, no. 1, pp.1–14, Jan. 2019, doi: 10.1007/
[34] G. Petit and B. Luzum, “IERS conventions (2010),” Tech. Rep. DTIC
s10291-018-0820-0.
Document,vol.36,p.180,Jan.2010.
[14] H.Li,X.Li,andQ.Kang,“HandlingmethodforoutagesofIGSreal-
[35] J.Böhm,G.Möller,M.Schindelegger,G.Pain,andR.Weber,“Develop-
time service (RTS) in GNSS real-time sensing of atmospheric water
mentofanimprovedempiricalmodelforslantdelaysinthetroposphere
vapor,”IEEEJ.Sel.TopicsAppl.EarthObserv.RemoteSens.,vol.16,
(GPT2w),”GPSSolutions,vol.19,no.3,pp.433–441,Jul.2015,doi:
pp.8310–8318,2023,doi:10.1109/jstars.2023.3312514.
10.1007/s10291-014-0403-7.
[15] X.Chenetal.,“TrimbleRTX,aninnovativenewapproachfornetwork [36] W. Zhang et al., “The use of ground-based GPS precipitable water
RTK,” in Proc. 24th Int. Tech. Meeting Satell. Division Inst. Navigat., measurementsoverChinatoassessradiosondeandERA-interimmois-
2011,pp.2214–2219. turetrendsanderrorsfrom1999to2015,”J.Climate,vol.30,no.19,
[16] C. Ozer Yigit et al., “Assessment of real-time PPP with trimble RTX pp.7643–7667,Oct.2017,doi:10.1175/jcli-d-16-0591.1.
correctionserviceforreal-timedynamicdisplacementmonitoringbased [37] W.Yang,Z.Chen,K.Lv,P.Xia,andT.Lu,“TheGNSSPWVretrieval
on high-rate GNSS observations,” Measurement, vol. 201, Sep. 2022, using non-observation meteorological parameters based on ERA5 and
Art.no.111704,doi:10.1016/j.measurement.2022.111704. its relation with precipitation,” Geodesy Geodynamics, vol. 15, no. 3,
[17] L. Pan, M. Deng, and B. Chen, “Real-time GNSS meteorology: A pp.302–313,May2024,doi:10.1016/j.geog.2023.09.002.
promisingalternativeusingreal-timePPPtechniquebasedonbroadcast
ephemeridesandtheopenserviceofGalileo,”GPSSolutions,vol.28,
no.3,p.113,Jul.2024,doi:10.1007/s10291-024-01659-x.
[18] O.Montenbruck,F.Kunzi,andA.Hauschild,“Performanceassessment
ofGNSS-basedreal-timenavigationfortheSentinel-6spacecraft,”GPS
Solutions, vol. 26, no. 1, p.12, Nov. 2021, doi: 10.1007/s10291-021-
01198-9.
[19] Z. Nie, X. Xu, Z. Wang, and J. Du, “Initial assessment of BDS
PPP-B2b service: Precision of orbit and clock corrections, and PPP
performance,” Remote Sens., vol. 13, no. 11, p.2050, May 2021, doi: Peiyuan Zhou received the Ph.D. degree from the
10.3390/rs13112050. UniversityofCalgary,Calgary,AB,Canada.
He is currently a Lecturer at Information Engi-
[20] Cabinet Office. (2023). Quasi-Zenith Satellite System Interface
neeringUniversity,Zhengzhou,China.Hisresearch
Specification Multi-GNSS Advanced Orbit and Clock Augmentation—
interests include GNSS precise positioning and
PrecisePointPositioning.Accessed:May7,2024.[Online].Available:
remotesensing.
https://qzss.go.jp/en/technical/download/pdf/ps-is-qzss/is-qzss-mdc-
002.pdf?t=1715054623305
[21] P.Zhou,G.Xiao,andL.Du,“InitialperformanceassessmentofGalileo
high accuracy service with software-defined receiver,” GPS Solutions,
vol.28,no.2,p.2,2024,doi:10.1007/s10291-023-01540-3.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:35:28 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE: 11 -->

ZHOUetal.:REAL-TIMEPRECISEZENITHTROPOSPHERICDELAYESTIMATION 5802011
Zhongkai Zhang received the Ph.D. degree in Guorui Xiao received the B.Sc. degree from the
space geodesy from the University of Bonn, Bonn, SchoolofGeodesyandGeomatics,WuhanUniver-
Germany. sity, Wuhan, China, and the Ph.D. degree from the
He is currently an Associate Professor at Infor- Geodetic Institute, Karlsruhe Institute of Technol-
mation Engineering University, Zhengzhou, China. ogy,Karlsruhe,Germany.
Hisresearchinterestsincludesatellitenavigationand HeiscurrentlyanAssociateProfessoratInforma-
astrodynamics. tionEngineeringUniversity,Zhengzhou,China.His
researchinterestsincludemulti-GNSSandmultisen-
sorintegratedprecisepositioningandapplications.
Zejun Liu received the Ph.D. degree in aerospace KaiXiaoreceivedthePh.D.degreeinsurveyingand
science and engineering from the National Univer- mapping from Information Engineering University,
sityofDefenseTechnology,Changsha,China. Zhengzhou,China.
He is currently an Associate Professor at Infor- He is currently an Associate Professor at Infor-
mation Engineering University, Zhengzhou, China. mation Engineering University. His research inter-
Hisresearchinterestsincludesatellitenavigationand estsincludeGNSS/multisourcedataprocessingand
astrodynamics. GNSSanti-spoofing.
Daqian Lyu received the Ph.D. degree in LanDureceivedthePh.D.degreeingeodesyfrom
information and communication engineering from Information Engineering University, Zhengzhou,
the National University of Defense Technology, China.
Changsha,China. She is a Professor at Information Engineering
HeiscurrentlyaLectureratNationalUniversityof University. Her research interests include satellite
Defense Technology. His research interests include navigation,spacegeodesy,andastrodynamics.
GNSSprecisepositioningandtimetransfer.
Authorized licensed use limited to: HANGZHOU DIANZI UNIVERSITY. Downloaded on May 22,2026 at 06:35:28 UTC from IEEE Xplore. Restrictions apply.