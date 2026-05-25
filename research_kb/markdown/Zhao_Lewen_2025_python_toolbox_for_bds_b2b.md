<!-- PAGE: 1 -->

REVIEW
GPS Solutions           (2025) 29:83 
https://doi.org/10.1007/s10291-025-01816-w
communication network support, and two-way communica-
tion with users for broadcasting corrections. Consequently, 
the server’s computational burden increases with the num-
ber of users. In contrast, Precise Point Positioning (PPP) 
(Zumberge et al. 1997) technology can achieve high-pre-
cision positioning globally with just a single station. With 
the availability of the International GNSS Service (IGS) 
real-time service (RTS) (Elsobeiey et al. 2016), it is now 
possible to achieve real-time PPP (RTPPP) using the precise 
satellite orbit and clock corrections. The performance of 
the products provided by various Multi-GNSS Experiment 
(MGEX) analysis centers has been validated, demonstrating 
that their accuracy meets the application needs of most users 
(Li et al. 2022).
Introduction
Real-Time Kinematic (RTK) positioning technology can 
achieve rapid, centimeter-level high-precision position­
ing. However, its quick positioning capability relies on 
However, RTPPP based on RTS still requires the sup-
port of terrestrial 4G and 5G networks, and communication 
delays often affect the positioning accuracy of real-time PPP. 
In contrast, China’s BDS-3 provides real-time corrections 
a dense network of ground reference stations, ground 
	
 Lewen Zhao
lwzhao@nuist.edu.cn
1	
School of Remote Sensing and Geomatics Engineering, 
Nanjing University of Information Science and Technology, 
Nanjing, Jiangsu 210044, China
2	
Technology Innovation Center for Integration Applications 
in Remote Sensing and Navigation, Ministry of Natural 
Resources, Nanjing, Jiangsu 210044, China
3	
Jiangsu Province Engineering Research Center of 
Collaborative Navigation/Positioning and Smart Application, 
Nanjing, Jiangsu 210044, China
 
 
 
 
 
 
Lewen Zhao1,2,3
Received: 28 August 2024 / Accepted: 3 January 2025
© The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2025
Abstract
Precision Point Positioning (PPP) technology can achieve decimeter to centimeter level positioning accuracy, which is 
essential for applications in industries such as autonomous driving, modern agriculture, and drone logistics. The PPP-B2b 
service provided by BDS and the High Accuracy Service (HAS) offered by Galileo, capable of achieving decimeter-level 
accuracy without relying on ground communication networks or commercial augmentation corrections, presents substan-
tial potential for various industries. However, challenges persist when users try to utilize and evaluate these corrections, 
such as the lack of open-source software capable of decoding these products and the absence of product archives necessary 
for such evaluations. To address these challenges, we present a comprehensive Python toolbox called NavDecoder, which 
can decode both PPP-B2b and Galileo HAS products and provide archived data in ASCII format, facilitating its applica-
tion. We also evaluated the accuracy of the two products, using the root mean square (RMS) of signal-in-space range error 
as a metric, with final products from Wuhan University serving as a benchmark. The average RMS was found to be 1.0 m 
for GPS in PPP-B2b and 0.62 m for GPS in Galileo HAS. For BDS in PPP-B2b, the average RMS was 0.67 m, while 
for Galileo in HAS, it was 0.18 m. Then, the accuracy of PPP-B2b and Galileo HAS products were validated using both 
static and kinematic PPP. A forward Kalman filter was employed for static PPP, while a combined forward and backward 
filter was used for kinematic PPP. The results demonstrate that comparable accuracy can be achieved through two posi-
tioning modes. BDS PPP-B2b offers superior positioning accuracy compared to Galileo HAS. Both products achieve an 
accuracy of 0.1 m with hourly PPP, with 4-hour observation periods yielding the most significant accuracy improvements.
Keywords Precise point positioning · PPP-B2b · Galileo · High accuracy service · Open 
Python toolbox for BDS PPP-B2b and Galileo HAS decoding and its 
products performance validation
source
1 3

> [2 Figure(s)]


|To|address t|hese|challenges|
|---|---|---|---|




