# Compound ROI Calculator

Thank you @flipsidecrypto for the bounty opportunity.

Put together by @ryanl and @MonetCapital

## How much interest and COMP would you earn for a $100K supply over 30 days on each of the active markets?

### Getting the Data
We first queried the *compound market stats* table for the APYs and COMP speeds of the different markets. This resulted in the following graphs.

![Average supply APY](/outputs/apy.png)

https://velocity-app.flipsidecrypto.com/velocity/visuals/6d81ccc0-49f6-47a7-9544-d11f0f19f097/0f0ebfaa-31ed-486f-9866-19de92de1903
(Average supply APY)

![Average COMP speed (USD)](/outputs/average_comp.png)

https://velocity-app.flipsidecrypto.com/velocity/visuals/7bfbccfd-3c45-472a-9163-6600251147ff/0f0ebfaa-31ed-486f-9866-19de92de1903
(Average COMP speed in USD value)

Using these values, we calculated the average interest of the 30 day period per market, as well as the comp value accrual over 31 days. As stated in the 
flipside table documentation, *COMP SPEED* is the rate at which COMP is distributed per block.

### Priming the Data
To get the average COMP accrual rate/day, we first removed any irregularities in the data such as infinite or null values. We then multiplied the comp
speed by the number of blocks during the specified time period (1 day). At this time, using Dune Analytic's community written query, I am able to see the amount
of Compound users during the last 30 days is roughly ~ 300K. ([dune analytics link](https://duneanalytics.com/queries/1010/5530?fbclid=IwAR3TcBocoadY20EPwStW6LcG8PdecVd4Zo2TyyfUIPlm2tMfPM1QuyoKjtk))

See the 31 day average APYs and COMP value accrued/day in the following output:

![Average APY and COMP](/outputs/market_interests.png)

From this, we can calculate the accrued value over the 31 day period with a 100K supply deposit in the respective markets.

![Value](/outputs/accrued_value.png)

Using this data, we are able to calculate a theoretical ROI for a month, and for a year.

![ROI Month](/outputs/roi_month.png)

![ROI Year](/outputs/roi_year.png)

### Conclusion
Seen from the above graphs and outputs, the stablecoins such as DAI, USDT and USDC have the most upside to them. In comparison, WETH and WBTC have lower APYs and therefore will have lower ROIs.
Running calculator.py will also allow you to choose different combinations of collateral and time in market! *Just be careful, you will need to have Python, numpy and pandas modules installed!*
