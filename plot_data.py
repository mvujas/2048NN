import matplotlib.pyplot as plt
import numpy as np

# steps, max_tile, score
data = [[116, 128.0, 1060.0], [165, 128.0, 1616.0], [168, 256.0, 2024.0], [71, 32.0, 428.0], [81, 64.0, 596.0], [94, 64.0, 668.0], [133, 128.0, 1288.0], [92, 64.0, 712.0], [92, 64.0, 652.0], [81, 64.0, 564.0], [150, 128.0, 1440.0], [74, 64.0, 500.0], [124, 128.0, 1192.0], [128, 128.0, 1152.0], [250, 256.0, 3000.0], [144, 128.0, 1380.0], [136, 128.0, 1248.0], [154, 128.0, 1468.0], [91, 64.0, 664.0], [154, 128.0, 1468.0], [142, 128.0, 1356.0], [88, 64.0, 648.0], [120, 128.0, 1184.0], [68, 32.0, 396.0], [86, 64.0, 644.0], [76, 64.0, 536.0], [136, 128.0, 1308.0], [148, 128.0, 1400.0], [188, 256.0, 2192.0], [152, 128.0, 1432.0], [102, 64.0, 748.0], [63, 32.0, 360.0], [73, 64.0, 524.0], [149, 128.0, 1408.0], [100, 64.0, 768.0], [161, 256.0, 1952.0], [110, 64.0, 868.0], [94, 64.0, 688.0], [151, 128.0, 1392.0], [146, 128.0, 1360.0], [131, 64.0, 1092.0], [57, 32.0, 332.0], [86, 32.0, 560.0], [153, 128.0, 1492.0], [105, 128.0, 960.0], [115, 128.0, 1056.0], [141, 128.0, 1284.0], [60, 32.0, 320.0], [84, 64.0, 588.0], [197, 256.0, 2340.0], [114, 128.0, 1064.0], [84, 64.0, 588.0], [195, 128.0, 2044.0], [131, 128.0, 1248.0], [98, 64.0, 716.0], [131, 128.0, 1276.0], [138, 128.0, 1300.0], [68, 32.0, 440.0], [90, 64.0, 660.0], [115, 128.0, 1052.0], [80, 64.0, 592.0], [174, 128.0, 1800.0], [161, 128.0, 1516.0], [102, 64.0, 760.0], [117, 64.0, 984.0], [133, 128.0, 1236.0], [118, 128.0, 1084.0], [163, 128.0, 1596.0], [137, 128.0, 1316.0], [96, 64.0, 700.0], [159, 128.0, 1492.0], [87, 64.0, 648.0], [123, 128.0, 1084.0], [81, 64.0, 544.0], [107, 64.0, 808.0], [118, 128.0, 1060.0], [84, 64.0, 632.0], [88, 64.0, 612.0], [151, 128.0, 1420.0], [134, 128.0, 1300.0], [185, 256.0, 2184.0], [88, 64.0, 608.0], [96, 64.0, 704.0], [130, 128.0, 1180.0], [83, 64.0, 628.0], [93, 64.0, 688.0], [189, 256.0, 2252.0], [84, 64.0, 592.0], [104, 64.0, 768.0], [120, 64.0, 952.0], [135, 128.0, 1304.0], [187, 128.0, 2008.0], [114, 128.0, 1136.0], [174, 256.0, 2112.0], [140, 128.0, 1340.0], [231, 256.0, 2904.0], [152, 128.0, 1472.0], [74, 64.0, 504.0], [75, 64.0, 536.0], [149, 128.0, 1412.0], [149, 128.0, 1420.0], [115, 64.0, 928.0], [104, 64.0, 820.0], [122, 128.0, 1124.0], [85, 64.0, 612.0], [84, 64.0, 592.0], [123, 128.0, 1192.0], [171, 256.0, 2028.0], [81, 64.0, 572.0], [142, 128.0, 1352.0], [164, 128.0, 1600.0], [169, 128.0, 1644.0], [112, 128.0, 1016.0], [114, 128.0, 1072.0], [84, 64.0, 592.0], [123, 128.0, 1192.0], [120, 128.0, 1072.0], [91, 64.0, 680.0], [113, 64.0, 900.0], [257, 256.0, 3020.0], [80, 64.0, 576.0], [102, 64.0, 848.0], [107, 64.0, 844.0], [77, 64.0, 544.0], [115, 128.0, 1060.0], [126, 128.0, 1232.0], [131, 128.0, 1240.0], [91, 64.0, 652.0], [141, 128.0, 1448.0], [90, 64.0, 632.0], [154, 128.0, 1508.0], [83, 64.0, 600.0], [87, 64.0, 620.0], [89, 64.0, 656.0], [90, 64.0, 632.0], [105, 64.0, 808.0], [140, 128.0, 1296.0], [120, 64.0, 1000.0], [129, 128.0, 1220.0], [175, 128.0, 1712.0], [132, 128.0, 1200.0], [110, 64.0, 828.0], [113, 128.0, 1024.0], [113, 128.0, 1040.0], [89, 64.0, 676.0], [76, 64.0, 540.0], [135, 128.0, 1204.0], [118, 128.0, 1052.0], [86, 64.0, 616.0], [144, 128.0, 1408.0], [128, 64.0, 1040.0], [65, 32.0, 352.0], [185, 256.0, 2156.0], [89, 64.0, 628.0], [51, 32.0, 260.0], [81, 64.0, 560.0], [85, 64.0, 596.0], [94, 64.0, 692.0], [91, 64.0, 712.0], [107, 128.0, 1000.0], [150, 128.0, 1460.0], [90, 128.0, 840.0], [97, 64.0, 784.0], [144, 128.0, 1392.0], [113, 64.0, 916.0], [150, 128.0, 1436.0], [59, 32.0, 312.0], [151, 128.0, 1608.0], [114, 64.0, 920.0], [221, 256.0, 2600.0], [188, 256.0, 2180.0], [163, 128.0, 1596.0], [166, 128.0, 1656.0], [148, 128.0, 1428.0], [185, 128.0, 1812.0], [102, 64.0, 788.0], [165, 256.0, 1948.0], [120, 128.0, 1092.0], [124, 128.0, 1156.0], [174, 256.0, 2056.0], [90, 64.0, 724.0], [79, 64.0, 564.0], [124, 128.0, 1192.0], [214, 256.0, 2476.0], [111, 64.0, 892.0], [87, 64.0, 624.0], [107, 128.0, 1028.0], [152, 128.0, 1400.0], [136, 128.0, 1296.0], [131, 128.0, 1200.0], [96, 64.0, 716.0], [87, 64.0, 620.0], [75, 32.0, 440.0], [108, 64.0, 884.0], [108, 64.0, 864.0], [133, 128.0, 1248.0], [121, 128.0, 1128.0], [114, 64.0, 908.0], [82, 64.0, 580.0], [91, 64.0, 668.0], [145, 128.0, 1368.0], [205, 256.0, 2392.0], [85, 64.0, 592.0], [145, 128.0, 1372.0], [129, 128.0, 1252.0], [87, 64.0, 620.0], [97, 64.0, 728.0], [205, 256.0, 2424.0], [71, 32.0, 440.0], [56, 32.0, 284.0], [95, 64.0, 700.0], [89, 64.0, 624.0], [82, 64.0, 584.0], [155, 128.0, 1488.0], [142, 128.0, 1376.0], [102, 128.0, 932.0], [98, 64.0, 712.0], [130, 128.0, 1244.0], [139, 128.0, 1344.0], [184, 128.0, 1876.0], [45, 32.0, 216.0], [169, 128.0, 1640.0], [132, 128.0, 1276.0], [73, 64.0, 508.0], [133, 64.0, 1160.0], [168, 128.0, 1656.0], [133, 128.0, 1208.0], [97, 64.0, 708.0], [103, 128.0, 936.0], [96, 64.0, 708.0], [129, 128.0, 1260.0], [135, 128.0, 1284.0], [136, 128.0, 1316.0], [86, 64.0, 612.0], [86, 64.0, 616.0], [144, 128.0, 1384.0], [100, 64.0, 800.0], [57, 32.0, 332.0], [126, 128.0, 1160.0], [93, 64.0, 660.0], [129, 128.0, 1264.0], [71, 64.0, 456.0], [106, 128.0, 988.0], [155, 128.0, 1456.0], [72, 64.0, 476.0], [148, 128.0, 1488.0], [112, 64.0, 848.0], [94, 64.0, 724.0], [100, 64.0, 780.0], [151, 128.0, 1440.0], [177, 128.0, 1740.0], [128, 128.0, 1168.0], [151, 128.0, 1396.0], [75, 64.0, 548.0], [92, 64.0, 644.0], [142, 128.0, 1388.0], [139, 128.0, 1336.0], [148, 128.0, 1384.0], [130, 128.0, 1220.0], [83, 64.0, 572.0], [82, 64.0, 580.0], [214, 256.0, 2464.0], [142, 128.0, 1340.0], [138, 128.0, 1316.0], [163, 128.0, 1684.0], [131, 64.0, 1116.0], [77, 64.0, 544.0], [155, 128.0, 1476.0], [185, 256.0, 2220.0], [144, 128.0, 1360.0], [93, 64.0, 696.0], [167, 256.0, 1992.0], [134, 128.0, 1288.0], [123, 128.0, 1128.0], [129, 128.0, 1172.0], [153, 128.0, 1524.0], [84, 64.0, 552.0], [176, 128.0, 1812.0], [79, 64.0, 508.0], [79, 64.0, 568.0], [72, 64.0, 480.0], [118, 128.0, 1108.0], [118, 128.0, 1092.0], [197, 256.0, 2320.0], [135, 128.0, 1292.0], [80, 64.0, 568.0], [51, 32.0, 260.0], [117, 128.0, 1064.0], [117, 64.0, 960.0], [70, 64.0, 456.0], [116, 64.0, 884.0], [123, 128.0, 1132.0], [147, 128.0, 1472.0], [146, 128.0, 1372.0], [144, 128.0, 1356.0], [129, 128.0, 1284.0], [150, 128.0, 1496.0], [108, 64.0, 864.0], [142, 128.0, 1344.0], [114, 128.0, 1044.0], [127, 128.0, 1212.0], [136, 128.0, 1296.0], [98, 128.0, 928.0], [88, 64.0, 668.0], [61, 32.0, 348.0], [136, 128.0, 1264.0], [192, 256.0, 2328.0], [213, 256.0, 2472.0], [166, 256.0, 2008.0], [120, 128.0, 1076.0], [132, 128.0, 1312.0], [110, 64.0, 868.0], [111, 64.0, 888.0], [144, 128.0, 1392.0], [257, 256.0, 3076.0], [139, 128.0, 1328.0], [125, 128.0, 1136.0], [78, 64.0, 520.0], [91, 32.0, 616.0], [81, 64.0, 580.0], [216, 256.0, 2580.0], [90, 64.0, 648.0], [222, 256.0, 2616.0], [128, 64.0, 1136.0], [107, 64.0, 812.0], [174, 256.0, 2048.0], [65, 32.0, 384.0], [59, 32.0, 328.0], [78, 64.0, 548.0], [158, 128.0, 1572.0], [129, 128.0, 1264.0], [137, 128.0, 1280.0], [55, 32.0, 324.0], [81, 64.0, 576.0], [205, 256.0, 2412.0], [192, 256.0, 2256.0], [92, 64.0, 688.0], [210, 256.0, 2444.0], [152, 128.0, 1440.0], [79, 64.0, 568.0], [81, 64.0, 576.0], [91, 64.0, 648.0], [122, 128.0, 1148.0], [91, 64.0, 724.0], [96, 64.0, 704.0], [85, 64.0, 612.0], [98, 64.0, 772.0], [72, 64.0, 516.0], [150, 128.0, 1604.0], [119, 128.0, 1080.0], [74, 64.0, 500.0], [135, 128.0, 1308.0], [109, 128.0, 1004.0], [151, 128.0, 1456.0], [38, 16.0, 132.0], [144, 128.0, 1404.0], [124, 128.0, 1152.0], [89, 64.0, 628.0], [84, 64.0, 604.0], [47, 32.0, 224.0], [96, 64.0, 676.0], [80, 64.0, 572.0], [113, 128.0, 1024.0], [143, 128.0, 1356.0], [134, 128.0, 1288.0], [102, 128.0, 936.0], [129, 128.0, 1260.0], [90, 64.0, 680.0], [178, 128.0, 1888.0], [80, 64.0, 552.0], [140, 128.0, 1328.0], [106, 64.0, 876.0], [115, 64.0, 968.0], [80, 64.0, 584.0], [101, 128.0, 928.0], [65, 64.0, 428.0], [112, 64.0, 836.0], [109, 128.0, 1028.0], [149, 128.0, 1424.0], [98, 64.0, 772.0], [63, 64.0, 440.0], [110, 128.0, 1012.0], [157, 128.0, 1508.0], [73, 64.0, 508.0], [130, 64.0, 1072.0], [139, 128.0, 1280.0], [157, 128.0, 1576.0], [120, 128.0, 1076.0], [66, 64.0, 480.0], [102, 64.0, 824.0], [126, 64.0, 1036.0], [115, 64.0, 972.0], [64, 32.0, 392.0], [111, 128.0, 1016.0], [83, 64.0, 592.0], [104, 64.0, 760.0], [176, 128.0, 1720.0], [116, 64.0, 936.0], [111, 128.0, 1020.0], [177, 128.0, 1728.0], [150, 128.0, 1480.0], [202, 256.0, 2376.0], [96, 64.0, 708.0], [62, 32.0, 312.0], [155, 128.0, 1460.0], [134, 128.0, 1300.0], [95, 64.0, 696.0], [131, 128.0, 1200.0], [93, 64.0, 688.0], [78, 64.0, 568.0], [121, 128.0, 1084.0], [94, 64.0, 648.0], [103, 128.0, 964.0], [125, 128.0, 1188.0], [104, 64.0, 816.0], [154, 128.0, 1452.0], [144, 128.0, 1364.0], [73, 64.0, 496.0], [74, 64.0, 536.0], [83, 64.0, 584.0], [128, 128.0, 1248.0], [108, 64.0, 800.0], [125, 128.0, 1144.0], [174, 128.0, 1828.0], [176, 128.0, 1684.0], [124, 128.0, 1112.0], [113, 64.0, 820.0], [110, 128.0, 1016.0], [113, 128.0, 1048.0], [108, 128.0, 1004.0], [136, 128.0, 1292.0], [101, 64.0, 744.0], [127, 128.0, 1196.0], [132, 128.0, 1280.0], [66, 64.0, 444.0], [97, 64.0, 768.0], [60, 32.0, 320.0], [200, 256.0, 2356.0], [94, 64.0, 692.0], [116, 64.0, 916.0], [103, 64.0, 752.0], [145, 128.0, 1308.0], [114, 128.0, 1068.0], [82, 64.0, 596.0], [83, 64.0, 568.0], [140, 128.0, 1352.0], [148, 128.0, 1404.0], [93, 64.0, 676.0], [104, 64.0, 760.0], [138, 128.0, 1300.0], [150, 128.0, 1432.0], [130, 128.0, 1240.0], [76, 32.0, 480.0], [54, 32.0, 284.0], [139, 128.0, 1340.0], [188, 256.0, 2240.0], [87, 64.0, 608.0], [129, 128.0, 1164.0], [219, 256.0, 2584.0], [88, 64.0, 624.0], [91, 64.0, 640.0], [81, 64.0, 572.0], [112, 128.0, 1020.0], [135, 128.0, 1320.0], [196, 256.0, 2300.0], [79, 64.0, 556.0], [159, 128.0, 1580.0], [143, 128.0, 1404.0], [80, 64.0, 660.0], [130, 128.0, 1248.0], [134, 128.0, 1304.0], [135, 128.0, 1292.0], [133, 128.0, 1280.0], [91, 64.0, 640.0], [117, 64.0, 932.0], [99, 64.0, 724.0], [88, 64.0, 672.0], [130, 128.0, 1224.0], [133, 128.0, 1248.0], [114, 128.0, 1064.0], [147, 128.0, 1408.0], [89, 64.0, 620.0], [147, 128.0, 1388.0], [146, 128.0, 1372.0], [158, 128.0, 1528.0], [123, 128.0, 1208.0], [96, 64.0, 724.0], [133, 128.0, 1284.0], [101, 64.0, 844.0], [179, 256.0, 2092.0], [161, 128.0, 1584.0], [79, 64.0, 552.0], [129, 64.0, 1080.0], [86, 64.0, 604.0], [198, 256.0, 2328.0], [74, 64.0, 528.0], [128, 128.0, 1164.0], [117, 128.0, 1060.0], [116, 128.0, 1068.0], [113, 128.0, 1004.0], [118, 128.0, 1096.0], [57, 32.0, 320.0], [100, 64.0, 768.0], [73, 64.0, 520.0], [147, 128.0, 1380.0], [177, 256.0, 2100.0], [174, 256.0, 2084.0], [99, 64.0, 768.0], [86, 64.0, 612.0], [149, 128.0, 1428.0], [148, 128.0, 1364.0], [114, 128.0, 1032.0], [91, 128.0, 844.0], [120, 128.0, 1116.0], [104, 128.0, 944.0], [216, 256.0, 2572.0], [92, 64.0, 688.0], [84, 64.0, 608.0], [117, 128.0, 1060.0], [163, 128.0, 1600.0], [83, 64.0, 600.0], [151, 128.0, 1408.0], [92, 64.0, 684.0], [139, 128.0, 1340.0], [76, 64.0, 540.0], [105, 64.0, 852.0], [73, 32.0, 432.0], [105, 64.0, 868.0], [141, 128.0, 1292.0], [107, 128.0, 988.0], [112, 128.0, 1024.0], [135, 128.0, 1308.0], [109, 64.0, 888.0], [121, 128.0, 1124.0], [218, 256.0, 2556.0], [115, 128.0, 1076.0], [204, 256.0, 2368.0], [99, 64.0, 704.0], [75, 32.0, 444.0], [115, 128.0, 1048.0], [96, 64.0, 708.0], [230, 256.0, 2820.0], [190, 256.0, 2244.0], [91, 64.0, 636.0], [131, 128.0, 1188.0], [125, 128.0, 1156.0], [95, 64.0, 700.0], [86, 64.0, 600.0], [91, 64.0, 684.0], [92, 64.0, 684.0], [124, 128.0, 1132.0], [118, 128.0, 1060.0], [144, 128.0, 1412.0], [81, 32.0, 488.0], [62, 32.0, 328.0], [96, 64.0, 724.0], [62, 32.0, 320.0], [111, 64.0, 832.0], [119, 64.0, 936.0], [161, 128.0, 1492.0], [131, 128.0, 1276.0], [85, 64.0, 612.0], [95, 64.0, 804.0], [120, 128.0, 1104.0], [87, 64.0, 608.0], [75, 64.0, 524.0], [96, 64.0, 704.0], [106, 128.0, 972.0], [183, 256.0, 2164.0], [117, 128.0, 1104.0], [147, 128.0, 1408.0], [123, 128.0, 1128.0], [156, 128.0, 1460.0], [209, 256.0, 2440.0], [144, 128.0, 1344.0], [129, 128.0, 1200.0], [83, 32.0, 568.0], [99, 64.0, 732.0], [160, 256.0, 1968.0], [81, 64.0, 572.0], [113, 64.0, 928.0], [78, 64.0, 564.0], [139, 128.0, 1324.0], [142, 128.0, 1336.0], [72, 32.0, 428.0], [129, 128.0, 1168.0], [215, 256.0, 2460.0], [97, 64.0, 724.0], [110, 128.0, 1028.0], [144, 128.0, 1420.0], [74, 32.0, 456.0], [146, 128.0, 1388.0], [98, 64.0, 756.0], [125, 128.0, 1140.0], [193, 256.0, 2288.0], [149, 128.0, 1396.0], [143, 128.0, 1388.0], [122, 128.0, 1188.0], [147, 128.0, 1376.0], [95, 64.0, 700.0], [120, 128.0, 1100.0], [98, 64.0, 720.0], [94, 64.0, 680.0], [138, 128.0, 1336.0], [116, 64.0, 960.0], [40, 16.0, 152.0], [96, 64.0, 708.0], [81, 64.0, 532.0], [99, 64.0, 776.0], [93, 64.0, 664.0], [135, 128.0, 1308.0], [112, 128.0, 1020.0], [125, 128.0, 1156.0], [105, 128.0, 948.0], [92, 64.0, 684.0], [146, 128.0, 1412.0], [80, 64.0, 556.0], [94, 64.0, 700.0], [122, 128.0, 1128.0], [82, 64.0, 624.0], [101, 64.0, 744.0], [119, 128.0, 1072.0], [148, 128.0, 1388.0], [67, 32.0, 392.0], [149, 128.0, 1428.0], [95, 64.0, 700.0], [112, 128.0, 1036.0], [132, 128.0, 1224.0], [90, 64.0, 648.0], [146, 128.0, 1388.0], [137, 128.0, 1296.0], [181, 256.0, 2092.0], [138, 128.0, 1316.0], [125, 128.0, 1216.0], [141, 128.0, 1304.0], [68, 64.0, 456.0], [153, 128.0, 1448.0], [123, 128.0, 1132.0], [85, 128.0, 820.0], [80, 64.0, 616.0], [123, 128.0, 1176.0], [129, 128.0, 1184.0], [151, 128.0, 1392.0], [91, 64.0, 736.0], [120, 128.0, 1088.0], [148, 128.0, 1468.0], [209, 256.0, 2544.0], [71, 64.0, 508.0], [132, 128.0, 1172.0], [153, 128.0, 1476.0], [97, 64.0, 768.0], [92, 64.0, 692.0], [97, 64.0, 768.0], [143, 128.0, 1400.0], [85, 64.0, 640.0], [91, 64.0, 692.0], [148, 128.0, 1424.0], [96, 64.0, 660.0], [115, 128.0, 1124.0], [77, 64.0, 560.0], [175, 128.0, 1744.0], [138, 128.0, 1316.0], [176, 128.0, 1748.0], [115, 128.0, 1048.0], [65, 64.0, 444.0], [189, 256.0, 2252.0], [221, 256.0, 2552.0], [65, 32.0, 356.0], [156, 128.0, 1480.0], [119, 128.0, 1108.0], [128, 128.0, 1216.0], [130, 128.0, 1224.0], [85, 64.0, 596.0], [125, 128.0, 1204.0], [129, 64.0, 1076.0], [159, 128.0, 1548.0], [121, 64.0, 1016.0], [139, 128.0, 1280.0], [164, 128.0, 1512.0], [60, 32.0, 348.0], [80, 64.0, 572.0], [155, 128.0, 1548.0], [63, 64.0, 436.0], [91, 64.0, 668.0], [136, 64.0, 1208.0], [53, 32.0, 256.0], [90, 64.0, 632.0], [104, 128.0, 936.0], [141, 128.0, 1380.0], [133, 64.0, 1096.0], [157, 128.0, 1520.0], [158, 128.0, 1512.0], [169, 128.0, 1624.0], [132, 128.0, 1280.0], [142, 128.0, 1380.0], [145, 128.0, 1384.0], [114, 128.0, 1076.0], [144, 128.0, 1392.0], [86, 32.0, 556.0], [112, 128.0, 1020.0], [149, 128.0, 1428.0], [65, 32.0, 372.0], [259, 256.0, 3108.0], [113, 64.0, 856.0], [106, 64.0, 812.0], [84, 64.0, 604.0], [93, 64.0, 688.0], [93, 64.0, 736.0], [151, 128.0, 1440.0], [91, 64.0, 652.0], [126, 128.0, 1152.0], [100, 64.0, 768.0], [89, 64.0, 632.0], [95, 64.0, 756.0], [85, 64.0, 596.0], [148, 128.0, 1408.0], [73, 32.0, 412.0], [151, 128.0, 1432.0], [82, 64.0, 576.0], [152, 128.0, 1472.0], [102, 64.0, 796.0], [157, 128.0, 1512.0], [56, 32.0, 284.0], [194, 128.0, 2060.0], [90, 64.0, 632.0], [121, 128.0, 1168.0], [89, 64.0, 644.0], [72, 32.0, 412.0], [112, 128.0, 1020.0], [124, 128.0, 1148.0], [135, 128.0, 1288.0], [251, 256.0, 3056.0], [133, 128.0, 1296.0], [97, 64.0, 772.0], [121, 128.0, 1108.0], [151, 128.0, 1440.0], [207, 256.0, 2436.0], [103, 64.0, 752.0], [79, 64.0, 572.0], [107, 128.0, 968.0], [140, 128.0, 1328.0], [131, 128.0, 1180.0], [75, 64.0, 548.0], [78, 64.0, 532.0], [131, 128.0, 1252.0], [155, 128.0, 1408.0], [229, 256.0, 2796.0], [97, 64.0, 708.0], [137, 128.0, 1228.0], [49, 32.0, 248.0], [135, 128.0, 1312.0], [163, 128.0, 1612.0], [107, 64.0, 868.0], [116, 128.0, 1068.0], [99, 64.0, 764.0], [171, 256.0, 2024.0], [88, 64.0, 604.0], [87, 64.0, 648.0], [57, 32.0, 304.0], [131, 128.0, 1288.0], [127, 128.0, 1168.0], [131, 128.0, 1180.0], [132, 128.0, 1272.0], [148, 128.0, 1376.0], [130, 128.0, 1220.0], [187, 256.0, 2156.0], [108, 64.0, 876.0], [93, 64.0, 708.0], [99, 64.0, 716.0], [122, 64.0, 988.0], [155, 128.0, 1452.0], [132, 128.0, 1280.0], [84, 64.0, 592.0], [150, 128.0, 1436.0], [74, 64.0, 500.0], [138, 128.0, 1316.0], [168, 128.0, 1756.0], [97, 64.0, 724.0], [89, 64.0, 652.0], [68, 64.0, 456.0], [88, 64.0, 628.0], [89, 64.0, 628.0], [85, 64.0, 644.0], [98, 64.0, 720.0], [147, 128.0, 1376.0], [121, 128.0, 1088.0], [99, 64.0, 688.0], [136, 128.0, 1248.0], [122, 128.0, 1124.0], [99, 64.0, 732.0], [119, 128.0, 1068.0], [124, 128.0, 1176.0], [105, 64.0, 848.0], [85, 64.0, 592.0], [76, 32.0, 496.0], [177, 256.0, 2160.0], [120, 128.0, 1140.0], [138, 128.0, 1348.0], [143, 128.0, 1360.0], [56, 32.0, 296.0], [147, 128.0, 1372.0], [160, 128.0, 1492.0], [131, 128.0, 1244.0], [168, 128.0, 1544.0], [104, 64.0, 760.0], [99, 64.0, 752.0], [65, 32.0, 384.0], [180, 128.0, 1932.0], [84, 64.0, 600.0], [89, 64.0, 656.0], [126, 128.0, 1144.0], [151, 128.0, 1428.0], [135, 128.0, 1304.0], [84, 64.0, 592.0], [182, 256.0, 2228.0], [100, 128.0, 952.0], [85, 64.0, 624.0], [127, 128.0, 1148.0], [198, 256.0, 2392.0], [89, 64.0, 672.0], [79, 64.0, 564.0], [98, 64.0, 732.0], [81, 64.0, 576.0], [168, 128.0, 1664.0], [140, 128.0, 1376.0], [94, 64.0, 692.0], [83, 64.0, 604.0], [179, 256.0, 2120.0], [112, 64.0, 936.0], [117, 64.0, 964.0], [100, 128.0, 956.0], [128, 64.0, 1044.0], [138, 128.0, 1328.0], [149, 128.0, 1400.0], [145, 128.0, 1392.0], [75, 32.0, 444.0], [110, 64.0, 828.0], [126, 64.0, 1036.0], [95, 64.0, 688.0], [78, 64.0, 564.0], [103, 64.0, 808.0], [111, 128.0, 1016.0], [189, 256.0, 2288.0], [110, 64.0, 836.0], [168, 256.0, 2012.0], [139, 128.0, 1296.0], [80, 64.0, 572.0], [111, 128.0, 1016.0], [133, 128.0, 1280.0], [109, 64.0, 872.0], [187, 256.0, 2156.0], [140, 128.0, 1332.0], [90, 64.0, 676.0], [79, 64.0, 568.0], [115, 128.0, 1080.0], [163, 128.0, 1556.0], [140, 128.0, 1372.0], [154, 128.0, 1576.0], [101, 64.0, 728.0], [100, 64.0, 736.0], [124, 128.0, 1172.0], [124, 128.0, 1140.0], [166, 256.0, 2000.0], [148, 128.0, 1424.0], [73, 32.0, 464.0], [131, 128.0, 1272.0], [63, 32.0, 356.0], [106, 64.0, 836.0], [80, 64.0, 576.0], [152, 128.0, 1444.0], [91, 64.0, 728.0], [180, 128.0, 1876.0], [139, 128.0, 1304.0], [70, 64.0, 468.0], [147, 128.0, 1376.0], [100, 64.0, 720.0], [86, 64.0, 616.0], [69, 64.0, 468.0], [108, 64.0, 884.0], [95, 64.0, 712.0], [151, 128.0, 1460.0], [136, 128.0, 1312.0], [212, 256.0, 2452.0], [194, 256.0, 2312.0], [125, 128.0, 1140.0], [158, 128.0, 1524.0], [96, 64.0, 704.0], [187, 256.0, 2172.0], [90, 64.0, 760.0], [44, 16.0, 172.0], [146, 128.0, 1312.0], [177, 256.0, 2080.0], [146, 128.0, 1372.0], [144, 128.0, 1392.0], [138, 128.0, 1320.0], [139, 128.0, 1240.0], [89, 64.0, 716.0], [80, 64.0, 568.0], [134, 128.0, 1296.0], [133, 128.0, 1224.0], [125, 128.0, 1116.0], [110, 128.0, 1012.0], [155, 128.0, 1460.0], [86, 64.0, 612.0], [131, 128.0, 1244.0], [151, 128.0, 1440.0], [76, 64.0, 556.0], [130, 128.0, 1164.0], [99, 64.0, 792.0], [80, 64.0, 572.0], [130, 128.0, 1256.0], [138, 128.0, 1260.0], [143, 128.0, 1364.0], [149, 128.0, 1432.0], [123, 128.0, 1148.0], [149, 128.0, 1428.0], [86, 64.0, 600.0], [123, 128.0, 1116.0], [124, 128.0, 1196.0], [158, 128.0, 1684.0], [123, 128.0, 1084.0], [310, 512.0, 4604.0], [199, 256.0, 2332.0], [148, 128.0, 1396.0], [129, 128.0, 1248.0], [89, 64.0, 656.0], [176, 256.0, 2080.0], [143, 128.0, 1356.0], [99, 64.0, 780.0], [67, 64.0, 456.0], [89, 64.0, 632.0], [209, 256.0, 2436.0], [126, 128.0, 1244.0], [150, 128.0, 1432.0], [136, 128.0, 1292.0], [141, 128.0, 1352.0], [103, 64.0, 840.0], [143, 128.0, 1344.0], [116, 128.0, 1056.0], [90, 64.0, 660.0], [140, 128.0, 1340.0], [209, 256.0, 2436.0], [55, 32.0, 276.0], [147, 128.0, 1360.0], [93, 64.0, 708.0], [150, 128.0, 1432.0], [152, 128.0, 1460.0], [131, 128.0, 1244.0], [72, 32.0, 416.0], [115, 128.0, 1048.0], [55, 32.0, 284.0], [109, 64.0, 824.0], [140, 128.0, 1328.0], [106, 64.0, 884.0], [71, 64.0, 472.0], [190, 128.0, 1936.0], [123, 64.0, 1008.0], [118, 64.0, 952.0], [154, 128.0, 1452.0], [93, 64.0, 688.0], [140, 128.0, 1388.0], [125, 128.0, 1140.0], [60, 32.0, 344.0], [136, 128.0, 1252.0], [109, 64.0, 896.0], [81, 64.0, 576.0], [141, 128.0, 1352.0], [157, 128.0, 1528.0], [77, 32.0, 468.0], [201, 256.0, 2360.0], [200, 256.0, 2336.0], [194, 256.0, 2332.0], [149, 128.0, 1380.0], [111, 64.0, 892.0], [132, 128.0, 1296.0], [92, 64.0, 656.0], [102, 64.0, 788.0], [141, 128.0, 1376.0], [202, 256.0, 2396.0], [177, 128.0, 1860.0], [119, 64.0, 988.0], [67, 64.0, 452.0], [66, 32.0, 388.0], [117, 64.0, 932.0], [189, 256.0, 2276.0], [88, 64.0, 608.0], [196, 256.0, 2256.0], [67, 32.0, 388.0], [141, 128.0, 1328.0], [135, 128.0, 1288.0], [198, 256.0, 2340.0], [96, 64.0, 692.0], [106, 64.0, 868.0], [106, 128.0, 972.0], [65, 32.0, 384.0], [78, 64.0, 548.0], [207, 256.0, 2432.0], [133, 128.0, 1284.0], [118, 128.0, 1060.0], [90, 64.0, 736.0]]

steps, max_tile, score = [0, 1, 2]

stat = score

max_x = 0
for i in data:
    max_x = max(max_x, i[stat])
max_x = int(max_x)

x = np.arange(0, int(max_x), 1)
y = np.zeros(x.shape)

for i in data:
    for j in range(int(i[stat])):
        y[j] += 1

y = y / len(data) * 100

plt.plot(x, y)
plt.show()