|for|Col2|GPS|Col4|in|PPP-B2b|Col7|Col8|Col9|Col10|Col11|Col12|0.62 m|Col14|for|GPS|Col17|in|Col19|Galileo|Col21|HAS|Col23|Col24|BDS|Col26|in|Col28|PPP-B2b,|Col30|the|Col32|averag|e|RMS|Col36|was|Col38|0.67 m|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|for<br>|for<br>|Galileo<br>|Galileo<br>|Galileo<br>|in<br>|<br>|HAS,<br>|i<br>|t<br>|was<br>|was<br>|<br>|0.18  <br>|0.18  <br>|0.18  <br>|0.18  <br>|0.18  <br>|0.18  <br>|0.18  <br>|0.18  <br>|0.18  <br>|<br>|PPP-B2b<br>|PPP-B2b<br>|and<br>|and<br>|Galileo<br>|Galileo<br>|HAS<br>|HAS<br>|p<br>|roducts<br>|wer<br>|wer<br>|e v<br>|alidated<br>|alidated<br>|alidated<br>|
|static and kinematic PPP<br>|static and kinematic PPP<br>|static and kinematic PPP<br>|static and kinematic PPP<br>|static and kinematic PPP<br>|static and kinematic PPP<br>|static and kinematic PPP<br>|static and kinematic PPP<br>|static and kinematic PPP<br>|static and kinematic PPP<br>|static and kinematic PPP<br>|. A<br>|. A<br>|forward Kalman flter<br>|forward Kalman flter<br>|forward Kalman flter<br>|forward Kalman flter<br>|forward Kalman flter<br>|forward Kalman flter<br>|forward Kalman flter<br>|forward Kalman flter<br>|forward Kalman flter<br>|forward Kalman flter<br>|forward Kalman flter<br>|forward Kalman flter<br>|forward Kalman flter<br>|tatic PPP,<br>|tatic PPP,<br>|tatic PPP,<br>|tatic PPP,<br>|tatic PPP,<br>|tatic PPP,<br>|tatic PPP,<br>|tatic PPP,<br>|tatic PPP,<br>|tatic PPP,<br>|tatic PPP,<br>|tatic PPP,<br>|tatic PPP,<br>|
|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|<br>flter was used for kinematic PPP<br>|




|with|users f|or broadcasting|corrections|
|---|---|---|---|




|real-time|service|
|---|---|




|satellite|Col2|orbit an|d clock|corrections.|
|---|---|---|---|---|




|their|accurac|y meets|the|application|needs|of|most u|sers|
|---|---|---|---|---|---|---|---|---|




|However, RT|Col2|Col3|PPP|based|Col6|Col7|on|Col9|RTS|still requires the sup-<br>s, and communication|requires|Col13|Col14|the|sup-|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|port<br>|of<br>|terrestrial<br>|4G<br>|and<br>|5G<br>|5G<br>|network<br>|network<br>|network<br>|network<br>|network<br>|communication<br>|communication<br>|communication<br>|communication<br>|
|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|delays often afect the positioning accuracy of real-time PPP.|



<!-- PAGE: 2 -->

GPS Solutions           (2025) 29:83 
accuracy (He et al. 2023; Nie et al. 2021; Tao et al. 2021; 
Naciri et al. 2023; Hauschild et al. 2022
via the GEO (Geostationary Earth Orbit) satellites’ B2b 
signal (PPP-B2b) (China Satellite Navigation Office 2020). 
According to the design, the structure of the BDS-3 PPP-
B2b signal can encode State Space Representation (SSR) 
corrections for BDS, GPS, GLONASS, and Galileo. How-
ever, currently, only SSR corrections for BDS-3 and GPS 
are broadcasted for users in and around China. Additionally, 
the High-Accuracy Service (HAS) provided by Galileo’s 
E6-B(European Union 2022) signal offers corrections for 
standard global PPP service and regional rapid positioning 
service. Relevant scholars have analyzed the availability 
and accuracy of correction products provided by both prod-
).
The formats of the messages received by PPP-B2b and 
Galileo HAS differ from the standard Radio Technical 
Commission for Maritime Services (RTCM) format due 
to restrictions on baud rate and ensuring the completeness 
of the broadcast corrections. For PPP-B2b messages, each 
message is 486 bits long and is encoded into 972 symbols 
using 64-ary Low Density Parity Check (64-ary LDPC). 
After LDPC decoding and CRC, the PPP service informa-
tion can be extracted. For Galileo HAS, a high-parity ver-
tical reed-solomon (HPVRS) encoding scheme is adopted 
(Fernández-Hernández et al. 2020), the decoding procedure 
is also required to recover the HAS corrections.
To support the decoding of raw messages for the evalu-
ation and application of real-time augmented PPP services, 
researchers have developed various open-source tools. 
Horst et al. (2022) introduced an open-source Python-based 
HAS decoder named HASlib. Further research has also 
concentrated on decoding Galileo HAS and integrating it 
with open processing packages (Prol et al. 2024; Borio et al. 
2023; Zhang et al. 2024). Additionally, Hirokawa provided 
a comprehensive Python tool called CSSRlib(Hirokawa et 
al. 2023), capable of performing RTK and PPP/PPP-RTK 
positioning using Receiver Independent Exchange Format 
(RINEX) (Gurtner et al. 2007) or correction data format-
ted in Compact SSR format. Moreover, an open-source 
software-defined radio (SDR) receiver was provided by 
Takasu (Ozeki et al. 2023; Tomoji 2022), which offers func-
tionality for decoding GNSS raw messages from satellites. 
However, the decoding modules in these two packages are 
not specifically designed for satellite-based PPP augmenta-
tion information, and the decoding of PPP-B2b has not been 
thoroughly demonstrated.
In response to these limitations, we have developed a 
Python-based toolkit, partially leveraging functions from 
CSSRlib and pocketSDR, to decode PPP-B2b and Galileo 
HAS messages. The decoded corrections are saved in a 
 
