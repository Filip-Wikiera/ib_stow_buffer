from .models import P1, P2, P3, P4, Trans, TSO, closest_count
from datetime import datetime

class TimePoint_Buffer():
    def __init__(self, timepoint):
        self.buffer = []
        self.time = timepoint.strftime("%H:%M")
        self.buffer.append(closest_count(P1, timepoint))
        self.buffer.append(closest_count(P2, timepoint))
        self.buffer.append(closest_count(P3, timepoint))
        self.buffer.append(closest_count(P4, timepoint))
        self.buffer.append(closest_count(Trans, timepoint))

    def trans_nyr(self):
        table = "<table class ='nyr'>"
        table += f"<tr><td>NYR&nbspTSI</td><td>{self.buffer[4].NYR}</td>"
        table += "<table>"

        return table


    def __str__(self):
        ap = 0
        but = 0
        hl = 0
        nc = 0
        trans = 0
        damage = 0
        konsola = 0
        ps_cret = 0
        hang = 0

        table = f"<table><thead><tr><th>{self.time}</th><th>AP</th><th>BUTY</th><th>H-L</th><th>N-C</th><th>TRANS</th><th>DAMAGE</th><th>KONSOLA</th><th>PS_CRET</th><th>HANGERS</th><th>TOTAL</th><th>Time</th>"
        for floor in self.buffer:

            time = floor.time_stamp.strftime("%H:%M")
            if floor.name != "Trans":
                table += f"<tr><td>{floor.name}</td><td>{floor.app_total()}</td><td>{floor.buty_total()}</td><td>{floor.hl_total()}</td><td>{floor.ns_total()}</td><td>{floor.TRANS}</td><td>{floor.DAMAGE}</td><td>{floor.KONSOLA}</td><td>{floor.PS_CRET}</td><td>{floor.HANGERS}</td><td>{floor.total()}</td><td>{time}</td>"
                ap += floor.app_total()
                but += floor.buty_total()
                hl += floor.hl_total()
                nc += floor.ns_total()
                trans += floor.TRANS
                damage += floor.DAMAGE
                konsola += floor.KONSOLA
                ps_cret += floor.PS_CRET
                hang += floor.HANGERS
            else:
                table += f"<tr><td>{floor.name}</td><td>-</td><td>-</td><td>-</td><td>-</td><td>{floor.TRANS}</td><td>{floor.TRANS_DMG}</td><td>-</td><td>-</td><td>-</td><td>{floor.total()}</td><td>{time}</td>"
                trans += floor.TRANS + floor.TRANS_DMG

        total = ap + but + hl + nc + trans + damage + konsola + ps_cret + hang
        table += f"<tr><td>Total</td><td>{ap}</td><td>{but}</td><td>{hl}</td><td>{nc}</td><td>{trans}</td><td>{damage}</td><td>{konsola}</td><td>{ps_cret}</td><td>{hang}</td><td>{total}</td><td>-</td>"


        table += "</table>"
        return table