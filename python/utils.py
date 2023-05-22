"""
    Contain all needed tools for this project;
"""

from os import system
from os import name
import string
from random import choice

OS_NAME = name

TEST_MESSAGE_2 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed faucibus bibendum velit, vel euismod urna laoreet ac.
Sed vel neque eget justo tempus ultrices. Duis euismod,
mi sed vestibulum faucibus, risus sapien suscipit sapien,
id bibendum dui quam quis nisl. Duis rutrum, ipsum at posuere sodales,
mauris neque convallis turpis, vel sagittis tellus velit ut nunc. Proin magna justo,
dignissim sit amet blandit ac, 
faucibus in orci. Praesent ut est sit amet libero consequat
lobortis non non augue. Sed ut felis auctor, laoreet massa nec, commodo leo. Donec at 
risus euismod, facilisis ipsum eget, dignissim metus. Nam nec elementum nunc, sit amet dictum orci. Donec
ultrices nulla non sapien finibus, quis bibendum ipsum egestas. Nullam bibendum, nisl ac bibendum maximus, sapien
lectus convallis sapien, eget venenatis justo risus vitae diam.
Sed euismod, massa ut aliquam tempus, mauris odio convallis mauris, sit amet placerat
em dui ut quam. Nulla facilisi. Suspendisse velit nisl, aliquam eu
magna a, consequat varius purus. Fusce eget enim id magna commodo viverra.
Integer euismod, nisl in fringilla blandit, arcu nunc bibendum risus, eu ultricies nisi mauris eget velit.
Praesent ac mauris eget sapien pellentesque tempus.
Ut non augue id felis lobortis dapibus.
Sed id leo ac felis porta eleifend.
Nullam tincidunt, urna ut convallis bibendum, tortor risus blandit tortor, vitae semper tortor elit vel urna.
Sed eleifend sapien vel velit interdum, id venenatis sapien laoreet.
Donec varius bibendum justo, vel malesuada lectus bibendum eu.
Mauris vitae arcu nisl.
Sed euismod urna vel nulla euismod, vel ullamcorper libero feugiat.
Nulla facilisi.
In hac habitasse platea dictumst.
Sed massa tellus, ullamcorper vel fermentum vel, fermentum vel lorem.
Sed vitae tellus euismod, dignissim libero id, facilisis ex.
Sed non ex vel elit tristique pharetra.
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
Duis vitae urna a urna dignissim maximus.
Insed sapien in mauris 
fringilla bibendum.
Ut eget turpis ut turpis sagittis imperdiet.
Aliquam erat volutpat.
Nullam auctor tortor sit amet magna bibendum, id facilisis erat fringilla.
Sed vel felis vel velit auctor fermentum.
Aliquam vitae velit vitae elit aliquet laoreet.
Integer cursus, nibh quis pretium commodo, magna massa luctus sapien, vel sagittis mi risus ut nisi.
Fusce vel nulla eget felis laoreet sodales.
Etiam id augue ac dui posuere vestibulum.
Donec consectetur dui eu mi bibendum, id posuere nisl bibendum.
Sed auctor, felis in auctor tincidunt, ipsum dolor aliquet eros, a consequat ex turpis vel libero.
Cras hendrerit, nisi id consectetur placerat, erat velit scelerisque purus, eu euismod
leo mauris vel nisl.
Aliquam sed velit euismod, malesuada sapien eu,
finibus odio.
Phasellus quis nunc sed erat porta convallis et vel mauris.
Sed eget libero vitae lectus faucibus laoreet.
Sed faucibus, mauris nec lobortis facilisis, lacus metus ullamcorper dui, ac bibendum dolor ante vitae odio.
Morbi sit amet eleifend velit.
Mauris eget ante non velit commodo lacinia.
Sed vehicula sapien eget odio dapibus, vel varius nisl malesuada.
Aliquam ante est, tincidunt id orci non, lobortis gravida turpis.
Integer dictum aliquet tortor sed tincidunt.
Fusce commodo, magna at lacinia blandit, sapien nunc faucibus magna, vitae malesuada est mauris eu metus.
Quisque sed enim vel nisi accumsan feugiat.
Nulla facilisi.
Suspendisse eget ante quis leo rutrum consequat vel at mauris.
Sed nec eros non arcu efficitur fermentum sit amet id diam.
Ut sit amet odio nec leo bibendum dictum sed vel eros.
Fusce id ante eget ipsum bibendum rhoncus a in magna.
Nunc vitae nunc id lacus sollicitudin
rhoncus.
Donec auctor tortor sit amet sapien mattis, id pharetra enim bibendum.
Nam euismod, quam id fermentum luctus, metus arcu pulvinar magna, at lobortis elit velit et nisl.
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Cras id quam sed orci feugiat bibendum.
Nullam sodales, augue eget imperdiet faucibus, augue turpis viverra augue, quis molestie elit ante non nulla.
Nunc commodo convallis libero eget ultricies.
Sed et diam porttitor, lacinia nulla quis, euismod mauris.
Suspendisse in nulla in nunc malesuada aliquam.
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; In non bibendum nulla.
Pellentesque euismod, elit vel bibendum bibendum, sem quam maximus augue, quis scelerisque magna orci in est.
Sed at justo sit amet justo rhoncus lobortis eu ac ligula.
Maecenas fringilla, risus non commodo lacinia, enim ipsum venenatis risus, et malesuada quam mauris
el ex.
Sed laoreet, augue eget pulvinar volutpat, ipsum urna ultricies tortor, vitae egestas ipsum velit ac mi.
Quisque malesuada, mauris ut tempus bibendum, purus mi interdum ligula, a elementum odio elit non erat.
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Ut in lorem vitae nunc eleifend tristique.
Cras tincidunt aliquet nulla, vitae egestas risus venenatis vitae.
Quisque interdum eros quis sem blandit, eu porttitortortor malesuada.
Nullam eget eros nunc.
Phasellus vestibulum massa sit amet ante venenatis, ac mollis purus scelerisque.
Fusce gravida sodales nibh, vel imperdiet velit.
Sed at purus sapien.
Nullam eget blandit tortor.
Donec vel justo euismod, tempus dolor eget, bibendum elit.
Suspendisse potenti.
Morbi auctor odio nec enim dictum, vel tincidunt mauris bibendum. Integer congue orci sit amet velit consectetur,
vel imperdiet eros efficitur. Aliquam non felis tincidunt, pellentesque elit a, fermentum nibh. Nullam aliquet,
nibh et tristique euismod, velit orci gravida enim, vel tincidunt nisl ante id dolor. Duis vestibulum blandit orci eu mollis. Suspendisse potenti.
duis pulvinar turpis sed est bibendum, at congue eros vestibulum. Sed mattis, eros quis rutrum feugiat,
tellus leo accumsan eros, ac imperdiet sapien ipsum nec sapien. Quisque pellentesque ipsum vitae ante finibus
in malesuada ante cursus. Pellentesque convallis, sapien et consectetur varius, urna est ultrices massa,
vel rutrum augue lacus sed nulla. Nullam quis sem eget urna mattis varius sit amet vel sapien. Fusce ut sapien sed ex congue eleifend.
Mauris laoreet sapien eget tincidunt molestie. Sed sed efficitur risus.
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam suscipit,
neque sed porta rutrum, nulla metus maximus sapien, vel elementum nulla neque vel ipsum. Proin a elit non lacus commodo placerat.
Duis rhoncus, velit id tincidunt scelerisque,
ex ipsum maximus nisl, ac bibendum est lorem sit amet diam. Sed eget volutpat dui, non fringilla tellus.
Suspendisse convallis, nisl at pulvinar lacinia, orci elit auctor turpis, sed pharetra velit metus vel lorem. In a leo eget urna malesuada rhoncus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean commodo, dui ut elementum venenatis, orci nulla convallis
"""

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
""" * 10

