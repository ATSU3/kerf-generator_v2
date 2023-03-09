# Kerf Check Parts Generator

## Example

![img1](./static/img/img_1.jpg)

- You can create a kerf checker by entering five parameters ((start-width),(pitch), (gap),(number-of-kerfs), (blade-diameter)).

- By clicking on the "createSVG" button, you can display the image on the screen.
Click on the image to download it.


![img2](./static/img/img_2.jpg)

- By setting "blade diameter" to 0, the "T-bone fillet" can be eliminated on the laser cutting machine, which can be used for kerf checking on the laser cutter.

![img3](./static/img/img_3.jpg)

- (pitch) can only be set to 1/100 mm increments. 


## Local setting

### pip install
```bash
pip install -r requirements.txt
```

### Start Server
```bash
FLASK_APP=index.py flask run
```