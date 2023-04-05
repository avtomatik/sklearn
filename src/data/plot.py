#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:12:38 2023

@author: alexandermikhailov
"""


import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import rfft
from pandas import DataFrame
from sklearn.metrics import r2_score


def plot_turnover(df: DataFrame) -> None:
    """Static Fixed Assets Turnover Approximation
        ================== =================================
        df.index           Period
        df.iloc[:, 0]      Fixed Assets Turnover
        ================== =================================
    """
    # =========================================================================
    # Linear: Fixed Assets Turnover
    # =========================================================================
    _lin = np.polyfit(
        df.index.to_series().astype(float),
        df.iloc[:, -1].astype(float),
        deg=1
    )
    # =========================================================================
    # Exponential: Fixed Assets Turnover
    # =========================================================================
    _exp = np.polyfit(
        df.index.to_series().astype(float),
        np.log(df.iloc[:, -1].astype(float)),
        deg=1
    )
    df['c_turnover_lin'] = df.index.to_series().mul(_lin[0]).add(_lin[1])
    df['c_turnover_exp'] = np.exp(
        df.index.to_series().astype(float).mul(_exp[0]).add(_exp[1]))
    # =========================================================================
    # Deltas
    # =========================================================================
    df['d_lin'] = df.iloc[:, -2].div(df.iloc[:, -3]).sub(1).abs()
    df['d_exp'] = df.iloc[:, -2].div(df.iloc[:, -4]).sub(1).abs()
    plt.figure(1)
    plt.plot(df.iloc[:, 2], df.iloc[:, 0])
    plt.title(
        'Fixed Assets Volume to Fixed Assets Turnover, {}$-${}'.format(
            *df.index[[0, -1]]
        )
    )
    plt.xlabel('Fixed Assets Turnover')
    plt.ylabel('Fixed Assets Volume')
    plt.grid()
    plt.figure(2)
    plt.scatter(
        df.index,
        df.iloc[:, -5],
        label='Fixed Assets Turnover'
    )
    plt.plot(
        df.iloc[:, [-4]],
        label='$\\hat K_{{l}} = {:.2f} {:.2f} t, R^2 = {:.4f}$'.format(
            *_lin[::-1],
            r2_score(df.iloc[:, -5], df.iloc[:, -4])
        )
    )
    plt.plot(
        df.iloc[:, [-3]],
        label='$\\hat K_{{e}} = \\exp ({:.2f} {:.2f} t), R^2 = {:.4f}$'.format(
            *_exp[::-1],
            r2_score(df.iloc[:, -5], df.iloc[:, -3])
        )
    )
    plt.title(
        'Fixed Assets Turnover Approximation, {}$-${}'.format(
            *df.index[[0, -1]]
        )
    )
    plt.xlabel('Period')
    plt.ylabel('Index')
    plt.grid()
    plt.legend()
    plt.figure(3)
    plt.plot(
        df.iloc[:, [-2]],
        ':',
        label='$\\|\\frac{{\\hat K_{{l}}-K}}{{K}}\\|, \\bar S = {:.4%}$'.format(
            df.iloc[:, -2].mean()
        )
    )
    plt.plot(
        df.iloc[:, [-1]],
        ':',
        label='$\\|\\frac{{\\hat K_{{e}}-K}}{{K}}\\|, \\bar S = {:.4%}$'.format(
            df.iloc[:, -1].mean()
        )
    )
    plt.title(
        'Deltas of Fixed Assets Turnover Approximation, {}$-${}'.format(
            *df.index[[0, -1]]
        )
    )
    plt.xlabel('Period')
    plt.ylabel('Index')
    plt.grid()
    plt.legend()
    plt.show()


def plot_discrete_fourier_transform(array: np.ndarray) -> None:
    """
    Discrete Fourier Transform

    Parameters
    ----------
    array : np.ndarray
        DESCRIPTION.

    Returns
    -------
    None
        DESCRIPTION.

    """
    # =========================================================================
    # TODO: Refine It
    # =========================================================================
    plt.plot(
        array,
        label='Labor Productivity',
    )
    plt.plot(
        rfft(array),
        'r:',
        label='Fourier Transform',
    )
    plt.grid()
    plt.legend()
    plt.show()