ucts, demonstrating that after a certain convergence time, 
Workflow 
they can meet decimeter to centimeter-level positioning
format compatible with the corrections format from BKG 
Ntrip Client (BNC) software (Weber et al. 2007), and an 
archive in plain ASCII format is provided for users to 
quickly assess the performance of these corrections. The 
remaining sections are organized as follows: first, we intro-
duce the details of the decoder toolkit, outlining its flow and 
characteristics; next, we evaluate the performance of the 
decoded orbits and clocks using final products from Wuhan 
University as a reference; finally, we assess the performance 
of both static and kinematic PPP.
 
NavCm is the in-house software designed to support both 
real-time and post-processing PPP and RTK applications. 
A key component, NavDecoder, is responsible for decoding 
various correction formats, including RTCM, Galileo HAS, 
and BDS PPP-B2b, to recover the plain format of the cor-
rections for simulated real-time processing or to feed the 
real-time engine. The architecture of the NavDecoder is 
shown in Fig. 1.
 
 
 
 
 
The module starts with downloading navigation messages 
in RINEX 3.X and RINEX 4.X formats, as well as real-time 
product archives from Centre National d´Etudes Spatiales 
(CNES) and rapid products from Wuhan University. These 
downloads are essential for evaluating the accuracy of PPP 
using satellite-based corrections, IGS MGEX real-time 
streams, and rapid products. Once the data is downloaded, 
the RINEX 3.X navigation files, together with Galileo HAS 
binary corrections, are used as inputs for the Galileo HAS 
decoder. Similarly, RINEX 4.X navigation files are used for 
BDS, where CNAV1 messages are processed along with 
PPP-B2b correction messages in the decoder.
In addition, two parameters, “max_age_clocks” and 
“max_age_orbits”, must be configured to manage the syn­
chronization of different types of corrections as well as the 
alignment between the corrections and the broadcast ephem­
eris. By default, PPP-B2b messages update clock correc­
tions every 6 s and orbit corrections every 48 s, while for 
Galileo HAS, clock corrections are updated every 10 s, and 
orbit corrections every 50 s. Although these corrections are 
generally consistent, discrepancies may occur due to miss­
ing correction products or ephemeris IOD (Issue of Data) 
switches. To ensure the continuity of PPP positioning, the 
NavDecoder considers both the matching of IOD param­
eters and the stability of orbit and clock products. Missing 
corrections are specifically addressed within a 300-second 
window for orbits and a 60-second window for clocks, 
achieved by the default settings of max_age_clocks=60 and 
max_age_orbits=300.
1 3
   83 
 
Page 2 of 10


|According to the design, th<br>B2b signal can encode Sta<br>corrections for BDS, GPS,<br>ever, currently, only SSR c<br>are broadcasted for users in|e structure of the BDS-3|PPP-|
|---|---|---|
|<br>According to the design, th<br>B2b signal can encode Sta<br>corrections for BDS, GPS,<br>ever, currently, only SSR c<br>are broadcasted for users in|te Space Representation (|SSR)|
|<br>According to the design, th<br>B2b signal can encode Sta<br>corrections for BDS, GPS,<br>ever, currently, only SSR c<br>are broadcasted for users in|GLONASS, and Galileo. How-|GLONASS, and Galileo. How-|
|<br>According to the design, th<br>B2b signal can encode Sta<br>corrections for BDS, GPS,<br>ever, currently, only SSR c<br>are broadcasted for users in|orrections for BDS-3 and|GPS|
|<br>According to the design, th<br>B2b signal can encode Sta<br>corrections for BDS, GPS,<br>ever, currently, only SSR c<br>are broadcasted for users in|and around China. Additionally,|and around China. Additionally,|
|the High-Accuracy Service<br>|(HAS) provided by Galileo’s<br>|(HAS) provided by Galileo’s<br>|
|E6-B(European Union202|2) signal ofers corrections for|2) signal ofers corrections for|




