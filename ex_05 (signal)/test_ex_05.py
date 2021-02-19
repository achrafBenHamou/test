import pytest
import numpy
import correction_ex_05 as ex_05


@pytest.fixture
def data_set():
    filename = "signal.npy"
    return ex_05.open_file(filename)


def test_open_file(data_set):
    pytest.data_set = data_set
    assert isinstance(data_set, numpy.ndarray)
    assert numpy.shape(pytest.data_set) == (261452,)


def test_compute_timestamp():
    pytest.ts = ex_05.signal_tools().compute_timestamp(pytest.data_set)
    assert len(pytest.ts) == 261452
    assert max(pytest.ts) == 131.29939678627932


def test_get_signal_freq():
    pytest.xf, pytest.yf = ex_05.signal_tools.compute_fourrier_transform(
        pytest.data_set, pytest.ts
    )
    pytest.fs = ex_05.signal_tools.get_signal_freq(pytest.xf, pytest.yf)
    assert pytest.fs == 320


def test_low_pass():
    signal_low_pass = ex_05.signal_tools.low_pass(pytest.data_set)
    assert abs(numpy.sum(numpy.diff(signal_low_pass))) < abs(numpy.sum(numpy.diff(pytest.data_set)))

def test_band_pass():
    signal_band_pass = ex_05.signal_tools.band_pass(pytest.data_set, pytest.fs - 1, pytest.fs + 1)
    assert numpy.abs(numpy.median(signal_band_pass)) < 0.001
    assert numpy.abs(numpy.mean(signal_band_pass)) < 0.001

def test_get_signal_envelope():
    pytest.env = ex_05.signal_tools.get_signal_envelope(pytest.data_set)
    assert numpy.median(pytest.env) > 20
    
def test_remove_side_effect():
    env2 = ex_05.signal_tools.remove_side_effect(pytest.data_set, pytest.fs - 1, pytest.fs + 1)
    
    side1 = pytest.env[:1000]
    side2 = pytest.env[-1000:]
    
    
    assert numpy.abs(numpy.mean(numpy.diff(side1))) > numpy.abs(numpy.mean(numpy.diff(env2[:1000]))) * 9
    assert numpy.abs(numpy.mean(numpy.diff(side2))) > numpy.abs(numpy.mean(numpy.diff(env2[-1000:]))) * 9
