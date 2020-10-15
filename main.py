#
# パルス周波数テーブル作る
#
import math

def main():
    # 初期条件やら最大パルスやら
    f0 = 0
    a = 2
    Nmax = 400

    # リスト内包表記でワンライン生成
    freqs = [calcPulseFreq(f0, a, n) for n in range(Nmax)]

    # ファイルに吐き出す
    with open("ferqTable.csv", "w") as f:
        f.write(",\n".join(["{0:.3f}".format(f) for f in freqs]))

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