TEST_MESSAGE_3 = """
Gay one the what walk then she. Demesne mention promise you justice arrived way. Or increasing to in especially inquietude companions acceptance admiration. Outweigh it families distance wandered ye an. Mr unsatiable at literature connection favourable. We neglected mr perfectly continual dependent.

Lose eyes get fat shew. Winter can indeed letter oppose way change tended now. So is improve my charmed picture exposed adapted demands. Received had end produced prepared diverted strictly off man branched. Known ye money so large decay voice there to. Preserved be mr cordially incommode as an. He doors quick child an point at. Had share vexed front least style off why him.

Am terminated it excellence invitation projection as. She graceful shy believed distance use nay. Lively is people so basket ladies window expect. Supply as so period it enough income he genius. Themselves acceptance bed sympathize get dissimilar way admiration son. Design for are edward regret met lovers. This are calm case roof and.

Manor we shall merit by chief wound no or would. Oh towards between subject passage sending mention or it. Sight happy do burst fruit to woody begin at. Assurance perpetual he in oh determine as. The year paid met him does eyes same. Own marianne improved sociable not out. Thing do sight blush mr an. Celebrated am announcing delightful remarkably we in literature it solicitude. Design use say piqued any gay supply. Front sex match vexed her those great.

Believing neglected so so allowance existence departure in. In design active temper be uneasy. Thirty for remove plenty regard you summer though. He preference connection astonished on of ye. Partiality on or continuing in particular principles as. Do believing oh disposing to supported allowance we.

Needed feebly dining oh talked wisdom oppose at. Applauded use attempted strangers now are middleton concluded had. It is tried ﻿no added purse shall no on truth. Pleased anxious or as in by viewing forbade minutes prevent. Too leave had those get being led weeks blind. Had men rose from down lady able. Its son him ferrars proceed six parlors. Her say projection age announcing decisively men. Few gay sir those green men timed downs widow chief. Prevailed remainder may propriety can and.

Ladyship it daughter securing procured or am moreover mr. Put sir she exercise vicinity cheerful wondered. Continual say suspicion provision you neglected sir curiosity unwilling. Simplicity end themselves increasing led day sympathize yet. General windows effects not are drawing man garrets. Common indeed garden you his ladies out yet. Preference imprudence contrasted to remarkably in on. Taken now you him trees tears any. Her object giving end sister except oppose.

Unpleasant nor diminution excellence apartments imprudence the met new. Draw part them he an to he roof only. Music leave say doors him. Tore bred form if sigh case as do. Staying he no looking if do opinion. Sentiments way understood end partiality and his.

Talking chamber as shewing an it minutes. Trees fully of blind do. Exquisite favourite at do extensive listening. Improve up musical welcome he. Gay attended vicinity prepared now diverted. Esteems it ye sending reached as. Longer lively her design settle tastes advice mrs off who.

When be draw drew ye. Defective in do recommend suffering. House it seven in spoil tiled court. Sister others marked fat missed did out use. Alteration possession dispatched collecting instrument travelling he or on. Snug give made at spot or late that mr.

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



def generate_random_text(length:int=1000):
    """
        Docstring;
    """
    
    text = ""
    
    for _ in range(length):
        text += choice(string.ascii_letters + string.digits)
    
    
    return text
    
    
    