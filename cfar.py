"""
cfar.py
Simple CA-CFAR on range profile or RD magnitude.
"""
import numpy as np

def ca_cfar_1d(x: np.ndarray, guard: int=2, train: int=12, pfa: float=1e-3):
    """
    CA-CFAR 1D for magnitude array x.
    Returns threshold and detections boolean.
    """
    n = x.size
    thr = np.zeros(n)
    det = np.zeros(n, dtype=bool)

    # scaling factor for CA-CFAR (approx)
    alpha = train * (pfa**(-1/train) - 1)

    for i in range(n):
        start1 = max(i - guard - train, 0)
        end1 = max(i - guard, 0)
        start2 = min(i + guard + 1, n)
        end2 = min(i + guard + train + 1, n)

        training_cells = np.concatenate([x[start1:end1], x[start2:end2]])
        if training_cells.size < 1:
            thr[i] = 0
            continue
        noise_level = np.mean(training_cells)
        thr[i] = alpha * noise_level
        det[i] = x[i] > thr[i]
    return thr, det
