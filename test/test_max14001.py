import pytest

hardware = "max14001"
classname = "adi,max14001"


######################################
@pytest.mark.iio_hardware(hardware)
@pytest.mark.parametrize("classname", [(classname)])
def test_max140001_rx_data (test_dma_rx, iio_uri, classname, channel):
    test_dma_rx(iio_uri, classname, channel)


# red supply
# black ground
# mosi blue
# miso violet
# cs2 white
# cout2 grey
# sclk green
# fault yellow