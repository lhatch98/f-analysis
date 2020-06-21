import matplotlib.pyplot as plt


def analysis(fname, n, float_perc):
    """
    5 year stock analysis
    ex day data = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume\n']
    """
    with open(fname, "r") as stock_data:
        five_yrs = [line.split(",") for line in stock_data]  # matrix of days
        del five_yrs[0]  # remove csv label row

        closes = [float(day[4]) for day in five_yrs]
        opens = [float(day[1]) for day in five_yrs]

        tot_buys = 0
        day_count = 0
        ct = 0
        data_ar = []
        prices = []
        pdifs = []
        avglist = []

        collect = False

        for i in closes[n:]:  # start checking on n
            ct += 1
            avg = sum(closes[ct:n + ct]) / n
            avglist.append(avg)

            # pdif =

            if i > avglist[ct - 1]:
                collect = True
                prices.append(i)
                day_count += 1
                high = max(prices)
                pdif = (i - high) / high
                pdifs.append(pdif)

            elif collect:
                prices.append(i)
                high = max(prices)
                pdif = (i - high) / high
                pdifs.append(pdif)
                day_count += 1
                if pdif <= -1*float_perc and collect or i < avg and collect:
                    data_ar.append((day_count, prices, ct + n, pdifs))
                    day_count = 0  # reset
                    prices = []  # reset
                    pdifs = []  # reset
                    tot_buys += 1
                    collect = False

            else:
                pass

        print(data_ar)
        print("number of buys: " + str(tot_buys))

        # plotting
        taxis = [i for i in range(1, len(closes) + 1)]

        buys_for_plots = [i[1][0] for i in data_ar]
        sells_for_plots = [i[1][-1] for i in data_ar]
        sell_times = [i[2] for i in data_ar]
        buy_times = [i[2] - i[0] for i in data_ar]

        plt.plot(taxis, closes, 'k-')
        ttaxis = taxis[n:]
        plt.plot(ttaxis, avglist)

        plt.plot(buy_times, buys_for_plots, 'g*')
        plt.plot(sell_times, sells_for_plots, 'r.')

        plt.title(fname)
        plt.xlabel("day/ 5 yr")
        plt.ylabel("stock price ($)")
        plt.show()

        return None


analysis("5yr_data/SBUX.csv", 40, 0.10)
