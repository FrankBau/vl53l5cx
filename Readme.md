# Nucleo-L432KC

    +---- USB ----+
    PA9         VIN
    PA10        GND
    NRST        NRST
    GND         +5V
    PA12        PA2
    PB0         PA7
    PB7         PA6
    PB6         PA5
    PB1  +----+ PA4
    N.C. |    | PA3
    N.C. +----+ PA1
    PA8         PA0
    PA11        AREF
    PB5         +3V3
    PB4         PB3
    +---- RST ----+

# PCB4109A; VL53L5CX-Satel

header pins 1..9:

| pin | signal | connect to | comment   |
|-----|--------|------------|-----------|
| 1 | GND           | GND   |
| 2 | EVK_IOVDD     | +3.3V |
| 3 | EVK_AVDD      | +3.3V |
| 4 | EVK_PWR_EN    | PA8   |  power enable; high active, internal pull-down |
| 5 | EVK_LPn       | PA12  |  disable I2C comm when low; pull-up R on satel |
| 6 | EVK_SCL       | PA9   |  I2C1_SCL |
| 7 | EVK_SDA       | PA10  |  I2C1_SDA |
| 8 | EVK_I2C_RST   | PB0   |  high pulse --> I2C reset; pull-down R on satel |
| 9 | EVK_INT       | PB1   |  open-drain output, pull-up R on satel |


The I2C bus on the VL53L5CX has a maximum speed of 1 Mbits/s and uses a default device 8-bit address of 0x52.

# minimal wiring

satel       nucleo
GND         GND
EVK_IOVDD   +3V3
EVK_AVDD    +5V
EVK_PWR_EN  +5V
EVK_SCL     PA9
EVK_SDA     PA10

# Example output

4x4 multizone distances in mm

```
  780  201  279 1276
  103  170  280 1223
   79  145  293  330
   92  112  282  264
```

UM2884: "To have consistent data, the user needs to filter invalid target status. To give a confidence rating, a target with status 5 is considered as 100% valid. A status of 6 or 9 can be considered with a confidence value of 50%. All other statuses are below the 50% confidence level."


# References

1. UM2884 User manual "A guide to using the VL53L5CX multizone Time-of-Flight ranging sensor with a wide field of view ultra lite driver (ULD)"

1. VL53L5CX Datasheet "Time-of-Flight 8x8 multizone ranging sensor with wide field of view"

1. PCB4109A; VL53L5CX-Satel Schematics

1. VL53L5CX-SATEL Data brief "VL53L5CX breakout board Time-of-Flight 8x8 multizone ranging sensor with wide field of view"

1. STSW-IMG023 Ultra Lite Driver (ULD) for VL53L5CX multi-zone sensor https://www.st.com/en/embedded-software/stsw-img023.html

# FAQ

Q: VL53L7CX/VL53L5CX API similarity and part identification <br>
A: https://community.st.com/t5/imaging-sensors/vl53l7cx-vl53l5cx-api-similarity-and-part-identification/td-p/576057