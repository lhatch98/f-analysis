import matplotlib.pyplot as plt
import argparse

class StockAnalysis:

    def __init__(self, fname, n, pdif_threshold):
        self.n = n
        self.fname = fname
        self.pdif_threshold = pdif_threshold

    def parseCSV(self):
        with open(self.fname, "r") as stock_data:
            n_yrs_data = [line.split(",") for line in stock_data]  # matrix of days
            del n_yrs_data[0]  # removes top title line from .csv
            opens = [float(day[1]) for day in n_yrs_data]
            closes = [float(day[4]) for day in n_yrs_data]
        return n_yrs_data, opens, closes

    def computation(self, n_yrs_data, opens, closes):
        tot_buys = 0
        day_count = 0
        ct = 0
        data_ar = []  # contains data on a (day_count, prices, ct + n, pdifs)
        prices = []
        pdifs = []
        avglist = []
        collect = False

        for i in closes[self.n:]:  # start checking on nth day
            ct += 1
            # calculating rolling avg from day i to day i - n
            avg = sum(closes[ct:self.n + ct]) / self.n
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
                if pdif <= -1*self.pdif_threshold and collect or i < avg and collect:
                    data_ar.append((day_count, prices, ct + self.n, pdifs))
                    day_count = 0  # reset
                    prices = []  # reset
                    pdifs = []  # reset
                    tot_buys += 1
                    collect = False

            else:
                pass

        return data_ar, avglist, tot_buys

    def plotting(self, data_ar, opens, closes, avglist, tot_buys):
        

        taxis = [i for i in range(1, len(closes) + 1)] # time-axis
        # it's worth noting that the NYSE averages 253 trading days a year NOT 365

        buys_for_plots = [i[1][0] for i in data_ar]
        sells_for_plots = [i[1][-1] for i in data_ar]
        sell_times = [i[2] for i in data_ar]
        buy_times = [i[2] - i[0] for i in data_ar]

        plt.plot(taxis, closes, 'k-', linewidth=0.5)
        ttaxis = taxis[self.n:]
        plt.plot(ttaxis, avglist, linewidth=0.5)

        plt.plot(buy_times, buys_for_plots, 'g*', markersize=3)
        plt.plot(sell_times, sells_for_plots, 'r.', markersize=3)

        plt.title(self.fname)
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

        return

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="stock analysis")

    parser.add_argument(
        "-d",
        "--days",
        help="integer number of days to base your rolling average off",
        default=40,
        type=int,
        dest='n'
    )

    parser.add_argument(
        "-p",
        "--pdif-threshold",
        help="percent dif (decimal/float) to base selling threshold off of",
        default=0.10,
        type=float,
        dest='pdif_thresh'
    )
    required = parser.add_argument_group('required arguments')
    
    required.add_argument(
        "-f",
        "--file-path",
        help="path to csv stock data file",
        required=True,
        type=str,
        dest='file_path'
    )

    cli_args = parser.parse_args()

    # 5yr_data/SBUX.csv
    inst = StockAnalysis(cli_args.file_path, cli_args.n, cli_args.pdif_thresh)
    file_data, open_data, close_data = inst.parseCSV()
    data_arr, avg_arr, tot_buyins = inst.computation(file_data, open_data, close_data)
    inst.plotting(data_arr, open_data, close_data, avg_arr, tot_buyins)

# TODO:
#   - add plot legend and update plot labels
#   - quantify profitablilty and print
#   - add docstrings
#   - need better file/function/class names
