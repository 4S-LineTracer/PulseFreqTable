#
# パルス周波数テーブル作る
#
import math

def main():
    # 初期条件
    f0 = 10
    fn = 500
    Nmax = 400
    Tclk = 100E-6 # 0.1ms ITU0の出力

    # 加速度を計算
    a = (f0 *f0 + fn * fn) / (2 * Nmax)
    print("accel: {0:.3f}".format(a))

    # パルス周波数を計算
    pulseFreqs = [calcPulseFreq(f0, a, n) for n in range(Nmax)]

    # GRA1の値に変換
    graValues = [(1 / freq) / Tclk - 1 for freq in pulseFreqs]

    # ファイルに出力
    with open("GRA1Table.csv", "w") as f:
        f.write(",\n".join(["{0:.0f}".format(f) for f in graValues]))
    
    with open("freqTable.csv", "w") as f:
        f.write(",\n".join(["{0:.3f}".format(f) for f in pulseFreqs]))

# パルス周波数を計算する
def calcPulseFreq(f0, a, n):
    fn = math.sqrt(f0 * f0 + 2 * a * n)
    return fn

if __name__ == "__main__":
    main()
    try:
        print("Type Ctrl+C to exit.")
        while True:
            pass
    except KeyboardInterrupt:
        pass
