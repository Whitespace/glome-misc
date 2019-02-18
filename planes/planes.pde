float l = 30;
PShape pentagon, hexagon;
float phi =  (sqrt(5)+1)/2;

void setup() {
  size(1200, 800, P3D);
  noFill();
  stroke(0);

  pentagon = createShape();
  float angle = TWO_PI / 5;
  pentagon.beginShape();
  for (float a = 0; a < TWO_PI; a += angle) {
    float sx = 0 + cos(a) * l/2;
    float sy = 0 + sin(a) * l/2;
    pentagon.vertex(sx, sy);
  }
  pentagon.endShape(CLOSE);
  
  hexagon = createShape();
  angle = TWO_PI / 6;
  hexagon.beginShape();
  for (float a = 0; a < TWO_PI; a += angle) {
    float sx = 0 + cos(a) * l/2;
    float sy = 0 + sin(a) * l/2;
    hexagon.vertex(sx, sy);
  }
  hexagon.endShape(CLOSE);
}

void draw() {
  background(204);
  translate(width/2, height/2);
  rotateY(millis()/2000.0);
  //rotateX(30);
  //box(400);
  //translate(mouseX,mouseY);
  //shape(hexagon, 2*l, 2*l);
  //shape(pentagon);
  l=100.0;
PVector v;
float a;

pushMatrix();
  v = new PVector(l * 0   , l * 1   , l * phi);
  translate(v.x,v.y,v.z);
  a = PVector.angleBetween(v, new PVector(0, v.y, 0));
  rotateX(-a/2);
  shape(pentagon);
popMatrix();
stroke(#FF0000);
line(0,0,0,v.x,v.y,v.z);
stroke(#000000);

pushMatrix();
  v = new PVector(l * 0   , l * 1   , l * -phi);
  translate(v.x,v.y,v.z);
  a = PVector.angleBetween(v, new PVector(0, v.y, 0));
  rotateX(a/2);
  shape(pentagon);
popMatrix();
stroke(#FF0000);
line(0,0,0,v.x,v.y,v.z);
stroke(#000000);

pushMatrix();
  v = new PVector(l * 0   , l * -1  , l * phi);
  translate(v.x,v.y,v.z);
  a = PVector.angleBetween(v, new PVector(0, v.y, 0));
  rotateX(a/2);
  shape(pentagon);
popMatrix();
stroke(#FF0000);
line(0,0,0,v.x,v.y,v.z);
stroke(#000000);

pushMatrix();
  v = new PVector(l * 0   , l * -1  , l * -phi);
  translate(v.x,v.y,v.z);
  a = PVector.angleBetween(v, new PVector(0, v.y, 0));
  rotateX(-a/2);
  shape(pentagon);
popMatrix();
stroke(#FF0000);
line(0,0,0,v.x,v.y,v.z);
stroke(#000000);

pushMatrix();
  v = new PVector(l * 1   , l * phi , l * 0);
  translate(v.x,v.y,v.z);
  a = PVector.angleBetween(v, new PVector(0, v.y, 0)) / 2;
  rotateX(-a);
  println(degrees(a));
  a = PVector.angleBetween(v, new PVector(v.x, 0, 0)) / 2;
  rotateY(a);
  shape(pentagon);
popMatrix();
stroke(#FF0000);
line(0,0,0,v.x,v.y,v.z);
stroke(#000000);

pushMatrix();
v = new PVector(l * 1   , l * -phi, l * 0);
popMatrix();

pushMatrix();
v = new PVector(l * -1  , l * phi , l * 0);
popMatrix();

pushMatrix();
v = new PVector(l * -1  , l * -phi, l * 0);
popMatrix();

pushMatrix();
v = new PVector(l * phi , l * 0   , l * 1);
popMatrix();

pushMatrix();
v = new PVector(l * -phi, l * 0   , l * 1);
popMatrix();

pushMatrix();
v = new PVector(l * phi , l * 0   , l * -1);
popMatrix();

pushMatrix();
  v = new PVector(l * -phi, l * 0   , l * -1);
  translate(v.x,v.y,v.z);
  a = PVector.angleBetween(v, new PVector(0, 0, v.z));
  rotateY(-a/2);
  shape(pentagon);
popMatrix();
stroke(#FF0000);
line(0,0,0,v.x,v.y,v.z);
stroke(#000000);

}
