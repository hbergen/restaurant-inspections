# Restaurant Inspections in King County, Washington (USA)

The purpose of this project is to explore public restaurant inspection records.

### About the data

The King County Public Health Department provides an API to retrieve the restaurant inspection data in XML format.

API documentation can be found here:
http://www.kingcounty.gov/healthservices/health/ehs/foodsafety/inspections/data.aspx

The XML data contains 'Business' elements, within which geographic, inspection, and violation (if applicable) details are nested for each business.

Below is some raw data in XML format for 1 sample business:

```xml
<Business>
<Name>10 MERCER RESTAURANT</Name>
<Program_Identifier>10 MERCER RESTAURANT</Program_Identifier>
<Description>Seating 13-50 - Risk Category III</Description>
<Address>10 MERCER ST</Address>
<City>Seattle</City>
<Zip_Code>98109</Zip_Code>
<Phone/>
<Longitude>-122.3561914741</Longitude>
<Latitude>47.6250635431</Latitude>
<Inspection>
<Inspection_Date>07/07/2016</Inspection_Date>
<Inspection_Business_Name>10 MERCER RESTAURANT</Inspection_Business_Name>
<Inspection_Type>Consultation/Education - Field</Inspection_Type>
<Inspection_Score>N/A</Inspection_Score>
<Inspection_Result>Complete</Inspection_Result>
<Inspection_Closed_Business>N</Inspection_Closed_Business>
<Violation>
<Violation_Type/>
<Violation_Descr/>
<Violation_Points/>
</Violation>
</Inspection>
<Inspection>
<Inspection_Date>02/24/2016</Inspection_Date>
<Inspection_Business_Name>10 MERCER RESTAURANT</Inspection_Business_Name>
<Inspection_Type>Routine Inspection/Field Review</Inspection_Type>
<Inspection_Score>15</Inspection_Score>
<Inspection_Result>Unsatisfactory</Inspection_Result>
<Inspection_Closed_Business>N</Inspection_Closed_Business>
<Violation>
<Violation_Type>RED</Violation_Type>
<Violation_Descr>2500 - Toxic substances properly identified,...</Violation_Descr>
<Violation_Points>10</Violation_Points>
</Violation>
<Violation>
<Violation_Type>BLUE</Violation_Type>
<Violation_Descr>
4200 - Food-contact surfaces maintained, clean, sanitized
</Violation_Descr>
<Violation_Points>5</Violation_Points>
</Violation>
</Inspection>
</Business>
```