|duce|the details of the decoder toolkit|Col3|
|---|---|---|
|<br>characteristics<br>|<br>characteristics<br>|<br>characteristics<br>|
|decoded orbits and clocks<br>|decoded orbits and clocks<br>|decoded orbits and clocks<br>|
|<br>University|<br>University|<br> as a reference|




|is|responsible|for|decoding|
|---|---|---|---|




|Galileo HAS differ from|the standard Radio Technical|Col3|
|---|---|---|
|<br>Commission for Maritime|<br>   Services (RTCM) format|<br>      due|




|various|correction|formats|
|---|---|---|




|of the broadcast corrections|. For PPP-B2b messages,|each|
|---|---|---|
|message is 486 bits long an|d is encoded into 972 symbols|d is encoded into 972 symbols|
|using 64-ary Low Density|Parity Check (64-ary LDPC).|Parity Check (64-ary LDPC).|
|After LDPC decoding and|CRC, the PPP service informa-|CRC, the PPP service informa-|
|tion can be extracted. For|Galileo HAS, a high-parity|ver-|
|tical reed-solomon (HPVR|S) encoding scheme is adopted|S) encoding scheme is adopted|
|(Fernández-Hernández et al|.2020), the decoding procedure|.2020), the decoding procedure|
|is also required to recover th|e HAS corrections.|e HAS corrections.|




|Horst et al. (2022) introduce|d an open-source Python-based|Col3|Col4|
|---|---|---|---|
|HAS decoder named HAS|lib. Further research has also|lib. Further research has also|lib. Further research has also|
|concentrated on decoding|Galileo HAS and integrating|Galileo HAS and integrating|it|
|with open processing packa|ges (Prol et al.2024; Borio et al.<br> dditionally, Hirokawa provided<br>   ol called CSSRlib(Hirokawa et<br>   rming RTK and PPP/PPP-RTK|et|al.|
|2023; Zhang et al.2024). A<br>a comprehensive Python to<br>al.2023), capable of perfo|2023; Zhang et al.2024). A<br>a comprehensive Python to<br>al.2023), capable of perfo|2023; Zhang et al.2024). A<br>a comprehensive Python to<br>al.2023), capable of perfo|2023; Zhang et al.2024). A<br>a comprehensive Python to<br>al.2023), capable of perfo|
|positioning using Receiver|Independent Exchange Format|Independent Exchange Format|Independent Exchange Format|
|(RINEX) (Gurtner et al.20|07) or correction data format-<br>    at. Moreover, an open-source<br>|07) or correction data format-<br>    at. Moreover, an open-source<br>|07) or correction data format-<br>    at. Moreover, an open-source<br>|
|ted in Compact SSR form<br>|ted in Compact SSR form<br>|ted in Compact SSR form<br>|ted in Compact SSR form<br>|




|However, the decoding mo|dules in these two package|s a|re|
|---|---|---|---|
|not specifcally designed for satellite-based PPP augment|not specifcally designed for satellite-based PPP augment|not specifcally designed for satellite-based PPP augment|a-|
|<br>tion information, and the de|<br>    coding of PPP-B2b has not|<br>         been|<br>         been|
|thoroughly demonstrated.|itations, we have developed a|itations, we have developed a|itations, we have developed a|
|In response to these lim|In response to these lim|In response to these lim|In response to these lim|



<!-- PAGE: 3 -->

