# Python Stock Investment

A Python program that simulates stock market investments.

## Overview

- Initial capital: $1000
- Each round presents 3 investment opportunities
- Each opportunity has two parameters:
  - Return Rate: Percentage gain if successful
  - Success Probability: Chance of positive outcome

## Interface

```
wallet : 1000
1: 25% Rate, 75% Success
2: 8% Rate, 92% Success
3: 60% Rate, 45% Success

Select option: 2
Investment amount: 200
```

## Outcome Mechanics

- Positive outcome (+++): balance + (investment * return rate)
- Negative outcome (---): balance - (investment * return rate)

## Program Features

- Investment opportunities are randomly generated
- Higher return rates typically correlate with lower success probabilities
- Continuous operation until manual termination

---

**Execution:**
```bash
python stocks.py
```