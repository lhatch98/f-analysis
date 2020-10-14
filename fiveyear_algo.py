import matplotlib.pyplot as plt


def analysis(fname, n, float_perc):
    """
    stock trend analysis
    example day data provided by yahoo csv is formatted as follows:
    ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume\n']
    """
    with open(fname, "r") as stock_data:
        five_yrs = [line.split(",") for line in stock_data]  # matrix of days
        del five_yrs[0]  # removes top title line from .csv

        closes = [float(day[4]) for day in five_yrs]
        opens = [float(day[1]) for day in five_yrs]

        tot_buys = 0
        day_count = 0
        ct = 0
        data_ar = []  # contains data on a (day_count, prices, ct + n, pdifs)
        prices = []
        pdifs = []
        avglist = []

        collect = False

        for i in closes[n:]:  # start checking on nth day
            ct += 1
            # calculating rolling avg from day i to day i - n
            avg = sum(closes[ct:n + ct]) / n
            avglist.append(avg)


            # if close price i exceeds current n day avg => buy
            if i > avglist[ct - 1]:
                collect = True
                prices.append(i)
                day_count += 1
                high = max(prices)
                pdif = (i - high) / high
                pdifs.append(pdif)

            # if currently holding
            elif collect:
                prices.append(i)
                high = max(prices)
                pdif = (i - high) / high
                pdifs.append(pdif)
                day_count += 1

                # while holding...
                # if the buy and sell %diff exceeds target %diff OR close price is below rolling n day avg => sell
                if pdif <= -1*float_perc and collect or i < avg and collect:
                    data_ar.append((day_count, prices, ct + n, pdifs))
                    day_count = 0  # reset
                    prices = []  # reset
                    pdifs = []  # reset
                    tot_buys += 1
                    collect = False

            else:
                pass

        # ===== plotting =====

        taxis = [i for i in range(1, len(closes) + 1)] # time-axis
        # it's worth noting that the NYSE averages 253 trading days a year NOT 365

        buys_for_plots = [i[1][0] for i in data_ar]
        sells_for_plots = [i[1][-1] for i in data_ar]
        sell_times = [i[2] for i in data_ar]
        buy_times = [i[2] - i[0] for i in data_ar]

        plt.plot(taxis, closes, 'k-', linewidth=0.5)
        ttaxis = taxis[n:]
        plt.plot(ttaxis, avglist, linewidth=0.5)

        plt.plot(buy_times, buys_for_plots, 'g*', markersize=3)
        plt.plot(sell_times, sells_for_plots, 'r.', markersize=3)

        plt.title(fname)
        plt.xlabel("day/ 5 yr")
        plt.ylabel("stock price ($)")
        plt.linewidth = 3
        plt.show()

        print(f"Total buy ins over {len(taxis)} days: {tot_buys}")
        days = [i[0] for i in data_ar]
        avg_days_held = sum(days) / len(data_ar)
        print(f"Total days held was {sum(days)} out of {len(taxis)} for {(sum(days) / len(taxis)) * 100}%")
        print(f"Avg duration hold was {avg_days_held} days")
        print("theoretical gain/loss was...")
        return None


analysis("5yr_data/SBUX.csv", 40, 0.10)

# TODO:
#     - add plot legend and update plot labels
#     - quantify profitablilty and print
#     - generalize code
#     - create classed version
#     - provide accurate and detailed readme