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

<div id="xlfvqawand" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#xlfvqawand table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }
&#10;#xlfvqawand thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xlfvqawand p { margin: 0; padding: 0; }
 #xlfvqawand .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xlfvqawand .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xlfvqawand .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xlfvqawand .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xlfvqawand .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xlfvqawand .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xlfvqawand .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xlfvqawand .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xlfvqawand .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xlfvqawand .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xlfvqawand .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xlfvqawand .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xlfvqawand .gt_spanner_row { border-bottom-style: hidden; }
 #xlfvqawand .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xlfvqawand .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xlfvqawand .gt_from_md> :first-child { margin-top: 0; }
 #xlfvqawand .gt_from_md> :last-child { margin-bottom: 0; }
 #xlfvqawand .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xlfvqawand .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xlfvqawand .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xlfvqawand .gt_row_group_first td { border-top-width: 2px; }
 #xlfvqawand .gt_row_group_first th { border-top-width: 2px; }
 #xlfvqawand .gt_striped { background-color: rgba(128,128,128,0.05); }
 #xlfvqawand .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xlfvqawand .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xlfvqawand .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xlfvqawand .gt_left { text-align: left; }
 #xlfvqawand .gt_center { text-align: center; }
 #xlfvqawand .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xlfvqawand .gt_font_normal { font-weight: normal; }
 #xlfvqawand .gt_font_bold { font-weight: bold; }
 #xlfvqawand .gt_font_italic { font-style: italic; }
 #xlfvqawand .gt_super { font-size: 65%; }
 #xlfvqawand .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xlfvqawand .gt_asterisk { font-size: 100%; vertical-align: 0; }
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

### Result
