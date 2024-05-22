import xml.etree.cElementTree as ET

def create_xml_file(file_name):
    # Create the root element
    root = ET.Element("OpenGeoSysProjectDiff", base_file=file_name + '.prj')

    # Add replace elements
    replace_elements = [
        ("/*/meshes/mesh[1]/text()", "3D_fullFracture.vtu"),
        ("/*/time_loop/processes/process/convergence_criterion/type/text()",
          "PerComponentDeltaX"),
        ("/*/time_loop/processes/process/convergence_criterion/abstols/text()",
          "1.0e-10 1e-9 1e-9 1e-10 1e-10 1e-10 1e-10"),
        ("/*/time_loop/processes/process/time_stepping/t_end/text()", "300"),
        ("/*/time_loop/processes/process/time_stepping/initial_dt/text()", "1e-5"),
        ("/*/time_loop/processes/process/time_stepping/minimum_dt/text()", "1e-5"),
        ("/*/time_loop/processes/process/time_stepping/multiplier/text()", "4.5 3.0 2 0.7 0.5"),
        ("/*/time_loop/output/prefix/text()", "GreatCell_3D_full_fracture_Greywacke"),
        ("/*/parameters/parameter[name='E1']/value/text()", "26.85e9"),
        ("/*/parameters/parameter[name='nu1']/value/text()", "0.27"),
        ("/*/parameters/parameter[name='k']/value/text()", "2.58e-19"),
        ("/*/parameters/parameter[name='Kn']/value/text()", "100.0e+9"),
        ("/*/parameters/parameter[name='Ks']/value/text()", "100.0e+9"),
        ("/*/parameters/parameter[name='aperture0']/value/text()", "1.0e-5"),
        ("/*/parameters/parameter[name='p_injection_rate']/value/text()", "5.0e-6"),
        ("/*/parameters/parameter[name='p_down_stream']/value/text()", "1.0e+5"),
        ("/*/parameters/parameter[name='p0']/value/text()", "1.0e+5"),
        ("/*/process_variables/process_variable[1]/boundary_conditions/boundary_condition[1]/mesh/text()",
           "G3_geometry_pumping_bore_hole"),
        ("/*/process_variables/process_variable[1]/boundary_conditions/boundary_condition[2]/mesh/text()",
           "G3_geometry_injection_bore_hole")
    ]

    for msel, value in replace_elements:
        ET.SubElement(root, "replace", msel=msel).text = value

    ## Add new mesh
    meshes = ET.SubElement(root, "add", sel="/*/meshes")
    mesh = ET.SubElement(meshes, "mesh")
    mesh.text = "G3_geometry_injection_bore_hole.vtu"
    mesh = ET.SubElement(meshes, "mesh")
    mesh.text = "G3_geometry_pumping_bore_hole.vtu"
 
    ## Remove tag abstol
    #ET.SubElement(root, "remove",
    #  sel="/*/time_loop/processes/process/convergence_criterion/abstols")

    ## Add new tag reltol
    convergence_criterion = ET.SubElement(root, "add", sel="/*/time_loop/processes/process/convergence_criterion")
    reltol = ET.SubElement(convergence_criterion, "reltols")
    #reltol.text = "1e-10 5e-10 5e-10 5e-10 1e-10 5e-10 2e-10"
    reltol.text = "1e-6 5e-5 7e-5 5e-5 1e-3 5e-5 3e-3"

    # Create an ElementTree and write to the specified file
    tree = ET.ElementTree(root)
    ET.indent(tree, '    ')
    tree.write(file_name + '_full_frature_greywacke_high_kn.xml', encoding="ISO-8859-1",
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
