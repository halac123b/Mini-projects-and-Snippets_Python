import __future__

class IIRFilter:
    r"""
    N-Order IIR filter
    Assumes working with float samples normalized on [-1, 1]

    ---

    Implementation details:
    Based on the 2nd-order function from
     https://en.wikipedia.org/wiki/Digital_biquad_filter,
    this generalized N-order function was made.
   """

    def __init__(self, order: int) -> None:
        self.order = order

        # a_{0} ... a_{k}
        self.a_coeffs = [1.0] + [0.0] * order
        # b_{0} ... b_{k}
        self.b_coeffs = [1.0] + [0.0] * order

        # x[n-1] ... x[n-k]
        self.input_history = [0.0] * self.order
        # y[n-1] ... y[n-k]
        self.output_history = [0.0] * self.order

    def set_coefficients(self, a_coeffs: list[float], b_coeffs: list[float]) -> None:
        """
        Set the coefficients for the IIR filter. These should both be of size order + 1.
        a_0 may be left out, and it will use 1.0 as default value.

        This method works well with scipy's filter design functions
            >>> # Make a 2nd-order 1000Hz butterworth lowpass filter
            >>> import scipy.signal
            >>> b_coeffs, a_coeffs = scipy.signal.butter(2, 1000,
            ...                                          btype='lowpass',
            ...                                          fs=48000)
            >>> filt = IIRFilter(2)
            >>> filt.set_coefficients(a_coeffs, b_coeffs)
        """