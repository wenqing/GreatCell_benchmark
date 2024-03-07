import xml.etree.cElementTree as ET

#from lxml import etree 
#import os
#import sys

def create_xml_file(file_name):
    # Create the root element
    root = ET.Element("OpenGeoSysProjectDiff", base_file=file_name + '.prj')

    # Add replace elements
    replace_elements = [
        ("/*/time_loop/processes/process/time_stepping/initial_dt/text()", "1e-3"),
        ("/*/time_loop/processes/process/time_stepping/minimum_dt/text()", "1e-3"),
        ("/*/parameters/parameter[name='E1']/value/text()", "26.85e9"),
        ("/*/parameters/parameter[name='nu1']/value/text()", "0.27"),
        ("/*/parameters/parameter[name='k']/value/text()", "2.58e-19"),
        ("/*/time_loop/output/prefix/text()", "GreatCell_3D_Greywacke")
    ]

    for msel, value in replace_elements:
        ET.SubElement(root, "replace", msel=msel).text = value
 
    # Create an ElementTree and write to the specified file
    tree = ET.ElementTree(root)
    ET.indent(tree, '    ')
    tree.write(file_name + '_Greywacke.xml', encoding="ISO-8859-1",
               xml_declaration=True)#, pretty_print=True)

if __name__ == "__main__":
    # Provide the desired file name as an argument
    projec_file_names = [
                     'great_cell_HM2_new_load_B',
                     'great_cell_HM2_new_load_C',
                     'great_cell_HM2_new_load_D',
                     'great_cell_HM2_new_load_E',
                     'great_cell_HM2_new_load_F',
                     ]
    for name in projec_file_names:
        create_xml_file(name)
        print(f"Patch for file '{name}.prj' has been generated successfully.")
