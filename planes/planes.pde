PShape hexagon, pentagon;

void setup() {
  size(1200, 800, P3D);
  noFill();
  stroke(0);

  int l = 30;
  float apotheum = l/2*sqrt(3);
  hexagon = createShape();
  hexagon.beginShape();
    //hexagon.vertex(0, 0); // center point
    hexagon.vertex(-l/2, -apotheum); // 0
    hexagon.vertex(l/2, -apotheum); // 1
    hexagon.vertex(l, 0); // 2
    hexagon.vertex(l/2, apotheum); // 3
    hexagon.vertex(-l/2, apotheum); // 4
    hexagon.vertex(-l, 0); //
  hexagon.endShape(CLOSE);
  
  pentagon = createShape();
  pentagon.beginShape();
    pentagon.vertex(0,0);
  pentagon.endShape(CLOSE);
}

void draw() {
  background(204);
  //translate(width/2, height/2);
  //rotateY(millis()/2000.0);
  //box(400);
  translate(mouseX,mouseY);
  shape(hexagon);
  shape(pentagon);
}
