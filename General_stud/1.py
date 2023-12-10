# Waveguide calc
import math as m


class Waveguide():
    def __init__(self, w, h, epsi, freq):
        self.w = w * 1e-3  # width in m
        self.h = h * 1e-3  # height in m
        self.epsi = epsi  # relative permittivity
        self.freq = freq * 1e9  # Frequency in GHz
        self.c = 299792458  # c in m/s
        self.mu = 1

    def getCutoff(self):
        Fc = self.c / (m.sqrt(self.epsi * self.mu) * 2 * self.w)

        return Fc * 1e-9

    def getWavelength(self):
        # lg = (2 * self.w)/(m.sqrt(4 * self.freq**2 * self.epsi * self.w**2 -1))
        lf = self.c / (self.freq * m.sqrt(self.epsi))
        lcof = 2 * self.w
        lg = lf / m.sqrt(1 - (lf / lcof) ** 2)
        return lg


WR10 = Waveguide(2.54, 1.27, 1, 90e9)

WR275 = Waveguide(0.864, 0.432, 1, 325e9)
WSi275 = Waveguide(0.2, 0.15, 11.9, 275e9)
WSi = Waveguide(0.65, 0.3, 11.9, 90e9)
# print(WR10.getCutoff())
# print(WSi.getCutoff())
# print(WR10.getWavelength())
print(WSi.getWavelength())
# print(WSi275.getWavelength())
# print(WSi275.getCutoff())
print(WSi275.getCutoff())
print(WSi.getCutoff())
