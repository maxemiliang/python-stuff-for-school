#coding=utf-8
import time
'''

Detta är en bubbelsorterings funktion som tar en lista som parameter och returnar den sorterade listan,
Den returnerar falskt om listan är tom eller om det är fel värde

'''
def bubble(values):
    try:
        if len(values) == 0:
            return False
    except TypeError:
        return False

    end = len(values) - 1

    while end > 0:
        now = 1
        while now <= end:
            if (values[now] < values[now - 1]):
                values[now], values[now - 1] = values[now - 1], values[now]
            now += 1
        end -= 1
    return values

def uppgift1(val):
    sortlist = bubble(val)
    if sortlist != False:
        print sortlist
    else:
        print "That's an empty list/a bad parameter"


def uppgift2(val):
    sort_timetest(val)

'''

Denna funktion tar en lista som parameter och provkör den med min implementation av bubble sort och sedan mot pythons inbyggda sort()

'''
def sort_timetest(val):

    list_size = len(val)

    # Min eget implementerade bubble sort
    t1 = time.clock()
    sorted_list = bubble(val)
    t2 = time.clock()

    # omvandla till sekunder istället
    exec_bubble = (t2 - t1) * 1000

    val_list = val

    # Inbyggda sorteringen
    t1 = time.clock()
    val_list.sort()
    t2 = time.clock()

    #omvandla till sekunder istället
    exec_built_in = (t2 - t1) * 1000

    print "Execution completed"
    print "Results:"
    print "Algorithm: Bubble Sort"
    print "----------------------"
    print "Time: {}".format(exec_bubble)
    print "List size: {}".format(list_size)
    print "Result: {}".format(sorted_list)
    print "----------------------"
    print "\n"
    print "Algorithm: Built-in sort()"
    print "----------------------"
    print "Time: {}".format(exec_built_in)
    print "List size: {}".format(list_size)
    print "Result: {}".format(val_list)
    print "----------------------"
    print "\n"

def check_file(f):
    try:
        of = open(f, "r")
        of.close()
        return True
    except IOError:
        return False

def sort_from_file(f):
    if check_file(f):
        file = open(f, "r")
        for line in file:
            print line
    else:
        uppgift3b()

def uppgift3b():
    file_to_open = raw_input("What file do you want to open?:")
    sort_from_file(file_to_open)



