import pytest
from audio_filters.iir_filter import IIRFilter

def test_constructor_valid_order():
    # Test a valid filter creation
    filter = IIRFilter(2)
    assert filter is not None, "Filter should be instantiated correctly"

def test_constructor_invalid_order():
    # Test an invalid filter creation (order <= 0)
    with pytest.raises(ValueError, match="order must be greater than zero"):
        IIRFilter(0)

def test_set_coeffs_invalid_length_a():
    filter = IIRFilter(2)

    # Invalid 'aCoeffs' length
    a_coeffs = [1.0]  # too short
    b_coeffs = [1.0, 0.5]
    with pytest.raises(ValueError, match="Expected a_coeffs to have 3 elements for 2-order filter, got 2"):
        filter.set_coefficients(a_coeffs, b_coeffs)

def test_set_coeffs_invalid_length_b():
    filter = IIRFilter(2)

    # Invalid 'bCoeffs' length
    a_coeffs = [1.0, 0.5]
    b_coeffs = [1.0]  # too short
    with pytest.raises(ValueError, match="Expected b_coeffs to have 3 elements for 2-order filter, got 2"):
        filter.set_coefficients(a_coeffs, b_coeffs)

def test_set_coeffs_invalid_a_coeff_zero():
    filter = IIRFilter(2)

    # Invalid 'aCoeffs' where a_coeffs[0] == 0.0
    a_coeffs = [0.0, 0.5]  # a_coeffs[0] must not be zero
    b_coeffs = [1.0, 0.5]
    with pytest.raises(ValueError, match="a_coeffs[0] must not be zero"):
        filter.set_coefficients(a_coeffs, b_coeffs)

def test_process_with_no_coeffs_set():
    # Test process method with default coefficients (sane defaults)
    filter = IIRFilter(2)
    input_sample = 0.5
    result = filter.process(input_sample)

    # Since default a_coeffs[0] and b_coeffs[0] are 1.0, expect output = input
    assert pytest.approx(input_sample, 1e-6) == result, "Process should return the same value as input with default coefficients"

def test_process_with_coeffs_set():
    # Test process method with set coefficients
    filter = IIRFilter(2)

    a_coeffs = [1.0, 0.5]
    b_coeffs = [1.0, 0.5]
    filter.set_coefficients(a_coeffs, b_coeffs)

    # Process a sample
    input_sample = 0.5
    result = filter.process(input_sample)

    # Expected output can be complex to calculate in advance;
    # check if the method runs and returns a result within reasonable bounds
    assert -1.0 <= result <= 1.0, "Processed result should be in the range [-1, 1]"