GPS Solutions           (2025) 29:83 
Once the inputs are configured, the decoding process 
begins. The main decoding functions, which support the 
binary format of the “BDSRawB2b” block and the “GAL­
RawCNAV” block from the Septentrio receiver and utilize 
components from CSSRLIB and Pocket-SDR libraries, have 
been reorganized for better integration, with some exter­
nal code removed. The NavDecoder also supports decod­
ing PPP-B2b plain text output from the Unicore receiver, 
addressing the fact that the raw messages from Septentrio 
do not decode the complex LDPC (162,81).
After decoding, the orbit and clock corrections with the 
matching epoch and IOD are synchronized, saving the data 
in a plain text format consistent with BNC message output. 
The system also supports plain ASCII formats for standard 
SP3 format. However, it is important to note that occasional 
gaps in the corrections for some satellites may occur. Users 
should account for these gaps when using SP3 format file 
for PPP, as interpolating the precise position across these 
gaps may introduce errors.
In summary, the key features of the NavDecoder are as 
follows:
1.	 Download tools for retrieving navigation and MGEX 
orbit/clock products.
2.	 Support for raw binary HAS data from Septentrio GNSS 
receivers: The system can be easily extended to support 
binary data from various manufacturers by extracting 
raw Galileo C/NAV data for input into the decoding 
function.
3.	 Support for PPP-B2b data from Septentrio and Unicore 
GNSS receivers: Septentrio provides raw binary for­
mat, which requires an LDPC decoder to recover plain 
corrections, while Unicore offers plain ASCII format 
that can be directly processed to recover corrections.
4.	 Capability to save corrections in the BNC universal 
format.
5.	 Capability to save corrections in SP3 format.
6.	 Provision of an archive for BDS PPP-B2b and Galileo 
 
 
 
 
 
In comparison, Fig.  4 presents the SISRE errors for 
GPS and Galileo satellites using Galileo HAS corrections. 
The HAS GPS corrections show fewer outliers compared 
to the PPP-B2b GPS corrections. Additionally, the SISRE 
HAS corrections.
Experiments and assessment
Signal-in-space range error assessment
The performance of the BDS PPP-B2b and Galileo HAS 
real-time correction messages was evaluated using the final 
GNSS precise orbit and clock data provided by Wuhan Uni-
versity as the reference. Figure 2 shows the time series of 
Signal-in-Space Range Error (SISRE) for GPS and BDS 
satellites from PPP-B2b products during days 075 to 174 
of the year 2024. The observed gaps in the figure were 
caused by interruptions in data recording due to a tempo-
rary storage capacity issue or power failure. Data record-
ing resumed once the issue was resolved. It is clear that the 
GPS SISRE errors are larger than those of BDS, with 98% 
of the averaged SISRE errors at 2.0 m for GPS and 1.7 m 
for BDS. There are also notable outliers in the GPS SISRE 
error series, with several satellites showing errors exceeding 
6 m. Figure 3 presents the Root Mean Square (RMS) error 
of SISRE for each satellite. The average RMS values are 
1.0 m for GPS and 0.67 m for BDS. Significant variations 
are observed among individual GPS satellites, whereas the 
RMS for BDS satellites is more consistent, primarily below 
1.0 m.
also reveals systematic biases among different satellites, as 
Fig. 1  Architecture of 
NavDecoder
 
1 3
Page 3 of 10 
   83

> [1 Figure(s)]

<!-- PAGE: 4 -->

Fig. 3  The RMS of the SISRE 
errors for GPS and BDS from 
PPP-B2b products respectively
 
Fig. 2  The SISRE error time series for GPS and BDS from PPP-B2b with reference to WUM products. Different colors represent different satellites
 
   83 
 
Page 4 of 10

> [2 Figure(s)]

<!-- PAGE: 5 -->

GPS Solutions           (2025) 29:83 
products. The averaged RMS values are plotted as bars, with 
different colors representing different observation session 
lengths, whereas the repeatability, measured by the stan­
dard deviation, is shown as red error bars on the bar chart. 
Overall, as the observation durations increase, the position­
ing accuracy and repeatability of PPP improve significantly. 
For the hourly PPP solutions, the average positioning accu­
racy is 0.067 m and 0.071 m in the horizontal and vertical 
direction respectively. The horizontal accuracy improves 
to 0.059 m and 0.048 m for 2-hour and 4-hour solutions, 
representing improvements of 15% and 30%, respectively. 
Furthermore, with additional increases in processing length, 
the enhancement in horizontal positioning accuracy and 
repeatability persists but at a diminishing rate. The 6-hour, 
12-hour, and 24-hour solutions achieve average accuracies 
of 0.046 m, 0.042 m, and 0.041 m, respectively. A similar 
trend is also visible in the vertical direction, with the aver­
age vertical positioning accuracy improving to 0.065 m and 
0.056 m for the 2-hour and 4-hour solutions, respectively, 
achieving an average accuracy of approximately 0.05 m for 
observation periods of 12 h or more.
In contrast, Fig. 8 presents the performance of PPP based 
on the GPS and Galileo dual-system combination using the 
indicated by the RMS values in Fig. 5. The average RMS of 
SISRE values is 0.62 m for GPS, which is superior to the 
GPS product provided by PPP-B2b. Galileo satellites show 
smaller RMS values, averaging 0.18 m, and show good con­
sistency across different satellites. Overall, the Galileo HAS 
GPS products demonstrate superior accuracy compared to 
the B2b products.
Static and kinematic PPP assessment
Galileo provides HAS service on a global scale. However, 
the orbit and clock corrections for PPP-B2b are transmitted 
by BDS-3 GEO satellites, with coverage primarily in the 
Asia-Pacific region. To compare the performance of these 
two products, PPP was calculated using MGEX stations 
located in the Asia-Pacific region, as shown in Fig. 6, with 
a data sampling rate of 5 s. All data were processed with 
a dual-frequency ionosphere-free combination. A forward 
Kalman filter and smoothing method were applied. The 
detailed strategies are outlined in Table 1.
Figure 7 illustrates the positioning accuracy and repeat­
ability of static PPP in both horizontal and vertical direc­
tions over different observation durations using PPP-B2b 
Fig. 4  The SISRE error time 
series based on HAS for GPS and 
GAL with reference to WUM 
products. Different colors repre­
sent different satellite
 
