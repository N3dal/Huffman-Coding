"""
    Contain all needed tools for this project;
"""

from os import system
from os import name
import math

OS_NAME = name

TEST_MESSAGE = """
uV2nUdR8plkiNEh
fcYWzRVDR8uVkJA
X7SVsVlu9hDe0HB
O2F2qPSKiYbxu0y
ITtjDbF5dJOfEQl
1gxNgsy03ymYVue
uYs4nzae88IukSh
ZYXUb1eakS2E64V
fX1SrYUcj7wsyPW
Ki3TgOvi6y0Btn6
PeUZZkKTbY89syz
Za8z1e87kLtbEGN
WN70nnzag0yQkxw
YH0JknWdwVXEvL2
Hufh3Qppb6vKlXj
7cBzpKoaETKnf68
fWaWlpIpnCLUWyV
uqY1QpZdbD5I40o
cE8k0sv7Ppfmq3b
JPzmMm2PWruFmqm
IRBt0xhgY1tsNCm
8X0hgfkMGNFmXKG
u2YYxkmXUXdap5z
o3mNPU3Oq2LufQ6
Ptwcl49IXkG64K2
J7AaW85ISJtdEls
uUP5feVRg7oFVq7
sOMgJgVNCcl2fpb
RDrvo2NLg1BgPvT
TboThiKvUFa5NGU
cGvXDDBJ4qucmhc
nsS61ag7rEPnkwV
ZhWdh8uo0JHbTxM
nVwBHTWYSzd52Gm
0ifXzX9r9hzYaCh
BeCDGZnsQeGwvFA
wKmOKXhMmSyzEhA
gdAW8ggNLNCkecA
WukHoM5bo2j3G83
EhJuzqe4lqYoQua
BUvnLthq5WbWW0X
FzHsV0tuGdQh7vy
EQaJyUn7o3ykVic
P9dXKyslCPTF42L
TgifgsjjSZxYzhb
IRzh9fIrLQ8IWh1
QwbVz4DJ0qULsuV
1tLBEOIEKmacksW
HSy87ZeKRHlRcZ1
HknOEkunMUCMwEl
5Oj0d3DxLAcLD5j
VQTeUE0IB7bAxyk
THgFJtmpGJACBnl
SMd0l5uDsZKSEcj
sBani7epDuOoOdh
71SGFmfypBDhcEg
V1MfXqHcITB6syt
Gx9YEJaIz1RcURX
WjiX049MzhiMwph
Pntc5rZ42MyobpG
T6CWB1kJX6yjeYl
wklzSHSfdgqr9Ya
FWsIsEafp9vvJpZ
eDif1csoEF5b4oy
Af2gKY9N7Ri9cfl
Xnn3DRG4eLVRCG9
p3tE6o4XmounXYo
0tc7FkMzRIEM9jk
MYmhGjlsSlJDKs0
yzcUzCNYSQzW19B
ur6r34J3AqVD0JS
i9oQ55iHaxGKT7t
9fvuH3im9jBQDn9
3hUZLXcb1IHpmS1
zFLzhlcSx80NBa7
MMrOPgNrp00J8Ad
M0mdR65X1lQro4E
RXDY4PFqHNUN9D8
GmpJv9uPLQqKPyf
yAAdWwg47x26mIv
l6lvaUfpulKaQrj
IBEI3gderFyiesl
adRq8Z093lE9CyB
q7ORZ8CTOA3IUFX
kcGNpKl7yxv7Y12
7WIWKWZ6bC9c6Ar
3oeAFFaNR95ypa5
cjZUgJ3o1LhPnAZ
J3DjEGdKVYiduVO
214nahKVXijnGq9
idLiQmbo1saGxwr
jqZ16BETM96Nz0q
rIigev7modjiRIZ
ZjqWjseurDBFWkt
KeuqQyq5rYjxlRi
fnhN3MzWS8KN6tG
KFsuFtv8o88G1Q7
TGA9aDCogiHT5jx
KydX680o3goOzfa
dpJo7y0Xkc0G83P
"""


def clear():
    """
        :ARGS:
            None;

        :RETURNS:
            return None;

        :INFO:
            wipe terminal screen;
    """

    if OS_NAME == "posix":
        # for *nix machines;
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for all other os in this world;
        # system("your-command-here")
        pass

    return None


def message_chars_probability(message: str):
    """
        :ARGS:  
            message:str => the message we want to count chars probability.

        :RETURNS:
            return dict contain each char with its probability;

        :INFO:
            find the probability for each character in a give string;
    """

    assert isinstance(
        message, str), f"message must be a str type not {type(message)}"

    message_length = len(message)

    return {char: (message.count(char) / message_length) for char in set(message)}
