<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE OGS-GML-DOM>
<OpenGeoSysGLI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ogs="http://www.opengeosys.org">
 <name>G3_geometry</name>
 <points>
  <point id="0" x="-0.097"   y="0.0" z="0.0" />
  <point id="1" x="0.097" y="0.0" z="0.0"/>
  <point id="2" x="0.097" y="0.0" z="0.2"/>
  <point id="3" x="-0.097"  y="0.0" z="0.2"/>
  <point id="4" x="0.04" y="0.0" z="0.1"/>
  <point id="5" x="0.04" y="0.0" z="0.2"/>
  <point id="6" x="0.0" y="0.0" z="0.1"/>
  <point id="7" x="0.0" y="0.0" z="0.2"/>
 </points>
 <polylines>
    <polyline name="fracture_left" id="0">
       <pnt>0</pnt>
       <pnt>3</pnt>
    </polyline>
    <polyline name="fracture_right" id="1">
       <pnt>1</pnt>
       <pnt>2</pnt>
   </polyline>
   <polyline name="fracture_bottom" id="2">
       <pnt>0</pnt>
       <pnt>1</pnt>
   </polyline>
    <polyline name="fracture_top" id="3">
       <pnt>2</pnt>
       <pnt>3</pnt>
   </polyline>      
    <polyline name="injection_bore_hole" id="0">
       <pnt>6</pnt>
       <pnt>7</pnt>
    </polyline>
    <polyline name="pumping_bore_hole" id="0">
       <pnt>4</pnt>
       <pnt>5</pnt>
    </polyline>
 </polylines>
</OpenGeoSysGLI>
