float[][] vertices = {
  { 1121.2, 887.2, 752.9 }, 
  { 1497.7, 745.3, 531.1 }, 
  { 1868.2, 608.3, 763.0 }, 
  { 1864.1, 610.8, 1221.8 }, 
  { 1489.4, 750.5, 1446.3 }, 
  { 1120.2, 887.1, 1213.2 }, 
  { 744.8, 749.6, 1437.6 }, 
  { 375.9, 606.4, 1205.5 }, 
  { 380.9, 605.0, 747.8 }, 
  { 752.6, 746.0, 520.7 }, 
  { 901.6, 517.7, 148.7 }, 
  { 1361.1, 517.0, 156.9 }, 
  { 1588.9, 149.4, 7.8 }, 
  { 1961.4, 9.0, 235.1 }, 
  { 2100.8, 237.3, 607.4 }, 
  { 2235.5, 4.0, 995.5 }, 
  { 2091.0, 232.3, 1361.7 }, 
  { 1947.2, 0.0, 1736.1 }, 
  { 1574.4, 142.4, 1962.4 }, 
  { 1348.1, 513.1, 1817.7 }, 
  { 888.2, 513.9, 1817.9 }, 
  { 650.4, 144.3, 1952.1 }, 
  { 281.8, 4.5, 1718.1 }, 
  { 140.4, 233.3, 1345.0 }, 
  { 0.0, 3.6, 975.3 }, 
  { 145.6, 232.3, 604.8 }, 
  { 290.7, 9.9, 221.9 }, 
  { 666.0, 151.0, 0.0 }, 
};

void setup() {
  size(1200, 800, P3D);
  noFill();
}

void draw() {
  background(255);
  camera(width*3.0, height*3.0, (height*3.0) / tan(PI*30.0 / 180.0), mouseX, mouseY, 0, 0, 1, 0);
  rotateY(millis()/2000.0);
  rotateX(millis()/4000.0);
  rotateZ(millis()/8000.0);
  
  ldraw(vertices[0], vertices[1]);
  ldraw(vertices[1], vertices[2]);
  ldraw(vertices[2], vertices[3]);
  ldraw(vertices[3], vertices[4]);
  ldraw(vertices[4], vertices[5]);
  ldraw(vertices[5], vertices[0]);

  ldraw(vertices[5], vertices[6]);
  ldraw(vertices[6], vertices[7]);
  ldraw(vertices[7], vertices[8]);
  ldraw(vertices[8], vertices[9]);
  ldraw(vertices[9], vertices[0]);

  ldraw(vertices[9], vertices[10]);
  ldraw(vertices[10], vertices[11]);
  ldraw(vertices[11], vertices[1]);

  ldraw(vertices[11], vertices[12]);
  ldraw(vertices[12], vertices[13]);
  ldraw(vertices[13], vertices[14]);
  ldraw(vertices[14], vertices[2]);

  ldraw(vertices[14], vertices[15]);
  ldraw(vertices[15], vertices[16]);
  ldraw(vertices[16], vertices[3]);

  ldraw(vertices[16], vertices[17]);
  ldraw(vertices[17], vertices[18]);
  ldraw(vertices[18], vertices[19]);
  ldraw(vertices[19], vertices[4]);

  ldraw(vertices[19], vertices[20]);
  ldraw(vertices[20], vertices[6]);

  ldraw(vertices[20], vertices[21]);
  ldraw(vertices[21], vertices[22]);
  ldraw(vertices[22], vertices[23]);
  ldraw(vertices[23], vertices[7]);

  ldraw(vertices[23], vertices[24]);
  ldraw(vertices[24], vertices[25]);
  ldraw(vertices[25], vertices[8]);

  ldraw(vertices[25], vertices[26]);
  ldraw(vertices[26], vertices[27]);
  ldraw(vertices[27], vertices[10]);
}

void ldraw(float[] a, float[] b) {
  line(a[0], a[1], a[2], b[0], b[1], b[2]);
}
