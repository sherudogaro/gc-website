# Monthly Performance Update Process

**Purpose:** Update Glenorchy Capital website with new monthly performance data from IBKR.

**Files to update:**
- `performance.html` - Main performance page (3 tabs)
- `index.html` - Homepage performance snapshot

**Frequency:** Monthly, after month-end close

---

## Step 1: Gather Data from IBKR

Paste your data in this format:

```
MONTH: [Month Year, e.g., November 2025]
DATE FORMAT: [e.g., 30 November 2025]

=== ASYMMETRIC STRATEGY ===

Annualized Returns:
Account           YTD      1 Year   3 Year   5 Year   Since Inception
ACWI              XX.XX    XX.XX    XX.XX    XX.XX    XX.XX
Asymmetric        XX.XX    XX.XX    XX.XX    XX.XX    XX.XX

Total Cumulative Return: XXX%
ACWI Cumulative Return: XXX%

=== DIVIDEND STRATEGY ===

Annualized Returns:
Account           YTD      1 Year   3 Year   Since Inception
DVY               XX.XX    XX.XX    XX.XX    XX.XX
Dividend          XX.XX    XX.XX    XX.XX    XX.XX

Total Cumulative Return: XX%
DVY Cumulative Return: XX%
Dividend Yield (if changed): X.X%
```

---

## Step 2: Calculate Excess Returns

For each period, calculate: **Excess = Strategy Return - Benchmark Return**

Example:
- Strategy YTD: 16.34%
- ACWI YTD: 21.32%
- Excess: 16.34 - 21.32 = -4.98%

**Sign convention:**
- Positive excess: use `+X.XX%` format
- Negative excess: use `-X.XX%` format

---

## Step 3: Update performance.html

### 3.1 Asymmetric Strategy Tab

#### Metric Cards (4 cards at top)
Location: Search for `id="asymmetric-metrics"`

| Card | What to Update |
|------|----------------|
| Total Net Return | Update `+166%` to new total (e.g., `+169%`) |
| Annualized Net Return | Update `18.01%` to new Since Inception value |
| Bear Market Protection | **STATIC** - Don't change (2022 historical data) |
| Outperformance | **Absolute difference:** Strategy Total - Benchmark Total (e.g., 169% - 109% = 60%) |

#### Annualized Returns Table
Location: Search for `id="asymmetric-cumulative-returns"`

- Update subtitle date: `as of 31 October, 2025` → `as of 30 November, 2025`
- Update all 5 rows (YTD, 1Y, 3Y, 5Y, Since Inception)
- Update Return, ACWI, and Excess columns
- Apply CSS classes: `positive` for gains, `negative` for losses

#### Annual Returns Table
Location: Search for `id="asymmetric-annual-returns"`

- Update subtitle date
- **Only update the YTD 2025 row** (other years are static)
- Update Return, ACWI, and Excess values

#### Chart Subtitles (2 charts)
Location: Search for `id="asymmetric-growth-chart"` and `id="asymmetric-returns-chart"`

- Update both: `as of 31 October, 2025` → `as of 30 November, 2025`

---

### 3.2 Dividend Strategy Tab

#### Metric Cards (4 cards at top)
Location: Search for `id="dividend-metrics"`

| Card | What to Update |
|------|----------------|
| Total Net Return | Update `+66%` to new total (e.g., `+71%`) |
| Annualized Net Return | Update `12.88%` to new Since Inception value |
| Current Dividend Yield | Update if changed (currently `7.8%`) |
| Outperformance | **Absolute difference:** Strategy Total - Benchmark Total (e.g., 71% - 38% = 33%) |

#### Annualized Returns Table
Location: Search for `id="dividend-cumulative-returns"`

- Update subtitle date
- Update all 4 rows (YTD, 1Y, 3Y, Since Inception)
- Note: Dividend strategy has no 5Y row (inception 2021)

#### Annual Returns Table
Location: Search for `id="dividend-annual-returns"`

- Update subtitle date
- **Only update the YTD 2025 row**

#### Chart Subtitles (2 charts)
Location: Search for `id="dividend-growth-chart"` and `id="dividend-returns-chart"`

- Update both subtitle dates

---

### 3.3 Combined Tab

Location: Search for `id="combined-content"`

- Update "Annualized Return Since Inception" row:
  - Asymmetric: Update to new Since Inception value
  - Dividend: Update to new Since Inception value

---

## Step 4: Update index.html

### Performance Snapshot (Hero Section)
Location: Search for `performance-snapshot`

Update these values:
- Asymmetric Strategy: `+166%` → new total
- Dividend Strategy: `+66%` → new total

### Strategy Cards
Location: Search for `strategy-metric`

Asymmetric card:
- Total Return: `+166%` → new total
- 5yr Annualized: `24.34%` → new 5 Year value

---

## Step 5: Verification Checklist

After updates, verify:

- [ ] All "as of" dates updated to new month
- [ ] Asymmetric metric cards (4) updated
- [ ] Dividend metric cards (4) updated
- [ ] Asymmetric annualized table (5 rows) updated
- [ ] Dividend annualized table (4 rows) updated
- [ ] Asymmetric annual table YTD row updated
- [ ] Dividend annual table YTD row updated
- [ ] All 4 chart subtitles updated (2 per strategy)
- [ ] Combined tab comparison values updated
- [ ] Homepage snapshot updated (2 values)
- [ ] Homepage strategy card updated (2 values)
- [ ] CSS classes correct (positive/negative)
- [ ] Test in browser - all 3 tabs work

---

## Reference: CSS Classes

```html
<!-- Positive returns (green) -->
<td class="positive">12.71%</td>

<!-- Negative returns (grey, or red for benchmark) -->
<td class="negative">-8.56%</td>
```

---

## Example Update (October → November 2025)

**Data provided:**
```
Asymmetric:
Account              YTD      1 Year   3 Year   5 Year   Since Inception
ACWI                 21.32    18.10    19.57    11.79    12.84
Asymmetric           16.34    13.49    12.38    21.55    18.36

Total: 169%

Dividend:
Account              YTD      1 Year   3 Year   Since Inception
DVY                  12.24    3.77     9.12     7.37
Dividend             27.45    26.94    16.88    12.98

Total: 71%
Dividend Yield: 7.8% (unchanged)
```

**Calculated Excess Returns:**

Asymmetric:
| Period | Return | ACWI | Excess |
|--------|--------|------|--------|
| YTD | 16.34% | 21.32% | -4.98% |
| 1 Year | 13.49% | 18.10% | -4.61% |
| 3 Year | 12.38% | 19.57% | -7.19% |
| 5 Year | 21.55% | 11.79% | +9.76% |
| Since Inception | 18.36% | 12.84% | +5.52% |

Dividend:
| Period | Return | DVY | Excess |
|--------|--------|-----|--------|
| YTD | 27.45% | 12.24% | +15.21% |
| 1 Year | 26.94% | 3.77% | +23.17% |
| 3 Year | 16.88% | 9.12% | +7.76% |
| Since Inception | 12.98% | 7.37% | +5.61% |

**Outperformance calculations (absolute difference):**
- Asymmetric: 169% - 109% (ACWI) = **60%** outperformance
- Dividend: 71% - 38% (DVY) = **33%** outperformance

---

## Notes

- **Charts (Infogram iframes):** The actual chart data is NOT updated through this process. Charts are hosted on Infogram and updated separately.
- **Annual rows (2020-2024):** These are historical and don't change month-to-month.
- **Bear Market Protection card:** This is a historical 2022 stat and remains static.
