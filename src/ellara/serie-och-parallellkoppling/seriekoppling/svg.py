import schemdraw
import schemdraw.elements as e
import schemdraw.elements
from time import time

e.style(e.STYLE_IEC)
schemdraw.config(font="NewComputerModernMath", mathfont="cm")

start_time = time()

with schemdraw.Drawing(file=f"batres.svg", show=False) as d:
    global u
    u = d.unit
    e.BatteryCell().left(2*u)
    e.Line().up()
    e.Resistor().right()
    e.Resistor().right()
    e.Line().down()

with schemdraw.Drawing(file=f"ex_tot_res.svg", show=False) as d:
    e.BatteryCell().left(2*u).label('10 V')
    e.Line().up()
    e.Resistor().right().label('2 Ω')
    e.Resistor().right().label('3 Ω')
    down_line = e.Line().down()
    e.CurrentLabelInline(ofst=0, direction='out').at(down_line).label('I')

with schemdraw.Drawing(file=f"ex_del.svg", show=False) as d:
    e.BatteryCell().left(3*u).label('10 V')
    e.Line().up()
    e.Resistor().right().label('20 Ω')
    e.Resistor().right().label('50 Ω')
    e.Resistor().right().label('30 Ω')
    down_line = e.Line().down()

with schemdraw.Drawing(file=f"kvl.svg", show=False) as d:
    e.BatteryCell().left().label('6 V')
    e.BatteryCell().left().label('6 V')
    e.Line().down()
    e.Resistor().right().label('$R_1$').label(('–', '10 V', '+'), loc='B')
    e.Resistor().right().label('$R_2$')
    e.Line().up()


print(f"Done in {time()-start_time} s")