1 3
Page 5 of 10 
   83

> [1 Figure(s)]

<!-- PAGE: 6 -->

Galileo HAS product, showing the positioning accuracy for 
various observation durations. For the hourly solution, the 
average positioning accuracies are 0.1 m in the horizontal 
direction and 0.079 m in the vertical direction. The verti­
cal accuracy is better than the horizontal, primarily due to 
the relatively poor eastward accuracy, measured at 0.08 m, 
which is even lower than the vertical accuracy. The hori­
zontal accuracy improves substantially with longer obser­
vation durations, reaching 0.089  m, 0.075  m, 0.068  m, 
0.061 m, and 0.057 m for 2-hour, 4-hour, 6-hour, 12-hour, 
and 24-hour periods, respectively. Similarly, the vertical 
accuracy improves to 0.07 1 m, 0.063 m, 0.059 m, 0.053 m, 
and 0.049  m for the same durations. In comparison with 
PPP-B2b solutions, the Galileo HAS product’s positioning 
accuracy is generally inferior in both horizontal and vertical 
directions.
Fig. 6  MGEX stations used for PPP-B2b and Galileo HAS perfor­
mance evaluation
 
Fig. 5  The RMS of the SISRE 
errors for GPS and Galileo from 
HAS products respectively
 
   83 
 
Page 6 of 10

> [2 Figure(s)]

<!-- PAGE: 7 -->

GPS Solutions           (2025) 29:83 
backward filtering to enhance accuracy during the conver­
gence phase. Figure 9 presents the positioning accuracy 
and repeatability using PPP-B2b products across differ­
ent observation durations. The analysis shows that the 
positioning accuracy of backward filtering is correlated 
with the observation duration. This is primarily because 
with increased convergence time, the tropospheric delay 
and ambiguity parameters estimated by PPP are continu­
ously refined. Overall, a 1-hour dynamic PPP achieves a 
positioning accuracy of 0.072 m horizontally and 0.076 m 
vertically. As the convergence time increases, the 4-hour 
observation duration demonstrates significant improve­
ments, with horizontal and vertical positioning accuracies 
improving to 0.043 m and 0.065 m, respectively. Further 
increases in convergence time result in limited accuracy 
improvements in dynamic PPP. Figure  10 shows the 
positioning accuracy using Galileo HAS products, with 
horizontal and vertical accuracies of 0.11  m/0.097  m, 
0.098 m/0.1 m, and 0.086 m/0.1 m for 1-hour, 2-hour, and 
4-hour durations, respectively.
We further analyze the positioning accuracy of dynamic 
PPP, which employs forward filtering followed by 
Table 1  PPP strategies using PPP-B2b and Galileo HAS products
Items
PPP-B2b products pro­
cessing strategies
Galileo HAS 
products pro­
cessing strategies
Observation 
frequency
GPS: L1/L2
BDS: B1-2/B3
GPS: L1/L2
Galileo: E1/E5a
Satellite orbits/clocks GPS: LNAV + PPP-B2b
BDS: CNAV1 + PPP-B2b
GPS: 
LNAV + HAS
Galileo: I/
NAV + HAS
Weighting scheme
Elevation dependent weighting
Elevation mask
7°
Satellite antenna 
phase center
No correction
Estimation method
Forward Kalman and backward smoothing
Ionospheric delay
Ionosphere-free combination
Tropospheric delay
Zenith wet delay is estimated as random 
walk noise process
Ambiguities
Estimated as float constant
Receiver clock and 
inter-system bias
Estimated as white noise
Fig. 7  Positioning accuracy and 
repeatability of static PPP using 
PPP-B2b across different obser­
vation durations
 
