
function setup() {
  x = y = 100;
  // put setup code here
  createCanvas(700, 600);
}

function draw() {
  background(200);
  dx = mouseX - x;
  dy = mouseY - y;
  angle1 = atan2(dy, dx);
  x = mouseX - (cos(angle1) * length)
  y = mouseY - (sin(angle1) * length)

  rect(x, y, 30, 30);

}
