import pandas as pd
import numpy as np


def bias_errors(sim, obs):
    if len(sim) != len(obs):
        raise ValueError('length of simulated and observed arrays must match')
    else:
        bias = np.subtract(sim, obs)
        error_df = pd.DataFrame(bias)
        stats = {'min': error_df.min(), 'q0.25': error_df.quantile(0.25), 'mean': error_df.mean(),
                 'median': error_df.median(), 'q0.75': error_df.quantile(0.75), 'max': error_df.max(),
                 'std': error_df.std()}
        return stats


def parse_to_quantiles(sim, obs):
    if len(sim) != len(obs):
        raise ValueError('length of simulated and observed arrays must match')
    else:
        quants = {}
        df = pd.DataFrame({'sim': sim, 'obs': obs})
        quants['Q1'] = df[df['obs'] <= df['obs'].quantile(0.25)]
        quants['Q2'] = df[(df['obs'].quantile(0.25) < df['obs']) & (df['obs'] <= df['obs'].quantile(0.5))]
        quants['Q3'] = df[(df['obs'].quantile(0.5) < df['obs']) & (df['obs'] <= df['obs'].quantile(0.75))]
        quants['Q4'] = df[(df['obs'].quantile(0.75) < df['obs']) & (df['obs'] <= df['obs'].max())]
        return quants


def cal_bias_stats(sim, obs):
    if len(sim) != len(obs):
        raise ValueError('length of simulated and observed arrays must match')
    else:
        quants = parse_to_quantiles(sim, obs)
        all_stats = {key: bias_errors(quants[key]['sim'].values, quants[key]['obs'].values) for key in quants}
        return all_stats


test = cal_bias_stats([x for x in range(1, 11)], [x for x in range(5, 15)])
print(test)