1 3
Page 7 of 10 
   83

> [1 Figure(s)]

<!-- PAGE: 8 -->

Fig. 9  Positioning accuracy and 
repeatability of kinematic PPP 
using PPP-B2b across different 
observation durations
 
Fig. 8  Positioning accuracy and 
repeatability of static PPP using 
Galileo HAS across different 
observation durations
 
Fig. 10  Positioning accuracy and 
repeatability of kinematic PPP 
using Galileo HAS across differ­
ent observation durations
 
   83 
 
Page 8 of 10

> [3 Figure(s)]

<!-- PAGE: 9 -->

GPS Solutions           (2025) 29:83 
Declarations
Ethical approval and consent to participate  Not applicable.
Competing interests  The authors declare no competing interests.
References
Borio D, Susi M, Gioia C (2023) GHASP: a Galileo HAS parser. GPS 
Solutions 27(4):197
China Satellite Navigation Office (2020) BeiDou Navigation Satel­
lite System Signal in Space Interface Control Document Precise 
Point Positioning Service Signal PPP-B2b, China Satellite Navi­
gation Office, China, 2020
Elsobeiey M, Al-Harbi S (2016) Performance of real-time precise 
point positioning using IGS real-time service. GPS Solutions 
20:565–571
European Union (2022) Galileo High Accuracy Service signal-in-
space interface control document. ​h​t​t​p​s​:​/​/​w​w​w​.​g​s​c​-​e​u​r​o​p​a​.​e​u​/​s​
i​t​e​s​/​d​e​f​a​u​l​t​/​f​​i​l​e​s​/​s​i​t​e​s​/​a​l​l​/​f​​i​l​e​s​/​G​a​l​i​l​e​o​_​H​A​S​_​S​I​S​_​I​C​D​_​v​1​.​0​.​p​d​f
Fernández-Hernández I, Senni T, Borio D, Vecchione G (2020) High‐
parity vertical Reed‐Solomon codes for long GNSS high‐accu­
racy messages. Navigation 67(2):365–378
Gurtner W, Estey L (2007) RINEX-the receiver independent exchange 
format-version 3.00[J]. Astronomical Institute, University of 
Bern and UNAVCO, Bolulder, Colorado
Hauschild A, Montenbruck O, Steigenberger P, Martini I, Fernandez-
Hernandez I (2022) Orbit determination of Sentinel-6A using 
the Galileo high accuracy service test signal. GPS Solutions 
26(4):120
He Q, Chen L, Liu L, Zhao D, Gong X, Lou Y, Guan Q (2023) Long-
term performance evaluation of BeiDou PPP-B2b products and 
its application in time service. Remote Sens 15(5):1358
Hirokawa R, Hauschild A, Everett T (2023), September Python Tool­
kit for Open PPP/PPP-RTK Services. In Proceedings of the 36th 
International Technical Meeting of the Satellite Division of The 
Institute of Navigation (ION GNSS + 2023) (pp. 2514–2526)
Horst O, Kirkko-Jaakkola M, Malkamäki T, Kaasalainen S, Fernán­
dez-Hernández I, Chamorro-Moreno A, Cancela-Díaz S (2022) 
HASlib: an Open-Source Decoder for the Galileo High Accuracy 
Service. 2625–2633 ION GNSS 2022, Institute of Navigation, 
Denver, Colorado, USA, September 19–23
Li B, Ge H, Bu Y, Zheng Y, Yuan L (2022) Comprehensive assessment 
of real-time precise products from IGS analysis centers. Satell 
Navig 3(1):12
Naciri N, Yi D, Bisnath S, de Blas FJ, Capua R (2023) Assessment of 
Galileo High Accuracy Service (HAS) test signals and prelimi­
nary positioning performance. GPS Solutions 27(2):73
Nie Z, Xu X, Wang Z, Du J (2021) Initial assessment of BDS PPP-B2b 
service: precision of orbit and clock corrections, and PPP perfor­
mance. Remote Sensing, 13(11), 2050
Ozeki T, Kubo N, Suzuki T, Ebinuma T, Takasu T (2023), Septem­
ber Evaluation of the Actual Performance of PPP in Urban Areas 
Using Pocket SDR. In Proceedings of the 36th International 
Technical Meeting of the Satellite Division of The Institute of 
Navigation (ION GNSS + 2023) (pp. 3488–3498)
Prol F, Kirkko-Jaakkola M, Horst O, Malkamäki T, Bhuiyan M, Kaas­
alainen S, Fernández-Hernández I (2024) Enabling the Galileo 
high accuracy service with open-source software: integration of 
HASlib and RTKLIB. GPS Solutions 28(2):71
Tao J, Liu J, Hu Z, Zhao Q, Chen G, Ju B (2021) Initial assessment of 
the BDS-3 PPP-B2b RTS compared with the CNES RTS. GPS 
Solutions 25:1–16
Conclusion
The open services provided by BDS PPP-B2b and Galileo 
HAS enable decimeter- to centimeter-level positioning for a 
wide range of users, without the need for commercial aug­
mentation. To facilitate the use of these services, a Python-
based toolkit was developed to decode PPP-B2b and Galileo 
HAS messages, partially leveraging functions from CSSR­
lib and pocketSDR. The decoded corrections are saved in 
an ASCII format compatible with BNC software, allowing 
users to quickly assess the performance of these corrections.
Firstly, the performance of PPP-B2b and Galileo HAS 
corrections was evaluated using the final GNSS precise 
orbit and clock data from Wuhan University as the refer­
ence, with the SISRE employed as the metric to account 
for both orbit and clock errors. The results indicate that the 
PPP-B2b corrections yield average RMS values of 1.0 m for 
GPS and 0.67 m for BDS. In contrast, Galileo HAS dem­
onstrated superior accuracy, providing an average RMS of 
0.62 m for GPS and 0.18 m for Galileo satellites.
Subsequently, the performance of PPP was assessed 
using MGEX stations in the Asia-Pacific region, given that 
PPP-B2b is a locally based augmentation service. For static 
PPP, the results show that accuracies better than 0.1 m can 
be achieved with both PPP-B2b and Galileo HAS solutions 
using hourly static PPP. Extended observation periods fur­
ther improve accuracy, with 4-hour durations yielding the 
most significant enhancements, achieving accuracies better 
than 0.05 m for BDS PPP-B2b and 0.08 m for Galileo HAS. 
To achieve an accuracy of 0.05 m in both horizontal and 
vertical directions, at least 12 h of observation are required. 
In kinematic PPP, accuracy comparable to that of static 
PPP can be achieved across varying observation durations 
through the use of backward smoothing.
Acknowledgements  The author gratefully acknowledges the open-
source toolbox cssrlib (​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​h​i​r​o​k​a​w​a​/​c​s​s​r​l​i​b) provided 
by the Hirokawa and PocketSDR provided by Tomoji Takasu (​h​t​t​p​s​:​/​/​
g​i​t​h​u​b​.​c​o​m​/​t​o​m​o​j​i​t​a​k​a​s​u​/​P​o​c​k​e​t​S​D​R).
Author contributions  L.Z. refined the python toolbox and write the 
manuscript.
Funding  This research was funded by the Technology Innovation 
Center for Integrated Applications in Remote Sensing and Naviga­
tion, Ministry of Natural Resources (TICIARSN-2023-01); National 
Natural Science Foundation of China (42104018), China Postdoctoral 
Science Foundation (2022M711669).
Data availability  The Python toolbox and the archived PPP-B2b and 
HAS correction datasets can be found at ​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​N​a​v​S​e​s​n​
e​/​N​a​v​D​e​c​o​d​e​r.
1 3
Page 9 of 10 
   83

<!-- PAGE: 10 -->

Publisher’s note  Springer Nature remains neutral with regard to juris­
dictional claims in published maps and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds 
exclusive rights to this article under a publishing agreement with the 
author(s) or other rightsholder(s); author self-archiving of the accepted 
manuscript version of this article is solely governed by the terms of 
such publishing agreement and applicable law.
Tomoji T (2022) ​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​t​o​m​o​j​i​t​a​k​a​s​u​/​P​o​c​k​e​t​S​D​R
Weber G, Mervart L (2007) The BKG ntrip client (BNC). In Report on 
EUREF symposium. ​h​t​t​p​s​:​/​/​i​g​s​.​b​k​g​.​b​u​n​d​.​d​e​/​n​t​r​i​p​/​b​n​c
Zhang R, Tu R, Lu X (2024) HASPPP: an open-source Galileo 
HAS embeddable RTKLIB decoding package. GPS Solutions 
28(4):169
Zumberge JF, Heflin MB, Jefferson DC, Watkins MM, Webb FH 
(1997) Precise point positioning for the efficient and robust analy­
sis of GPS data from large networks. J Geophys Research: Solid 
Earth 102(B3):5005–5017
   83 
 
Page 10 of 10
