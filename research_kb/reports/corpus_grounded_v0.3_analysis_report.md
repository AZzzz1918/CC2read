# Corpus Grounded v0.3 — 37-Paper Baseline Analysis

**Date:** 2026-05-22

---

## 1. Product Source 分布

| Value | Count | % |
|-------|-------|---|
| BDS3_PPP_B2B_BROADCAST | 25 | 67.6% |
| MIXED_PRODUCTS | 7 | 18.9% |
| CNES_OR_OTHER_RTS | 3 | 8.1% |
| QZSS_CLAS | 2 | 5.4% |

### 分类粒度不足
- **Galileo HAS 无独立类别** — 3 篇 CNES_OR_OTHER_RTS 混合了 Galileo HAS (Borio GHASP, Zhou Peiyuan) 和 general PPP (Liu Wei)。建议细分。
- **CNES vs RTS vs HAS vs CLAS 混用** — CNES_OR_OTHER_RTS 语义模糊。实际内容覆盖 Galileo HAS + general PPP。
- **QZSS_CLAS 仅 2 篇** — 覆盖不足。

## 2. 技术路线分析

### 路线分布

| 路线 | 论文数 | 代表论文 |
|------|--------|----------|
| PPP-B2b 定位性能 | 15+ | Yan Liu 2022, Tang Chenggan 2022, Nie 2021, Peida Wu 2023 |
| PPP-B2b 授时 | 3 | Quad-Frequency, Single-Frequency, Comparative Broadcast |
| PPP-B2b ZTD/PWV | 4 | Zhou Linghao 2025, Wang 2024, Oceanic PWV, RT ZTD |
| PPP-B2b 组合 (INS/factor graph) | 1 | Factor Graph PPP-B2b/INS |
| B2b/HAS/CLAS/RTS 对比 | 7 | Pan Lin 2025, Wei Haopeng 2024, Comparative, RT ZTD, RT Orbit LEO |
| Toolbox/Decoder | 3 | GKit SSRDecoder, Zhao Lewen NavDecoder, Lu 2021 SDR |
| 地震监测 | 1 | Jianfei Zang 2024 |
| 轨道/钟差生成 | 1 | Tang Chenggan 2022 |

### 路线缺失
- **PPP-AR (ambiguity resolution) with B2b**: 0 篇
- **PPP-RTK with B2b**: 0 篇
- **Multi-constellation beyond GPS+BDS**: 少（仅 MIXED 论文覆盖）

## 3. 问题演化

| 时期 | 论文数 | 主要关注 |
|------|--------|----------|
| 2020-2021 | 3 | BDS-3 PPP-B2b 初始评估、SDR 解码 |
| 2022-2023 | 10 | 全面性能评估、实时 PPP、系统原理、HAS 初现 |
| 2024-2025 | 18 | 低成本设备、HAS/B2b 对比、组合增强、工具化、下游应用 |
| year=0 | 6 | DOI-only 论文（year 未从 markdown 提取） |

**趋势：从系统验证 (2020-2022) → 性能对比 (2023-2024) → 应用落地 (2024-2025)。**

## 4. 方法谱系

| 方法 | 论文数 |
|------|--------|
| Ionosphere-free PPP | 25+ |
| Kalman filter estimation | 10+ |
| SISRE evaluation | 15+ |
| PPP time transfer | 3 |
| PWV/ZTD retrieval | 4 |
| Factor graph optimization | 1 |
| SDR decoding | 1 |
| Helmert coordinate transformation | 1 |

## 5. 可复现性分析

| 维度 | 最佳 | 最差 |
|------|------|------|
| 代码开源 | Zhao Lewen (NavDecoder), GKit SSRDecoder | 大部分论文无代码 |
| 数据公开 | IGS MGEX stations 普遍使用 | PPP-B2b correction archive 几乎无公开 |
| 产品路径 | GFZ/CAS/WHU products 可获取 | BDS-3 GEO broadcast stream 不可获取 |
| 参数完整 | 少数 (Tang Chenggan 轨道策略详细) | 多数缺失 Kalman filter/PF 配置 |

### 复现就绪度评分

| 分数 | 论文数 | 说明 |
|------|--------|------|
| 4-5 | 2 | Toolbox 论文（软件开源） |
| 2-3 | 8 | 方法详细但数据/校正流不可得 |
| 0-1 | 27 | 主要 blocker：数据不可得 + 参数缺失 |

## 6. 关键发现

1. **BDS3_PPP_B2B_BROADCAST 占比 67.6%** — corpus 偏向核心 B2b 论文。这是预期的（项目目标是 PPP-B2b 审计）。
2. **12/37 有明确实验日期** — 25/37 为 NOT_MENTIONED。部分是正确的（overview/toolbox 论文），但部分需要在深度提取时补全。
3. **DCB 覆盖不足** — 16/37 标记 NOT_MENTIONED。6/37 有 EXPLICITLY_DESCRIBED。
4. **2024 年论文最多 (15)** — 与 BDS-3 全面运营后研究增长一致。
