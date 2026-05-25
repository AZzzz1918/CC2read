<!-- PAGE: 1 -->

# Uncombined PPP with BDS-3 Multi-Frequency Observations

Chen Li, Wei Zhang

## Abstract

This paper presents an uncombined PPP model using BDS-3 B1I/B3I/B2b multi-frequency observations.

<!-- PAGE: 2 -->

## Mathematical Model

The observation equations for uncombined PPP are:

P_i = rho + c*dt_r - c*dt^s + T + I_i + b_r,i - b_i^s + epsilon

where I_i is the slant ionospheric delay on frequency i, b_r,i is the receiver code bias, and b_i^s is the satellite code bias. The ionospheric delay is estimated as unknown parameter.

The stochastic model uses elevation-dependent weighting with sigma^2 = a^2 + b^2/sin^2(elev). No specific DCB product is mentioned for code bias handling.
