# PCA9533 
#
# Copyright (C) 2018  Kevin O'Connor <kevin@koconnor.net>
#
# This file may be distributed under the terms of the GNU GPLv3 license.
import bus

class pca9533:
    def __init__(self, config):
        self.i2c = bus.MCU_I2C_from_config(config)
        self.set_white()
    def set_white(self):
        self.i2c.i2c_write([0b00000101, 0b01010101])

def load_config_prefix(config):
    return pca9533(config)
