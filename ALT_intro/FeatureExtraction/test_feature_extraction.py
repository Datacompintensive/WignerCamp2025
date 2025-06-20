import torch
import pytest
from feature_extraction import mean_all, mean_percentile

def test_mean_all_simple():
    x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    assert mean_all(x) == pytest.approx(2.5)

def test_mean_percentile_median():
    x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    assert mean_percentile(x, 0.5) == pytest.approx((2.0 + 5.0) / 2)

def test_mean_percentile_extreme():
    x = torch.tensor([[10.0, 20.0, 30.0], [40.0, 50.0, 60.0]])
    assert mean_percentile(x, 0.0) == pytest.approx((10.0 + 40.0) / 2)
    assert mean_percentile(x, 1.0) == pytest.approx((30.0 + 60.0) / 2)

def test_random_matrix():
    torch.manual_seed(42)
    x = torch.rand(100, 50)
    m_all = mean_all(x)
    m_perc = mean_percentile(x, 0.25)
    assert 0.0 <= m_perc <= 1.0
    assert abs(m_all - x.mean().item()) < 1e-6
