# November Energy Report


``` python
import pandas as pd
from great_tables import GT, md
from EnergyConsumption import EnergyConsumption
```

## Calculate yearly energy consumption

``` python
energy_consumption = EnergyConsumption()
```

### VREG API

Based on the default inputs, the VREG estimates a yearly consumption as
indicated below.

``` python
df_VREG = pd.DataFrame(data = {
  'Day': [energy_consumption.default_VREG['Day']],
  'Night': [energy_consumption.default_VREG['Night']],
  'Gas': [energy_consumption.default_VREG['Gas']]})

(
    GT(df_VREG)
    .tab_header(
        title=md("Estimated yearly consumption based on VREG"),
        subtitle=md("*In kWh*"),
    )
    .cols_label(
        Day="Electricity Day",
        Night="Electricity Night",
        Gas="Gas",
    )
    .cols_align("center")
    .fmt_integer(sep_mark='.')
)
```

<div id="nrqzbitmbp" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#nrqzbitmbp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }
&#10;#nrqzbitmbp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nrqzbitmbp p { margin: 0; padding: 0; }
 #nrqzbitmbp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nrqzbitmbp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nrqzbitmbp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nrqzbitmbp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nrqzbitmbp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nrqzbitmbp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nrqzbitmbp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nrqzbitmbp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nrqzbitmbp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nrqzbitmbp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nrqzbitmbp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nrqzbitmbp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nrqzbitmbp .gt_spanner_row { border-bottom-style: hidden; }
 #nrqzbitmbp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nrqzbitmbp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nrqzbitmbp .gt_from_md> :first-child { margin-top: 0; }
 #nrqzbitmbp .gt_from_md> :last-child { margin-bottom: 0; }
 #nrqzbitmbp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nrqzbitmbp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nrqzbitmbp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nrqzbitmbp .gt_row_group_first td { border-top-width: 2px; }
 #nrqzbitmbp .gt_row_group_first th { border-top-width: 2px; }
 #nrqzbitmbp .gt_striped { background-color: rgba(128,128,128,0.05); }
 #nrqzbitmbp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nrqzbitmbp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nrqzbitmbp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nrqzbitmbp .gt_left { text-align: left; }
 #nrqzbitmbp .gt_center { text-align: center; }
 #nrqzbitmbp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nrqzbitmbp .gt_font_normal { font-weight: normal; }
 #nrqzbitmbp .gt_font_bold { font-weight: bold; }
 #nrqzbitmbp .gt_font_italic { font-style: italic; }
 #nrqzbitmbp .gt_super { font-size: 65%; }
 #nrqzbitmbp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nrqzbitmbp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 &#10;</style>

| Estimated yearly consumption based on VREG |                   |        |
|--------------------------------------------|-------------------|--------|
| *In kWh*                                   |                   |        |
| Electricity Day                            | Electricity Night | Gas    |
| 1.195                                      | 1.674             | 14.715 |

&#10;</div>
        &#10;
### Energy consumption pattern - extrapolated

In case no full history of the energy consumption is available, data
will be extrapolated based on the below pattern. This is the actual
consumption of a house in Belgium.

``` python
energy_consumption.plot_default_consumption_pattern('Gas')
energy_consumption.plot_default_consumption_pattern('Day')
energy_consumption.plot_default_consumption_pattern('Night')
```

![](november_energy_consumption_files/figure-commonmark/cell-5-output-1.png)

![](november_energy_consumption_files/figure-commonmark/cell-5-output-2.png)

![](november_energy_consumption_files/figure-commonmark/cell-5-output-3.png)

### Energy consumption pattern - actuals

The following energy consumption was inputted by the user.

``` python
energy_consumption.plot_actual_consumption_data('Gas')
energy_consumption.plot_actual_consumption_data('Day')
energy_consumption.plot_actual_consumption_data('Night')
```

![](november_energy_consumption_files/figure-commonmark/cell-6-output-1.png)

![](november_energy_consumption_files/figure-commonmark/cell-6-output-2.png)

![](november_energy_consumption_files/figure-commonmark/cell-6-output-3.png)

Extracting the data from the last 12 months, we can calculate the yearly
consumption.

``` python
# Calculate yearly consumption based on actuals
yearly_consumption = energy_consumption.get_actual_consumption_data_last_12_months()


df_consumption = pd.DataFrame(data = {
  'Day': [yearly_consumption['Day']],
  'Night': [yearly_consumption['Night']],
  'Gas': [yearly_consumption['Gas']]})

(
    GT(df_consumption)
    .tab_header(
        title=md("Actual yearly consumption based on user input"),
        subtitle=md("*In kWh*"),
    )
    .cols_label(
        Day="Electricity Day",
        Night="Electricity Night",
        Gas="Gas",
    )
    .cols_align("center")
    .fmt_integer(sep_mark='.')
)
```

<div id="kjeshdqcos" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#kjeshdqcos table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }
&#10;#kjeshdqcos thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kjeshdqcos p { margin: 0; padding: 0; }
 #kjeshdqcos .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kjeshdqcos .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kjeshdqcos .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kjeshdqcos .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kjeshdqcos .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kjeshdqcos .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kjeshdqcos .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kjeshdqcos .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kjeshdqcos .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kjeshdqcos .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kjeshdqcos .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kjeshdqcos .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kjeshdqcos .gt_spanner_row { border-bottom-style: hidden; }
 #kjeshdqcos .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kjeshdqcos .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kjeshdqcos .gt_from_md> :first-child { margin-top: 0; }
 #kjeshdqcos .gt_from_md> :last-child { margin-bottom: 0; }
 #kjeshdqcos .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kjeshdqcos .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kjeshdqcos .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kjeshdqcos .gt_row_group_first td { border-top-width: 2px; }
 #kjeshdqcos .gt_row_group_first th { border-top-width: 2px; }
 #kjeshdqcos .gt_striped { background-color: rgba(128,128,128,0.05); }
 #kjeshdqcos .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kjeshdqcos .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kjeshdqcos .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kjeshdqcos .gt_left { text-align: left; }
 #kjeshdqcos .gt_center { text-align: center; }
 #kjeshdqcos .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kjeshdqcos .gt_font_normal { font-weight: normal; }
 #kjeshdqcos .gt_font_bold { font-weight: bold; }
 #kjeshdqcos .gt_font_italic { font-style: italic; }
 #kjeshdqcos .gt_super { font-size: 65%; }
 #kjeshdqcos .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kjeshdqcos .gt_asterisk { font-size: 100%; vertical-align: 0; }
 &#10;</style>

| Actual yearly consumption based on user input |                   |       |
|-----------------------------------------------|-------------------|-------|
| *In kWh*                                      |                   |       |
| Electricity Day                               | Electricity Night | Gas   |
| 1.035                                         | 738               | 8.037 |

&#10;</div>
        &#10;
### Result
