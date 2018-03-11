def inverse(cdf, target_winrate):
    idx = (np.abs(cdf.cdf_value - target_winrate)).argmin()
    return cdf[idx, 'value']