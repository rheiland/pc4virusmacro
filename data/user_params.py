 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='viral_replication_rate', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'tan'

        self.viral_replication_rate = FloatText(
          value=0.4167,
          step=0.1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='min_virion_count', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'lightgreen'

        self.min_virion_count = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='burst_virion_count', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'tan'

        self.burst_virion_count = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name4 = Button(description='viral_internalization_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'lightgreen'

        self.viral_internalization_rate = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name5 = Button(description='viral_diffusion_coefficient', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'tan'

        self.viral_diffusion_coefficient = FloatText(
          value=1e3,
          step=100,
          style=style, layout=widget_layout)

        param_name6 = Button(description='number_of_infected_cells', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'lightgreen'

        self.number_of_infected_cells = IntText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='number_of_macrophages', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'tan'

        self.number_of_macrophages = IntText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='min_virion_detection_threshold', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'lightgreen'

        self.min_virion_detection_threshold = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name9 = Button(description='virus_digestion_rate', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'tan'

        self.virus_digestion_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name10 = Button(description='macrophage_persistence_time', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'lightgreen'

        self.macrophage_persistence_time = FloatText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='macrophage_migration_speed', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'tan'

        self.macrophage_migration_speed = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='macrophage_migration_bias', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'lightgreen'

        self.macrophage_migration_bias = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name13 = Button(description='macrophage_relative_adhesion', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'tan'

        self.macrophage_relative_adhesion = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        units_button1 = Button(description='viral particles/min', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'tan'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'lightgreen'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'tan'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'lightgreen'
        units_button9 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'tan'
        units_button10 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'lightgreen'
        units_button11 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'tan'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'lightgreen'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'tan'

        desc_button2 = Button(description='rate at which infected cells create new viral particles', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='minimum number of virions to start replication', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='max virion load, where infected cells lyse to release viral particles', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='internalization rate for viral particles', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='diffusion coefficient for viral particles', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='initial number of infected cells', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='initial number of macrophages', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='minimal viral load for microphages to detect as infected', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='rate that macrophages digest internalized viral particles', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'

        row2 = [param_name1, self.viral_replication_rate, units_button1, desc_button2] 
        row3 = [param_name2, self.min_virion_count, units_button2, desc_button3] 
        row4 = [param_name3, self.burst_virion_count, units_button3, desc_button4] 
        row5 = [param_name4, self.viral_internalization_rate, units_button4, desc_button5] 
        row6 = [param_name5, self.viral_diffusion_coefficient, units_button5, desc_button6] 
        row7 = [param_name6, self.number_of_infected_cells, units_button6, desc_button7] 
        row8 = [param_name7, self.number_of_macrophages, units_button7, desc_button8] 
        row9 = [param_name8, self.min_virion_detection_threshold, units_button8, desc_button9] 
        row10 = [param_name9, self.virus_digestion_rate, units_button9, desc_button10] 
        row11 = [param_name10, self.macrophage_persistence_time, units_button10, desc_button11] 
        row12 = [param_name11, self.macrophage_migration_speed, units_button11, desc_button12] 
        row13 = [param_name12, self.macrophage_migration_bias, units_button12, desc_button13] 
        row14 = [param_name13, self.macrophage_relative_adhesion, units_button13, desc_button14] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)

        self.tab = VBox([
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.viral_replication_rate.value = float(uep.find('.//viral_replication_rate').text)
        self.min_virion_count.value = float(uep.find('.//min_virion_count').text)
        self.burst_virion_count.value = float(uep.find('.//burst_virion_count').text)
        self.viral_internalization_rate.value = float(uep.find('.//viral_internalization_rate').text)
        self.viral_diffusion_coefficient.value = float(uep.find('.//viral_diffusion_coefficient').text)
        self.number_of_infected_cells.value = int(uep.find('.//number_of_infected_cells').text)
        self.number_of_macrophages.value = int(uep.find('.//number_of_macrophages').text)
        self.min_virion_detection_threshold.value = float(uep.find('.//min_virion_detection_threshold').text)
        self.virus_digestion_rate.value = float(uep.find('.//virus_digestion_rate').text)
        self.macrophage_persistence_time.value = float(uep.find('.//macrophage_persistence_time').text)
        self.macrophage_migration_speed.value = float(uep.find('.//macrophage_migration_speed').text)
        self.macrophage_migration_bias.value = float(uep.find('.//macrophage_migration_bias').text)
        self.macrophage_relative_adhesion.value = float(uep.find('.//macrophage_relative_adhesion').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//viral_replication_rate').text = str(self.viral_replication_rate.value)
        uep.find('.//min_virion_count').text = str(self.min_virion_count.value)
        uep.find('.//burst_virion_count').text = str(self.burst_virion_count.value)
        uep.find('.//viral_internalization_rate').text = str(self.viral_internalization_rate.value)
        uep.find('.//viral_diffusion_coefficient').text = str(self.viral_diffusion_coefficient.value)
        uep.find('.//number_of_infected_cells').text = str(self.number_of_infected_cells.value)
        uep.find('.//number_of_macrophages').text = str(self.number_of_macrophages.value)
        uep.find('.//min_virion_detection_threshold').text = str(self.min_virion_detection_threshold.value)
        uep.find('.//virus_digestion_rate').text = str(self.virus_digestion_rate.value)
        uep.find('.//macrophage_persistence_time').text = str(self.macrophage_persistence_time.value)
        uep.find('.//macrophage_migration_speed').text = str(self.macrophage_migration_speed.value)
        uep.find('.//macrophage_migration_bias').text = str(self.macrophage_migration_bias.value)
        uep.find('.//macrophage_relative_adhesion').text = str(self.macrophage_relative_adhesion.value)
