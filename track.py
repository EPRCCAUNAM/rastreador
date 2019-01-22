import solarDtr as solar

sun = solar.detector(filename='test/test02.cca')
sun.delay=0.3
while (True):
    sun.detect()