test_val_huge = [8651, 4496, 9013, 3915, 5570, 4608, 9965, 10709, 12044, 7797, 12342, 9644, 10543, 5451, 9645, 12056, 10168, 4867, 4579, 11004, 1257, 11386, 10794, 9915, 6588, 9770, 11768, 3244, 11403, 11290, 9837, 6187, 10584, 5419, 3458, 3844, 2584, 2093, 4909, 4358, 4907, 6541, 1415, 6318, 4733, 5703, 746, 1172, 9414, 6169, 8602, 6292, 6353, 5411, 3808, 6760, 9663, 11833, 7918, 6265, 4106, 5191, 6245, 7480, 3308, 426, 3102, 3673, 6675, 2126, 1836, 10755, 10939, 5954, 6969, 6183, 7516, 929, 3919, 1274, 512, 10812, 10242, 2350, 3056, 6728, 1632, 3716, 4006, 5246, 10046, 315, 8630, 2538, 2988, 2582, 2920, 10514, 10760, 9859, 9657, 1504, 369, 4370, 7193, 8577, 907, 12078, 12010, 3094, 9098, 2557, 4831, 10287, 11277, 11091, 5845, 11864, 10982, 3736, 11476, 11116, 111, 1378, 8396, 7455, 56, 8187, 9797, 2520, 9738, 5302, 10280, 8019, 5781, 2874, 7770, 5663, 10562, 11089, 9085, 6390, 7836, 9332, 8590, 7766, 11805, 3366, 8198, 3527, 5608, 12062, 5280, 3908, 202, 6172, 10635, 10082, 1712, 9565, 6029, 8295, 9605, 8411, 4749, 7761, 10045, 9421, 9794, 1635, 4902, 4701, 2793, 4314, 3127, 6266, 2598, 1645, 7550, 8287, 11869, 8217, 6310, 10860, 1143, 7882, 3930, 11195, 5553, 156, 3967, 1016, 5202, 8635, 2745, 57, 1396, 9185, 6146, 681, 6055, 7572, 3408, 11395, 6782, 8867, 11725, 3035, 11787, 7911, 7890, 1116, 5956, 1621, 926, 6369, 9699, 9731, 1757, 8778, 9528, 12024, 11178, 12242, 878, 2945, 590, 8566, 10920, 8003, 12186, 3746, 7726, 1377, 11542, 136, 5963, 287, 6110, 1076, 5182, 8483, 4031, 5118, 3613, 6360, 3355, 3762, 1915, 11149, 9961, 11928, 12014, 126, 5250, 11628, 965, 5289, 5814, 11163, 2837, 5839, 1804, 1714, 5537, 11801, 704, 11141, 1289, 9247, 5016, 11021, 4898, 6794, 8556, 11797, 7084, 7731, 9649, 8223, 10821, 4134, 3931, 9337, 5989, 4049, 544, 5864, 4980, 6062, 8903, 155, 8531, 11617, 1572, 2530, 1312, 5859, 1583, 1414, 3081, 2771, 7305, 8933, 3469, 5911, 10099, 2121, 2884, 1011, 645, 1260, 11808, 4497, 10943, 6443, 10173, 5803, 1367, 12180, 8733, 10330, 12049, 1774, 772, 2606, 4633, 8725, 7729, 2030, 8601, 6483, 8212, 3747, 1689, 10041, 736, 4821, 6073, 4599, 6718, 7375, 12028, 3900, 2681, 1929, 5392, 596, 5278, 4735, 2629, 6922, 522, 4619, 10315, 3534, 8307, 5616, 9955, 5523, 1218, 2930, 10136, 10377, 9231, 12221, 9377, 5741, 11741, 6514, 2056, 3594, 7102, 692, 7259, 725, 6666, 6503, 12161, 7645, 10765, 10764, 11188, 6550, 8619, 8575, 12187, 11229, 9476, 7998, 10048, 5485, 11036, 4544, 7295, 7714, 11508, 10544, 6681, 7694, 3368, 11053, 9163, 12026, 6243, 4452, 217, 7975, 11243, 4870, 6944, 2110, 4357, 3313, 7723, 2023, 4299, 518, 11863, 4010, 3909, 9389, 9308, 2643, 1769, 7809, 10243, 4644, 1036, 7418, 7015, 5342, 3660, 7847, 1250, 8400, 6571, 9555, 1718, 10504, 4457, 1241, 3053, 8087, 1552, 4247, 4094, 1400, 3769, 6223, 11175, 11314, 12059, 7159, 2906, 6866, 7620, 11909, 1596, 9891, 1818, 4936, 1798, 3332, 8890, 6704, 9175, 10415, 4081, 6138, 4088, 4811, 6935, 5993, 12079, 3602, 9935, 11674, 11246, 135, 10745, 7728, 6568, 3524, 11948, 6748, 10911, 11654, 8373, 1434, 5069, 9767, 1960, 208, 9864, 8012, 2545, 2051, 3981, 980, 8690, 5571, 9998, 1736, 6194, 9856, 1558, 4830, 1458, 5805, 6763, 434, 11119, 4503, 6417, 6321, 8310, 1512, 8815, 3935, 5526, 2819, 6524, 2882, 5446, 3459, 4960, 6826, 972, 9640, 1693, 9041, 2707, 7954, 6754, 10907, 10607, 11019, 2581, 1470, 11938, 3409, 6998, 1491, 780, 8124, 8329, 1376, 10033, 11216, 7861, 1104, 1884, 11618, 6693, 11651, 4913, 9881, 9422, 10605, 10852, 2915, 1984, 11069, 5860, 441, 12265, 49, 8809, 2225, 4828, 6837, 1319, 11278, 3972, 8795, 2276, 4347, 11201, 11432, 3106, 11135, 6471, 9719, 511, 2190, 5811, 2661, 10230, 8454, 186, 6625, 4999, 8291, 8083, 8603, 811, 8334, 12011, 4666, 11731, 1177, 7738, 8897, 11335, 10326, 10417, 6176, 11143, 10160, 12334, 891, 2815, 6540, 2115, 5486, 6755, 11914, 7092, 606, 3365, 8853, 1226, 3494, 3023, 4455, 6350, 9182, 7080, 10063, 10958, 46, 6256, 5876, 971, 1191, 10424, 10445, 3735, 5886, 7220, 5276, 8594, 4904, 5640, 4771, 6812, 11992, 6261, 9367, 9076, 10482, 659, 4122, 2720, 5916, 8919, 3152, 6916, 1188, 6841, 3466, 1589, 5239, 9886, 9500, 4272, 7303, 7963, 906, 5594, 4305, 7807, 6385, 11718, 10104, 12325, 7607, 2651, 6522, 3410, 5241, 5970, 5670, 4469, 9278, 8781, 11347, 7777, 3669, 6337, 8337, 5852, 4629, 11334, 1779, 11312, 10837, 10685, 4573, 5027, 8913, 11769, 4757, 3741, 8242, 8303, 192, 10120, 6670, 12041, 9562, 9363, 9273, 471, 7319, 3929, 623, 1086, 7064, 5196, 3153, 1802, 10649, 2675, 11017, 4355, 12113, 9695, 982, 3481, 11298, 9550, 10610, 6773, 1426, 3280, 2090, 7888, 6767, 7664, 2444, 1496, 8388, 9229, 10524, 6284, 8712, 7206, 9174, 5008, 5529, 1283, 715, 7573, 4500, 9823, 1703, 2737, 3433, 9973, 11213, 1447, 2339, 3812, 6226, 11872, 4750, 2694, 6739, 11479, 7786, 2766, 4356, 8766, 4865, 4295, 3436, 8150, 1655, 10366, 3522, 4050, 698, 12174, 10159, 11297, 9342, 302, 2325, 8314, 10236, 1536, 5014, 1581, 4436, 7012, 5680, 3572, 11489, 12197, 10692, 9116, 10007, 6823, 6814, 10404, 2904, 11756, 8235, 4891, 6309, 11353, 5327, 5644, 11762, 10209, 5799, 59, 7149, 11680, 3027, 10743, 11154, 8558, 9611, 7337, 3737, 3584, 9039, 9940, 7843, 1211, 10968, 7997, 5005, 11690, 5204, 9557, 7793, 6861, 3231, 6839, 5548, 6972, 2161, 4407, 11181, 531, 8340, 2998, 7360, 10659, 2477, 4637, 9652, 1781, 6607, 131, 9208, 93, 1674, 6538, 3595, 4397, 1093, 9260, 4492, 5040, 8692, 11563, 7663, 7832, 5844, 5908, 2727, 10284, 7125, 4747, 2382, 9804, 1813, 11835, 10139, 10859, 3738, 5421, 9828, 3084, 5743, 3393, 6235, 199, 6447, 8466, 4680, 9338, 8061, 9696, 11275, 2461, 10246, 3583, 491, 2532, 5747, 5569, 3533, 4292, 5106, 4744, 2227, 5688, 2108, 3431, 8023, 5231, 7229, 4317, 11567, 11120, 1791, 6, 3103, 1185, 966, 1566, 10264, 9631, 11629, 6158, 5329, 9618, 3707, 7895, 3719, 3269, 9493, 7780, 6569, 9207, 8490, 11419, 7034, 2593, 4893, 91, 1921, 3079, 4807, 10151, 8206, 5632, 8172, 5554, 3405, 8445, 3792, 4674, 4690, 3374, 11701, 5733, 6015, 5888, 71, 9902, 10374, 2334, 8082, 6533, 1444, 351, 495, 9715, 10877, 2970, 3848, 8047, 6600, 1700, 9213, 10478, 2429, 6539, 5431, 7439, 5588, 4836, 1611, 5159, 10640, 11078, 6807, 5143, 7743, 8638, 1339, 1115, 9879, 10707, 10630, 12008, 1177, 6920, 5000, 10960, 455, 9583, 4944, 8521, 9435, 6840, 5020, 9895, 12149, 10007, 4963, 4389, 690, 555, 4144, 9101, 6336, 6814, 11502, 3720, 6171, 4604, 5192, 11264, 8102, 5356, 2127, 8983, 10176, 6092, 900, 8128, 3073, 6323, 1229, 7049, 12002, 8034, 8847, 1301, 7867, 6055, 12078, 8136, 11305, 7949, 10370, 3078, 5315, 7602, 734, 5890, 12159, 3666, 4528, 10105, 6136, 11249, 11854, 5645, 4257, 6194, 787, 8520, 10785, 1379, 12179, 9470, 8237, 9562, 9200, 4202, 11809, 762, 12245, 1478, 1509, 806, 7120, 1982, 8463, 1944, 10904, 10716, 9596, 5996, 4595, 11117, 2432, 10096, 1837, 8434, 5750, 3289, 1281, 9008, 5854, 6919, 292, 282, 12074, 8836, 4216, 1283, 6213, 11523, 5137, 308, 9144, 7086, 8985, 7693, 10557, 6460, 674, 6197, 9356, 6773, 1535, 10614, 2439, 8825, 3780, 1889, 7277, 9795, 5636, 2866, 2556, 7438, 7545, 6019, 2263, 843, 7523, 7264, 11791, 2575, 1461, 4088, 6209, 6411, 4064, 4310, 6526, 5308, 835, 5438, 3845, 5594, 8739, 7937, 11642, 11339, 9842, 8848, 11784, 7751, 3549, 443, 4576, 8907, 9863, 7645, 7181, 8178, 4407, 6547, 1786, 10037, 3397, 8199, 4503, 7673, 26, 353, 7085, 3508, 2937, 10029, 7842, 9786, 9840, 5317, 9219, 8372, 9437, 11513, 3159, 11539, 363, 11651, 2001, 8759, 4672, 7813, 7402, 12085, 3719, 5193, 6662, 6130, 10868, 10196, 8815, 6305, 4977, 8731, 12127, 8306, 161, 11672, 6520, 6916, 8045, 1008, 4492, 1998, 1470, 1799, 210, 1025, 12211, 4384, 1852, 1333, 205, 10352, 12283, 5652, 6708, 10304, 6790, 7426, 5969, 10532, 4605, 5439, 1973, 6378, 7969, 8592, 8294, 3962, 10429, 155, 10576, 5904, 2126, 1756, 12170, 297, 696, 10473, 611, 2939, 11596, 7611, 2751, 11560, 6639, 7027, 3703, 9798, 6995, 7674, 851, 4208, 4813, 10268, 3199, 7677, 2062, 4878, 2998, 6797, 10257, 2003, 10049, 11210, 7659, 5196, 9962, 7652, 9229, 9303, 11944, 606, 8364, 10856, 755, 64, 6809, 1184, 7531, 6144, 6873, 11704, 1828, 10314, 11359, 1335, 6421, 4570, 7318, 2411, 4267, 2006, 9960, 7963, 7623, 11330, 5510, 8481, 7044, 7041, 8822, 3766, 8447, 1131, 11916, 1583, 7588, 10744, 12164, 6596, 4873, 1418, 11963, 6463, 6374, 10562, 510, 10006, 45, 12017, 9339, 10517, 1455, 8869, 6153, 3412, 2626, 9475, 10777, 5493, 10181, 2499, 12312, 3115, 3547, 11917, 11351, 5635, 11765, 6227, 1200, 8033, 6543, 3518, 5694, 6309, 3490, 3230, 5553, 2070, 9147, 8351, 73, 5068, 1465, 2030, 951, 2468, 923, 6021, 10405, 7164, 567, 3970, 3370, 8888, 5714, 720, 3419, 987, 11881, 7799, 11012, 2569, 12134, 11180, 4830, 5881, 10851, 5215, 9946, 9848, 9799, 2143, 11718, 2004, 9914, 1922, 5074, 9623, 8251, 7117, 4211, 6780, 3965, 2929, 6864, 2451, 4669, 10164, 2053, 5902, 2247, 8255, 11450, 10941, 11919, 6296, 1735, 7771, 1574, 6198, 798, 11882, 12083, 11484, 9319, 6638, 1909, 768, 10035, 7448, 9034, 5807, 11006, 5260, 3270, 2349, 1174, 9624, 4145, 8011, 11302, 1295, 3496, 3555, 7651, 4908, 4312, 1150, 11666, 3582, 11979, 9074, 9001, 3794, 2648, 1266, 2869, 6956, 4302, 2236, 8546, 2702, 4132, 10135, 11541, 7522, 5669, 3147, 8323, 11454, 10892, 7953, 11723, 11757, 5776, 764, 1946, 984, 7753, 1130, 9228, 5242, 10690, 11133, 3590, 11574, 11655, 51, 2276, 4331, 8570, 2680, 10193, 10766, 4205, 7453, 9166, 568, 1667, 543, 4969, 514, 2406, 5374, 2039, 12314, 6010, 2028, 2733, 5050, 5911, 10225, 8829, 11139, 10649, 9070, 654, 6967, 11548, 4068, 1434, 11300, 8365, 11619, 9738, 4436, 9085, 8347, 8535, 2625, 4555, 9503, 1578, 12023, 6770, 8523, 241, 8214, 10210, 10390, 9802, 255, 8533, 285, 11055, 757, 6081, 4170, 4355, 3967, 5495, 9167, 7717, 1825, 11599, 7633, 1016, 10050, 3744, 2353, 1428, 7488, 2771, 811, 3344, 3492, 4768, 10536, 6835, 10362, 397, 4793, 6113, 2266, 2086, 932, 10895, 11328, 10188, 4625, 3420, 8083, 5247, 2781, 3671, 9492, 3831, 4659, 8849, 7760, 5030, 5289, 2067, 2035, 2493, 229, 6242, 10244, 6274, 4427, 1518, 11270, 7114, 9700, 12014, 3844, 4179, 6493, 518, 8088, 11214, 4727, 7195, 8197, 542, 5484, 3111, 2129, 8686, 1614, 12190, 9706, 2993, 10867, 11703, 6536, 5710, 8793, 10189, 9727, 8299, 11706, 8644, 2793, 3909, 7728, 3076, 5837, 12108, 4049, 2766, 12136, 9852, 8804, 5117, 9418, 3245, 2107, 10128, 8932, 11848, 12001, 6601, 11088, 8402, 3943, 10981, 10872, 5618, 1795, 3679, 7095, 8119, 2367, 11673, 7885, 9716, 237, 3705, 5442, 7690, 12035, 10918, 113, 9165, 10111, 9968, 1408, 3966, 2815, 2570, 849, 5849, 3641, 7584, 5454, 6506, 7648, 10662, 11354, 11615, 248, 11545, 6262, 9178, 11043, 11695, 4376, 1793, 3025, 2790, 823, 4543, 5267, 7945, 4234, 405, 459, 10418, 10206, 796, 7511, 10566, 4713, 1427, 11077, 8155, 413, 10988, 83, 3333, 1906, 9381, 1480, 12217, 74, 1917, 4842, 2207, 10940, 4494, 7159, 4957, 11329, 5664, 964, 1603, 5796, 7818, 3396, 6038, 1665, 3601, 85, 3465, 11852, 5809, 6022, 7770, 3047, 7821, 11136, 5639, 7136, 2728, 307, 11261, 1468, 6085, 5799, 11357, 8975, 8108, 2909, 3771, 7533, 1708, 10237, 7860, 4147, 5588, 10799, 2749, 9655, 2278, 11555, 8439, 9864, 6884, 9018, 10222, 47, 1456, 2007, 4631, 9883, 6277, 5763, 1860, 3993, 4457, 8750, 1494, 6435, 9772, 9328, 7895, 3239, 3924, 7680, 760, 11065, 7653, 9592, 10236, 174, 7203, 12093, 8931, 4349, 995, 10415, 5835, 10937, 2845, 10160, 3444, 7043, 1299, 6532, 4089, 6910, 572, 6434, 9944, 1323, 4785, 7010, 1755, 9563, 11891, 2088, 1561, 7762, 1324, 1236, 11397, 9988, 10399, 8586, 956, 11307, 10008, 9794, 28, 7272, 9262, 7691, 4432, 9733, 4573, 9337, 8198, 4152, 10596, 6987, 3923, 6202, 6703, 9180, 78, 7929, 723, 4032, 11186, 203, 2168, 3118, 7477, 2285, 2717, 6222, 1496, 8969, 7764, 12061, 8778, 7333, 6012, 1159, 77, 9821, 7137, 9687, 9929, 11564, 503, 2535, 9491, 6538, 773, 10046, 8563, 9089, 6540, 3227, 7607, 6244, 11744, 9458, 1128, 10397, 3732, 8462, 144, 2872, 7708, 5183, 6653, 10705, 2052, 1244, 8536, 5105, 790, 1875, 3529, 11997, 3561, 1314, 277, 9668, 4138, 6620, 822, 5565, 3150, 3568, 11960, 2326, 7072, 4429, 8074, 5657, 9362, 2673, 7947, 9277, 2676, 3497, 2605, 10032, 6669, 4735, 11471, 6399, 4146, 3911, 8243, 1859, 3580, 3122, 10881, 1857, 5552, 5966, 463, 7843, 456, 11893, 7305, 5784, 7811, 8137, 687, 2256, 2046, 7620, 3166, 4970, 9354, 3179, 7001, 2878, 10681, 11665, 3152, 6059, 6730, 4229, 6958, 7286, 315, 2166, 9566]
test_val_min = [1,5,6,3,2]
empty = 0
#uppgift1(test_val)
#uppgift2(test_val_min)
#uppgift2(test_val_huge)
uppgift3b()




