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


The I2C bus on the VL53L5CX has a maximum speed of 1 Mbits/s and uses a device 8-bit address of 0x52.

# Example output

```
VL53L5CX ULD ready ! (Version : VL53L5CX_2.0.0)
Print data no :   0
Zone :   0, Status :   6, Distance :  991 mm
Zone :   1, Status :   6, Distance : 1162 mm
Zone :   2, Status :   6, Distance : 1472 mm
Zone :   3, Status :   6, Distance : 1599 mm
Zone :   4, Status :   6, Distance :  912 mm
Zone :   5, Status :   6, Distance : 1045 mm
Zone :   6, Status :   6, Distance : 1197 mm
Zone :   7, Status :   6, Distance : 1562 mm
Zone :   8, Status :   6, Distance :  844 mm
Zone :   9, Status :   6, Distance :  967 mm
Zone :  10, Status :   6, Distance : 1091 mm
Zone :  11, Status :   6, Distance : 1342 mm
Zone :  12, Status :   6, Distance :  777 mm
Zone :  13, Status :   6, Distance :  883 mm
Zone :  14, Status :   6, Distance : 1007 mm
Zone :  15, Status :   6, Distance : 1188 mm

Print data no :   1
Zone :   0, Status :   5, Distance :  996 mm
Zone :   1, Status :   9, Distance : 1142 mm
Zone :   2, Status :   9, Distance : 1254 mm
Zone :   3, Status :   5, Distance : 1602 mm
Zone :   4, Status :   5, Distance :  913 mm
Zone :   5, Status :   5, Distance : 1039 mm
Zone :   6, Status :   5, Distance : 1214 mm
Zone :   7, Status :   5, Distance : 1558 mm
Zone :   8, Status :   5, Distance :  834 mm
Zone :   9, Status :   5, Distance :  967 mm
Zone :  10, Status :   9, Distance : 1086 mm
Zone :  11, Status :   5, Distance : 1298 mm
Zone :  12, Status :   5, Distance :  775 mm
Zone :  13, Status :   5, Distance :  879 mm
Zone :  14, Status :   9, Distance :  997 mm
Zone :  15, Status :   9, Distance : 1180 mm
```

UM2884: "To have consistent data, the user needs to filter invalid target status. To give a confidence rating, a target with
status 5 is considered as 100% valid. A status of 6 or 9 can be considered with a confidence value of 50%. All
other statuses are below the 50% confidence level."


# References

1. UM2884 User manual "A guide to using the VL53L5CX multizone Time-of-Flight ranging sensor with a wide field of view ultra lite driver (ULD)"

1. VL53L5CX Datasheet "Time-of-Flight 8x8 multizone ranging sensor with wide field of view"

1. PCB4109A; VL53L5CX-Satel Schematics

1. VL53L5CX-SATEL Data brief "VL53L5CX breakout board Time-of-Flight 8x8 multizone ranging sensor with wide field of view"


# FAQ

Q: VL53L7CX/VL53L5CX API similarity and part identification <br>
A: https://community.st.com/t5/imaging-sensors/vl53l7cx-vl53l5cx-api-similarity-and-part-identification/td-p/576057