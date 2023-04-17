# reconfiguration

**SOLVED**

> As Pandora set out on her quest to find the ancient alien relic, she knew that the journey would be treacherous. 
> The desert was vast and unforgiving, and the harsh conditions would put her cyborg body to the test. 
> Pandora started by collecting data about the temperature and humidity levels in the desert. 
> She used a scatter plot in an Orange Workspace file to visualize this data and identified the areas where the temperature was highest and the humidity was lowest. 
> Using this information, she reconfigured her sensors to better withstand the extreme heat and conserve water. 
> But, a second look at the data revealed something otherwordly, it seems that the relic's presence beneath the surface has scarred the land in a very peculiar way, can you see it?

ows file? looks like xml config

```xml
<?xml version='1.0' encoding='utf-8'?>
<scheme version="2.0" title="Visualization of Data Subsets" description="Some visualization widgets, like Scatter Plot and several data project widgets, can expose the data instances in the data subset. In this workflow, Scatter Plot visualize the data from the input data file, but also marks the data points that have been selected in the Data Table (selected rows).&#10;&#10;Again, this workflow works best if both Scatter Plot and Data Table are open.">
	<nodes>
		<node id="0" name="Scatter Plot" qualified_name="Orange.widgets.visualize.owscatterplot.OWScatterPlot" project_name="Orange3" version="" title="Scatter Plot" position="(341.0, 165.0)" />
		<node id="1" name="File" qualified_name="Orange.widgets.data.owfile.OWFile" project_name="Orange3" version="" title="File" position="(124.0, 165.0)" />
	</nodes>
	<links />
	<annotations />
	<thumbnail />
	<node_properties>
		<properties node_id="0" format="pickle">
<!-- ... -->
```

https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/visualize/scatterplot.html

https://orangedatamining.com/download/#linux

```sh
pip3 install PyQt5 PyQtWebEngine
pip3 install orange3

python3 -m Orange.canvas
```

Opened csv in file node, connected it to plot, opened plot

`HTB{sc4tter_pl0ts_4_th3_w1n}`