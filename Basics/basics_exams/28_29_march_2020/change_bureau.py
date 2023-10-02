bitcoins = int(input())
chinese_yuan = float(input())
commission = float(input())

bitcoin_to_bgn = bitcoins * 1168
chinese_yuan_to_usd = chinese_yuan * 0.15
chinese_yuan_to_bgn = chinese_yuan_to_usd * 1.76
total_bgn = chinese_yuan_to_bgn + bitcoin_to_bgn
bgn_to_eur = total_bgn / 1.95
total_after_commission = bgn_to_eur - (bgn_to_eur * (commission / 100))

print(f"{total_after_commission:.2f}")