from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("app.html")


@app.route("/kerf_check", methods=["POST"])
def kerf_check():
    json = request.json
    stw = json["stw"]
    inc = json["inc"]
    gap = json["gap"]
    lp = json["lp"]
    tbone = json["tbone"]

    if abs(inc) < 0.01:
        return "刻み幅が小さすぎます。刻み幅は1/100mm単位までしか設定できません。", 500

    txt = generate_svg(stw, inc, gap, lp, tbone)

    return txt, 200, {"Content-Type": "image/svg+xml"}


def generate_svg(stw, inc, gap, lp, tbone):
    # GAP = 16
    MARGIN = 10
    PARTS_HEIGHT = 50
    KERF_HEIGHT = 20

    if inc < 0:
        # inc = inc * (-1)
        inc = -inc
        stw = stw - inc * (lp - 1)

    cw = (stw + inc * lp + gap) * lp + gap + MARGIN * 2
    ch = PARTS_HEIGHT + MARGIN * 2
    orign_x = MARGIN
    orign_y = MARGIN

    st1 = f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{cw}mm" height="{ch}mm" viewBox="0 0 {cw} {ch}">'
    ed1 = "</svg>"

    temp = f'<path stroke="red" stroke-width="0.1" fill="none" d="M{orign_x},{orign_y}'
    txt = ""

    x = orign_x
    y = orign_y
    kerf_width = stw

    y += PARTS_HEIGHT
    temp += f" V{y}"
    x += gap
    temp += f" H{x}"

    for i in range(lp):
        kerf_width = stw + inc * i
        # kerf_width=Math.round(kerf_width*100)/100
        kerf_width = round(kerf_width, 2)
        if len(str(kerf_width)) == 1:
            adjst = len(str(kerf_width)) - 1
        else:
            adjst = len(str(kerf_width)) - 2

        txt += f'<text x="{x - adjst}" y="25" font-size="3" fill="black">{kerf_width}</text>'

        y -= KERF_HEIGHT
        temp += f" V{y}"
        # Tボーンフィレット左側生成
        # t_bone = f" A 1 1 0 0 1 {x} {y-2} "
        t_bone = f" A {tbone / 2} {tbone / 2} 0 0 1 {x} {y - tbone}"
        temp += t_bone
        x += kerf_width
        temp += f" H{x}"
        # t_bone = f" A 1 1 0 0 1 {x} {y} "
        t_bone = f" A {tbone / 2} {tbone / 2} 0 0 1 {x} {y}"
        temp += t_bone
        y += KERF_HEIGHT
        temp += f" V{y}"
        x += gap
        temp += f" H{x}"

    y = y - PARTS_HEIGHT
    temp += f" V{y}"
    x = orign_x
    temp += f" H{x}"
    temp += '"/>'

    result = f"{st1}\n{temp}\n{txt}\n{ed1}"

    return result
