##A python script to ID accession numbers and format tombstone data for the BAMPFA art collection wall

###The wall 
The art collection wall is a set of touchscreen monitors that display a preselected set of important images from the BAMPFA art collection. The images are formatted such that there is whitespace below the actual image, and the "tombstone data" is displayed in the format below:

>*Westward the course of empire takes its way (Bishop Berkeley)*

>*Weir, John F.*

>*1873*

>*oil on canvas*

>*72 3/8 x 51 1/4 in.*

###Data sources
Data is exported from the BAMPFA art collection database as a CSV. From this CSV, only the relevant fields \(columns\) are kept.

A list of the selected images is produced, from the results of that 'find' command \(e.g.: **./bampfa\_1967-40\_1\_1.tif**\) a list of accession numbers \(e.g.: **1967.40**\)is generated that are then used as primary keys to search the full database CSV and generate a second CSV of only the relevant artworks. 

From the match CSV, a list of the concatenated fields separated by carriage returns is appended to the corresponding row, which an intern can then copy and paste into the Photoshop document she creates.

Now to automate the psd creation and formatting...