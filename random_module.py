from random import *
# Password generation using random module choice() function
n = randint(8,16)
char = [chr(33),chr(34),chr(35),chr(36),chr(37),chr(38),chr(39),chr(40),chr(41),chr(42),
        chr(43),chr(44),chr(45),chr(46),chr(47),chr(48),chr(49),chr(50),chr(51),chr(52),
        chr(53),chr(54),chr(55),chr(56),chr(57),chr(58),chr(59),chr(60),chr(61),chr(62),
        chr(63),chr(64),chr(65),chr(66),chr(67),chr(68),chr(69),chr(70),chr(71),chr(72),
        chr(73),chr(74),chr(75),chr(76),chr(77),chr(78),chr(79),chr(80),chr(81),chr(82)
        ,chr(83),chr(84),chr(85),chr(86),chr(87),chr(88),chr(89),chr(90),chr(91),chr(92),
        chr(93),chr(94),chr(95),chr(96),chr(97),chr(98),chr(99),chr(100),chr(101),chr(102),
        chr(103),chr(104),chr(105),chr(106),chr(107),chr(108),chr(109),chr(110),chr(111),
        chr(112),chr(113),chr(114),chr(115),chr(116),chr(117),chr(118),chr(119),chr(120),
        chr(121),chr(122),chr(123),chr(124),chr(125)]
y = ''
for i in range(n):
    x = choice(char)
    y = y + x

print("Password: ",y)
